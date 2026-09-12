# Visual Asset Management System V1｜P0.2 Design Baseline

Status: `ACTIVE / RULE BASELINE LOCKED / DETAILED SCHEMA NEXT`

本文件记录《诡舍·黑衣夫人》P0.2 已由 Product Owner 确认的视觉资产管理方向。它不是 P0.2 Gate PASS，也不代表自动化已实现；P0.2 后续仍需完成 schema、标准视图、存储、Resolver、Audit Trail 和现有资产迁移验证，并最终提交 Product Owner 审批。

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

主要人物必须遵循统一的 Character Asset Specification，避免角色之间 Reference 角度、构图、比例和职责不一致。

已锁定原则：

- 所有主要人物必须使用同一套 Mandatory Core View 定义；
- `Front / 3/4 / Profile / Rear or Back / Full Body` 等角色视图的角度含义必须统一；
- 同类型 Reference 应尽可能统一背景、光线、摄影距离和人物比例；
- 额外表情、受伤、湿身、换装、特殊姿势等作为 Variant / Conditional Asset，不强制所有角色预制；
- Exact Core Set 的数量、左右侧要求、角度参数和画幅标准在 P0.2 下一步专项锁定。

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

## 6. Atomic Master 与 Reference Sheet

底层 Atomic Master 是权威输入；Reference Sheet 是生产便利层。

例如人物可由若干 Atomic Character References 生成一张或两张生产总图；日常生图优先使用 Reference Sheet，只有特殊视角或异常情况才额外调用 Atomic Reference。

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
2. 主要人物 Character Core Set 的精确定义；
3. Scene / Costume / Prop / State / Variant 规范；
4. Naming / Version / Authority rules；
5. Storage strategy；
6. Reference Sheet template；
7. Reference Resolver selection rules；
8. Automatic Ingest contract；
9. Audit Trail schema；
10. Production Readiness / Completeness 计算规则；
11. 使用现有《黑衣夫人》资产做一次真实迁移与自动选图验证。

完成上述工作后，P0.2 只能进入 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`；最终 PASS 仍由 Product Owner 审批。
