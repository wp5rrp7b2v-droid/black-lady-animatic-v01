# 《诡舍·黑衣夫人》｜Opening P01 V009 审片候选（开头与结尾定向整改）
日期：2026-11-06
状态：**V008 26–43s PO SCOPED PASS RETAINED / V009 TECHNICAL PASS / V009 PO ARTISTIC VERDICT PENDING / NOT CANONICAL**

## 1. 新增 PO 审片反馈（事实）
- Product Owner 对拆出的第一段 00–26s 指出：“第一段第一个镜头应该是第二个”。
- 对第二段 43–63.375s 指出：“第二段感觉不太对”。
- **事实/确认的失败**：旧版本第一镜为 `INS00` 空住宅入口、第二镜为 `INS05` 白潇潇劝阻；PO要求开头由原第二镜承接。
- **推断/待审假设**：旧结尾 `OPEN05` 感激→`INS08` 担忧单人→`INS09` 低头纠结单人→`OPEN07` 三人收束，两个连续单人内心镜让宁秋水与“怕连累他人”的关系消失。PO 未具体指出问题根因，此推断不是 PO 已认可的解释。
- 既有 **V008 26.000–43.000s PO scoped audio-visual PASS**（BL-D-196）仍为 baseline；此前的 `INS04` 搭肩 `32.500–38.750s` 严格保持编辑时间线。

## 2. V009 实际改动及 EDL（9段、8次切镜）
| 开始(s) | 结束(s) | 镜头 | 处理 |
|---:|---:|---|---|
| 0.000 | 3.750 | INS05 | 原第二镜成为第一镜；删除起始 INS00 住宅门口空镜，不重新插回 |
| 3.750 | 10.500 | INS07 | 沿用 V008 决定开口镜 |
| 10.500 | 17.500 | OPEN02 | 沿用 V008 决心持续镜 |
| 17.500 | 25.000 | INS06 | 沿用 V008 白潇潇风险解释 |
| 25.000 | 32.500 | OPEN03 | **含已批准中段26–32.5**，沿用 V008 源画面 |
| 32.500 | 38.750 | INS04 | **已批准中段** 宁秋水搭肩，时间与画面保留 |
| 38.750 | 44.500 | OPEN05 | **已批准中段38.75–43** 完整保留；43–44.5亦沿用旧版 |
| 44.500 | 55.000 | OPEN06 | 以已有 Approved 宁秋水＋君鹭远关系镜，替换 V008 连续 INS08/INS09 单人特写 |
| 55.000 | 63.375 | OPEN07 | 三人决定镜提前由57.5s至55s；以较完整关系镜收束 |

- V008 11段/10次切镜 → V009 **9段/8次切镜**，无新出图/复用失败镜头。
- 仅改变原视频 `0–3.75s` 与 `44.5–63.375s` 两处；其余时段从 V008 解码帧沿用（重新H.264编码）。完整 **0–63.375s** 原声保持不动。
- 这只验证有依据的 **一个结尾设计候选**，不是对 PO“感觉不太对”的根因已独立证明。若 PO 不认可，仍仅围绕结尾声音、情绪与人物空间定位修正，不扩大镜头生产。

## 3. Exact source / 音视频实测核查
- Source MP4: `OPENING_P01_V008_NARRATIVE_SYNC_REVIEW_63S.mp4` SHA256 `0d29bfeae202ba1b143bda9cfd8d3efa6f6a67df5d19ad60dbdca4ed0f320296` 已匹配。
- 原音 `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a` SHA256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac` 已匹配。已认证14张GitHub来源PNG/JPEG在本轮再次对照 artifact manifest：14/14 SHA256/bytes PASS；仅衍生帧修改，不更改任何 Canonical Story Shot 图片。
- 新视频 `OPENING_P01_V009_OPENING_AND_ENDING_REVIEW_63S.mp4`，942×1672/24fps/1521帧，视频轨63.375s、封装时长63.381s（AAC尾帧）；大小 **8,108,239 bytes**，SHA256 `461dcae9bf5032802d9958779602ee353dfe22feab74ea8cb6d99dc4752e58d5`。
- FFmpeg完整解码0错误；从 V009及获批完整原音的0–63.375s提取AAC→ADTS，`cmp` **bit-exact PASS**，共同SHA256 `427f5993d7da774fc42cfda4d7fa97755ccbf0a12ec3f1a4f90d1ff0e1a48056`。
- 已批准区间 **26.000–43.000s 全408帧**从 V008 解码后沿用相同素材与时间线，并在 V009 输出逐帧独立核对：两者全408帧平均绝对像素差均值2.1459/255、最大单帧均值2.2256/255，属重新编码误差；**非二进制/像素逐字节相等，不能称 exact binary unchanged**。镜头行为与边界原样保留。
- 新增两段仅做PO review：`OPENING_P01_V009_OPEN_00_26_REVIEW.mp4` 26.0s，SHA256 `d2bab4695b630aa805f0fb192c6cab21ef029c666966d3d4e799f9f52a1f1b56`；`OPENING_P01_V009_END_40_63_REVIEW.mp4` 23.375s（40–43仅为锁定上下文），SHA256 `6291e4030d5ebdddb5bacfcab6c64af2b55fb72812a63caeeeb0c81247274808`。
- 对应Storyboard `OPENING_P01_V009_SHOTBOARD.jpg` SHA256 `4deb78a58476ee1d68326534c68457c9a50a52d54f06c96490611bce192cc932`，EDL JSON SHA256 `fd3e651a09efee44b621a61aaba316992e270b3d1b2527a84b5c01d3b438c58b`。
- 上述媒体只在Chat会话交付，**不将含版权原音的review MP4上传到公开 GitHub**；本报告保留审计元数据及候选状态。

## 4. Gate 与下一步
- **TECH PASS:** 已批准素材来源、音轨完整性、63.375s片长、帧数、音画封装与中段保留检查。
- **PO REVIEW PENDING:** 开头是否符合“原第二镜作首镜”；结尾关系镜是否解决情绪与声画衔接问题；完整63.375s艺术效果尚未审核。
- **PO FAIL:** 用户指出结尾依然情绪不对/镜头拖长/人际关系不成立时，仅在44.5–63.375s实证修正，26–43s不动。
- 无 Formal Video publication/registration；Story Shots 49、Audit Events 239、Formal Videos 3，P0.3 IN PROGRESS；Mac本地同步仍待真实终端证据。
