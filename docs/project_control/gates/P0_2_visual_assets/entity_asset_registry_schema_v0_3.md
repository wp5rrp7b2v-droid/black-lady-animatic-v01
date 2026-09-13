# P0.2-02｜Entity / Asset Registry Schema V0.3

Status: `LOCKED / PRODUCT OWNER APPROVED 2026-09-13`

本文件定义《诡舍·黑衣夫人》Visual Asset Management System V1 的 Entity / Asset Registry 正式数据模型。Schema V0.3 已通过宁秋水真实 Character 资产、A04 Shot Asset 与 Derived Character Reference Sheet 逻辑 Walkthrough，并由 Product Owner 于 2026-09-13 明确批准。

本文件锁定 Schema，不代表 P0.2 Gate 已 PASS。P0.2 仍需完成角色 Tier Assignment、Gap Analysis、Scene / Costume / Prop / State / Variant 规范、Storage、Resolver、Automatic Ingest、真实迁移与工程核对，并最终提交 Product Owner Gate 审批。

## 1. 长期数据模型

正式系统保持四个长期数据层：

`Entity Registry → Asset Registry ↔ Asset Relations → Append-only Audit Event Log`

另设：

`Migration Mapping Manifest`

Migration Mapping Manifest 仅用于旧资产迁移，不是第五个长期 Registry，也不参与正常 Resolver 查询。

正式生产链：

`Entity / Shot Spec → Reference Resolver → Reference Package → Generation → Product Owner Approval → Automatic Ingest → Asset Registry + Relations + Audit Trail`

## 2. Entity Registry

Entity 表示稳定叙事对象，不表示文件。

最小字段：

- `entity_id`：PK / unique；格式 `^(CHAR|SCENE|PROP|COSTUME)_[A-Z0-9_]+$`
- `entity_type`：`CHARACTER / SCENE / PROP / COSTUME`
- `display_name`：required
- `entity_status`：`ACTIVE / RETIRED`
- `character_tier`：Character 专用，`A / B / C / D / null`
- `primary_side`：Tier B Character 专用，`LEFT / RIGHT / null`
- `created_at`：UTC / immutable
- `updated_at`：UTC

前缀必须与 `entity_type` 一致。

角色尚未完成 Tier Assignment 时允许 `character_tier = null`；此时 `PRODUCTION_READY = FALSE`。

## 3. Asset Registry

Asset 表示一个具体、可验证的正式文件版本。

最小字段：

- `asset_id`：immutable PK，格式 `AST_<MEDIA_CODE>_<6-digit sequence>`
- `entity_id`：Entity-bound Asset 使用
- `shot_id`：Shot-bound Asset 使用，必须引用 canonical Shot ID
- `media_code`：`IMG / VID / AUD / MDL / TEX`
- `asset_class`：`ATOMIC / DERIVED_REFERENCE / SHOT`
- `role`：按 `asset_class` 使用受控 vocabulary
- `variant`：required，默认 `DEFAULT`
- `state`：required，默认 `DEFAULT`
- `version_no`：integer >= 1
- `approval_status`：Formal Registry 仅允许 `APPROVED`
- `lifecycle`：`CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`
- `authority_class`：见第 8 节
- `resolver_usage`：`DEFAULT / CONDITIONAL / NEVER`
- `provenance_status`：`COMPLETE / PARTIAL / UNKNOWN`
- `filename`：Automatic Ingest 自动生成
- `storage_uri`：required / unique / resolvable
- `sha256`：lowercase hex 64
- `mime_type`：与 media code 一致
- `byte_size`：> 0
- `approved_at`：UTC
- `ingested_at`：UTC，且 >= approved_at

Generated / Candidate / ChatGPT Reviewed / Rejected / Not Adopted / Invalid Test 等不进入 Formal Asset Registry，保留在 Generation / Review / Evidence 层。

## 4. Asset Class 与归属

### 4.1 ATOMIC

人物、场景、服装、道具的单项正式资产：

- `entity_id = REQUIRED`
- `shot_id = null`

### 4.2 DERIVED_REFERENCE

由多个 Atomic Asset 派生的 Character / Scene / Costume / Prop Reference Sheet：

- `entity_id = REQUIRED`
- `shot_id = null`

### 4.3 SHOT

正式剧情镜头资产：

- `entity_id = null`
- `shot_id = REQUIRED`

Shot 中出现一个或多个 Character 都不改变该规则。人物、场景、道具组成关系由 Shot Register / Shot Spec 表达，不写入 Shot 文件名，也不把 Shot 强行挂在任一 Character Entity 下。

## 5. Role Vocabulary

Role 必须按 `asset_class` 分组校验。

### Character Core Roles

- `FACE_FRONT`
- `FACE_3Q_LEFT`
- `FACE_3Q_RIGHT`
- `PROFILE_LEFT`
- `PROFILE_RIGHT`
- `REAR_3Q_LEFT`
- `REAR_3Q_RIGHT`
- `BODY_FRONT`
- `BODY_BACK`
- `CHARACTER_REFERENCE_SHEET`

可按真实生产需要增加 supplementary roles，例如：

- `UPPER_BODY_3Q_RIGHT`
- `STRUCTURE_FRONT_3Q_BODY_RIGHT`

Supplementary role 不自动计入 Character Tier Core Set。

### Shot Role

V0.3 当前锁定：

- `SHOT_MASTER`

未来仅在出现真实生产需求时扩展，不预建大量无用途 Role。

## 6. LEFT / RIGHT 定义

正式采用 screen-facing convention：

- 面部 / 鼻尖朝画面右侧 = `RIGHT`
- 面部 / 鼻尖朝画面左侧 = `LEFT`

不得与人物自身解剖学左右混用。

## 7. Variant 与 State

`variant` 与 `state` 必须分离。

Variant 表示相对稳定的设计差异，例如：

- `DEFAULT`
- `PROFILE_REVEAL`
- `FORMAL`
- `CASUAL`

State 表示生产中的临时或连续性状态，例如：

- `DEFAULT`
- `WET`
- `DIRTY`
- `INJURED`
- `BLOODSTAINED`
- `DAY`
- `NIGHT`
- `RAIN`

Scene Master 锁定场景事实。若 DAY/NIGHT、门开闭、壁炉熄灭/点燃等已锁定事实发生变化，必须建立受控 Variant / State，不得在 Shot 中静默改变。

## 8. Authority / Lifecycle / Resolver Usage

三者必须分离：

- Authority：资产能够证明什么
- Lifecycle：资产处于什么版本状态
- Resolver Usage：生产时是否以及在何种条件下允许调用

`authority_class`：

1. `MASTER`
2. `AUXILIARY`
3. `DERIVED`
4. `CONTINUITY`
5. `SUPPLEMENTARY`
6. `LEGACY_SUPPLEMENTARY`

`resolver_usage`：

- `DEFAULT`：正常生产自动选择
- `CONDITIONAL`：只有 Shot / Task Spec 明确满足条件时选择
- `NEVER`：正常生产禁止选择

A01–A07 等正式历史 Shot 可合法表现为：

`APPROVED / ARCHIVED / CONTINUITY / CONDITIONAL`

SH01–SH08 默认：

`LEGACY_SUPPLEMENTARY / NEVER`

其中 SH02 Neil 与 SH08 V2 Black Lady 为已锁定 `CONDITIONAL` 例外。

## 9. Single Current

不维护独立 `default=true / latest=true / current_master=true` 等重复事实层。

Entity-bound Asset：

`UNIQUE(entity_id, role, variant, state) WHERE lifecycle = CURRENT`

版本唯一性：

`UNIQUE(entity_id, role, variant, state, version_no)`

Shot-bound Asset：

`UNIQUE(shot_id, role, variant, state) WHERE lifecycle = CURRENT`

Resolver 的默认选择由 CURRENT + Rule Match 动态推导。

## 10. Provenance Status

`provenance_status`：

- `COMPLETE`
- `PARTIAL`
- `UNKNOWN`

未来新生产的正式资产正常应达到 `COMPLETE`，即能够追踪 Reference、生成任务、批准、版本、文件、hash 与关系。

Legacy Migration 允许 `PARTIAL / UNKNOWN`。不得为了填满字段而事后编造历史 `USES_REFERENCE` 关系。

## 11. Asset Relations

最小字段：

- `source_asset_id`
- `relation_type`
- `target_asset_id`
- `created_at`
- `created_by_event_id`

唯一约束：

`UNIQUE(source_asset_id, relation_type, target_asset_id)`

且 source != target。

V0.3 关系类型：

### `DERIVED_FROM`

Derived Reference → Atomic Asset。禁止 dependency cycle。

### `SUPERSEDES`

方向固定：

`NEW_ASSET SUPERSEDES OLD_ASSET`

必须匹配同一 entity/shot + role + variant + state，且 new.version_no > old.version_no。

新旧生命周期更新应原子执行：

- new = `CURRENT`
- old = `SUPERSEDED`

### `USES_REFERENCE`

记录正式生成结果实际使用的具体 Asset IDs / versions。只记录能够证明的关系。

## 12. Derived Reference Sheet 与 Dependency Stale

Reference Sheet 通过多条 `DERIVED_FROM` 指向具体 Atomic Assets。

若任一上游依赖被 SUPERSEDED / DEPRECATED / invalidated，Reference Sheet 计算状态变为：

`DEPENDENCY_STALE`

`DEPENDENCY_STALE` 不是 Lifecycle 值。Sheet 可以仍为 `CURRENT`，但不得继续作为 Resolver `DEFAULT` 输入，直到重新生成并由 Product Owner 批准新版本。

## 13. Resolver Eligibility

不存储独立手工 `resolver_eligible` 布尔值。

Resolver Eligibility 动态计算，至少考虑：

- approval_status
- resolver_usage
- lifecycle
- storage / hash integrity
- entity / shot / task match
- role / variant / state match
- Single Current
- dependency validity

返回：

- `ELIGIBLE`
- `NOT_ELIGIBLE`
- `REFERENCE_GAP`

需要的关键参考不存在且不能安全覆盖时必须返回 `REFERENCE_GAP`；不得静默调用 obsolete asset 或用镜像推断代替权威事实。

## 14. Append-only Audit Event Log

最小字段：

- `event_id`
- `event_time`
- `event_type`
- `entity_id`
- `asset_id`
- `actor_type`
- `actor_id`
- `previous_value`
- `new_value`
- `reason`
- `task_id`
- `source_reference`

`actor_type`：

- `PRODUCT_OWNER`
- `CHATGPT`
- `CODEX`
- `SYSTEM`

初始 `event_type`：

- `ENTITY_CREATED`
- `ENTITY_UPDATED`
- `TIER_CHANGED`
- `ASSET_APPROVED`
- `ASSET_INGESTED`
- `ASSET_MIGRATED`
- `LIFECYCLE_CHANGED`
- `ASSET_SUPERSEDED`
- `RELATION_CREATED`
- `RESOLVER_USAGE_CHANGED`

Audit Event Log 为 INSERT ONLY；不得 UPDATE / DELETE 历史事件。

Tier / Lifecycle / Resolver Usage / Supersession / Relation 等业务表变化必须与 Audit Event 同一事务写入，否则整个操作失败。

## 15. Migration Mapping Manifest

Manifest 仅用于将旧体系映射到 Schema V0.3。

最小字段：

- `legacy_asset_id`
- `legacy_filename`
- `legacy_path`
- `legacy_role`
- `legacy_status`
- `canonical_entity_id`
- `canonical_shot_id`
- `new_role`
- `variant`
- `state`
- `authority_class`
- `lifecycle`
- `resolver_usage`
- `mapping_status`
- `evidence`

`mapping_status`：

- `CONFIRMED`
- `MAPPING_REQUIRED`
- `NOT_MIGRATED`

Manifest 保留为迁移证据，但不参与正常 Resolver 查询。

## 16. Canonical Naming

### Entity-bound Asset

`<ENTITY_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`

示例：

`CHAR_NING_QIUSHUI_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`

### Shot-bound Asset

`<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`

示例：

`A04_SHOT_MASTER_DEFAULT_DEFAULT_V001.png`

文件名不得包含 `approved / final / current / lock / reboot / latest / good` 等状态词。Approval、Lifecycle、Authority 与 Resolver Usage 均由 Registry metadata 表达。

## 17. Legacy REBOOT Shot ID 迁移

项目重新梳理后，`REBOOT` 仅保留为历史 identifier，不进入新的 canonical Shot ID：

- `A01_REBOOT → A01`
- `A02_REBOOT → A02`
- ...
- `A08_REBOOT → A08`

例如旧：

`A04_REBOOT_approved_v001.png`

迁移后 canonical：

`A04_SHOT_MASTER_DEFAULT_DEFAULT_V001.png`

Legacy identifier 与 legacy filename 保留在 Migration Mapping Manifest 中以便追溯。

## 18. 实际 Walkthrough 验证

### 宁秋水

现有 Approved 资产可以无冲突映射到 Role + Variant + Lifecycle + Resolver 模型。

若后续 Tier Assignment 将宁秋水定为 Tier A，当前可确认覆盖：

- FACE_FRONT
- FACE_3Q_RIGHT
- PROFILE_RIGHT
- REAR_3Q_RIGHT
- BODY_FRONT
- BODY_BACK

即 6/9；缺 FACE_3Q_LEFT / PROFILE_LEFT / REAR_3Q_LEFT。当前不提前补图。

Rear 3/4 示例：

- `REAR_3Q_RIGHT / DEFAULT / V001 → SUPERSEDED`
- `REAR_3Q_RIGHT / DEFAULT / V002 → CURRENT`
- `REAR_3Q_RIGHT / PROFILE_REVEAL / V001 → CURRENT + CONDITIONAL`

### A04

新体系 canonical Shot ID 为 `A04`，不保留 `REBOOT`。

正式迁移目标：

- `asset_class = SHOT`
- `role = SHOT_MASTER`
- `variant = DEFAULT`
- `state = DEFAULT`
- `approval_status = APPROVED`
- `lifecycle = ARCHIVED`
- `authority_class = CONTINUITY`
- `resolver_usage = CONDITIONAL`
- `provenance_status = PARTIAL`

A04 中出现多个 Character 不影响 Shot Asset 归属；人物/场景关系由 Shot Register / Shot Spec 表达。

## 19. Schema V0.3 相对 V0.2 的正式修订

1. 增加临时 `Migration Mapping Manifest`；
2. `role` 按 `asset_class` 分组，并新增 `SHOT_MASTER`；
3. Asset Registry 增加 `provenance_status = COMPLETE / PARTIAL / UNKNOWN`；
4. Naming 分为 Entity-bound / Shot-bound 两种模板；
5. Naming 正式纳入 `STATE`，避免不同 State 的同版本资产重名；
6. Canonical Shot ID 移除历史 `REBOOT` 标记；
7. 多人物 Shot 的人物组成由 Shot Register / Shot Spec 表达，不进入 Shot filename。

## 20. Gate Boundary

Schema V0.3 已 LOCK，但 P0.2 Gate 仍为 ACTIVE。

下一阶段：

`Schema V0.3 LOCK → 9 Character Tier Assignment → Gap Analysis → historical asset mapping / remaining engineering checks → downstream Resolver / Automatic Ingest validation`

P0.2 技术与治理条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

最终 `PASS` 必须由 Product Owner 明确审批。
