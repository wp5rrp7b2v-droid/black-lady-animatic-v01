# P0.1-02｜现有源数据盘点

- 项目：BLACK-LADY-001｜《诡舍·黑衣夫人》
- 日期：2026-09-12
- Gate：P0.1｜故事与文本数据基线
- 状态：INVENTORY COMPLETE / BASELINE BUILDING

## 1. 源数据命名

- S1：`S1_SOURCE_NOVEL_FULL_V001.txt`
- S2：`S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
- S3：`S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

## 2. 盘点结果

| Source | 目标职责 | 当前证据 | 当前状态 | 结论 |
|---|---|---|---|---|
| S1 `S1_SOURCE_NOVEL_FULL_V001.txt` | 完整《诡舍》世界观、人物、跨篇章上下文检索 | Product Owner 于 2026-09-12 指定当前上传 `诡舍.txt` 为完整原文；UTF-8 plain text；6,480,028 bytes；第1章至第1002章结局；SHA-256=`f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e` | CANONICAL / LOCKED | P0.1-04 COMPLETE；S1 作为系列级最高原著事实源 |
| S2 `S2_SOURCE_BLACK_LADY_TEXT_V001.txt` | 《黑衣夫人》篇章原著工作文本 | Product Owner 于 2026-09-12 指定当前上传文本为唯一 canonical source；第133–164章；UTF-8 plain text；SHA-256=`159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6` | CANONICAL / LOCKED | P0.1-03 COMPLETE；其他同名/近似文本均为 NON-CANONICAL |
| MVP1 Scope | 第一个正式成片范围 | Product Owner 已锁定起点并提供实际有声小说录屏 | LOCKED START / END MAPPING IN PROGRESS | 从 S2 第134章《【黑衣夫人】参观》开头开始；实际音频连续进入第135章开头，终点按有声小说音频边界锁定，不按原文章节硬切 |
| MVP1 RAW_CAPTURE `ScreenRecording_09-12-2026 13-40-39_1.MP4` | MVP1 原音来源证据 | 235,987,834 bytes；381.958333 sec；AAC 2ch 44.1kHz + H.264；SHA-256=`9bab514775f0771987b094cdd9394b81d6a49a7bace995ef9ad4dbcce448abd1`；画面确认第097集【黑衣夫人】主人 | RAW CAPTURE / VERIFIED IDENTITY | 对应有声小说约00:00–06:20；起点映射第134章开头，后段映射第135章开头 |
| MVP1 RAW_AUDIO_EXTRACT `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a` | 从 RAW_CAPTURE 无重编码抽取的音频工作源 | 5,244,616 bytes；381.941995 sec；AAC 2ch 44.1kHz；SHA-256=`d9a297b275a2fc42b85fa7b26407c4824c17efc63d1b9d148470f224d96be7f2` | RAW_AUDIO_EXTRACT / CANONICAL CANDIDATE | 已验证可作为 canonical audio 的直接候选；仍需去除录屏起止冗余并锁定精确内容边界 |
| 历史测试音频 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` | 过去 Animatic / 音频实验 | 2,636,183 bytes；195.844989 sec；AAC 2ch 44.1kHz；SHA-256=`abaaab1c0c8362e6d61268ba09b0f0ce6cb915cf49c046fd3b32c49405746551` | NON-CANONICAL TEST AUDIO | 仅保留为历史测试证据，不作为 MVP1 canonical audio baseline |
| D-056 `SOURCE_AUDIO_INDEX_V001` | 历史原音频导航索引 | Project Control Execution Log 已确认存在并已使用 | EXISTS / NAVIGATION ONLY | 可用于粗定位；ASR segment 时间边界不能直接作为正式剪辑边界 |
| S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` | MVP1 实际有声小说片段的朗读文本、说话顺序、对白/旁白检索 | 尚未建立正式 S3 | NOT ESTABLISHED | 第一版覆盖实际 MVP1 音频跨度（第134章开头→第135章开头），并与 canonical audio 绑定；必须区分 RAW / REVIEWED / VERIFIED |

## 3. S1 特殊登记

S1 结构检查发现：源文件章节标题由 `第460章 客人` 直接跳至 `第462章 诡异的死法`，没有检测到 `第461章` 标题。

该现象登记为：`SOURCE-NATIVE NUMBERING ANOMALY`。

处理规则：保持源文件原样，不补章、不重编号、不推断缺失内容。后续 derived index 必须保留这一事实。

## 4. MVP1 范围边界

- 正式 MVP1 起点：S2 第134章《【黑衣夫人】参观》开头。
- 第133章：`CONTEXT_ONLY`，只用于理解人物进入本篇前的情境，不进入 MVP1 正式成片。
- 有声小说章节/分集进度与原文章节边界并非完全一致，因此 MVP1 不再定义为“第134章 only”。
- 当前提供的第097集录屏从第134章开头开始，并连续进入第135章开头；录屏末段已到莫妮卡夫人入座、众人开始跟随入座附近。
- MVP1 终点以实际 canonical audio 的内容边界与时间码为准；S2 章节仅承担内容映射与追溯职责。
- 旧 A01–A07 / SH01–SH08 资产可作为历史输入，但是否全部适用于 MVP1，仍需在后续 Gate 重新审核，不能因历史 APPROVED 自动继承为正式生产资产。

## 5. 音频准备方法｜P0.1-05A

已验证当前可行的数据源准备链：

`用户提供完整录屏 RAW_CAPTURE` → `无重编码提取原始 AAC 音轨 RAW_AUDIO_EXTRACT` → `人工/内容校验起止锚点` → `裁切为 CANONICAL_AUDIO` → `登记文件规格与 SHA-256` → `建立 S3`。

当前录屏及提取音轨已验证前两步成立。下一步不是重新编码，而是锁定精确音频起止边界并生成 canonical trim。

## 6. 存储边界

canonical repo 为 **Private**。

Project Control 保存状态、规则、盘点和验收信息。正式文本源数据统一进入仓库根目录 `source_material/`；大型音视频二进制的最终存储策略仍需单独锁定。

正式路径：

- S1：`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`
- S2：`source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
- S3：`source_material/S3_audio_transcript/`

## 7. 当前缺口

1. S1 已锁定。
2. S2 已锁定。
3. MVP1 起点已锁定为第134章开头；实际内容跨入第135章开头。
4. MVP1 RAW_CAPTURE 与 RAW_AUDIO_EXTRACT 已取得并完成身份/规格核验。
5. MVP1 canonical audio 的精确起止时间码尚未锁定。
6. D-056 只能作为历史导航，不是精确剪辑边界。
7. S3 正式转写尚未建立。

## 8. P0.1 当前判断

P0.1 仍不能 PASS。

下一阶段：

- P0.1-05A：锁定当前 RAW_AUDIO_EXTRACT 的准确起止内容与时间码，并生成/登记 MVP1 canonical audio；
- P0.1-05B：设计 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` 结构与验证等级，覆盖实际 MVP1 音频跨度；
- P0.1-05C：选取真实音频小样逐段校验，验证从原音到 VERIFIED transcript 的方法；
- 完成后再评估 P0.1 是否具备 PASS 条件。
