# 《诡舍·黑衣夫人》｜Opening 新人物 Master Reference V001｜导演设计草案

Date: 2026-11-01  
Status: **DRAFT / SOURCE FACTS CHECKED / ROLE-TIER AND APPEARANCE AWAIT PO APPROVAL / NO IMAGE OUTPUT OR FORMAL REGISTRY**

## 1. 工作目标及冻结边界

围绕 PO 已通过完整原声审听的 Opening P01→P04→Neil `192.257s` 版本，**在 P01/P02 新镜头分镜之前**建立白潇潇与孟军两名未登记角色的可复用人物 Master Reference。目标是让各视角人物身份与服装稳定，而不是提前制作剧情镜头。

正式声源：私有 Drive `1xFkf3sC20yWVt_a3SJy9OrJ6KpWJ8bTV`，SHA-256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`；既有 PO 审批记录 `OPENING_COMPACT_AUDIO_V001_PO_LISTENING_APPROVAL_2026-11-01.md`。声音基准不作修改。P03-A/B/C 已批准的图像、Opening V001、Story Shot Index35、Video Index3 不变。

## 2. 原著事实与 Registry 缺口（FACT）

- 源文：`source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt` 第133章。
- 经独立读取 `production/asset_registry/entity_registry.jsonl` 与 `production/asset_registry/asset_registry.jsonl`，目前 **没有** `CHAR_BAI_XIAOXIAO`、`CHAR_MENG_JUN` 的正式实体或 CURRENT/APPROVED 资产；因此 **NOT PRODUCTION_READY**。不得因为建立草案就在两份正式 Registry 插入角色或占用 Asset ID。
- 白潇潇（女）：在自己住处向君鹭远交代试炼的残酷性、需要诡舍老人陪同，关心他的安危；喝气泡水；询问宁秋水是否想好；叮嘱「活着回来」。她不是签约人，也不是血门中的怪物。
- 孟军（男）：在诡舍大厅独自喝酒、看肥皂剧，态度冷淡；带宁秋水和君鹭远到三楼；**让君鹭远**伸手，用刀划开其手掌，再把君鹭远的手按/贴向木门；契约后说明身体恢复规则。不能误画为孟军或宁秋水本人签约。
- 原著本章没有提供两人的**精确年龄、身高、脸型、发色、发型、具体服装款式/颜色**。因此以下外形皆为导演候选，不冒称原著事实。

## 3. 工作假设（需 PO 审核）

根据 `character_asset_rules_v1.md` 的锁定分级，本轮两名角色暂按 **Tier B 候选**设计：白潇潇在 P01 参与多轮对话，孟军在 P02 同时需要对话与手部操作，存在中近景、多机位、身份一致性要求。Tier B 不是当前 Registry 中已批准的正式分级，待 PO 确认后才可登记。若后续实测显示仅极少机位，允许依锁定规则复核为 Tier C（3-view）减少制作量；不得为追求九视图而擅自升级 Tier A。

Tier B 正式 Mandatory Set 每人6张 Atomic Views：
`FACE_FRONT` / `FACE_3Q_PRIMARY` / `PROFILE_PRIMARY` / `REAR_3Q_PRIMARY` / `BODY_FRONT` / `BODY_BACK`。 
`primary_side` 候选设为 `RIGHT`（仅为消除左右角色混乱的工作选择，未经 PO 批准）。完整 Atomic Set 通过后再派生至少1张 Character Reference Sheet，包含 `derived_from` 列表，不把拼图 Sheet 当作原子资产。各张主参考为 **9:16**，中性背景、自然站姿/眼平摄影、稳定中性光线，符合锁定的角色审核顺序。

## 4. 可供讨论的人物视觉方向：非原著定论

### 白潇潇 / CHAR_BAI_XIAOXIAO / P01
- 叙事职责：理性说明危险、审慎保护君鹭远，同时尊重其个人选择。
- 建议视觉年龄感：**30岁上下成年女性**（工作假设，非原著指定）。
- 身份轮廓候选：清爽利落、成熟但不过度严厉；深色中长发或简洁束发；五官自然、有辨识度；不画成青春少女/贵妇/恐怖人物。
- 日常默认服装候选：现代简约生活装，低饱和灰蓝、暖灰、米灰等，避免欧洲古堡年代戏装扮；对话情绪由剧情镜头表达，不写死为 Character Master 的「担忧」表情。
- **重要边界：** 气泡水瓶属于该场剧情临时道具，不绑定到 FACE/BODY 主参考；其准确外形若需特写，之后另建小型 Prop reference，不额外制作与当前 blocker 无关的资产。

### 孟军 / CHAR_MENG_JUN / P02
- 叙事职责：诡舍内熟练处理血门契约的人；冷淡、克制，未呈现夸张凶恶或宗教身份。
- 建议视觉年龄感：**35–45岁成年男性**（工作假设，非原著指定）。
- 身份轮廓候选：短发、冷静克制、面容线条较硬朗；体态正常而稳，不设计成执刀杀手、古堡管家或鬼怪。
- 默认服装候选：深灰/炭黑等低饱和现代常服，避免与已经批准的尼尔管家制服产生角色混淆；无额外武器作为默认人物识别特征。
- **重要边界：** 划掌的刀与人物手部操作是 **P02 的剧情特定 Prop/Conditional Reference**，不是永久 Character Atomic Master。不得让主参考出现流血、腐烂手臂、阴暗舞台光或反复变化的服装。

## 5. 最低成本验证与扩产 Gate

**Phase 0 — 身份 Seed（本文件讨论，不等于已授权制图）**
- 每角色只拟 1 张 `FACE_FRONT` 身份锚定候选，分别由受验证输入的 Bundle 交 Work 出图。
- 要求：9:16、原著一致、清晰、与现有宁秋水、君鹭远及尼尔有可辨别差异、无额外剧情、可作为长期固定身份。
- PASS：PO 视觉确认「这就是该角色」，可开始相同身份的完整 Tier B Atomic Set；FAIL：只调整该角色的身份 Seed，不批量制作其他角度。

**Phase 1 — Tier Core Set**
- 采用相同 Approved Seed 锁定脸部结构、发型、基础服装和身形，完成余下5张/角色（若 Tier B 获 PO 确认），优先角色需求的同侧3/4与全身，再完成侧面、后3/4、背面。
- PASS：每张符合锁定的七项 Fixed Standard Review、角色跨角度一致、六个必需角色视角完整、每张 PO 批准。
- FAIL：任一视角改变脸型/体态/服装、9:16不合规或 identity 漂移，退回受影响的视角，不撤销已通过的 Seed。

**Phase 2 — Formal Ingest**
- 只有 PO 批准对应原子图后才 Exact Binary Verification、正式 Entity/Asset Registry、Atomic Source 发布及 Dependency Sheet 构建/登记。
- 再以 Resolver 测试一次 P01/P02 中预期所需的代表性人脸与全身角度，未达 `PRODUCTION_READY` 不进入 Work 正式 Story Shot 制图。
- 任何后续新增的表现型动作/表情图都必须由真实镜头需要触发，不在本轮盲目生成。

## 6. 当前审批问题与停止条件

- 待 PO 批准：两人身份确认、Tier B 方案与默认外形方向；两人的 `primary_side` 是否采用 `RIGHT`。
- 当前只授权内容设计和事实核查；没有 Work 制图、Asset Registry 登记、Story Shot、视频或更改音频的授权。
- 已确认本轮前置最小 blocker：两名人物没有经过 PO 审核的身份 Seed。先按 Phase 0 逐人检验，可最快淘汰错误视觉方向；Seed 未 PASS 不做12张正式角色图，也不新建其他管理文件。
- 与此前会话提出的「每人多视图+表情」概念相比，本次经 GitHub 锁定规则核对，标准化为 **Tier B 6-view + 可追溯 Sheet**；剧情表情与手部变体不属于强制 Core Set，不提前批量制作。
