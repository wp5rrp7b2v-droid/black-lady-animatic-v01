# 《诡舍·黑衣夫人》｜NEW-02 环境动态 M01+M03 单镜头测试 V001｜Technical Closeout

日期：2026-10-14

**状态：技术制作成功 + 独立二进制核验 PASS / PO 视频视觉审核待完成 / 非正式视频母版 / 未合并 main**

## 上游 Product Owner 决定

用户在审阅 N23 烛光 Stage A 自然度通过后，批准建立 `ENVIRONMENT_DYNAMIC_ENHANCEMENT_FRAMEWORK_V001`，并授权使用 NEW-02 进行第二个环境动态测试：仅 **M01 受控烛光 + M03 极轻浮尘**，不做人物动作，不重做原始 Story Shot，不修改 V006 候选。

## Framework 完成

- `docs/project_control/gates/P0_3_video_pipeline/ENVIRONMENT_DYNAMIC_ENHANCEMENT_FRAMEWORK_V001.md`
- `production/environment_dynamic/module_registry_v001.json`：M01/N23 已获 PO 视觉效果认可；M02/M04/M05 仍为设计阶段；M03 仅本轮待 PO 审核试验。
- `production/environment_dynamic/shot_profiles/NEW02_M01_M03_TEST_V001.json`：逐镜头、只读原图身份、归一化建筑区域遮罩、受控强度和颗粒配置。
- `scripts/environment_dynamic_render_v001.py`：可复用 Python Pillow+NumPy+FFmpeg 环境动态渲染器，独立数据配置，非付费 AI 视频工具。
- `.github/workflows/new02-environment-motion-m01-m03-test-v001.yml`：恰好一条 MP4 云端制图。
- `.github/workflows/new02-environment-motion-independent-verify-v001.yml`：独立核验工作流。
- **未批量处理其他 Story Shot**。

## 唯一生成的 NEW-02 环境动态候选

- 原始已批准 PNG：`production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png`
- 941×1672 / 1,963,410 bytes。
- 原始 SHA-256：`d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`
- 原始 Git blob：`d8feba3692ebe25afd0e51f5e3ab32358ea19ded`
- 唯一测试 MP4：`production/environment_dynamic/review_candidates/NEW02_M01_M03_TEST_V001/NEW02_M01_M03_ENVIRONMENT_MOTION_TEST_V001.mp4`
- 参数与机器证据：`production/environment_dynamic/review_candidates/NEW02_M01_M03_TEST_V001/NEW02_M01_M03_ENVIRONMENT_MOTION_TEST_V001_EVIDENCE.json`
- 4.000 秒，720×1280，30 fps，120 帧，无音频、无人物动作、摄影机不动。
- MP4 SHA-256：**`bc4fd4f87100c0bcae8ab72b21d671ad44ca2de7e49ded6afca17ed06926f05d`**。
- MP4 Git blob SHA-1：**`0e6388626b14758bfbbdc284a77b571dbd052003`**。
- MP4 bytes：**242,703**。
- 编码前 Raw RGB：局部授权环境区以外**0 像素修改**，最大通道差 **11/255**；首帧和末帧均恢复到未叠加环境特效的基础图；授权动态区域占画面 10.43%，本轮浮尘 13 粒。
- **重要限制：** 非授权区域 RAW RGB 精确不变，是渲染脚本单独计算并输出到测试证据，H.264 压缩后不保证逐像素无损；独立 verifier 复核证据与原始 MP4 / 原图，但**不额外重建 raw 帧作逐像素二次计算**。不夸大核验范围。
- 人物与衣料真实动作**未制作**，浮尘和烛光只应在后续由 PO 观看评定是否自然。

## GitHub Actions 验证

- 构建 / 验证原图并渲染：Run **`38582338284`** SUCCESS，源图 SHA、Git blob、字节数、尺寸匹配。
- 构建完成时只提交该新 MP4 和其 QC evidence JSON 至审核分支；源 Story Shot 不动。
- 单独 Exact Independent Verification Run **`38582805861`** SUCCESS。
- 独立证据 Artifact **`11903542606`**（`NEW02_ENVIRONMENT_M01_M03_EXACT_EVIDENCE_V001`）。
- Artifact SHA-256：`e367989e0472f75e7170f0c2c9655190fb058413f55cb162ca4ed68b756af24e`。
- 复核项：源 PNG SHA、Git blob/大小/尺寸；批准镜头；MP4 SHA、Git blob、字节数；120 帧 / 30fps / H264 / 无音轨；全片解码；用户审核权限；动态配置与证据一致；候选原始提交只有两个新增路径；V006 候选 MP4 Git blob `d92d23ac6b5a542e07572e29a9e648e2c4141854` 仍不变，正式 `production/video/video_index.jsonl` Git blob `84fb0f70ebd92536b95c6b01c6ac69a27a6986c7` 不变；main 未合并。

## 本轮状态和下一门槛

**Framework V001 已建立；NEW-02 唯一 M01+M03 技术样片通过核验并保存到 GitHub review branch；PO 视觉判断待完成。**

请 PO 观看整个 4 秒镜头，判断是否太淡、浮尘是否自然、烛光变化是否如 N23 一样不破坏压抑基调。没有 PO 独立视觉通过，不把 M03 模块状态升级到 APPROVED 或应用到其他镜头。严禁因候选技术 PASS 而自动修改 V006 粗剪候选或正式母版。
