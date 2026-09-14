# P0.2-04｜AO-02｜Legacy Character Assets → Long-term Registry / Audit

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Date: `2026-09-14`

Product Owner approval: `EXPLICITLY APPROVED IN CHAT 2026-09-14`

## 1. Scope

AO-02 migrates the 48 D-059 `CONFIRMED + APPROVED` legacy Character assets from Migration Manifest-readable state into the formal long-term Asset Registry / Append-only Audit model.

This migration changes identity and audit metadata only. It does not copy, rename, regenerate, or re-approve PNG files.

## 2. Source / Exclusion

- D-059 Manifest rows: `49`
- Eligible legacy assets: `48`
- Migrated assets: `48`
- Explicitly excluded: `CHAR_NEIL_REAR_TURN_45_SUPPLEMENTARY`
- Exclusion state remains: `MAPPING_REQUIRED / NOT MIGRATED`

## 3. Asset ID Migration

Deterministic backfill range:

`AST_IMG_000001..AST_IMG_000048`

Existing runtime Asset IDs preserved unchanged:

- `AST_IMG_000049`
- `AST_IMG_000050`
- `AST_IMG_000051`

Post-migration Asset Registry record count: `51`.

## 4. Validation Results

Pre-apply dry-run:

- eligible count = `48`
- Single Current validation = `PASS`
- SHA / storage validation = `PASS`
- migration events planned = `48`
- provable relations planned = `1`
- relation events planned = `1`

The single AO-02 relation is the provable Ning Qiushui `REAR_3Q_RIGHT` V002 `CURRENT` superseding V001 `SUPERSEDED` relation.

Post-apply record counts:

- `production/asset_registry/asset_registry.jsonl` = `51`
- `production/asset_registry/asset_relations.jsonl` = `2`
- `production/asset_registry/audit_event_log.jsonl` = `56`
- `ao02_legacy_asset_registry_migration_map_v1.csv` = `49` lines including header (`48` asset rows)

## 5. Safety / Immutability

Verified after apply:

- Character PNG working tree changes = none
- D-059 CSV Manifest diff = none
- D-059 JSON Manifest diff = none
- `git diff --check` = clean
- unrelated local ZIP / `production/audio/` were not included in AO-02 changes

Legacy migrated records use `provenance_status = PARTIAL`; missing historical generation/reference provenance was not fabricated.

## 6. Idempotency / Rollback

Automated AO-02 tests:

- deterministic ID plan independent of Manifest traversal order = PASS
- injected controlled write failure restores all controlled files = PASS
- partial migration is blocked without self-repair = PASS
- successful apply second run is idempotent = PASS
- wrong eligible count blocks before planning = PASS

Test result: `5/5 PASS`.

Second real run after successful apply returned:

- `status = ALREADY_APPLIED`
- `change = NO CHANGE`
- `migrated_count = 48`
- `asset_id_range = AST_IMG_000001..AST_IMG_000048`

## 7. Publication

Migration commit:

`4803b928baaa38d875e9c6edd46f4a458e627b61`

Commit message:

`P0.2 AO-02 migrate legacy character assets to long-term registry`

Remote verification:

- `git-proxy-auto push origin main` completed successfully
- final Terminal check returned `FINAL_STATUS=REMOTE_VERIFIED`
- GitHub `main` independently confirmed at commit `4803b928baaa38d875e9c6edd46f4a458e627b61`

## 8. Definition of Done Review

AO-02 Definition of Done is satisfied:

- 48 eligible legacy assets represented as `AST_IMG_000001–000048`
- `AST_IMG_000049–000051` preserved
- no duplicate Asset ID
- no duplicate storage URI
- no duplicate Current
- canonical PNG hashes/storage validated
- D-059 Manifest unchanged
- Neil MAPPING_REQUIRED asset excluded
- legacy provenance not fabricated as COMPLETE
- append-only migration/audit records created
- only provable SUPERSEDES relation added
- migration idempotent
- controlled failure rollback test passed
- automated tests passed
- GitHub publication remotely verified

## 9. Approval / Closeout

Product Owner explicitly approved AO-02 in Chat on `2026-09-14`.

Final status:

`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

AO-03 is the next formal Approved-but-Open closeout task.

P1 Wave 2 remains HOLD until AO-01～AO-07 are all `COMPLETE / VERIFIED` and the remaining resume-lock conditions are satisfied.

Execution routing note: AO-02 was completed through Chat-led design/GitHub updates plus Terminal execution/verification. No Codex engineering task was required, so AO-02 does not consume a new D-### number.