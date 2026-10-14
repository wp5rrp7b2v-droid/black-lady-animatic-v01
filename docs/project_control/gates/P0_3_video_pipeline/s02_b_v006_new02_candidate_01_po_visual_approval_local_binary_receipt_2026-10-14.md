# 《诡舍·黑衣夫人》｜S02-B V006 NEW-02｜Candidate 01 PO 审批与原始 PNG 身份落档

Date: 2026-10-14

**GATE STATUS: PO VISUAL APPROVAL = PASS / CHAT ORIGINAL PNG BINARY VERIFIED / GITHUB STAGING PNG PENDING / NO CANONICAL PUBLICATION, REGISTRATION OR VIDEO CHANGE.**

## 1. Product Owner 决定

2026-10-14 用户针对 **V006 NEW-02 人群内部侧向机位 Candidate 01** 上传单张原图并直接批准：「批准该图」。

镜头任务：`S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`

作用：在已批准 N22 与 N23 之间引入人群内部近景遮挡、纵深错位步态和阴暗石拱廊侧向机位，以不同摄影机位置改善 V006 的镜头语言。

PO 批准的是已上传的**具体原始 PNG**，并不授权 Chat 或 Work 重生图、自动迭代、修改图片、发布 Canonical Story Shot、登记 Story Shot、剪辑视频或合并 main。

## 2. 原始批准 PNG 本地二进制核验

- 原始上传文件：`城堡幽暗拱廊中的穿行人群(1).png`
- PNG signature：**PASS**。
- PIL 解码完整性验证：**PASS**。
- Image mode：`RGB`
- 尺寸：**941×1672**
- 原始字节数：**1,963,410**
- SHA-256：**`d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`**
- Git blob SHA-1：**`d8feba3692ebe25afd0e51f5e3ab32358ea19ded`**。
- 未调整像素、未截图、未重新编码、未改变 PNG 字节。

## 3. 来源 Bundle

- `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
- 5/5 Validation-only：Run `38551894857` **PASS**。
- 正式 5/5 Bundle：Run `38553600591` **SUCCESS**。
- Artifact ID：`11887079610`。
- Artifact SHA-256：`f3bf0ca2f4de860a4c47ba7276ff2b8653196c0bc1a747a5fbdfb8b9d9f084b7`。
- N21 原批准尺寸 941×1671 已保留在上游参考，不影响本轮新图 941×1672。

## 4. GitHub Candidate Intake 门槛

- Repository：`wp5rrp7b2v-droid/black-lady-animatic-v01`
- Branch：`review/s02b-jun-nod-insert-20261014`
- 交付 Spec：`production/candidate_delivery_specs/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_CANDIDATE_01_DELIVERY_V001.json`
- 暂存目录：`staging/story_shot_candidates/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01/`
- 唯一候选 PNG 可保留原名 `城堡幽暗拱廊中的穿行人群(1).png`；若 GitHub 自动去除 `(1)`，也可用 `城堡幽暗拱廊中的穿行人群.png`。两个文件名都只能对应同一个批准原始 SHA / Git blob，且一次只能上传一张。
- 专用工作流：`.github/workflows/s02b-v006-new02-po-candidate-intake-v001.yml`。
- 工作流对准原始批准 SHA256/bytes/Git blob/941×1672 执行 Exact Intake；文件名别名仅在 Runner 临时工作区选择并验证，不改变已提交的 PNG 文件或通过新图代替批准图。

**当前 GitHub staging 原始 PNG 尚未完成独立核验。本收据不能冒充 Candidate Intake PASS。**

## 5. 下一步骤和禁止操作

等待原始 PNG 上传到 GitHub staging → Exact Candidate Intake workflow PASS → 单独 PO 授权 Exact Binary Canonical Publication、Story Shot Registration 与 Registration Verification（不会在图片上传后自动执行）。

- 不再生成 Candidate 02。
- 不修改任何 N21/N22/N23、NEW-01、母版或音轨。
- 不改变原始 PNG。
- 不自动发布、登记或合并 main。

**当前结束在：PO APPROVED / ORIGINAL CHAT FILE VERIFIED / AWAITING GITHUB EXACT INTAKE.**
