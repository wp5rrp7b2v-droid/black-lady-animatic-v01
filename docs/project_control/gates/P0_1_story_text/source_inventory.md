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
| MVP1 Scope | 第一个正式成片范围 | Product Owner 已锁定连续有声小说边界 | LOCKED | 起点映射 S2 第134章开头，终点映射第135章开头；按真实有声小说连续音频边界定义，不按原文章节硬切 |
| MVP1 RAW_CAPTURE `ScreenRecording_09-12-2026 13-40-39_1.MP4` | MVP1 原音来源证据 | 235,987,834 bytes；381.958333 sec；AAC 2ch 44.1kHz + H.264；SHA-256=`9bab514775f0771987b094cdd9394b81d6a49a7bace995ef9ad4dbcce448abd1`；画面确认第097集【黑衣夫人】主人 | RAW CAPTURE / VERIFIED IDENTITY | 对应首个 MVP 有声小说连续片段 |
| MVP1 RAW_AUDIO_EXTRACT `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a` | 从 RAW_CAPTURE 无重编码抽取的音频工作源 | 5,244,616 bytes；381.941995 sec；AAC 2ch 44.1kHz；SHA-256=`d9a297b275a2fc42b85fa7b26407c4824c17efc63d1b9d148470f224d96be7f2` | RAW_AUDIO_EXTRACT / VERIFIED | canonical audio 的直接上游源 |
| MVP1 CANONICAL_AUDIO `AUDIO_MVP1_CANONICAL_V001.m4a` | S3 与后续正式剪辑的最高音频事实源 | 4,957,338 bytes；359.141995 sec；AAC 2ch 44.1kHz；SHA-256=`8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`；Product Owner QC 通过 | CANONICAL / LOCKED | 起点完整保留“欢迎各位来到艾伦古堡”；终点完整保留“而后又匆匆离去备餐”；P0.1-05A COMPLETE |
| 历史测试音频 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` | 过去 Animatic / 音频实验 | 2,636,183 bytes；195.844989 sec；AAC 2ch 44.1kHz；SHA-256=`abaaab1c0c8362e6d61268ba09b0f0ce6cb915cf49c046fd3b32c49405746551` | NON-CANONICAL TEST AUDIO | 仅保留为历史测试证据，不作为 MVP1 canonical audio baseline |
| D-056 `SOURCE_AUDIO_INDEX_V001` | 历史原音频导航索引 | Project Control Execution Log 已确认存在并已使用 | EXISTS / NAVIGATION ONLY | 可用于粗定位；ASR segment 时间边界不能直接作为正式剪辑边界 |
| S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` | MVP1 实际有声小说片段的朗读文本、说话顺序、对白/旁白检索 | canonical audio 已锁定，S3 尚未正式建立 | NEXT / NOT ESTABLISHED | 第一版覆盖 `AUDIO_MVP1_CANONICAL_V001.m4a` 全部跨度，并必须区分 RAW / REVIEWED / VERIFIED |

## 3. S1 特殊登记

S1 结构检查发现：源文件章节标题由 `第460章 客人` 直接跳至 `第462章 诡异的死法`，没有检测到 `第461章` 标题。

该现象登记为：`SOURCE-NATIVE NUMBERING ANOMALY`。

处理规则：保持源文件原样，不补章、不重编号、不推断缺失内容。后续 derived index 必须保留这一事实。

## 4. MVP1 范围边界

- 正式 MVP1 起点：有声小说内容“欢迎各位来到艾伦古堡”，映射 S2 第134章《【黑衣夫人】参观》开头。
- 正式 MVP1 终点：有声小说内容“而后又匆匆离去备餐”，整体内容映射已进入 S2 第135章开头。
- 第133章：`CONTEXT_ONLY`，只用于理解人物进入本篇前的情境，不进入 MVP1 正式成片。
- 有声小说章节/分集进度与原文章节边界并非完全一致，因此 MVP1 不定义为“第134章 only”。
- `AUDIO_MVP1_CANONICAL_V001.m4a` 是正式音频边界与后续 S3 的最高音频事实源。
- 旧 A01–A07 / SH01–SH08 资产可作为历史输入，但是否全部适用于 MVP1，仍需在后续 Gate 重新审核，不能因历史 APPROVED 自动继承为正式生产资产。

## 5. 音频准备方法｜P0.1-05A｜COMPLETE

已验证并锁定当前可行的数据源准备链：

`用户提供完整录屏 RAW_CAPTURE` → `无重编码提取原始 AAC 音轨 RAW_AUDIO_EXTRACT` → `人工/内容校验起止锚点` → `stream copy 裁切为 CANONICAL_AUDIO` → `Product Owner 首尾 QC` → `登记文件规格与 SHA-256` → `建立 S3`。

本次 canonical audio 由 `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a` 约 22.800 sec 起切至源末尾，未重新编码。Product Owner 已完成首尾听审并批准。

## 6. 存储边界

canonical repo 为 **Private**。

Project Control 保存状态、规则、盘点和验收信息。正式文本源数据统一进入仓库根目录 `source_material/`；大型音视频二进制当前保留本地正式项目目录，最终仓储策略后续单独锁定。

正式路径：

- S1：`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`
- S2：`source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
- S3：`source_material/S3_audio_transcript/`
- MVP1 canonical audio：本地正式项目 `production/audio/source/MVP1/AUDIO_MVP1_CANONICAL_V001.m4a`

## 7. 当前缺口

1. S1 已锁定。
2. S2 已锁定。
3. MVP1 范围与 canonical audio 已锁定。
4. P0.1-05A 已完成。
5. D-056 只能作为历史导航，不是精确剪辑边界。
6. S3 正式结构、分段规则与 VERIFIED 小样尚未建立。

## 8. P0.1 当前判断

P0.1 仍不能 PASS。

下一阶段：

- P0.1-05B：设计并锁定 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` 字段、segment 规则与 RAW / REVIEWED / VERIFIED 验证等级；
- P0.1-05C：选取 `AUDIO_MVP1_CANONICAL_V001.m4a` 真实小样逐段校验，验证从原音到 VERIFIED transcript 的方法；
- 完成后再评估 P0.1 是否具备 PASS 条件。
