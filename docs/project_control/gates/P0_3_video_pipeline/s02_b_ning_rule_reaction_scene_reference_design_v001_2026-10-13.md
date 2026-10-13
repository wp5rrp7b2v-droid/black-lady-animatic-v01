# S02-B｜宁秋水「夫人的要求」反应插镜｜Scene Reference Design V0.1

日期：2026-10-13

**状态：PRODUCT OWNER APPROVED / SCENE REFERENCE DESIGN LOCKED / BUNDLE NOT YET AUTHORIZED**

## 1. 授权与范围

Product Owner 先前批准独立的宁秋水规则反应插镜导演概念；2026-10-13 对“Scene Reference Design 审核”节点明确回复“批准”。本次按已展示的三张参考方案锁定 **Scene Reference Design V0.1**，不将该批准扩大为 Bundle Build、Work 出图或正式母版修改。

上级批准概念：
`docs/project_control/gates/P0_3_video_pipeline/s02_b_ning_rule_reaction_editorial_insert_concept_2026-10-13.md`

临时剪辑测试标识：`TAIL_NING_REACTION_TEST_01`。它**不是正式 Story Shot ID**，正式命名和登记仅在独立候选视觉/剪辑验证后决定。

## 2. 镜头叙事与前后连续

既有正式序列末段：`N23 → N24 → A06 → N25 → N26`；N27 已吸收进 N26。

- **前镜 N25（已批准）：** 尼尔向古堡内部继续行进，平静、头也不回地回答“城堡大门只会在下雨天关闭”；人群仍主要处于停顿/转向阶段。
- **拟增画面（仅供局部测试）：** 尼尔说出“这是夫人的要求”时，独立切入宁秋水的克制观察反应。宁秋水只是记住这条特殊规则；不得暗示已知夫人的意图或危险真相。
- **后镜 N26（已批准）：** 回到尼尔领队、宁秋水和君鹭远跟随的群体运动；“各位，请随我来”自然接续。
- **音频责任边界：** “这是夫人的要求。各位，请随我来。”仍整体归属 N26。新增的是 **N26 台词期间的一次视觉插入**，不改变故事节点归属、不移动/重复/变速原音频。
- **时长与微切点：** UNKNOWN，需从正式音轨和原母版精确测量后，再制作局部 A/B；禁止仅按这份方案臆定秒数。

## 3. 镜头视觉设计

- 画幅：9:16 纵向；候选目标 941×1672 PNG，单张出图。
- 机位：**新的侧前方斜机位，宁秋水独立中近景/近景，3/4 侧脸可辨认**；明显区别于 N26 的群体中景/中远景。机位必须能合理存在于内门厅空间，不是 N26 已批准原图裁切。
- 镜头主语：**NING_QIUSHUI**；只需宁秋水成为第一视觉主体。无需尼尔或君鹭远在同一画面中证明人数完整。
- 动作：宁秋水正随人群由停顿转为前行，听到“夫人的要求”时目光极轻微停顿/转移；肩颈放松、步态不僵硬。此为静帧瞬间的导演语义，不要求动画。
- 情绪：警觉而内敛、留意信息，不惊讶、不恐慌、不皱眉夸张，不作已经理解规则的判断。
- 身体：自然步态；**严禁插袋**、双手交叉摆拍、正对镜头凝视。
- 场景：`CASTLE_ENTRANCE_INNER_LOBBY`；自然暗石墙/木构与有限纵深，背景可适度虚化但仍可识别为同一内部空间。禁止 First Hall、壁炉、主楼梯、新房间、门外晴空、可见雨、关门动作。
- 光色：延续 N25/N26 **低调暖暗光**，克制琥珀色灯光、自然皮肤、可读暗部、清晰无脏噪，不整体提亮。背景与人像应共享光照环境；不允许棚拍/抠图感。
- 不锁定左右屏幕方向：必须先核对 N25、N26 的批准画面与实际剪辑行进轴，再选可成立的机位侧别，防止跨轴、突然倒退或人群运动断裂。

## 4. 锁定的三张直接参考（3 / 5 cap）

### R1｜宁秋水 Character Reference Sheet
- ID：`AST_IMG_000060`
- 路径：`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256（已登记原始资产）：`15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- Git blob（2026-10-13 重新核对 MATCH）：`b674733242ab5d603dc42c53b8f7582003064499`
- 用途：脸型/年龄/发型/服装/身材全局一致性；不复制参考板构图。

### R2｜宁秋水 FACE_3Q_LEFT
- ID：`AST_IMG_000071`
- 路径：`production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256（已登记原始资产）：`8d92bcc601220654499f7be57fc83411c57dedccc44e8f764cc65ce1b840334e`
- Git blob（2026-10-13 重新核对 MATCH）：`31cfa62e27233b2a955e3201d5a88f96ad1dc6c3`
- 用途：可辨识的宁秋水 3/4 左侧脸/五官几何，不可变成正面证件照或完全面向镜头。

### R3｜Castle Entrance Inner Lobby Scene Master
- ID：`AST_IMG_000108`
- 路径：`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`
- SHA-256（已登记原始资产）：`f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3`
- Git blob（2026-10-13 重新核对 MATCH）：`91471e32dab1c7b51b7e718ffd539305d81daf85`
- 用途：同一古堡内门厅的空间/材质/光色权威；不得照抄空镜中心对称构图。

**直接参考总数 = 3**，不默默添加第四张或第五张。新 Bundle 要按 Manifest 再做正式 PNG bytes/SHA/Git blob 核验；今日回查证明仓库存在且 Git blob 与登记 MATCH，**不声称重新计算了 PNG SHA-256**。

## 5. 相邻批准图作为非直接参考

- N25：`production/image_library/approved/story_shots/N25_RAIN_DAY_RULE_NEIL_ANSWERS_WITHOUT_TURNING_APPROVED_V001.png`；Git blob `8e523285a832496f1e316fd20737293668cf18db`（本次回查 MATCH）。
- N26：`production/image_library/approved/story_shots/N26_LADYS_RULE_AND_FORWARD_MOTION_APPROVED_V001.png`；Git blob `a5ce429689a99437773385e25b9813745e380f74`（本次回查 MATCH）。

用途仅限导演/剪辑的真实机位、运动轴、服装、光色、角色动作前后连续审核。不能把 N26 进行裁切充当新增画面。若实景核对发现 3 张直接参考不能确保连续性，停止执行并提出具体的 Scene Reference 修订，不擅自变更 3 张已批准直接参考。

## 6. 最小验证与硬性 FAIL

**最关键假设：** 新机位宁秋水特写能够融入 N25→N26 的运动和视听节奏，并在“夫人的要求”处提供真正新的信息/情绪，而非仅切到同一个人的面孔。

**低成本验证顺序：**
1. 在 Bundle 设计阶段校核 N25/N26 实际画面行进轴、表情变化和光色；出现不可消解的跨轴/身份风险，则停下。
2. 一次 Bundle 正式构建和 exact-match 核验（需单独授权）后，Work 仅产出一张 PNG 候选供 PO 审核；不扩展多个备选。
3. 静帧批准之后，制作 N25 → 新反应插镜 → N26 的最短上下文 A/B，以批准的 S02-B V001 对应局部为对照，音轨保持连续。
4. PO 确认明显改善叙事和观感才算 **EDITORIAL TEST PASS**；否则 **FAIL / STOP**，不进一步批量制图、也不修改 S02-B 母版。

**硬 FAIL：** 宁秋水身份漂移、插袋、僵硬摆拍、夸张惊讶、背景空间虚假/漂移、增亮过度、脏噪/抠图感、N25/N26 运动轴错乱、门外景或全新大厅、实际台词与视觉错位；同源裁切不能冒充独立镜头。

## 7. 状态与下一 Gate

- `SCENE REFERENCE DESIGN V0.1 = PRODUCT OWNER APPROVED / LOCKED`
- `BUNDLE DESIGN = NEXT / NOT YET AUTHORIZED FOR BUILD`
- `WORK GENERATION = NOT AUTHORIZED`
- `S02_B_ASSEMBLY_V001 = APPROVED / CANONICAL / UNCHANGED`
- `N16–N17 V004 = APPROVED SEGMENT / UNCHANGED`
- `TAIL V001 / V002 = NOT APPROVED / ON HOLD`
- `P0.3 = IN PROGRESS`
- `VIDEO INDEX / STORY SHOT INDEX = UNCHANGED`
