# Opening｜第133章音源收录与独立归档验证｜2026-10-28

状态：**SOURCE CAPTURE + AUDIO DERIVED ARCHIVE VERIFICATION PASS** / **NARRATION TIMECODES NOT YET LOCKED** / **ORIGINAL OPENING V001 LOCKED**

## 1. 定位与读取

用户于 2026-10-28 上传至 Drive `Black Lady Project` 根目录：
- 文件：`ScreenRecording_10-28-2026 13-25-34_1.mp4`
- 根目录临时 ID：`1D_kH7mLEM54qFEVpY3tpa-Z29Eo3iZLx`
- 字节：62,331,202，SHA-256：`4d60d1835a7cc4160c580501e5d4c419d74beaf7121f28fe0357122e583d07e8`
- 实测 ffprobe：290.720 秒；HEVC 1284×2778；AAC 44.1 kHz 双声道。
- 截帧视觉核对：有声小说第096集《契约》，录屏画面覆盖人物/契约及血门任务和提示相关段落。**尚未逐句听审确认各句音频准确时间码**，不将可视文本直接视为逐句有声对齐 PASS。

## 2. 已完成永久归档：Google Drive 私有项目 06_Audio

| 资产 | 文件 | Drive ID | 字节 | SHA-256 |
|---|---|---|---:|---|
| 原样备份视频 | `CH133_ORIGINAL_CAPTURE_20261028_SOURCE_LOCKED_V001.mp4` | `115KUWFR2JaABxUllTGKn7NfQbuhmwRyF` | 62331202 | `4d60d1835a7cc4160c580501e5d4c419d74beaf7121f28fe0357122e583d07e8` |
| 无重编码提取音轨 | `CH133_AUDIO_SOURCE_UNTRIMMED_V001.m4a` | `1hl9XNYZ5s0hk-VEjyKk7eyPrguY8zdEK` | 3994021 | `26d41ab241228f0de10531ceb6e67129f530a25589aa89a4c3417b884b7b9b20` |

私有文件路径：`Black Lady Project/06_Audio/`，父文件夹 ID：`1yzcpckOoogFznfiQdPDLKxhzIG6PoQx4`。

原样视频复制后重新从 Drive 下载：字节数和原始根目录来源 SHA-256 **完全一致**。音轨 `ffmpeg -map 0:a:0 -c:a copy` 无重编码提取并上传到 Drive；重新从 Drive 下载：字节数和提取源 SHA-256 **完全一致**。

原视频的 AAC compressed stream SHA-256：`c47863e262d308b9a3ec3ef917bea2b6e306648272f14cff12dd7c525ebe20c4`。
本地音轨及 Drive 回读音轨压缩流 SHA-256：`c47863e262d308b9a3ec3ef917bea2b6e306648272f14cff12dd7c525ebe20c4`，**字节流一致**，全音频 FFmpeg 解码无错误。

- <https://drive.google.com/file/d/115KUWFR2JaABxUllTGKn7NfQbuhmwRyF/view>（原样备份）
- <https://drive.google.com/file/d/1hl9XNYZ5s0hk-VEjyKk7eyPrguY8zdEK/view>（正式输入候选音轨）

## 3. 版权、权限及 Source of Truth

正式仓库为公开 GitHub，**没有把可能受版权保护的完整有声小说或录屏二进制公开上传**。GitHub 保存来源/校验/审批状态；原媒体及提取音频存于独立私有 Google Drive 06_Audio。此分层存储不会导致重传、且保留恢复能力。

机器清单：`production/audio_sources/CH133_AUDIO_SOURCE_UNTRIMMED_V001_MANIFEST.json`。

## 4. 删除前确认

**可以由用户自行删除根目录原始临时文件（ID `1D_kH7mLEM54qFEVpY3tpa-Z29Eo3iZLx`）**：因为 06_Audio 已有 SHA-256 一致的独立原样 MP4 备份和提取 M4A。**不要删除 `06_Audio` 内的两份归档文件**。本轮没有删除任何 Drive 文件。

## 5. 仍需验证的后续制作 Gate

1. 按第133章正式文字定位实际音频 P01 人物选择、P02 契约代价、P03 五日钥匙任务、P04 两个警示的朗读句子及时间码，不能凭截图当成已对齐。
2. 只在真实朗读音质与内容验证通过后规划最小 8–13 秒的声画 proof；每条镜头仍按 Chat → GitHub Actions → Work → PO → Chat 正式制作流程。
3. 本轮不授权新图片/视频、不改变 P0.1 原音或正式 Opening、Story Shot Index 32、Video Index 3，血门木门仍暂停。

**本轮实际证明：来源文件可完整读取；提取音轨与原录屏 AAC 完全一致，两个私有归档文件 SHA 回读通过。尚未证明：第133章逐句剪辑点、试片节奏与视觉效果。**
