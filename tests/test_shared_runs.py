from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil

import pandas as pd
import pytest
from entice_inventory.core.shared_runs import publish_trial, remaining_workbook, run_name


def trial_fixture(tmp_path,status='accepted'):
    from test_parent_budgets import _baseline
    _baseline(tmp_path)
    trial=tmp_path/'trial';trial.mkdir()
    source=trial/'add_sectors.xlsx'
    pd.DataFrame({'Sector':['New']}).to_excel(source,sheet_name='Master',index=False)
    manifest=dict(status=status,started_at='2026-10-21T04:55:00+00:00',source_preparation=str(tmp_path),
                  accepted_checkpoints=[])
    if status=='accepted':
        checkpoint=trial/'checkpoints/001_Test';checkpoint.mkdir(parents=True)
        shutil.copytree(tmp_path/'baseline',checkpoint/'database')
        for name in ('step_add_sectors.xlsx','remaining_add_sectors.xlsx'):shutil.copy2(source,checkpoint/name)
        state=dict(format='mario-sector-steps-v1',status='complete',completed_sectors=['New'],
                   files={str(p.relative_to(checkpoint)):hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (checkpoint/'database').rglob('*') if p.is_file()})
        (checkpoint/'state.json').write_text(json.dumps(state))
        manifest['accepted_checkpoints']=[str(checkpoint)]
    (trial/'trial.json').write_text(json.dumps(manifest))
    return trial


@pytest.mark.parametrize('status',['accepted','failed'])
def test_publication_pairs_names_and_preserves_inputs_and_matrices(tmp_path,status):
    trial=trial_fixture(tmp_path,status)
    original={str(p.relative_to(trial)):hashlib.sha256(p.read_bytes()).hexdigest() for p in trial.rglob('*') if p.is_file()}
    options=dict(inventory_root=tmp_path/'Inventories/D2.8 inventories',database_root=tmp_path/'Database')
    result=publish_trial(trial,**options)
    inventory=Path(result['inventory'])
    database=tmp_path/'Database'/result['name']
    assert inventory.name==database.name=='20261021 0655 - 3 regions and 1 sectors'
    assert (inventory/'add_sectors.xlsx').read_bytes()==(trial/'add_sectors.xlsx').read_bytes()
    assert (database/'flows').exists()==(status=='accepted')
    if status=='accepted':
        assert result['database']==str(database)
        assert remaining_workbook(database)==inventory/'remaining_add_sectors.xlsx'
        state=json.loads((database/'state.json').read_text())
        assert state['database_directory']=='.'
        assert all(hashlib.sha256((database/p).read_bytes()).hexdigest()==digest for p,digest in state['files'].items())
        from mario.ops.add_sector_steps import load_checkpoint
        assert load_checkpoint(database).get_index('Region')==['R1','R2','R3']
    else:
        assert result['database'] is None and not database.exists()
        assert (inventory/'diagnostics/trial.json').is_file()
    assert original=={str(p.relative_to(trial)):hashlib.sha256(p.read_bytes()).hexdigest() for p in trial.rglob('*') if p.is_file()}
    with pytest.raises(FileExistsError):publish_trial(trial,**options)


def test_run_name_keeps_original_project_time_and_rejects_ambiguous_times():
    assert run_name('2026-10-20T20:09:02+00:00',13,17)=='20261020 2209 - 13 regions and 17 sectors'
    with pytest.raises(ValueError):run_name(datetime(2026,10,21),13,67)
