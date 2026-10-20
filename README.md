# ENTICE inventory — GTAP12 disaggregation toolkit (D2.4)

Tooling for the ENTICE **D2.4 — Enhanced GTAP database** deliverable. It turns
sector-level cost inventories into MARIO `add_sector` workbooks, applies them to
the GTAP database, and exports the per-sector D2.4 inventory workbooks plus QA
plots.

The [maintained project report](docs/baseline/README.md) is the single place for
baseline findings, current status, agreed decisions and next steps towards D2.8
and T2.6. This README covers installation and usage. The report is updated in
place; new narrative audit/follow-up reports are not created. All 67 D2.4
inventories have been reproduced from the preserved MARIO inputs; full split
MRIO certification remains open. Source and release manifests are in `manifests/`.

`data/GTAP12_matching.xlsx` currently supplies the runner's GTAP parent mapping.
It is not an independently validated NACE registry: the reconstruction identified
aliases and classification/scope conflicts. New consumers use the canonical
registry described below. The historical parent mapping has not been replaced
globally: parent-dependent coefficients and quantities must be rebuilt together.

For one-sector re-export from saved coefficients, use
`python scripts/export_d24_sector.py --help`. The
[recovery guide](docs/baseline/README.md#regenerating-one-sector)
includes a concrete command. The export-only dependencies are pinned in
`requirements/d24-export.txt`; they do not certify the upstream solver environment.

## Layout

```text
data/                         bundled mappings/region definitions and local licensed inputs
data/registry/                sector identities, GTAP12 adapter and explicit region groups
scripts/run_d24_pipeline.py   end-to-end driver (Jupyter #%% cells)
src/entice_inventory/
  core/        matching_utils, residual_sector_cluster, paths
  inventory/   template_/exioiot_/copcosts_to_inventory, inventory_writer, template_checker
  export/      build_d24_inventories, plot_d24_split
```

## Install

```bash
pip install -e .            # core (openpyxl)
pip install -e '.[plots]'   # + pandas/numpy/matplotlib for the QA plots
```

For the tested MARIO/CVXLAB workflow, use `python3.13 scripts/bootstrap_producer.py`
to create an isolated environment from pinned revisions, dependencies and explicit
compatibility patches. See the [producer verification and commands](docs/baseline/README.md#producer-environment-and-representative-verification)
for the representative HYE check and its remaining numerical warnings. This is
separate from the lightweight export-only installation.

## Licensed GTAP inputs

The numerical GTAP database and `GTAP12_X.xlsx` are not distributed with this
repository. Supply them from your licensed source. The configured shared archive supplies the totals workbook from
`Database/GTAP Power 2023/Cache/GTAP12_X.xlsx` for inventory construction and QA features
that require parent output weights. An explicit local copy at
`data/GTAP12_X.xlsx` is also supported and ignored by Git.
Its expected sheet is `GTAP totals`, with columns `Region`, `Full name regions`,
`Sector to`, `Sector to full name` and `X` (M USD, reference year 2023).
Do not infer missing parent-output weights as observed zeros.

## Two pipelines

### 1. Inventory creation — `entice_inventory.inventory`

Build `Add_sector_*.xlsx`. Three entry points, one per data source, each
exposing `make_inventory(...)`:

| Module | Source | Sectors |
| --- | --- | --- |
| `template_to_inventory` | ENTICE data-collection Excel templates | hand-collected inventories |
| `exioiot_to_inventory` | `EXIOIOT.csv` (Purdue) | sectors flagged `Pipeline = EXIOIOT` |
| `copcosts_to_inventory` | `COPCOSTS.csv` (Purdue) | copper sectors not in EXIOIOT |

Shared building blocks: `inventory_writer` (`write_inventory_workbook`, the one
place that emits the shared `Add_sector_*.xlsx` layout), `template_checker`
(parse/validate templates), `core.residual_sector_cluster` (append the "rest of
parent" residual clusters), `core.matching_utils` (read `GTAP12_matching.xlsx`).

### 2. D2.4 export — `entice_inventory.export`

| Module | Role |
| --- | --- |
| `build_d24_inventories` | `export_d24_inventories(...)` + `update_trades_in_exported_inventories(...)` — read the applied MARIO database and write the per-sector D2.4 workbooks. |
| `plot_d24_split` | `plot_sector_split(...)` — QA plots of the X / VA disaggregation per parent sector. |

## Running it

Copy `config/paths.example.json` to `paths.local.json` in the repository root
and set `data_root` to your local copy of `Data split/Inventory generation` on the
project SharePoint. This personal configuration is ignored by Git. Alternatively,
set `ENTICE_DATA_ROOT`; it takes precedence over the file. `ENTICE_CONFIG` selects
a configuration stored elsewhere, including when using an installed wheel.

The `paths` object can override individual data roles without changing source
code. Relative paths are resolved from `data_root`, including sibling paths
such as `../Data collection/PURDUE/Shared material/Trades/trade.xlsx`.
`core.paths.data_path()` resolves the same roles for the driver, export and QA.

The shared layout is:

```text
Data split/
  Data collection/                 partner submissions and Shared sources.xlsx
    PURDUE/Shared material/
      Cost structures/            EXIOIOT, copper and supporting cost data
      Output and trade targets/   June1 splttargs.xlsx and original GDX
      Trades/                     May13 trade.xlsx and original GDX
      _old/May27/                 preserved older delivery
  Inventory generation/
    Classifications/
      ENTICE classifications.xlsx consolidated review view
      _sources/                   original specialist concordances
    Database/GTAP Power 2023/
      Original/                   licensed original CSV archive
      Cache/                      preserved D2.4 parquet baseline and output totals
    Data collection/Inventory cleaning/  preserved partner/MARIO intermediates
    Inventories/<run-id>/         generated inventory Excel files only
```

Technical evidence, personal runners and original Git backups are held in the
private eNextGen `Inventory archive`. Portable file roles and hashes are in
`manifests/data_sources.json` and the storage-reorganisation manifest in Git.
Access to the code does not grant access to private or licensed payloads.

`baseline_format` selects `mario_parquet` (the verified D2.4 replay), `gtap_csv`
or `gtap_gdx`. For an original GTAP bundle, extract it first, point `paths.baseline`
to its directory and select the corresponding format. This delegates directly
to MARIO's native `parse_gtap`; GDX also requires its GAMS runtime dependencies.
It does not silently fall back to cached matrices. The original CSV archive has
been preserved, but equivalence of a fresh parse to the historical D2.4 cache
has not yet been certified. Other MRIOs need their own parser and target adapter;
adding their files does not make them supported automatically.

End-to-end: open `scripts/run_d24_pipeline.py` and run the `#%%` cells in order.
Each run creates a new date/time directory, with short sector-code filenames.
Coefficients and the export diagnostic report go to ignored `build/runs/<run-id>`.
MARIO's insertion settings are unchanged. The exporter and QA plots use the same
configured data roles.

The modules with a `__main__` block can also be run from the command line, e.g.:

```bash
python -m entice_inventory.export.build_d24_inventories --help
python -m entice_inventory.inventory.template_to_inventory --help
```

## Configurable geography and sequential MRIO splits

The final geography is selected in ENTICE preprocessing. The same partition
aggregates the GTAP baseline, output targets, resolved cost profiles and trade.
Use `geography: null` for the native geography, or add this to the local config:

```json
"geography": {
  "name": "ENTICE13",
  "mapping": "/path/to/GTAP region to 13.xlsx"
},
"disaggregation": {
  "inventories": "Inventories/20261001",
  "steps": null
}
```

The mapping is a complete source-to-target partition. XLSX contains two
columns after the header; CSV/TSV have the same layout; JSON is a source-to-target
object. Relative mapping and inventory paths are resolved from `data_root`.
The 13-region map supplied with Camilla's pipeline is supported without making
13 a fixed number. Missing/duplicate region assignments are rejected.
Its versioned JSON copy is `data/geographies/gtap13.json` (163 source regions).

Use the MARIO `codex/intermediate-sector-steps` worktree based on
`dev_SUT_disag`, with CVXLAB 1.1.0 in the `mario` environment. Prepare without
solving:

```bash
python scripts/run_disaggregation.py \
  --inventories '/path/to/resolved/native/inventories' \
  --mapping '/path/to/GTAP region to 13.xlsx' \
  --intermediate-steps --output build/disaggregation/trial01
```

Edit `add_sectors.xlsx` in the prepared directory: rename the columns in
`Intermediate steps` and distribute every sector exactly once. Alternatively
provide `--steps groups.json`, whose keys are custom group names and whose
values are ordered sector lists. Omit the plan and `--intermediate-steps` for a
oneshot workbook. Then explicitly solve the prepared inputs:

```bash
python scripts/run_disaggregation.py \
  --prepared build/disaggregation/trial01 --solve
```

The runner reads the plan actually present in the edited workbook. Each
accepted group saves a reloadable database and remaining template under
`checkpoints`. Resume after revising the remaining groups:

```bash
python scripts/run_disaggregation.py --solve \
  --resume build/disaggregation/trial01/checkpoints/001_Mining \
  --workbook '/path/to/revised_remaining.xlsx' \
  --output build/disaggregation/trial01/checkpoints
```

This adapter consumes **resolved native profiles**, the boundary used by
Camilla's shortcut. The original D2.4 generation runner now also calls it after
resolving/exporting its native profiles when a geography is configured. It does
not average unresolved partial overrides or treat unknown production as zero.
Sparse export coverage is completed from explicitly stored `Total outputs` in
the original MARIO inputs (`paths.mario_inventories`, or `--output-references`).
The manifest records which observations and reference files were used; absent
native observations still cause an error.
Missing rows of a resolved sparse profile mean zero; a positive output without
a profile is an error. Zero-output groups retain an unweighted reference profile
with a warning. Nonempty structural exclusions require a separate aggregation
policy; origin clusters partly covering a target region must first be resolved
into origin flows. Sources are never edited, and each preparation requires a
new output directory. Missing split-support tabs are generated explicitly
(empty Exclusions; delta/eps zero); existing settings are retained.

Parquet flows are aggregated in column batches before constructing the smaller
database. No baseline closure or artificial zero-output epsilon is applied.
Production and interregional trade totals are sums; costs are output-weighted
averages. Within-group trade is absent from interregional targets and remains
inside the aggregated baseline. These transformations preserve flows;
geographic aggregation does not certify the numerical feasibility of `split=True`.

Two cumulative budget checks are **mandatory and blocking** in the D2.4 runner,
input preparation, and immediately before a prepared or resumed solve:

- For each parent and selected region, the sum of **all** child output targets
  must not exceed the supplied baseline parent X.
- For each parent and directed foreign origin/destination pair, summed child
  trade targets must not exceed parent deliveries to that destination in Z + Y.

All planned children are checked together, including those assigned to later
groups. On resume, pending children are compared with the remaining parent
flows in the checkpoint. Equality is allowed; the numerical allowance is
`1e-6 + 1e-8 * abs(parent)` in the parent sector's units. Targets must use those
same units. This is not the optional 1% exports/output review screen.
Every violation is recorded in `parent_budgets.json` and raises an error; targets
are not rescaled. Missing native outputs also block acceptance, even if other
members of an aggregated region have known output. After a failed preparation,
the report remains in the hidden staging directory named in the exception.
Edited workbooks are checked again in `parent_budgets_solve.json` or
`parent_budgets_resume.json` before invoking MARIO's solver.

## Canonical registry

Three editable JSON files have distinct roles: `sectors.json` holds activity
identities, source aliases and NACE Rev. 2 scopes; `gtap12.json` holds the reviewed
NACE-to-GTAP bridge and historical mappings; `regions.json` holds geography and
explicit cluster membership. They include source references and hashes. The
older NACE CSV is preserved review evidence, not a second live mapping.

`Classifications/ENTICE classifications.xlsx` is the consolidated, filterable
review view of this registry, operational compatibility tables, preserved partner
vocabularies and inherited crosswalks. The source of truth remains the versioned
registry and operational mapping workbook in Git. Unreviewed NACE declarations
and EXIOBASE crosswalks are explicitly labelled; they are not promoted to resolved
parents. Edit the maintained source records, then regenerate the view:

```bash
python scripts/export_classification_tables.py --output-dir build/classifications
node scripts/build_classification_workbook.mjs \
  build/classifications/classification_tables.json \
  build/classifications/ENTICE-classifications.xlsx \
  /path/to/bundled/node_modules
```

The builder uses the bundled `@oai/artifact-tool` runtime. Review the generated
workbook before replacing the shared view. Legacy parent lookups have not been
silently migrated to newly reviewed parents.

```bash
python scripts/registry.py sector BVL
python scripts/registry.py sector WNT --scope turbine_sets
python scripts/registry.py region GLOBAL
python scripts/registry.py --output build/registry-check.json check
python scripts/registry.py --output build/hye-check.json inspect-inventory '/path/to/Add_sector_HYE.xlsx'
```

Use `--registry-dir /path/to/registry` before the subcommand to supply an explicit
registry location. Outputs are JSON; `--output` refuses to overwrite an existing
file and prints a concise summary. Diagnostic checks are optional: `check
--checks classification regions` runs only those checks; `check --checks` skips
all optional checks and lists them as skipped. Invalid registry structure,
unreadable workbooks and ambiguous lookups produce a failed result and exit 1.
Ordinary diagnostic warnings return normally, with an action for each finding.

Python consumers can call `Registry.load()`, `registry.sector(code)`,
`registry.parent(code, target='GTAP12', scope=None)` and
`registry.members(group, geography='GTAP12')` from
`entice_inventory.core.registry`. An unresolved parent is `None` with an explicit
status; there is no fallback to a published or legacy parent. A scope selected
for a mixed activity gives a conditional mapping, not proof that its source
observations match that activity. Querying never changes data or activates a
catalogue-only sector. EXIOBASE has no adapter yet.

The template importer now takes its GTAP12 region universe from this registry,
including MRT. Its optional `registry_dir` argument selects a different registry
directory. Regenerate affected intermediates before rebuilding coefficients;
editing a published `GLOBAL` list alone would leave derived values stale.
Newly restored regions have output estimation notes in `Total outputs`.

The GTAP baseline is preserved as supplied. Producer verification diagnoses its
existing residuals without correcting matrices; the earlier experimental
baseline-closure option has been removed. Full build acceptance remains open.

## Notes

- The legacy personal `Run.py` and `paths.yml` are in the private eNextGen
  `Inventory archive/Personal runners`; they are excluded from public Git history.
- `.d24_split_cache.pkl` / `.d24_split_mixed_cache.pkl` are regenerable caches for
  `plot_d24_split` (`refresh_cache=True` rebuilds them); git-ignored.
