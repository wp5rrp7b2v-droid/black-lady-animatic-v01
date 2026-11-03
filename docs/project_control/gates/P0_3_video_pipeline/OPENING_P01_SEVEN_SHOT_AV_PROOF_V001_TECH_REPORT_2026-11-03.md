# 《诡舍·黑衣夫人》｜Opening P01 七镜声画装配样片 V001 技术记录

日期：2026-11-03（Asia/Shanghai）

状态：**LOCAL TECHNICAL PASS / PRODUCT OWNER AUDIOVISUAL REVIEW PENDING / NOT A CANONICAL VIDEO / P0.3 IN PROGRESS**

## 1. 工作授权与边界

Product Owner 指令「进行声画装配」，在一次暂停后指令「继续工作」。本次只装配已批准且 GitHub 正式登记的 `OPENING_P01_OPEN_01` 至 `OPENING_P01_OPEN_07`，配合此前 PO 已听审通过的 192.257s Opening 原声**开头63.38秒**。不修改七张 Canonical 图片、源音或既有正式视频，不将视频登记为正式 Video，也不宣告 P0.3 PASS。

## 2. 输入与来源核验

- 原音：`OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a`，48kHz 双声道 AAC，原文件时长192.257秒，4,647,911 bytes。
- 原音 SHA-256：`1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`；本次下载并本地重算 PASS。
- 正式七镜：`production/image_library/approved/story_shots/OPENING_P01_OPEN_01...` 至 `OPENING_P01_OPEN_07...`，此前 Story Shot Registry 42条。
- GitHub Actions [41548552777](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41548552777) SUCCESS；`P01_SEVEN_EXACT_SOURCE_DELIVERY_PASS 7`，精确读取七个已批准 Git Blobs 并匹配 SHA-256、字节数、PNG尺寸/JPEG头后生成仅包含七张原图的打包 Artifact `P01_SEVEN_EXACT_ORIGINAL_IMAGES`，artifact ID `13190735101`。
- 下载 Artifact 并在本地逐一复算七张原始文件 SHA-256、尺寸及大小，一致；视频制作使用独立派生帧，不覆盖 Canonical 二进制。

## 3. 试剪 EDL （近似，未锁定逐句）

| 镜头 | 时间范围（秒） | 时长 |
|---|---|---:|
| P01-OPEN-01 | 0.00–4.00 | 4.00 |
| P01-OPEN-02 | 4.00–19.00 | 15.00 |
| P01-OPEN-03 | 19.00–32.00 | 13.00 |
| P01-OPEN-04 | 32.00–40.00 | 8.00 |
| P01-OPEN-05 | 40.00–48.00 | 8.00 |
| P01-OPEN-06 | 48.00–58.00 | 10.00 |
| P01-OPEN-07 | 58.00–63.38 | 5.38 |

时间来自 `OPENING_192257_AUDIO_VISUAL_CUE_SHEET_V001_2026-11-02.md`，属于导演级近似；63.38s是当前P02段预计接点，未获得逐字同步 PASS，不能视为最终锁定EDL。

## 4. 实际输出与本地技术核验

- 用户可审样片：`P01_SEVEN_SHOTS_AUDIOVISUAL_PROOF_V001.mp4`（当前仅由 Chat 会话文件交付，**没有公开上传至 GitHub**，其中含受版权保护的原声）。
- 画面：942×1672，24 fps，H.264 / yuv420p；1521帧。
- 声音：48 kHz 双声道 AAC，192 kbps，由已批原声开头裁切并经 AAC 编码；**派生音轨并非原 AAC 的 Exact Binary Copy**。
- 容器：MP4，63.380秒，3,825,692 bytes。
- 输出 SHA-256：`2234e13382674bf80959636fb067e59653159f689c4fca6554e7976bcc886fcc`。
- 原音和输出音频单声道解码信号相关系数 0.999781，最大相关对齐偏移0采样，支撑声源连续和无意外替换；不构成逐词画音匹配的证明。
- 七个抽检时点 1/10/25/36/44/53/60秒，画面与对应批准图片的视频派生帧一致；平均像素误差 1.13–1.22 (8-bit, H264损失编码)。
- `ffmpeg -v error -i OUTPUT -f null -` 全视频解码 PASS；未发现容器或解码错误。
- 首镜原JPEG 864×1536及其他PNG在视频中适配到统一942×1672画布。OPEN05原批准941×1671的尺寸差异仅在视频画布做填充；原Canonical从未被修改。
- 这版只做静态镜头硬切与原音配合，不宣称已经制作人物动画、逐帧动作、口型或镜头运动。

## 5. PO审片 Gate

**PASS（需Product Owner实际观看）：** 从00:00起完整叙事可理解；每段对应人物、位置和情绪自然；停留时长与切镜顺序合理；末句不被掐断且P01接P02可继续顺畅。

**FAIL：** 抽样Cue误配重要语句、镜头停留显著过长、镜头时间点切断句子、开头缺少叙事成立感或P01结尾突兀。若FAIL仅调整必要时间切点/过门；不修改正式静帧或重新制图，除非出现可指出的视觉事实问题。

下一步只等待 Product Owner 对这一个 63.38s 声画样片的审片意见。尚无PO全片批准或Video Index登记。Project State R411、Dashboard V330继续代表上一已审核登记的正式事实，暂不提升项目Gate。
