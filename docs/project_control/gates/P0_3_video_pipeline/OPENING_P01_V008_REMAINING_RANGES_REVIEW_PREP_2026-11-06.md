# Opening P01 V008｜0–26秒及43–63.375秒专项审片准备与技术检验

日期：2026-11-06
状态：**REVIEW MATERIALS PREPARED / NO NEW EDITORIAL APPROVAL / NO RE-EDIT**

## Baseline与PO已锁定批准范围
- GitHub Project Control R414 / BL-D-196：Product Owner 审片回复“这段可以”，仅批准 V008 **26.000–43.000秒**中段视觉与听感。
- INS04 搭肩原编辑入出点 `32.500–38.750s` 保持；此次只是从V008全片派生审片片段，没有改变任何母版帧、镜头顺序或原音。
- V008 母片SHA256：`0d29bfeae202ba1b143bda9cfd8d3efa6f6a67df5d19ad60dbdca4ed0f320296`；63.375秒/942×1672/24fps/1521帧/11镜10切。

## 本次最小检查
- 实际审片第一段 **00:00–00:26**，视频 `OPENING_P01_V008_OPEN_00_26_PO_REVIEW.mp4`，26.000s，3,053,424 bytes，SHA256 `cd90c87aec28117c1e2ab5aa973396bb0a034df20edc9ed1b756de8fef5ebeac`。重点观察3.75s君鹭远入、10.50s同角色双景别衔接、17.50s白潇潇解释起点。仍无逐字发声核验，不把合理性检查冒充PO批准。
- 第二段待审为 **00:43–00:63.375**；为保留与已批准中段的完整上下文，从40.000秒提取，审片视频 `OPENING_P01_V008_END_40_63_375_PO_REVIEW.mp4`，23.375s，2,996,636 bytes，SHA256 `55cba07935addcd84aeded81eda0efc400d6d5e5c714b614b30cf6ae0d819043`。**40–43秒仅为锁定上下文，不重新审核或修改。** 重点观察44.5s感激转担忧、49.75s由担忧入纠结、57.50s三人收束。
- 两段H.264/AAC 942×1672/24fps，FFmpeg零错误完整解码，音频与V008相应时间片PCM 8kHz单声道相关系数分别 **0.99958771** / **0.99971932**；这些审片片段进行了音频重新编码，故不能声称与完整母片AAC逐字节相同。
- 实际10个镜头关键时刻联系图 `OPENING_P01_V008_REMAINING_SECTIONS_REVIEW_BOARD.jpg` SHA可在本地会话中验证。母片文件未写入、未变更，没有V009；所有衍生审片视频只留会话中，不公开上传版权原声到GitHub。

## Review结论及Scale Gate
- **TECH PASS：**可独立回看的两个审片片段存在、解码成功、时间范围正确、音频内容高相关；完整V008已批准26–43秒局部未被触碰。
- **UNKNOWN：**两段是否获得PO声画美学PASS。没有新的明确审片失效证据，因此不继续编辑或产生V009，不因单纯“再看一次”改变原设计。
- **PO PASS条件：**两段无显著台词与画面归属不匹配、重复切镜或错误情绪衔接；然后再进行完整V008 63.375秒的显式视频批准决策。
- **PO FAIL条件：**指出具体时点与实际失败表现，则只修改该失败区间，保护已批准26–43秒，不新增镜头、不变更批准资产。
- No Canonical Video/Video Index edit; index保持3、Story Shots保持49、Audit Events239，P0.3仍IN PROGRESS；Mac EOD同步无新的独立证据。
