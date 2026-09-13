# P0.2-02｜Character Asset Rules V1

Status: `LOCKED DESIGN RULE / PARTIALLY VALIDATED IN P1 PRODUCTION`

本文件定义《诡舍·黑衣夫人》Visual Asset Management System V1 的人物资产标准。该规则已由 Product Owner 在 2026-09-12 当前 Chat 明确确认，并于 2026-09-13 通过 P1 Character Gap Production 的真实生产进一步验证。

本规则不代表 P0.2 Gate 已通过。后续仍需继续完成 Scene / Costume / Prop / Variant 结构化、真实 Shot Spec Resolver 验证、完整 Audit reverse-trace 等 Gate evidence，并最终提交 Product Owner 审批。

## 1. 核心原则

人物资产采用 **Tier 分级管理**，而不是所有角色使用同一数量的锚定图。

Tier 决定该角色在正式生产中的 **Minimum Reference Coverage**；实际生产需求可以触发升级或按需补充 Conditional Reference。

目标：

- 核心角色获得长期稳定的多角度人物事实基线；
- 重要配角保持足够一致性而不过度建设；
- 普通角色与群演不因形式完整而制造大量低价值资产；
- 正常生产中由 Reference Resolver 自动选取资产，不由 Product Owner 手工挑图。

## 2. Character Tier

### Tier A｜Core Character

适用：高频出现、承担主要剧情、需要多机位连续镜头、转头/运动/动画连续性要求高的角色。

Mandatory Core Set = **9-view**：

1. `FACE_FRONT`｜正面，0°
2. `FACE_3Q_LEFT`｜左前 3/4，约 45°
3. `FACE_3Q_RIGHT`｜右前 3/4，约 45°
4. `PROFILE_LEFT`｜左侧标准侧脸，90°
5. `PROFILE_RIGHT`｜右侧标准侧脸，90°
6. `REAR_3Q_LEFT`｜左后 3/4，约 135°
7. `REAR_3Q_RIGHT`｜右后 3/4，约 135°
8. `BODY_FRONT`｜全身正面
9. `BODY_BACK`｜全身背面

Tier A 的目的不是让每次生图同时输入 9 张图片，而是建立完整 canonical turnaround coverage；日常生产优先使用 Derived Character Reference Sheet，特殊镜头再由 Resolver 自动追加对应 Atomic View。

### Tier B｜Important Supporting Character

适用：有明确身份、会重复出现，但镜头角度和动画复杂度明显低于 Tier A 的角色。

Mandatory Core Set = **6-view**：

1. `FACE_FRONT`
2. `FACE_3Q_PRIMARY`
3. `PROFILE_PRIMARY`
4. `REAR_3Q_PRIMARY`
5. `BODY_FRONT`
6. `BODY_BACK`

Tier B 必须记录 `primary_side = LEFT | RIGHT`。`FACE_3Q_PRIMARY / PROFILE_PRIMARY / REAR_3Q_PRIMARY` 默认使用同一侧方向，避免同一角色的核心参考左右混乱。

当正式镜头持续需要 opposite-side coverage，或角色发生明显视角复杂度升级时，应升级 Tier 或生成受控 Conditional Reference，不得长期依赖模型自行镜像推断。

### Tier C｜Limited Character

适用：少量出场、机位需求有限、无需完整 turnaround 的普通角色。

Minimum Set = **3-view**：

1. `FACE_IDENTITY`｜正面或 3/4 身份识别视图；具体取向必须在 Registry 中固定，不得同一角色反复变化
2. `BODY_FRONT`｜全身正面
3. `REAR_OR_BACK`｜背面或背侧识别视图；具体 Role 必须明确登记

Tier C 不是完整 turnaround 标准。若后续出现侧面对话、连续转头、多角度反复出场等需求，应补 Conditional Reference 或升级至 Tier B。

### Tier D｜Background / One-off Character

适用：群演、背景人物、一次性临时角色。

- 不要求建立完整 Character Core Set；
- 可按 Shot 需求生成最小角色参考或直接由场景 / 人群设计控制；
- 若角色开始重复出现、承担独立叙事功能或出现连续性要求，必须先升级为 Tier C 或更高等级，再进入持续生产。

## 3. Tier 判定依据

Tier 不只按“剧情重要程度”判断，应综合：

1. `narrative_importance`｜叙事重要性；
2. `screen_frequency`｜预计/实际出场频率；
3. `view_complexity`｜需要覆盖的机位与头身角度复杂度；
4. `continuity_sensitivity`｜人物一致性对镜头连续性的敏感程度；
5. `animation_requirement`｜是否存在转头、运动、表情或动画插值需求。

原则：**Production Need 决定 Tier，不为了形式完整制造无用资产。**

Tier 可以随生产需求升级。升级后，新 Tier 所要求的 Mandatory Core Set 补齐并经 Product Owner 批准后，才视为该 Tier 的 `PRODUCTION_READY`。

## 4. 统一摄影 / 生成标准

同一 Tier 内相同 Role 的人物资产必须尽可能使用统一制作条件，避免角色 A 与角色 B 的 Reference 标准不一致。

### Format Compliance｜硬性前置检查

- Character Atomic / Auxiliary production reference 的目标画幅统一为 **9:16 竖版**；
- generator-native 的极小像素取整误差可以接受，但视觉与几何上必须等效为 9:16，不得改成 3:4、2:3 或其他版式；
- 画幅不符合时，固定标准审核直接判定 FAIL，不进入 Identity / Role Accuracy 等后续质量判断；
- 不得为了把旧构图强行塞入 9:16 而造成明显拉伸、裁断人物关键结构或破坏角色比例。

### Fixed Standard Review｜P1 生产审核顺序

P1 人物补图统一采用：

`Generation → 用户发送【审核】→ Fixed Standard Review → PASS / Targeted Revision`

固定审核顺序：

1. `Format Compliance`
2. `Identity`
3. `Role Accuracy`
4. `Continuity`
5. `Production Utility`
6. `Reference Type Purity`
7. `Problem Check`

普通 Chat 中图片生成完成后不会自动触发下一轮文本审核，因此“自动审核”不作为流程名称；生成完成后等待 Product Owner 发送最短触发词 `【审核】`。

### Face / Head Views

- 中性或轻度自然表情，不做剧情表演；
- 眼平机位；
- 中性、低干扰背景；
- 均匀、可辨识五官结构的光线；
- 不使用戏剧性景深、强烈透视或夸张镜头；
- 同类 Role 的头部/上半身占画比例保持一致；
- 角度含义严格按 Role 定义，不以“看起来差不多”替代。

### Full Body Views

- 从头到脚完整可见；
- 自然中立站姿；
- 眼平或接近眼平机位；
- 不使用明显广角畸变；
- 默认服装完整可见；
- 统一背景和基础光线；
- 人物在画面中的尺度尽量统一，便于跨角色比较身形比例。

## 5. Costume / Prop 边界

Character Core Set 主要定义“这个人是谁”和基础体型/轮廓。

- `BODY_FRONT / BODY_BACK` 可以穿该角色当前默认服装，用于定义人物整体 silhouette；
- 复杂服装结构、可替换服装、关键配饰和独立道具不得只依赖 Character Core Set，应作为 Costume / Prop Entity 单独管理；
- 与人物身份不可分割的固定特征可以出现在 Core Set 中，但仍应在 Registry 中明确其职责；
- 不因某次剧情镜头需要而把临时状态永久写入 Character Core Set。

## 6. Conditional Reference / Variant

以下内容默认不要求所有角色预制：

- opposite-side additional view（Tier B/C）；
- Expression Sheet；
- 特殊手部 / 足部；
- 特殊动作 / pose；
- wet / injured / bloodstained / dirty 等人物状态；
- costume variant；
- 年龄 / 时间阶段变化；
- 极端俯视、仰视或特殊镜头角度。

Conditional Reference 必须有明确生产用途，并登记其适用范围；不得因为“以后也许会用”而无限扩充资产库。

## 7. Atomic Master 与 Character Reference Sheet

Mandatory Core Set 的单张权威资产属于 `Atomic Character Assets`。

日常生产默认使用由当前有效 Atomic Assets 派生的：

`CHARACTER_REFERENCE_SHEET`

规则：

- Reference Sheet 是生产便利层，不取代 Atomic Master 的事实权威；
- Reference Sheet 必须记录其 `derived_from` Asset IDs 和版本；
- 上游 Atomic Master 被替代后，系统必须能够标记受影响的 Reference Sheet；
- 默认目标为每个需要持续生产的角色至少一张 Current Character Reference Sheet；若单张图无法保持有效分辨率，可拆分为 Identity / Body 等少量派生 Sheet，但不得无理由增加 Sheet 数量。

## 8. Resolver 使用规则

正常路径不得由 Product Owner 手工进入 Library 挑人物参考图。

Reference Resolver 根据：

`character entity + tier + requested view/pose + costume + state/variant + continuity requirement`

自动选择：

1. 当前 `CHARACTER_REFERENCE_SHEET`；
2. 如镜头需要，再追加与视角最匹配的 Current Atomic Character Asset；
3. 如所需视角不存在且不能由当前 Tier 安全覆盖，返回 `REFERENCE_GAP`，不得静默使用废弃资产或把镜像图当作新的权威事实。

## 9. Production Readiness

角色的 Tier 完整度应可机器计算。

示例：

`Tier A Core Coverage = 9 / 9`

角色只有在以下条件同时满足时，才可标记该 Tier 的 `PRODUCTION_READY`：

- 当前 Tier 的 Mandatory Core Set 完整；
- 所有 Mandatory Core Assets 均为 Product Owner Approved；
- 生命周期为 `CURRENT`；
- 不存在同一 `entity + role + variant` 多个 Current 的冲突；
- 默认 Character Reference Sheet 可用，或已明确记录临时例外。

Tier D 不按 Core Coverage 计算 Production Readiness。

## 10. Approval / Lifecycle

本规则沿用 Visual Asset Management System V1：

- 只有 Product Owner 明确批准的图像才进入正式 Asset Registry；
- `approval_status = APPROVED` 与生命周期分离；
- 生命周期只使用 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；
- DRAFT / CANDIDATE / REVIEWED / REJECTED 属于生成与审核日志，不进入正式 Asset Registry。

## 11. Audit Trail

人物资产至少必须可追溯：

- character tier 及其变更；
- Atomic Role；
- 生成来源 / model / prompt or instruction / input references；
- Product Owner approval；
- version / supersession；
- Reference Sheet dependency；
- 被哪些 Reference Package / Shot 使用；
- Tier 升级原因及缺失资产补齐记录。

## 12. 当前验证状态

截至 2026-09-13：

- Tier Assignment V1 已锁定；
- Gap Mapping V1 已锁定；
- D-059 已完成 48 张 canonical Character references 的迁移；
- D-060～D-063 已验证 Character Reference Package 自动选图、P1 role 泛化、Migration + Runtime Current 统一解析；
- Automatic Ingest 已通过真实 `PROFILE_LEFT` / `REAR_3Q_LEFT` 资产验证；
- Controlled Current Supersession 已通过 `PROFILE_LEFT V001 → V002` 真实替换验证；
- 宁秋水 P1 Wave 1 已完成，当前 Tier A Core Coverage = `8 / 9`；
- 尚未完成全部角色 Core Gap、Derived Character Reference Sheet、完整 Shot-level Reference Resolver / Audit reverse-trace，因此 P0.2 Gate 仍为 ACTIVE。
