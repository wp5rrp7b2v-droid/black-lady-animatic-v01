# Opening CH133 前奏｜内容审批与音源／资产可行性核查 V001

日期：2026-10-28　状态：CONTENT DESIGN PO APPROVED / AUDIOVISUAL PRODUCTION GATE BLOCKED
项目基线：Opening V001 LOCKED（33.088s）；原正式 S2/S3 / Asset Registry / Google Drive `06_Audio`。此文不改变已有媒体身份。

## 1. Product Owner 决策边界

PO 对第133章四节拍内容最小验证回答“可以”。据此批准 **P01 人物选择 → P02 契约代价 → P03 五日庄园钥匙任务 → P04 两条警告 → 原第134章33秒 Opening** 作为单个 Opening 新候选的设计 baseline。
当前授权足以继续声源／参考资产验证与最小 Animatic 设计；不等于批准新增音频生成、正式 Story Shot 出图、恢复木门 A/B、扩大整个 MVP1 的正式原音锁定范围、替换正式母版或批准新视频发布。
与 R366 比较：原先 PO_REVIEW_PENDING 的剧情骨架已提升为 DESIGN_APPROVED；P0.1 已锁定原始 MVP1 边界本身未变。

## 2. 已验证事实｜原音

- 正式 `AUDIO_MVP1_CANONICAL_V001.m4a` 以第134章尼尔迎宾开头；S3 第一段 0–33.02s 不包含任务和禁忌。
- 历史 P0.1 Source Inventory 记载原始录屏 `ScreenRecording_09-12-2026 13-40-39_1.MP4`（235,987,834 bytes，SHA-256 `9bab514775f0771987b094cdd9394b81d6a49a7bace995ef9ad4dbcce448abd1`），以及无重编码音频提取 `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`（5,244,616 bytes，SHA-256 `d9a297b275a2fc42b85fa7b26407c4824c17efc63d1b9d148470f224d96be7f2`）。
- 同一正式 Source Inventory 说明现行 canonical 音频从上游提取音频**约 22.800 秒处起切**；此段上游未进入正式音频。关键未知：被裁去的 0–22.8 秒是否含有第133章末尾任务 / 两条提示。**必须先查真实原始录音，不得把这 22.8 秒直接标为第133章音源。**
- 已搜索已连接 Google Drive 的 `MVP1`、`audio`、`第096集`、`第097集`、`诡舍`、`ScreenRecording` 等文件名；`06_Audio` 文件夹 ID `1yzcpckOoogFznfiQdPDLKxhzIG6PoQx4` 当前读取结果为空。未找到可认证第133章文件，但这一覆盖仅限已连接 Drive。
- 本次没有取得原 RAW_CAPTURE、RAW_AUDIO_EXTRACT 的真实二进制或其解码波形，无法确认被裁剪内容；此项 `UNKNOWN/NOT VERIFIED`，不是音源不存在的结论。

## 3. 已验证事实｜人物、场景与镜头资产

直接按 main Asset Registry `production/asset_registry/asset_registry.jsonl` 的 CURRENT/APPROVED 项及 GitHub 目录元数据检查，已定位：

| 用途 | 正式注册与物理候选 | 审核等级 / 限制 |
|---|---|---|
| P01 宁秋水 | CURRENT 人物正面／三分之四脸／上身等，例 `AST_IMG_000034` FACE_FRONT、`AST_IMG_000071` FACE_3Q_LEFT | EXISTING APPROVED REF；未验证能否直接构成 P01 情境新镜头 |
| P01 君鹭远 | CURRENT 人物正面／三分之四脸／全身，例 `AST_IMG_000017` FACE_FRONT、`AST_IMG_000072` FACE_3Q_LEFT | EXISTING APPROVED REF；叙事新情境需另行出图批准 |
| 前序其他说话人 | `CHAR_BAI_XIAOXIAO`、`CHAR_MENG_JUN` 在当前 Asset Registry 均无记录，正式角色目录也未找到 | MISSING MASTER；首轮尽量不引入这两人的屏幕形象 |
| P02 手腕黑手印 | 第133章有原著事实锚点，但尚无专用 APPROVED Prop/Story Shot | NEEDS NEW VISUAL EVIDENCE；不得将角色正面图冒充手印特写 |
| P03 血门任务文字场景 | 第133章文字原著成立；先前单独“木门 A”候选尚未 PO 通过，B 未授权且专项暂停 | NOT REUSABLE AS APPROVED；不得绕过木门暂停、默认复工 |
| P04 危险提示视觉 | 可复用已批准人物表情作参考；`N17_BLOOD_DOOR_WARNING_APPROVED_V001.png` 属于原第134章及后续场景 Story Shot | REFERENCE ONLY；不可移到第133章作为相同时空的成片镜头 |
| 原 Opening 衔接 | 已批准 A01/A02/N01–N10 镜头和完整 33.088s Opening V001 | VERIFIED PUBLISHED；原片不修改 |
| 古堡入口/庄园大门 | `AST_IMG_000105` Castle Entrance V002 DAY/DOOR_OPEN；`AST_IMG_000107` Manor Gate V002 DAY/CLOSED | 两个 APPROVED 场景 Master。**庄园大门和古堡大门是不同地点**，不能混淆；现有庄园大门图仅说明场景结构，未证明可演示任务完成 |

本次 GitHub 目录列表核对了相关 PNG 的文件名、大小、Git blob SHA，Asset Registry 给出历史批准状态与 SHA-256。**没有对原图重新执行 binary SHA-256**，故本次结果为 `REGISTRY AND METADATA MATCH / NEW-SHOT EXACT VERIFICATION PENDING`。

## 4. 最小可行制作决策

**建议保持 P01–P04 四节拍不变，但不立即连续批量出图。** 当前的关键假设是：可用原声音源（或独立获批的新音频方案）能在约20–24秒内自然传递 P01–P04 信息，而新镜头能尊重原著场景时序。

**最先做的可证伪实验：** 查原 RAW_AUDIO_EXTRACT `00:00.000–00:22.800` 的真实听审文本、说话者、时间码和音质，并对照第133章任务/提示。只需这一段即可判断是否能复用上游真实声音；不先生成新人物、不花成本制作完整前奏。

PASS-A：在截掉的 22.8 秒内确实有可完整利用的任务及两条提示，且边界、声质与使用许可合规，可继续精确 source audio mapping。
FAIL-A：只有广告、过门、无关对白或提示不完整等；停止将其作为完整第133章音源路线。此时新配音方案需另行批准，不能从不存在的 audio source 编出声画。
PASS-B：P01/P02 至少一段视觉能用宁秋水/君鹭远 APPROVED refs，生成可追踪的真实新候选经 PO 审核；P03/P04 不使用被暂停的木门 A/B。
FAIL-B：无法在原情境下保持人物身份、没有手腕素材、画面仅文字卡堆砌且观感无实质提升；不进入完整22秒扩展。

## 5. 推荐最小声画样片目标（尚未渲染）

优先只做 **P01＋P02（约 8–9 秒）** 的人物情绪→身体异常连贯性试验，或在上游音频包含完整任务时优先做 **P03＋P04（约 10–13 秒）** 的任务可理解性试验。二者只是备选最小测试，不同时批量执行；先以原音审听结果和资产可用性决定哪一个更快、成本更低。
试片生成前必须完成：可追溯音轨／合规新声方案、Source/Scene Reference、Bundle、Work 单候选、PO 审核、Exact Binary Verification。GitHub Actions 做渲染及技术 QC。走既定 Chat → GitHub Actions → Work → PO → Chat 流程，不切 Codex。

## 6. 继续与停止界限

- 已通过：PO 四节拍内容设计 Gate；CH133 原著事实与 CH134 开场内容的时序核对；宁/君人物现有正式 Reference 的存在性与 CURRENT 记录。
- 未通过：第133章新音源、22.8秒被裁片头内容、契约手印视觉、成片观感、任何 Story Shot / Video Index 新注册。
- 保留：Opening V001 SHA-256 `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`、Story Shots=32、Video Index=3、P0.3 IN PROGRESS、血门 A PAUSED / B NOT AUTHORIZED。
- 此文件用作恢复工作的单一审片与验证清单，不制造额外登记矩阵，不把 UNKNOWN 改为 PASS。

## 2026-10-28｜新增核查：第133章原声提交范围与旧片头试验

- 历史分支 `feature/episode-unified-premise-pilot-20261018` 仍保留 `EPISODE_UNIFIED_PREMISE_PILOT_V001–V004` 和同源QC。10月18日已有 `14秒任务/提示静默文字板 + 约6.57秒原欢迎` 的独立短样。V002风格过强、V003版式被否定，V004未获PO视觉批准。**不将无旁白纯文字卡直接作为新路线，也不重开此失败版式。**
- GitHub main及该历史分支已核查相关 audio/MP4 文件树。项目有 `AUDIO_MVP1_CANONICAL_V001.m4a`，没有定位出较早的 `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a` 或 `ScreenRecording_09-12-2026 13-40-39_1.MP4` 的原始可听二进制；已连接 Google Drive `06_Audio` 目录为空，Project/Library 文件检索也未找到上游音频。**因此历史开头22.8秒仍为 UNKNOWN，未实际听审。**
- **制作建议：按已批准的 P01–P04 故事结构，要完成有原著声音支撑的前奏，应补充第133章原始有声小说录音。**这不是证明“所有新前奏绝对需要语音”，而是对当前非纯文字卡路线与已获得素材的结论；未发起音频生产，也未修改原音锁定。
- 如果用户可提供完整第133章原音，优先提供完整原音并自动定位；若只能提供剪辑，最小三组内容边界为：
  1. 人物选择：君鹭远“我不怕”起，至宁秋水“我带你吧……顺便也正好可以历练一下”止；
  2. 契约代价：孟军要求君鹭远伸手、划破手掌起，至契约结束、痛苦和虚弱消失（可包含腕部黑手印）止；
  3. 任务和警示：“下一刻，血门上又出现了几行血字”起，至“提示2：不要长时间和它对视”止。
- 每组应保留约5–10秒音频 handles（不得截句）。实际时码、音色、读者版权及配音对应关系在用户提供音源后核验，尚未核验前不填写虚构时间码。
- 如果上游0–22.8秒以后被找到，优先独立听审能否复用 P03/P04 的局部内容，但其处于原章节末尾，不能凭仅这段录音覆盖早前 P01/P02。若含足够完整内容，可减少用户需要补交的第三段；**目前不宣称其含有任务提示**。
- 现有第134章Opening原音不需要再提供；正式Opening V001、Story Shot 32、Video Index 3不变。血门A/B专项继续暂停。
