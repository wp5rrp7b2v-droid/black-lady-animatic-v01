# Production Asset Registry Runtime

本目录用于 Visual Asset Management System V1 的运行时正式登记数据。

当前轻量实现由 `scripts/automatic_ingest_controller_v0_1.py` 自动维护：

- `asset_registry.jsonl`：正式 Asset Registry 的 V0.1 运行时记录；仅写入 Product Owner 明确批准并完成正式入库的新生产资产。
- `audit_event_log.jsonl`：append-only Audit Event Log；V0.1 对每次正式入库至少写入 `ASSET_APPROVED` 与 `ASSET_INGESTED`。

## 与 D-059 Migration Manifest 的关系

`docs/project_control/gates/P0_2_visual_assets/migration_evidence/character_asset_migration_manifest_v1.csv`
仍是旧资产迁移证据，不作为新生产资产的登记目标。

V0.1 在执行冲突检查、版本计算和 Asset ID 顺序预留时会同时读取：

1. D-059 Migration Manifest；
2. 本目录 `asset_registry.jsonl`。

因此新生产资产不会反写 Migration Manifest。

## V0.1 边界

- 仅支持 Character PNG；
- 仅处理已由 Product Owner 明确批准的结果；
- 不自动 supersede 已存在的 CURRENT；如检测到 Single Current 冲突则停止；
- 不自动修改 Dashboard / Project State / Character Gap Mapping 文档；这些仍由主流程 Chat 在远端核验后更新；
- `tmp/ingest_receipts/` 为本地执行回执，不进入正式 Registry。

Schema authority：
`docs/project_control/gates/P0_2_visual_assets/entity_asset_registry_schema_v0_3.md`
