# Visual Asset Management System V1｜P0.2 Design Baseline

Status: `ACTIVE / CHARACTER RULE + ASSET NAMING LOCKED / REGISTRY SCHEMA NEXT`

本文件记录《诡舍·黑衣夫人》P0.2 已由 Product Owner 确认的视觉资产管理方向。它不是 P0.2 Gate PASS，也不代表自动化已实现；P0.2 后续仍需完成 schema、场景/服装/道具规范、存储、Resolver、Audit Trail 和现有资产迁移验证，并最终提交 Product Owner 审批。

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

## 3. 人物资产标准化要求

P0.2-02 已正式锁定 Tier-based Character Asset 规则，详见：

`docs/project_control/gates/P0_2_visual_assets/character_asset_rules_v1.md`

正式原则：

- 人物资产不采用所有角色一刀切的固定数量，而采用 `Tier A / B / C / D` 分级；
- Tier A 核心角色采用 9-view canonical turnaround；
- Tier B 重要配角采用 6-view Core Set，并固定 primary side；
- Tier C 普通角色采用 3-view Minimum Set；
- Tier D 群演 / 一次性角色不建立完整 Character Core Set；
- Tier 由叙事重要性、出场频率、视角复杂度、连续性敏感度和动画需求共同决定；
- Production Need 可以触发 Tier 升级；不为了形式完整制造无实际用途资产；
- Character Core Set 的 Atomic Masters 与 Derived Character Reference Sheet 分离；
- 正常生产由 Resolver 自动使用 Character Reference Sheet，并按镜头需要追加对应 Atomic View；
- 所需视角不存在且不能安全覆盖时应返回 `REFERENCE_GAP`，不得静默使用废弃资产或把镜像推断当作新的权威事实。

同类型 Character Reference 必须尽可能统一背景、光线、摄影距离、人物比例、机位和角度定义，避免角色之间的 Reference 标准不一致。

## 4. 场景、服装、道具资产完整性

正式生产不能只依赖人物 Face / Body Reference。

P0.2 必须建立：

- Scene Master / Spatial Layout / Key Object / Material / Lighting State 的场景资产规则；
- Costume Master / Costume Detail / Placement 的服装资产规则；
- Prop Master / Scale / Placement / Detail 的关键道具资产规则；
- State / Variant 机制，例如 DAY / NIGHT / RAIN、NORMAL / WET / INJURED 等。

原则上只提前建立对生产控制有明确价值的核心资产；特殊资产可按 Shot 需求生成，避免为了“齐全”而制造大量无实际用途的图片。

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

### 5.3 Asset ID / Naming Standard

P0.2-02 已锁定资产 ID 与文件命名规则，详见：

`docs/project_control/gates/P0_2_visual_assets/asset_naming_rules_v1.md`

正式原则：

- Asset ID 使用 `AST_<MEDIA_CODE>_<6-digit sequence>`，例如 `AST_IMG_000128`、`AST_VID_000037`、`AST_AUD_000012`；
- `asset_id` 只负责永久唯一识别，不把人物、角度、版本、审批或生命周期语义塞入 ID；
- Entity ID 使用稳定业务前缀，例如 `CHAR_* / SCENE_* / PROP_* / COSTUME_*`；
- 人类可读文件名默认使用 `<ENTITY_ID>_<ROLE>_<VARIANT>_V###.<ext>`；
- Reference Sheet 若文件实体为图片，仍使用 `AST_IMG_*`，其职责由 Registry 的 `asset_class` 表达；
- 文件改名、移动目录或切换 Storage 不得改变 Asset ID；
- Asset ID、正式文件名、hash 与 Registry 写入由 Automatic Ingest 自动完成，Product Owner 不手工编号、命名或登记。

## 6. Atomic Master 与 Reference Sheet

底层 Atomic Master 是权威输入；Reference Sheet 是生产便利层。

例如人物可由若干 Atomic Character References 生成一张或少量生产总图；日常生图优先使用 Reference Sheet，只有特殊视角或异常情况才额外调用 Atomic Reference。

Reference Sheet 必须保存依赖关系，例如：

`CHAR_NQ_REFERENCE_SHEET_V002 → FACE_MASTER_V003 + PROFILE_V002 + REAR3Q_V002 + FULL_BODY_V001`

当上游 Master 更新时，系统必须能够识别哪些 Sheet 已受影响。

## 7. Reference Resolver

目标不是“把所有图片传到 GitHub 后人工更容易找”，而是取消正常路径中的人工挑图。

Shot / Task Spec 至少应能描述：

- character / entity；
- view / pose；
- scene；
- costume；
- prop；
- state / variant；
- continuity requirement。

Resolver 根据这些字段以及 Asset Registry 中的：

`entity_id + role + authority + lifecycle + version + variant`

自动返回当前有效资产，并生成唯一 `reference_package_id`。

Reference Package 必须记录当次真实使用的 Asset IDs 和版本，供后续复现与问题追踪。

## 8. Automatic Ingest

Product Owner 批准后，正常流程目标是自动完成：

1. Asset ID；
2. 规范命名；
3. 文件存储位置；
4. hash / integrity metadata；
5. Entity / Role / Version metadata；
6. Registry 写入；
7. parent / derived_from / supersedes 等关系；
8. 缩略图或必要派生文件；
9. Audit Trail。

Product Owner 不承担例行下载、搬运、命名或登记。

## 9. Audit Trail

系统必须能够回答：

- 这张资产是谁 / 什么 Entity 的？
- 如何生成？用了哪个模型、Prompt/Instruction 和 Reference？
- 何时、由谁批准？
- 当前是否是 Current？如果不是，被谁替代或为什么废弃？
- 哪些 Reference Sheet 依赖它？
- 哪些 Shot / Reference Package 曾经调用它？
- 某个镜头生成时实际使用的是哪些版本？

Audit Trail 必须覆盖：source、identity/version、approval、lifecycle、dependency、production usage。

## 10. Storage Boundary

GitHub 作为 Project Control、Registry、规则、版本关系和 Audit Trail 的 canonical 管理入口；高容量图片、视频等二进制资产不应无规则堆入普通 Git。

P0.2 必须进一步决定实际存储方案，例如 Git LFS / 私有对象存储 / 其他可由自动化流程稳定读取的资产层，并验证 Reference Resolver 能够按 Registry 地址取得真实文件。

## 11. P0.2 后续必须补齐

在 Gate Review 前至少需要完成：

1. Entity / Asset Registry schema；
2. Character Core Set 精确定义：**COMPLETE / LOCKED，见 `character_asset_rules_v1.md`**；
3. Scene / Costume / Prop / State / Variant 规范；
4. Naming rules：**COMPLETE / LOCKED，见 `asset_naming_rules_v1.md`**；Version / Authority rules 仍待锁定；
5. Storage strategy；
6. Reference Sheet template；
7. Reference Resolver selection rules；
8. Automatic Ingest contract；
9. Audit Trail schema；
10. Production Readiness / Completeness 计算规则；
11. 使用现有《黑衣夫人》资产做一次真实迁移与自动选图验证。

完成上述工作后，P0.2 只能进入 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`；最终 PASS 仍由 Product Owner 审批。
