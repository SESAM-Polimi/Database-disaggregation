# ENTICE inventory: reconstruction and implementation plan

Updated 14 October 2026. This is the single maintained report for the D2.4 reconstruction, consistency findings, agreed decisions and work towards D2.8 and T2.6. Update it in place; do not create separate follow-up, decision or audit Markdown reports. The [repository README](../../README.md) is the installation and usage guide. CSV/JSON evidence and manifests retain their separate purpose: reproducible records that this report references. Links under `build/` refer to retained local audit artifacts; that ignored directory is outside the published Git history.

## Current status and next steps

The published baseline and its available source chain have been identified. Project SharePoint matches the published cached values; the damaged ZIR workbook has been recovered without changing its workbook parts. Re-exporting ZIR alone reproduces its numerical records. A clean, pinned MARIO/CVXLAB environment and the native HYE coefficient replay are available. The first canonical registry is implemented: 67 published records, 21 inactive catalogue-only records, NACE-led target resolution and 163 explicit GTAP regions. The HYE geography defect has been traced and corrected in the template importer. **Full MRIO certification remains open. The GTAP baseline must remain as supplied; its accounting discrepancies are diagnostics, not an inventory-project correction task.**

The [full inventory regeneration](#full-d24-inventory-regeneration) completed on 2 October 2026 using the unchanged native MARIO workflow. All 67 distinct released sectors were recalculated from the supplied baseline and existing MARIO inputs. Their coefficient, output and trade records reproduce the operational D2.4 reference exactly. Three legacy parent-label overrides and existing numerical warnings remain visible. Verified copies use short code filenames under `Inventories/20261001` in the project SharePoint data root; originals remain unchanged.

The [all-sector split-readiness audit](#all-sector-split-readiness-audit-12-october-2026) now covers those 67 distinct regenerated sectors, all 68 MARIO intermediates, 36 partner templates and the complete native GTAP reference. It identifies joint production, trade and fixed-profile conflicts and source-definition/unit risks before `split=True`. This is read-only evidence, not an adopted correction or a solver certification. All 187 numerical/configuration source files used were rehashed unchanged; production code and source workbooks remain untouched.

Following the target simulation, the owner selected warning plus proportional reduction of child output targets whenever their regional sum exceeds the supplied parent's output. APS REST OF EUROPE excludes GBR; SDG GLOBAL means the rest of the world. These are adopted planning decisions, not implemented transformations. A subsequent direct GDX/API check confirms that REPOUT stores only positive records and in-domain omissions read as zero in the delivered sparse numerical parameter. This source-level meaning does not independently certify empirical production; partner coverage omissions remain distinct.

The 14 October discussion clarified that a binding proportional cap assigns the original parent's entire output to its children and leaves zero output for the residual parent in the split database. This assumes that the children exhaust the parent's activities. A positive residual, where justified by activity coverage, would require reserving a supported output amount before fitting the children. No residual reserve has been selected, and the cap remains pending implementation and coverage review.

The [joint target simulation](#joint-output-and-trade-target-simulation-13-october-2026) now applies those decisions across all 67 activities and compares matched May27/June1 Purdue deliveries. All 69 over-budget parent-region groups are reduced proportionally, but output-only trade preparation still leaves 7,538–7,542 conditional parent-route excesses. Under the unharmonized native monetary-envelope assumption, the maximum-retention benchmark requires about 10.9% less selected trade. This is a measure of candidate-data incompatibility under specified constraints, not an adopted empirical trade correction. Source scope/valuation, 17 composite trade allocations, 41 unknown output cells, 57 positive outputs lacking released profiles and full MRIO feasibility remain open.

At the owner's request, [actual `split=True` runtime attempts](#actual-splittrue-runtime-diagnostic-13-october-2026) now complement those target simulations. The reduced DEU/ROW diagnostic loads all 67 children and reaches CVXLab optimisation. CLARABEL fails with and without trade; SCS declares the same no-trade model infeasible. Twelve negative child-reference Tax/TTM values lie outside the current relative-entropy objective's domain. No supplied baseline values, source workbooks or operational modules were changed. This is a verified failure diagnosis, not a successful native 163-region split.

The remaining work is implementation and controlled verification. The order below reflects dependencies, with no calendar commitments:

| Order | Concrete work | Completion evidence |
|---|---|---|
| 1. Reproducible build | Implemented: pinned installer, compatibility patches, native HYE replay, representative end-to-end check and all-sector D2.4 inventory regeneration. Remaining: full split acceptance with the baseline preserved. | All 67 regenerated inventories reproduce reference coefficients, outputs and trades exactly. The earlier reconciled diagnostic remains historical evidence only. No new baseline closure is allowed. |
| 2. Canonical sector and region registry | Implemented: three purpose-specific JSON files, Python API, CLI, explicit scope/alias warnings and canonical geography in the template importer. Classification review remains partial. | 88 identities, including 67 published records; 25 have reviewed activity definitions/options. Ambiguous aliases never select a first row. HYE regeneration restores MRT and records its estimated output. |
| 3. Transformations and diagnostics | Implement the agreed optional warning policy; make trade-source selection and normalisation/caps/factor completion traceable. Repair cluster allocation after defining units, overlaps and direct-observation precedence. | Warnings and skipped checks visible; input-to-output changes traceable; targeted regression comparisons, including HVC cluster totals and production/trade screening. |
| 4. Guided Excel pilot | Build one compact HYE workbook on the existing SharePoint, with filterable tables for metadata/sources, cost inputs, production and trade. Preserve unavailable original observations as unavailable and identify inherited baseline values. | A colleague can edit an observation in Excel; a recorded snapshot can be validated and that sector regenerated; the numerical change and any warnings can be reviewed. Assess layout/usability before migrating all sectors. |
| 5. Extend and clean | Apply the tested model to the other sectors, expose the same operations for T2.6, then trial another MRIO. Perform broad file cleanup after replacements and provenance are verified. | Reusable source data and target adapters; a two-target comparison explaining mapping, geography and valuation differences; obsolete files identified against working replacements. |

The registry now provides a common basis for the guided Excel pilot and T2.6. Next connect source observations and transformation records to it, progressively complete the remaining activity reviews, and replace legacy parent lookups during controlled sector rebuilds. Keep full-scale numerical acceptance open. The baseline-residual policy is settled: report the supplied residuals and any new extension residuals separately, without repairing GTAP.

The owner has now selected the project SharePoint for operational data and editing: `Data split/Inventory generation`. Git holds code, schemas, mappings/configuration and manifests. MARIO/CVXLAB is the selected implementation. Diagnostics are optional, with clear warnings and visible skipped checks; the final MRIO must still satisfy accounting identities within reported numerical tolerances.

Navigate to [baseline and source chain](#the-release-reference), [recovery](#why-zir-failed-and-what-was-recovered), [classification](#nace-led-parent-definitions), [consistency](#production-and-trade-consistency), [environment](#producer-environment-and-representative-verification), [Excel and T2.6](#portability-excel-and-t26), [single-sector export](#regenerating-one-sector), or [decision register](#decision-register).

## Repository integration and publication

Publication completed on 1 October 2026: [ENTICE_inventory](https://github.com/SESAM-Polimi/ENTICE_inventory) is the public code repository; [ENTICE_inventory_archive](https://github.com/SESAM-Polimi/ENTICE_inventory_archive) retains the original private history. A fresh clone from GitHub was checked before changing visibility. Its complete reachable history excludes the three file names listed below, including both historical locations of the licensed totals workbook.

The original private repository integrates all reconstruction and registry changes in merge `b5382268ccc051cac222116e7e62eb1af40ff17e`. Its first parent is the original main `14fc2bf52802ca1572efd557de15c15cf4abf77d`, also preserved by the annotated tag `backup/main-before-registry-2026-10-01`. Verified Git bundles preserve the complete history before and after integration, alongside the pre-merge working tree and staged/unstaged patches.

The public code history excludes both historical paths of the numerical `GTAP12_X.xlsx` workbook and the personal `Run.py`/`paths.yml` files. The original history remains in the private archive repository and on SharePoint. Public commit identifiers differ from the original private identifiers; a backup tag in the filtered history represents the corresponding code state without excluded files. The original main has not been lost or overwritten.

The [GTAP 12 terms, section 3](https://www.gtap.agecon.purdue.edu/databases/documents/GTAP12DataBase_TermsConditions.pdf) restrict redistribution of database values and large aggregations. Public code therefore uses externally supplied licensed inputs. The working files and historical text were checked for common credential/private-key patterns, with no matches; this is a limited check, not an exhaustive security certification. Ignored numerical data, private configuration and archived evidence are not published on GitHub.

### Project SharePoint organisation

The current operational root is `Data split/Inventory generation`. Partner submissions and `Shared sources.xlsx` are in the sibling `Data split/Data collection`. The owner reorganised the initial archive on 2 October; the configuration and source catalogue now follow that structure. The initial 1 October copy contained 1,170 files (approximately 2.47 GB), verified against source and destination SHA-256. That historical transfer is not the current folder inventory. Original eNextGen source files were retained.

| Current location | Purpose |
|---|---|
| `Data collection/PURDUE/Shared material/Cost structures` | June1 EXIOIOT and copper data; original cost container and supporting tables. |
| `Data collection/PURDUE/Shared material/Output and trade targets` | June1 `splttargs.xlsx` and its original GDX. |
| `Data collection/PURDUE/Shared material/Trades` | May13 `trade.xlsx` and its original GDX. |
| `Data collection/PURDUE/Shared material/_old/May27` | Previous delivery, preserved for comparison. |
| `Inventory generation/Classifications` | One consolidated review workbook; original specialist files under `_sources`. |
| `Inventory generation/Database/GTAP Power 2023/Original` | Original licensed Purdue CSV archive. |
| `Inventory generation/Database/GTAP Power 2023/Cache` | The eight unchanged D2.4 baseline parquet matrices and `GTAP12_X.xlsx`. |
| `Inventory generation/Data collection/Inventory cleaning` | Preserved partner/MARIO intermediate inputs, historical D2.4 inventories and coefficients. |
| `Inventory generation/Inventories/20261001` | Only the 67 regenerated inventory workbooks. |

`Repository inputs` was a staging folder, not a separate database or classification layer: it held the licensed numerical `GTAP12_X.xlsx` and personal runners. It has been removed after relocating those contents. **GTAP12_X is not a mapping:** it holds regional GTAP output totals used for weights, caps and QA. It therefore belongs beside the baseline cache, not in Classifications.

The private eNextGen `ENTICE - Documents/Inventory archive` now holds `Repository backups`, `Archive records`, `Personal runners`, `Regeneration 20261001`, `Legacy audits` and `ZIR recovery`. `Archive records` held transfer scripts and copy logs with personal paths. Their portable file roles, relative locations and hashes are recorded in Git; the raw private records stay off public GitHub. The run's fresh coefficient database and verification evidence are preserved privately, rather than deleted or shown beside partner outputs. The owner's deleted `Reference documents` and `Verification` folders were not recreated; local evidence and original source documents remain available.

The [source catalogue](../../manifests/data_sources.json) records file purposes; the [reorganisation manifest](../../manifests/storage_reorganization_2026-10-02.json) records 128 moves: 61 to private storage and 67 within the project tree. 125 were hash-verified. Three cloud placeholders were renamed without claiming content verification: `New sectors classification.xlsx` and two ICCS Costa Rica support workbooks. No numeric source data were edited.

#### What the Purdue deliveries contain

| File or group | Content and current use |
|---|---|
| `EXIOIOT.csv` | Source matrix used to derive cost structures; raw entries are not assumed to be normalised coefficients. |
| `COPCOSTS.csv`, `COPSEC.csv` | Copper cost coefficients and their sector definitions. |
| `costsup.gdx`, `costsup.xlsx` | Original mixed cost/support container and a partial Excel extraction containing sets and fertilizer shares. The Excel file is not a complete replacement for all extracted CSV tables. |
| `splttargs.xlsx` | June1 region/sector sets, output targets (`REPOUT`) and preliminary bilateral trade (`BLTTRD`). |
| `trade.xlsx` | May13 trade values and tariff data. `NTSCIF` supplies final D2.4 trades; `NTSTAR` and `MTRAT` are preserved but not used by that export. |
| `Cost structures/Supporting data` | Fertilizer use/cost shares, mineral supply observations and definition sets. Absence from the present importer does not establish obsolescence. |

May27 contains **11 byte-identical duplicates** of June1 and **four different older files**: `NFCOSTSHR.csv`, `costsup.gdx`, `splttargs.gdx` and `splttargs.xlsx`. The whole previous delivery is retained under `_old/May27`; the four differing versions were not discarded or silently merged. The existing June1-cost/output and May13-final-trade selection is unchanged. Purdue sector/HS/EXIOBASE concordances now sit in `Classifications/_sources/Purdue`.

#### Original database and derived cache

The original eNextGen `Database/GTAP 2023/12a csv/2023_csv.zip` was copied to `Database/GTAP Power 2023/Original/2023_csv.zip`, retaining its source. Its 956,283,934 bytes match SHA-256 `0e9844736cbd5cd89287fd3a0da245d4c5dcfb3dc68dcfd44754e20cdc4b51d4` on both sides and on a second source read. It contains the five original GSDF CSV tables. Member CRC checks and numerical equivalence of a fresh parse to the D2.4 cache have **not** yet been verified.

The parquet files remain necessary for reproducing the verified D2.4 baseline until that comparison is done; their presence does not establish that they are an interchangeable representation of every original GTAP delivery. `baseline_format` now selects the existing native MARIO parquet, GTAP CSV or GTAP GDX reader. CSV/GDX input must be extracted and configured explicitly; there is no silent fallback or accounting repair. GDX requires its GAMS dependencies. No MARIO source, insertion setting or numerical rule was changed. Other MRIOs may be stored as separate database directories but still require a parser and a target adapter before use.

#### One classification review workbook

`Classifications/ENTICE classifications.xlsx` consolidates **13 filterable sheets**: ENTICE sectors (88), activity scopes (33 rows), GTAP Power sectors (76), regions (163, including MRT), region-group membership (610 rows), inherited EXIOBASE bridge (345 rows), legacy concordance (178 rows), partner vocabulary (3,302 distinct rows from 36 preserved templates), the current working catalogue (187 rows), inherited CPC/NACE/ISIC source concordances (621 rows), and the unchanged operational Sector (200) and Factor of production (14) tables, plus Sources.

The workbook distinguishes reviewed NACE scopes from inherited declarations. For the 88 activities, **18 parents resolve, 7 require an activity scope and 63 remain unreviewed**. Old GTAP9/11/11Power labels are not presented as a verified GTAP12 NACE concordance. The EXIOBASE crosswalk groups sectors rather than asserting one-to-one matches; regional groups other than the complete GLOBAL universe retain their inherited review limitations. Specialist HS and other source tables remain in `_sources` rather than being flattened into misleading matches.

This is a generated review view. The maintained registry and operational compatibility workbook remain versioned in Git; editing the view alone does not change the pipeline. `scripts/export_classification_tables.py` prepares the source tables and `scripts/build_classification_workbook.mjs` builds the view with the bundled artifact runtime. Corrections should be applied to maintained source records and then regenerated. All saved rows were checked against their sources, all 13 sheets rendered for inspection, and text identifiers such as `29.10`, `01.12` and `0113` verified without truncation or loss of leading zeroes. No parent mapping was silently activated by consolidation.

#### Validation and remaining cloud limitation

All 14 configured data roles resolve after relocation. Before reopening OneDrive, SHA-256 checks confirmed that the eight baseline matrices, 68 MARIO inputs, 68 reference inventories and 67 regenerated workbooks were byte-identical to the run records. A subsequent check after reopening confirms unchanged baseline bytes and unchanged worksheet/value parts and original workbook relationships in every Excel file. Cloud-side packaging added or updated metadata/custom-XML relationships in 203 Excel containers; those hash changes do not represent numerical edits. The local preserved snapshots retain their original bytes. All 28 tests pass in the pinned producer environment. A real ZIR export through the relocated inputs reproduces 14,739 coefficient, 163 output and 1,805 trade records exactly; its technical record is saved outside the inventory folder. Future full runs use date/time output folders and local ignored build directories for coefficients and diagnostic reports. Single-sector export likewise keeps evidence separate.

The final local tree has 552 files, a longest absolute path of 384 characters and no candidates from the checked reserved-character, 255-character segment and 400-character local-path screens. Two long ICCS filenames and two MARIO filenames with reserved punctuation were shortened; readable workbook bytes are unchanged. This local screen is not certification of SharePoint's server-side paths or successful cloud sync.

OneDrive was reported closed or blocked. Seven source files initially timed out: `New sectors classification.xlsx`, `Shared sources.xlsx`, `GTAP_energy_prices.xlsx` and four Purdue Livestock CSVs. After a command to reopen OneDrive, **all seven became readable** and were hashed and inspected. Remote synchronisation is still unconfirmed.

`GTAP_energy_prices.xlsx` contains average basic energy prices in domestic absorption, USD/toe, in separate 2017 and 2023 sheets. `Shared sources.xlsx` is a reference/link index. The Livestock files contain bilateral trade and output (million USD), feed use (tonnes) and emissions (ktCO2e), on a 160-region source geography. They are distinct supporting datasets, retained in place; they are not automatically merged into the current D2.4 workflow.

The now-readable working `New sectors classification.xlsx` is **not the published workbook** used to initialise the registry. Its main catalogue has 187 rows versus 181 in that published snapshot. It contains seven additional codes (`?`, `CPH`, `FCH`, `ISC`, `QRZ`, `XNM`, `XOM`), while `XOO` appears only in the published catalogue. Three common codes have changed descriptions (MGC, NMX, PGM); no common-code parent change was found. Its split flag also differs conceptually from the published deliverable field. The unified view therefore includes this working catalogue and its CPC/NACE/ISIC declarations separately, without silently replacing published identities or treating the placeholder `?` as a valid new sector.

### Full D2.4 inventory regeneration

Run `D24-20261001` started on 1 October and completed on 2 October 2026 at 06:34 UTC. It executed steps 1–5 of `scripts/run_d24_pipeline.py` from public commit `d23e531b580450c7a08c29dd55be52bc33752141`. Only the two output destinations were replaced; the optional final QA plot was omitted. The native call remained `add_sectors(split=False, VA_fix=True, accept_non_unitary_sum=True)`. No MARIO engine, method or numerical setting was changed for this run. Hashes of the installed insertion engine, workbook reader and database API still match the prepared producer environment after completion.

The workflow read the original GTAP flow database and normal `MARIO inventories` directory, calculated fresh coefficients, saved and reloaded a new coefficient database, exported the workbooks and replaced their trade sheets with May13 `NTSCIF` using the existing runner. Previously archived D2.4 coefficients were not used as the calculation source. Experimental attempts were discarded and are excluded from these results and from the shared run archive.

**67 new workbooks cover all 67 distinct released sector codes.** The 68-file operational reference contains two MUN workbooks; both were compared with the single regenerated MUN. The empty BF-BOF natural-gas-injection source has no inventory sheet and was skipped by the existing workflow; it is not an omitted released sector. The normal MARIO inputs were used unchanged, including their existing geography. The earlier HYE/MRT pilot was not substituted into this run.

| Verification | Result |
|---|---|
| Workbook integrity | All 67 ZIP containers and worksheets read successfully; no Excel error cells, uncached formulas, missing Master sheet links or duplicate numeric keys. |
| Coefficients | 840,203 keyed records; no changed, added or removed keys against either applicable reference; maximum absolute difference 0. |
| Total outputs | 9,830 keyed records; same keys and values; maximum absolute difference 0. |
| Bilateral trades | 90,332 keyed records; same keys and values; maximum absolute difference 0. |
| Coverage | No missing or unexpected sector codes. All 68 operational reference files were readable. |
| Source preservation | All 147 data/reference files and the repository matching workbook retained their recorded SHA-256 hashes. |

The reference for this comparison is the operational D2.4 folder transferred from POLIMI/eNextGen into project SharePoint. The earlier section documents its relationship to Zenodo; this run did not download Zenodo again. Comparisons align records by database identity, unit, region and change type, rather than Excel row position or display labels. Comparison tolerances were relative `1e-10` and absolute `1e-12`; the observed maximum difference was zero for every numeric category.

Three metadata differences reproduce the current exporter's historical mapping overrides: **BVL: OTP → MVH; MSI: OXT → CHM; SOP: EEQ → ELE**. MARIO insertion still uses the source Master definitions, while the exporter resolves parent metadata through `GTAP12_matching.xlsx`. These overrides do not establish a newly reviewed NACE parent or a recalculation under the displayed parent. They remain a mapping-consistency issue to resolve separately.

Existing numerical diagnostics are preserved: **2,017 of 9,830 regional monetary profiles** fall outside `1 ± 0.01`, excluding satellite rows; 7,161 coefficient values are negative; 21 sectors have empty final trade sheets. Negative values are diagnostic observations, not automatically errors. Exact reproduction shows that these values were already in the reference. The earlier published-package count of 2,007 distinct sum warnings excluded ZIR; its ten warnings account for the difference. The native `export_d24_report.txt` describes preliminary June1 trade coverage before replacement; final trade coverage is recorded separately in `verification_summary.json`. A read-only HYE preview confirms rendering but retains the native narrow columns, which clip some labels and numbers. No workbook formatting was changed.

The run's current shared location is `Data split/Inventory generation/Inventories/20261001`: 67 files named by sector code, such as `HYE.xlsx` and `ZIR.xlsx`. Its fresh coefficient database, executed pipeline, environment/source hashes, comparison results, warning details and copy manifest have moved to the private eNextGen `Inventory archive/Regeneration 20261001`.

All 95 files (approximately 1.24 GB) were hash-verified during the original run transfer; `archive.json` retains its historical paths. The reorganisation manifest records subsequent moves. The date in the inventory directory is the run start date. No original inventory or database was overwritten. Remote SharePoint synchronisation has not been independently confirmed. Local execution evidence remains in ignored `build/rebuild_d24_2026-10-01/`.

This completes regeneration of the D2.4 inventory package with the original MARIO behaviour. It does not certify a balanced split MRIO: `split=False` was retained, existing data warnings were not corrected, and the supplied GTAP baseline was not repaired.

## The release reference

The D2.4 report, dated 30 June 2026, cites concept DOI `10.5281/zenodo.20592035`. At retrieval this resolves to the versioned record [10.5281/zenodo.20592036](https://zenodo.org/records/20592036), published on 30 June 2026. Its record was last updated on 7 July 2026; that metadata date alone does not establish whether files changed.

| Property | Verified value |
|---|---|
| Archive | `D2.4 Data Inventories.zip` |
| Size | 41,027,273 bytes |
| Zenodo MD5, independently matched | `0bdd89a38b3a882c89051795d622caeb` |
| Independently calculated SHA-256 | `c137eb656d950abba678c01f59b1ec45d14eb9d0af2784d081cf584d82ad147e` |
| Contents | 68 inventory workbooks and `New sectors classification.xlsx` |
| Readable inventory workbooks in the original archive | 67; ZIR has since been recovered separately without replacing the published file |
| Distinct sector identities | 67 including recovered ZIR; the original readable-only audit covered 66, with MUN present twice |

The [published release manifest](../../manifests/d24_published_release.json) records each member's hash, its parse status, and the fixed download URL. The original downloaded ZIP remains unchanged under `build/audits/d24_baseline_2026-10-01/`.

The dataset metadata records `CC-BY-NC-SA-4.0`. The PDF report has a separate CC-BY-4.0 statement. Code, report, inventory data and licensed GTAP inputs must retain their respective provenance and licence metadata; the report's statement is not used as the inventory dataset's licence.

## What has been preserved

The [candidate source manifest](../../manifests/d24_source_candidates.json) records 193 captured files, using paths relative to the shared ENTICE root. All 193 were successfully read and copied into a local evidence snapshot. They comprise:

- 36 partner workbooks, 68 MARIO intermediate workbooks and 68 SharePoint D2.4 workbooks;
- four existing audit reports and two manual-check/startup files;
- 11 selected Purdue inputs covering May13, May27 and June1;
- the D2.4 report and signed grant agreement;
- `X.parquet` and `units.parquet` from the baseline `2023entice` database.

The snapshot also preserves the available ENTICE Git revisions, the pre-existing working changes, current inspected modules and mappings, and MARIO/CVXLAB repository states. These are **candidate sources**, not a claim that the captured working copy is the original delivery environment.

Two existing audit CSVs changed modification time during capture after initially being cloud-only. Their captured bytes subsequently matched a fresh read of the source files. The original metadata-change flags remain in the manifest; they are not silently treated as proof of a content change.

Large evidence files, source data and numerical audit reports are in the already ignored `build/` directory. The manifests and this report can be versioned without adding those payloads to Git. The GTAP totals workbook is supplied through the private shared archive and excluded from public Git history. Original input data and source workbooks remain unchanged. Subsequent changes added workbook recovery, a single-sector export command, atomic exporter saves and visible Python warnings; these are described below. Redundant Markdown reports have been consolidated here. The reconstruction and registry work is committed for integration; no data release has been published.

## Reconstructed data chain

```mermaid
flowchart TD
    P[Partner templates] --> T[Template importer]
    E[Purdue EXIOIOT and output targets] --> I[EXIOIOT importer]
    C[Purdue copper costs and mappings] --> K[Copper importer]
    T --> M[MARIO intermediate inventories]
    I --> M
    K --> M
    G[GTAP output weights and mapping tables] --> T
    M --> A[MARIO coefficient insertion and factor completion]
    B[Licensed GTAP baseline] --> A
    A --> D[D2.4 coefficient database]
    D --> F[Regional inventory export]
    M --> F
    S[May13 NTSCIF bilateral trade data] --> F
    F --> Z[Published D2.4 inventory package]
    Z --> U[User runs split and optimisation with MARIO and CVXLAB]
```

This separates inventory production from the subsequent balanced database disaggregation. The committed D2.4 builder and current runner call `add_sectors(split=False, VA_fix=True, accept_non_unitary_sum=True)`. The public example calls `split=True`. Finding optimisation constraints in MARIO therefore does not show that they were executed during the D2.4 inventory export.

| Stage | Available evidence | What is established |
|---|---|---|
| Partner collection | `Partner inventories`, original ancillary material, `template_checker.py` | Inputs include cost profiles, regional output observations, sources and mappings. Layout and naming remain heterogeneous. |
| Template processing | `template_to_inventory.py`, region clusters, matching and GTAP totals | Maps inputs, creates coverage profiles, estimates/caps output, and can append residual input clusters. Some implemented rules diverge from comments/report; see checks. |
| Purdue processing | EXIOIOT/COPCOSTS, `splttargs.xlsx`, mappings | Current importers map cost items, aggregate and normalise cost structures, and read output targets. Current copper code is untracked at capture and absent from the last committed ENTICE revision. Its delivery-time provenance remains open. |
| Intermediate inventories | 68 `Add_sector_*.xlsx` files | Provide an operational, pre-export layer. They already contain target-specific transformations and are not raw observations. |
| Coefficient construction | D2.4 builder, MARIO insertion/factor code | Uses the GTAP baseline with `split=False`; parent-derived coefficients and factor completion can affect resulting inventories. |
| Final coefficients | Exporter's `aggregate_sector_coefficients` | Aggregates intermediate-input coefficients over supplying regions, retains producing regions, and exports factor/satellite rows separately. Input origin becomes `GLOBAL`. |
| Final output targets | Intermediate `Total outputs` and published workbooks | For every readable published workbook, all shared regional output values and unit labels exactly match the corresponding intermediate workbook. Export may omit regions without rendered inventory rows. |
| Final trade targets | May13 `trade.xlsx`, sheet `NTSCIF` | All 46 readable published files with trade rows exactly match this source after the exporter's sector/region/zero filtering. The other 21 readable files also match its empty result. The 46 files include both MUN copies. |
| Published release | Versioned Zenodo ZIP | Hash-verified distribution reference, including its defects and duplicate files. |

### The GTAP reference

The captured baseline output matrix contains 163 regions and 76 sectors, or 12,388 region-sector observations. Every `GTAP12_X.xlsx` entry matches `2023entice/X.parquet` within an absolute difference of `1e-8`; the maximum observed difference is approximately `9.31e-9`. This supports using that workbook as the output reference for this audit.

The original audit did not load or recompute the full baseline matrices. The subsequent ZIR export read the required columns from saved D2.4 coefficients and recorded original-file and projected-file hashes. The later [full inventory regeneration](#full-d24-inventory-regeneration) recalculated all 67 sectors from the supplied baseline and MARIO sources; balanced split acceptance remains unverified.

## Project folder versus Zenodo

The additional folder inspected is `RCD-Entice-EXT - Documents/General/2.Deliverables and Milestones/WP2. Improved data and empirics on trade and climate/D2.4 - Enhanced GTAP database (M18)/D2.4 Data Inventories`. Its sibling `New sectors classification.xlsx` was also inspected.

- All 67 readable inventories match the published sheet names, cell coordinates and cached values.
- The classification workbook also matches those values.
- These 68 readable files differ in their container bytes; file dates alone do not establish numerical changes.
- ZIR is byte-identical to the unreadable published ZIR.
- Refreshed [Zenodo record 20592036](https://zenodo.org/records/20592036) still reports the same archive checksum and size as the preserved download.

The captured files, cell-level comparisons and refreshed metadata are under `build/audits/d24_followup_2026-10-01/`. This comparison does not assert equality of formula expressions, formatting or all Excel objects.

The original POLIMI/eNextGen D2.4 folder was also captured: all 67 readable published workbooks match its sheet names, cell coordinates and non-empty cached values, although all 68 inventory file hashes differ. Its readable ZIR copy was subsequently compared with the recovered published file and has the same cached values. Neither shared source folder has been overwritten.

## Why ZIR failed and what was recovered

The XLSX is a ZIP container. Its 194 local file entries are complete and pass their CRC and uncompressed-size checks. All XML parts parse and their internal relationship targets exist. The central directory begins at byte 805,588, but the file ends at byte 809,758, in the middle of that directory, without an end-of-directory record.

`scripts/repair_xlsx_directory.py` rebuilt the directory while preserving the original local headers and compressed payload bytes. The recovered file is 820,377 bytes and opens with 171 sheets. Every workbook part is unchanged; its cell values also match the previously preserved POLIMI/eNextGen copy. This is container recovery, not a recalculation or replacement with guessed data.

The exact operation that truncated the file cannot be identified from its bytes. An interrupted save, copy or synchronisation is possible. The verified outer Zenodo ZIP contains this damaged payload, and the project folder contains the same bytes: the defect is not explained by a bad local download alone.

The recovered workbook and its per-part recovery manifest are now preserved in the private eNextGen archive:

```text
Inventory archive/ZIR recovery/2026-10-01/
  ZIR - Manufacture of refined zinc.xlsx
  ZIR - Manufacture of refined zinc.recovery.json
```

This is a reviewable recovery candidate. Publishing a replacement or a new Zenodo version remains a separate release action.

## MUN and identity management

Both MUN files contain the same sector code, description, NFM parent, regional coefficients, output and trade. Their `DB units` catalogues differ: the filename without the comma contains 127 sectors; the filename with the comma contains 143. The latter has 16 additional sector entries. Consequently, the files are not identical apart from their names.

The historical exporter constructed output filenames from the intermediate filename's descriptive text and did not remove previous filenames. The current exporter uses stable sector-code filenames and new run directories. That historical naming behaviour could leave two MUN files after a description changed. The different unit catalogues support different database/export states; the exact rename event has not been recovered. There is no evidence here of two different intended MUN activities or competing MUN parents.

Use one stable sector identity, keep alternate names as aliases, and create each release in a fresh output directory. For this baseline, the comma version's catalogue is consistent with the 143-sector database used in the single-sector trial. The original files remain preserved; no silent deletion has been made.

NMC and NCM require more care: their published parents are OME and EEQ respectively, and 14 of 162 common regional outputs differ. They are not interchangeable duplicate files. PLSR appears to be a legacy spelling of catalogue code PLS, but that inference is not evidence that either activity was withdrawn.

## NACE-led parent definitions

The review uses **NACE Rev. 2**, matching the delivered classification's version, with product detail where a broad activity name is ambiguous. NACE Rev. 2.1 is a distinct version and must not be substituted implicitly. Target parents follow a versioned NACE–ISIC–GTAP bridge. [Eurostat version guidance](https://ec.europa.eu/eurostat/web/nace) and the [official GTAP GSC3 concordance](https://www.gtap.agecon.purdue.edu/databases/contribute/concordinfo.asp) establish this basis.

The [review table](../../data/classification/d24_nace_review.csv) records all 67 published identities, preserves duplicate catalogue rows, and gives 24 targeted scope determinations. Untargeted rows are explicitly not certified at class level. This table is review evidence, not a new silently active production mapping.

| Activity | NACE Rev. 2 scope | Appropriate GTAP parent | Finding |
|---|---|---|---|
| BVL, light-duty motor vehicles | 29.10 | MVH | Published OTP is incorrect for this activity. |
| MSI, silicon | 20.13 | CHM | Published OXT is incorrect; HS 280469 identifies silicon, not extraction. |
| SOP, photovoltaic components/modules | 26.11 | ELE | Published EEQ is inconsistent with this scope. |
| AGT, artificial graphite | 23.99 | NMM | Published parent is appropriate; competing CHM catalogue/NACE entries must be reconciled. |
| MGC, magnesite and the listed magnesia products | 08.99 | OXT | Official product detail includes the processed magnesia forms; the two name variants are an identity issue, not evidence of a second parent. |
| PCP, coke | 19.10 | P_C | Both matching rows agree on the parent; different source aliases should be separate from the sector registry. |
| NMC/NCM, batteries | 27.20 | EEQ | NMC's OME is inconsistent with battery manufacture; selection/alias history remains distinct from classification. |
| GAR, gallium metal | 24.45 | NFM | Chemical-parent/source assumptions conflict with the stated metal and HS scope. HS 811292 also covers other metals and requires a narrower product allocation. |
| WNT, turbines and turbine-generator sets | 28.11 | OME | Distinguish these from separate electrical generators, 27.11 → EEQ; WNT is currently reused for both names. |

The silicon determination is supported by the [official silicon product entry](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=intcom%3AC%282021%298413). Artificial graphite is explicitly classified under CPA 23.99.14 in the [official product list](https://eur-lex.europa.eu/eli/reg/2019/1933/oj/eng). [NACE explanatory notes](https://sfc.ec.europa.eu/system/files/documents/sfc2007/2022-10/nace-rev-2.pdf) distinguish turbines, generators, secondary-metal production and materials recovery. [The 2022 product classification](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2552) supplies detail for magnesia and photovoltaic/chemical products.

Other important scope findings:

- ZIR's HS 281700 covers zinc oxide/peroxide, with CPA 20.12.11: CHM is appropriate for that chemical scope. Zinc metal would instead require NACE 24.43 and NFM. COR, MNR, TIR and other misleadingly named refined-material inventories also use chemical-product trade definitions. Names must state that scope.
- PLR/RAL/RCP cannot inherit a manufacturing parent just because their recovered material is plastic/aluminium/copper. Materials recovery at 38.32 maps to WTR; actual secondary-metal manufacture maps to NFM. Products made from recycled material and recovery services must not be merged or double-counted.
- PLP needs a product definition: plastics in primary forms, 20.16 → CHM, differs from finished plastic products, division 22 → RPP. PLSR/PLS similarly needs an activity definition in addition to an alias decision.
- Several vehicle concordance entries include both divisions 29 and 30, even though ordinary road vehicles belong in 29. RER combines metal and compound trade categories; a single parent cannot be assigned by ignoring that difference.

These are categorical rules for defined activities, not requests to choose a convenient parent. Where a source mixes activities, the remaining work is to separate or explicitly delimit its scope, then rebuild target-dependent quantities and coefficients.

### Implemented canonical registry

The registry has three files with separate responsibilities:

| File | Role |
|---|---|
| [sectors.json](../../data/registry/sectors.json) | 88 stable records: the 67 published codes plus 21 catalogue-only codes that remain inactive. Namespaced source aliases, NACE version and activity scopes, related-but-unmerged records, evidence references. |
| [gtap12.json](../../data/registry/gtap12.json) | Versioned target adapter. NACE rules determine parents. Published parents, matching rows, declared concordances and file hashes are retained as historical evidence. Rebuild dependencies are explicit. |
| [regions.json](../../data/registry/regions.json) | 163 GTAP region codes/names and 32 explicit groups from the common region reference. These are GTAP geographic units, including aggregates, not an ISO country list. `GLOBAL` must contain all target regions exactly once. |

The [Python API](../../src/entice_inventory/core/registry.py) and [CLI](../../scripts/registry.py) read these files directly. Identity resolution requires a namespace for source aliases. Shared source labels such as `XCH_BPH` cannot silently select one sector. Both MUN filenames resolve to MUN; NMC/NCM and PLS/PLSR remain separate related records. Catalogue absence does not establish withdrawal and querying an entry does not activate it.

The registry carries the previous 24 targeted definitions plus HYE: hydrogen is PRODCOM 20.11.11.50, under NACE Rev. 2 20.11 and ISIC Rev. 4 2011, hence CHM in the reviewed GTAP bridge. This follows the [official product classification](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32022R2552) and [NACE notes, printed page 140](https://sfc.ec.europa.eu/system/files/documents/sfc2007/2022-10/nace-rev-2.pdf). The electrolysis/steam-reforming distinction remains important for source profiles even though both activities belong to the same class.

Of the 67 published records, 18 currently yield a parent for a defined scope, seven require scope resolution and 42 remain unreviewed at this level. The 21 catalogue-only records also remain unreviewed. A missing determination returns `parent: null` with a reason, never the old parent as a fallback. Conditional scope selection is exposed as conditional, not treated as certification of its observations. Five resolved parents differ from the release: BVL, GAR, MSI, NMC and SOP. Source/name alignment warnings remain separate from parent changes. EXIOBASE has no adapter yet.

Diagnostics are optional and produce structured warnings with identifiers, source records, observations, references and suggested actions. Skipped checks are listed. Invalid data structure, unreadable workbooks and ambiguous identity requests are technical failures, not successful validations. All 68 preserved MARIO workbooks have been inspected read-only with the new checks; detailed findings are in `build/registry/inventory_diagnostics.json`. These warnings do not themselves establish that incomplete coverage is an error for every sector.

**Integration boundary:** the template importer now uses the canonical geography. Existing importer/exporter parent lookups still use the historical matching workbook; switching all of them without rebuilding dependent coefficients would be misleading. New code can obtain NACE-derived parents directly from the registry. The old review CSV remains preserved evidence and must not be maintained as a competing live mapping. Usage is in the repository README.

### Mauritania: cause, correction and verification

The common `Regions_clusters.xlsx` contains MRT at `Sheet1!A142:G142`, including GLOBAL membership. The preserved partner HYE template's internal `Region` reference table omits MRT entirely. The old template importer built its target universe from that internal list, propagating the omission to GLOBAL, synthetic producing-region coverage and Total outputs. This is not evidence of a deliberate geographic exclusion.

The importer now takes its target region universe from the canonical registry and warns when a partner reference list is incomplete. A private HYE regeneration now covers all 163 regions in GLOBAL and Master expansion, and includes MRT in Total outputs. Its output is approximately **0.00417905 M USD**, generated by the existing median-ratio estimation rule. The row explicitly identifies the method and source and states that it is an estimate. No new Mauritanian production observation was found. The conflicting HYE Summary description remains visible as a separate warning.

The read-only scan found MRT as the sole missing GLOBAL member in **24 of the 68** preserved intermediate workbooks. Eight others omit XWS (Rest of Western Asia); the remaining 36 have complete GLOBAL membership. Correction must be applied through source regeneration and coefficient reconstruction, not by editing the published GLOBAL list alone. Only the HYE intermediate has been regenerated as a verification candidate in this step; this does not certify a new D2.4/HYE final workbook. Original partner, intermediate and common-region reference hashes remain unchanged. Evidence and the private candidate are in `build/registry/hye_verification.json` and `build/registry/hye_candidate.xlsx`.

Verification covers the registry's identity/scope resolution, ambiguous aliases, invalid parents, NACE versions, skipped checks, geography integrity and read-only workbook diagnostics. The repository's 20 tests pass, including the existing producer/recovery checks. A separate HYE source regeneration exercises the real importer and verifies full coverage, the MRT estimate and unchanged source hashes. A built wheel was installed in an isolated target directory and successfully loaded the bundled registry from outside the checkout. This is not a full MRIO rebuild.

## Production and trade consistency

The original numerical audit covers 67 readable published workbooks, excludes the then-unreadable ZIR, and includes both MUN files unless explicitly deduplicated. Recovery has not silently expanded these historical counts.

In the inspected producer, there is no dedicated pre-export check that compares the sum of a commodity's exports against its total output. `build_trade_rows` filters diagonal, negligible and out-of-coverage trade rows, but does not compare trade with production. The subsequent May13 trade replacement also performs no production feasibility check and does not refresh the earlier export report.

MARIO's split implementation validates split metadata and quantities, checks new output against parent output and checks for negative residual parent output. Its CVXLAB model then constrains total supply/use and observed bilateral trade jointly. In the inspected `model_settings.xlsx/problem`, these are the production/column constraints and the trade constraints labelled 2, 3 and 4. These are optimisation constraints, not a separate diagnostic explaining incompatible trade/output inputs.

The D2.4 builder invokes `split=False`; those split/optimisation checks do not validate the exported package during that producer run. The public consumer example invokes `split=True`, so inconsistent targets can surface later, when a user attempts to solve the model.

For a commodity produced in region r, under a common valuation and scope and non-negative domestic allocation:

```text
sum of observed exports from r <= total output in r
```

This is a useful necessary-condition screen, not a universal rule for unharmonised customs data. Re-exports, CIF versus domestic producer valuation, trade margins, commodity/activity scope and different reference years must be reconciled first. Negative inventory changes can also affect simple non-negativity assumptions. Solver tolerances need to be applied in the direction of the actual model inequalities before claiming infeasibility.

`output + observed imports - observed exports` is recorded as a descriptive diagnostic. Imports may be incomplete, so a negative value is not by itself proof of negative actual domestic consumption. Global exports equal global imports when summed from the same bilateral table by construction; that identity cannot independently establish consistency with production.

### Observations in the published package

- 2,606 workbook-region entries have observed exports above output at the audit threshold; this is 2,575 distinct sector-region pairs after removing the duplicated MUN observations.
- Of these distinct pairs, 1,768 have reported output equal to zero and positive observed exports.
- Example: AGT/BEL has output 8.1212720871 M USD and observed exports 9.5301914814 M USD. Both values were independently checked with openpyxl.
- The numerical trade source is May13 NTSCIF, explicitly labelled CIF imports scaled to GTAP. Matching unit text `M USD` alone does not establish equal valuation.
- All final trade endpoints are inside the exported coverage because the exporter filters them. The absence of endpoint errors does not show that no source flows were discarded.

These are screening flags for review, not 2,575 confirmed data errors. The audit records observations without modifying them.

## Existing checks and their execution

| Check or behaviour | Implementation | Existing execution / limitation |
|---|---|---|
| Sector, region and factor cluster membership | `template_checker.check_*_clusters` | Returned as issues by the parser. The personal runner can block on selected lists, but `perform_checks=False` in the captured runner. |
| Unit-process identifiers and mapped inputs | `check_unit_process_region_names`, `check_unit_process_inputs` | Same optional runner gate. These checks do not establish economic correctness of a mapping. |
| Monetary profile selection | `read_unit_process` | Always applied during parsing; non-monetary profiles are discarded with warnings. |
| Monetary coefficient sum | `read_unit_process` | Tolerance `1e-3`; non-unitary regional profiles can be discarded, all-zero profiles kept with warnings, GLOBAL retained as fallback. The runner's blocking list omits `unit_process_columns`. |
| Production-region identifiers | `check_total_production_regions` | Optional runner gate. |
| Production against GTAP parent | `check_total_production_vs_gtap` | Only computed when `gtap_path` is supplied. The generator calls `parse_template` without it. The optional runner prints violations but does not include them in its `all_ok` decision. |
| Coverage gaps | `check_missing_regions` | Returned/printed for diagnosis; not a comprehensive mandatory acceptance gate. |
| Missing/non-numeric production | `read_total_production` | Converted to `0.0`; this is a transformation, not successful validation. Non-zero GLOBAL production rows are skipped. |
| Cluster-level production allocation | `template_to_inventory.make_inventory` | Comments and D2.4 section 3.5 describe allocation by parent output. In both HEAD and the working copy, the detected `_matched_cl` is not used in the output-resolution loop; execution falls through to median estimation. Requires reconciliation. |
| Individual production cap | `make_inventory` | Caps some template-derived direct values against parent output; no equivalent full sibling-envelope gate is established for the producer. |
| EXIOIOT/COPCOSTS input resolution | Their importers | Missing mappings, zero-total cost structures and missing regional cost coverage can raise errors; malformed/near-zero input rows may be skipped and surviving coefficients normalised. |
| Residual input shares | `apply_residual_sector_clusters` | Rescales existing rows and appends an input cluster; the captured runner requests 1%. This is a methodological modification, distinct from the residual parent sector after splitting. |
| MARIO factor completion | `add_sector_engine`, `VA_fix=True` | May add parent factor values and rescale inventory rows. With `accept_non_unitary_sum=True`, non-unitary inventories proceed with warnings and zero-total inventories are skipped. |
| Split quantity/schema validation | `add_sector_split.normalize_split_info` | Invoked in the split workflow, not the D2.4 `split=False` exporter. Negative checks do not constitute complete numeric validation because coercion to NaN is not itself rejected there. |
| Individual and combined output envelope | `add_sector_split.build_split_scenario` | Individual child-parent comparison and rejection of negative residual parent output. Conditional on running the split stage. |
| Missing versus zero bilateral trade | `cvxlab_bridge` and `Trade_selector` | Missing values in an internal dense table become zero, but selectors activate only explicitly supplied trade rows; absent observations are not automatically imposed as zero constraints. Upstream export discards explicit near-zero rows, so their original meaning cannot be recovered from the release alone. |
| Joint output, trade and accounting constraints | CVXLAB `Split_sectors/model_settings.xlsx` | Enforced when optimisation runs; infeasibility or success is not a substitute for interpretable preflight checks and post-solve residual reports. |
| Solver outcome | `optimize_split_in_cvxlab` | Checks solver status before loading results. No delivery-time solver log was found. |
| Missing trade, empty inventories, coefficient sums | Exporter's `write_export_report` | Text report, not a release-blocking gate. Its sum checker includes all written rows, including satellite accounts with different units. |
| Parent label comparison | `plot_d24_split.check_parent_consistency` | Diagnostic function exists; not invoked by the end-to-end runner. |
| X/VA split charts | `plot_d24_split` | Uses selected/mixed sources, can substitute zero for missing VA, and clips plotted residuals with `max(parent - children, 0)`. Charts do not certify non-negative regional residuals or solver feasibility. |

Relevant production files are under [inventory](../../src/entice_inventory/inventory/), [export](../../src/entice_inventory/export/), [core](../../src/entice_inventory/core/), and [the runner](../../scripts/run_d24_pipeline.py). Dependency code inspected is preserved in the local source snapshot, with Git revisions in the candidate manifest.

## Independent consistency results

| Audit | Result | Scope and interpretation |
|---|---|---|
| Output lineage | No changed values or unit labels on common regions | Applies to readable published files matched by code to one intermediate inventory. Regional omission is listed separately. |
| Catalogue consistency | BVL, MSI and SOP parent conflicts; NMC/PLSR missing | Compared with the classification included in the same release; do not silently relabel output in this audit. |
| Current runner lookup | PCP and MGC ambiguous | Current matching contains multiple rows for these codes. |
| Intermediate metadata | AGT Master/parent disagreement in 163 rows | Summary and Master are not consistent. Current parent overrides may conceal the historical discrepancy. |
| Intermediate completeness | SGI has no regional inventory sheets | The current exporter skips it; absence must remain visible in release coverage. |
| Monetary sums | 2,051 of 9,830 parsed regional sheets outside 1 ± 0.01 | 2,007 distinct sector-region profiles after removing the MUN duplicate. Satellites are excluded. This is an independent screening result, not the exporter's mixed-unit sum. |
| Individual output envelope | 23 entries exceed parent at the strict audit threshold | 14 exceed the parent by more than 0.01%; the rest need precision review. Reference output workbook matches the captured baseline X matrix. |
| Combined output envelope | 44 parent-region groups exceed the envelope | Uses declared published parents; both ambiguous MUN copies are omitted and ZIR was excluded from this original audit. Thus it is incomplete. Alias conflicts and parent disagreements also affect interpretation. |
| Original template checker | All 36 workbooks parsed; 33 produce at least one diagnostic | Includes unused/example cluster definitions and warnings; do not interpret every diagnostic as a defect in a delivered sector. |
| Production header layout | Six templates have repeated `2023 Value` headers | The current parser takes the last exact match and defaults the unit column to H if `2023 Unit` is absent. This needs explicit disambiguation. |

The strict output/trade screen uses `max(1e-8, abs(output) * 1e-8)` as a numerical comparison allowance. This is an audit threshold, not a calibrated economic tolerance or a substitute for the solver's tolerance settings.

Examples of material individual-envelope flags are CPP/COD (about 1.2401 times its declared parent's output) and TIR/MOZ (about 11.5199 times). Their cause is not assigned by this audit. The current producer's template cap cannot be assumed to protect all source pipelines.

The original checker returned 247 unit-process-column diagnostics, 62 production-versus-parent violations, 21 unresolved production-region references, and other mapping/cluster issues. Detailed per-file records are preserved in `template_checks.json` and `template_issues.json`. The template layout scan found no formula errors or uncached formulas in the columns selected as 2023 output values; that does not validate the selected columns' meaning or units.

## All-sector split-readiness audit: 12 October 2026

The owner requested work towards `split=True` across **all sectors and regions**, without changing production code. The audit uses the 67 regenerated inventories under `Inventories/20261001`: ZIR is included and MUN is counted once. It also reads the 68 preserved MARIO inputs, all 36 partner templates, both Purdue output/trade deliveries currently selected by the producer, the canonical registry and the full native GTAP parquet cache. No source observations, targets, inventories, mappings or GTAP matrices were changed; no solver was run.

The principal review views are the [67-sector dashboard](../../build/audits/split_readiness_2026-10-12/sector_dashboard.csv), [12-parent dashboard](../../build/audits/split_readiness_2026-10-12/parent_dashboard.csv), [issue register](../../build/audits/split_readiness_2026-10-12/issue_register.csv) and [machine-readable summary](../../build/audits/split_readiness_2026-10-12/summary.json). Numerical evidence and one-off analysis scripts stay in ignored local `build/`; they are not a release or new production implementation.

### Current coverage and numerical findings

| Check | Current result | Interpretation |
|---|---|---|
| Coverage | 67 sectors, 12 declared parents, 9,830 regional profiles/output targets, 90,332 bilateral trade rows | Covers the entire regenerated release. Catalogue-only activities are not activated. |
| Individual output envelope | 23 sector-region flags across 13 sectors | Four have a relative excess at most `1e-6`; they still require provenance review before being called rounding. The comparison uses the native recomputed parent output. |
| Joint output envelope | 39 parent-region flags | NFM 12, CHM 9, OXT 9, RPP 5, MVH 2, NMM 2. All children of each parent are included once. |
| Parent-label sensitivity | 44 joint flags if the same final values are grouped under intermediate Summary parents | The difference from 39 reflects metadata choices, particularly BVL, MSI and SOP; it does not establish a numerical correction. Historical audit exclusions/duplicates are separate. |
| Observed exports versus output | 2,623 sector-region flags at the adopted `1e-6 M USD + 1% × output` review threshold | 2,647 at the strict legacy threshold; 2,605 remain at 5%. CIF/scope/re-export comparability must be resolved before calling these infeasible. All 46 sectors with final trade contain at least one policy-threshold flag. |
| Zero output and positive observed exports | 1,788 sector-region flags | 1,167 EXIOIOT, 617 template/unspecified and four COPCOSTS cases. These are written zeros, not proof of observed zero production. Sparse source omissions remain distinct. |
| Monetary coefficient sums | 2,017 of 9,830 profiles outside `1 ± 0.01`, across 61 sectors | Satellite rows are excluded; no normalization is imposed by this audit. |
| Bilateral parent envelope | 5,164 flags among 44,434 observed parent/origin/destination comparisons | Conditional comparison of summed child trade with parent `Z + Y` by destination. CIF targets and GTAP flows are not yet on a certified common valuation/scope. |
| Implied intermediate/factor use | 18,859 flags among 144,038 parent-region-input comparisons | Conditional on exact supplied coefficients, exact output, nonnegative residuals and conservation of aggregated parent flows. These do not prove infeasibility of an optimizer that can adjust the profiles. Signed factors are not subjected to a blanket nonnegative-residual test. |
| Trade provenance | Every final trade table exactly matches the filtered May13 NTSCIF source | 21 sectors have no final trade observations. CPP, CPS, LIT and REE retain June1 child-specific trade candidates; no source union or composite-code allocation is applied. Origin/destination follow the exporter interpretation, pending independent source-axis confirmation. |
| Output provenance | All common intermediate-to-final output values are unchanged | The exporter omits 1,060 intermediate regional rows across 24 sectors. The missing rows and discarded trade flows remain in evidence rather than being presumed zero. |

[Output checks](../../build/audits/split_readiness_2026-10-12/output_checks.csv), [joint parent checks](../../build/audits/split_readiness_2026-10-12/parent_region_checks.csv), [trade/output checks](../../build/audits/split_readiness_2026-10-12/trade_output_checks.csv), [bilateral checks](../../build/audits/split_readiness_2026-10-12/bilateral_parent_checks.csv), [conditional input checks](../../build/audits/split_readiness_2026-10-12/fixed_profile_input_checks.csv) and [source lineage](../../build/audits/split_readiness_2026-10-12/source_lineage.csv) retain coordinates, values and interpretation. Conditional diagnostics must not be aggregated into a count of confirmed errors.

### Source definitions and transformations to resolve first

The [template identity checks](../../build/audits/split_readiness_2026-10-12/template_identity_checks.csv) identify **24 of 36 templates** whose General info activity resolves differently from the filename/intermediate candidate. Examples span batteries, vehicles, chemicals and steel; some involve related aliases such as PLS/PLSR. These are metadata discrepancies requiring content review, not automatic evidence that every cost profile is wrong. General info must not silently link a template to another activity. Name-based source links remain candidates, not certified provenance.

All 36 templates embed the same numerical GTAP reference table, and it differs from the operational 2023 totals. Its year/valuation and its effect on originally collected observations need to be established. No embedded reference has been replaced. [Reference-table comparisons](../../build/audits/split_readiness_2026-10-12/template_reference_checks.csv) retain the fingerprints and differences.

Replaying the current production-column selection exposes unit risks in **30 templates with positive selected values**. Six templates contain physical or unresolved production-unit rows; one has numeric values in the selected unit field. Across raw selected rows there are 2,136 missing unit labels, 269 physical/unresolved labels, 54 currency/scale/year cases and 73 numeric unit-field values. Only 211 rows carry an explicitly recognized M USD 2023 label. None of the 36 sheets has the exact `2023 Unit` header sought by the parser, so it falls back to column H; six have repeated `2023 Value` headers, for which the parser selects the last match.

The current importer takes parsed production values without a conversion at this resolution step and writes `M USD` in Total outputs. Physical units, USD rather than M USD, EUR and 2017 monetary values therefore require explicit column selection and conversion rules before a fresh template-derived build. **This is a finding about the current templates/parser; it does not assign that cause to preserved historical intermediates.** [Unit checks](../../build/audits/split_readiness_2026-10-12/template_unit_checks.csv), [header checks](../../build/audits/split_readiness_2026-10-12/template_header_checks.csv) and [raw production states](../../build/audits/split_readiness_2026-10-12/template_production_states.csv) retain the evidence. The latter records 283 blanks that the parser turns into zero; a stored numeric zero also does not prove an empirical zero observation.

The cluster review covers 23 observations in eight activities: APS, HVC, MSI, MTH, PLP, PLR, PLSR and SOP. Direct observations, inclusive versus residual totals, overlap and units must be settled before repairing the unused allocation branch. [Cluster observations](../../build/audits/split_readiness_2026-10-12/template_cluster_observations.csv) compare their current regional targets without adopting a new allocation.

The registry still has 18 resolved parents, seven scope-required and 42 unreviewed classifications among the final 67 sectors. GAR and NMC have resolved parents differing from their regenerated workbook parents. BVL, MSI and SOP instead have source-to-final parent-label changes, which must be traced through parent-derived coefficients and caps rather than treated as completed rebuilds. AGT's intermediate Summary/Master parent conflict also remains. Among sources used by the 67 final sectors, 31 intermediates omit MRT or XWS from GLOBAL; complete GLOBAL lists in the final exporter do not reconstruct the source coefficients.

All 67 final workbooks lack the Exclusions and Tolerances sheets required by the inspected current MARIO split reader. An explicit consumer-input preparation step is needed; its schema and numerical settings must be tied to the actual dependency revision.

### Native GTAP accounting, preservation and verification

The complete 163-region, 76-sector reference contains 12,388 output observations. Native row sums reproduce stored X within the diagnostic allowance, with a maximum difference around `1.23e-8 M USD`. **10,857 columns exceed `1e-6 + 1e-8 × abs(X)` M USD** for intermediate inputs plus value added; the maximum absolute residual is approximately `0.246320 M USD`. The allowance is a diagnostic, not observed-target uncertainty. Z and Y have no negative or non-finite entries; V has 1,280 negative entries, whose account-specific signs must be preserved. [Native accounting evidence](../../build/audits/split_readiness_2026-10-12/baseline_accounting.csv) is separate from extension diagnostics; no baseline closure is applied.

Independent openpyxl checks cover a selected output, monetary profile and observed-export sum in **every one of the 67 sectors**, plus all 36 General info activity cells. Nine parent/origin/destination aggregates and nine unit/value source examples were independently checked. Summary counts reconcile with the detailed tables, and **all 187 used source files were rehashed unchanged**. The [verification record](../../build/audits/split_readiness_2026-10-12/verification.json) and [evidence manifest](../../build/audits/split_readiness_2026-10-12/evidence_manifest.json) preserve these checks. They validate extraction and aggregation, not source truth or solver feasibility.

### Production provenance and reconciliation design follow-up

The next read-only tranche provides a [decision sheet for every released sector](../../build/audits/split_provenance_2026-10-12/sector_reconciliation_decisions.csv), a [workplan for all 12 current parents](../../build/audits/split_provenance_2026-10-12/parent_reconciliation_workplan.csv), [36 template column proposals](../../build/audits/split_provenance_2026-10-12/template_selection_proposals.csv) and a [structured reconciliation design](../../build/audits/split_provenance_2026-10-12/reconciliation_design.json). These are reviewable analytical proposals, not implemented policies, regenerated inventories or solver inputs. Parent groups can change after scope review, including materials recovery; the current 12 groups are not a final classification boundary.

Reading adjacent unit fields, second header rows and formulas clarifies much of the earlier parser-unit warning. **27 of 36 templates have an explicit positive 2023 monetary-column proposal in million USD without an identified column-unit/year conflict**, including 23 of the 30 templates linked to the final release; SDG has an additional candidate with contradictory header/row units. A correct monetary column does not certify its activity, price basis or source truth. The parser's fixed H unit field remains a defect in many layouts, but its physical label does not establish that the selected numerical values are physical. For example, AMM K and HYE J convert USD to MUSD, while SCI I and MTH K already contain monetary candidates. All 209 checked AMM/HYE/CEM conversion formulas reproduce their cached values; their underlying prices are not independently certified.

| Activity/source | Concrete evidence | Proposed treatment before reconciliation |
|---|---|---|
| PLSR | Parser chooses AJ, labelled plastics production in Mt/y; E is secondary plastic products in MUSD. Final CHN 137.79 matches AJ, while E is about 37,325.27. | Review activity/alias and choose the intended monetary product column. Numeric equality identifies a source candidate, not the historical execution or the right economic scope. |
| LMO | Selected G contains 163 blanks. E has two positive values; its header says 2017 while F units say M USD 2023. Every final LMO output is zero. | Resolve the conflicting year and use supported observations; blank selection is not evidence of zero production. |
| RBR | E is blank; computed values are in F, labelled Unit, with `F = H × B` and MUSD 2017 in F2. H stores fractions despite a percent header. | Preserve the source share and old-parent derivation. A share applied to the operational parent would be a new explicit estimate, not an original observed 2023 output. |
| CEM | E uses `G × I / 1000`, with G in thousand metric tonnes and I in USD/t. | Dimensions yield MUSD; resolve price year/valuation and traditional versus CCS scope. The parser's H physical unit belongs to G, not E. |
| MSI, OXT candidate, TVP | Paired positive-row labels explicitly say USD 2023. MSI and the nonreleased mining-silicon candidate share 12 positive values. | Literal division by one million is shown only as a sensitivity. Confirm original scale and activity scope before adopting it; do not activate OXT as a new child. |
| SDG, SDH, HYS candidate | SDG I has positive MUSD row units but J2 says Mtpa; SDH has no positive monetary observation; nonreleased HYS has physical kt H2 and cost notes. | Resolve SDG's declaration conflict; keep unavailable production distinct from an observed zero; a production cost is not a certified producer sales price. |
| NCM | Fourteen monetary output values depend on external `[1]Shares` formulas, with cached values available. | Retain the snapshot and identify the external source before claiming a reproducible fresh calculation; keep NMC identity review separate. |

The PLSR and PLR monetary E columns have **26 matching positive geographic identifiers**, including cluster/GLOBAL identifiers. This raises an activity/product overlap question: a recycled product value must not automatically be used again as the output of a recovery service. [Overlap evidence](../../build/audits/split_provenance_2026-10-12/source_overlap_candidates.csv) records equality without merging or deleting activities. The six templates with no active-final candidate remain outside the released set; the broader coal-products file is not silently assigned to PCP.

[Joint output sensitivity](../../build/audits/split_provenance_2026-10-12/joint_output_sensitivity.csv) quantifies the necessary budget adjustment for each of the 39 flagged parent-region groups. Even allowing every supplied child output to fall uniformly by 1%, 5%, 10% or 20% leaves respectively **36, 34, 28 or 21 groups** above their current parent budget. These are lower-bound feasibility screens on supplied targets, not adopted uncertainty bands or optimization results. The largest required uniform downward fraction is about 92.74% in CHM, 75.02% in OXT, 55.84% in NFM, 43.61% in MVH, 16.39% in RPP and 0.112% in NMM. Source and mapping corrections may change these values; no reduction was applied.

Trade decision coverage is now explicit for all 67 sectors: 29 have retained child-code candidates in both releases, 17 in May13 only, four in June1 only and 17 in neither. This differs from the final-file coverage: 21 have no final trade, including the four June1 candidates. The per-sector decision sheet preserves the source choice, sparse output omissions, scope questions and transformations still needed. Missing routes remain unselected observations, not empirical zero trade.

**Signed value added is a model compatibility problem across all 12 current parents.** The pinned native factors contain 196 negative parent Tax observations. The inspected split model declares V nonnegative and uses `Vold >= aggregate(V) × (1 − eps)`. For a retained negative original Tax value and `0 ≤ eps < 1`, that constraint contradicts nonnegative V; all 196 original reference values also fall outside the admissible domain of the current entropy operator. [Signed-account evidence](../../build/audits/split_provenance_2026-10-12/signed_factor_checks.csv) and the [pinned model contract](../../build/audits/split_provenance_2026-10-12/split_model_contract.json) record the necessary incompatibility. This is an algebraic/input-contract finding; no optimizer was run. The bridge's optional nonnegative residue threshold zeros negative input entries, including original V/Vold, and is therefore not an acceptable preservation workaround. A later implementation must retain signs and use a suitable variable/objective and signed-value band formulation.

The design distinguishes four kinds of allowance: source-observation uncertainty, screening thresholds, aggregation precision and accounting precision. The pinned model currently shares delta between trade and row/column accounting, applies eps to baseline aggregation, and takes X as exogenous. Adding missing Tolerances/Exclusions sheets alone cannot implement source-specific adjustable output/trade targets. The deterministic initializer also changes overflowing technology priors through median shares and clips negative Z; those transformations need an explicit record.

Reconciliation must prepare all children of a parent jointly before MARIO's hard output precheck, track the residual parent and then preserve both supply/use axes in a connected/full-system solve. Cluster observations constrain their declared member sums; direct observations must not be counted again. Technology estimates remain traceable priors unless a source justifies hard coefficients. Exact aggregation to a baseline with nonzero accounting residuals implies those residuals persist in aggregate: demanding exact zero residuals everywhere at the same time is incompatible. Report inherited and extension residuals separately and retain the agreed baseline-preservation policy.

Independent openpyxl verification checks 5,189 production-value records, paired unit cells and expanded formulas in the local snapshots, while direct numerical recomputation checks all 39 budget sensitivities and all 196 signed-parent observations. Production-code hashes are unchanged. A repeat cloud read stalled and was interrupted; the local source snapshots used for formula expansion match all 5,115 first-pass current production observations and paired unit fields. Their container hashes differ, so whole-workbook byte equivalence or a final cloud rescan is not claimed. The [verification](../../build/audits/split_provenance_2026-10-12/verification.json) and [follow-up manifest](../../build/audits/split_provenance_2026-10-12/evidence_manifest.json) record this limitation. No currency/valuation correction, source change or solver execution was performed.

### All-sector target regeneration simulation

At the owner's request, the next tranche simulates output targets for **all 67 sectors on the complete 163-region grid**, compares parent budgets and trade, and preserves each transformation. The [67-sector review](../../build/audits/split_target_simulation_2026-10-12/sector_candidate_dashboard.csv), [current/candidate/reason table](../../build/audits/split_target_simulation_2026-10-12/changed_target_review.csv), [12-parent comparison](../../build/audits/split_target_simulation_2026-10-12/parent_candidate_dashboard.csv) and [summary](../../build/audits/split_target_simulation_2026-10-12/summary.json) are analytical evidence. No production module, source workbook, inventory, mapping or GTAP matrix was changed, and no MARIO/CVXLAB MRIO solve was run. Twenty small target-only linear programs were run to test cluster-allocation assumptions; their results do not certify MRIO feasibility.

**Purdue delivery version is a separate source of change.** Across the 36 EXIOIOT/COPCOSTS sectors, all **1,684 common output values exactly match May27 REPOUT**. June1 has 1,693 common values: 670 exact matches, 844 differences beyond `max(1e-6 MUSD, 1e-8 × abs(current))`, and 179 smaller differences. The 844 differences affect 22 sectors. Both deliveries also contain 55 positive regional observations outside the released output coverage. [Per-sector delivery lineage](../../build/audits/split_target_simulation_2026-10-12/Purdue_output_release_lineage.csv) preserves cells and counts. This establishes numerical lineage, not an execution log. It supplements the configured June1 cost/output selection in [data_sources.json](../../manifests/data_sources.json): reproducing preserved MARIO inputs and rerunning the raw-source importers are different operations. June1 output substitution is therefore simulated separately from reading-column corrections; neither the selection manifest nor historical sources were rewritten.

The candidate vectors retain labelled historical estimates where no supported positive source candidate is available. Source blanks and numeric zeros remain in the observation ledger; neither becomes a newly certified zero constraint. The complete grid has 10,921 sector-region cells, of which 1,091 have no released output target. Candidate values outside released profile coverage do not constitute usable full inventories. Name-based template identity, classification scope and common basic-price valuation remain unresolved where already recorded.

| Output scenario | Available regional targets | Changed target cells | Individual parent flags | Joint parent-region flags | Conditional export/output flags with released trade |
|---|---:|---:|---:|---:|---:|
| S0: preserved release | 9,830 | 0 | 23 | 39 | 2,623 |
| S1: positive monetary-column candidates, preserving May27 Purdue lineage | 9,886 | 87 | 29 | 57 | 2,623 |
| S1J: S1 with June1 Purdue output substitution | 9,886 | 931 | 29 | 57 | 2,604 |
| S2: S1 plus CEM dimensional money and SDG monetary row labels | 9,887 | 109 | 51 | 77 | 2,623 |
| S3: S2 plus literal USD scale, LMO row-year and RBR native-parent-share assumptions | 9,887 | 201 | 47 | 69 | 2,637 |
| S6: S3 with inclusive cluster tests; APS/SDG remain unallocated | 9,890 | 239 | 52 | 73 | 2,641 |
| S7: S3 with residual cluster tests | 9,891 | 243 | 56 | 73 | 2,641 |

These flags use declared release parents and unharmonized valuations; they are conditional diagnostics. S1 includes restoring positive uncapped source values, not just changing a header lookup. No independent child cap, coefficient normalization, target uncertainty or GTAP closure is imposed. The unchanged count of flags in S1J does not mean its 844 extra numerical changes are negligible. [Parent flag transitions](../../build/audits/split_target_simulation_2026-10-12/parent_flag_changes.csv) distinguish removed, new and persistent flags.

The literal MSI USD-to-MUSD assumption reduces CHM joint flags from nine to three and removes MSI's four individual flags. That improvement does not establish the intended source scale or mining/manufacturing scope. Reading PLSR's E monetary column instead of AJ physical production increases RPP joint flags from five to 21 in S1; output overlap with PLR and PLP's product scope need review. Restoring CEM's dimensionally monetary values exposes 22 NMM parent-region flags in S2 rather than two. LMO gains two positive targets, totalling 4,993.89 MUSD under the row-year interpretation; the conflicting year header remains open. Alternative TVP scale and LMO/RBR 2017-price scenarios are also retained. The 2017-price scenario uses the template's **division by its price index**, giving a 2017-to-2023 multiplier of 1.2239; it does not extrapolate production volumes.

Joint cluster tests impose positive direct observations and declared totals simultaneously, with nonnegative regional outputs and an L1 distance to historical priors scaled by parent output. They do not impose parent capacity, trade, technology or MRIO accounting constraints. The explicit SOP GLOBAL “Rest of” note is used as residual in both tests. Other inclusive/residual alternatives are sensitivity assumptions, not source-definition decisions. Two inclusive interpretations are infeasible already at this target-only level: APS REST OF EUROPE is 230.955 MUSD but its declared membership includes GBR with a direct 293.246 MUSD observation; SDG GLOBAL is 22,312.540 MUSD against 58,305.935 MUSD across its six positive direct countries. [Conflict explanations](../../build/audits/split_target_simulation_2026-10-12/cluster_conflict_explanations.csv) and [allocation statuses](../../build/audits/split_target_simulation_2026-10-12/cluster_allocation_results.csv) retain the assumptions. Failed allocations preserve visibly flagged seed targets. Residual interpretations solve these small systems but still leave 73 joint parent-budget flags; they are not a validated replacement method.

**Subsequent owner decisions.** Apply the output-budget policy to every parent-region group, not only the 69 flagged groups in historical S3. After source selection, monetary conversion, mapping and geographic allocation, let `S` be the sum of resolved child output targets and `X` the supplied GTAP parent output. If `S > X`, warn and apply the same factor `f = X / S` to every child target in that group; otherwise retain the targets. Preserve source observations and record the parent, region, original sum, reference output, factor and each original/adjusted target. No upward scaling, GTAP correction, automatic coefficient scaling or trade scaling is selected by this decision. Missing observations do not become certified zeros. This policy closes the scalar output-budget excess for the resolved targets, with zero parent residual at a binding budget; trade and full MRIO feasibility remain separate checks. Historical scenario counts remain unchanged evidence.

For APS, remove GBR from REST OF EUROPE and allocate the 230.955 MUSD observation across ALB, SRB and XER, retaining the separate GBR observation. For SDG, treat GLOBAL as residual after explicitly represented geographies; the template's GLOBAL note supports this definition. EU27's inclusive/residual meaning and monetary/physical unit conflict remain to resolve. The ledger also retains SDG WORLD at 90,350 MUSD, with no mapped members in the simulation: the tested residual interpretation of both GLOBAL and EU27 implies 80,813.959 MUSD across positive direct countries and the two residual groups, leaving a conditional 9,536.041 MUSD difference. WORLD was not an enforced constraint in those small allocation tests; do not describe their success as source-total reconciliation.

The [trade alternatives](../../build/audits/split_target_simulation_2026-10-12/trade_candidate_policy.csv) retain all existing per-sector choices and simulate June1 child-specific observations for CPP, CPS, LIT and REE separately. They add **2,008 routes**, taking 90,332 to 92,340 rows and 46 to 50 sectors with trade; the corresponding source-production pairing remains explicit. Restoring native-region coverage under those same choices yields 101,150 rows. It reveals **407 positive-export cases with unavailable output** under S3. Conditional bilateral parent-envelope flags increase from 5,164/44,434 observed keys to 5,376/44,941 with the four June1 candidates and 6,596/47,881 with native geography. These are CIF-versus-GTAP screens, not confirmed infeasibility or a reason to reject the source numerically. Composite codes are not duplicated into children and alternative releases are not added together.

A follow-up read-only join finds 400 written intermediate zeros and seven missing MRT rows among these 407 sector-region cases across 27 sectors; none has a released technical profile. The deeper source check below refines the 400 into **388 in-domain Purdue implicit zeros and 12 explicit PCP partner-template zeros**. PCP is not a REPOUT sector, so absence of its records from REPOUT cannot diagnose its production coverage. The seven MRT omissions concern HEL, ICH, ICL, PLR, RAL, RBR and SOP. Positive NTSCIF exports alone do not establish that any source zero is wrong.

**Direct sparse-REPOUT verification.** At the owner's request, the original May27 and June1 `splttargs.gdx` files, matching current workbooks and retained `_old/GDX_to_excel.py` converter were captured and rehashed unchanged. GDXDUMP reads REPOUT as a two-dimensional parameter with the explanatory text `Output valuess, million USD [[VOUT:REG*REPSEC]]`. Both files declare 163 REG and 37 REPSEC elements, a 6,031-cell domain. May27 stores 1,742 REPOUT records and June1 stores 1,751; every stored value is positive, with no explicit zeros, EPS, NA or undefined values. GDX/XLSX keys match completely and all values agree within the declared extraction precision (maximum absolute difference 5.01e-12 MUSD). The retained converter passes `gdxpds.to_dataframes` records directly to Excel without an explicit value filter; this is compatible conversion evidence, not an execution log for each delivery.

The GDX symbols have unrestricted `(*, *)` dimensions rather than formal domain metadata. The read-only GAMS Transfer check binds them in memory to the separately declared REG/REPSEC sets, following the parameter's explanatory text, and obtains complete 163-by-37 dense arrays. These have **4,289 zero cells in May27 and 4,280 in June1**. Every one of the 388 flagged cases inside that domain is zero in both arrays. An independent sparse-key/default-zero reconstruction matches all 6,031 API values in each delivery. This follows [GAMS sparse-parameter semantics](https://www.gams.com/latest/docs/UG_GDX.html): missing in-domain entries have numerical value zero. The optional GAMS-language load probes stopped at licensing; the GDXDUMP and Transfer API checks succeeded without a solver. No upstream Purdue preparation/model code was found in the searched project/repository material, so empirical completeness before GDX creation is not established by these checks.

The **source-reading policy** is therefore to preserve in-domain REPOUT omissions as zeros of the supplied parameter, with implicit-zero provenance, rather than declare them unknown solely because no Excel row exists. This does not generalise to sectors absent from REPSEC, missing partner coverage, or independent claims of observed production. All 12 PCP cases have explicit numeric zero cells in the retained partner-template ledger. The remaining seven cases are geographic omissions and retain that status. The [407-case classification](../../build/audits/repout_sparse_2026-10-12/407_case_classification.csv) and [verification summary](../../build/audits/repout_sparse_2026-10-12/summary.json) preserve the separate evidence.

There is also a paired-trade difference: for all 388 in-domain cases, the first-region/exporter axis of BLTTRD in both matching GDX deliveries has zero total, following the pipeline's direction convention. Positive trade in the 407-case screen comes from the retained May13 NTSCIF choice. This establishes dependence on trade-source choice, not the economic reason for the difference: customs/re-export, product scope, valuation and direction semantics still need harmonisation. Do not increase output to accommodate NTSCIF or replace the selected trade source automatically. Captured inputs and prior evidence hashes are retained in the new audit manifest; no production code, source workbook, mapping or GTAP value was changed.

The separate S8 positive-evidence view has 2,611 direct positive candidates and 8,310 unavailable cells; cluster totals remain separate observations and parent-share/legacy estimates do not become empirical data. Its smaller count of screened trade flags is **not an improvement in full feasibility**: under native trade coverage it has 2,945 positive-export cases without a direct positive output candidate. This distinction is retained in the ledger and summary rather than turning unavailable production into zero.

Independent openpyxl extraction verifies all 5,977 numeric/blank source records used, 72 sector/delivery comparisons and every one of the 2,008 newly selected June1 routes. Direct recomputation checks all 109,210 scenario target rows, 19,560 parent-region groups, 327,630 trade screens and 50 successfully allocated cluster constraints. Historical output/trade/bilateral controls are reproduced; 32 local source snapshots and seven production-code hashes are unchanged. [Verification](../../build/audits/split_target_simulation_2026-10-12/verification.json) and the [simulation manifest](../../build/audits/split_target_simulation_2026-10-12/evidence_manifest.json) document the checks and the use of preserved snapshots instead of a new cloud rescan. Source truth, currency/valuation bridges, coefficient rebuilding and full MRIO feasibility remain open.

### Next work across the complete sector set

1. Separate historical reproduction from a new source-delivery build: freeze and identify May27/June1 production, cost and trade choices together. Close source identity, monetary-column/year/scale decisions and classification scope, prioritizing the measured MSI, plastics, cement and geographic-total effects while retaining the complete 67-sector review.
2. Establish per-sector trade-source choices and explicit composite-product mappings, including the four June1 candidates. Resolve direction, CIF/GTAP valuation and re-export treatment before enforcing bilateral constraints.
3. Incorporate the selected APS/SDG geographic meanings, warning-plus-proportional parent-budget policy and verified in-domain REPOUT zero interpretation into the reconciliation design. Review signed Tax handling, exogenous outputs, common delta and inherited GTAP residuals against the pinned model contract. Resolve remaining source confidence/bands, partner coverage and trade-source compatibility without changing the supplied baseline.
4. In a later implementation, prepare dependency-specific split inputs and exercise representative source, cluster, parent-change, signed-factor and joint-overflow cases, followed by connected-parent/full-system and order-sensitivity checks. Distinguish exact/reference constraints from adjustable observations and quantify every adjustment.

No full MRIO optimization, new NACE/HS certification, raw EXIOIOT/COPCOSTS coefficient reconstruction, currency-exchange/basic-price valuation bridge or source correction was performed. Literal scale and price-year conversions and target-only allocations above are declared scenarios, not adopted corrections. Remaining and skipped checks are not passes.

## Trade source policy and tolerances

### Observed trade lineage

The May13 `NTSCIF` header describes **imports at CIF prices, scaled to GTAP, in M USD**. This valuation label is not carried into a structured valuation field in the final workbooks, which say `M USD`.

The committed exporter reads June1 `splttargs.xlsx/BLTTRD`. The current working tree adds `update_trades_in_exported_inventories`, which replaces the trade sheets using May13 `NTSCIF`. The published files match the latter, not the former, wherever published trade is present. This establishes the numerical source, but does not date or identify the exact code execution that performed the replacement.

For four sectors the sources lead to materially different coverage:

| Sector | June1 rows retained under the published region filter | Published trade rows |
|---|---:|---:|
| CPP | 955 | 0 |
| CPS | 273 | 0 |
| LIT | 410 | 0 |
| REE | 370 | 0 |

These counts describe coverage, not a complete source-selection decision. The review below identifies paired-source candidates and remaining metadata gaps. An empty trade sheet is missing evidence, not a claim of zero trade.

### Selection policy and tolerance settings

Among the 66 distinct readable published codes in the original audit, the existing coverage filter yields 28 with observations in both sources, 17 with May13 only, four with June1 only, and 17 with neither. ZIR was excluded from these original counts. June1-only codes are CPP, CPS, LIT and REE.

The mismatch is partly taxonomic: May13 includes composite codes such as `RRE_LIT`, `CPR`, `ALM`, `LBT` and `HYD`, rather than every disaggregated child code. A composite observation must not be copied into each child or added to child observations. June1's shared output observations match the published CPP, CPS and LIT values exactly, making it a strong candidate for their corresponding trade targets. REE has output differences and needs a paired production/trade review.

The D2.8 source-selection policy should preserve both sources, use explicit per-sector/product mappings, select a preferred observation for each overlapping key and keep its provenance. Use June1's child-specific observations as candidates where May13 only has aggregates; retain May13-only evidence where its scope matches. For overlaps, valuation/year/coverage consistency determines preference, not whichever value happens to pass a numerical check. June1 BLTTRD has no valuation/unit description in its header; numerical plausibility cannot fill that metadata gap. No blanket replacement or unqualified union has been applied.

### All-sector trade compatibility review 12 October 2026

Following the sparse-REPOUT check, the owner authorised a read-only comparison of directions, product coverage and valuation across the complete sector set. [The 67-sector proposal](../../build/audits/trade_compatibility_2026-10-12/67_sector_trade_policy.csv) distinguishes source-domain membership from positive trade coverage. [Route comparisons](../../build/audits/trade_compatibility_2026-10-12/route_source_comparison.csv), [direction checks](../../build/audits/trade_compatibility_2026-10-12/direction_summary.csv) and [17 composite-scope candidates](../../build/audits/trade_compatibility_2026-10-12/17_composite_scope_candidates.csv) retain alternatives; no source choice or composite allocation was activated.

| Candidate workflow | Released activities | Interpretation |
|---|---:|---|
| Positive BLTTRD with a matching REPOUT code | 33 | Compare output and trade from the same May27 or June1 delivery, then review product/activity scope and valuation. Numeric coherence alone is not source certification. |
| Positive NTSCIF with no positive BLTTRD | 17 | Fourteen partner-derived activities plus NFR/PFR/KFR. Preserve observations and resolve scope/re-export/valuation questions. |
| Composite or no direct trade code | 17 | Review joint product envelopes and technology/chemistry allocation. Absence of a child code is not evidence of zero activity trade. |

Both REPOUT files declare 37 source codes, of which 36 are released activities and GAL is not released. Thus 36 released activities have a declared output/trade parameter domain, but **NFR, PFR and KFR have no positive BLTTRD records**. May13 supplies respectively 5,313, 4,875 and 4,960 positive routes on native geography. An all-zero sparse BLTTRD parameter for those codes does not, by itself, justify deleting the NTSCIF evidence or imposing empirical zero-trade constraints. The supplied H6 mapping groups fertilizer HS products under FRT rather than documenting the NFR/PFR/KFR subdivision, which remains to establish.

**Direction and source pairing.** The entire 163-by-37 source grid is checked in each delivery. With the pipeline's first-region-as-exporter interpretation, paired BLTTRD sums never exceed REPOUT beyond `1e-6 MUSD + 1e-8 * abs(output)`; reversing regions produces 2,752 May27 and 2,757 June1 precision-screen excesses. On the 32 source codes also declared in NTSCIF (5,216 regional cells), the forward May13 comparison gives 2,177 one-percent output/export flags against May27 REPOUT and 2,157 against June1; reversing it increases these to 2,982 and 2,965. These patterns support the current direction and paired-source candidacy, not a numerical rule for selecting truth. Formal named exporter/importer metadata and the upstream Purdue preparation code remain unavailable.

**Confirmed differences in product boundaries.** The supplied H6 table assigns RCP to copper-containing residues (262030) and copper waste/scrap (740400), RAL to aluminium residues/scrap, and PLR to plastic waste/scrap. These goods do not automatically represent the output value of the corresponding recycling activity. PGM is assigned HS261690, a broad category of precious-metal ores other than silver, rather than a PGM-only category; [UNSD's classification](https://unstats.un.org/unsd/classifications/Econ/Detail/EN/32/261690) confirms that breadth. NIO's HS261590 likewise includes other minerals besides niobium. PCP's trade mapping includes coal/lignite briquettes, coke and tar, while its source methodology describes coke, coal tar and coke-oven gas. These are explicit scope warnings, not automatic reassignments or new canonical classifications.

MIO includes HS260112 agglomerated iron ore/pellets alongside non-agglomerated ore and unroasted pyrites. For the previously flagged BHR/OMN cases, [Bahrain Steel describes converting imported iron ore fines into pellets](https://bahrainsteel.com.bh/product-stewardship/raw-materials/), and [Vale documents its Omani pellet plants supplied from Brazil](https://www.sec.gov/Archives/edgar/data/917851/000129281425001137/valeform20f_2024.htm). A classification check is essential here: [NACE Rev. 2 class 07.10](https://ec.europa.eu/eurostat/documents/3859598/5902521/KS-RA-07-015-EN.PDF.pdf/dd5443f5-b886-40e4-920d-9df03590ff91?t=1414781457000%2Fdata) includes beneficiation and agglomeration of iron ores and excludes extraction/preparation of pyrites. Pelletisation therefore cannot simply be declared outside MIO if its target is the complete NACE class. The H6 mapping's pyrites item, conversely, requires review against that boundary.

The REPOUT zeros are genuine numerical values of the delivered parameter, but the company's processing evidence means production coverage needs review: does the source count only mine extraction, or also merchant pelletisers using imported feed? For a full 07.10 target, an extraction-only source could underrepresent production; for an explicitly narrower target, trade and technology must follow that narrower boundary. No actual activity-specific output revision, HS-level share of the captured exports or country re-export quantity has been established. Do not automatically move pellet flows to another industry, classify them all as re-exports, raise output to the export total, or delete trade because the delivered output parameter is zero.

**Valuation and model observations.** Native GDX describes NTSCIF as CIF imports scaled to GTAP and BLTTRD as bilateral trade in million USD; the latter still lacks a certified price basis/year bridge to the supplied MRIO. Native API, GDXDUMP and workbook extraction agree on all 272,145 NTSCIF records. NTSTAR and MTRAT also match their native API records. A separate `MTRAT * NTSCIF` versus NTSTAR diagnostic has 26,970 discrepancies beyond `1e-6 MUSD + 1% * abs(NTSTAR)` on 272,154 union keys, so these fields cannot be treated as an unquestioned conversion identity. No tariff, CIF/FOB or basic-price correction was applied. [GTAP's valuation definitions](https://gtap.agecon.purdue.edu/resources/faqs/faqs_display.asp?F_ID=162) distinguish output and transaction prices; [its re-export guidance](https://www.gtap.agecon.purdue.edu/databases/contribute/reexports.asp) requires origin-compatible trade and balanced treatment of re-exports. Whether NTSCIF already has the relevant adjustments remains unverified. The pinned MARIO bridge activates explicitly supplied cross-region trade observations and excludes same-region rows; sparse source values and the solver observation selector must remain separate.

**The agreed output cap requires trade reconciliation as well.** A target-only sensitivity sums the 36 Purdue children without the other 31 activities and applies the selected common parent-region factor. Both deliveries already have 16 over-budget parent-region groups in this restricted set, and paired BLTTRD exports then exceed reduced child output by the one-percent screen in 12 cases, also when same-region trade is excluded. This is a subset/lower bound, not the all-sector cap or a new count replacing S3's 69. For June1 COB/COD, the restricted-group factor is approximately 0.24945: output falls from 2,507.98 to 625.62 MUSD while paired exports remain 2,507.98 MUSD. Output reduction therefore needs a subsequent joint trade-target adjustment; no trade scaling was applied in this sensitivity and its rule remains to specify. Conditional native-parent bilateral screens also remain: forward June1 child trade exceeds the declared parent's `Z + Y` envelope on 5,449 of 19,303 observed parent/origin/destination keys, versus 4,741 of 46,482 for May13 alone on released codes. These have different coverage and unresolved valuations/scopes and must not be interpreted as competing source quality scores.

The concrete next preparation is a per-sector source adapter with matched delivery, source code/product boundary, explicit units/year/valuation, implicit-zero provenance and a separate trade-observation mask. Compare paired BLTTRD for the 33 positive candidates, retain the 17 May13-only candidates including fertilizers, and allocate the 17 composite/no-direct-code cases only after their boundaries are defined. Then reconcile child output and trade jointly against the unchanged parent budgets, recording every target adjustment and optional warning. No source switch, workbook edit, canonical-parent change, production-module change or MRIO solve was performed. [Independent verification](../../build/audits/trade_compatibility_2026-10-12/verification.json) recomputes eight direction summaries, 67 policy records, 169,908 conditional bilateral rows and 11,736 restricted-cap values against frozen inputs. The source-check record distinguishes unchanged current bytes, metadata-only container changes and any live cloud rereads skipped after 15 seconds; every retained input snapshot is rehashed. [June1's container comparison](../../build/audits/trade_compatibility_2026-10-12/June1_container_change_check.json) confirms exact cell/formula equality in all five sheets despite changed custom-XML/trash parts. All seven production-code hashes remain unchanged. Live-source checks are not claimed passed when skipped; the numerical results refer to the captured deliveries.

### Joint output and trade target simulation 13 October 2026

The owner authorised proceeding with the analytical preparation across all activities while retaining the instruction against operational changes. The [simulation](../../build/audits/joint_reconciliation_2026-10-13/simulate_joint.py), [summary](../../build/audits/joint_reconciliation_2026-10-13/summary.json) and [67-sector dashboard for each scenario](../../build/audits/joint_reconciliation_2026-10-13/sector_dashboard.csv) make the joint target problem concrete. Four scenarios combine the matched May27 or June1 REPOUT/BLTTRD delivery with inclusive or residual interpretations of SDG EU27. Neither a preferred delivery nor an EU27 interpretation is adopted by running the scenarios.

**Output preparation.** Start from the earlier S3 candidate grid, retaining its explicitly unconfirmed MSI/TVP USD scale, LMO year and RBR parent-share assumptions. Replace the 36 Purdue activities with the complete native REPOUT parameter from each delivery, including verified in-domain implicit zeros. Allocate APS REST OF EUROPE over ALB/SRB/XER and its CARIBBEAN total over its supplied members. Allocate SDG GLOBAL over the rest of the world after its six explicit countries and the EU27 geography. In each activity, exact positive country and applicable cluster observations are solved together by a nonnegative L1-distance allocation using S3 as a prior and inverse native-parent output as the distance weight. Allocation is an estimate; this weight is not source confidence or a capacity constraint. Other unresolved cluster definitions remain S3 priors rather than silently adopting every residual interpretation.

Then apply the adopted common factor `min(1, parent output / sum(child outputs))` once per complete parent-region group. All four scenarios have **69 over-budget parent-region groups**, all with complete child-target coverage. The [budget ledger](../../build/audits/joint_reconciliation_2026-10-13/parent_output_budgets.csv) records the warning, factor and residual; the [output ledger](../../build/audits/joint_reconciliation_2026-10-13/output_targets.csv) preserves every original and reduced candidate with provenance. No target is increased to fit trade. Across the full grid, 10,880 output cells are available and 41 remain unknown; 57 positive adjusted output cells have no released technical profile. Partial groups elsewhere describe available targets only and cannot certify a complete split.

**Selected trade evidence.** Use positive cross-region paired BLTTRD for 33 activities and May13 NTSCIF for the other 17 direct-code candidates, including NFR/PFR/KFR. The remaining 17 composite/no-direct-code activities receive no child trade target, rather than zero trade. This source pairing is a simulation of the previous proposal, not a source-policy change. Same-region records are outside the split bridge's trade-observation mask; implicit zero routes are not expanded into hard-zero observations. The June1 variant includes 110,241 positive routes. Of these, 148 routes, totalling 262.25 MUSD, have unknown producer output and remain unreconciled. [Coverage](../../build/audits/joint_reconciliation_2026-10-13/sector_coverage.csv) and the [full route ledger](../../build/audits/joint_reconciliation_2026-10-13/trade_targets.csv) retain these distinctions.

Three methods are compared on routes with available producer output:

1. **Output-only proportional preparation (P1):** reduce each producer's observed routes by one factor only when their export sum exceeds its capped output; retain destination shares.
2. **Proportional joint preparation (P2):** after P1, reduce the selected children on an over-budget parent/origin/destination route by one shared factor. This respects both producer-output and parent-route capacities without increasing any observed trade. It preserves child proportions on that route after P1, but can change each child's overall destination pattern.
3. **Maximum-retention LP benchmark:** maximise retained trade MUSD subject to nonnegative route values no larger than the original observation, producer exports no larger than capped output, and selected child trade on a parent route no larger than native parent `Z + Y`. Parent/origin groups are independent in this limited capacity model. Each MUSD has equal objective weight; individual child/route optima may be nonunique. The benchmark measures the minimum aggregate reduction under these assumptions. It does not select empirical truth or certify a uniquely preferable child allocation.

The native parent-route envelope requires comparable activity boundaries, origin treatment, reference years and valuation. Those bridges are still unresolved, particularly for CIF NTSCIF versus native MRIO flows. P2 and the LP are therefore **conditional monetary-envelope sensitivities**, not deployable corrections. Nonnegative unknown activity flows could consume remaining capacity later; the capacity tests below cover selected, available-output observations only. Full row/column accounting, intermediate-input composition, domestic demand and signed value added are outside this target-only problem.

| Result | May27 pair | June1 pair |
|---|---:|---:|
| Available-output trade before preparation, MUSD | 2,204,835.13 | 2,205,194.49 |
| Trade retained after P1, MUSD | 1,988,515.19 | 1,988,861.54 |
| Trade retained after P2, MUSD | 1,962,738.79 | 1,963,067.48 |
| Maximum retainable trade under the LP constraints, MUSD | 1,964,434.66 | 1,964,760.96 |
| Minimum conditional reduction | 10.90% | 10.90% |
| Raw export/output precision-screen flags | 1,298 | 1,296 |
| Raw conditional parent-route flags | 9,577 | 9,579 |
| Parent-route flags remaining after P1 | 7,538 | 7,542 |
| Selected output/route budget flags after P2 and LP | 0 | 0 |

The EU27 alternatives produce identical trade results because SDG has no direct selected child trade observations. This does not resolve EU27 semantics. P2 retains just 1,693.48 MUSD less than the June1 LP maximum, about 0.077% of available-output original trade. Its arithmetic simplicity is useful for a future reviewed fallback, but proximity to an optimum does not establish empirical correctness. [Parent/origin retention](../../build/audits/joint_reconciliation_2026-10-13/retention_by_parent_origin.csv) and [parent-route budgets](../../build/audits/joint_reconciliation_2026-10-13/parent_route_budgets.csv) record the comparison. Any LP child-specific reduction should be read with its nonuniqueness caveat; an individual child's retained trade need not exceed its P2 value even though the aggregate LP optimum does.

**Where the unresolved cases concentrate.** There are 928 zero-output producer cells with positive stored selected trade, of which **920 exceed 1e-6 MUSD**. All arise in the 17 NTSCIF-only candidates; the 33 native paired BLTTRD candidates contribute none. Fertilizers account for 313 of the material cases. The [zero-case ledger](../../build/audits/joint_reconciliation_2026-10-13/zero_output_trade_cases.csv) distinguishes REPOUT implicit-zero provenance from S3/partner priors and preserves available template states/cells. This changed source selection and full-geography coverage is a new screen, not a revised classification of the previous 407 cases. A conditional zero retained by a capacity calculation means the zero-output candidate and positive trade cannot coexist under the assumed activity match; it does not independently demonstrate zero real trade, inaccurate output, or re-export volumes.

Vehicle activities HEL/ICL/ICH have particularly large output-stage incompatibilities. In the frozen heavy-duty ICEV template, Germany is explicitly written as zero in `Total production!E7`; the selected ICH/DEU NTSCIF exports sum to **8,208.18 MUSD**. France, Sweden and the Netherlands also have explicit template zeros alongside positive NTSCIF. Those are source conflicts to investigate, not grounds to replace zero with exports or delete the trade. In the June1 benchmark, the 33 paired candidates retain 481,400.85 of their 509,973.21 MUSD available-output trade; the 17 NTSCIF-only candidates retain 1,483,360.10 of 1,695,221.28 MUSD. This is one equal-MUSD optimum, not separate source-family optima or a source-quality ranking. [Source-family totals](../../build/audits/joint_reconciliation_2026-10-13/source_family_summary.csv) and [largest proportional adjustments](../../build/audits/joint_reconciliation_2026-10-13/largest_conditional_adjustments.csv) provide the review coordinates.

**APS and SDG.** APS's adopted GBR exclusion produces an exact pre-cap REST OF EUROPE total of 230.955191 MUSD over ALB/SRB/XER; the cluster's total is unchanged by the subsequent cap in these scenarios. SDG GLOBAL is exactly 22,312.539683 MUSD over the 131 residual regions. Both EU27 interpretations permit nonnegative allocation, but neither resolves the raw WORLD observation: inclusive EU27 produces a global sum of 80,720.583683 MUSD, **9,629.416317 below WORLD's 90,350**; residual EU27 produces 80,813.958921, **9,536.041079 below WORLD**. These gaps already exist before applying any parent cap. [WORLD conflicts](../../build/audits/joint_reconciliation_2026-10-13/SDG_WORLD_conflicts.csv) retain the incompatible observation explicitly; the exact all-source-total problem cannot be called solved. The monetary row/header conflict and product-price proxy remain open.

**Verification and next work.** [Independent verification](../../build/audits/joint_reconciliation_2026-10-13/verification.json) rechecks 43,684 output cells, 7,824 parent-output groups, 439,956 available-output routes, 592 unknown-output route records across four scenarios and 16 geographic constraints. It confirms proportional factors, source values, native capacities, preserved unknowns and all 67 dashboard rows per scenario. All 3,518 solved LP groups have checked primal and dual certificates: maximum stationarity residual is zero, maximum primal-dual gap is `2.91e-11 MUSD`, and maximum constraint excess is `9.93e-8 MUSD`. All 12 frozen input hashes and seven production-code hashes match. Current cloud sources were not reread in this tranche; their present equality is not certified. The [evidence manifest](../../build/audits/joint_reconciliation_2026-10-13/evidence_manifest.json) records the captured inputs and generated artifacts.

The next dependency is source-contract review, prioritising vehicle production coverage, fertilizer product subdivision, methanol's scope/cluster assumptions and the previously identified scrap/ore boundaries, followed by explicit valuation/origin treatment and composite allocation. Preserve disputed observations and choose reviewed bands or adjustment penalties; do not turn this 10.9% conditional benchmark into a blanket trade cut. Before a full `split=True` trial, resolve the 41 unknown outputs, 57 missing positive-output profiles and the model's existing signed-factor/accounting incompatibility. The supplied GTAP remains unchanged, and no new MARIO solve, operational source switch or trade correction was performed.

The agreed validation direction is captured in [validation-policy.json](../../config/validation-policy.json): checks are optional, warnings remain visible and skipped checks are listed. It is a policy artifact, not yet wired into the full production runner. Technical failures cannot be reported as successful exports.

The standalone exporter no longer globally suppresses Python warnings. The single-sector command warns that a metadata parent override does not recalculate coefficients.

For exploratory output/export screening, the initial configurable threshold is `exports > output + 1e-6 M USD + 1% × abs(output)`. This is a review threshold, not an assumed statistical error band. In the original audit scope it flags 2,556 distinct sector-region pairs; even a 5% relative tolerance leaves 2,538. Tolerance alone does not resolve missing output, valuation or scope problems.

The final MRIO must satisfy its supply/use and column-accounting identities within explicitly reported solver tolerances. Output equals domestic use plus exports under the appropriate origin accounting, not exports alone. Observed output/trade targets can have configurable absolute/relative bands or penalties, with every adjustment reported. Diagnostic tolerances, empirical uncertainty and solver numerical tolerances are separate parameters.

### Actual split=True runtime diagnostic 13 October 2026

The owner explicitly requested trying the actual split rather than continuing target-only analysis. [The runtime harness](../../build/audits/actual_split_2026-10-13/run_actual_split.py) calls the installed, pinned MARIO `read_add_sectors_excel(..., split=True)` and `add_sectors(..., split=True)`, not a mock or substitute optimisation. [Results and tracebacks](../../build/audits/actual_split_2026-10-13/results.json), [the alternative-solver run](../../build/audits/actual_split_2026-10-13/solver_diagnostics.json) and [verification](../../build/audits/actual_split_2026-10-13/verification.json) retain what happened. Only local analytical artifacts and this report were written.

**Published inputs first.** Direct native-workbook parsing was attempted for all 67 locally preserved final inventories using the pinned split reader. All fail with `WrongExcelFormat: Missing required split-support sheet in add-sectors workbook: Exclusions`. ZIP-level verification also confirms that all 67 lack `Tolerances`. [Reader results](../../build/audits/actual_split_2026-10-13/raw_67_reader_checks.json) preserve every file's failure. This is the current pinned reader's contract, not a claim that the colleague's different MARIO version must fail at the same earlier stage. Empty Exclusions and explicit `delta=0`, `eps=0` were added only to the diagnostic workbooks so that the runtime could proceed.

**Numerical scope.** The existing original, uncorrected GTAP aggregation to Germany plus ROW retains all 76 native sectors. Its factor values and every origin-sector/destination-region `Z + Y` aggregate were checked against the complete native reference before use. Maximum factor aggregation difference is `2.79e-9 MUSD`; the original two-region table contains 16 negative factor cells and a maximum column residual of 0.341909881 MUSD. Those values remain unchanged. This specifically uses `hye_deu/baseline/flows`, not the historical baseline-corrected `hye_scale100` outputs. [Baseline evidence](../../build/audits/actual_split_2026-10-13/baseline_integrity.json) records hashes and checks.

All 67 child identities are included. The 63 with a published German profile are active in Germany. MAO, MCU, NIK and PGM lack a German profile and are active in ROW using output-weighted averages of their published positive-output foreign profiles. [Profile preparation](../../build/audits/actual_split_2026-10-13/profile_preparation.csv) records counts, values and the rule. Inactive child locations are assigned zero **as a definition of this reduced experiment**, not as inferred empirical zeros. Only published trade originating at an active child location is supplied; foreign countries collapse to ROW and intra-ROW observations are outside the cross-region mask. Monetary matrices and output/trade targets are divided by 100 and satellite coefficients adjusted consistently for numerical scaling.

This pilot deliberately exercises all child identities while keeping the optimisation small. Expanding a partially covered GLOBAL cluster to ROW changes input-origin weights; four foreign profiles are averaged and the other 63 countries' ROW child production is inactive. These are recorded [scope limitations](../../build/audits/actual_split_2026-10-13/pilot_scope.json). A result here cannot certify the complete 163-region production/trade/profile allocation, nor reproduce every native parent-budget conflict.

| Actual call | Preparation | Observed result |
|---|---|---|
| `published_targets` | Published active-location output and selected published trade | Loads all 67 children, creates the deterministic split and CVXLab model, then CLARABEL raises `SolverError`. |
| `capped_targets` | The same inputs with the agreed common parent-region cap available | Reaches optimisation and produces the same CLARABEL error. |
| `capped_no_trade` | Capped preparation with no supplied trade observations | Reaches optimisation and produces the same CLARABEL error. The generated Trade_selector is entirely zero. |

All cap factors happen to be one in this reduced pilot: the selected regional targets do not exceed its aggregated parent budgets. The cap and published-output cases therefore have identical X/V0/Z0 and parent-reference data. This experiment does **not** independently test the 69 native cap adjustments; that coverage belongs to the joint target simulation above. Removing trade, however, is a real change in the selected constraints and the failure persists.

**Concrete model blocker.** Every generated model contains **12 negative `V0` reference entries**: Tax and TTM for HEL, ICL, MUN, PGR, SIR and ZIR in Germany. The copied operator evaluates `entropy(V,V0)` as `cp.rel_entr(V, V0 + 1e-8)`. Each listed reference remains negative even after that offset. Relative entropy has no finite value there for a nonnegative V; an independent scalar evaluation at V=0 returns infinity for all 12 entries. [Domain evidence](../../build/audits/actual_split_2026-10-13/entropy_domain_evidence.json) preserves coordinates, parameter values and the immutable generated inputs. These signs originate in published child profiles; they were not introduced by an empirical-zero trade decision.

This reduced model's `Vold` contains only the 12 parent industries on its two regions and is nonnegative after geographic aggregation. Thus the observed child-reference domain failure is distinct from the earlier **196 negative native parent Tax entries** and their nonnegative-V aggregation contradiction, which still matter for the eventual native-geography model. Do not attribute the current runtime result solely to negative native parent values or to the original APP/MOZ scalar-output check.

To check that this was more than a CLARABEL-specific failure, the generated no-trade model was copied without changing its setup, CSV inputs or observation selectors. Using the same MARIO compatibility contexts to reload it, verbose CLARABEL terminates with `InsufficientProgress`; **SCS returns `infeasible`**, at iteration 350, with an infinite objective. [Verbose solver evidence](../../build/audits/actual_split_2026-10-13/solver_diagnostics.log) records both runs. The conic formulation has 109,494 variables and 449,422 constraints in this reduced case. The relative-entropy domain contradiction independently proves a blocker; the solver's infeasible result does not establish that no other conflicts are present.

The first temporary workbook adapter used incorrect inventory column headers and its runs stopped on `KeyError: Item type`; those were corrected to the source's exact seven-column schema and preserved under `initial_adapter_failures`. A first model-reload helper likewise omitted the installed MARIO nullable-settings compatibility context; its validation errors are retained separately. Neither adapter failure is counted as a repository/source defect or as one of the three correctly loaded runtime results above.

**Integrity and next dependency.** Independent checks verify 16,110 core coefficient cells across the three diagnostic inputs against the German source profiles or the declared weighted foreign profiles. All 67 source workbook hashes, eight original baseline Parquet hashes and seven operational-code hashes are unchanged; the caller's baseline matrices are bitwise identical before and after each failed `inplace=False` call. No `residue` threshold, factor clipping, baseline closure or tolerance relaxation was used. The no-trade case omits trade constraints as an explicit experiment; its source records remain in the preceding cases and ledger. Current cloud source files were not reread; the diagnosis refers to the frozen local captures. [The evidence manifest](../../build/audits/actual_split_2026-10-13/evidence_manifest.json) records all runtime artifacts.

The next model design must allow signed factors where required and use a loss with a valid domain for their signed reference values. The existing negative-parent aggregation constraints, inherited accounting residuals and shared accounting/trade tolerance also require explicit treatment. Changing solver, enlarging trade tolerances or applying the output cap does not remove the proven entropy-domain failure. A full native `split=True` acceptance trial remains open; no successful split database or deployable model modification is claimed.

## B07 and B10: why code decisions still need review

B07 is partly about making transformations explicit, and partly about whether they implement the intended method. Code already normalises, caps, estimates and fills factors, but different entry points apply different rules. A non-unitary profile can survive one path while another rejects or rescales it. The existence of code does not establish that a published exception is intentional. Transformation logs should show original value, changed value, rule and rationale, alongside optional consistency warnings.

B10 is a concrete missing branch. `template_to_inventory.py` identifies `_matched_cl` but never uses it to allocate the cluster's output. Uncovered countries receive a median new/parent ratio instead. `_global_val_to` is likewise unused, while non-zero GLOBAL production rows are already dropped by the parser.

For HVC, the current source contains EU27 excluding Germany with a total of about 19,558.47. Replaying the current resolution logic gives about 45,465.78 across its 26 members. Austria receives about 1,517.89 from the median method, versus 652.97 under the commented parent-weighted cluster allocation. These are a current-input illustration, not an assertion of bit-identical historical replay; the published Austrian value is 1,517.9157. The parser does not provide a unit label for this row, another issue to retain before changing the method.

The scan found cluster observations with uncovered members in eight templates: APS, HVC, MSI, MTH, PLP, PLR, PLS and SOP. There are 23 cluster observations, 21 positive. A correction must define overlaps, direct observations within clusters, unit conversion and whether cluster totals are inclusive or residual. It must then report changes against the baseline. No cluster-allocation correction has been silently applied in this follow-up.

## Code provenance

| Evidence | Revision or observation | Interpretation |
|---|---|---|
| First committed D2.4 export | `f3fdc94`, 4 June 2026 | Historical candidate preserved as a Git archive. |
| Latest ENTICE commit at capture | `14fc2bf52802ca1572efd557de15c15cf4abf77d`, 8 June 2026 | Latest committed producer candidate; references the absent `MARIO inventories copy`; the owner confirmed it was an overwrite safeguard, so the normal folder can be used. |
| ENTICE working copy | Existing staged moves, modified modules/mapping and untracked modules | Material differences from HEAD include parent overrides, copper processing and the trade replacement step. |
| Public guided example before delivery | `04697834466cea3649607b5b7d87bef9599d2b16`, 10 June 2026 | Preserved fixed revision; points to MARIO branch `dev_gtap_VA`, not a pinned dependency commit. |
| Public example at audit | `81f3c077a9f514641ca17b114198189b8978266e` | July changes in the available history concern README installation instructions. |
| Local MARIO at capture | `590426673589dc474d1d23547b1d366758d7fec7` plus recorded working changes | Current inspection reference, not the certified delivery version. |
| Local CVXLAB at capture | `1f2521b52d85ca0783dca5991d697d22bfa044a3`, clean | Current inspection reference, not the certified delivery version. |

The available local MARIO `dev_GTAP_VA` and remote-tracking `dev_gtap_VA` references point to a July revision. Their names cannot recover the exact June environment. No delivery-time dependency lock, solver log, environment export, or full build manifest has been found in the inspected material.

An older existing audit covers 50 files in `MARIO inventories copy`, while the current intermediate folder contains 68. The old audit is preserved as historical evidence; its counts are not treated as findings about today's folder.

Recovering that copy folder is no longer a prerequisite. Its older 50-file audit remains historical evidence; the normal 68-file intermediate folder is the working source candidate.

## Producer environment and representative verification

The runtime is now reproducibly installable. The [installer](../../scripts/bootstrap_producer.py), [dependency lock](../../requirements/d24-producer.txt) and [source/patch configuration](../../config/producer-environment.json) create a fresh environment without inheriting system packages. Tested on Python 3.13.14, macOS arm64. This is an explicitly reconstructed integration environment, not evidence of the exact June execution environment.

| Component | Fixed reference / change |
|---|---|
| MARIO | Commit `590426673589dc474d1d23547b1d366758d7fec7`; local patch pins pandas 2.3.3 and reads both mapping-based and attribute-based CVXLAB settings. |
| CVXLAB | Commit `1f2521b52d85ca0783dca5991d697d22bfa044a3`; local patch declares the required SALib 1.5.2 dependency. |
| Numerical packages | pandas 2.3.3, numpy 2.1.1, CVXPY 1.9.2, CLARABEL 0.11.1; remaining dependencies are pinned in the lock. |
| Patch validation | MARIO's copied-template test now checks preserved model contents when the existing compatibility routine rewrites the Excel container. Byte identity is still required when no rewrite is needed. |
| Scope | The patches are retained in this repository and applied to isolated source copies. Original MARIO/CVXLAB repositories and the user's existing Python environment are preserved. Compatibility is tested for this workflow, not every MARIO feature. |

The earlier dependency conflict, undeclared SALib import and `ModelSettings.get` failure are resolved in this environment. The clean installer completes and `pip check` finds no broken requirements. Focused checks pass: 10 repository tests, 20 MARIO insertion/bridge tests and 48 CVXLAB unit tests. The integration test checks actual accounting, aggregation back to the parent, and an observed bilateral trade target; a successful solver return alone is not the assertion.

### What the HYE reconstruction establishes

The [verification command](../../scripts/verify_producer.py) has two distinct checks:

- **Native-geography replay:** independently evaluate the HYE/DEU coefficient rules against the original GTAP inputs and compare with the preserved D2.4 workbook. All 93 coefficients match within `1e-12` absolute / `1e-10` relative allowance; maximum absolute difference is approximately `2.78e-17`. This explains a regional inventory numerically, not the complete historical database build.
- **Representative software run:** aggregate GTAP to Germany plus ROW while retaining all 76 sectors, select the existing HYE/Germany profile, run MARIO insertion and the repository exporter, then consume the exported workbook in a real MARIO/CVXLAB split. The script supplies the current API's required empty Exclusions sheet and explicit Tolerances sheet. Missing HYE trade observations remain unconstrained and are reported as a skipped validation.

Two previously implicit rules explain why insertion after aggregation differs from the historical inventory:

1. `OthVA` is distributed using unweighted sums of baseline value-added coefficients across all regions and sectors. Changing the regional aggregation changes those weights. Using native geography reproduces all four published HYE/DEU factor coefficients; for example Tax is `0.1784005986438553`, while the uncorrected two-region pilot gives `0.1764123802463593`.
2. HYE's `GLOBAL` cluster contains 162 of the 163 GTAP regions and omits **MRT (Mauritania)**. The importer initially inherits the CHM parent column and replaces inputs only for covered origins. Mauritanian parent inputs therefore remain. Including that inherited remainder reproduces the published sector-input coefficients as well. Expanding `GLOBAL` to every target region would change the data.

The two-region pilot merges covered and uncovered countries into ROW, which changes that source-cluster boundary. It is a software diagnostic, not an approved migration rule. Production portability must resolve source profiles before aggregation or retain regions needed to represent source coverage. The original HYE workbook also has a conflicting Summary description (steam reforming versus its electrolysis filename/profile); the canonical registry must resolve the activity description without silently treating matching numbers as correct metadata.

### Accounting and solver outcome

The input GTAP table already has small column-accounting residuals. In the two-region aggregation, 109 of 152 columns exceed the diagnostic allowance; the maximum absolute residual is about **0.341910 M USD**. The source of these residuals has not been established. They are not automatically labelled rounding errors or caused by HYE insertion.

The earlier diagnostic experiment rescaled value added in a private copy, retaining factor shares and signs. Its recorded adjustments and results below remain historical evidence. **The owner has now explicitly ruled out correcting the GTAP baseline.** The baseline-closure function and command-line option have been removed from the current verification tool. New runs preserve the supplied values, report pre-existing residuals and report any solver incompatibility without repairing the baseline. The old experiment's largest relative factor adjustment was about `7.06e-5` (0.00706%), its largest individual adjustment about 0.183735 M USD, and its total adjustment about +1.234802 M USD. None of these adjustments is adopted for production.

For the recorded diagnostic run, monetary matrices/targets are divided by 100 for the solver and restored afterwards; satellite coefficients are adjusted consistently with that numerical scaling. The model's `delta` and `eps` are both set to zero. Post-solve checks use `absolute residual <= 1e-6 + 1e-8 × abs(reference)` in the original monetary units. The accounting allowance was not loosened to obtain a pass.

| Check | Recorded result |
|---|---|
| Row accounting | Pass; maximum absolute residual zero. |
| Column accounting | Pass at every coordinate; maximum absolute residual approximately `1.86408e-4` M USD, within the corresponding relative allowance. |
| HYE/Germany output target | Pass against 71.99337 M USD; absolute difference approximately `2.92e-8` M USD. |
| Aggregation back to baseline Y and V | Pass with the same absolute/relative rule. |
| Aggregation back to baseline Z | Two entries fail; retained as warnings with coordinates, values and allowances in the verification JSON. |
| Solver | `optimal_inaccurate`; retained as a warning. |
| Child-specific HYE trade target | Skipped because no such observations were supplied; this is not a zero-trade assumption. A separate synthetic integration check exercises an observed trade target. |
| Very small negative flows | Minimum Z approximately `-6.08e-9` M USD; reported, not silently clipped. Negative baseline factor values are retained. |

The result is **completed with warnings**, not a certified release. Remaining numerical work is to resolve the Z aggregation flags and establish full-scale acceptance, while keeping diagnostic tolerances, observed-target uncertainty and exact accounting separate. The upstream model currently shares `delta` between output/trade bands and accounting constraints; merely increasing it would permit imbalance. The full 163-region optimisation and rebuilding every inventory remain outside this completed representative check.

### Repeatable commands

Create a new environment directory with Python 3.13. The optional local-repository arguments read immutable commits and ignore working-tree changes; omitting them fetches the configured public repositories.

```bash
python3.13 scripts/bootstrap_producer.py \
  --directory build/my_producer \
  --mario-repository /path/to/MARIO \
  --cvxlab-repository /path/to/cvxlab

ENTICE_PRODUCER_TESTS=1 build/my_producer/.venv/bin/python \
  -m unittest discover -s tests -v

build/my_producer/.venv/bin/python scripts/verify_producer.py \
  --baseline-dir '/path/to/2023entice' \
  --source-workbook '/path/to/MARIO inventories/Add_sector_Manufacture of hydrogen via electrolysis.xlsx' \
  --published-workbook '/path/to/D2.4 inventories/HYE - Manufacture of hydrogen via electrolysis.xlsx' \
  --output-dir build/my_hye_check
```

The last command preserves baseline values and can expose their incompatibility with the selected constraints. It refuses to overwrite an existing run. Python/API/solver failures produce a failed result and non-zero exit status; completed checks with warnings remain reviewable and return normally. The previous experimental closure option is no longer available. Its source snapshot is retained with the old evidence under `build/reproduction/recorded-code/`.

The [producer verification manifest](../../manifests/d24_producer_verification.json) records inputs, code hashes, environment and verification evidence. Large or licensed data, generated workbooks, matrices and detailed logs remain in ignored `build/` directories. The original baseline manifests remain unchanged.

## Controls to add after the reconstruction

Following the owner's response, diagnostic checks are optional and warnings/skipped checks must be visible. The earlier suggestion of mandatory acceptance gates is superseded. These are check capabilities and reporting requirements, not mandatory data gates or changes already made to the existing producer. The agreed policy is recorded in [validation-policy.json](../../config/validation-policy.json); it is not yet wired into the full runner.

1. Validate completeness, finite numbers, unit/valuation/year semantics and explicit missing/zero states before processing.
2. Validate stable identifiers and active catalogue membership; represent aliases separately from unique sector definitions.
3. Report coefficient sums by comparable quantity type, excluding physical satellite accounts. Apply sign rules by factor/account rather than blanket positivity.
4. Validate output envelopes jointly across all children of a parent, with declared tolerances and no silent clipping.
5. Run production/trade necessary-condition screens, detect valuation and scope conflicts, and retain the full list and value of filtered-out trade observations.
6. Require a reviewed source-selection policy. A later source must not silently erase another source's observations without a recorded decision.
7. Preserve pre-transform values and record every estimate, normalisation, cap, residual allocation and factor completion.
8. After an actual split, test solver status, row/column residuals, constrained trade residuals, parent aggregation, structural zeros, satellite accounting and intended handling of negative flows.
9. Make the release report describe the final post-trade-replacement files and state which checks were skipped, rather than treating skipped checks as passes.

Keep data corrections, policy changes and code refactoring attributable through commits and machine-readable change records. Update their status here; the preserved evidence remains the comparison reference.

## Portability, Excel and T2.6

The signed grant agreement describes T2.6 as a user-friendly open disaggregation tool, with underlying inputs, protocols and implementation guidance. It explicitly supports additional splits in other I-O frameworks of similar granularity. The tool is associated with D2.7; D2.6 is the transport-matrix deliverable and should not be confused with Task 2.6.

The project owner has confirmed that SPLITCOM was a suggestion and MARIO/CVXLAB is the selected implementation. No further confirmation is required for this repository's design.

### Why portability extends beyond remapping

| Dependency observed in the current workflow | Consequence for another MRIO | Information to preserve |
|---|---|---|
| Input descriptions/codes collapse into GTAP parents or clusters | A finer or differently bounded target cannot recover lost distinctions by renaming the GTAP code | Original input concept, source classification/version, and source-to-target mapping separately |
| Cluster allocation uses the GTAP parent's structure | The detailed coefficients depend on the target database | Empirical cluster total separately from the generated detailed allocation |
| Regional output estimates and caps use GTAP parent output | A value calibrated/capped to GTAP is not automatically an observation for EXIOBASE | Observed value, reference year, monetary basis, estimation method and target-specific resolved value |
| Country/cluster coverage reflects GTAP geography; HYE GLOBAL omits MRT and leaves inherited parent inputs there | Aggregation can erase a meaningful covered/uncovered boundary; cluster names alone cannot establish coverage | Explicit membership/version, inherited remainder and a coverage/priority policy |
| Factor mapping combines original categories; HYE OthVA allocation uses unweighted sums of coefficients across the database | Both factor detail and regional aggregation affect the result; the native HYE replay verifies this dependence | Original factor codes, explicit weighting rule and target-specific allocations |
| Cost profiles are monetary and normalised | Changing currency, valuation or year requires harmonisation beyond a label change | Functional unit, normalisation basis, currency, price year and valuation |
| May13 trade source is CIF imports | Linking these observations to domestic output or basic-price MRIO flows requires a valuation bridge | Trade direction, CIF/FOB/basic-price basis, margins and source coverage |
| Final exporter aggregates supplying regions and writes GLOBAL | Final files do not preserve all origin detail used upstream | Source origin information before aggregation |
| Current pipeline is invoked as IOT | A product-by-product, industry-by-industry or SUT target needs an explicit accounting choice | Target table type, technology assumption where relevant, activity/product distinction |
| Energy/emission template rows are skipped by the monetary parser; output satellites can come from the parent database | Final satellite rows cannot automatically be called independent technology-specific observations | Satellite source, physical unit, gas/energy category and whether inherited or observed |
| Input residual share and parent residual sector are different operations | Conflating them changes the model | Separate names, definitions, parameters and provenance for each |
| Target already contains some proposed sectors or has overlapping parents | Naive insertion can duplicate an existing activity or exceed an accounting envelope | Target coverage checks and mappings that explicitly handle multiple/overlapping parents |

The reusable layer should therefore contain source evidence and reviewed assumptions, with target-specific adapters resolving that evidence into operational inventories. GTAP-resolved intermediates remain valuable for the D2.4 baseline, but do not by themselves preserve everything needed for a target-independent inventory.

The published classification already includes HS and NACE/ISIC concordance sheets. The captured Purdue material also includes EXIOBASE mappings. These are evidence assets to review and version; their availability alone does not establish full coverage, compatible definitions or reversible mappings.

### Human-readable inventories and internal data model

The proposed compact `HYE.xlsx` is an editing interface over a structured data model; its authoring location is the existing SharePoint, not an independently editable Git copy. The current MARIO workbooks are migration evidence, not the proposed collaborator interface. A model should preserve at least:

- a stable sector/concept identity, description, scope and owner;
- source observations for cost profiles, production, trade and satellites;
- units, functional units, years, price bases and source references;
- geography/profile coverage and explicit missing/zero/structural-zero meanings;
- versioned mappings, assumptions and reviewed overrides;
- target-specific resolved data and a transformation log, separate from empirical observations.

Original observations and target-resolved values may both be needed. Their provenance must remain distinguishable even when only the resolved baseline value can initially be recovered. Do not invent an original observation by reversing a lossy transformation.

### Excel on SharePoint and reproducibility in Git

The owner subsequently selected the project SharePoint `Data split/Inventory generation` as the operational data and authoring location. The scoped migration is recorded above; the original POLIMI/eNextGen files remain preserved. Git continues to hold code, schemas, mapping/configuration evidence and manifests.

Each accepted input revision must be ingested as a fixed snapshot, recording file identity, available SharePoint version identity, content hash and validation result. A reproducible run refers to that snapshot rather than an unfixed live workbook. SharePoint history supports collaboration; a checksum and captured payload identify the exact bytes used by a build. Machine-readable exports are generated from the accepted Excel version and are not a second independently editable source of truth.

This can support external users through downloadable versioned release inputs without requiring access to the consortium's SharePoint site. Data licences and access rules apply separately to source observations, derived inventories, code and licensed target databases.

### Boundary for the T2.6 interface

The repository should expose reusable operations independent of Excel or SharePoint:

```text
load an identified input revision
validate observations and mappings
resolve inventories for a declared target database
preview changes and consistency diagnostics
build the extension and run the selected reconciliation method
export outputs with provenance and validation results
```

The eventual UI can call the same operations as a CLI or automated build. Errors should carry structured fields such as check identifier, severity, sector, region, source record, explanatory message and remediation. This allows an interface to guide a user to the relevant observation rather than expose Python tracebacks or implicit fallback rules.

A credible portability pilot should trace one sector from source evidence to two target-specific representations and explain every difference attributable to classification, geography, valuation, inherited structure or estimation. Selecting the target EXIOBASE version, table type and accounting basis is a prerequisite to that pilot, not a decision made during the D2.4 audit.

Cross-database benchmarking is recorded for that later phase: compare resolved coefficients, production and trade while exposing mapping, valuation and estimation differences. It is not implemented during baseline recovery.

## Regenerating one sector

The new `scripts/export_d24_sector.py` exports a selected sector from the saved D2.4 coefficient database. It reads only that sector's parquet columns and accepts one intermediate workbook, an explicit trade source and an explicit parent policy. It does not rebuild or optimise the entire MRIO.

```bash
python scripts/export_d24_sector.py \
  --sector ZIR \
  --coefficients-dir '/path/to/D2.4 database/coefficients' \
  --source-workbook '/path/to/Add_sector_Manufacture of refined zinc.xlsx' \
  --trade-workbook '/path/to/May13/trade.xlsx' \
  --trade-sheet NTSCIF \
  --parent-policy source \
  --output-dir '/path/to/a/new/export/folder'
```

For a reviewed mapping update, use `--parent-policy matching --matching /path/to/GTAP12_matching.xlsx`. Merely changing the parent label does not rebuild coefficients previously derived from a different parent. A source-data correction still requires the upstream coefficient construction step before re-export.

The ZIR trial reproduced all 14,739 inventory coefficient records exactly when matched by their item/type/unit/origin keys. Its output and trade tables also match exactly. The trial has 163 regional inventories and 1,805 trade rows. Differences at fixed Excel cell coordinates are due to factor/satellite ordering, the DB-unit catalogue order and the parent display name. The recovered original is therefore the preferred release-repair candidate; the regenerated file remains an internal verification artifact.

Exporter saves now write a temporary file, verify its ZIP checksums and workbook sheet catalogue, then replace the destination. A failed save leaves the previous destination intact. This protects the exporter stage; it is not proof against every later cloud or publication failure. Six focused recovery/save/selection tests cover the recovery, an interrupted write and single-source selection beside an unrelated damaged workbook.

The exercised export environment is recorded in `requirements/d24-export.txt` and the audit environment manifest. It is separate from the full MARIO/CVXLAB production environment.

A compact capture of the ZIR coefficient columns, intermediate source and trade workbook is retained under `Inventory archive/ZIR recovery/2026-10-01/rebuild_inputs` in private eNextGen storage. It supports repeating this export without loading the full coefficient matrix. These are internal build inputs, not an additional public release. Original coefficient-file hashes and projected-file hashes are recorded separately.

## Running and inspecting the audit

The main audit uses Python's standard library and does not import MARIO or invoke a solver:

```bash
python scripts/audit_d24_baseline.py \
  --published-zip /path/to/published_d24.zip \
  --cleaning-dir /path/to/Inventory\ cleaning \
  --matching data/GTAP12_matching.xlsx \
  --gtap-totals '/path/to/Data split/Inventory generation/Database/GTAP Power 2023/Cache/GTAP12_X.xlsx' \
  --output-dir build/audits/my_run
```

Use a new output directory for a new evidence capture. The completed audit used the captured source files, rather than reading changing SharePoint files during comparison. Cloud-only files are reported as unread if they have not been materialised. Unreadable published workbooks are recorded and excluded from numerical results; they are not counted as successful zero-valued inventories.

Detailed results are in [the local evidence directory](../../build/audits/d24_baseline_2026-10-01/results/). Key files are `workspace_comparison.csv`, `output_lineage.csv`, `trade_lineage.csv`, `classification_comparison.csv`, `inventory_sums.csv`, `trade_output_screening.csv`, and the parent/sibling output screening tables. Additional read-only evidence scripts and logs are preserved beside them.

Representative trade, output and coefficient-sum results were independently recalculated with openpyxl. The invalid published ZIR and readable local ZIR were also independently checked. These checks validate the reported observations; they do not certify the full historical build.

Final verification checked all 193 captured source hashes, all 69 published member hashes, the 19 numerical evidence-file hashes and the audit script hash against the manifests. Those baseline checks were completed before the recovery/export changes described here; they describe the preserved snapshot, not the current working tree. The verification record is in `build/audits/d24_baseline_2026-10-01/verification.json`.

The [follow-up evidence manifest](../../manifests/d24_followup_2026-10-01.json) records the 69 project-folder file hashes, recovery, coefficient comparisons, code versions and diagnostic environment results. Its captured numerical evidence remains under `build/audits/d24_followup_2026-10-01/`. These manifests identify historical evidence; updating this report does not rewrite their results.

Primary documentary sources also include the shared `General/Deliverables/D2.4 – Enhanced GTAP Database.pdf` (sections 3.1–3.6 and annex), the signed grant agreement WP2 descriptions, and the [fixed public example revision](https://github.com/it-is-me-mario/MRIO-disaggregation-model/tree/04697834466cea3649607b5b7d87bef9599d2b16).

## Decision register

Accepted directions and their implementation status are maintained here. An accepted policy is not a claim that the corresponding code is implemented.

| ID | Agreed direction / finding | Status and remaining work |
|---|---|---|
| B01 | ZIR’s ZIP directory was truncated; all 194 parts are intact. Recovery is saved on the existing shared area. Single-sector re-export reproduces the numerical records. | Recovery verified; no replacement release published. |
| B02 | One MUN identity; the two unit catalogues cover 127 versus 143 sectors. Description-derived filenames can leave older exports behind. | Both filenames now resolve to one registry identity. Historical files remain preserved; the comma version has the fuller catalogue. |
| B03 | Parent assignments follow defined NACE activities and versioned target concordances, not discretionary confirmation. | Registry implements categorical resolution for reviewed scopes, explicit scope alternatives and unresolved states. Five resolved parents differ from the release. Complete the remaining reviews and rebuild affected quantities before migrating legacy parent lookups. |
| B04 | Missing entries can be discarded activities, aliases or stale exports; do not reactivate them automatically. | NMC/NCM differ numerically; battery parent is EEQ. PLSR/PLS needs scope/alias reconciliation. PCP/MGC duplicate names belong in an alias layer. |
| B05 | Preserve both trade sources; choose by scope, valuation, period and coverage. Avoid global replacement. | Composite codes explain some gaps. CPP/CPS/LIT June1 output matches support paired-source candidates; REE and overlaps need harmonisation. No unqualified merge applied. |
| B06 | Allow configurable tolerances on observed targets; retain consistent MRIO accounting. Output is not constrained to equal exports alone. Preserve supplied GTAP residuals. | Initial screening threshold recorded. Target bands and post-solve reporting remain to implement in the full pipeline, distinguishing pre-existing residuals from extension effects. Baseline correction is excluded. |
| B07 | Make transformations explicit and check that they implement the intended method. | Clarified: distinguish noise, source errors and intentional normalisation/caps/factor completion. No blanket correction. |
| B08 | The copy folder was an overwrite safeguard; use the normal MARIO folder. | Resolved as a prerequisite. Preserve historical reports; no need to recover the missing folder before proceeding. |
| B09 | Establish a reproducible environment and explain differences from the baseline. Preserve GTAP as supplied. | Clean pinned environment installed; 93 HYE/DEU coefficients reproduced. Earlier private closure results remain historical evidence only; the closure option is removed. Full historical execution and full-scale acceptance remain open. |
| B10 | Explain the unused cluster branch before changing it. | Traced across eight templates, including HVC. Implement an explicit allocation/overlap/unit policy with a baseline comparison in a separate change. |
| B11 | Diagnostic checks should be optional, with clear warnings and visible skipped checks. | Implemented for registry and metadata/coverage inspection, with structured actions and skipped-check lists. Extension to numerical transformations and the full runner remains. Technical failures are reported as failures. |
| B12 | Preserve source evidence versus target-resolved values; add benchmarking when multi-MRIO work begins. | Direction accepted; benchmarking deferred. |
| B13 | Use project SharePoint `Data split/Inventory generation` for operational data; keep technical evidence and original repository backups on private eNextGen storage. | Reorganised and verified locally on 2 October. Portable records remain in Git. Cloud synchronisation is not independently certified. |
| B14 | SPLITCOM was a suggestion; use MARIO/CVXLAB. | Resolved by the owner; T2.6 follows this implementation choice. |
| B15 | Advance towards `split=True` across all sectors and regions, starting with read-only joint diagnostics rather than an NFM/MOZ-only pilot. | Audit, design and 10 target scenarios cover all 67 sectors and 163 regions. May27 numerically reproduces 1,684 common Purdue outputs; June1 changes 844 beyond screening precision. Reading/source restoration alone leaves 57 joint flags, and ambiguous unit/share scenarios leave 69. Signed Tax handling, source scope/valuation and confidence bands remain open; code/data unchanged and no MRIO split solve certified. |
| B16 | Warn on joint child-output excess and proportionally reduce all resolved child targets to the regional parent total, preserving their relative shares and the supplied GTAP baseline. | Planning rule adopted after the simulation; pending implementation and coverage review. Apply `X / sum(children)` only to over-budget groups after geographic allocation, recording original/adjusted values and the warning. The 14 October clarification identifies zero residual-parent output wherever the cap binds. Any positive residual reserve needs a supported amount and revised child budget; no reserve has been selected. This is an output-target policy, not full MRIO or trade certification. |
| B17 | APS REST OF EUROPE excludes the separately reported GBR; SDG GLOBAL denotes the rest of the world. | Adopted by the owner; pending implementation. APS residual members are ALB/SRB/XER. SDG EU27 meaning, unit conflict and WORLD reconciliation remain open. |
| B18 | Verify whether REPOUT contains only nonzero output records before interpreting source omissions as missing production. | Direct GDXDUMP, workbook and GAMS Transfer checks confirm positive-only records and default-zero in-domain values in both deliveries. Preserve 388 Purdue implicit zeros and 12 explicit PCP partner zeros in the 407-case review; seven MRT coverage omissions remain distinct. Paired BLTTRD has no exporter-axis trade in the 388 cases, whereas the May13 NTSCIF screen does. Trade-source compatibility remains to resolve; no empirical completeness or automatic output/trade correction is inferred. |
| B19 | Continue the all-sector output/trade compatibility review without operational changes. | Source review covers all 67 activities: 33 positive paired BLTTRD candidates, 17 positive May13-only candidates and 17 composite/no-direct-code cases. The 13 October joint target simulation applies the adopted output/geography decisions and verifies proportional and maximum-retention trade scenarios against conditional native capacities. The 69 output caps alone do not resolve bilateral trade; the conditional aggregate LP requires about 10.9% reduction. Source scope/valuation, disputed zeros, EU27/WORLD and full MRIO feasibility remain open. No source switch or trade adjustment adopted. |
| B20 | Try an actual isolated `split=True` run to establish concrete runtime blockers. | Completed as a failure diagnosis on 13 October: all 67 published files fail the pinned reader's missing support-sheet contract; prepared DEU/ROW inputs load all 67 children and reach optimisation in three real MARIO calls. CLARABEL fails even without trade and SCS marks the unchanged no-trade model infeasible. Twelve signed child-reference values violate the current entropy domain. Full native-geography acceptance and model changes remain open; GTAP, source workbooks and operational code are unchanged. |

Broad code/data cleanup remains a later activity; the redundant narrative reports have been consolidated into this file. Historical files and baseline manifests are not silently updated when a correction candidate is created.
