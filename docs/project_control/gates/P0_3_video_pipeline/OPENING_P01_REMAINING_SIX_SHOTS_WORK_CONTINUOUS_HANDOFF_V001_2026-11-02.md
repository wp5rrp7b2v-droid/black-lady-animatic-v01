# 《诡舍·黑衣夫人》｜P01 后续六镜｜Work 一次性连续制图正式指令 V001

**Product Owner 执行授权：**2026-11-02「直接一次性P01后续的全部制图流程」。
**任务边界：**正式生成六张 P01 剩余镜头各一张 Candidate PNG，按 OPEN-02 → OPEN-07 顺序连续完成，不要每做完一张就要求用户重复批准；全部生成后一次性提交六张供 PO 视觉审核。此许可**不等于**任何候选视觉已 Approved，不授权 Canonical Publication/Story Shot Registry/视频母版替换/P0.3 Gate PASS。

## 一、先读权威导演设计

Repo: wp5rrp7b2v-droid/black-lady-animatic-v01
Director Plan: docs/project_control/gates/P0_3_video_pipeline/OPENING_P01_REMAINING_SIX_SHOTS_BATCH_DIRECTOR_AND_WORK_PLAN_V001_2026-11-02.md
Sound→Visual Cue Sheet: docs/project_control/gates/P0_3_video_pipeline/OPENING_192257_AUDIO_VISUAL_CUE_SHEET_V001_2026-11-02.md
Approved prior shot P01-OPEN-01 scene:
production/image_library/approved/story_shots/OPENING_P01_OPEN_01_THREE_PERSON_DECISION_ESTABLISH_APPROVED_V001.jpeg
Scene Anchor controlled manifest:
production/controlled_references/opening_p01_open01/OPENING_P01_OPEN_01_BAI_RESIDENCE_SCENE_ANCHOR_V001.manifest.json

**不可更改 Baseline：**
- 已批准紧凑原音192.257秒；P01在全片00:00开始，剩余本批画面接约00:04-01:03。上述秒数是近似Cue，不能声称已做词级精确EDL。
- 首镜是PO已批准 **864×1536 JPEG原始二进制**，不是941×1672 PNG，不得转码、重采样替换 Canonical 或改变 SHA。
- 首镜三人同一现实住所：白潇潇坐在画面左侧、红色睡裙；君鹭远右前、蓝灰外套、未签血门契约时身体仍虚弱；宁秋水后侧、黑衣。后续房间家具、窗户和光向连续。
- 白潇潇 approved C06 front/3Q-left 独立脸，不准将温倾雅或苏小小脸作其正向引用。其他人物分别使用已批准Identity Sheet。场景JPEG只控制 **空间/构图/服装连续性**，不高于人物Identity Master。

## 二、六个正式 GitHub Actions 验证 Bundle

每个 Bundle 都已经在 GitHub Actions 实际 SUCCESS、产生独立Artifact，并经 Chat 独立下载后对所有Reference PNG/JPEG逐字节重算SHA-256、Git Blob、尺寸及manifest一致性通过。

| 顺序 | Shot / 候选名 | Bundle ID | Actions Run | Artifact ID | 参考数 |
|---|---|---|---|---|---|
| 02 | OPENING_P01_OPEN_02_JUN_RESOLVE_CANDIDATE_01.png | OPENING_P01_OPEN_02_JUN_RESOLVE_REFERENCE_DELIVERY_BUNDLE_V001 | 41389184689 | 13116697397 | 3/3 |
| 03 | OPENING_P01_OPEN_03_BAI_CAUTION_CANDIDATE_01.png | OPENING_P01_OPEN_03_BAI_CAUTION_REFERENCE_DELIVERY_BUNDLE_V001 | 41389189620 | 13115898648 | 4/4 |
| 04 | OPENING_P01_OPEN_04_NING_VOLUNTEERS_CANDIDATE_01.png | OPENING_P01_OPEN_04_NING_VOLUNTEERS_REFERENCE_DELIVERY_BUNDLE_V001 | 41389193290 | 13116895544 | 5/5 |
| 05 | OPENING_P01_OPEN_05_JUN_GRATEFUL_CANDIDATE_01.png | OPENING_P01_OPEN_05_JUN_GRATEFUL_REFERENCE_DELIVERY_BUNDLE_V001 | 41389232188 | 13116244660 | 4/4 |
| 06 | OPENING_P01_OPEN_06_JUN_BURDEN_CANDIDATE_01.png | OPENING_P01_OPEN_06_JUN_BURDEN_REFERENCE_DELIVERY_BUNDLE_V001 | 41389235686 | 13115684617 | 4/4 |
| 07 | OPENING_P01_OPEN_07_DECISION_CLOSE_CANDIDATE_01.png | OPENING_P01_OPEN_07_DECISION_CLOSE_REFERENCE_DELIVERY_BUNDLE_V001 | 41389239263 | 13116900086 | 5/5 |

Each spec is located at: production/bundle_specs/{Bundle ID}.json
Each Actions ZIP contains delivery_manifest.json, WORK_HANDOFF.md and exactly N direct reference files. No manual PO uploads are required.

**Exact downloaded archive SHA-256 for troubleshooting (ZIP identities, not image identities):**
- 02: 1f0a6159aa5123b33860c16d2f68433dedab693c816c0d9eefe2fbe0cea1a58d
- 03: 98cc5045f826abb6b6acba694ae0663854ee2fee258f922956baa58616818246
- 04: 4d1a6fd517851cee20a1ef7c98d657d087c973ba19f52a57dfcd9942431ac34c
- 05: 6718d9061b86e9c5bc3113db61277f0c9e13c57ba07140b431d9afadef4b2fcb
- 06: 0ba4d7e72b01b888c3ffd166f7d60ce1c7827241c24fddcf04cbf978d4089141
- 07: c88c6fe2db88d938253ed08a9a0baa7c3cc9134a80671843060b60603b075789

## 三、连续导演任务

**02（约00:04–00:19）君鹭远的决心：**沿首镜从君鹭远右前自然推进，中近景，病弱但神态坚决，眼睛朝白潇潇，不拍成康复者英雄写真。
**03（约00:19–00:32）白潇潇的警告：**白潇潇左侧座位3/4侧前中近景，认真、理性、担忧；保留君鹭远肩影建立视线，不要单纯美颜特写，保持她的红色睡裙与C06脸。
**04（约00:32–00:40）宁秋水主动陪同：**原后侧黑衣宁秋水进入镜头主位，平静、自然、坚定；前景有君鹭远肩影，勿提前演绎成大悲大喜、握拳或站队。
**05（约00:40–00:48）君鹭远感激：**换为看向宁秋水的相对近景，感激笑容短暂、克制略苦；与02的表情/视线方向区别明显。
**06（约00:48–00:58）君鹭远担忧牵连：**比05更侧向、安静的关系镜，笑意消退，Jun前景、宁秋水中景，双手自然搭膝；不得复刻05同一张近景只换嘴角。
**07（约00:58–01:03）准备签约：**三人在同一现实客厅、不同于首镜机位的较宽关系镜，表达危险决定已经做出；不要提前显示血门、巴士、诡舍，维持真实生活场景。

风格：2.5D半写实动画电影感，9:16，目标941×1672 PNG；自然错位，光照一致，不插袋、不背包、不摆拍。保持高质量人物面部和手部。**每个镜头只生成一张，不自动生成第二版**。

## 四、工作执行纪律

1. Work 从上述六个 GitHub Actions Artifacts 下载参考包；逐一核对 manifest 内容与参考图片字节，尤其其中的Approved原始JPEG。
2. 不得以个别图片缺失为由随意换图或删减正式场景Reference；如有Bundle失效、权限、下载或哈希问题，报真实阻塞，不虚构PASS。
3. 严格按02→03→04→05→06→07顺序生成。前一张完成后可以自动进入下一张，**无需每张生成后停下请求PO批准**。禁止未经授权一次生成多张备选/无限重试。
4. 每张候选为独立原件。若单张出现角色撞脸、空间混乱或技术异常，记为FAIL、不要作为后续镜头Reference；仍可在不污染输入的前提下继续其余镜头。对真实共用输入错误必须停止全批。
5. 全六张完成后，给出顺序总览+六张原图+完整文件名/尺寸/来源；PO可以按镜头分别批准/返修。Work不得宣布Approved、操作Canonical/Registry、修改已批准Opening母版或任何原始音轨。
6. 不重新启动旧血门A/B项目；不得切换Codex完成这个纯Story Shot制图任务。

**验收终点：**6张独立Candidate（或明确报告哪些镜头FAIL及原因）+ 单次统一交PO视觉审核；正式图像资产落档只在各张PO视觉批准后由Chat接续。
