# P0.1-02｜现有源数据盘点

- 项目：BLACK-LADY-001｜《诡舍·黑衣夫人》
- 日期：2026-09-12
- Gate：P0.1｜故事与文本数据基线
- 状态：INVENTORY COMPLETE / BASELINE BUILDING

## 1. 源数据命名

- S1：`S1_SOURCE_NOVEL_FULL_V001`
- S2：`S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
- S3：`S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001`

## 2. 盘点结果

| Source | 目标职责 | 当前证据 | 当前状态 | 结论 |
|---|---|---|---|---|
| S1 `S1_SOURCE_NOVEL_FULL_V001` | 完整《诡舍》世界观、人物、跨篇章上下文检索 | canonical GitHub main 未发现；ChatGPT File Library 检索未发现可确认的完整《诡舍》全本文件 | MISSING / UNCONFIRMED | P0.1 尚缺完整系列级原著基线；不得把 S2 反推为 S1 |
| S2 `S2_SOURCE_BLACK_LADY_TEXT_V001.txt` | 《黑衣夫人》篇章原著工作文本 | Product Owner 于 2026-09-12 指定当前上传文本为唯一 canonical source；第133–164章；UTF-8 plain text；SHA-256=`159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6` | CANONICAL / LOCKED | P0.1-03 COMPLETE；其他同名/近似文本均为 NON-CANONICAL |
| 原始有声小说音频 | S3 与正式剪辑的真实音频事实源 | 2026-09-11 preliminary audit 已确认存在；当前 canonical GitHub main 不保存音频实体 | EXISTS / PATH NOT YET CANONICALIZED | 保留为音频最高事实依据；需登记实际文件、格式、时长、哈希 |
| D-056 `SOURCE_AUDIO_INDEX_V001` | 原音频导航索引 | Project Control Execution Log 已确认存在并已使用 | EXISTS / NAVIGATION ONLY | 可用于粗定位；ASR segment 时间边界不能直接作为正式剪辑边界 |
| S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001` | 《黑衣夫人》有声小说实际朗读文本、说话顺序、对白/旁白检索 | 当前 canonical GitHub main 与 File Library 检索均未发现可确认的正式 S3 转写文件 | NOT ESTABLISHED | 需建立；必须与原始音频绑定，并区分 RAW / REVIEWED / VERIFIED 状态 |

## 3. 存储边界

canonical repo 已于 2026-09-12 确认为 **Private**。

Project Control 仅保存状态、规则、盘点和验收信息。正式源数据统一进入仓库根目录 `source_material/`；大型音视频二进制的具体存储方式在后续 Gate 中单独决定。

## 4. 当前缺口

1. S1 完整《诡舍》原著：尚未找到/登记。
2. S2 已锁定唯一 canonical source。
3. 原始音频存在，但 canonical 路径、文件名、格式、时长、哈希尚未登记。
4. D-056 只能作为导航，不是精确剪辑边界。
5. S3 正式转写尚未建立。

## 5. P0.1 当前判断

P0.1 不能 PASS。

下一阶段：

- P0.1-04：定位并登记 S1 完整《诡舍》源文件；
- P0.1-05：登记原始有声小说音频实体，并设计/验证 S3 转写结构；
- 完成一小段 S3 与真实音频逐段校验后，再评估 P0.1 是否具备 PASS 条件。
