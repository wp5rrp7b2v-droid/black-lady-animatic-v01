# S3｜《黑衣夫人》有声小说转写

Canonical ID: `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

Status: `MVP1 SEARCHABLE INDEX COMPLETE / P0.1 BASELINE LOCKED`

Canonical file: `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv`

## 1. S3 的正式职责

S3 是 **machine-searchable source-audio index / transcript / verification layer**。

它负责回答：

- 原音频里实际说了什么；
- 是旁白还是对白；
- 谁在说；
- 内容大约位于 canonical source audio 的什么位置；
- 与 S2 哪一段文本对应；
- 当前验证等级是什么。

S3 **不是**：

- 动画节奏母版；
- 最终剪辑时间线；
- 预先切好的成片级 Audio Clip 库。

正式硬规则：

`SOURCE AUDIO TC ≠ FINAL EDIT TC`

## 2. Canonical audio baseline

- Audio Source ID：`AUDIO_MVP1_CANONICAL_V001`
- 文件：`AUDIO_MVP1_CANONICAL_V001.m4a`
- 时长：359.141995 sec
- AAC / 44.1kHz / 2ch
- SHA-256：`8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`
- 起点：`欢迎各位来到艾伦古堡`
- 终点：`而后又匆匆离去备餐`
- 映射范围：S2 第134章开头 → 第135章开头

## 3. 正式字段

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

其中：

- `speaker_type`：`NARRATION` / `DIALOGUE` / `OTHER`
- `speaker`：角色名、`NARRATOR` 或 `UNKNOWN`
- `text`：优先记录实际有声小说内容，不以 S2 直接覆盖声音事实
- `source_start_tc / source_end_tc`：S3 可使用近似 source TC；只有 VERIFIED 才能作为精确提取边界

## 4. 验证等级

### RAW_TRANSCRIPT

用于初始导航；文字、speaker、时间码允许存在误差。

### REVIEWED_TRANSCRIPT

已结合 S2、上下文和同步屏幕转写进行人工复核，足以用于机器检索和候选定位；source TC 可以是近似范围，**不得当作成片级精确切割边界**。

### VERIFIED_TRANSCRIPT

已直接听审 canonical audio，确认：

- 文字正确；
- speaker / speaker_type 正确；
- source TC 不吃字、不串句。

当前 `S3-MVP1-0001`–`0009` 已完成 VERIFIED 小样验证。

## 5. P0.1 最低完备标准｜LOCKED

P0.1 对 S3 的正式要求是：

1. 覆盖 `AUDIO_MVP1_CANONICAL_V001.m4a` 的完整 MVP1 内容范围；
2. 每个主要对白 / 旁白语义单元可通过 `text / speaker / speaker_type / approx source TC / source_text_ref` 被机器检索；
3. S3 可以把后续系统带到正确的原音候选区域；
4. 不要求在 P0.1 阶段把整个 359 秒音频逐句做到毫秒级精确切割；
5. 不要求全部 segment 升级为 VERIFIED；
6. 成片真正采用的声音，其自动定位、精确提取、handles、边界 QC 由 P0.3 `Audio Alignment / Resolver` 验证并承担。

当前 MVP1 searchable index 已完成，共 41 个 segment；其中 9 个为 VERIFIED，其余为 REVIEWED searchable entries。

## 6. 完整性抽查｜PASSED

已从开头、中段、后段进行检索抽查，均可唯一命中对应 S3 segment：

- `欢迎各位来到艾伦古堡` → `S3-MVP1-0001`
- `腰间空空如也` → `S3-MVP1-0006`
- `城堡大门只会在下雨天关闭` → `S3-MVP1-0020`
- `六幅` → `S3-MVP1-0027`
- `红色指甲油` → `S3-MVP1-0038`
- `匆匆离去备餐` → `S3-MVP1-0041`

结论：S3 已达到 P0.1 的机器可检索 source-audio index 要求。

## 7. 后续生产使用方法

正式生产流程：

`A1 / Story Beat / Shot Plan → Audio Alignment / Resolver → 检索 S3 → 定位 canonical audio → 自动提取带 handles 的 Audio Clip → Animatic / Edit Timeline → Final QC`

用户不承担常规“搜台词 / 找 source TC / 手工逐句切音”的工作。

人工只处理：低置信度匹配、歧义、边界异常、连续性问题和最终听审。
