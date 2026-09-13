# P0.2｜人物锚定与 Scene Master 资产治理

Status: `ACTIVE / REGISTRY SCHEMA V0.3 LOCKED / TIER ASSIGNMENT NEXT`

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
- Entity-bound / Shot-bound filename 均包含 Role + Variant + State + Version，状态词不进入 filename。

详细规则见：

- `visual_asset_management_system_v1.md`
- `character_asset_rules_v1.md`
- `asset_naming_rules_v1.md`
- `asset_authority_audit.md`
- `entity_asset_registry_schema_v0_3.md`

## 当前任务

### P0.2-01｜Visual Asset Authority Audit

Authority Mini-Close 已锁定；仍需在 P0.2 Gate Review 前完成：

1. 旧 4 份 canonical register 与实际图库实体工程对账；
2. 12 张 Auxiliary 在新 Role / Variant / State / Lifecycle 下的唯一映射验证；
3. 两张 Scene Master 的事实字段结构化。

这些核对不再阻塞 Schema 设计，但必须在真实迁移与 Gate Review 前完成。

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

## 下一步

进入：

`9 Character Tier Assignment → Gap Analysis`

原则：

- 先判 Tier，再判断缺口；
- 不为了形式完整提前补图；
- Tier / Gap 只基于真实生产需求与当前 approved/current 资产；
- 宁秋水 Walkthrough 仅证明：如果最终定为 Tier A，当前标准 Coverage 为 6/9，不等于已正式指定 Tier A。

完成 Tier Assignment 后，再推进 Scene / Costume / Prop / State / Variant 规范、Storage、Reference Sheet、Resolver、Automatic Ingest 与真实迁移验证。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。
