# P0.2｜人物锚定与 Scene Master 资产治理

Status: `ACTIVE / CHARACTER MIGRATION V1 PUBLISHED / P1 CHARACTER GAP PRODUCTION`

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
- Gap Priority Classification / P1 Execution V1 已落档；
- D-059 Character Asset Migration V1 已完成并远端验证：48 张 canonical PNG + CSV/JSON Migration Mapping Manifest 已发布到 GitHub；
- D-060 Reference Package Exporter V0.1 已由 Product Owner 批准测试：自动选图 + 本地 Reference Package 生成链路已验证成立。

详细规则与当前基线见：

- `visual_asset_management_system_v1.md`
- `character_asset_rules_v1.md`
- `character_tier_assignment_v1.md`
- `character_asset_gap_mapping_v1.md`
- `character_gap_priority_v1.md`
- `asset_naming_rules_v1.md`
- `asset_authority_audit.md`
- `entity_asset_registry_schema_v0_3.md`
- `d059_character_asset_migration_v1_completion.md`
- `d060_reference_package_exporter_v0_1_test.md`

## 当前任务

### P0.2-01｜Visual Asset Authority Audit

Authority Mini-Close 已锁定。D-059 已将 48 张 approved Character references 迁入 canonical GitHub storage，并发布 Migration Mapping Manifest。

P0.2 Gate Review 前仍需：

1. 旧 4 份 canonical register 与实际图库实体完成最终工程对账；
2. 将已发布 Migration Manifest 接入正式长期 Asset Registry / Audit Event 实现；
3. 两张 Scene Master 的事实字段结构化；
4. 用已发布 Character assets 验证 Reference Resolver 的自动选图行为与制图交付链路。

这些核对不阻塞当前 P1 Character Gap Production。

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

### P0.2-03｜Character Tier Assignment + Gap Analysis + P1 Production

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

黑衣夫人旧 `three_quarter_half_body_angle_reference_v001` 因人物 likeness 不足，迁移目标为：`DEPRECATED / resolver NEVER`；历史 approval 事实保留，未作为 Current canonical Character asset 发布。

Gap Priority Classification V1：

- P1 = 10
- P2 = 7
- P3 = 6

P1/P2/P3 仅表示 Character Gap Production Priority，不是项目 Gate / Phase 编号。

## D-059｜Character Asset Migration V1

Status: `COMPLETE / REMOTE VERIFIED`

- Remote commit: `d9fb763fb63e57023aa2cf11119c9be1bef037d6`
- Canonical PNG: `48`
- Migration Manifest: `CSV + JSON`
- Character storage root: `production/image_library/character_references/`
- Migration evidence root: `docs/project_control/gates/P0_2_visual_assets/migration_evidence/`
- Neil `CHAR_neil_rear_turn_45_full_body_aux_reference_v001.png`: `MAPPING_REQUIRED / NOT MIGRATED`

注意：D-059 完成的是 canonical file storage + Migration Mapping Manifest publication；长期 Asset Registry / Audit Event 数据层与 Automatic Ingest 仍需后续实现和验证。

## D-060｜Reference Package Exporter V0.1

Status: `TEST APPROVED / PRODUCT OWNER APPROVED`

测试对象：`CHAR_NING_QIUSHUI → PROFILE_LEFT`

验证结果：

- 自动从正式 Character assets 选出 4 张参考图；
- 选择为 `FACE_FRONT / PROFILE_RIGHT / FACE_3Q_RIGHT / BODY_FRONT`；
- canonical source / APPROVED / CONFIRMED / CURRENT 条件全部满足；
- SHA source / copy / manifest = `4/4 PASS`；
- 正确识别目标 `PROFILE_LEFT = REFERENCE_GAP`；
- 无 Duplicate CURRENT 冲突；
- 未修改任何正式源图。

正式结论：

`Canonical Character Assets → automatic selection → local Reference Package`

已经通过真实测试验证。

当前尚未验证：

`Reference Package → image-production Chat / image-generation environment`

因此后续若继续工程验证，应优先做 Delivery Bridge，而不是扩大 V0.1 的选图复杂度。

## 当前执行基线

P1 按人物整组推进：

1. 宁秋水：`PROFILE_LEFT + REAR_3Q_LEFT`
2. 君鹭远：`PROFILE_LEFT + REAR_3Q_LEFT`
3. 尼尔：`PROFILE_RIGHT + REAR_3Q_RIGHT`
4. 苏小小：`PROFILE_LEFT + REAR_3Q_LEFT`
5. 廖健：`PROFILE_LEFT + REAR_3Q_LEFT`

制图与主流程分离：图片制作对话框负责生成 + 内部审核 + 迭代收敛；只有内部审核通过的最终候选返回主流程，由主流程执行 canonical registration / GitHub publication / Project Control 更新。

## 下一步

P1 生产目标仍为：

`P0.2-03｜P1 Wave 1｜宁秋水 PROFILE_LEFT + REAR_3Q_LEFT`

在正式依赖自动 Reference Package 工作流前，建议先验证 Delivery Bridge：如何将 V0.1 自动生成的 Reference Package 稳定送入制图环境，减少 Product Owner 手工上传和搬运。

原则：

- 新图属于 production auxiliary reference，不是剧情 Shot；
- LEFT / RIGHT 按 screen-facing convention；
- 制图对话框内部完成审图与返修；
- 只有内部审核通过的最终候选返回主流程；
- 只有 Product Owner 明确批准的结果才能进入正式 canonical storage / Registry；
- 不因 P1 制图跳过旧 Register 对账、Reference Sheet / Resolver / Automatic Ingest 后续验证。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。
