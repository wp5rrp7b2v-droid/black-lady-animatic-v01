# P0.2｜人物锚定与 Scene Master 资产治理

Status: `ACTIVE / ASSET SYSTEM DESIGN + AUTHORITY AUDIT`

## 当前目标

P0.2 不再只做“图库整理”，而是建立可规模化的 **Visual Asset Management System V1**，并把现有《黑衣夫人》视觉资产迁移到统一治理模型中。

当前锁定的系统方向：

`Entity → Atomic Master Assets → Derived Reference Sheet → Reference Resolver → Shot Reference Package → Generation → Product Owner Approval → Automatic Ingest → Asset Registry / Audit Trail`

目标是在正常生产中取消 Product Owner 的例行人工挑图、下载、命名、存储、登记与版本维护；Product Owner 只保留创意判断、异常处理与正式审批。

## 已锁定项目级规则

- 只有 Product Owner 明确批准的视觉结果才能进入正式 Asset Registry；
- 人物 / 场景 / 服装 / 道具统一采用 Entity → Asset 模型；
- Approval 与 Lifecycle 分离；正式生命周期为 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；
- Atomic Master 与 Derived Reference Sheet 分离；Derived Reference 必须可追踪其上游依赖；
- 正常生产目标为 `Shot / Task Spec → Reference Resolver → Reference Package`，不得依赖人工进入 Library 凭印象挑图；
- 正式资产的来源、审批、版本、替代、依赖与生产调用必须有 Audit Trail。

详细规则见：

`visual_asset_management_system_v1.md`

## 当前任务

### P0.2-01｜Visual Asset Authority Audit

继续核对既有 Character Master、Auxiliary Reference、Scene Master、A01–A07、A08 HOLD、SH 历史资产与一致性测试资产的权威关系。

当前已建立：

`asset_authority_audit.md`

### P0.2-02｜Visual Asset Management System V1 Design

在已锁定项目级规则上补齐：

- Entity / Asset Registry schema；
- 主要人物统一 Character Core Set；
- Scene / Costume / Prop / State / Variant 规范；
- Naming / Version / Authority rules；
- Storage strategy；
- Reference Sheet template；
- Reference Resolver；
- Automatic Ingest contract；
- Audit Trail schema；
- Production Readiness / Completeness 规则。

P0.2-01 与 P0.2-02 完成后，需要使用现有《黑衣夫人》资产做真实迁移与自动选图验证，不能只凭文档宣布体系可用。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。
