# AO-01｜Four legacy registers reconciliation V1

Status: `INCOMPLETE / PO DECISION REQUIRED`

Evidence date: 2026-09-14

Baseline: local `0159ec57809040a3baeb19222d5b1e35f19d7de7`; fetched `origin/main` `197d1df368567ba896547c05767fe9ee65a4dc0c`; fast-forwarded before this review.

## Scope and authority

This is AO-01 evidence only. It does not ingest the 48 D-059 legacy assets, change an Asset ID, approve a Gate, or release the Wave 2 hold. Current authority remains `entity_asset_registry_schema_v0_3.md`, the Runtime Asset Registry/Relations/Audit Event Log, canonical Character storage, and the migration-only D-059 Manifest. A reference to an old CSV is not evidence that its contents or authority are available now.

## Source inventory and locating result

Searched the entire working tree including ignored/hidden/untracked paths with `rg --files --hidden --no-ignore`, a case-insensitive filename scan, `find`, all reachable Git history (`git log --all --name-only`), `origin/main` tree, and the untracked D-059 ZIP listing. No exact, case variant, duplicate, backup, old, or archive copy of any of the four named CSVs was found. Git shows no tracked historical copy in reachable history. The ZIP contains a different migration manifest, not these registers. The untracked ZIP and audio files were left untouched.

| Register | Exact current path / presence | Git state | Rows | Headers | SHA-256 | Last confirmable source |
|---|---|---|---|---|---|---|
| `SHOT_REGISTER.csv` | `NOT PRESENT IN CURRENT WORKTREE` | never found tracked in reachable Git history; no untracked copy | unknown | unknown | unavailable | `asset_authority_audit.md` §5; `entity_asset_registry_schema_v0_3.md` Shot composition rule |
| `ASSET_REGISTER.csv` | `NOT PRESENT IN CURRENT WORKTREE` | same | unknown | unknown | unavailable | `asset_authority_audit.md` §5; `approved_open_tasks_v1.md` AO-01 |
| `IMAGE_REGISTER.csv` | `NOT PRESENT IN CURRENT WORKTREE` | same | unknown | unknown | unavailable | `asset_authority_audit.md` §5; D-059 Manifest `evidence` column refers to legacy IMAGE_REGISTER “when matched” |
| `IMAGE_RENAME_MANIFEST.csv` | `NOT PRESENT IN CURRENT WORKTREE` | same | unknown | unknown | unavailable | `asset_authority_audit.md` §5; `approved_open_tasks_v1.md` AO-01 |

The `107` image-library figure in `asset_authority_audit.md` is an older audit scope, not the current canonical Character PNG count. No row data or source path for the missing registers can be inferred from that figure. No CSV was reconstructed.

## Register responsibilities and final disposition

| Register | Current role / disposition | Authority and successor |
|---|---|---|
| `SHOT_REGISTER.csv` | **HISTORICAL EVIDENCE / CURRENT OPERATIONAL ROLE UNVERIFIED**. It may contain Shot membership/composition facts. Retain if recovered; do not archive or replace its production role without inspection. | Canonical Shot ID and schema rules are locked; operational Shot Register/Shot Spec is not supplied by this CSV in the current worktree. |
| `ASSET_REGISTER.csv` | **SUPERSEDED BY RUNTIME REGISTRY / HISTORICAL EVIDENCE**, provisional pending source inspection. | Runtime `asset_registry.jsonl`, `asset_relations.jsonl`, `audit_event_log.jsonl` for formal long-term assets. It cannot override those records. |
| `IMAGE_REGISTER.csv` | **MIGRATION / APPROVAL PROVENANCE EVIDENCE ONLY**, provisional pending source inspection. | D-059 Manifest records selected legacy-to-canonical Character mappings. Runtime Registry is the long-term successor; AO-02 handles the 48 approved legacy records. |
| `IMAGE_RENAME_MANIFEST.csv` | **RENAME EVIDENCE ONLY / HISTORICAL EVIDENCE**, provisional pending source inspection. | D-059 Manifest currently provides legacy/uploaded/canonical names and paths for Character migration. Actual old rename rows and completion flags cannot be confirmed. |

No absent legacy CSV is declared current authority. These dispositions preserve potentially unique Shot facts while avoiding a silent promotion of missing sources.

## Reconciliation performed against available sources

- D-059 CSV parses to **49 rows**: 48 confirmed mappings with canonical paths (47 `CURRENT`, one `SUPERSEDED`) and one Neil `MAPPING_REQUIRED` row with no canonical filename/path. All 48 referenced canonical PNGs exist and match recorded SHA-256 and byte size. The Neil row is intentionally unmigrated per D-059 and is **not** a missing-file error. The legacy file is present only inside the untracked D-059 ZIP under `legacy_pending_mapping/neil/`.
- Runtime Asset Registry parses to **3 rows**, distinct asset IDs and storage URIs. All three PNGs exist and match recorded SHA-256 and size. Relations JSONL parses to one `SUPERSEDES` edge (`AST_IMG_000050 → AST_IMG_000049`); Audit Event Log parses. All Runtime paths are separate from D-059 Manifest paths. The 48 manifest-mapped assets have **no Runtime rows yet**; this is the AO-02 boundary, not an AO-01 ingest action.
- Canonical Character storage contains **51 PNGs**: 48 D-059 files plus 3 Runtime files. Every PNG is referenced by one of those two sources; **0 orphan canonical PNGs** under this storage root. `.DS_Store` is a non-PNG local metadata file, not an Asset. No confirmed stale canonical storage path or filename among these 51 rows/files.
- The Manifest's `legacy_filename` and `uploaded_filename` preserve old names; `canonical_filename`/`target_storage_path` identify migrated files. D-059 completion evidence confirms the 48 published migrations. Whether any row of the missing `IMAGE_RENAME_MANIFEST.csv` was complete, incomplete, duplicate, or inconsistent is unverified.
- Within the Manifest and Runtime data, there are **0 duplicate canonical paths**, **0 duplicate Runtime asset IDs**, **0 duplicate Current slots** keyed by `entity_id + role + variant + state`, and **0 cross-source storage path overlaps**. No old-Register duplicate-row or duplicate-Current claim is possible without the four CSVs.
- `AST_IMG_000049` is Ning Qiushui `PROFILE_LEFT` V001 `SUPERSEDED`; `AST_IMG_000050` is V002 `CURRENT`; `AST_IMG_000051` is `REAR_3Q_LEFT` V001 `CURRENT`. A stale resolver regression assertion was updated to check current effective version semantics.
- The canonical Shot mapping remains `A01_REBOOT → A01` through `A08_REBOOT → A08` by schema rule. No historical Shot Register row was rewritten. A08 mapping does not imply A08 approval.

## Conflict, orphan, duplicate, and legacy naming findings

| Finding | Observed result | Disposition |
|---|---|---|
| Authority conflict in available formal sources | 0 observed | Runtime and schema remain authoritative. Missing old CSVs prevent an all-source conflict exclusion. |
| Orphan old-register rows / duplicate old-register rows | **UNKNOWN** | Requires original rows; no zero finding asserted. |
| Orphan canonical Character PNGs | 0 of 51 | All referenced by Manifest or Runtime. |
| Duplicate Current in available sources | 0 | Ning V001 is `SUPERSEDED`; V002 alone is Current. Missing CSV contents still cannot be checked. |
| Stale paths / stale filenames in available canonical references | 0 confirmed | Legacy names in Manifest are intentional history; status of missing rename register is unknown. |
| Unresolved mappings | Neil `REAR_TURN_45` one `MAPPING_REQUIRED`; plus four unavailable CSV source inventories | Neil stays excluded from canonical storage; old-row mapping checks await source or explicit PO scope decision. |
| Manifest / Runtime coverage | 48 Manifest-only D-059 assets | AO-02, explicitly out of scope here. |

## Unresolved items and completion assessment

Four source files are unavailable, and reachable Git history contains no copies. Consequently their exact paths, row counts, headers, hashes, row-to-file links, Shot composition facts, rename completion, orphan rows, and duplicate rows cannot be verified. The four source dispositions above are limited to roles supported by Project Control evidence; they are not a claim of row-level final reconciliation. This prevents AO-01 completion conditions 1, 3–4, and 7–8 from being fully evidenced.

**AO-01 remains `INCOMPLETE / PO DECISION REQUIRED`.** The Product Owner must either provide the four original CSVs or explicitly decide that an evidence-only reconciliation with unavailable legacy sources is sufficient, including how unique Shot composition information will be recovered or represented. Until then, AO-01 stays open, AO-02 is the named next action but is **not started**, and P1 Wave 2 stays on HOLD. No Project Control completion state/revision is advanced by this incomplete assessment.
