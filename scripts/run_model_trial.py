"""Run one MRIO model experiment from prepared inputs or an accepted checkpoint.

Inputs must already contain the intended Intermediate steps plan. No cleaning,
source selection, baseline closure or modification of the source run occurs.
Use a fresh output directory for every experiment.
"""
import argparse
import hashlib
from importlib.metadata import version
import inspect
import json
from pathlib import Path
import shutil
import subprocess
import time
import traceback


def fingerprints(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file()}


def code_identity(module):
    source = Path(module.__file__).resolve()
    result = {'module': str(source)}
    try:
        repo = Path(subprocess.check_output(
            ['git', '-C', str(source.parent), 'rev-parse', '--show-toplevel'], text=True,stderr=subprocess.DEVNULL).strip())
        result.update(repository=str(repo), revision=subprocess.check_output(
            ['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip(),
            dirty=bool(subprocess.check_output(
                ['git', '-C', str(repo), 'status', '--porcelain'], text=True).strip()))
        result['python_sha256'] = {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in sorted(source.parent.rglob('*.py'))}
    except subprocess.CalledProcessError:
        result['revision'] = None
        result['python_sha256'] = {str(p.relative_to(source.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in sorted(source.parent.rglob('*.py'))}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument('--prepared', type=Path)
    source_group.add_argument('--resume', type=Path, help='Accepted MARIO intermediate checkpoint.')
    parser.add_argument('--workbook', type=Path, help='Remaining workbook override; requires --resume.')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--options', type=Path, help='MARIO split_model_options JSON; omit for the unchanged model.')
    parser.add_argument('--solver-options', type=Path)
    parser.add_argument('--solver', default='CLARABEL')
    parser.add_argument('--stop-after-step', help='Defaults to Mining for a fresh preparation; resume runs all pending groups.')
    args = parser.parse_args()
    options = json.loads(args.options.read_text()) if args.options else None
    solver_options = json.loads(args.solver_options.read_text()) if args.solver_options else None
    if args.workbook and not args.resume:
        parser.error('--workbook requires --resume.')
    source = (args.resume or args.prepared).resolve()
    stop_after_step = args.stop_after_step if args.resume else args.stop_after_step or 'Mining'
    output = args.output.resolve()
    if output == source or source in output.parents:
        parser.error('The output must be separate from the immutable preparation.')
    if args.resume:
        if not (source/'state.json').is_file():
            parser.error('Expected state.json in --resume.')
        if args.options is None:
            options = json.loads((source/'state.json').read_text()).get('split_model_options')
        workbook = (args.workbook or source/'remaining_add_sectors.xlsx').resolve()
    else:
        workbook = source/'add_sectors.xlsx'
    if not args.resume and (not (source/'baseline'/'flows').is_dir() or not workbook.is_file()):
        parser.error('Expected baseline/flows and add_sectors.xlsx in --prepared.')
    output.mkdir(parents=True, exist_ok=False)
    baseline_hashes = fingerprints(source if args.resume else source/'baseline')
    workbook_hash = hashlib.sha256(workbook.read_bytes()).hexdigest()
    if not args.resume:
        shutil.copytree(source/'baseline', output/'baseline')
    shutil.copy2(workbook, output/'add_sectors.xlsx')
    import mario
    import cvxlab
    import entice_inventory
    from entice_inventory.core.parent_budgets import ParentBudgets, ChildTargets, require_parent_budgets
    manifest = {'status': 'running', 'source_checkpoint' if args.resume else 'source_preparation': str(source),
                'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'source_baseline_sha256': baseline_hashes, 'source_workbook_sha256': workbook_hash,
                'split_model_options': options, 'solver': args.solver, 'solver_options': solver_options,
                'source_workbook': str(workbook), 'stop_after_step': stop_after_step,
                'runtime': {p: version(p) for p in ('mariopy','cvxlab','cvxpy','numpy','pandas','clarabel')},
                'code': {name: code_identity(module) for name,module in
                         [('mario',mario),('cvxlab',cvxlab),('entice_inventory',entice_inventory)]}}
    path = output/'trial.json'
    path.write_text(json.dumps(manifest, indent=2))
    started = time.monotonic()
    exit_code = 1
    try:
        if options is not None and 'split_model_options' not in inspect.signature(mario.Database.add_sectors).parameters:
            raise RuntimeError('The selected MARIO checkout does not support split_model_options.')
        if args.resume:
            from mario.ops.add_sector_steps import load_checkpoint
            db = load_checkpoint(source)
        else:
            db = mario.parse_from_parquet(str(output/'baseline'/'flows'), table='IOT', mode='flows')
        db.read_add_sectors_excel(output/'add_sectors.xlsx', read_inventories=True, split=True)
        targets = ChildTargets.from_workbook(db.add_sectors_workbook)
        if args.resume:
            targets = targets.pending(db)
        require_parent_budgets(ParentBudgets.from_database(db), targets,
                               report_path=output/'parent_budgets.json')
        if not db.add_sectors_workbook.intermediate_steps:
            raise ValueError('A model trial requires an explicit Intermediate steps plan.')
        kwargs = dict(split=True, intermediate_steps=True, save_intermediates=output/'checkpoints',
                      stop_after_step=stop_after_step, solver=args.solver, solver_parameters=solver_options)
        if options is not None:
            kwargs['split_model_options'] = options
        db.add_sectors('inventories', **kwargs)
        manifest.update(status='accepted', completed_sectors=db._intermediate_steps_state['completed_sectors'],
                        pending_recalculations=db._intermediate_steps_state.get('pending_recalculations',[]))
        exit_code = 0
    except Exception as exc:
        manifest.update(status='failed', error=str(exc), traceback=traceback.format_exc())
        traceback.print_exc()
    finally:
        manifest['elapsed_seconds'] = time.monotonic()-started
        manifest['source_baseline_unchanged'] = fingerprints(source if args.resume else source/'baseline') == baseline_hashes
        manifest['source_workbook_unchanged'] = hashlib.sha256(workbook.read_bytes()).hexdigest() == workbook_hash
        manifest['working_baseline_unchanged'] = (True if args.resume else fingerprints(output/'baseline') == baseline_hashes)
        manifest['accepted_checkpoints'] = [str(p.parent) for p in sorted((output/'checkpoints').glob('*/state.json'))
                                            if not p.parent.name.startswith('.')]
        if not all(manifest[k] for k in ('source_baseline_unchanged','source_workbook_unchanged','working_baseline_unchanged')):
            manifest.update(status='failed', integrity_error='Input hashes changed during the trial.')
            exit_code = 1
        path.write_text(json.dumps(manifest, indent=2, allow_nan=False))
        print(json.dumps({k: manifest.get(k) for k in ('status','elapsed_seconds','error','completed_sectors',
                                                     'pending_recalculations')}, indent=2))
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
