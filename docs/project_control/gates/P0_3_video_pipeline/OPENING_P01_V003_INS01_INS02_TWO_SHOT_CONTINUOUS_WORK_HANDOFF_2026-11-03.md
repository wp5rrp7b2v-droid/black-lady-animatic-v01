# 《诡舍·黑衣夫人》｜Opening P01｜新增室内补镜 INS01 / INS02｜Work 连续制图交接 V001

日期：2026-11-03

状态：**REFERENCE DELIVERY 2/2 VERIFIED / WORK TWO-CANDIDATE GENERATION AUTHORIZED / PO VISUAL REVIEW PENDING / REGISTRATION DEFERRED**。

## 0. 授权、状态和不可变更的事实

PO 在看到无人住宅入口 INS00 后表示「这张批准，先不登记，继续制作其他需要增加的，后面再一起登记」，之后要求「继续」。因此：
- INS00 的 PO 视觉批准仅限用户展示的那一张无人住宅入口原图；**明确延后 GitHub Canonical 发布、Story Shot 登记及批量登记工作**。
- INS00 用户上传的实际审核 PNG：`OPENING_P01_INS_00_RESIDENCE_GATE_ESTABLISH_CANDIDATE_01(1).png`，本会话本地核验：941×1672，2,152,581 bytes，SHA256 `9f5b55574e417c002aab20472277f6b413b50be06106c23e95bb520bb70b21e7`。**此文件尚未以原件形式上传到 GitHub**，哈希记录不等于 GitHub Exact Binary Verification 或登记；晚些时候批量登记应回收此 exact binary，不能偷换成图片预览/重编码版本。
- 现有七张 P01 OPEN01–07 已获批并正式登记；GitHub Story Shot Index 总量仍为42，官方 Video Index 3。
- PO 要求继续新增有独立叙事功能的画面。按已提出并验证的最小方案先完成两张室内关系补镜，不扩大到第三张手部图，不新创室内外空间，也不改原音和原有已批准静帧。
- Chat 内此前展示的三张示意/预览画面只是未核验的构图候选，不作为身份或空间正向生图参考，不因展示或“继续”自动晋升 Approved。

## 1. 必须优先阅读的正式导演设计

`docs/project_control/gates/P0_3_video_pipeline/OPENING_P01_V003_NEW_COVERAGE_SHOTS_DIRECTOR_DESIGN_DRAFT_2026-11-03.md`

仓库：`wp5rrp7b2v-droid/black-lady-animatic-v01`。

来源连续性：
- P01 已批准住宅场景锚点：`production/image_library/approved/story_shots/OPENING_P01_OPEN_01_THREE_PERSON_DECISION_ESTABLISH_APPROVED_V001.jpeg`。**它只作室内家具、光照、窗户、站位、服装参考，不是独立人物脸 Master。**
- 白潇潇：approved C06 FACE_FRONT AST_IMG_000109 和 FACE_3Q_LEFT AST_IMG_000110；不得正向引用温倾雅、苏小小。
- 君鹭远：approved reference sheet AST_IMG_000057；灰蓝上衣，身体病弱。
- 宁秋水：approved reference sheet AST_IMG_000060 和 FACE_3Q_LEFT AST_IMG_000071；黑衣。
- 沿用同一住宅客厅窗/沙发/茶几/光线。红睡裙白潇潇位于左侧座位，君鹭远在右前，宁秋水在后侧；三人不能不合逻辑地换位。
- 2.5D半写实电影感，9:16，941×1672 PNG，无摆拍/插袋/背包/古堡/血门/幻觉。

## 2. GitHub Actions 已构建并通过独立下载的两个正式 Bundle

| 按序 | 待出 Candidate | Bundle ID | GitHub Actions SUCCESS | Artifact ID | 直接参考 |
|---|---|---|---|---|---|
| INS01 | `OPENING_P01_INS_01_BAI_JUN_REVERSE_EXCHANGE_CANDIDATE_01.png` | `OPENING_P01_INS_01_BAI_JUN_REVERSE_EXCHANGE_REFERENCE_DELIVERY_BUNDLE_V001` | [41563717089](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41563717089) | `13198277638` | 4/4 |
| INS02 | `OPENING_P01_INS_02_NING_JUN_RESPONSE_TWO_SHOT_CANDIDATE_01.png` | `OPENING_P01_INS_02_NING_JUN_RESPONSE_TWO_SHOT_REFERENCE_DELIVERY_BUNDLE_V001` | [41563734933](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41563734933) | `13197158143` | 4/4 |

已独立下载并在 Chat 工具环境重算两个 ZIP 内所有来源的SHA256、Git Blob、尺寸（对PNG）和字节数：**PASS 2/2 Bundles / 8/8 actual reference entries**。注意共享原件重复参与不同镜头，非八张独立人物资产。

- INS01 下载 ZIP SHA256 `6178c93cbd5e35d7d87ddf6237307aa7c89057dd9d7113957297674fd2f3cc3f`；内容一张 JPEG 室内场景锚点、两张白潇潇身份原图、一张君鹭远参考表、`delivery_manifest.json`、`WORK_HANDOFF.md`。GitHub Actions 日志 `PASS: 4/4 exact canonical reference binaries verified`, `GENERATION_ALLOWED=TRUE`。
- INS02 下载 ZIP SHA256 `cf1c2cf76077bfb845e0797d60a65aa37f5274d320726d851f1a3ee3c8b64a4e`；内容一张 JPEG 室内场景锚点、两张宁秋水身份图、一张君鹭远参考表、`delivery_manifest.json`、`WORK_HANDOFF.md`。GitHub Actions 日志 `PASS: 4/4 exact canonical reference binaries verified`, `GENERATION_ALLOWED=TRUE`。
- 每个 Bundle 内原图对 `delivery_manifest.json` 各自匹配，Work 必须复验，不得以本交接记录代替原件下载。
- 两份正式 Spec 分别位于 `production/bundle_specs/<Bundle ID>.json`，`build_authorized=true`、`work_generation_authorized=true`，仅为这次一图一个候选的 Work 制图授权，**不授权登记**。

## 3. Work 连续执行要求

**INS01：白潇潇与君鹭远反打关系镜（原音近似23–30s）**

1. 从君鹭远右肩附近以真实客厅空间和透视关系反打白潇潇。白潇潇坐左侧沙发，红色睡裙，C06本人脸，正对病弱君鹭远解释必须有人陪同/危险条件；前景保留君鹭远蓝灰肩部与模糊侧影，脸不需要再呈现。
2. 要有明显区别于现有OPEN03单人警告图的双人视线与茶几空间；不生成白潇潇的另一张人物写真，不改变原房间布局。
3. 只生成 `OPENING_P01_INS_01_BAI_JUN_REVERSE_EXCHANGE_CANDIDATE_01.png` 一张。

**INS02：宁秋水与君鹭远双人回应镜（原音近似34–40s）**

1. 从白潇潇左侧座位附近向沙发右侧横向拍摄，宁秋水黑衣轻微前倾、平静提出陪同，灰蓝衣的君鹭远稍显苍白、自然看向宁秋水。
2. 两个男角色须保持不同批准身份、动作与空间层次，不可让宁秋水和君鹭远撞脸、夸张摆姿势。白潇潇可以只以极少红衣模糊前景暗示在场，不要生成可辨识的人脸。
3. 只生成 `OPENING_P01_INS_02_NING_JUN_RESPONSE_TWO_SHOT_CANDIDATE_01.png` 一张。

**连续性纪律：**按 INS01→INS02 顺序，工作中不要一张一停或每步向 PO 重复提问；若某一镜身份/空间 FAIL，标记该镜 FAIL，不把失败图当下一镜 reference。两个镜头都优先用各自已核验正式 Bundle，不基于上一步新生成的候选重新作人物母图。

## 4. 验收边界

Work 提交 **2张独立原始PNG及尺寸、文件大小、生成源 Bundle、失败原因（如有）**，一次性供 PO 审核。不得在 Work 中自行声明 PO Approved 或向 `production/image_library/approved/` 上传。

**PASS：**每张人物身份、住宅几何与既有七图一致，两种机位承担不同叙事职责、增强对白/回应的观感。**FAIL：**撞脸、空间漂移、只是旧图微裁切/重复正脸写真、人物站位扭曲。

若2张 PO 实际审核认可，再制订局部音画A/B，只有声画带来的改进通过PO后才考察手部插镜是否值得另做。批量Story Shot正式发布登记按PO“后面再一起登记”的约束继续 HOLD。

此阶段结束后能证明的是两个新候选图是否达标，不是整个P01开头成片已获批准。
