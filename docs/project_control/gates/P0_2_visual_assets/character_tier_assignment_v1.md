# P0.2-03｜Character Tier Assignment V1

Status: `LOCKED / PRODUCT OWNER APPROVED`

Date: 2026-09-13

本文件记录《诡舍·黑衣夫人》9 名正式角色在 Visual Asset Management System V1 下的正式 Tier Assignment。

本次只锁定 Tier，不代表 P0.2 Gate PASS，也不代表现有资产已经满足对应 Tier 的 Mandatory Core Set。

判定依据沿用 `character_asset_rules_v1.md`：

1. narrative_importance；
2. screen_frequency；
3. view_complexity；
4. continuity_sensitivity；
5. animation_requirement。

原则：Production Need 决定 Tier，不按“现有图片数量”反推 Tier。

## 1. Locked Tier Assignment

### Tier A｜Core Character

- 宁秋水｜`CHAR_NING_QIUSHUI`
- 君鹭远｜`CHAR_JUN_LUYUAN`
- 尼尔｜`CHAR_NEIL`
- 黑衣夫人｜`CHAR_BLACK_LADY`

Tier A Mandatory Core Set = 9-view canonical turnaround：

`FACE_FRONT / FACE_3Q_LEFT / FACE_3Q_RIGHT / PROFILE_LEFT / PROFILE_RIGHT / REAR_3Q_LEFT / REAR_3Q_RIGHT / BODY_FRONT / BODY_BACK`

### Tier B｜Important Supporting Character

- 温倾雅｜`CHAR_WEN_QINGYA`
- 苏小小｜`CHAR_SU_XIAOXIAO`
- 廖健｜`CHAR_LIAO_JIAN`
- 古堡小主人｜`CHAR_CASTLE_YOUNG_MASTER`

Tier B Mandatory Core Set = 6-view：

`FACE_FRONT / FACE_3Q_PRIMARY / PROFILE_PRIMARY / REAR_3Q_PRIMARY / BODY_FRONT / BODY_BACK`

Tier B 必须在 Gap Mapping 中确定 `primary_side = LEFT | RIGHT`，且 FACE_3Q / PROFILE / REAR_3Q 三项默认使用同一侧。

### Tier C｜Limited Character

- 光勇｜`CHAR_GUANG_YONG`

Tier C Minimum Set = 3-view：

`FACE_IDENTITY / BODY_FRONT / REAR_OR_BACK`

具体 `FACE_IDENTITY` 与 `REAR_OR_BACK` 由迁移映射到明确 canonical Role，不保留模糊职责。

### Tier D｜Background / One-off

当前 9 名正式命名角色中：`NONE`。

Tier D 保留给未来真正的群演、背景人物与一次性临时角色。

## 2. Locked Distribution

- Tier A = 4
- Tier B = 4
- Tier C = 1
- Tier D = 0

## 3. Initial Gap Baseline

以下仅为 P0.2-03 初始估算，用于启动 Gap Mapping；最终数字必须由真实 Approved/Current 资产逐项映射确认。

| Character | Tier | Mandatory Slots | Initial Mappable Coverage | Initial Core Gap |
|---|---:|---:|---:|---:|
| 宁秋水 | A | 9 | 6 | 3 |
| 君鹭远 | A | 9 | 6 | 3 |
| 尼尔 | A | 9 | 6 | 3 |
| 黑衣夫人 | A | 9 | 4 | 5 |
| 温倾雅 | B | 6 | 4 | 2 |
| 苏小小 | B | 6 | 4 | 2 |
| 廖健 | B | 6 | 4 | 2 |
| 古堡小主人 | B | 6 | 4 | 2 |
| 光勇 | C | 3 | 3 | 0 |

Initial total：

- Mandatory Core Slots = 66
- Initial Mappable Coverage ≈ 43
- Initial Core View Gap ≈ 23

这些数字不是“必须补 23 张图”的生产指令。后续必须把缺口分类为：

- `CORE_VIEW_GAP`
- `REFERENCE_SHEET_GAP`
- `STATE_VARIANT_GAP`
- `NO_ACTION_REQUIRED`

只有对当前/近期生产有真实价值的缺口才进入补资产任务。

## 4. Confirmed Ning Qiushui Example

宁秋水已完成第一轮真实 Migration Review。

若按本次已锁定 Tier A 计算，当前标准 Coverage = 6/9：

- `FACE_FRONT` ✓
- `FACE_3Q_RIGHT` ✓
- `PROFILE_RIGHT` ✓
- `REAR_3Q_RIGHT` ✓
- `BODY_FRONT` ✓
- `BODY_BACK` ✓
- `FACE_3Q_LEFT` GAP
- `PROFILE_LEFT` GAP
- `REAR_3Q_LEFT` GAP

该结果仅用于证明新 Schema / Mapping 逻辑成立；具体补图时机由 Production Need 决定。

## 5. Next Step

P0.2-03 下一步进入角色级 Asset Gap Mapping：

1. 对 Tier B 四人确认 `primary_side`；
2. 对 Tier A 四人确认左右方向的真实 Current Coverage；
3. 把旧 `Face Master / Body Master / Angle Reference / Back Reference / Auxiliary Reference` 映射到 Schema V0.3 canonical Role；
4. 分离 Core View Gap、Reference Sheet Gap、State / Variant Gap；
5. 不在 Gap Mapping 完成前批量补图。

最终 Tier / Gap 结果写入 Registry 后，角色是否 `PRODUCTION_READY` 由机器规则计算，不人工维护第二套状态。
