# S3｜《黑衣夫人》有声小说转写

Canonical ID: `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

Status: `NOT ESTABLISHED`

Initial production scope: `MVP1 actual audiobook span`

MVP1 正式故事从 S2 第134章《【黑衣夫人】参观》开头开始；第133章只作为前置语境，不进入 MVP1 正式成片。

重要：MVP1 不再定义为 `S2 Chapter 134 only`。

有声小说的分集/叙事进度与原文章节边界并不完全一致。Product Owner 提供的 MVP1 录屏从第134章开头开始，并连续进入第135章开头。因此第一版 S3 必须覆盖“实际 MVP1 canonical audio 的完整连续跨度”，而不是按原文章节标题强行截断。

当前已接收并核验：

- RAW_CAPTURE：`ScreenRecording_09-12-2026 13-40-39_1.MP4`
- 有声小说集数：`097【黑衣夫人】主人`
- 录屏时长：381.958333 sec
- RAW_CAPTURE SHA-256：`9bab514775f0771987b094cdd9394b81d6a49a7bace995ef9ad4dbcce448abd1`
- RAW_AUDIO_EXTRACT：`AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`
- 提取方式：原 AAC 音轨 stream copy / 无重编码
- RAW_AUDIO_EXTRACT：AAC / 44.1kHz / 2ch / 381.941995 sec / 5,244,616 bytes
- RAW_AUDIO_EXTRACT SHA-256：`d9a297b275a2fc42b85fa7b26407c4824c17efc63d1b9d148470f224d96be7f2`
- 当前状态：`RAW_AUDIO_EXTRACT / CANONICAL CANDIDATE`
- 内容映射：S2 第134章开头 → 第135章开头；精确终止时间码尚待锁定

正式建立后 S3 必须区分：

- `RAW_TRANSCRIPT`
- `REVIEWED_TRANSCRIPT`
- `VERIFIED_TRANSCRIPT`

每个 S3 segment 至少应绑定：`audio_source_id`、`start_tc`、`end_tc`、`speaker_type`、`speaker`、`text`、`verification_status`。

精确剪辑边界仍以 canonical audio 本身为最终事实依据；S3 用于内容定位、说话顺序、对白/旁白识别与校验，不得替代真实音频边界判断。

历史 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 仍为 `NON-CANONICAL TEST AUDIO`，不属于 MVP1 canonical audio baseline。
