"""Prepare regional inputs, optionally solve, or resume a committed step.

No model is solved unless --solve is supplied. Paths/configuration remain in
the existing ENTICE_CONFIG/data_root mechanism.
"""
import argparse
import json
from pathlib import Path

from entice_inventory.core.paths import local_config, project_data_root, data_path
from entice_inventory.core.geography import Geography, configured_geography
from entice_inventory.core.disaggregation import prepare_inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    existing = parser.add_mutually_exclusive_group()
    parser.add_argument('--inventories', type=Path)
    parser.add_argument('--mapping', type=Path, help='Two-column regional partition; overrides geography in config.')
    parser.add_argument('--output-references', type=Path, help='Original MARIO inventories with complete native output observations.')
    parser.add_argument('--steps', type=Path, help='JSON object: named groups in execution order; omit for oneshot.')
    parser.add_argument('--output', type=Path, help='New preparation directory, or checkpoint root when resuming.')
    parser.add_argument('--intermediate-steps', action='store_true', help='Generate an editable initial group when no --steps JSON is supplied.')
    existing.add_argument('--prepared', type=Path, help='Solve a previously prepared directory after editing its workbook.')
    parser.add_argument('--solve', action='store_true')
    parser.add_argument('--solver', default='CLARABEL')
    existing.add_argument('--resume', type=Path, help='Committed MARIO step directory.')
    parser.add_argument('--workbook', type=Path, help='Edited remaining or full source workbook when resuming.')
    args = parser.parse_args()
    if (args.resume or args.prepared) and any((args.mapping, args.inventories, args.steps,
                                              args.output_references, args.intermediate_steps)):
        parser.error('Existing runs retain their geography; edit the workbook for group changes, or prepare a new run.')
    if args.resume:
        if not args.solve:
            parser.error('--resume requires --solve')
        if not args.output:
            parser.error('--resume requires --output for the checkpoint root')
        from mario.ops.add_sector_steps import load_checkpoint
        db = load_checkpoint(args.resume)
        workbook = args.workbook or args.resume / 'remaining_add_sectors.xlsx'
        db.add_sectors(workbook, split=True, intermediate_steps=True, save_intermediates=args.output,
                       solver=args.solver)
        return
    if args.prepared:
        if not args.solve:
            parser.error('--prepared requires --solve')
        destination = args.prepared
    elif args.workbook:
        parser.error('--workbook requires --resume or --prepared')
    elif not args.output:
        parser.error('--output is required for input preparation')
    config = local_config().get('disaggregation', {})
    source = args.inventories
    if source is None and not args.prepared:
        if not config.get('inventories'):
            parser.error('Supply --inventories or disaggregation.inventories in the local config.')
        source = Path(config['inventories']).expanduser()
        if not source.is_absolute():
            source = project_data_root(required=True) / source
    if not args.prepared:
        geography = Geography.read(args.mapping) if args.mapping else configured_geography()
        steps = json.loads(args.steps.read_text()) if args.steps else config.get('steps')
        destination = prepare_inputs(source, args.output, geography=geography, steps=steps,
                                     intermediate_steps=args.intermediate_steps,
                                     output_reference_dir=args.output_references or data_path('mario_inventories'))
        print(f'Prepared inputs: {destination}')
    if args.solve:
        import mario
        db = mario.parse_from_parquet(str(destination / 'baseline' / 'flows'), table='IOT', mode='flows')
        workbook = args.workbook or destination / 'add_sectors.xlsx'
        db.read_add_sectors_excel(workbook, read_inventories=True, split=True)
        steps = db.add_sectors_workbook.intermediate_steps
        options = dict(split=True, solver=args.solver)
        if steps is not None:
            options.update(intermediate_steps=True, save_intermediates=args.output if args.prepared and args.output else destination / 'checkpoints')
        else:
            options['cvxlab_path'] = destination / 'cvxlab'
            options['cvxlab_path'].mkdir()
        if (destination / 'final').exists():
            raise FileExistsError('A final database already exists in this preparation directory.')
        db.add_sectors('inventories', **options)
        db.to_parquet(path=destination / 'final', flows=True, coefficients=False, include_meta=True)


if __name__ == '__main__':
    main()
