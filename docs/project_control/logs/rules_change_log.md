# Rules Change Log｜BLACK-LADY-001

| ID | 日期 | 规则变化 | 状态 |
|---|---|---|---|
| RC-011 | 2026-09-12 | 资产永久 ID 与文件命名规则锁定：`asset_id` 采用 `AST_<MEDIA_CODE>_<6-digit sequence>`，当前媒体代码包括 `IMG / VID / AUD`，并预留 `MDL / TEX`；Asset ID 只承担永久唯一识别，不编码人物、角度、版本、审批或生命周期。Entity ID 使用 `CHAR_* / SCENE_* / PROP_* / COSTUME_*` 等稳定业务前缀；人类可读文件名默认采用 `<ENTITY_ID>_<ROLE>_<VARIANT>_V###.<ext>`。Reference Sheet 若实体为图片仍使用 `AST_IMG_*`，其业务职责由 Registry 的 `asset_class` 表达。Asset ID 与正式文件名均由 Automatic Ingest 自动分配/生成，Product Owner 不承担手工编号、命名或登记。 | ACTIVE / P0.2-02 ASSET NAMING RULE LOCKED |
| RC-010 | 2026-09-12 | Character Asset 规则锁定为 Tier 分级：Tier A 核心角色 9-view；Tier B 重要配角 6-view 并固定 primary side；Tier C 普通角色 3-view minimum；Tier D 群演/一次性角色不建完整 Core Set。Tier 由叙事重要性、出场频率、视角复杂度、连续性敏感度与动画需求共同决定；Production Need 可触发升级。同类视图必须统一角度、背景、光线、机位和人物比例；Atomic Character Asset 与 Derived Character Reference Sheet 分离；正常生产由 Resolver 自动选图，缺失关键视角时返回 `REFERENCE_GAP`。 | ACTIVE / P0.2-02 CHARACTER RULE LOCKED |
| RC-009 | 2026-09-12 | 视觉资产管理规则升级：只有 Product Owner 明确批准的视觉结果可进入正式 Asset Registry；人物/场景/服装/道具统一采用 Entity → Asset 模型；Approval 与 Lifecycle 分离，正式生命周期为 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；Atomic Master 与 Derived Reference Sheet 分离并记录依赖；正常生产目标改为 `Shot / Task Spec → Reference Resolver → Reference Package`，取消 Product Owner 的例行手工挑图、下载、命名、存储与登记；所有正式资产必须具备来源、审批、版本、替代、依赖和生产调用 Audit Trail。 | ACTIVE / P0.2 SYSTEM RULE LOCKED |
| RC-008 | 2026-09-12 | 正式审批权锁定为 Product Owner：任何 Gate / Phase 即使已满足验收条件，ChatGPT / Codex 也只能标记 `READY_FOR_APPROVAL`；只有 Product Owner 明确批准后，才能更新为 `PASS / APPROVED / CLOSED`。P0.1 的 PASS 由 Product Owner 在 2026-09-12 当前 Chat 明确确认。 | ACTIVE |
| RC-007 | 2026-09-12 | Project Control 目录升级为 1.1：`core/`、`logs/`、`gates/`、`dashboard/`、`archive/`；生产源数据移出 Project Control，统一进入 `source_material/`。 | ACTIVE |
| RC-005 | 2026-09-11 | Dashboard V002 获批：必须可视化总体 Gate 完成度、当前 Gate 状态、阶段目标和真实 Blocker；项目控制规则区明确命名为 `Project Control Rules`。 | ACTIVE |
| RC-006 | 2026-09-11 | canonical repo 锁定为 `wp5rrp7b2v-droid/black-lady-animatic-v01`；新的项目 Chat 以其 `main/docs/project_control/` 为正式读取入口。 | ACTIVE |
| RC-001 | 2026-09-11 | 项目从依赖 Chat handoff / 分散记录，切换为 `docs/project_control/` 作为正式事实源。 | ACTIVE |
| RC-002 | 2026-09-11 | Dashboard 明确降级为 Project Control 的派生可视化，不再承担项目状态源职责。 | ACTIVE |
| RC-003 | 2026-09-11 | 新 Chat 的标准启动方式改为：先读取 Project Control，再继续项目。 | ACTIVE |
| RC-004 | 2026-09-11 | 重启阶段先完成 P0.1 / P0.2 / P0.3 三项基础专项，再根据验证结果设计正式生产 Roadmap。 | ACTIVE |

后续若规则被替代，不删除历史；新增记录并标记旧规则 `SUPERSEDED`。
