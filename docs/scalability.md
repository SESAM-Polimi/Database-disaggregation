# Regional scalability pilot

The first larger-geography experiment uses the inherited Purdue GTAP → EXIOBASE
crosswalk: 163 native GTAP regions → the legacy EXIOBASE 3 axis of 44 countries
and five rest-of-world aggregates. This remains a GTAP monetary IOT with GTAP
sectors; it does not import EXIOBASE transactions or change sector classification.

`data/geographies/exiobase49.json` is the complete partition. Its adjacent
`.source.json` records the shared source workbook, sheet, checksum and scope.
The source is `Classifications/_sources/Purdue/GTAP_EXIOBASE_maps.xlsx`,
`Regions_map`, with GTAP codes converted to uppercase. The inherited territorial
concordance is not independently certified. The same mapping is also present
in the consolidated classification workbook. The EXIOBASE axis is described at
<https://exiobase.eu/about-exiobase/>.

## Reproduce the one-sector test

Select MARIO `codex/mrio-model-improvements` and this repository's
`codex/configurable-regions` branch; configure your own `data_root`. From this
repository root, with the MARIO environment activated:

```bash
export MARIO_SOURCE="/path/to/the/matching/MARIO/checkout"
export PYTHONPATH="$MARIO_SOURCE:$PWD/src"
python scripts/run_disaggregation.py \
  --mapping data/geographies/exiobase49.json \
  --cleaning-policy config/cleaning-policy.json \
  --steps config/exiobase49-pilot-steps.json \
  --output build/scalability/my_exio49/prepared
python scripts/run_model_trial.py \
  --prepared build/scalability/my_exio49/prepared \
  --options config/model-trials/quadratic-gurobi.json \
  --solver GUROBI \
  --solver-options config/model-trials/gurobi.json \
  --stop-after-step "Pilot MCU"
```

Preparation retains all 67 children for consistent cumulative output/trade
budgets and future supplier references. The solve introduces only **MCU (copper
ore mining)**; 66 children remain pending. The baseline has 76 sectors per
region (3,724 sector/region coordinates); an accepted pilot has 77 (3,773).

The quadratic formulation uses inherited accounting, Capital/Labor ≥ 0,
signed Tax/TTM, exact preceding aggregates and deferred E recalculation. Its normalized objective/accounting options match the previous quadratic
policy; the new policy selects Gurobi for the affine feasibility check as well
as the QP. The two-thread, 1,800-second controls and tight solver tolerances do
not change the constraints, objective or independent acceptance criteria.
The feasibility probe retains the same absolute numerical envelope as before. Source data and
the native baseline are preserved; geography changes always start from scratch.

Record preparation and trial wall times separately, solver times, model variable
and constraint counts, sampled peak process-tree RSS (not a physical-memory/PSS
measurement), status, and independent checkpoint conservation/accounting/target
checks. A resource stop is not a proof of mathematical infeasibility. A successful
one-child pilot does not establish feasibility or runtime for all 67 children.
The historical 13-region Mining run introduced 17 children and used an older
factor policy, so its runtime is context rather than a controlled scaling ratio.

Numerical workspaces and resource logs stay under ignored `build/scalability/`;
published inputs/results use the standard paired SharePoint folders. Results
will be appended here once the real run finishes.
