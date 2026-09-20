# P0.2-03｜Character Gap Live Progress V1

Status: `EOD PAUSED / P1 VISUAL 10/10 PO APPROVED / P2 7/7 GENERATED, 6/7 PO APPROVED / 14 APPROVED CORE VIEWS TRANSPORT-INGEST PENDING`

Date: `2026-09-20 EOD`

This file tracks live production progress after the locked baseline in `character_asset_gap_mapping_v1.md`.

## Locked baseline

- Mandatory Core Slots = `63`
- Confirmed Core Coverage baseline = `40`
- Core View Gap baseline = `23`
- Coverage baseline = `63.5%`

The baseline remains unchanged for historical traceability.

## Current formal live coverage

Only Product Owner-approved **and formally ingested** assets count toward formal coverage.

- Current Confirmed Core Coverage = `42 / 63`
- Current Core View Gap = `21`
- Current Core Coverage = `66.7%`
- Formal P1 completion = `2 / 10`

Formally ingested P1 views:

- Ning Qiushui `PROFILE_LEFT` = `CURRENT V002 / APPROVED / INGESTED`
- Ning Qiushui `REAR_3Q_LEFT` = `CURRENT V001 / APPROVED / INGESTED`

No 2026-09-20 visual approval is counted in formal coverage until exact-byte publication + Automatic Ingest succeeds.

## P1 visual production

- Locked P1 baseline = `10`
- PO-approved visual results = `10 / 10`
- Formally ingested = `2 / 10`
- Approved but transport/ingest pending = `8 / 10`

Pending P1: Jun PROFILE_LEFT V002; Jun REAR_3Q_LEFT V001; Neil PROFILE_RIGHT V001; Neil REAR_3Q_RIGHT V001; Su PROFILE_LEFT V001; Su REAR_3Q_LEFT V001; Liao PROFILE_LEFT V001; Liao REAR_3Q_LEFT V001.

## P2 visual production

Locked P2 baseline = `7`: Ning FACE_3Q_LEFT; Jun FACE_3Q_LEFT; Neil FACE_3Q_RIGHT; Wen PROFILE_LEFT; Wen REAR_3Q_LEFT; Castle Young Master PROFILE_LEFT; Castle Young Master REAR_3Q_LEFT.

- Generated = `7 / 7`
- Explicit Product Owner approval = `6 / 7`
- Formal ingest = `0 / 7`

PO-approved P2 views pending publication/ingest: Ning FACE_3Q_LEFT V001; Jun FACE_3Q_LEFT V001; Neil FACE_3Q_RIGHT V001; Wen PROFILE_LEFT V001; Wen REAR_3Q_LEFT V001; Castle Young Master PROFILE_LEFT V001.

PO review pending: Castle Young Master `REAR_3Q_LEFT V001` = `GENERATED / WORK INTERNAL PASS / PO REVIEW PENDING / DO NOT INGEST`.

## Approved-but-uningested exact source identities

Total = `14`.

### P1

| Asset | Bytes | SHA-256 |
|---|---:|---|
| `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png` | 1,938,522 | `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c` |
| `CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png` | 1,941,468 | `97ad38c259274eced5be61035cda4c28df72babe084fc452fbbc927a2a6da21e` |
| `CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png` | 1,693,697 | `17dff7f50b7392915db6d74f1d04b506f2de884e9069ba11f9013bbe2fce8262` |
| `CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png` | 1,656,490 | `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6` |
| `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png` | 2,088,722 | `3af763a5d96d043ccce061459b16af93114e0bcf59d44a98c9df17130c97868c` |
| `CHAR_SU_XIAOXIAO_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png` | 2,096,951 | `1fb43ffef96d36bebef05a6d08f297108684c026b9bd64a11543cd9614bd06f7` |
| `CHAR_LIAO_JIAN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png` | 1,889,115 | `421a1bd6052bcf291a374dccededb32a25a5f6077cfad21168e90fa2b28664bd` |
| `CHAR_LIAO_JIAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png` | 1,917,221 | `2d3a223a7365a49f5b912df98aeb5fe18d4227507f5c093f42360399a7de91be` |

### P2

| Asset | Bytes | SHA-256 |
|---|---:|---|
| `CHAR_NING_QIUSHUI_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png` | 1,761,408 | `8d92bcc601220654499f7be57fc83411c57dedccc44e8f764cc65ce1b840334e` |
| `CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png` | 2,002,451 | `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b` |
| `CHAR_NEIL_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png` | 1,738,212 | `92ef0fc973093c7cc99f3b70f3aab1fabd09d2d82c29921e72065f0d7b9ac366` |
| `CHAR_WEN_QINGYA_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png` | 2,027,950 | `3068d9ad2c345191d3e5cf7a5a657ba64d61d01c5077d9c04c05521e7db36309` |
| `CHAR_WEN_QINGYA_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png` | 1,902,463 | `2f52fe5067671d52f5b35eb9dc83567dbcd9bd76030ef1280a35e88e102c7344` |
| `CHAR_CASTLE_YOUNG_MASTER_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png` | 2,030,361 | `142448eb20d63a9576e9600c15cfdc0b2885252517781659b36d086572764589` |

All listed production candidates are 941 × 1672 PNGs.

## Current production boundary

- P1 visual production: `COMPLETE / 10/10 PO APPROVED`
- P2 visual generation: `COMPLETE / 7/7 GENERATED`
- P2 Product Owner approvals: `6/7`
- Castle Young Master `REAR_3Q_LEFT V001`: explicit PO approval still required.
- P3 Black Lady 6-view lateral rebuild: `NOT STARTED`

## Next actions

1. Resolve PO review for Castle Young Master `REAR_3Q_LEFT V001`.
2. Gather all approved exact source binaries.
3. Exact-byte publish to canonical GitHub paths.
4. Re-read remote binaries and verify SHA-256 / byte size.
5. Run Automatic Ingest; verify Registry / Audit / Single Current.
6. Update formal coverage only after successful ingest.
7. Perform GitHub → Local truth sync before local formal production resumes.
8. Continue AO-06 / D-069 separately; do not allocate D-070.

## Governance note

AO-06 remains mandatory before P0.2 final closeout / READY_FOR_APPROVAL, but it does not block Character image production. P0.3 remains QUEUED / DO NOT START EARLY.
