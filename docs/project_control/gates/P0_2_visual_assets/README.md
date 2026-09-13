# P0.2｜人物锚定与 Scene Master 资产治理

Status: `ACTIVE / GAP MAPPING V1 LOCKED / P1 CHARACTER GAP PRODUCTION BASELINE`

## 当前目标

P0.2 不再只做“图库整理”，而是建立可规模化的 **Visual Asset Management System V1**，并把现有《黑衣夫人》视觉资产迁移到统一治理模型中。

当前锁定的系统方向：

`Entity → Atomic Master Assets → Derived Reference Sheet → Reference Resolver → Shot Reference Package → Generation → Product Owner Approval → Automatic Ingest → Asset Registry / Audit Trail`

目标是在正常生产中取消 Product Owner 的例行人工挑图、下载、命名、存储、登记与版本维护；Product Owner 只保留创意判断、异常处理与正式审批。

## 已锁定项目级规则

- 只有 Product Owner 明确批准的视觉结果才能进入正式 Asset Registry；
- 人物 / 场景 / 服装 / 道具统一采用 Entity → Asset 模型；
- Approval 与 Lifecycle 分离；正式生命周期为 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；
- Authority / Lifecycle / Resolver Usage 分离；
- Atomic Asset 与 Derived Reference Sheet 分离；Derived Reference 必须可追踪上游依赖；
- 正常生产目标为 `Shot / Task Spec → Reference Resolver → Reference Package`；
- 正式资产的来源、审批、版本、替代、依赖与生产调用必须有 Audit Trail；
- Entity / Asset Registry Schema V0.3 已由 Product Owner 于 2026-09-13 批准锁定；
- canonical Shot ID 不继承历史 `REBOOT` 标签；多人物 Shot 仍为 Shot-bound Asset，人物组成由 Shot Register / Shot Spec 表达；
- Entity-bound / Shot-bound filename 均包含 Role + Variant + State + Version，状态词不进入 filename；
- 9 名正式角色 Tier Assignment V1 已由 Product Owner 于 2026-09-13 批准锁定；
- Character Asset Gap Mapping V1 已完成实图核对并落档；
- Gap Priority Classification / P1 Execution V1 已落档。

详细规则与当前基线见：

- `visual_asset_management_system_v1.md`
- `character_asset_rules_v1.md`
- `character_tier_assignment_v1.md`
- `character_asset_gap_mapping_v1.md`
- `character_gap_priority_v1.md`
- `asset_naming_rules_v1.md`
- `asset_authority_audit.md`
- `entity_asset_registry_schema_v0_3.md`

## 当前任务

### P0.2-01｜Visual Asset Authority Audit

Authority Mini-Close 已锁定；仍需在 P0.2 Gate Review 前完成：

1. 旧 4 份 canonical register 与实际图库实体工程对账；
2. 12 张 Auxiliary 在新 Role / Variant / State / Lifecycle 下的唯一映射验证；
3. 两张 Scene Master 的事实字段结构化。

这些核对不阻塞当前 P1 Character Gap Production，但必须在正式迁移与 Gate Review 前完成。

### P0.2-02｜Visual Asset Management System V1 Design

已完成并锁定：

- Character Tier A/B/C/D 规则；
- Asset ID / Naming 基线；
- Authority Mini-Close；
- Entity / Asset Registry Schema V0.3；
- Single Current；
- Asset Relations；
- Provenance Status；
- Resolver Eligibility 计算原则；
- Append-only Audit Event Log 结构；
- Legacy Migration Mapping Manifest；
- Shot-bound / Entity-bound 归属与命名边界。

### P0.2-03｜Character Tier Assignment + Gap Analysis

Tier Assignment 已锁定：

- Tier A：宁秋水 / 君鹭远 / 尼尔 / 黑衣夫人；
- Tier B：温倾雅 / 苏小小 / 廖健 / 古堡小主人；
- Tier C：光勇；
- Tier D：当前 9 名正式角色中无。

Character Asset Gap Mapping V1 实图核对后的正式基线：

- Mandatory Core Slots = `63`
- Confirmed Coverage = `40`
- Core View Gap = `23`
- Core Coverage = `63.5%`
- Reference Sheet Gap = `9`（Derived Asset Gap，单独统计）

Tier B 四人均锁定 `primary_side = LEFT`。

黑衣夫人旧 `three_quarter_half_body_angle_reference_v001` 因人物 likeness 不足，迁移目标为：`DEPRECATED / resolver NEVER`；历史 approval 事实保留。

Gap Priority Classification V1：

- P1 = 10
- P2 = 7
- P3 = 6

P1/P2/P3 仅表示 Character Gap Production Priority，不是项目 Gate / Phase 编号。

## 当前执行基线

P1 按人物整组推进：

1. 宁秋水：`PROFILE_LEFT + REAR_3Q_LEFT`
2. 君鹭远：`PROFILE_LEFT + REAR_3Q_LEFT`
3. 尼尔：`PROFILE_RIGHT + REAR_3Q_RIGHT`
4. 苏小小：`PROFILE_LEFT + REAR_3Q_LEFT`
5. 廖健：`PROFILE_LEFT + REAR_3Q_LEFT`

不跨角色无差别批量补图；一人完成并通过 Product Owner 审批后再推进下一 Wave。

## 下一步

进入：

`P0.2-03｜P1 Wave 1｜宁秋水 PROFILE_LEFT + REAR_3Q_LEFT`

原则：

- 新图属于 production auxiliary reference，不是剧情 Shot；
- LEFT / RIGHT 按 screen-facing convention；
- 先检查人物身份和角度，再判断是否批准；
- 只有 Product Owner 明确批准的结果才能进入正式 Asset Registry / Automatic Ingest；
- 不因 P1 制图跳过旧 Register 对账、Migration Mapping、Reference Sheet / Resolver / Automatic Ingest 后续验证。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。
