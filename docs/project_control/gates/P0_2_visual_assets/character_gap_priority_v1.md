# P0.2-03｜Character Gap Priority Classification + P1 Execution V1

Status: `LOCKED / PRODUCT OWNER APPROVED BASELINE`

Locked on: `2026-09-13`

本文件把 `character_asset_gap_mapping_v1.md` 中确认的 23 个 Core View Gap 按生产优先级分层，并锁定第一批 P1 执行清单。

注意：这里的 `P1 / P2 / P3` 是 Gap Production Priority，不是项目阶段编号，不等同于 `P0.1 / P0.2 / P0.3`。

## 1. Priority definition

- `P1`：当前优先补制。优先解决高频角色在侧面对话、反打、行进、背侧回头等镜头中的生产风险。
- `P2`：Core 必补，但不阻塞当前第一批生产。
- `P3`：可延后；当前不应抢占 P1/P2 资源。

该优先级是当前生产基线，可随 Shot Plan 和真实生产需求调整；任何变更需保留 Audit / Decision 记录。

## 2. Corrected 23-gap classification

### P1｜10

1. 宁秋水 `PROFILE_LEFT`
2. 宁秋水 `REAR_3Q_LEFT`
3. 君鹭远 `PROFILE_LEFT`
4. 君鹭远 `REAR_3Q_LEFT`
5. 尼尔 `PROFILE_RIGHT`
6. 尼尔 `REAR_3Q_RIGHT`
7. 苏小小 `PROFILE_LEFT`
8. 苏小小 `REAR_3Q_LEFT`
9. 廖健 `PROFILE_LEFT`
10. 廖健 `REAR_3Q_LEFT`

### P2｜7

1. 宁秋水 `FACE_3Q_LEFT`
2. 君鹭远 `FACE_3Q_LEFT`
3. 尼尔 `FACE_3Q_RIGHT`
4. 温倾雅 `PROFILE_LEFT`
5. 温倾雅 `REAR_3Q_LEFT`
6. 古堡小主人 `PROFILE_LEFT`
7. 古堡小主人 `REAR_3Q_LEFT`

### P3｜6

黑衣夫人侧向体系整体延后重建：

1. `FACE_3Q_LEFT`
2. `FACE_3Q_RIGHT`
3. `PROFILE_LEFT`
4. `PROFILE_RIGHT`
5. `REAR_3Q_LEFT`
6. `REAR_3Q_RIGHT`

Total = `10 + 7 + 6 = 23`。

光勇 Tier C Core 已 `3/3`，不在 23 个 Core Gap 中。

## 3. P1 execution order

P1 按人物整组执行，不跨角色交错生产：

1. 宁秋水
2. 君鹭远
3. 尼尔
4. 苏小小
5. 廖健

每人先完成两张：

- 缺失侧 `PROFILE`
- 缺失侧 `REAR_3Q`

## 4. P1 exact execution checklist

### Wave 1｜宁秋水

Target Roles：

- `PROFILE_LEFT`
- `REAR_3Q_LEFT`

Legacy-style working filenames before Automatic Ingest may be human-readable working names, but formal V0.3 filename must ultimately be generated from Registry metadata using：

`<ENTITY_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`

Canonical targets：

- `CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
- `CHAR_NING_QIUSHUI_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Reference priority：Face Master → Current Angle/3Q identity reference → Current opposite-side Profile / Rear 3Q → Body Master when needed for silhouette.

QC emphasis：保持宁秋水偏长脸型、克制坚毅气质；不得过嫩、过圆或偶像化。Rear 3Q 以背向为主，只保留足够身份识别的侧脸信息。

### Wave 2｜君鹭远

Target Roles：

- `PROFILE_LEFT`
- `REAR_3Q_LEFT`

Canonical targets：

- `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
- `CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Reference priority：Face Master → Current `FACE_3Q_RIGHT` / Angle Reference → Current `PROFILE_RIGHT` / `REAR_3Q_RIGHT` → Body Master.

QC emphasis：保持人物成熟、稳定、克制；不得过度年轻或锐化。Rear 3Q 要服务与宁秋水同场时的侧后观察、行进与反应镜头。

### Wave 3｜尼尔

Target Roles：

- `PROFILE_RIGHT`
- `REAR_3Q_RIGHT`

Canonical targets：

- `CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`
- `CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Reference priority：Face Master → Current `FACE_3Q_LEFT` → Current `PROFILE_LEFT` / `REAR_3Q_LEFT` → Body / Costume references.

QC emphasis：必须像已锁定尼尔，而不是泛化英国绅士。服装连续性保持黑色管家轮廓、白衬衫/领结逻辑；画幅允许时保持十字架与白手帕角的一致性。重点检查发型、肩线、体型和年龄结构。

### Wave 4｜苏小小

Target Roles：

- `PROFILE_LEFT`
- `REAR_3Q_LEFT`

Canonical targets：

- `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
- `CHAR_SU_XIAOXIAO_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Reference priority：Face Master → Current `FACE_3Q_PRIMARY(LEFT)` → Body Front/Back.

QC emphasis：保持现实人物感与既有人物身份，不二次元化、不过度柔美或甜化；Rear 3Q 要能在群像中稳定区分人物。

### Wave 5｜廖健

Target Roles：

- `PROFILE_LEFT`
- `REAR_3Q_LEFT`

Canonical targets：

- `CHAR_LIAO_JIAN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`
- `CHAR_LIAO_JIAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Reference priority：Face Master → Current `FACE_3Q_PRIMARY(LEFT)` → Body Front/Back.

QC emphasis：保持普通现实男性质感，不英雄化、不过度精英化；Rear 3Q 重点检查身形、肩背和头型识别稳定性。

## 5. Uniform production standard for all P1 assets

任务性质：`production auxiliary reference`，不是正式剧情 Shot、海报或情绪肖像。

统一要求：

- 中性低干扰背景；
- 单人，无剧情环境；
- 写实风格与当前 approved Character References 一致；
- Profile = 标准 90° 侧脸，bust framing；
- Rear 3Q = 标准约 135° 背侧视角，half-body framing；
- 中性、克制表情；
- 眼平或接近眼平机位；
- 不做夸张透视、戏剧性景深或动作表演；
- LEFT / RIGHT 按 screen-facing convention 判定。

## 6. P1 approval criteria

每张图至少满足：

1. Character identity 稳定；
2. Role 角度明确，不模糊成其他 3/4 角度；
3. 服装、发型、体型与现有 Current References 连续；
4. 明确属于中性生产辅助参考，而非剧情图；
5. 能安全服务正式 Shot 生产；
6. Product Owner 明确批准后才可进入正式 Asset Registry / Automatic Ingest。

## 7. Black Lady note

黑衣夫人旧 `three_quarter_half_body_angle_reference_v001` 已由 Product Owner 判定 likeness 不足，迁移目标为 `DEPRECATED / resolver NEVER`。黑衣夫人 6 个侧向 Core Gap 全部归入 P3，后续作为独立人物侧向体系重建任务处理，不与当前 P1 混做。
