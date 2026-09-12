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
| MVP1 Scope | 第一个正式成片范围 | Product Owner 于 2026-09-12 明确锁定 | LOCKED | MVP1 从 S2 第134章《【黑衣夫人】参观》开始；第133章仅作前置语境，不进入 MVP1 正式成片 |
| MVP1 原始有声小说音频 | 第134章 S3 与正式剪辑的真实音频事实源 | 当前尚未准备 canonical 第134章原音频 | NOT PREPARED | 音频的获取、准备、登记本身纳入 P0.1-05 能力建设；不要求先准备完整《黑衣夫人》全部有声书 |
| 历史测试音频 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` | 过去 Animatic / 音频实验 | 2,636,183 bytes；195.844989 sec；AAC 2ch 44.1kHz；SHA-256=`abaaab1c0c8362e6d61268ba09b0f0ce6cb915cf49c046fd3b32c49405746551` | NON-CANONICAL TEST AUDIO | 仅保留为历史测试证据，不作为 MVP1 第134章 canonical audio baseline |
| D-056 `SOURCE_AUDIO_INDEX_V001` | 历史原音频导航索引 | Project Control Execution Log 已确认存在并已使用 | EXISTS / NAVIGATION ONLY | 可用于粗定位；ASR segment 时间边界不能直接作为正式剪辑边界 |
| S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` | MVP1 第134章有声小说实际朗读文本、说话顺序、对白/旁白检索 | 尚未建立正式 S3 | NOT ESTABLISHED | 第一版只需覆盖 MVP1 第134章，并与其 canonical 原音频绑定；必须区分 RAW / REVIEWED / VERIFIED |

## 3. S1 特殊登记

S1 结构检查发现：源文件章节标题由 `第460章 客人` 直接跳至 `第462章 诡异的死法`，没有检测到 `第461章` 标题。

该现象登记为：`SOURCE-NATIVE NUMBERING ANOMALY`。

处理规则：保持源文件原样，不补章、不重编号、不推断缺失内容。后续 derived index 必须保留这一事实。

## 4. MVP1 范围边界

- 正式 MVP1：S2 第134章《【黑衣夫人】参观》。
- 第133章：`CONTEXT_ONLY`，只用于理解人物进入本篇前的情境，不进入 MVP1 正式成片。
- P0.1 的音频工作仅需先服务 MVP1 第134章，不需要一次性完成第133–164章全部原音频准备。
- 旧 A01–A07 / SH01–SH08 资产可作为历史输入，但是否全部适用于 MVP1，仍需在后续 Gate 重新审核，不能因历史 APPROVED 自动继承为正式生产资产。

## 5. 存储边界

canonical repo 为 **Private**。

Project Control 仅保存状态、规则、盘点和验收信息。正式源数据统一进入仓库根目录 `source_material/`；大型音视频二进制的具体存储方式在后续 Gate 中单独决定。

正式路径：

- S1：`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`
- S2：`source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
- S3：`source_material/S3_audio_transcript/`

## 6. 当前缺口

1. S1 已锁定。
2. S2 已锁定。
3. MVP1 第134章范围已锁定。
4. MVP1 第134章 canonical 原音频尚未准备；需先建立获取/准备/登记方法并锁定实际文件实体。
5. D-056 只能作为导航，不是精确剪辑边界。
6. S3 正式转写尚未建立。

## 7. P0.1 当前判断

P0.1 仍不能 PASS。

下一阶段：

- P0.1-05A：准备并锁定 MVP1 第134章 canonical 原音频实体；
- P0.1-05B：设计 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` 结构与验证等级，第一版只覆盖第134章；
- P0.1-05C：选取真实音频小样逐段校验，验证从原音到 VERIFIED transcript 的方法；
- 完成后再评估 P0.1 是否具备 PASS 条件。
