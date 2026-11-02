# 《诡舍·黑衣夫人》｜P01-OPEN-01｜Product Owner 批准→原始JPEG正式发布→Story Shot登记→独立核验闭环

日期：2026-11-02
状态：**COMPLETE / PO APPROVED / ORIGINAL BINARY PRESERVED / STORY SHOT APPROVED CURRENT / REGISTRATION EXACT PASS**
范围：仅首镜 P01-OPEN-01 及其同图受控住宅 Scene Anchor。**不代表192.257秒Opening整片已通过**。

## 1. Product Owner审批事实

用户于2026-11-02发送图片「客厅中的危险抉择.jpeg」并明确：「批准这张图，按流程登记」。
此前 P01-OPEN-01 导演设计已获得PO授权；五张正式人物参考Bundle已由 Actions 41382711097 / Artifact 13113956992 校验通过。
PO实际批准的是**上传的原始图像本身**，不能把先前拟定的941×1672 PNG当成最终同一文件。

## 2. 原始图身份

- 用户原件：「客厅中的危险抉择.jpeg」；JPEG / RGB / **864×1536**（9:16）；**336,546 bytes**。
- 原始SHA-256：`4ccebb6a903b9cbeac1dfdc2e8b05c7f5dafa05e31cff53e775dfa2f37945452`。
- Git blob SHA-1：`9c5fc2d1d5bcc711a0be129fcc3e3229f039bf3a`。经GitHub `create_blob` 返回相同SHA；本地原件重算也一致。
- 原件经私有Drive上传作为临时交接中转，Drive ID：`16jYjBMtqJ8Dcgb5Fbqjwk2MX3aIFoMTO`；GitHub发布没有改变原始图像二进制。
- **规格差异：**原计划941×1672 PNG，实际为864×1536 JPEG。PO已批准所见图，故登记实际源格式尺寸，不擅自升级/PNG重编码；将来成片如需视频尺寸适配，只做明确标识的编辑派生，不修改Canonical原件。

## 3. Canonical Publication / Registry

- GitHub main 原始文件路径：`production/image_library/approved/story_shots/OPENING_P01_OPEN_01_THREE_PERSON_DECISION_ESTABLISH_APPROVED_V001.jpeg`
- Canonical + index + scene anchor + 3条 audit events + independent Actions workflow 一次提交 **80668e58fbef7f29ef20f76e81907c2894013796**；main推送通过。
- Story Shot Index：**35→36**，其中 `OPENING_P01_OPEN_01` **唯一1条、APPROVED / CURRENT**；第一画面对应已批准192.257秒原音绝对 `00:00.000`，具体台词级镜头出点待声画编辑锁定。
- 场景参考指针：`production/controlled_references/opening_p01_open01/OPENING_P01_OPEN_01_BAI_RESIDENCE_SCENE_ANCHOR_V001.manifest.json`
- Scene Anchor **复用同一原始JPEG**，用于P01私家住宅空间布局、家具、光照、人物站位连续性；不是另外生成的一张Scene Master，也不是自动批准所有服装变体。
- 正式审计事件：`EVT_20261102_OPENING_P01_OPEN01_A`、`_I`、`_R`；Audit Events **197→200**。Asset Registry **111**、Entity Registry **35**、Video Index **3** 不变。

## 4. 独立核验结果

- GitHub Actions：**Run 41386602412** — `Opening P01 Open01 Exact JPEG Registration`；触发commit `80668e58fbef7f29ef20f76e81907c2894013796`。
- Job **125088714109**：`completed / success`。
- 验证日志明确：`OPENING_P01_OPEN01_REGISTRATION_EXACT_PASS`。
- SHA-256与 Git Blob 双一致，JPEG帧头尺寸 **864×1536**，故事镜头索引数 **36**、单条唯一APPROVED/CURRENT、受控Scene Anchor、3条审计事件均PASS。
- 另行GitHub readback：main HEAD确认为同一发布commit；正式索引唯一且路径、scene manifest、SHA、Git tree中的原始文件blob及size全部匹配。
- 验证地址：https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41386602412

## 5. Gate 与后续边界

**已证明：**这张PO批准的864×1536 JPEG原始文件无字节变更正式入库，成功登记为第36张Approved/Current Story Shot，并作为**同图P01专用受控场景连续性参考**，GitHub Actions独立核验PASS。

**尚未证明：**此画面配合原声的实际播放节奏、人物脸与5个已批准身份图的自动像素级相似度、192.257秒整片视觉覆盖、后续P01镜头生产可行性，以及JPEG作为原PNG-only Reference Bundle Builder直接输入的兼容性。不能把PO审图视为自动跨镜头完整电影QC。

**下一步：**沿用户锁定的音轨开头顺序推进 P01 下一段君鹭远的决心反应镜（声音约00:04开始，实际词句切点仍须确认）。先复用本Scene Anchor，但由于当前 Bundle Builder V1只接纳PNG，应只针对**需要复用此JPEG作为正式输入**的实际任务解决最小兼容性问题；不得未经验证假装Bundle Builder已经能读JPEG。继续按照Director Design→Scene Reference→Bundle→Work→PO→Chat执行，每张候选须独立授权/审核。保留192.257秒原音、正式旧Opening及其它Story Shots和3视频不动。P0.3仍 IN PROGRESS。

**Project Control收口：**本文件只关闭当前P01-OPEN-01镜头登记事项，不把整个P0.3关闭；本地Mac同步保留2026-11-01既有已核验检查点，**今天没有Mac终端同步的证据**，不能把GitHub云端成功误写成Mac本地已同步。
