# 《诡舍·黑衣夫人》｜Opening P01→P02 D01–D03｜PO 视觉批准及正式二进制入库 Gate

日期：2026-11-17
状态：**3/3 PRODUCT OWNER VISUAL APPROVAL CONFIRMED / 2/3 EXACT ORIGINAL PNG LOCAL PREFLIGHT PASS / 1/3 SOURCE FORMAT MISMATCH / GITHUB CANONICAL PUBLICATION BLOCKED / STORY SHOT REGISTRATION NOT STARTED / P0.3 IN PROGRESS**

## 1. 本轮 PO 选择（已获准、不可自行替换）

Product Owner 在当前对话中明确指出「这版01｜诡舍外观可以通过」，随后对经修订的 02｜三楼环境、03｜木门回复「三个镜头都通过，完成登记」，并再次要求「按照我们既定的流程完成登记」。

视觉导演基线：`OPENING_P02_D01` 漆黑而有人居住气息的别墅外观 → `OPENING_P02_D02` 低调整洁、空旷而神秘的三楼环境 → `OPENING_P02_D03` 同空间封闭旧血色木门；推镜由远及近、由外入内。诡舍≠艾伦古堡≠莫妮卡庄园。不得提前制作任务血字，不改 P01 V018。

## 2. 原始文件本地读取与独立核验（FACT）

| Shot | PO 选择的原图文件名 | 容器实际格式 | 实际尺寸 | 字节数 | SHA-256 | Git object blob SHA-1 |
|---|---|---|---:|---:|---|---|
| D01 | `a_cinematic_realistic_moody_nighttime_scene_in_v.png` | **WEBP / RIFF，文件名误用 .png** | 940×1672 | 1,787,658 | `4b36a7579fcf108885e225e5c092d91992a160338f59145475f032fbe02800e9` | `369a9b37f2315d6f551d3095788bfc132f9dd555` |
| D02 | `第三层尽头的沉静木门.png` | PNG（签名有效） | 941×1672 | 1,645,509 | `4098fc1fe5af158b459b2d2575ccbd4db648a4fee6ce8b05f6eb69f3d58b51dc` | `837a62335fccdcef5c076ddd2313a42127846310` |
| D03 | `暗红旧门_幽邃别墅的静默守望.png` | PNG（签名有效） | 941×1672 | 1,805,752 | `f1c706e7ed60accf169e75a8b1d131974489c438bf179b093847ec3860fd43c3` | `75dd1c13fdf31a4794c9a8f5dd10aff101ee3811` |

文件均由当前会话附件真实物理路径读取，通过 PIL 识别、字节长度、SHA-256 和 Git object SHA-1 算法重新计算。**关键反证**：此前回答把 D01 称为有效 PNG 是错误的，不能继续沿用此事实断言。D01 的 940px 宽度不是文件格式错误，也不被擅自拉伸到 941px。

## 3. D01 原图与无视觉变化的 PNG 修正候选

- 本地另行制成 `OPENING_P02_D01_GHOST_HOUSE_EXTERIOR_CONVERTED_PNG_REVIEW.png`，是从原始 WEBP 的已解码 RGB 像素转存的 PNG；图像尺寸 940×1672，**逐像素 RGB bytes 相等 PASS**。
- 新 PNG：2,339,571 bytes；SHA-256 `7732555dde7f3395f08854b9f56ea3e857a4e58248dec3c2ce108b76b6f44dde`；Git blob SHA-1 `66e561b3a23f0356db55239a8d2c6de22d62afc2`。
- **审批范围差异**：PO 已批准的源图确实是 WEBP 原始字节，转换版虽逐像素一致，**不是相同的原始二进制**。按原 Story Shot SOP 的“原始 PNG / no re-encode”规定，不自动将转换版判为已批准 canonical。转换候选需明确新的二进制采用裁定，或由 Work 依正式 Bundle 产生可获批原生 PNG。
- 本地输出的准备包 `P02_D_APPROVAL_INTAKE_PENDING_REGISTRATION_20261117.zip` 含 D01 原始 WEBP（真实格式命名）、D01 PNG 修正版候选、D02/D03 精确原始 PNG、README JSON；它不是 GitHub Canonical 存储，也不是 CI 证明。

## 4. 正式登记 Gate（必须 FAIL-CLOSED）

权威 SOP：`docs/project_control/gates/P0_3_video_pipeline/story_shot_production_registration_sop_v1.md`。正式完成必须同时满足 PO Approved / Canonical Binary PUBLISHED / Index Registered / Independent Registration Verification PASS。

**当前缺口：**
1. 原始图当前存在于对话附件工作环境，而非 GitHub `staging/story_shot_candidates/` 或 `production/image_library/approved/story_shots/`；GitHub create_file/create_blob 不具备直接读取容器内图片的路径能力。**不得虚构 GitHub blob 已创建、Actions 已运行或 Canonical 已发布**。
2. D01 源为 WEBP 而非 PNG。须对转换版获得明确的二进制采用授权后，才能按 PNG intake 对其运行独立 CI。
3. 本轮三张图由 Chat 概念图工具输出，尚无可证明的正式 GitHub Actions Reference Delivery Bundle → Work 生成来源。当前项目锁定的 Story Shot 制图流程仍须检查该来源边界；PO 对图像的视觉通过并不自动伪造 Work provenance。

**Counts remain unchanged**：Story Shots 49；Audit Events 239；原视频索引维持 5 条历史 APPROVED、4 条 CURRENT；P0.3 Gate = IN PROGRESS。不得提前写入 `production/story_shots/story_shot_index.jsonl`，不得将 Po approval 记录冒充三张正式 Story Shot。

## 5. 最小解除阻塞路线

- 将原始两张 PNG 与获正式采用的 D01 PNG 上传一次到既有 GitHub staging intake 路径（已批准输出原件上传属 SOP Step5，非人工上传 Reference）；无需再设计镜头。
- 由现有 candidate intake verifier 或最小 exact CI 验证尺寸、签名、字节、SHA-256、Git blob；核对 Work/Bundle 来源要求，若未满足则按流程补齐/记录有权限的独立决议，不能假填。
- Gate PASS 后 Chat 执行 Canonical exact-blob publication、3 条唯一 Story Shot Index、对应 audit events、独立 CI/回读，最后更新 Project Control 和 Dashboard。
- 当前事实没有 Mac 本地 HEAD/同步日志，不声明 local sync PASS。

**本阶段实际证明**：已锁定三张 PO 选定视觉作品的身份，查出 D01 文件格式错误，验证一个逐像素等价的 PNG 候选，以及 D02/D03 两个有效 PNG 原件；**尚未证明 GitHub 侧正式入库与登记闭环**。
