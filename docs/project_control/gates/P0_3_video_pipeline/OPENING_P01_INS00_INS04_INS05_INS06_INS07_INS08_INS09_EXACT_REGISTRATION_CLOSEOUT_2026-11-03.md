# 《诡舍·黑衣夫人》｜Opening P01｜2026-11-03 七张 PO 已批补镜｜Exact Binary Publication、Registration、Verification Closeout

Date: 2026-11-03
Status: **7/7 APPROVED ORIGINALS EXACT CANONICAL PUBLISHED / 7 UNIQUE STORY SHOT REGISTERED / INDEPENDENT GITHUB ACTIONS SUCCESS / PROJECT CONTROL R412 / P0.3 STILL IN PROGRESS**

## 1. Product Owner 原始授权与更正

Product Owner 在本会话已明确批准 INS-00住宅入口、INS-04轻搭肩膀、INS-05白潇潇抬手劝阻、INS-06白潇潇前倾解释、INS-07君鹭远坚定开口、INS-08君鹭远担忧欲言、INS-09君鹭远沉默纠结，并在2026-11-03要求将今日已批准、未登记的镜头**全部完成登记流程**。随后PO手动向GitHub `main` 同一Staging目录上传七张原图并确认。

**原件格式重大更正：**PO最终明确表示 `INS-05` 批准源是上传的 **PNG**，此前另一对话框将它误写为 JPEG。此更正取代此前的JPEG审批技术记录；此次只按**已上传、原样的 `红裙女子旁的沙发修复.png`**精确核验并登记，绝无把JPEG改名为PNG、无重新编码、无默许替换。INS-05实际源格式PNG 980×1605。

PO批准的原件规格不同于部分旧Work指令的目标941×1672，并不改变PO对这些具体原始图的视觉批准；严格保留原文件大小、像素和PNG签名。视频需要统一画布时，只能在派生剪辑层处理，不能更改正式图像资产。

## 2. GitHub 正式原始输入与七张精确身份

Staging（PO手工上传）：
`staging/story_shot_candidates/OPENING_P01_20261103_SEVEN_APPROVED/`

Canonical（原始Git Blob 直接复用）：
`production/image_library/approved/story_shots/`

| Shot | Staging原始文件 | 实际尺寸 | Bytes | SHA-256 | Git Blob SHA-1 | Canonical名称 |
|---|---|---|---:|---|---|---|
| INS-00 | `OPENING_P01_INS_00_RESIDENCE_GATE_ESTABLISH_CANDIDATE_01.png` | `941×1672` | 2,152,581 | `9f5b55574e417c002aab20472277f6b413b50be06106c23e95bb520bb70b21e7` | `2dc1a02c7b2adf75cd8a219f113de4b5914594d9` | `OPENING_P01_INS_00_RESIDENCE_GATE_ESTABLISH_APPROVED_V001.png` |
| INS-04 | `暖光下轻搭肩膀.png` | `941×1672` | 1,803,413 | `a9ca228f99f70b0ebf38852002b408808a2d43aceb184fdc918732d3e4abd96d` | `38c20bfaf0c7d71e035c4721ea100af20d770029` | `OPENING_P01_INS_04_NING_SHOULDER_TOUCH_APPROVED_V001.png` |
| INS-05 | `红裙女子旁的沙发修复.png` | `980×1605` | 1,969,960 | `1788b61943ed6b531fec0a7677e9f592713093671b1e134a10f822d428f8c219` | `e51c3b9fae09e89cd2a0387d257cef4ff2add25b` | `OPENING_P01_INS_05_BAI_RESTRAINING_GESTURE_APPROVED_V001.png` |
| INS-06 | `沙发后的中央黑衣男子.png` | `980×1605` | 2,034,228 | `1a93f9167781155c5706b26b5bc12ea2a29775a67ba1323eb3a99a4d24cdf1c0` | `76c3a4dd3c58457608dbbdfe7874b228f8382e6b` | `OPENING_P01_INS_06_BAI_FORWARD_WARNING_EXPLAIN_APPROVED_V001.png` |
| INS-07 | `窗边沙发上的轻声交谈.png` | `981×1602` | 2,003,846 | `51abced890798ab233782c6ffb8535b79127ffd4e0cb1c49698e121750cc9995` | `4d039789cf6e2338b0ea84d85a35464bec353dbb` | `OPENING_P01_INS_07_JUN_DECIDED_SPEAKING_APPROVED_V001.png` |
| INS-08 | `暖光书架前的温柔凝视.png` | `981×1602` | 2,000,337 | `585c9a051fc2ccb88e5a66fc666c48e71bd2a1f5f4df78aac057f2ca064b8683` | `78e78b2e8e9848977c4f4a36eb3f8585cb68c0ce` | `OPENING_P01_INS_08_JUN_WORRIED_TO_NING_APPROVED_V001.png` |
| INS-09 | `低头男子的淡白唇色.png` | `981×1602` | 2,073,345 | `1bd7a3b87e4980bd25eff9609b2754df12c7f739bfac4aa6c141d6a668178ffa` | `36c2a8c7f4fa2bf5fdb81cbeb0bcef210038f8e3` | `OPENING_P01_INS_09_JUN_CONFLICTED_SILENT_APPROVED_V001.png` |

七张独立Staging Git blob互不重复；Canonicals直接复用Staging已有原始blob。图片内容并未通过Chat生成、重采样或转换。JPEG并非这七张之一。

## 3. 实际完成的核验、提交与二次回归

- Pre-publication GitHub Actions [Run 41671115422](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41671115422) **SUCCESS**, `P01_SEVEN_PO_APPROVED_INTAKE_EXACT_PASS__7_OF_7`；检查七个原始Git Blob、文件大小、SHA-256、PNG签名和真实尺寸，其中INS-05 SHA-256在CI由上传的PNG直接计算为 `1788b61943ed6b531fec0a7677e9f592713093671b1e134a10f822d428f8c219`。
- GitHub Canonical发布、Story Shot Index与审计事件在同一Git树提交 [85eb2ca6c8718d4ce854240f969fa097fdc53ce7](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/commit/85eb2ca6c8718d4ce854240f969fa097fdc53ce7) 内完成：**42→49 Story Shots**，7条唯一APPROVED/CURRENT记录；审计事件 **218→239**，每张恰好3个事件（PO approval / exact publication / registration）。
- **登记后独立Actions [Run 41672117062](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41672117062) SUCCESS**，逐张重读原Staging与Canonical二进制确认字节完全一致，复核SHA-256、blob、格式、尺寸、registry元数据、7个唯一登记记录及21个审计事件，日志：`P01_20261103_SEVEN_EXACT_REGISTRATION_PASS__49_STORY_SHOTS__239_AUDITS`。
- 旧六镜OPEN-02→07独立回归工作流原先错误把全库条数写死为42，在总数增长至49后产生**非图像错误**；已将计数检查调整为至少42、保留六张原图全部精确二进制/索引检查，并通过 [Run 41672778647](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41672778647) SUCCESS：`OPENING_P01_02_07_REGISTRATION_EXACT_PASS__AT_LEAST_42_STORY_SHOTS__CURRENT_49`。
- 回归：原先OPEN01 JPEG、白潇潇C06正脸、左3/4及PROFILE_LEFT独立核验（Run 41672117087、41672116992、41672116866、41672116825）全部SUCCESS。
- GitHub具体Staging目录README是历史接收说明，提及旧INS05 JPEG处被PO新PNG更正取代，不能作为当前权威。正式镜头二进制权威由本报告的七原件和正式Story Shot Index确定。

## 4. 不因本次落档而改变的事实

- 已批准的P01 OPEN01–07七镜、其原始JPEG/PNG、白潇潇身份Reference、192.257秒原音均未修改。
- 原有正式Video Index仍3条；P01 V005/V006剪辑为技术测试，**尚未获得PO整段正式声画母版批准**。新增INS07–09虽PO批准静图，仍需要以原声实测两个局部段落A/B，不能自称已完成视频。
- 今日七张的审批/发布/登记已经完成，**不需再向PO要求重复上传或审批**。
- P0.3仍处于**IN PROGRESS**，不能因七张图片正式登记就升格全片Gate PASS。
- Mac本地同步仍未提供独立新HEAD证据；GitHub `main`为SSOT，收尾不表示Mac已同步。

## 5. 本阶段已经证明了什么、下一步

**FACT：**7/7 PO批准、7/7手工上传、7/7Git blob原样入库、7/7独立精确相等验证、49 unique APPROVED/CURRENT、239唯一审计事件；旧六镜及既有角色Reference回归全部PASS。

**UNKNOWN：**P01新表情镜与原音的词级说话起点、是否避免后段重复剪辑、整体V007音画的PO审片结论。

**Minimum next proof：**基于已经登记的7张原图与V006叙事版，分别针对君鹭远约00:04–00:19的坚定开口和00:40–00:58的担忧/纠结进行短片A/B，原声顺序不动，按实际PO听审决定是否继续；不要先大量新增镜头或未经批准升级正式Video。

Project Control revision R412 · Dashboard V331 · Entities 35 · Assets 111 · Story Shots 49 · Audit Events 239 · Formal Videos 3.
