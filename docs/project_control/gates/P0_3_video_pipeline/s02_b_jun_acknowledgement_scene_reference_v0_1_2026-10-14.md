# S02-B｜君鹭远认可回应近景｜Scene Reference Design V0.1
Date: 2026-10-14
Target: `S02B_JUN_ACKNOWLEDGEMENT_TEST_01`
Status: SCENE REFERENCE DRAFT / PENDING PRODUCT OWNER REVIEW / NO WORK GENERATION
Parent design: `s02_b_jun_acknowledgement_director_design_v0_2_2026-10-14.md` — PO-approved direction.

## A. 镜头事实：来自已批准 V003 的实帧观察
- 原 N20 镜头内，宁秋水位于画面左侧，君鹭远位于右侧，两人由背面继续朝古堡内部行走。君鹭远是短发、浅蓝灰色外套，肩颈自然、没有背包。
- 约全片 35.933s 由 N20 切换到 N21 群体入堡画面。此切点来自现有剪辑；不代表旁白逐字时间码。
- N20 的批准 Story Shot 本身是 941×1672；N21 的批准 Story Shot 为 941×1671 且有 PO 尺寸例外。两个已批准 PNG 均不得因新镜头而重做、改变或改编出所谓新正片资产。
- 已批准 V003 基线包含 N16–N17 V004 以及尾部宁秋水 B V002。新增镜头不影响两处既有修改，也不改变 64.250 秒原声音频。

## B. Camera / Composition（导演设计意图，非已验证 3D 机位）
- Shot size: 君鹭远面部至上胸为主体的 **CLOSE-UP / MEDIUM CLOSE-UP**。人物头部及胸肩自然完整，不挤压头顶。
- Camera: 行进路线略前方斜侧机位，观察君鹭远的 **3/4 LEFT** 面部；选择符合既有角色资产的左 3/4 脸参考，避免机械重复 N20 背影视角。
- Jun: 略向前方/宁秋水方向看，**下巴微抬，嘴唇轻启、嘴角一丝自然笑意，眼神明亮坚定**。表情传达“听懂并接受提醒，准备继续入堡”，不画出正在讲话、明显低头点头、大幅仰颌、大笑或愤怒。
- Ning: 非必须出现。确需保留相邻人物关系时，只允许少量虚化肩背进入画面边缘，不准双人合影、人物对镜头。
- Depth: 君鹭远为唯一清晰视觉重点；后景内厅暖壁灯、石墙/木质构件逐级虚化，人与后景的景深和阴影自然融合。
- Spatial continuity: 与 N20 同处古堡入口内侧，并沿人群向内行进。门可以不入画；禁止通过窗/门新增大片室外蓝天或强自然光。
- Look: 低调阴暗、暖光克制、皮肤不发灰，眼部微小高光使其有神，但绝不整体提亮、橙色泛光、强棚拍灯或人像抠图硬边。
- Output candidate: 唯一 1× PNG，竖幅目标 941×1672（9:16 近似），保留原始生成输出供 PO 审核，不得在出图轮多张生成。

## C. 直接视觉参考选择：4 张（低于 5 张限制）
1. `N20_APPROVED_STORY_SHOT` (`N20`)：连续性主参照 — 同一队伍、君鹭远浅蓝灰衣着、N20 阴暗背景、身体方向。此图不要求复制 N20 的机位。
2. `AST_IMG_000057` / `CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET`：君鹭远身份与比例、服装家族锚定；**参考表排版不是镜头构图依据**。
3. `AST_IMG_000072` / `CHAR_JUN_LUYUAN_FACE_3Q_LEFT`：面部身份与侧前 3/4 五官参照，表情遵循 PO 本次修订要求，而非机械复制参考图原表情。
4. `AST_IMG_000108` / `SCENE_CASTLE_ENTRANCE_INNER_LOBBY`：同族阴暗古堡内厅建筑、有限壁灯暖光、空间材料参照；不强制复刻整个空镜或切换入另一大厅。

`N21` 仅作上/下游剪辑语境的视觉审查，**不作为第五张直接图**；如 N20/N21 实帧与上述 4 张参考的机位或服装显示明确冲突，应 STOP 并重新调整 Scene Reference，不自行追加来源。

## D. 可审核事实 vs 未证实判断
- FACT：GitHub main 已登记 N20、N21 批准原图及君鹭远角色资产；V003 原片抽帧显示背影走向和约 35.93s 切点。
- INFERENCE：将君鹭远的近景插入 N20 与 N21 可增强该叙事句的表情信息，需以片段试剪证明。
- WORKING HYPOTHESIS：侧前 3/4 左脸镜头与现有行进轴线兼容；没有实际 3D 轴线测绘，不能把“空间轴完全正确”标成 FACT。
- UNKNOWN：最自然的精确入点、画面保持长度，以及静态近景在完整剪辑中的最终观感。

## E. 最小验证与停止门
PASS（单图门）：身份/服装一致，微抬下巴、自然微张唇、轻微笑意与明亮坚定目光均读得出；眼部清晰但场景仍昏暗；人物融入背景，非合影/摆拍。
FAIL（单图门）：看起来像低头点头、讲话嘴型、过度夸张的正面大笑、身份漂移、强光或空间不合；仅重做必要局部，不继续批量制图。
PASS（剪辑门）：N20→新镜头→N21 以原声连续、总时长不变的局部 A/B 试映，PO 认可后再考虑 V004 完整审核版。

## F. 授权与发布边界
- 本文件与其 Bundle Spec 仅为 DESIGN。PO 未授权正式 Bundle Builder 执行、Work PNG、Story Shot Canonical、Video Index 或 main 合并。
- 必须先审定 Scene Reference 和 Bundle Design，然后提交 **Validation-only / build_authorized=false** 执行申请；后续正式构建、单 PNG Work 出图、PO 审核为分离 Gate。
- 本轮制图归属 Chat + GitHub Actions + Work，不切换 Codex。
