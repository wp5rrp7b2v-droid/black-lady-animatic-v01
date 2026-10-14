# 《诡舍·黑衣夫人》｜君鹭远认可回应近景｜Product Owner 候选图选择记录

日期：2026-10-14
任务：`S02B_JUN_ACKNOWLEDGEMENT_TEST_01`
当前状态：**PO APPROVED SELECTED VISUAL VIA NEW CHATGPT SHARE LINK / EXACT SOURCE PNG NOT YET INGESTED / NO CANONICAL PUBLICATION**

## 1. 最新 PO 直接决定（取代前一候选选择）
Product Owner 明确指示：

> 前面这张不通过，以现在这个连接为批准件：https://chatgpt.com/s/m_6acee7af3ad081918088dbaf92e0771a

这条新决定的优先级高于此前任何关于前一候选图的临时认可或拟上传安排。

### 被拒绝的旧候选
- 旧 ChatGPT Share URL：`https://chatgpt.com/s/m_6acee25f66748191aca3eb4b064500ec`
- 旧 Candidate 01 报告 SHA256：`1020ae12483812271edf6d3ba9c7df033f94b38bc84825c570d8061e7b51b804`
- **PO 结果：REJECTED / DO NOT STAGE AS APPROVED / DO NOT PUBLISH / DO NOT REGISTER.**
- 以上旧 SHA256 **不得继承到新的批准图**。

### 本轮 PO 选择的新候选
- **PO 已明确批准的视觉版本分享 URL：**
  `https://chatgpt.com/s/m_6acee7af3ad081918088dbaf92e0771a`
- PO 判定：**VISUAL SELECTED / APPROVED AS SEEN**。
- 实际原始 PNG 文件名、宽高、字节数、SHA256、Git blob：**PENDING / NOT YET PROVIDED OR INDEPENDENTLY VERIFIED**。
- 此链接为候选选择/视觉审批依据，不能当成 GitHub 源图文件或二进制哈希。
- 当前 Chat 通过公开 URL 无法可靠提取此分享页面的原始 PNG；不得从分享截图、旧图或原参考图重制/推定新文件。
- 审批结论有效；**Exact Binary Verification、Canonical Publication、Story Shot Registration 均未完成**。

## 2. 下一步执行——仅取得已批准原始 PNG
1. Work 根据最新分享链接选择的那张 **原始 PNG**，不得重新生成、裁切、调色、提高分辨率、转换格式、重新压缩或用旧图代替。
2. 上传到 GitHub 审核分支 `review/s02b-jun-nod-insert-20261014` 的 `staging/story_shot_candidates/S02B_JUN_ACKNOWLEDGEMENT_TEST_01/` 内，建议文件名 `S02B_JUN_ACKNOWLEDGEMENT_TEST_01_PO_SELECTED.png`；不得以旧 SHA 命名、冒充原图。
3. 返回新图的实际尺寸、字节数、SHA256、Git blob、GitHub 路径与 commit。
4. Chat 对 GitHub staging 的真实 PNG 独立核验，确认与本次 PO 已批准的版本对应；仅在核验完成且另有发布授权后才执行 canonical publication 和登记。
5. 如果 Work 无法将已批准 PNG 无损上传，停止并报告；不再次生成候选。

## 3. 严禁超范围
- 不使用被拒旧图作为“批准件”。
- 不擅自发布为正式 Approved Story Shot、更新 Story Shot Index 或 Video Index。
- 不调整或替换当前 PO 审核通过的 S02-B 全片 V003（含 N16-N17 V004 与宁秋水 B V002）。
- 不将此视觉审批冒充原始 PNG 二进制已经 Exact PASS。
