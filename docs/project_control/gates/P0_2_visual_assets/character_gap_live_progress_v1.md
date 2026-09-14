# P0.2-03｜Character Gap Live Progress V1

Status: `ACTIVE / POST-BASELINE LIVE PROGRESS / WAVE 2 HOLD`

Date: `2026-09-14`

This file tracks live production progress after the locked baseline in `character_asset_gap_mapping_v1.md`.

The locked baseline remains unchanged for historical traceability:

- Mandatory Core Slots = `63`
- Confirmed Core Coverage baseline = `40`
- Core View Gap baseline = `23`
- Coverage baseline = `63.5%`

## Current live coverage

After Product Owner approval and formal Automatic Ingest of Ning Qiushui `PROFILE_LEFT` and `REAR_3Q_LEFT`:

- Current Confirmed Core Coverage = `42 / 63`
- Current Core View Gap = `21`
- Current Core Coverage = `66.7%`

`PROFILE_LEFT` remains one filled Core slot; its approved 9:16 replacement changed the Current version from V001 to V002 without changing coverage count. `REAR_3Q_LEFT` added one new confirmed Core slot.

## Ning Qiushui

Tier: `A`

Current Core Coverage: `8 / 9`

Current Core:

- `FACE_FRONT`
- `FACE_3Q_RIGHT`
- `PROFILE_LEFT`
- `PROFILE_RIGHT`
- `REAR_3Q_LEFT`
- `REAR_3Q_RIGHT`
- `BODY_FRONT`
- `BODY_BACK`

Remaining Core Gap:

- `FACE_3Q_LEFT`

### Current PROFILE_LEFT

- Role: `PROFILE_LEFT`
- Asset ID: `AST_IMG_000050`
- Filename: `CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png`
- Lifecycle: `CURRENT`
- Resolver Usage: `DEFAULT`
- SHA-256: `c53549b0b70de7fdc9da123b351aa37dcf433801b431479750287c73b84440fd`
- Supersedes: `AST_IMG_000049 / V001`
- Remote ingest commit: `eba06283cccd10a22addd02307c9012cc06d3ac0`

### Newly filled REAR_3Q_LEFT

- Role: `REAR_3Q_LEFT`
- Asset ID: `AST_IMG_000051`
- Filename: `CHAR_NING_QIUSHUI_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- Lifecycle: `CURRENT`
- Resolver Usage: `DEFAULT`
- SHA-256: `e3cbe5ca8be8584e1b3c48d3da6bb2555a619bf36f761ebeefa78734efcbfaf8`
- Remote ingest commit: `a90854dee5f2cef736b622650a2120b22bc8279e`

## P1 live progress

Locked P1 baseline = `10` Core View Gaps.

Current completed = `2 / 10`.

Current remaining = `8 / 10`.

Wave 1｜宁秋水:

- `PROFILE_LEFT` = `COMPLETE / APPROVED / INGESTED / CURRENT=V002`
- `REAR_3Q_LEFT` = `COMPLETE / APPROVED / INGESTED`

Next locked production target remains:

- 君鹭远 `PROFILE_LEFT`

P1 Wave 2 is currently held by the remaining Approved-but-Open closeout tasks.

Completed closeout items:

- `AO-01` = `COMPLETE / VERIFIED`
- `AO-02` = `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- `AO-07` = `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- `RISK-001` = `CONTROLLED / MITIGATION VERIFIED`

Remaining pre-Wave2 blockers:

- `AO-03`｜Scene Master Structured Facts + Scene / Costume / Prop / State / Variant executable Spec
- `AO-04`｜9 Character Derived Reference Sheets + dependency / staleness
- `AO-05`｜Delivery Bridge
- `AO-06`｜Real Shot Spec Resolver + Shot-level Audit reverse-trace

Current pre-Wave2 task:

`P0.2-04｜AO-03｜NEXT / NOT STARTED`

Subsequent locked P1 order remains unchanged:

1. 君鹭远 `PROFILE_LEFT`
2. 君鹭远 `REAR_3Q_LEFT`
3. 尼尔 `PROFILE_RIGHT`
4. 尼尔 `REAR_3Q_RIGHT`
5. 苏小小 `PROFILE_LEFT`
6. 苏小小 `REAR_3Q_LEFT`
7. 廖健 `PROFILE_LEFT`
8. 廖健 `REAR_3Q_LEFT`

## Governance note

This live-progress overlay does not rewrite the Product Owner-approved original 40/63 baseline. It records approved production changes after that baseline.

Only Product Owner-approved and formally ingested assets count toward live coverage.

The Wave 2 HOLD changes execution sequencing only; it does not change the locked P1 priority baseline or current coverage counts.
