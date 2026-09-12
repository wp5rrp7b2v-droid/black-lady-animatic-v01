# P0.1-02｜现有源数据盘点

- 项目：BLACK-LADY-001｜《诡舍·黑衣夫人》
- 日期：2026-09-12
- Gate：P0.1｜故事与文本数据基线
- 状态：INVENTORY COMPLETE / BASELINE NOT YET LOCKED

## 1. 源数据命名

- S1：`S1_SOURCE_NOVEL_FULL_V001`
- S2：`S2_SOURCE_BLACK_LADY_TEXT_V001`
- S3：`S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

注：S3 名称已按 Product Owner 指示由 `S3_SOURCE_AUDIO_TRANSCRIPT_V001` 更名为 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`，明确限定为《黑衣夫人》有声小说转写。

## 2. 盘点结果

| Source | 目标职责 | 当前证据 | 当前状态 | 结论 |
|---|---|---|---|---|
| S1 `S1_SOURCE_NOVEL_FULL_V001` | 完整《诡舍》世界观、人物、跨篇章上下文检索 | canonical GitHub main 未发现；ChatGPT File Library 检索未发现可确认的完整《诡舍》全本文件 | MISSING / UNCONFIRMED | P0.1 尚缺完整系列级原著基线；不得把 S2 反推为 S1 |
| S2 `S2_SOURCE_BLACK_LADY_TEXT_V001` | 《黑衣夫人》篇章原著工作文本 | File Library 存在多份 `黑衣夫人完整故事.txt`；可确认从第133章【黑衣夫人】起，并检索到第163章【黑衣夫人】天晴 | EXISTS / DUPLICATES / CANONICAL COPY NOT YET DESIGNATED | 内容基础已存在；下一步需选择唯一 canonical copy、计算哈希并登记来源/范围 |
| 原始有声小说音频 | S3 与正式剪辑的真实音频事实源 | 2026-09-11 Project Control preliminary audit 已确认“原始有声小说音频源文件”存在；当前 canonical GitHub main 不保存音频实体 | EXISTS / EXTERNAL-OR-LOCAL / PATH NOT YET CANONICALIZED | 保留为音频最高事实依据；需在受控目录中登记实际文件、格式、时长、哈希 |
| D-056 `SOURCE_AUDIO_INDEX_V001` | 原音频导航索引 | Project Control Execution Log 已确认存在并已使用 | EXISTS / NAVIGATION ONLY | 可用于粗定位；历史验证表明 ASR segment 时间边界不能直接作为正式剪辑边界 |
| S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` | 《黑衣夫人》有声小说实际朗读文本、说话顺序、对白/旁白检索 | 当前 canonical GitHub main 与 File Library 检索均未发现可确认的正式 S3 转写文件 | NOT ESTABLISHED | 需建立；必须与原始音频绑定，并区分 RAW / REVIEWED / VERIFIED 状态 |

## 3. 仓库与存储现状

当前 canonical repo：`wp5rrp7b2v-droid/black-lady-animatic-v01`。

截至本次盘点，GitHub `main` 主要保存：Project Control、Remotion 工程、workflow、历史 artifact payload；未发现 S1/S2/S3 正式源数据实体。

在仓库仍为 Public 时，本次只写入源数据元数据与状态，不上传小说正文、完整音频或转写正文。

## 4. 当前缺口

1. S1 完整《诡舍》原著：尚未找到/登记。
2. S2 已存在，但存在多份同名副本，尚未指定唯一 canonical copy。
3. 原始音频存在，但实际 canonical 路径、文件名、格式、时长、哈希尚未纳入 Project Control。
4. D-056 索引存在，但只能作为导航，不是精确剪辑边界。
5. S3 正式转写尚未建立。

## 5. P0.1 当前判断

P0.1 不能 PASS。

下一阶段应优先完成：

- P0.1-03：锁定 S2 唯一 canonical copy，并确认《黑衣夫人》篇章范围与来源；
- P0.1-04：定位并登记 S1 完整《诡舍》源文件；
- P0.1-05：登记原始有声小说音频实体，并设计/验证 S3 转写结构；
- 完成一小段 S3 与真实音频的逐段校验后，再评估 P0.1 是否具备 PASS 条件。
