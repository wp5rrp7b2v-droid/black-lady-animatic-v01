# 《诡舍·黑衣夫人》S02-B V019 自由重构｜导演决议与 Work 连续执行指令 V001

日期：2026-10-18  
状态：**Product Owner 已授权自由重构的制作任务；本文是导演执行设计 / 候选设计，不代表新视频视觉批准。**  
执行仓库：`wp5rrp7b2v-droid/black-lady-animatic-v01`  
唯一工作分支：`feature/s02b-v019-directors-cut-20261018`  
**严禁合并 main、替换任何正式资产、标记 V019 已批准。**

## 1. 已核验源与目标

- 正式视觉参考 V018 全片，精确 SHA-256：`6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427`；路径：`production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4`
- 正式设计基础：`production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V002_RENDERED_RECONSTRUCTED_REVIEW.json`
- 新剪辑唯一机器状态源：`production/editorial_specs/S02_B_V019_DIRECTORS_CUT_EDL_V001.json`
- 源音轨：V018 原 AAC packets，**严格 copy，不重新混音、截断、变速或重配音**。
- 目标：1,927帧、30fps、720×1280、完整约64.23秒的单部审核版。PO 只审核最终完整视频。
- 已获准的画面顺序改动：`N21 → NEW-02 → N22 → N23`，保持不反复讨论。
- 暂停或停止的技术：空间脚步音效、浮尘/薄雾、暗场与叠化转场、重复拉近拉远、变形人物动画；本版本不恢复。
- 付费 AI 视频服务：禁止；允许依照项目既有 Work 静态 PNG 工作流，禁止增加付款依赖。
- V018 原有烛火动态只通过保留**已渲染进 V018 的帧**继承；不要宣称它已通过跨场景通用引擎验证。新增静帧无需额外模拟火苗。

## 2. 事实和导演判断

**FACT｜已实际检查**：V018 原视频 34 帧 Chronology Contact Sheet，路径：
`production/video_candidates/review/s02b_v019_directors_cut_preflight/S02B_V019_DIRECTOR_CHRONOLOGY_CONTACT_V001.jpg`

**FACT**：N16 的双人近景持续约9.37秒，N17 的宁秋水面部反应近景约12.57秒；N18 仍有6.03秒晴空观察，N20 之后已有更明显的 OTS、人物反应、群体内纵深及视角变化。

**INFERENCE｜待完成整片审片验证**：首21.9秒的相近人物构图是“连播图片感”的重要贡献因素之一，而不一定是所有问题的唯一原因。

**WORKING HYPOTHESIS**：仅替换3个功能明确的画面区间，能够提升前段镜头语言，不必继续高成本微特效探索。

## 3. V019 首轮导演决策（3个静帧，足够；不得无限增图）

时间均为 S02-B 本段起点计的本地时间，终帧 exclusive：

| 新镜头 | 帧范围 | 时长 | 原有画面被替换 | 叙事职责 |
|---|---:|---:|---|---|
| `D01_JUN_SISTER_QUESTION_LISTEN` | 164–280 | 3.90秒 | N16_PART_2 | 君鹭远听宁秋水回应姐姐的问题，显示关系和脆弱，不再重复整段双人照 |
| `D02_NING_WARNING_SPACE` | 426–518 | 3.10秒 | N17 中间 | 血门规则从抽象谈话变成宁秋水针对君鹭远的严肃提醒，显示二人空间关系 |
| `D03_JUN_LISTENS_LOOKS_OUTSIDE` | 519–657 | 4.63秒 | N17 后段 | 君鹭远接收警告、目光过渡向门外晴空，建立进入 N18 的视线承接 |

所有替换仅在 **V019 新候选** 内进行，不修改 N16、N17 等批准 PNG 原件或 V004、V018 旧版文件。

其余段落复用原 V018 对应帧，中段按已批准的 N21/NEW-02/N22/N23 顺序整理；后段 N23/A06/N24/N25/宁反应/N26 保持。

### D01｜君鹭远听回答
- 一张真正不同于原 N16 的**非合影式近景**，视觉锚点是君鹭远正在听宁秋水回答“不全是”，而非再口型表演整段对话。
- 君鹭远浅蓝衬衫外套、白色上衣一致；宁秋水深色外套，仅可在近前景形成自然的模糊肩膀/侧背。
- 机位从宁秋水附近观察君鹭远，表情自然、微带关注，不忧伤夸张、不宣传照。
- 门侧古堡内部，弱暖烛光/有限自然光一致；绝不把强烈日光当成棚拍主光。
- 建议参考 ≤3张：`N16_SISTER_QUESTION_APPROVED_V001.png`、`N17_BLOOD_DOOR_WARNING_APPROVED_V001.png`、`N18_CLEAR_SKY_DOUBT_APPROVED_V001.png`。
- 正式候选输出：`production/video_candidates/v019_directors_cut/assets/D01_JUN_SISTER_QUESTION_LISTEN_CANDIDATE_V001.png`

### D02｜宁秋水提醒
- 不再重复原 N17 一张脸的特写。采用中近景3/4侧拍，宁秋水在清楚的前/中景、君鹭远后退半个身位听，二人形成自然纵深与视线互动。
- 宁秋水说话嘴略微自然分开，双手不插袋；无过火训斥表情。二人都要与石地面、柱廊光线真实结合。
- 不制造背包、挎包、额外角色或动线错误。
- 建议参考 ≤4张：`N16_SISTER_QUESTION_APPROVED_V001.png`、`N17_BLOOD_DOOR_WARNING_APPROVED_V001.png`、`N19_CONDITIONS_CAN_CHANGE_APPROVED_V001.png`、`N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`。
- 正式候选输出：`production/video_candidates/v019_directors_cut/assets/D02_NING_WARNING_SPACE_CANDIDATE_V001.png`

### D03｜君鹭远应答后注意天气
- 机位进一步落在君鹭远侧背/3/4侧脸，让观众先理解他听完提醒，继而顺着眼神看到仍然晴朗的门外光线，随后切回正式 N18 晴空怀疑镜头。
- 必须是**摄影角度和主体安排明显不同的画面**，不是把 N18 原图裁切或换个亮度。
- 远处开门后的晴空可以适度可见，但门两侧均为城堡内部；外部蓝天只在门洞远端，不能大面积直射内部大厅。门保持对外敞开，不下雨。
- 宁秋水可以只以虚化肩背或暗色身影出现在后侧，不要求强行露脸。
- 建议参考 ≤4张：`N18_CLEAR_SKY_DOUBT_APPROVED_V001.png`、`N19_CONDITIONS_CAN_CHANGE_APPROVED_V001.png`、`N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`、`N21_COHORT_ENTERS_INSIDE_THE_FLOW_APPROVED_V001.png`。
- 正式候选输出：`production/video_candidates/v019_directors_cut/assets/D03_JUN_LISTENS_LOOKS_OUTSIDE_CANDIDATE_V001.png`

以上所有参考图均在：`production/image_library/approved/story_shots/`。请**真实读取原图**，不能仅根据文件名、文字说明或预览截图假定人物身份通过。

## 4. Work 自动连续执行契约（PO 不承担过程审批）

1. 先在 GitHub 读取上述 EDL、34帧接触表、正式批准 PNG、V018 精确源；验证分支与授权范围。原始素材只读。
2. 一次只生成 **1 张 PNG**，且每次输入图不超过 5 张；每张 **941×1672、9:16**。按 D01→D02→D03 顺序完成。
3. Work 在本次**完整导演版授权**下可连续内部审核、必要时内部重试（每件最多 2 次），无需每生成一张停下来问 PO。任何图身份、空间轴、身形、场景连续性明显失败时，不得把它上传到最终 `assets/` 指定位置。
4. 合格单张图上传至本分支的指定 `assets/` 文件名并在源素材中不修改任何已批准二进制。不得把未经核验的候选标注为 `APPROVED`。
5. Work 完成第三张并提交后，GitHub Actions workflow `s02b-v019-directors-cut-auto-render.yml` 自动合成 64.23秒完整审核候选。三个资产不齐时，不应渲染半成品或造假占位图。
6. 验证 `S02_B_V019_DIRECTORS_CUT_QC_V001.json` 机器 PASS：1927帧、30fps、原AAC packet SHA相同、3张 PNG尺寸/identity source复核、正式版不变。
7. Work 自主检查完整视频视觉关系。若有明显错误，最多围绕该异常进行定点修复（后续另起 V002 asset/EDL，避免覆盖 V001）；如无法稳定解决，请提交清晰阻碍说明，不伪称完成。
8. 最终交付**完整 MP4 + 1页简明镜头变更说明 + QC**，只请 PO 对整片做视觉审核。**不自动正式发表或合并 main**。

### Fail-fast 门槛
- 核对不出正式源 / 不能取得参考图 / PNG 身份明显漂移 → **STOP，报告具体依赖缺口**。
- 3个新静帧合格且渲染成功 → **TECHNICAL PASS**，可提交整片 PO 审核。
- PO 认为仍是相同图片感、故事提升不显著 → **VISUAL FAIL**，不扩展这一路线；继续保留已批准 V018。

## 5. 用户审批权与后续治理

- **新增镜头和 V019 完整视频均只是独立候选，未经 PO 审片不得登记 `Approved`。**
- V001、V006、V018 以及已有正式 Shot 原始二进制持续有效，严格 append-only。
- N23 V002 局部音效曾获认可是历史事实；空间音效全片推广已被 PO 叫停，V019 不使用。
- M01 跨 S 通用性必须等下一个 S 完成后验证，通过才正式定稿登记，不能因为本片继承 V018 就提前封版。
- **本分支不合并 main；不得建立新的 Master/Matrix/Register 以此代替实际出片。**

## 6. 完工验收

客观交付：`production/video_candidates/v019_directors_cut/review/S02_B_V019_DIRECTORS_CUT_FULL_REVIEW_V001.mp4`

对照基线：V018 精确二进制及已批准的 N21→NEW-02→N22→N23 重排局部。PO 最终只回答：**新版整段是否值得作为有效新视频迭代。**

机器 PASS 不等于艺术 PASS。没有完整视频，不得声称导演版已交付。
