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

These commands describe the recorded quadratic pilot below. New experiments
now default to the [entropy-first model/solver policy](model-policy.md); keep the
explicit quadratic arguments only to reproduce that formulation.

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
as the QP. A working Gurobi installation and licence are required. The two-thread,
1,800-second controls and tight solver tolerances do
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
published inputs/results use the standard paired SharePoint folders.

## Accepted result — 21 October 2026

The real MCU pilot completed with Gurobi in both stages and was published as
`20261021 1741 - 49 regions and 1 sectors`. This folder name counts newly
introduced sectors: the database contains **49 regions and 77 total sectors**.
The paired folders, relative to `data_root`, are:

- `Inventories/D2.8 inventories/20261021 1741 - 49 regions and 1 sectors`
- `Database/D2.8/20261021 1741 - 49 regions and 1 sectors`

The exact pre-split baseline is `Database/_GTAP Power 2023/EXIOBASE49 baseline`.
Run provenance records pipeline revision `6d75770` and MARIO revision `90da5c8`.

| Measurement | Accepted pilot |
| --- | ---: |
| Scalar variables in the feasibility probe | 749,602 |
| Canonical affine constraint rows | 3,350,168 |
| Gurobi feasibility solver time | 31.5 s |
| Gurobi QP solver time | 6.3 s |
| Trial wall time before publication | 544.3 s |
| Trial wall time including publication | 746.8 s |
| Peak sampled process-tree RSS | 3.59 GiB |
| Read-only benchmark wall time | 8.1 s |

The feasibility LP represents equality envelopes as two inequality rows, giving
3,922,324 native Gurobi rows. Its nominal absolute envelope and Gurobi's native
feasibility tolerance are both recorded in `diagnostics/feasibility.json`.
It is a preliminary diagnostic; the original QP constraints and independent
acceptance checks determine whether a checkpoint is accepted.

Most elapsed time was outside the native solver: workbook/database I/O,
construction, canonicalisation, verification and publication. These measurements
are from one run on an 18 GiB Mac, with two solver threads and one-second RSS
sampling. The RSS sum can double-count shared pages and excludes compressed
memory. Preparation is excluded from the successful-trial wall times above.

The independent checkpoint verifier accepted the result. The saved-matrix
benchmark passed all **11 hard checks**, including reaggregation, inherited
accounting, nonnegative Z, all 49 prepared child outputs and 346 selected prepared
trade observations. Capital and Labor are nonnegative in the affected child and
residual columns. The report computed Leontief stability diagnostics for both
databases. E remains pending recalculation.

The dashboard nevertheless reports **85 economic review flags across 45
sector/region coordinates**: 25 for gross flows at effectively zero output,
29 for imported-input share changes, 19 for export share changes, 11 for VA share
changes and one for a final-demand share change. Passing accounting and target
checks does not establish economic plausibility or independently validate the
harmonised targets. These flags remain visible for review; no post-hoc matrix
patch was applied.

### Preparation and attempt history

The full 67-child preparation contains **3,283 region/sector inventory sheets**.
Its first export was interrupted after about 19 minutes when profiling identified
a repeated quadratic sheet lookup in the Excel writer. MARIO now constructs the
same sheet-name mapping in one pass. A ZIP-member regression comparison verified
that the writer preserves the workbook contents. Serialization then resumed from
the 67 already reconciled, unchanged workbooks in 136.6 seconds, without a second
reconciliation. This is a recovery measurement, not a clean end-to-end preparation
benchmark. All 174 original source files were hash-verified unchanged.

An initial Clarabel trial reached `optimal`, but a sparse-expression error in the
independent verifier prevented acceptance and publication of a database. MARIO's
verifier now handles sparse affine domains without changing the acceptance
thresholds. Tests cover valid results and rejection of actual violations. The
subsequent Gurobi trial reused the same preparation and mathematical policy.
The two attempts are not a controlled solver-speed comparison.

The first read-only benchmark was also stopped: the published XLSX container
changed during reading. Comparison with the accepted local step input showed
identical model worksheets, workbook, strings and styles; differences were in
package metadata. The retry passed the original file-integrity checks, without
relaxing them. Both benchmark logs and the package comparison are retained.

The accepted database includes the dashboard (`benchmarking.html`), report JSON,
sector CSV, and `diagnostics/scalability/summary.json` with resource logs,
preparation audit and attempt history. The 66 pending children were not solved;
this result establishes only the feasibility of this one-child, 49-region pilot.
