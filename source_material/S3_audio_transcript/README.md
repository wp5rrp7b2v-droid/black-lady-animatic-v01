# S3｜《黑衣夫人》有声小说转写

Canonical ID: `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

Status: `STRUCTURE TO ESTABLISH / AUDIO SOURCE LOCKED`

Initial production scope: `MVP1 canonical audiobook span`

MVP1 正式故事从 S2 第134章《【黑衣夫人】参观》开头开始；第133章只作为前置语境，不进入 MVP1 正式成片。

重要：MVP1 不定义为 `S2 Chapter 134 only`。

有声小说的分集/叙事进度与原文章节边界并不完全一致。第一版 S3 必须覆盖 `AUDIO_MVP1_CANONICAL_V001.m4a` 的完整连续跨度，而不是按原文章节标题强行截断。

当前 canonical audio baseline：

- Audio Source ID：`AUDIO_MVP1_CANONICAL_V001`
- 文件：`AUDIO_MVP1_CANONICAL_V001.m4a`
- 上游 RAW_CAPTURE：`ScreenRecording_09-12-2026 13-40-39_1.MP4`
- 上游 RAW_AUDIO_EXTRACT：`AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`
- 有声小说集数：`097【黑衣夫人】主人`
- 提取/裁切方式：原 AAC 音轨 stream copy / 无重编码
- 编码：AAC / 44.1kHz / 2ch
- 时长：359.141995 sec
- 大小：4,957,338 bytes
- SHA-256：`8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`
- 起点内容锚点：`欢迎各位来到艾伦古堡`
- 终点内容锚点：`而后又匆匆离去备餐`
- 状态：`CANONICAL / LOCKED / PRODUCT OWNER QC PASSED`

正式建立后的 S3 必须区分：

- `RAW_TRANSCRIPT`
- `REVIEWED_TRANSCRIPT`
- `VERIFIED_TRANSCRIPT`

每个 S3 segment 至少应绑定：

- `segment_id`
- `audio_source_id`
- `start_tc`
- `end_tc`
- `speaker_type`
- `speaker`
- `text`
- `verification_status`
- `notes`

P0.1-05B 当前任务是正式锁定字段定义、segment 拆分规则和状态升级条件；P0.1-05C 再用真实音频小样验证从原音到 `VERIFIED_TRANSCRIPT` 的方法。

精确剪辑边界仍以 `AUDIO_MVP1_CANONICAL_V001.m4a` 本身为最终事实依据；S3 用于内容定位、说话顺序、对白/旁白识别与校验，不得替代真实音频边界判断。

历史 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 仍为 `NON-CANONICAL TEST AUDIO`，不属于 MVP1 canonical audio baseline。
