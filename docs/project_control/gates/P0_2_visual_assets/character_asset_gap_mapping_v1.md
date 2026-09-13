# P0.2-03｜9 Character Asset Gap Mapping V1

Status: `LOCKED / PRODUCT OWNER APPROVED BASELINE`

Locked on: `2026-09-13`

本文件记录 9 名正式角色基于实图逐项核对后的 Character Core Coverage 与 Gap。它替代此前聊天和 Dashboard 中的初算值。

## 1. Corrected baseline

已锁定 Tier：

- Tier A：宁秋水 / 君鹭远 / 尼尔 / 黑衣夫人
- Tier B：温倾雅 / 苏小小 / 廖健 / 古堡小主人
- Tier C：光勇
- Tier D：当前 9 名正式角色中无

Mandatory Core Slots：

- Tier A：4 × 9 = 36
- Tier B：4 × 6 = 24
- Tier C：1 × 3 = 3
- Total = `63`

实图确认结果：

- Confirmed Core Coverage = `40`
- Core View Gap = `23`
- Core Coverage = `40 / 63 = 63.5%`

此前出现过的 `66 / 43 / 23` 与 `63 / 41 / 22` 均为初算，不再使用。

## 2. Character summary

| Character | Tier | Primary / Dominant Side | Mandatory | Covered | Core Gap |
|---|---:|---|---:|---:|---:|
| 宁秋水 | A | RIGHT coverage | 9 | 6 | 3 |
| 君鹭远 | A | RIGHT coverage | 9 | 6 | 3 |
| 尼尔 | A | LEFT coverage | 9 | 6 | 3 |
| 黑衣夫人 | A | — | 9 | 3 | 6 |
| 温倾雅 | B | LEFT | 6 | 4 | 2 |
| 苏小小 | B | LEFT | 6 | 4 | 2 |
| 廖健 | B | LEFT | 6 | 4 | 2 |
| 古堡小主人 | B | LEFT | 6 | 4 | 2 |
| 光勇 | C | n/a | 3 | 3 | 0 |
| **TOTAL** |  |  | **63** | **40** | **23** |

LEFT / RIGHT 继续沿用已锁定 screen-facing convention：面部/鼻尖朝画面右侧 = RIGHT；朝画面左侧 = LEFT。

## 3. Tier A exact mapping

### 宁秋水｜6 / 9

Current Core：

- `FACE_FRONT`
- `FACE_3Q_RIGHT`
- `PROFILE_RIGHT`
- `REAR_3Q_RIGHT`
- `BODY_FRONT`
- `BODY_BACK`

Core Gap：

- `FACE_3Q_LEFT`
- `PROFILE_LEFT`
- `REAR_3Q_LEFT`

### 君鹭远｜6 / 9

Current Core：

- `FACE_FRONT`
- `FACE_3Q_RIGHT`
- `PROFILE_RIGHT`
- `REAR_3Q_RIGHT`
- `BODY_FRONT`
- `BODY_BACK`

Core Gap：

- `FACE_3Q_LEFT`
- `PROFILE_LEFT`
- `REAR_3Q_LEFT`

`front_three_quarter_body_body_master` 不重复占用标准 `FACE_3Q_RIGHT` Core Slot；迁移时作为结构/姿态型 Supplementary / Conditional 资产处理。

### 尼尔｜6 / 9

Current Core：

- `FACE_FRONT`
- `FACE_3Q_LEFT`
- `PROFILE_LEFT`
- `REAR_3Q_LEFT`
- `BODY_FRONT`
- `BODY_BACK`

Core Gap：

- `FACE_3Q_RIGHT`
- `PROFILE_RIGHT`
- `REAR_3Q_RIGHT`

尼尔存在两张背侧 3/4 历史资产；正式迁移时同一 `role + variant + state` 只允许一个 `CURRENT`，另一张必须作为 Supplementary / Conditional 或其他明确非冲突职责。

### 黑衣夫人｜3 / 9

Current Core：

- `FACE_FRONT`
- `BODY_FRONT`
- `BODY_BACK`

Core Gap：

- `FACE_3Q_LEFT`
- `FACE_3Q_RIGHT`
- `PROFILE_LEFT`
- `PROFILE_RIGHT`
- `REAR_3Q_LEFT`
- `REAR_3Q_RIGHT`

Product Owner 已判定旧：

`CHAR_black_lady_three_quarter_half_body_angle_reference_v001.png`

人物 likeness 不足，后续重制。迁移目标：

- historical approval fact 保留
- `lifecycle = DEPRECATED`
- `resolver_usage = NEVER`
- 不计入 Current Core Coverage

## 4. Tier B exact mapping

四名 Tier B 角色的 `primary_side` 均已通过实图锁定为 `LEFT`。

### 温倾雅｜4 / 6

Current Core：`FACE_FRONT / FACE_3Q_PRIMARY(LEFT) / BODY_FRONT / BODY_BACK`

Gap：`PROFILE_LEFT / REAR_3Q_LEFT`

### 苏小小｜4 / 6

Current Core：`FACE_FRONT / FACE_3Q_PRIMARY(LEFT) / BODY_FRONT / BODY_BACK`

Gap：`PROFILE_LEFT / REAR_3Q_LEFT`

### 廖健｜4 / 6

Current Core：`FACE_FRONT / FACE_3Q_PRIMARY(LEFT) / BODY_FRONT / BODY_BACK`

Gap：`PROFILE_LEFT / REAR_3Q_LEFT`

### 古堡小主人｜4 / 6

Current Core：`FACE_FRONT / FACE_3Q_PRIMARY(LEFT) / BODY_FRONT / BODY_BACK`

Gap：`PROFILE_LEFT / REAR_3Q_LEFT`

## 5. Tier C exact mapping

### 光勇｜3 / 3

Tier C Mandatory Core：

- `FACE_IDENTITY`
- `BODY_FRONT`
- `REAR_OR_BACK`

Core Coverage = `3 / 3`，Core Gap = `0`。

现有 `FACE_3Q_RIGHT / PROFILE_RIGHT / REAR_3Q_RIGHT` 可继续作为 Beyond-Minimum / Conditional Reference 使用，但不改变其 Tier C 身份，也不计入 Tier C Mandatory Core 分母。

## 6. Derived gap

除 Core View Gap 外，当前 9 名正式角色尚未完成 Schema V0.3 下正式登记的 Current `CHARACTER_REFERENCE_SHEET`。

因此另有：

- `REFERENCE_SHEET_GAP = 9`

该项是 Derived Asset Gap，不与 23 个 Core View Gap 相加为“需要额外生成 32 张人物锚定图”。Reference Sheet 应由 Current Atomic Assets 派生。

## 7. Production rule

`23 Core View Gaps ≠ immediately generate 23 images`。

所有 Gap 必须按 Production Need 排序；正式优先级与执行清单见：

`character_gap_priority_v1.md`
