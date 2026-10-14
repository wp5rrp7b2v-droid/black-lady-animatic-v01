# 《诡舍·黑衣夫人》S02-B V006 NEW-02｜内厅人流侧向穿行｜Scene Reference Design V0.2

日期：2026-10-14

状态：**NEW-02 DESIGN READY / SOURCE PROVENANCE PRECHECK COMPLETE / EXACT VALIDATION PENDING / NO WORK PNG GENERATED**。
承接 `s02_b_v006_new02_crowd_interior_side_depth_scene_reference_v0_1_2026-10-14.md`；V0.2 明确摄影机责任、五份权威参考的准确登记类型及非生成边界。启动指令来自 PO「开始NEW-02｜人群内部侧向机位制作」。

## 1. 生产角色、镜头和时长

- Shot ID: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`。
- 作用：摄影机从古堡入口的人群侧边进入观众人眼高度的队伍内部，以**真实遮挡、前中后景及行进空间方向**使原本静态的镜头组产生电影感。
- V006 EDL 建议位置：N22 后、N23 前；frames `1299:1366`，30 fps，43.300–45.533 秒（**仅导演粗剪时段，不是逐字音频边界**）。
- 同一时段叙述：16 名诡客已进入古堡，男女各半；**单张图不承担画出全部16人的责任**。
- N21/N22/N23 都是已批准镜头，不允许改动原图、人物位置、视频母版；NEW-02 为一个真正独立机位，不是 N22 再裁切。

## 2. 机位及空间轴（最重要）

- 镜头在古堡入口内厅道路的侧边、**人群内部一臂距离**，摄影机高度略低于前一张 N22 的观察角度，有真实人眼旁观的人群临场感，不能是极低鱼眼、地面仰拍或舞台合影。
- 视觉方向与已批准 N21→N22→N23 的**人物实际行进方向**一致；镜头可斜向拍摄，但不得翻转门的左右空间轴，不得凭设计文本猜测已经建立的屏幕左右。由 Work 在直接读取 N21、N22、N23 实际像素后核对。
- 古堡正门保持开放；但本镜头**可以完全看不到门**，只要纵向空间仍然成立。门槛两侧均属古堡内部空间关系，画面不能误造露天门廊或第二个出口。
- 摄影机贴近人流：**近前景**一到两位匿名诡客的侧背/肩部自然经过且略失焦，占据画面局部，遮挡不是覆盖在人物上的 Photoshop 虚化层。
- **中景**三到四位诡客前后错位行走，步幅、转头和手臂动作不同步，不能并排站军姿、排队、正面看镜头。
- **远景**石拱、古堡走廊入口渐入深暗，真实可行走的石地面将人物连接成一个物理空间；不提早展示正式第一大厅全貌。
- 构图以纵深与自然人流占画面大部分，避免上半幅空墙、近景只有一个巨大的整面背影或强对称中央通道。

## 3. 角色与身份

- 本镜头主角是「**人流中的空间体验**」，不是尼尔/宁秋水/君鹭远的主角特写。
- 优先使用项目 Generic Guest A–J 的已批准服装和头身比例（约 7.5–7.8 头身）。匿名人物在不同景深下要有明显体型、发型和服装差异，不能克隆同一张人脸。
- 若镜头中出现来自 Generic Guest A–J 的可识别人物，其后侧轮廓与服装必须与 `REAR_3Q` 控制板一致；控制板不授权复制其排版、背景或位置。
- **不强制**宁秋水、君鹭远、尼尔露脸；若辨识不充分，宁君可完全不出现。避免连续性救援工作反而吞没这次的镜头语言价值。

## 4. 场景与光线

- 使用已批准 `SCENE_CASTLE_ENTRANCE_INNER_LOBBY` 作为空间、石墙、烛光基准。
- 阴冷压抑、低调暖烛光，减少橙色过亮地面反射，保留黑衣石墙细节。清晰度足够但不整体提亮；自然软化人物轮廓，避免“人物贴在背景上”。
- 不允许室外蓝天/大面积自然日光侵入，不允许人物单独棚拍强光。
- 不出现背包、挎包、行李、过度镜头畸变、重复克隆人物、同步列队。

## 5. 精确五张直接参考图（CURRENT APPROVED / SOURCE PROVENANCE PRECHECK）

1. `N21_COHORT_ENTERS_INSIDE_THE_FLOW_APPROVED_V001.png` — 承担从入口向内走的群体空间连续性；**注意其 PO 锁定 941×1671 特批尺寸，不得 resize**。
2. `N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png` — 诡客已有服装、体态和构图变化；这张图不能直接裁切当作 NEW-02。
3. `N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png` — 负责接续画面的空间轴、门边尼尔位置；NEW-02 不须复制其构图。
4. `AST_IMG_000108 | SCENE_CASTLE_ENTRANCE_INNER_LOBBY` — MASTER 场景：1448×1086。
5. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q` — **P0.3_CONTROLLED_PRODUCTION_REFERENCE / PRODUCT_OWNER_APPROVED**，依据 `production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.manifest.json` 的结构化控制登记（不是 P0.2 Asset Registry 常规记录）。

5 张 direct reference，固定输入上限为 **5/5**。正式 Bundle Spec 的每一张需要对照 Story Shot Index、Asset Registry 或 Controlled Reference Manifest，并在 GitHub Actions 上从 PNG 本体重新计算 SHA-256、Git blob、字节数和尺寸。

## 6. 拒绝/接受判据

**接受：** 近景真遮挡；中景人群自然错位；远景幽暗古堡纵深；场景轴成立；各角色与背景同一光源和透视；与 N22/N23 是真正不同的摄影机视角。

**拒绝：** 新画面仍像合影、人物排一列、假遮挡、对称站位、大量过曝橙光、门外蓝天涌入、重复/身份克隆、人物高锐度抠图感、背包行李、把 N22 放大/复制、尼尔成为突兀正面讲话特写。

## 7. 工序与权限

- 本轮启动：设计与 GitHub 结构化核验推进，**不得据此宣称 Work PNG 已生成**。
- 先创建 V001 **Validation-only Bundle Spec（`build_authorized=false`）**，GitHub Actions 验证 5/5 文件身份；Validation-only 不能创建正式 Artifact。
- 正式 Bundle build/artifact、Work 生成 1 PNG 941×1672、PO Candidate 审核、Exact Canonical Publication/Registration、V006 试剪、主仓 main merge，各自遵守独立授权及验证门槛。
- 单轮候选 PNG 恰好 **1 张，完成即停止**，不自行生成第二张。
