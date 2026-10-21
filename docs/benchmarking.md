# Benchmarking saved monetary MRIO databases

The experimental `codex/configurable-regions` branch provides an **offline,
read-only dashboard** for the accepted 13-region, 67-new-sector experiment.
The final database contains 143 sectors (76 original sectors/residuals + 67
children), not 67 total sectors. The baseline contains the original 76 sectors
at the exact same 13-region geography.

This is post-processing: it imports no MARIO/CVXLab/optimisation solver and does
not run the disaggregation, balance flows, reconcile targets or recalculate E.
Keep the numerical dashboard, JSON and CSV in the shared Data split storage.
The repository contains code, methodology and synthetic tests only.

## Run

```bash
pip install -e '.[benchmark]'
python scripts/benchmark_database.py \
  --database 'Database/D2.8/20261021 0655 - 13 regions and 67 sectors' \
  --baseline 'Database/_GTAP Power 2023/ENTICE13 baseline'
```

Relative paths resolve against `data_root` in the usual `paths.local.json`
configuration (or `ENTICE_DATA_ROOT`). Explicit absolute paths are also accepted.
Both database arguments are required; the script never guesses the latest run.
It writes three files directly beside the final database:

- `benchmarking.html`: self-contained interactive dashboard, with embedded data;
  open in a browser, including offline. No web server, CDN, external fonts or
  online accounts are needed. SharePoint's preview may not execute HTML: open
  the synchronised/downloaded file in a browser.
- `benchmarking.json`: full KPIs, checks, screening findings and input hashes.
- `benchmarking-sectors.csv`: scalar KPIs for every sector-region pair. Baseline
  parent indices/outputs are explicit; detailed factor/demand/route arrays are
  in the JSON and dashboard.

`--output` chooses another HTML filename, with matching JSON and CSV stems.
Existing report files are protected unless `--overwrite` is supplied. Output
inside source `flows/` is rejected. `--skip-system` skips Leontief linear algebra
and explicitly marks those diagnostics as not computed. Exit code 2 means a
hard benchmark check failed; review flags alone do not cause failure.

The published `ENTICE13 baseline` is a byte-for-byte copy of the original
accepted Mining trial's pre-split baseline. `baseline_provenance.json` records
its source and original hashes. The copy requires no model or geography rerun.
Do not substitute the D2.4 `split=False` database, the 163-region cache or a
preceding 17/49-child checkpoint for this comparison.

## Dashboard views

1. **Overview:** aggregate output, V, foreign deliveries, conservation checks,
   gross signed flows, review counts and largest common-shock differences.
2. **Sector explorer:** region, parent, scope, name/code and output filters;
   sortable/ranked technology, V/Y/trade and multiplier KPIs. Detail compares a
   child or residual with its baseline parent, on a common input classification.
3. **Trade & adjustments:** all origin-destination Z+Y deliveries for a selected
   sector, in M USD or as a delivery/X difference from the baseline parent;
   route-level prepared-prior → projected-target → final audit where available.
4. **System response:** comparable final demand shocks, output multipliers,
   spectral radius, conditioning and omitted zero-output flows.
5. **Review queue:** filterable findings, click-through to sector detail, CSV
   export. Findings stay separate from hard accounting checks.
6. **Method & sources:** formulas, thresholds, scope limits and full input hashes.

## Hard checks

All monetary flows must be finite; labels must be unique and align explicitly;
the geography and child-parent map must match. Sector/factor units must be M USD.
Final checkpoint files are verified against `state.json`. Baseline provenance
hashes are verified when present. Source hashes are checked again at the end;
an input change aborts publication.

- Reaggregate children **and the remaining original parent** to the baseline.
  Aggregate both axes of Z, the rows of Y/X and the columns of V. Compare EY and
  VY unchanged, without adding unlike environmental units together.
- Read **authoritative X from X.parquet**. A generic flow parser that recomputes
  X from row sums would erase inherited discrepancies and invalidate this test.
- Row discrepancy: `sum(Z row) + sum(Y row) - X`. Column discrepancy:
  `sum(Z column) + sum(V column) - X`. For `accounting="inherit"`, the expected
  final discrepancy is the original parent's discrepancy times `X_child/X_parent`.
- Monetary comparisons use `1e-6 + 1e-8 * abs(reference)` M USD per cell, matching
  the accepted checkpoint. EY/VY are unchanged exactly. Z values below −1 USD
  per cell fail the nonnegativity check. Gross sums can exceed 1 USD despite
  every constituent cell falling within tolerance; both views are reported.
- Traverse the published run's predecessor chain and inspect only each stage's
  applied `step_sectors` in its paired `add_sectors.xlsx`. Recheck every listed
  output and bilateral trade observation, including explicit zero targets.
  Unlisted routes are unobserved, not zero. Target adherence concerns the
  **prepared** data and is not independent validation. A missing published chain
  is marked unavailable; incomplete child-output coverage in an available
  chain fails a hard check.

This first version deliberately requires the saved `accounting="inherit"`
policy and the above tolerances. Other policies need their own explicit audits.

## Economic indicators and screening

The reference for a fine sector is its **original parent in the baseline**, not
the parent's remaining residual in the final database. Intermediate input
coefficients use `Z_ij/X_j`; supplier rows are summed over all origins and
mapped to original sectors. Technology distance is the L1 sum of differences
between the two complete coefficient vectors; the dashboard plots the 12 largest
input coefficients across the two profiles. Input import share divides foreign
intermediate inputs by all intermediate inputs; export propensity divides
foreign Z+Y deliveries by X. Export HHI uses positive foreign deliveries only.
Final demand categories sum over destinations and retain their signs. Factor
shares, net Y/X and gross positive/negative Y are available separately.

There is no universal “good share” constraint or composite quality score.
Transparent first screening rules are:

- negative labor or capital beyond 1 USD, with the baseline parent's sign;
- remaining gross Z/Y/V flows beyond 1 USD when X is at most 1 USD;
- exhausted parent residuals where the baseline parent had material output;
- V/X, exports/X, input import share or Y/X differing by >25 percentage points
  from the baseline parent;
- common-shock output multipliers differing by >0.25 output per unit shock.

These thresholds select cases to inspect; they are **not empirical acceptance
tests**. Ratios for denominators ≤1 USD remain null. The output filter helps
separate tiny sectors from material results. Negative taxes and margins are
reported, without being automatically interpreted as errors.

## Leontief diagnostics

Build `A = Z / X` by column and solve `(I-A) response = shock` by LU, without
optimisation. Report the spectral radius, a 1-norm condition estimate, column-sum
output multipliers and linear solve residual. Tiny signed Z values remain in A.
X≤1 USD rows/columns are excluded; report their gross input and output flows.
**Material excluded inputs make the resulting multipliers conditional on that
exclusion** and require review even when the matrix is numerically stable.

Each common shock adds 1 M USD of final demand to one baseline sector/region.
In the detailed system it is allocated to the children and residual in fixed
authoritative-X shares of that same original parent/region. No share is fitted
to reproduce the baseline response. If active fine-sector shares fail to retain
the full shock to within 1e-8, exclude that shock instead of renormalising it.
Aggregate output responses geographically for comparison. Do not require fine
and coarse Leontief multipliers to coincide: conservation of flows does not
imply conservation of economic responses. Median/max multiplier statistics span
different sector universes; common shocks provide the aligned comparison.

## Limits and next steps

E/energy/emission intensities and footprints are unavailable until recalculation.
Prepared-prior adherence, model sensitivity, sequential-order sensitivity,
external/held-out observations and the full raw→prepared harmonisation chain
are separate work. The current route-level adjustment view covers the recorded
final row-feasibility projection only. This report does not certify full MRIO
economic plausibility merely because the hard accounting tests pass.

## Verification

```bash
python -m pytest tests/test_benchmark.py -q
```

Synthetic tests cover two-axis aggregation, independent X, inherited accounting,
common shocks against a direct inverse, undefined ratios/gross signed flows,
new negative labor despite exact conservation, hash/non-finite/mapping failures,
offline export and source/overwrite protection. Browser verification of the
generated report should cover tab navigation, filters, sector drill-down, trade
views, common shocks and review exports before sharing a new template version.

An optional DOM smoke test exercises those interactions on a synthetic exported
fixture, including JSON/CSV downloads. It is not a visual browser/layout test:

```bash
npm install --prefix /tmp/benchmark-dom --no-audit --no-fund jsdom@26.1.0
NODE_PATH=/tmp/benchmark-dom/node_modules ENTICE_BENCHMARK_DOM_TEST=1 \
  python -m pytest tests/test_benchmark.py -q
```
