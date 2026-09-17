# Production Asset Registry Runtime

本目录用于 Visual Asset Management System V1 的运行时正式登记数据。

当前轻量实现由 `scripts/automatic_ingest_controller_v0_1.py` 自动维护：

- `asset_registry.jsonl`：正式 Asset Registry 的 V0.1 运行时记录；仅写入 Product Owner 明确批准并完成正式入库的新生产资产。
- `entity_registry.jsonl`：稳定 Entity identity；AO-03 首先登记两个 Scene Entities。
- `scene_state_profiles.json`：Scene stable facts、多维 State Profiles、source master 与 evidence/status 的 executable mapping。
- `audit_event_log.jsonl`：append-only Audit Event Log；V0.1 对每次正式入库至少写入 `ASSET_APPROVED` 与 `ASSET_INGESTED`。
- `asset_relations.jsonl`：受控替换时创建，记录 `NEW_ASSET SUPERSEDES OLD_ASSET`；无替换时无需空文件。

## 与 D-059 Migration Manifest 的关系

`docs/project_control/gates/P0_2_visual_assets/migration_evidence/character_asset_migration_manifest_v1.csv`
仍是旧资产迁移证据，不作为新生产资产的登记目标。

V0.1 在执行冲突检查、版本计算和 Asset ID 顺序预留时会同时读取：

1. D-059 Migration Manifest；
2. 本目录 `asset_registry.jsonl`。

因此新生产资产不会反写 Migration Manifest。

## Automatic Ingest Controller V0.1 边界

- Controller 仅支持 Character PNG；AO-03 Scene records 由 D-067 对既有 approved source files 一次性 formalization，并由 resolver/tests 校验；
- 仅处理已由 Product Owner 明确批准的结果；
- 默认遇到 Single Current 冲突仍停止。只有 Product Owner 明确选择替换、同时传入 `--po-approved --supersede-current`，才允许将唯一的 Runtime Registry CURRENT 标记为 `SUPERSEDED`，并把连续下一版本登记为 `CURRENT`。Migration Manifest-only CURRENT 不支持替换；
- 受控替换保留旧 PNG、旧文件名、SHA 和版本号，并在 Asset Relations 与 append-only Audit Event Log 中记录关系和 `ASSET_SUPERSEDED` 事件；正式写入失败会恢复执行前的 Registry、Relations、Audit 和 Git 暂存状态；
- `--supersede-current --dry-run --po-approved` 只预览，不拉取、推送或写正式文件；`--inspect-current` 供一键入口只读判断是否需要二次确认；
- 不自动修改 Dashboard / Project State / Character Gap Mapping 文档；这些仍由主流程 Chat 在远端核验后更新；
- `tmp/ingest_receipts/` 为本地执行回执，不进入正式 Registry。

Schema authority：
`docs/project_control/gates/P0_2_visual_assets/entity_asset_registry_schema_v0_3.md`
