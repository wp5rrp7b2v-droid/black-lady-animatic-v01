# S02-B｜君鹭远 B V002 批准及 A06 / N24 镜头换序｜审查记录

日期：2026-10-14
Status: **JUN LOCAL B V002 PO-APPROVED / A06 ↔ N24 REORDER DIRECTED / NEW VIDEO REVIEW-ONLY / NO CANONICAL REPLACEMENT**

## PO 最新决定

Product Owner 明确表示：**“批准B V002，然后我还发现A06和光勇提问这两个镜头顺序要换一下”**。

1. 已接受的局部审核片为 `S02_B_N20_JUN_ACK_N21_CONTEXT_B_V002_FULL_LINES.mp4`（相对于原 V003），不再回退原 A 或不完整台词 B V001。
2. 新的有效顺序在 N23 之后是 **N23 → A06（门仍打开）→ N24（光勇提问）→ N25（尼尔回答）→ 后续宁秋水/ N26**。
3. 此 PO 新决定覆盖 2026-10-06 `s02_b_sequence_order_correction_n24_a06_n25_2026-10-06.md` 中的旧有 `N24 → A06 → N25`，但不删除旧记录。新顺序重新采用较早 Patch 03 的 `A06 → N24`，以最新明确审批为准。
4. **不改变任何已经批准的 PNG**、台词或音频内容。

## V003 的源文件和精确拆镜事实

完整 V003 审核版：`S02_B_ASSEMBLY_REVIEW_V003_N16N17_V004_NING_REACTION.mp4`，SHA256 `827905c725ec0bc8c6b5fb169d8bc623c45c51c5c6c6fd514bb27f718cf10141`，720×1280，30fps，1927 帧，64.250s（含 AAC 尾部），此版本继续作为不可覆写母基线。

现有真实切点经相邻帧画面变化检查：
- N20→N21: frame 1078，35.933333s
- N23→N24: frame 1566，52.200000s
- N24→A06: frame 1631，54.366667s
- A06→N25: frame 1694，56.466667s
- N25→尾部宁反应: frame 1810，60.333333s
- 宁反应→N26: frame 1863，62.100000s

镜头调序不改变区段总帧数，N24 为 65 帧、A06 为 63 帧。改后：
- A06 显示 frames 1566:1629（取原源 1631:1694，63 帧，约 52.20–54.30s）
- N24 显示 frames 1629:1694（取原源 1566:1631，65 帧，约 54.30–56.467s）
- N25 从原 frame 1694 起不动。

君鹭远近景的已批准 B V002 视频处理保留：原 V003 frame 1078:1114 的 36 帧（1.2s）替换为 PO 选定 Jun PNG 静帧（941×1672，SHA256 `1af236000b271d327278e82bf3e744fee08bd49682966eb5fa75f731a67c46e7`，GitHub Approved-in-Staging，Actions exact intake `38507541961` PASS）。

## 本轮工作权限

- 允许依据当前叙述指令创建本地 **review-only** 完整视频及必要的局部预览；不擅自修改官方已发布母版。
- 必须完整保留 N16–N17 V004 的已批重剪、后段宁反应 B V002 已批静帧、整段原声、以及其它现有镜头时长与次序。
- 不进行 Story Shot canonical publication 或 registration，不合并 main。
- 待新的 V004 Review 通过后，另行处理正式视频版本发表及项目索引治理。
