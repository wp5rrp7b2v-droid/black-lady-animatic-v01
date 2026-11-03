# 《诡舍·黑衣夫人》｜Opening P01 V005｜白潇潇 INS-05 / INS-06 双镜连续制图正式交接

日期：2026-11-03

状态：**DIRECTOR DESIGN LOCKED / BOTH REFERENCE DELIVERY BUNDLES SUCCESS / EXACT 10/10 VERIFICATION PASS / WORK CANDIDATE PRODUCTION AUTHORIZED / PO VISUAL REVIEW PENDING / NO REGISTRATION OR VIDEO**

## 一、Product Owner 授权及精确范围

PO在连续审看片段后要求缩短无人住宅入口、对白白潇潇多一些真实动作与神态变化，并表示「先准备制作这两张」。本次为两张动作补镜的前置 Director→Bundle→GitHub Actions 生产准备及 Work 交接。**本文件授权 Work 按已验证各Bundle各生成1张原始PNG，但不代表任何生成结果已通过视觉审核。**

**第一张 INS-05**：
`OPENING_P01_INS_05_BAI_RESTRAINING_GESTURE_CANDIDATE_01.png`

**第二张 INS-06**：
`OPENING_P01_INS_06_BAI_FORWARD_WARNING_EXPLAIN_CANDIDATE_01.png`

均为独立 **941×1672、9:16、PNG**，一次按 INS05→INS06 连续完成，然后统一提交 PO。不得借口每张审核单独停止或自行生成多个备选。

### 正式导演设计

`docs/project_control/gates/P0_3_video_pipeline/OPENING_P01_V005_BAI_ACTION_TWO_SHOTS_AND_SHORT_GATE_DIRECTOR_V001_2026-11-03.md`

须在制图前完整阅读，以其为两张的导演与空间连续性权威。

## 二、正式 GitHub Reference Delivery 输入

Repository：`wp5rrp7b2v-droid/black-lady-animatic-v01`

| 镜头 | GitHub Actions Run | Artifact ID | Bundle ID | 独立验证 |
|---|---:|---:|---|---|
| INS-05 劝阻手势 | [41586133347](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41586133347) | `13207768479` | `OPENING_P01_INS_05_BAI_RESTRAINING_GESTURE_REFERENCE_DELIVERY_BUNDLE_V001` | **5/5 PASS** |
| INS-06 前倾解释 | [41586137738](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41586137738) | `13208151660` | `OPENING_P01_INS_06_BAI_FORWARD_WARNING_EXPLAIN_REFERENCE_DELIVERY_BUNDLE_V001` | **5/5 PASS** |

两次 GitHub Actions 结论均为 completed/success，日志明确：
`PASS: 5/5 exact canonical reference binaries verified`；
`GENERATION_ALLOWED=TRUE`。

Work须下载**各自** Artifact 并打开 `delivery_manifest.json`、`WORK_HANDOFF.md`，逐一核验图像原件，不得省略。

经 Chat 自 GitHub Actions 实际下载 ZIP，在本地再次用独立脚本解析manifest，并对每份图像重新计算 SHA256、Git Blob、字节数、PNG/JPEG签名和尺寸：

- INS05 ZIP `P01_INS05_BAI_RESTRAINING_BUNDLE_V001.zip`：8,880,807 bytes；SHA256 **`3ddb095fcb208b2f151908fc7740d460dafef2e27735c761c761361c556229e1`**；5/5 PASS，ZIP CRC PASS。
- INS06 ZIP `P01_INS06_BAI_WARNING_BUNDLE_V001.zip`：8,773,995 bytes；SHA256 **`2cfefb9b631b081c2f0387ef2d56c2a2e116b07068e04d500f6b34a0a8981b63`**；5/5 PASS，ZIP CRC PASS。

每个Bundle拥有5个已批准直接参考，四项共用：
1. P01 OPEN01 PO批准原始JPEG，864×1536，为客厅**空间/光线/座位**锚点；不是白潇潇的脸Master；
2. 白潇潇 C06 FACE_FRONT Identity AST_IMG_000109；
3. 白潇潇 FACE_3Q_LEFT Identity AST_IMG_000110；
4. 君鹭远 Character Reference Sheet AST_IMG_000057，控制前景蓝灰衣和人物身份；

第五项分别不同：
- INS05: 已批准 `OPENING_P01_OPEN_07_DECISION_CLOSE_APPROVED_V001.png`，用于约束白左、宁中后、君右前的三人空间轴线。
- INS06: 已批准 `OPENING_P01_OPEN_03_BAI_CAUTION_APPROVED_V001.png`，用于约束白潇潇左沙发、红睡裙、照明，不得简单复制旧图作为“新动作”。

**Reference正向禁用项：**温倾雅/苏小小脸；已经PO视觉否决的INS01/INS02；旧站立INS04 V001/V002候选；Chat演示图及未核验截图。

## 三、必须显著不同的动作/情绪设计

### INS-05：开场白潇潇劝阻，约00:00–00:04

- 白潇潇仍坐在**画面左侧原沙发**，红色睡裙。靠扶手自然转身面对右前方的君鹭远。
- **一只手从扶手抬起，掌心微向外或下方**，形成明确但克制的“不要冒险/先想清楚”动作，另一手留在膝盖或扶手。
- 神态是**担忧、微蹙眉、眼神关切**，嘴唇自然微启；不怒吼、不哭泣、不摆拍。
- 有沙发扶手、部分茶几；君鹭远仅可为右前方**蓝灰色虚化肩膀**，不要再新增面孔。人物身体动作必须能被读出，避免做成白正脸美颜特写。
- 推荐镜位：自然左侧3/4中景。

### INS-06：中段白潇潇解释危险/同行条件，约00:19–00:31

- 白潇潇仍在相同左侧沙发、同一红睡裙/同一C06脸，但**比INS05明显前倾**，一只手放膝自然支撑身体，**另一只手掌心微朝上向君鹭远自然摊开**，表现理性说明风险与条件。
- 神态从开头焦急担忧转为**冷静、审慎、坚定**；不要重复INS05的劝阻掌。
- 镜位相较INS05**略低更侧**，有真实茶几/沙发空间和对话视线，明显不同于已批准OPEN03中的警告特写。
- 后期用INS06与OPEN03等V002多景别镜头交替，不让这张新图一停就是12秒。

### 统一场景锁

白潇潇左、君鹭远右前、宁秋水中后；家具、书架、台灯、沙发、窗向及暖暗室内光照和Approved P01 OPEN01/OPEN07一致。2.5D半写实动画电影感，人物自然错位。动作是**静态关键帧**，不冒称已生成完整抬手或前倾动画。

## 四、制图执行纪律

1. Work先完整阅读本交接及正式导演V001，下载两个已验证 ZIP。
2. 逐个对照Manifest复验**5/5**参考图的 SHA256、Git Blob、bytes、格式及尺寸。
3. 先生成 INS05 一张，随后无需再次询问用户直接生成 INS06 一张，两图分别取用自己的正式Bundle，**不得用INS05新生候选反哺INS06**。
4. 若图片出现撞脸、沙发位置错乱、浮空手、手指多余、动作不明确、换衣等，标识具体 FAIL，不自动生成多个版本修补；共用输入损坏则停止并报告。
5. 完成后提供两张**原始PNG可下载文件**、按顺序的预览、像素尺寸、字节数、与各自 Run/Artifact 来源。
6. 不制作音视频、不编辑 192.257s 原音、不主动发布、不注册 Story Shot、不更新 Canonical Project Control Gate、不宣告PO视觉批准。

## 五、PO后续验证

需要 PO实际审阅两张候选动作是否确有不同、脸/服装/空间连续、手部正确。若两张都PASS，Chat才进入最小开头00:00–~00:10与白潇潇说话00:19–~00:31两段的A/B剪辑。

**视频后续创作方向仍未锁EDL**：无人住宅入口从旧5.875秒压缩试剪到约1.5–2秒，然后切 INS05白潇潇劝阻，再按真正声音切已批准OPEN02君鹭远单人；第二张INS06用在约19–31秒。严格保留**V002多景别快切+轻推进**风格与原音时间顺序，直到PO审片。

**登记HOLD**：PO已批准INS00无人住宅入口和INS04轻搭肩原始PNG，但明确不在本轮登记；旧INS01、INS02及INS04站立失败图不得进入日后批量审批注册。正式Story Shot Index仍42；Formal Video Index 3；P0.3 IN PROGRESS。
