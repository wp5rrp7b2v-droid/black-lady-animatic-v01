# Visual Asset Management System V1｜P0.2 Design Baseline

Status: `ACTIVE / CHARACTER RULE + NAMING + AUTHORITY + REGISTRY SCHEMA LOCKED`

本文件记录《诡舍·黑衣夫人》P0.2 已由 Product Owner 确认的视觉资产管理方向。它不是 P0.2 Gate PASS，也不代表自动化已实现；P0.2 后续仍需完成角色 Tier Assignment、Gap Analysis、场景/服装/道具规范、存储、Resolver、Automatic Ingest、真实迁移与工程核对，并最终提交 Product Owner 审批。

## 1. 目标

把当前依赖人工找图、挑图、下载、命名、登记的方式升级为可规模化的 Production Asset System。

目标生产链：

`Entity → Atomic Master Assets → Derived Reference Sheet → Reference Resolver → Shot Reference Package → Generation → Product Owner Approval → Automatic Ingest → Asset Registry / Audit Trail`

正常生产中，Product Owner 负责创意判断与正式审批；系统负责机械性的资产选择、命名、存储、登记、版本与追踪。

## 2. 统一资产对象模型

人物、场景、服装、道具统一采用同一底层模型：

- `Entity`：稳定叙事对象，如宁秋水、第一大厅、尼尔十字架、尼尔默认管家服；
- `Atomic Asset`：具体权威图像，如 Face Master、Profile、Scene Master、Prop Master；
- `Derived Reference`：由多个 Atomic Assets 派生的 Character / Scene / Costume / Prop Reference Sheet；
- `Reference Package`：针对某个 Shot / Generation Task 自动解析出的实际参考资产集合；
- `Generated Shot / Asset`：模型生成结果，经 Product Owner 批准后才可进入正式资产库。

Schema V0.3 已正式锁定，详见：

`docs/project_control/gates/P0_2_visual_assets/entity_asset_registry_schema_v0_3.md`

长期数据层保持：

`Entity Registry → Asset Registry ↔ Asset Relations → Append-only Audit Event Log`

另设只服务于旧资产迁移的 `Migration Mapping Manifest`，不参与正常 Resolver 查询。

## 3. 人物资产标准化要求

P0.2-02 已正式锁定 Tier-based Character Asset 规则，详见：

`docs/project_control/gates/P0_2_visual_assets/character_asset_rules_v1.md`

正式原则：

- 人物资产采用 `Tier A / B / C / D` 分级；
- Tier A 核心角色采用 9-view canonical turnaround；
- Tier B 重要配角采用 6-view Core Set，并固定 primary side；
- Tier C 普通角色采用 3-view Minimum Set；
- Tier D 群演 / 一次性角色不建立完整 Character Core Set；
- Tier 由叙事重要性、出场频率、视角复杂度、连续性敏感度和动画需求共同决定；
- Production Need 可以触发 Tier 升级；不为了形式完整制造无实际用途资产；
- Character Core Set 的 Atomic Assets 与 Derived Character Reference Sheet 分离；
- 正常生产由 Resolver 自动使用 Character Reference Sheet，并按镜头需要追加对应 Atomic View；
- 所需视角不存在且不能安全覆盖时返回 `REFERENCE_GAP`，不得静默使用废弃资产或把镜像推断当成新的权威事实。

同类型 Character Reference 必须尽可能统一背景、光线、摄影距离、人物比例、机位和角度定义。

LEFT / RIGHT 采用 screen-facing convention：人物面部/鼻尖朝画面右侧 = RIGHT，朝画面左侧 = LEFT。

## 4. 场景、服装、道具资产完整性

正式生产不能只依赖人物 Face / Body Reference。

P0.2 必须建立：

- Scene Master / Spatial Layout / Key Object / Material / Lighting State 的场景资产规则；
- Costume Master / Costume Detail / Placement 的服装资产规则；
- Prop Master / Scale / Placement / Detail 的关键道具资产规则；
- State / Variant 机制，例如 DAY / NIGHT / RAIN、NORMAL / WET / INJURED 等。

Scene Master 锁定的是场景事实，不锁死 Shot 摄影表现。已锁定场景事实如 DAY/NIGHT、门开闭、壁炉熄灭/点燃发生变化时，必须建立受控 Variant / State，不得在 Shot 中静默改变。

## 5. 正式资产准入与生命周期

### 5.1 Generation Workflow

生成过程可以出现：

`GENERATED → CHATGPT REVIEW → PRODUCT OWNER APPROVE / REJECT`

这些状态属于 Generation / Review Log，不进入正式 Asset Registry。

### 5.2 Formal Asset Registry

只有 Product Owner 明确批准的资产进入正式 Asset Registry。

正式资产：

`approval_status = APPROVED`

生命周期独立记录：

- `CURRENT`
- `SUPERSEDED`
- `DEPRECATED`
- `ARCHIVED`

历史 Approval 不因后续 Supersede / Deprecate / Archive 被删除。

Authority、Lifecycle、Resolver Usage 三者分离管理。

### 5.3 Asset ID / Naming Standard

P0.2-02 已锁定资产 ID 与文件命名规则，详见：

`docs/project_control/gates/P0_2_visual_assets/asset_naming_rules_v1.md`

正式原则：

- Asset ID 使用 `AST_<MEDIA_CODE>_<6-digit sequence>`；
- `asset_id` 只负责永久唯一识别；
- Entity ID 使用 `CHAR_* / SCENE_* / PROP_* / COSTUME_*`；
- Entity-bound filename：`<ENTITY_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`；
- Shot-bound filename：`<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`；
- canonical Shot ID 不继承旧 `REBOOT` 标签，例如 `A04_REBOOT → A04`；
- 多人物 Shot 不把人物名单写入 filename；组成关系由 Shot Register / Shot Spec 表达；
- 文件改名、移动目录或切换 Storage 不得改变 Asset ID；
- Asset ID、正式文件名、hash 与 Registry 写入由 Automatic Ingest 自动完成。

## 6. Registry Schema V0.3

正式 asset class：

- `ATOMIC`
- `DERIVED_REFERENCE`
- `SHOT`

Entity-bound Asset 使用 `entity_id`；Shot-bound Asset 使用 canonical `shot_id`。

正式 Single Current 规则：

- Entity-bound：同一 `entity_id + role + variant + state` 最多一个 `CURRENT`；
- Shot-bound：同一 `shot_id + role + variant + state` 最多一个 `CURRENT`。

不再维护独立 `default=true / latest=true / current_master=true` 作为平行事实源。

正式 provenance：

- `COMPLETE`
- `PARTIAL`
- `UNKNOWN`

新生产资产应正常达到 COMPLETE；Legacy Migration 可为 PARTIAL / UNKNOWN，且不得事后编造历史 `USES_REFERENCE`。

## 7. Atomic Asset 与 Reference Sheet

底层 Atomic Asset 是权威输入；Reference Sheet 是生产便利层。

Reference Sheet 必须通过 `DERIVED_FROM` 保存对具体 Atomic Asset IDs / versions 的依赖。

当任一上游依赖被替代或失效时，Sheet 计算为：

`DEPENDENCY_STALE`

该状态不属于 Lifecycle。即使 Sheet 仍是 CURRENT，也不得继续作为 Resolver DEFAULT 输入，直到重新生成并经 Product Owner 批准。

## 8. Reference Resolver

目标不是“把所有图片传到 GitHub 后人工更容易找”，而是取消正常路径中的人工挑图。

Shot / Task Spec 至少应能描述：

- character / entity；
- view / pose；
- scene；
- costume；
- prop；
- state / variant；
- continuity requirement。

Resolver 根据 Registry 的 Entity / Shot、Role、Authority、Lifecycle、Resolver Usage、Variant、State、Single Current、dependency 和 integrity 自动生成 Reference Package。

Resolver Eligibility 不保存为人工布尔值；动态返回：

- `ELIGIBLE`
- `NOT_ELIGIBLE`
- `REFERENCE_GAP`

Reference Package 必须记录当次真实使用的 Asset IDs 和版本。

## 9. Asset Relations

V0.3 正式关系：

- `DERIVED_FROM`
- `SUPERSEDES`
- `USES_REFERENCE`

`SUPERSEDES` 方向固定为 NEW → OLD，且新旧必须属于同一 entity/shot + role + variant + state；新 CURRENT 与旧 SUPERSEDED 应原子更新。

`USES_REFERENCE` 只记录能够证明的实际引用关系。

## 10. Automatic Ingest

Product Owner 批准后，正常流程目标是自动完成：

1. Asset ID；
2. 规范命名；
3. 文件存储位置；
4. hash / integrity metadata；
5. Entity / Shot / Role / Variant / State / Version metadata；
6. Registry 写入；
7. Relations；
8. 缩略图或必要派生文件；
9. Audit Trail。

Product Owner 不承担例行下载、搬运、命名或登记。

## 11. Audit Trail

系统必须能够回答：

- 这张资产属于谁 / 什么 Entity 或 Shot？
- 如何生成？用了哪些可证明的 Reference？
- 何时、由谁批准？
- 当前 Lifecycle 是什么？如果不是 Current，被谁替代或为什么废弃？
- 哪些 Reference Sheet 依赖它？
- 哪些 Shot / Reference Package 曾调用它？
- 某个镜头生成时实际使用的是哪些版本？

Audit Event Log 为 append-only。Tier / Lifecycle / Resolver Usage / Supersession / Relation 等业务变化必须与 Audit Event 同一事务写入。

## 12. Legacy Migration

旧资产通过 Migration Mapping Manifest 映射到新体系。

Manifest 至少保留 legacy asset id / filename / path / role / status，以及 canonical entity/shot、new role、variant、state、authority、lifecycle、resolver usage、mapping status 与 evidence。

历史 `REBOOT / approved / final / current / lock` 等词不进入新 canonical filename。

宁秋水真实 Walkthrough 已验证 Role + Variant + Lifecycle + Resolver 可以表达旧 Master / Auxiliary / Supplementary / Superseded 关系；A04 已验证多人物 Shot 仍应使用 Shot-bound Asset，不挂在任一 Character Entity 下。

## 13. Storage Boundary

GitHub 作为 Project Control、Registry、规则、版本关系和 Audit Trail 的 canonical 管理入口；高容量图片、视频等二进制资产不应无规则堆入普通 Git。

P0.2 仍需决定实际 Storage strategy，并验证 Reference Resolver 能按 Registry 地址取得真实文件。

## 14. P0.2 后续必须补齐

在 Gate Review 前至少需要完成：

1. Entity / Asset Registry Schema：**COMPLETE / LOCKED，见 `entity_asset_registry_schema_v0_3.md`**；
2. Character Core Set 精确定义：**COMPLETE / LOCKED，见 `character_asset_rules_v1.md`**；
3. 9 Character Tier Assignment + Gap Analysis；
4. Scene / Costume / Prop / State / Variant 规范；
5. Naming / Version / Authority rules：**Naming + Authority baseline LOCKED；实现验证仍待完成**；
6. Storage strategy；
7. Reference Sheet template；
8. Reference Resolver selection rules / implementation contract；
9. Automatic Ingest contract；
10. Production Readiness / Completeness 计算规则；
11. 旧 Register / 实际图库实体工程核对与真实迁移；
12. 自动选图验证。

完成上述工作后，P0.2 只能进入 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`；最终 PASS 仍由 Product Owner 审批。
