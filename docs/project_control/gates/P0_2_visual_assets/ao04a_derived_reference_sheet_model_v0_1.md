# AO-04A｜Derived Character Reference Sheet Model + Approval Boundary V0.1

Status: `APPROVED / PRODUCT OWNER APPROVED 2026-09-17`

Project: `BLACK-LADY-001 / 诡舍·黑衣夫人`

Gate: `P0.2｜人物锚定与 Scene Master 资产治理`

Task: `AO-04｜9 Character Derived Reference Sheets`

## 1. Purpose

AO-04 建立 9 名正式 Character 的 `DERIVED_REFERENCE / CHARACTER_REFERENCE_SHEET`，用于后续 Resolver / image-production environment 一次性读取多张已批准人物参考资产。

Reference Sheet 的职责仅是把既有正式 Atomic Character Assets 以确定性版式组合为可追踪的派生参考资产。它不是新的人物事实源，也不增加 Character Core Coverage。

## 2. Non-generative rule

Reference Sheet 必须由现有正式 Atomic Assets 直接确定性拼版生成：

- 不使用生成式 AI 重绘人物；
- 不修改人物脸、发型、服装、体型或姿态；
- 不做镜像推断；
- 不用插值或补画方式制造不存在的视角；
- 不允许 `DEPRECATED / NEVER` 资产填补正式 Core Slot；
- 不得为了形成完整九宫格而伪造资产或 Coverage。

缺失正式视角时，对应格必须明确标记：

`REFERENCE_GAP`

## 3. Authority boundary

Atomic Asset 继续拥有角色身份、视角与结构事实的正式权威。

Reference Sheet：

- `asset_class = DERIVED_REFERENCE`
- `role = CHARACTER_REFERENCE_SHEET`
- `authority_class = DERIVED`

Reference Sheet 不得反向覆盖 Atomic Master / Auxiliary 的 Authority、Lifecycle、Role、Variant、State 或 Core Coverage。

`REFERENCE_SHEET exists ≠ Core View exists`

例如黑衣夫人当前缺失的侧向 Core Views 即使 Sheet 已建立，Atomic Gap 仍保持原状态。

## 4. Tier-driven deterministic layout

### Tier A

3×3 canonical grid，目标 Slot：

1. `FACE_FRONT`
2. `FACE_3Q_LEFT`
3. `FACE_3Q_RIGHT`
4. `PROFILE_LEFT`
5. `PROFILE_RIGHT`
6. `REAR_3Q_LEFT`
7. `REAR_3Q_RIGHT`
8. `BODY_FRONT`
9. `BODY_BACK`

缺失 Slot 显示 `REFERENCE_GAP`。

### Tier B

2×3 canonical grid：

1. `FACE_FRONT`
2. `FACE_3Q_PRIMARY`
3. `PROFILE_PRIMARY`
4. `REAR_3Q_PRIMARY`
5. `BODY_FRONT`
6. `BODY_BACK`

Tier B 当前已批准的 `primary_side = LEFT` 适用于：

- `CHAR_WEN_QINGYA`
- `CHAR_SU_XIAOXIAO`
- `CHAR_LIAO_JIAN`
- `CHAR_CASTLE_YOUNG_MASTER`

因此 `FACE_3Q_PRIMARY / PROFILE_PRIMARY / REAR_3Q_PRIMARY` 映射至相应 LEFT canonical roles。

### Tier C

3-slot Minimum Sheet：

- `FACE_IDENTITY`
- `BODY_FRONT`
- `REAR_OR_BACK`

具体输入必须映射到已批准 canonical Atomic Role，不保留模糊职责。

当前 Tier C：`CHAR_GUANG_YONG`。

## 5. Runtime truth source

AO-04 必须从实时 Runtime / unified resolver truth 获取 `CURRENT + APPROVED` Atomic Assets。

历史 Gap 文档只作为历史基线和预期核对，不允许用历史 Coverage 替代实时 Registry。

例如 `CHAR_NING_QIUSHUI` 当前已存在新生产的 `PROFILE_LEFT` 与 `REAR_3Q_LEFT`；Sheet 必须反映实时 Current Assets，而不是 2026-09-13 的 6/9 historical baseline。

## 6. Character Entity prerequisite

AO-04 启动时已发现：Runtime `entity_registry.jsonl` 当前只有两个 Scene Entity，而正式 Character Assets 已大量存在。

在 Formal Derived Reference Asset 创建前，必须补齐 9 个 Stable Character Entity，并保持与已批准 Tier Assignment 一致：

### Tier A

- `CHAR_NING_QIUSHUI`
- `CHAR_JUN_LUYUAN`
- `CHAR_NEIL`
- `CHAR_BLACK_LADY`

### Tier B / primary_side=LEFT

- `CHAR_WEN_QINGYA`
- `CHAR_SU_XIAOXIAO`
- `CHAR_LIAO_JIAN`
- `CHAR_CASTLE_YOUNG_MASTER`

### Tier C

- `CHAR_GUANG_YONG`

Character Entity 补登记不得重建或改变既有 Character Assets，也不得产生第二套 Character identity。

## 7. Two-stage production model

### Stage A｜Candidate Build / Pre-approval

工程实现必须首先：

1. 补齐 9 个 Character Entity；
2. 建立 deterministic Reference Sheet Builder；
3. 从实时 Current/Approved Atomic Assets 生成 9 张 Candidate Sheet；
4. 生成 dependency manifest / provenance metadata；
5. 实现 dependency-staleness 计算与 automated tests；
6. 将 Candidate 置于正式 Registry 之外；
7. 停在 `WAITING_PRODUCT_OWNER_VISUAL_APPROVAL`。

在 Product Owner 对 9 张 Sheet 明确批准前：

- 不得写入 Formal Asset Registry；
- 不得分配正式 Derived Asset approval；
- 不得把 Candidate 标记为 CURRENT formal production asset。

### Stage B｜Formalization / Post-approval

Product Owner 明确批准 9 张 Sheet 后，才允许正式晋级：

- `asset_class = DERIVED_REFERENCE`
- `role = CHARACTER_REFERENCE_SHEET`
- `variant = DEFAULT`
- `state = DEFAULT`
- `approval_status = APPROVED`
- `lifecycle = CURRENT`
- `authority_class = DERIVED`
- `resolver_usage = DEFAULT` only when dependency validity passes

同时必须：

- 为每张 Sheet 记录实际使用的上游 `Asset IDs / versions / SHA`；
- 写入 `DERIVED_FROM` relations；
- 写入对应 Audit Events；
- 写入 canonical filename / storage_uri / sha256 / byte_size；
- 验证 Single Current；
- 验证 dependency validity。

Stage A 与 Stage B 属于同一个 AO-04 / D-068 工程任务，中间设置 Product Owner approval stop，不另占新的 D 编号。

## 8. Dependency stale rule

若任一上游 Atomic dependency 被：

- `SUPERSEDED`
- `DEPRECATED`
- invalidated / integrity failure

对应 Reference Sheet 必须动态计算为：

`DEPENDENCY_STALE`

规则：

- `DEPENDENCY_STALE` 不是 Lifecycle；
- Sheet 可以保持 `CURRENT`；
- 但不得继续作为 Resolver `DEFAULT` eligible input；
- 必须重新生成新版本并由 Product Owner 批准后恢复正常生产使用。

真实正式资产状态不得为了测试而被破坏。Staleness 测试应在 fixture / controlled test data 中模拟上游 supersede/deprecate/invalidation。

## 9. AO-04 Definition of Done

AO-04 只有同时满足以下 8 项才可提交最终验收：

1. 9 个 Character Entity 正式存在于 Entity Registry，Tier / primary_side 与已批准基线一致；
2. 9 张 Reference Sheet 均由实时 `CURRENT + APPROVED` Atomic Assets 确定性生成；
3. 无重绘、镜像、补画、deprecated/never 填槽或伪造 Coverage；
4. 缺失 Tier Core Slot 明确显示 `REFERENCE_GAP`；
5. 每张 Sheet 可精确追踪实际 `derived_from Asset IDs / versions / SHA`；
6. Product Owner 明确批准 9 张 Sheet 后才进入 Formal Asset Registry；
7. 至少一组 machine-verifiable dependency-staleness 正负案例通过，stale Sheet 不得 DEFAULT eligible；
8. Character / Scene Resolver、Automatic Ingest、Single Current、D-067 基线与完整测试回归不得被削弱。

## 10. Formal boundary

AO-04 完成不等于：

- P0.2 PASS；
- P1 Wave 2 自动解除 HOLD；
- AO-05 自动启动；
- Character Core Gap 自动减少。

AO-04 最终只能在完成 DoD 后提交 Product Owner 验收。Product Owner 明确批准前，不得标记 `COMPLETE / VERIFIED / CLOSED`。
