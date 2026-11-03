# 《诡舍·黑衣夫人》｜P01 INS-04 V002｜宁秋水在沙发后原位起身拍肩｜Work 单张正式修正指令

2026-11-03 · 状态：**REFERENCE BUNDLE 5/5 PASS / WORK SINGLE-CANDIDATE AUTHORIZED / PO VISUAL REVIEW PENDING / NO REGISTRATION / NO VIDEO**

## 1. 任务和审核失败事实

上一版正式生成的 `OPENING_P01_INS_04_NING_STAND_HAND_ON_JUN_SHOULDER_CANDIDATE_01.png` 因人物**空间连续性 FAIL** 被 Product Owner 否决：宁秋水原本位于三人座次的后方、沙发靠背后侧，却突然来到君鹭远侧前方、侵占白潇潇原在的左侧位置。不能仅因拍肩手势本身自然就认为场景通过。

上一版 V001 Bundle 和制图授权已撤回。上一版图 SHA256 `b00ba821f39f6348bfd30c458462e0b65359e4ccd441bb054f79cda51d1c8c24`，仅用于失败溯源，**禁止作为正向参考**。

本轮目标：在**宁秋水原本就在沙发后方**的空间约束下，修正同一个拍肩叙事动作，仅生成一张替代的未获批准候选，不改变七镜既有 Canonical。

阅读最新导演指令（取代旧V001）：
`docs/project_control/gates/P0_3_video_pipeline/OPENING_P01_INS04_REAR_SOFA_SHOULDER_TOUCH_DIRECTOR_V002_2026-11-03.md`

## 2. 本轮唯一有效 Reference Delivery Bundle

Repository: `wp5rrp7b2v-droid/black-lady-animatic-v01`

Bundle ID:
`OPENING_P01_INS_04_NING_REAR_SOFA_SHOULDER_TOUCH_REFERENCE_DELIVERY_BUNDLE_V002`

正式 Spec：
`production/bundle_specs/OPENING_P01_INS_04_NING_REAR_SOFA_SHOULDER_TOUCH_REFERENCE_DELIVERY_BUNDLE_V002.json`

GitHub Actions [Run 41579300322](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41579300322) **completed SUCCESS**，原始验证日志明确：
- `PASS: 5/5 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`

Artifact **13204063800**, name:
`OPENING_P01_INS_04_NING_REAR_SOFA_SHOULDER_TOUCH_REFERENCE_DELIVERY_BUNDLE_V002`

独立下载的原始 ZIP SHA256：
`957ea2dce9007d705f29d1e07d1599d640ff4e80c5e911c329c0675eea4ecb78`

### 5张直接正向参考（均原始精确核验 PASS）

| 参考 | 目的 | 维度 | SHA256 |
|---|---|---|---|
| PO Approved `P01_OPEN01` original scene JPEG | 第一权威：白左/宁中后/君右前、家具、沙发靠背与光向 | 864×1536 | `4ccebb6a903b9cbeac1dfdc2e8b05c7f5dafa05e31cff53e775dfa2f37945452` |
| Approved `P01_OPEN07` relationship PNG | 第二权威：相同三人空间轴线与后/前站位核对 | 941×1672 | `f63487a767d93dbb8bb10ef9eca36c45e6ffff39ca43f309150d805472645140` |
| AST_IMG_000060 Ning CHARACTER_REFERENCE_SHEET | 宁秋水已批准黑衣人物身份/身体比例 | 1440×1620 | `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be` |
| AST_IMG_000071 Ning FACE_3Q_LEFT | 宁秋水三分之四脸身份 | 941×1672 | `8d92bcc601220654499f7be57fc83411c57dedccc44e8f764cc65ce1b840334e` |
| AST_IMG_000057 Jun CHARACTER_REFERENCE_SHEET | 君鹭远已批准蓝灰衣人物身份与身体比例 | 1440×1620 | `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e` |

本轮 ZIP 共 `delivery_manifest.json`、`WORK_HANDOFF.md`、5张 JPEG/PNG 原件；Chat 实际下载后重新计算 **5/5 SHA256 + Git Blob + bytes + 图片格式尺寸 PASS**。Work 必须独立下载与重核，不能只相信此文字报告。

## 3. 只生成这一个新候选

**输出完整文件名：**
`OPENING_P01_INS_04_NING_REAR_SOFA_SHOULDER_TOUCH_CANDIDATE_01.png`

规格：**941×1672、9:16 原始 PNG，2.5D 半写实电影感**。不自动生成候选02，不生成替代画面组，不做动画。

### 构图—物理几何锁定

1. 先以P01_OPEN01批准画面重建空间轴：**左侧/前景白潇潇红睡裙，中央靠后宁秋水黑衣，右前坐着君鹭远蓝灰衣**。书架偏左，台灯中左，白色窗帘偏右，茶几为前景；沙发靠背位置不能被改画或消除。
2. **宁秋水从中后方沙发靠背后原位置起身并站直**，不是走到沙发前方；宁的髋部和腿仍在靠背后侧区域。身体可以略向前、向右倾，手从**后方越过靠背**触及君鹭远的**后侧近肩**。
3. **君鹭远保持在右前原位置坐着**，病弱、脸色苍白，受到肩膀触碰后自然微侧头看向身后宁秋水；不得改变座位、衣服或身体朝向到不可能角度。
4. **白潇潇仍在左侧原空间**；若五张正向参考不足以支持她完整脸部的身份精度，保留红衣衣角/模糊左侧坐姿即可，不要擅自增加别人的女性脸，也不能让宁占据她的位置。
5. 必须画出**清楚的沙发靠背作为前后深度边界**：宁在靠背后、君在靠背前。拍肩的手臂有连贯的肩→肘→腕→手结构，手掌自然贴在君的靠近宁的一侧肩部。不得穿过沙发、穿头颈、断臂、多手、多指或浮空。
6. 摄影机维持与已批准三人关系镜**同一空间轴侧**，只拉近成为中景/中全景，不得反打翻转左右位置；宁不是从君左前方扶住他的姿势。
7. 宁神情平静而坚定，嘴唇微启，视觉上表现他说出「我来带他吧」的瞬间；图上不得有对白字和口型动画。一张PNG只能证明接触状态，不能证明真实起身动作连续动画。

**硬失败条件：**宁依然到了前方/左边；两个男角色都坐着；无法从靠背后合理触肩；人物脸或衣装漂移；沙发、灯和视线轴线错乱；手臂穿模等。发现任一关键问题立即提交 FAIL，不要通过擅自让宁绕过沙发规避问题。

## 4. 交付与权限

仅输出这一张原始 PNG、下载链接、尺寸、字节数、使用的 Run/Artifact、视觉问题说明。完成后停止供 Product Owner 视觉审核。

原音剪辑仅作为后续参考，宁表态粗 Cue `00:32–00:35`，非逐字锁定，不在Work中编辑原声。

禁止 Canonical Publication、Story Shot登记、视频合成、更新Video Index或替换既有Approved静帧。PO批准的无人住宅入口 INS00 仍**待后续统一登记**，被拒绝的 INS01/INS02及本镜旧V001禁止纳入批准批次。

**本轮证明目标：**宁从批准位置**沙发后侧**站立并自然触及右前方仍坐着的君，构图轴线与两张已批准三人关系图一致，且具备可提交PO审核的真实原件。
