# Automatic Ingest Controller V0.1｜First Live Ingest

Status: `LIVE INGEST VERIFIED / HISTORICAL FIRST-INGEST EVIDENCE`

Date: `2026-09-13`

> EOD consistency note：本文件保留“第一次真实 ingest”发生时的证据，不代表该资产仍是 CURRENT。`AST_IMG_000049 / PROFILE_LEFT V001` 后续因 Character reference 画幅标准纠正，已通过受控 supersession 被 `AST_IMG_000050 / V002` 替代，当前 lifecycle = `SUPERSEDED`。当前状态以 `asset_registry.jsonl`、`character_gap_live_progress_v1.md` 与 `core/project_state.json` 为准。

## Purpose

验证在不使用 Codex 的正常生产路径下，Product Owner 明确批准后的最终图片能否通过轻量 Automatic Ingest Controller 自动完成 canonical 命名、本地正式存储、长期 Asset Registry、Append-only Audit Event Log、Git commit 与 GitHub publication。

## Test asset

- Entity: `CHAR_NING_QIUSHUI`
- Role: `PROFILE_LEFT`
- Variant: `DEFAULT`
- State: `DEFAULT`
- Authority: `AUXILIARY`
- Resolver Usage: `DEFAULT`
- Task: `P0.2-03 / P1 Wave 1`
- Product Owner approval: explicit approval in main Chat on `2026-09-13`

## Dry-run result

- Status: `DRY_RUN PASS`
- Asset ID: `AST_IMG_000049`
- Version: `V001`
- Canonical filename: `CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
- Storage URI: `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `bbb4fbbb055af001307019b92665fad14e35694da0bcde206af0d419c9d42c0e`
- Byte size: `2763545`

## First live ingest result

Remote commit:

`65e7fbec9acbe970797479ae523abf9f9e4f55df`

Commit message:

`P0.2 ingest CHAR_NING_QIUSHUI PROFILE_LEFT V001`

Remote verification confirmed exactly three formal ingest outputs were committed at that time:

1. `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
2. `production/asset_registry/asset_registry.jsonl`
3. `production/asset_registry/audit_event_log.jsonl`

Registry result **at first ingest time**:

- `approval_status = APPROVED`
- `lifecycle = CURRENT`
- `authority_class = AUXILIARY`
- `resolver_usage = DEFAULT`
- `provenance_status = COMPLETE`
- `asset_id = AST_IMG_000049`

Audit result:

- `ASSET_APPROVED` recorded with `actor_type = PRODUCT_OWNER`
- `ASSET_INGESTED` recorded with `actor_type = SYSTEM`
- controller actor = `AUTOMATIC_INGEST_CONTROLLER_V0.1`

## Later lifecycle update｜same day

Character production format was corrected to 9:16. `PROFILE_LEFT V001` was retained for audit history but replaced by the approved 9:16 version:

- Old: `AST_IMG_000049 / V001` → `SUPERSEDED`
- New: `AST_IMG_000050 / V002` → `CURRENT`
- Controlled supersession commit: `eba06283cccd10a22addd02307c9012cc06d3ac0`
- Relation semantics: `NEW SUPERSEDES OLD`

Therefore this document proves the **first live ingest mechanism**, not the current visual version of `PROFILE_LEFT`.

## Conclusion

The following production path was verified by a real approved asset:

`Product Owner Approval → Automatic Ingest Controller → canonical local storage → Asset Registry → Audit Event Log → Git commit → GitHub publication`

Subsequent D-061～D-065 work extended this baseline with one-click ingest, P1 role generalization, unified Migration + Runtime resolution, controlled Current supersession and macOS Bash launcher compatibility.

## V0.1 limitations at first test / later resolution

1. Original dry-run network behavior：later hardened by D-061 workflow changes.
2. Network reliability remains external to ingest logic；2026-09-13 GitHub HTTP/2 instability was mitigated for this repo by Git HTTP/1.1.
3. Original V0.1 blocked existing CURRENT replacement；D-064 added explicit PO-approved controlled supersession while retaining block-by-default behavior.
4. Character PNG remains the validated production scope of this controller path.
5. Gap live progress remains separate from the locked original Gap Mapping baseline.

## Current production continuation

`P1 Wave 1` is now complete：

- `PROFILE_LEFT` → `AST_IMG_000050 / V002 / CURRENT`
- `REAR_3Q_LEFT` → `AST_IMG_000051 / V001 / CURRENT`

Next P1 target：

`CHAR_JUN_LUYUAN / PROFILE_LEFT`

The locked 40/63 baseline remains historical baseline；current live progress is maintained in `character_gap_live_progress_v1.md`.
