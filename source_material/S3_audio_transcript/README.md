# S3｜《黑衣夫人》有声小说转写

Canonical ID: `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

Status: `STRUCTURE LOCKED / SAMPLE VALIDATION NEXT`

Initial production scope: `MVP1 canonical audiobook span`

MVP1 正式故事从 S2 第134章《【黑衣夫人】参观》开头开始；第133章只作为前置语境，不进入 MVP1 正式成片。

重要：MVP1 不定义为 `S2 Chapter 134 only`。

有声小说的分集/叙事进度与原文章节边界并不完全一致。第一版 S3 必须覆盖 `AUDIO_MVP1_CANONICAL_V001.m4a` 的完整连续跨度，而不是按原文章节标题强行截断。

## 1. S3 的职责

S3 是“原音素材索引 / 转写 / 校验层”，不是动画时间轴。

S3 只负责回答：

- 原音频里实际说了什么；
- 是旁白还是对白；
- 谁在说；
- 这段原音在 canonical source audio 的什么位置；
- 该段是否已经人工验证到可可靠提取。

S3 不负责决定：

- 镜头何时开始或结束；
- 动画节奏；
- 镜头时长；
- 画面停顿；
- 转场；
- 某句原音在最终成片中的出现时间。

正式硬规则：

`SOURCE AUDIO TC ≠ FINAL EDIT TC`

原音频只是后续动画的配音 / 旁白素材来源，不是动画节奏母版。最终画面节奏与声音编排由后续 `A1 ADAPTATION_SCRIPT` 与 `Animatic / Edit Timeline` 决定。

## 2. Canonical audio baseline

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

## 3. 正式字段

Canonical file：`S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv`

字段固定为：

1. `segment_id`
2. `audio_source_id`
3. `source_start_tc`
4. `source_end_tc`
5. `speaker_type`
6. `speaker`
7. `text`
8. `source_text_ref`
9. `verification_status`
10. `notes`

字段定义：

- `segment_id`：唯一段落编号，例如 `S3-MVP1-0001`。
- `audio_source_id`：第一版固定为 `AUDIO_MVP1_CANONICAL_V001`。
- `source_start_tc` / `source_end_tc`：相对于 canonical source audio `00:00:00.000` 的素材定位时间码；只代表原素材位置，不代表最终成片时间码。
- `speaker_type`：仅允许 `NARRATION` / `DIALOGUE` / `OTHER`。
- `speaker`：如 `NARRATOR`、`尼尔`、`宁秋水`；无法确认时使用 `UNKNOWN`。
- `text`：实际有声小说中听到的内容，不直接复制原著文本。
- `source_text_ref`：用于映射 S2，例如 `S2-CH134`、`S2-CH135`。
- `verification_status`：`RAW_TRANSCRIPT` / `REVIEWED_TRANSCRIPT` / `VERIFIED_TRANSCRIPT`。
- `notes`：记录原著差异、听辨疑点、背景声、边界问题等。

## 4. Segment 拆分规则

Segment 定义为：最小可独立定位、独立审核、独立提取的完整语义单元。

强制拆分：

- 说话者变化；
- `NARRATION ↔ DIALOGUE` 变化；
- 明显叙事段落变化。

一般规则：

- 不按固定 5 秒 / 10 秒机械切割；
- 不在一句话中间拆段；
- 同一说话者连续极短句、无明显停顿时可以合并；
- 同一旁白连续过长时，可在完整句末拆分；一般建议单段不超过约 10–15 秒，但以语义完整性优先。

## 5. 验证等级

### RAW_TRANSCRIPT

初始自动或人工粗转写。

允许：

- 文字错误；
- speaker 错误；
- 时间码近似。

用途：内容导航与初步定位。

不得视为正式提取边界。

### REVIEWED_TRANSCRIPT

已对照 S2 与上下文人工检查：

- 文字；
- speaker；
- `NARRATION / DIALOGUE` 类型；
- 明显识别错误。

但尚未逐段直接听音确认 source TC 边界。

### VERIFIED_TRANSCRIPT

已直接对照 `AUDIO_MVP1_CANONICAL_V001.m4a` 逐段确认：

- 实际音频文字正确；
- speaker 正确；
- speaker_type 正确；
- `source_start_tc / source_end_tc` 不截字、不串句、不吃掉对白。

只有 `VERIFIED_TRANSCRIPT` 才能作为可靠的“原音提取索引”。

即使达到 VERIFIED，它也仍然不是最终动画时间轴。

## 6. S2 与 S3 的冲突规则

S2 只能辅助校对 S3，不能覆盖真实有声小说。

如果 S2 写 A，而有声小说实际说 B：

- S3 `text` 必须记录 B；
- 差异写入 `notes`；
- 精确声音事实以 canonical audio 为最终依据。

## 7. 与后续动画制作的关系

三层职责正式分离：

1. `S3`：原音素材定位与验证。
2. `A1 ADAPTATION_SCRIPT`：决定成片保留、删除、重组哪些内容。
3. `Animatic / Edit Timeline`：决定镜头节奏、画面时长、停顿、转场，以及选中的原音在最终成片中的摆放位置。

允许：

- 画面先于对白出现；
- 对白跨镜头持续；
- 对白结束后画面继续停留；
- 为镜头节奏加入无对白画面时间；
- 将源音频中的相邻片段在最终时间线上重新编排，只要不违背 A1 和声音连续性要求。

不允许：

- 改变原音语速来迁就镜头时长；
- 把 source TC 直接当作 final edit TC；
- 因 S3 时间轴顺序而自动决定镜头节奏。

## 8. P0.1-05C 小样验证标准

下一步不直接转写整个 MVP1。

先选择约 20–40 秒真实 canonical audio 小样，且小样必须包含一次或多次：

- `DIALOGUE → NARRATION → DIALOGUE`；或
- `NARRATION → DIALOGUE → NARRATION`。

目标是验证历史失败点：

- 不把旁白误当对白；
- 不把对白截断；
- source TC 可准确回切到完整原音。

P0.1-05C 的通过链：

`RAW → REVIEWED → VERIFIED → 按 VERIFIED source TC 回切原音 → 听感无截字 / 串句`

小样验证成功后，才扩展到整个 MVP1。

## 9. 当前状态

- P0.1-05A：COMPLETE。
- P0.1-05B：COMPLETE / STRUCTURE LOCKED。
- P0.1-05C：NEXT / SAMPLE VALIDATION。

历史 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 仍为 `NON-CANONICAL TEST AUDIO`，不属于 MVP1 canonical audio baseline。
