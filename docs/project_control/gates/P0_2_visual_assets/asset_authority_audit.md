# P0.2｜Visual Asset Authority Audit

Status: `IN_PROGRESS / DOCUMENTARY BASELINE ESTABLISHED`

Date: 2026-09-12

## 1. Audit goal

P0.2 不重做已有图片。先确认现有视觉资产的类别、权威层级、状态、可复用范围与禁止用途，再决定是否需要补资产或工程核验。

## 2. Current documented inventory baseline

### Character identity assets

- 9 名正式人物：宁秋水、君鹭远、尼尔、温倾雅、苏小小、廖健、光勇、古堡小主人、黑衣夫人。
- 每名人物均有 4 项正式职责：`face_master / body_master / angle_reference / back_reference`。
- 现有记录显示 36 项正式职责均为 `approved + current_master=true`，且每项唯一。
- 正常基础身份状态均保持 `frozen / frozen_for_production`；特殊状态按既有记录分别保持 `deferred / eligible_not_started`。

### Auxiliary character references

- D-055：8 张 `production_auxiliary_reference` + 1 张尼尔 `supplementary_auxiliary_reference`。
- D-056：宁秋水新增 3 张 `production_auxiliary_reference`。
- 共计 12 张侧向/辅助类资产；全部不得成为第五类 master，`current_master=false`。
- 宁秋水 Rear Three-quarter v002 为该辅助方向默认版本；v001 保留历史 approved，但不是默认。

### Scene Masters and current A-Series

- `CASTLE_ENTRANCE_OPEN_DOOR_DAY`：`APPROVED / SCENE_MASTER / REUSABLE_REFERENCE`。
- `FIRST_HALL_FIREPLACE`：`APPROVED / SCENE_MASTER / REUSABLE_REFERENCE`；壁炉状态锁定 `EXTINGUISHED / NOT BURNING`。
- A01–A07：7 张正式镜头资产，现有记录为 `APPROVED / LOCK / ARCHIVED`。
- A08：`NOT APPROVED / HOLD_FOR_ANIMATIC_REVIEW`；approved 正式资产数 = 0。

### Legacy / evidence-only assets

- 旧 `A Candidate` / D-054 撤销资产：历史保留，但 `NOT_ADOPTED`，不得恢复为 active production reference。
- 宁秋水单人物一致性测试 15 张：`evidence_only`。
- 宁秋水＋君鹭远双人物测试 11 张：`evidence_only`；常规双人物/相邻镜头有试行价值，复杂受力交互仍 FAIL。
- SH01–SH08：保留各自历史批准与 QA 事实，但与当前 A-Series 严格隔离；不得因为历史 approved 自动成为 A-Series 的人物身份或连续性权威来源。
- 例外补充参考：SH02 继续作为尼尔电影镜头形象的优先补充参考；SH08 第二版继续作为黑衣夫人批准补充镜头参考，但均不替代正式 master。

## 3. Preliminary authority hierarchy

当前先采用以下审计工作顺序，待 P0.2 结束前由 Product Owner 审批锁定：

1. `Character Master`：人物身份最高视觉权威。
2. `Approved Auxiliary Reference`：只补充特定角度/结构，不得覆盖 master。
3. `Scene Master`：场景空间、光线、固定环境元素的最高场景参考。
4. `Locked A-Series Shot Asset`：具体镜头的画面事实，可用于镜头连续性；不得反向替代 Character Master / Scene Master。
5. `Legacy approved SH asset / supplementary shot reference`：仅在明确指定用途时作为历史或补充参考。
6. `evidence_only test asset`：只证明能力边界，不进入正式生成 reference set。
7. `candidate / rejected / not_adopted / invalid_test`：不得作为正向生产参考。

## 4. P0.2-01 unresolved checks

1. 核对当前本地 4 份 canonical register：`SHOT_REGISTER.csv / ASSET_REGISTER.csv / IMAGE_REGISTER.csv / IMAGE_RENAME_MANIFEST.csv` 与实际 107 张图库实体是否仍一致。
2. 为 A01–A07 明确 `ARCHIVED` 的语义：它是“已锁定镜头资产的文件管理状态”，不是 `rejected`；确认后续 Animatic / Shot Plan 是否仍允许调用。
3. 明确 SH 系列除 SH02 / SH08 指定补充职责外，是否统一降为 `legacy_reference_only`，防止与 A-Series 产生双权威。
4. 核对 12 张辅助人物资产的默认/非默认关系，确保同一目标角度不会出现两个 default reference。
5. 确认两张 Scene Master 的具体连续性字段与后续可继承边界。

## 5. Gate rule

P0.2 技术与治理条件满足后，只能进入 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`；必须由 Product Owner 明确批准后才可 `PASS`。
