# Automatic Ingest Controller V0.1｜First Live Ingest

Status: `LIVE INGEST VERIFIED / FIRST PRODUCTION ASSET COMPLETE`

Date: `2026-09-13`

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

## Live ingest result

Remote commit:

`65e7fbec9acbe970797479ae523abf9f9e4f55df`

Commit message:

`P0.2 ingest CHAR_NING_QIUSHUI PROFILE_LEFT V001`

Remote verification confirms exactly three formal ingest outputs were committed:

1. `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
2. `production/asset_registry/asset_registry.jsonl`
3. `production/asset_registry/audit_event_log.jsonl`

Registry result:

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

## Conclusion

The following production path is now verified by a real approved asset:

`Product Owner Approval → Automatic Ingest Controller → canonical local storage → Asset Registry → Audit Event Log → Git commit → GitHub publication`

This validates the minimum non-Codex ingest path for new Character PNG assets.

## Known V0.1 limitations

1. `--dry-run` currently attempts `git pull` unless `--no-pull` is explicitly supplied. Future revision should make dry-run network-independent by default.
2. Network reliability remains external to ingest logic. The first live test used a separate push command after local ingest/commit to reduce risk.
3. V0.1 intentionally blocks automatic supersession when an existing `CURRENT` asset already occupies the same `entity + role + variant + state` slot.
4. V0.1 scope is Character PNG only.
5. Gap live progress is tracked separately from the locked original Gap Mapping baseline.

## Next production action

Continue `P1 Wave 1` with:

`CHAR_NING_QIUSHUI / REAR_3Q_LEFT`

The existing locked 40/63 baseline remains historical baseline; live post-baseline coverage is tracked in `character_gap_live_progress_v1.md`.
