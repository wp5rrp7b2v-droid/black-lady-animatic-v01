# P0.2-04｜AO-02｜Long-term Registry Migration Design V1

Status: `LOCKED / PRODUCT OWNER APPROVED 2026-09-14`

Purpose: lock the engineering design for migrating D-059 approved legacy Character assets from Migration Manifest-readable state into the formal long-term Asset Registry / Audit model. This design approval does **not** mean AO-02 implementation has started or completed.

## 1. Scope

AO-02 migrates the **48 D-059 CONFIRMED + APPROVED legacy Character assets** that already exist in canonical storage into:

`Long-term Asset Registry + Append-only Audit Trail + necessary Asset Relations`

This task migrates identity and audit metadata only. It does not recopy, rename, regenerate, or re-approve PNG files.

The D-059 Migration Manifest remains immutable historical migration evidence and is not converted into a fifth runtime registry.

## 2. Eligible migration set

A D-059 Manifest row is eligible only if all of the following are true:

- `mapping_status = CONFIRMED`
- `approval_status = APPROVED`
- `target_storage_path` is present
- `canonical_filename` is present
- canonical PNG exists
- SHA-256 matches Manifest
- byte size matches Manifest
- MIME type is `image/png`

The eligible count must be exactly **48** before any formal write occurs. Otherwise AO-02 stops before mutation.

### Explicit exclusion

`CHAR_NEIL_REAR_TURN_45_SUPPLEMENTARY` remains `MAPPING_REQUIRED` and is excluded from AO-02. It receives no Asset ID, no canonical path inference, and no guessed Role. Its supplementary Role requires separate governance before any future ingest.

## 3. Asset ID allocation

The existing Automatic Ingest Controller already reserves the 48 CONFIRMED legacy rows in the Asset ID sequence, which is why new production begins at `AST_IMG_000049`.

AO-02 therefore backfills the reserved legacy identity range:

`AST_IMG_000001` through `AST_IMG_000048`.

Existing runtime IDs remain unchanged:

- `AST_IMG_000049` = Ning Qiushui PROFILE_LEFT V001 / SUPERSEDED
- `AST_IMG_000050` = Ning Qiushui PROFILE_LEFT V002 / CURRENT
- `AST_IMG_000051` = Ning Qiushui REAR_3Q_LEFT V001 / CURRENT

The 48 legacy rows are deterministically sorted by:

`canonical_entity_id → new_role → variant → state → version_no → canonical_filename`

Sorted rows 1–48 receive IDs `AST_IMG_000001–000048` respectively. Filesystem traversal order must never influence Asset ID assignment.

Once successfully applied, this mapping is immutable.

## 4. Long-term Asset Registry record

For each eligible legacy asset:

- `asset_id` = deterministic AO-02 assignment
- `entity_id` = Manifest `canonical_entity_id`
- `shot_id` = null
- `media_code` = IMG
- `asset_class` = ATOMIC
- `role` = Manifest `new_role`
- `variant` = Manifest
- `state` = Manifest
- `version_no` = Manifest
- `approval_status` = APPROVED
- `lifecycle` = Manifest
- `authority_class` = Manifest
- `resolver_usage` = Manifest
- `provenance_status` = PARTIAL
- `filename` = Manifest `canonical_filename`
- `storage_uri` = Manifest `target_storage_path`
- `sha256` = Manifest
- `mime_type` = image/png
- `byte_size` = Manifest
- `legacy_asset_id` = Manifest legacy ID
- `migration_source` = D-059

Legacy assets use `provenance_status = PARTIAL` because formal approval and file identity are provable, while the earlier generation/reference/use chain does not satisfy the current complete production audit model. Historical `USES_REFERENCE`, generation records, or other missing provenance must not be invented.

## 5. Approval time normalization

Where Manifest evidence contains a reliable approval date but no exact UTC time, Registry normalization uses:

`YYYY-MM-DDT00:00:00Z`

with:

`approval_time_precision = DATE_ONLY`

This is a technical normalization value, not a claim that approval occurred at midnight UTC.

If an otherwise eligible asset lacks a provable approval date, the entire AO-02 transaction stops before mutation.

`ingested_at` records the actual AO-02 long-term Registry migration execution time.

## 6. Single Current validation

Before writing, validate the combined set of:

- 48 legacy candidate records
- current Runtime Registry
- existing `AST_IMG_000049–000051`

Constraint:

`UNIQUE(entity_id, role, variant, state) WHERE lifecycle = CURRENT`

Any conflict stops the migration. AO-02 must not automatically supersede, renumber, rewrite Manifest data, or choose a preferred asset without Product Owner decision.

Ning Qiushui runtime states 49–51 must remain unchanged.

## 7. Asset Relations

AO-02 creates only relations that are provable from formal evidence.

`SUPERSEDES` may be created only when old/new assets share entity + role + variant + state, have unambiguous ordered versions, and lifecycle evidence clearly identifies old=`SUPERSEDED`, new=`CURRENT`.

Direction is fixed:

`NEW_ASSET SUPERSEDES OLD_ASSET`

AO-02 does not fabricate `USES_REFERENCE` or `DERIVED_FROM` relations.

`DERIVED_FROM` belongs to AO-04. `USES_REFERENCE` is validated in AO-06.

## 8. Audit model

Each successfully migrated legacy asset receives one append-only:

`ASSET_MIGRATED`

event at the actual AO-02 migration execution time.

This event means the already-approved legacy asset entered the formal long-term Registry/Audit model at that time. AO-02 does not backfill fabricated historical `ASSET_APPROVED` or `ASSET_INGESTED` events.

Any provable `SUPERSEDES` relation created by AO-02 also receives a corresponding `RELATION_CREATED` audit event.

Audit Event Log remains INSERT ONLY.

## 9. Migration Manifest immutability

The D-059 CSV/JSON Migration Manifest remains unchanged.

AO-02 creates a separate machine-readable mapping:

`ao02_legacy_asset_registry_migration_map_v1.csv`

Minimum fields:

- legacy_asset_id
- asset_id
- canonical_entity_id
- role
- variant
- state
- version_no
- lifecycle
- canonical_filename
- storage_uri
- sha256
- migration_status

Responsibilities remain separate:

- Migration Manifest = historical migration evidence
- AO-02 Migration Map = long-term identity conversion evidence
- Asset Registry = current formal asset facts

## 10. Implementation model

AO-02 must not call the normal Automatic Ingest Controller 48 times.

Implement a dedicated one-time, testable:

`Legacy Registry Migration Controller`

Its controlled pipeline is:

`Manifest → validate → deterministic ID plan → Registry/Audit/Relations transaction`

It does not copy, rename, or modify PNG binaries.

## 11. Atomicity

AO-02 is all-or-nothing.

Before mutation, construct and validate the complete target states for:

- Asset Registry
- Asset Relations
- Audit Event Log
- AO-02 Migration Map

Only after all validations pass may all controlled files be written.

Any failure restores the complete pre-AO-02 state. A partially applied result such as `23/48` is prohibited.

## 12. Idempotency

After a successful application, re-running the controller against the same source state must return:

`ALREADY_APPLIED / NO CHANGE`

and must not:

- allocate a second Asset ID set
- append another 48 migration events
- duplicate relations
- alter original migration timestamps

If only part of the expected migration exists or any identity/hash/path differs, return:

`PARTIAL_OR_CONFLICTING_MIGRATION`

and stop without self-repair.

## 13. Network publication boundary

Local Registry migration and remote GitHub publication are separate completion dimensions.

If transaction + tests + local commit succeed but push fails:

`COMPLETE / PENDING_REMOTE_PUBLICATION`

The migration must not be rerun. After network recovery, retry publication of the existing commit only.

Only after verifying:

`HEAD == origin/main`

may AO-02 be considered remotely verified.

This failure/recovery sequence may also serve as real evidence for AO-07.

## 14. Completion evidence

AO-02 implementation must produce:

`ao02_legacy_asset_registry_migration_v1.md`

recording at least:

- source count
- migrated count
- excluded count
- Asset ID range
- Single Current validation
- SHA/storage validation
- Relations created
- Audit Events created
- Neil MAPPING_REQUIRED status
- idempotency test
- rollback/failure test
- Git commit and remote verification

## 15. Definition of Done

AO-02 is eligible for Product Owner completion approval only when all 48 eligible legacy assets are represented in the long-term Registry as `AST_IMG_000001–000048`, while:

- `AST_IMG_000049–000051` remain unchanged
- no duplicate Asset ID exists
- no duplicate storage URI exists
- no duplicate Current exists
- all canonical PNG hashes verify
- D-059 Manifest remains unchanged
- Neil MAPPING_REQUIRED is not migrated
- legacy provenance is not fabricated as COMPLETE
- Audit remains append-only
- only provable Supersedes relations are created
- migration is idempotent
- controlled failure leaves no partial migration
- tests pass
- GitHub publication is remotely verified

Only then may AO-02 become `COMPLETE / VERIFIED` and AO-03 become the next task.

P1 Wave 2 remains HOLD.

## 16. Out of scope

AO-02 does not:

- implement Scene Master facts
- create Derived Reference Sheets
- build real Shot Specs
- create `USES_REFERENCE`
- implement Delivery Bridge
- finish the GitHub Network Runbook
- produce missing Character views
- govern Neil REAR_TURN_45
- generate new visual assets

Those remain AO-03–AO-07 or separate governed work.
