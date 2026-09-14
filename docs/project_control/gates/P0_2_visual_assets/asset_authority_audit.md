# P0.2｜Visual Asset Authority Audit

Status: `IN_PROGRESS / AUTHORITY MINI-CLOSE LOCKED`

Date: 2026-09-13

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
- 宁秋水 Rear Three-quarter v002 为该辅助方向当前有效版本；v001 保留历史 approved，但后续迁移时应映射为 `SUPERSEDED`，不得与 v002 同时成为 Current。

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
- 例外补充参考：SH02 继续作为尼尔电影镜头形象的指定补充参考；SH08 第二版继续作为黑衣夫人指定补充镜头参考，但均不替代正式 master。

## 3. Authority Mini-Close｜Product Owner Approved 2026-09-13

以下四项业务规则已经 Product Owner 明确批准，作为后续 Registry Schema、Resolver 与资产迁移的正式前提。

### 3.1 A01–A07 `ARCHIVED` semantics

`ARCHIVED` 表示已完成、已冻结、不再作为可迭代 Master 维护的正式镜头资产；不等于失效、Rejected 或禁止调用。

A01–A07 后续迁移目标：

- `approval_status = APPROVED`
- `lifecycle = ARCHIVED`
- `authority_class = CONTINUITY`
- `resolver_usage = CONDITIONAL`

允许在 continuity reference、previous-shot reference、explicit shot reference 等明确场景下由 Resolver 调用；不得反向替代 Character Master / Scene Master。

### 3.2 SH series authority boundary

SH01–SH08 默认统一降为受限历史补充层：

- `authority_class = LEGACY_SUPPLEMENTARY`
- `resolver_usage = NEVER`

保留两个明确例外：

- SH02：尼尔指定补充参考，`resolver_usage = CONDITIONAL`；
- SH08 V2：黑衣夫人指定补充参考，`resolver_usage = CONDITIONAL`。

仅当 Shot / Task Spec 明确满足指定用途时，例外资产才可进入 Reference Package。历史 approved 不自动形成当前 A-Series / Character Master 的双权威。

### 3.3 Auxiliary Current rule

取消独立的 `default=true / false` 事实层，不再同时维护 `current / default / latest` 三套概念。

对相同：

`entity_id + role + variant + state`

正式 Registry 最多只允许一个 `lifecycle = CURRENT` 的资产。Resolver 的默认选择由 Current 状态推导。

因此同方向历史 approved 辅助图可以保留，但旧版本必须为 `SUPERSEDED` 等非 Current 生命周期；不得与新版本同时作为 Current。

### 3.4 Scene Master inheritance boundary

Scene Master 锁定的是场景事实，不锁死单个 Shot 的摄影表现。

必须继承的场景事实包括：

- 空间拓扑 / 房间结构；
- 固定建筑元素；
- 固定关键物件及其位置关系；
- 已锁定连续性状态；
- 核心材质与建筑身份。

Shot 可变化的表现层包括：

- 机位；
- 景别；
- 焦段；
- 人物站位；
- 遮挡；
- 景深；
- 局部曝光；
- 构图。

若要改变 `DAY / NIGHT`、门开闭、壁炉熄灭 / 点燃等场景事实，不得在 Shot 中静默改变；必须通过受控 Scene `Variant / State` 建立对应状态，再由 Resolver 调用正确资产。

## 4. Locked authority model for Registry / Resolver design

Authority、Lifecycle、Resolver Usage 三个维度必须分离：

- `Authority`：资产能够证明什么；
- `Lifecycle`：资产当前处于什么版本状态；
- `Resolver Usage`：生产时是否以及在何种条件下允许调用。

当前 Authority 层级：

1. `MASTER`：Character / Scene / Costume / Prop 的最高事实基线；
2. `AUXILIARY`：特定角度或结构补充；
3. `DERIVED`：Reference Sheet 等派生资产；
4. `CONTINUITY`：A01–A07 等正式 Shot Asset 的镜头连续性事实；
5. `SUPPLEMENTARY`：当前明确允许的补充参考；
6. `LEGACY_SUPPLEMENTARY`：SH 等历史资产；
7. evidence-only / candidate / rejected / not-adopted / invalid-test：不得作为正常正向生产参考。

该层级不意味着低层资产可以覆盖高层资产；Resolver 必须结合 `authority_class + lifecycle + resolver_usage + Shot/Task Spec` 决定实际调用。

## 5. Remaining P0.2-01 checks

Authority Mini-Close 已解决此前关于 A01–A07 ARCHIVED 语义、SH 权威边界、Auxiliary default/current 逻辑与 Scene Master 继承边界的设计决策。

仍需完成的工程核对：

1. AO-01：四份旧 Register 在当前可取得范围内均缺失；BL-D-028 已接受不重建、退出 Current authority。可取得 Manifest / Runtime / canonical storage 已核对；旧表内部项 `UNKNOWN / SOURCE UNAVAILABLE`。AO-01 已远端验证为 `COMPLETE / VERIFIED`；
2. 在真实资产迁移时验证 12 张辅助人物资产均能唯一映射到新 Registry Role / Variant / State / Lifecycle，不产生多个 Current；
3. 在 Scene Registry / Scene Spec 阶段把两张 Scene Master 的具体事实字段结构化登记。

上述工程核对不阻塞当前 Entity / Asset Registry Schema 的 V0.3 Walkthrough，但必须在 P0.2 Gate Review 前完成。

## 6. Gate rule

P0.2 技术与治理条件满足后，只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确批准后才可标记 `PASS`。
