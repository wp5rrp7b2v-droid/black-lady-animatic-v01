# P0.2-03｜Character Gap Live Progress V1

Status: `ACTIVE / POST-BASELINE LIVE PROGRESS / P1 PRODUCTION RESUMED`

Date: `2026-09-19 EOD`

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

Formal completed = `2 / 10`.

Formal remaining = `8 / 10`.

Only Product Owner-approved **and formally ingested** assets count toward these numbers.

### Formally ingested

Wave 1｜宁秋水:

- `PROFILE_LEFT` = `COMPLETE / APPROVED / INGESTED / CURRENT=V002`
- `REAR_3Q_LEFT` = `COMPLETE / APPROVED / INGESTED`

### Product Owner approved but NOT yet ingested

These four views are approved visual results but do **not** yet change coverage:

- 君鹭远 `PROFILE_LEFT V002` — `PO APPROVED / TRANSPORT-INGEST PENDING`
- 君鹭远 `REAR_3Q_LEFT V001` — `PO APPROVED / TRANSPORT-INGEST PENDING`
- 尼尔 `PROFILE_RIGHT V001` — `PO APPROVED / TRANSPORT-INGEST PENDING`
- 尼尔 `REAR_3Q_RIGHT V001` — `PO APPROVED / TRANSPORT-INGEST PENDING`

At 2026-09-19 EOD, all four canonical GitHub target paths were independently checked and were still absent. No Registry / Audit / Core Coverage update is claimed.

### Current production target

- 苏小小 `PROFILE_LEFT V001` — dedicated Delivery Bundle workflow created; artifact build pending.

Remaining locked P1 order after the current target:

1. 苏小小 `PROFILE_LEFT`
2. 苏小小 `REAR_3Q_LEFT`
3. 廖健 `PROFILE_LEFT`
4. 廖健 `REAR_3Q_LEFT`

The original full P1 order remains historically locked; Jun/Neil production steps have now reached PO-approved visual state but await formal ingest.

## Governance note

This live-progress overlay does not rewrite the Product Owner-approved original 40/63 baseline.

Current formal coverage remains `42 / 63 = 66.7%` and P1 formal completion remains `2 / 10` until the four pending exact-byte assets are formally ingested.

BL-D-039 / RC-020 removed the sequencing HOLD on P1 production only. AO-06 remains mandatory before P0.2 final closeout / READY_FOR_APPROVAL.
