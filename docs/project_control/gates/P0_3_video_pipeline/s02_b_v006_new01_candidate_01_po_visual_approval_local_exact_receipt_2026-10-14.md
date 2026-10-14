# S02-B V006 NEW-01｜Candidate 01｜PO 视觉审批与原始 PNG 本地身份收据

Date: 2026-10-14

**STATE: PO VISUAL APPROVED / USER ATTACHED ORIGINAL PNG VERIFIED LOCALLY / GITHUB STAGING EXACT INTAKE PENDING / NO CANONICAL PUBLICATION / NO STORY SHOT REGISTRATION.**

## PO 决定及镜头职责
Product Owner 于用户上传单张图片时明确说：**“这张为批准图”**。这仅批准本次单独生成的镜头图像，不自动授权剪辑母版更新、正式出版或登记。

- Shot task: `S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01`，Candidate 01.
- 镜头：君鹭远肩后过肩机位，宁秋水边走边轻声提醒。用于 V006 约 33.20–35.93 秒 N20 后段，并接入先前单独批准的君鹭远 B V002 近景。
- 所有已批准 N16–N17 V004、N19/N20 原图、N21、君鹭远 B V002、宁秋水结尾 B V002、S02-B 正式母版均不修改。

## 已收到的原始 PNG（二进制本地实测）
- Chat 附件名称：`烛光回廊里的轻声提醒(1).png`
- PNG 签名：PASS
- PIL 原图完整性校验：PASS
- 图片尺寸：**941×1672**
- Mode: **RGB**
- 字节数：**1,840,569**
- SHA-256: **`f3002984a377a31e05cd7490e914c0da4009509c8ddb5eaf45a5d45144775989`**
- Git blob SHA-1: **`7fedcdc93f2b366d1a8597e86ffe8c99006ce027`**
- 原始 PNG 未做重新生成、编辑、缩放、转换或压缩。

## 上游已核验 Bundle
- Bundle ID: `S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`.
- Validation-only Run: **38540725413**，5/5 PASS，无 Artifact。
- Formal Build Run: **38541197812**，5/5 PASS。
- Artifact ID: **11882167307**。
- Artifact digest: **sha256:e229a2cdec6401347c0e43cec5c223225b18dbd29d758515ecd98aeb69fbd7bc**。

## GitHub staging & Candidate Intake
- Branch: `review/s02b-jun-nod-insert-20261014`.
- Exact delivery Spec: `production/candidate_delivery_specs/S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01_CANDIDATE_01_DELIVERY_V001.json`.
- Target staging path: `staging/story_shot_candidates/S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01/烛光回廊里的轻声提醒(1).png`.
- Exact intake workflow: `.github/workflows/s02b-v006-new01-po-candidate-intake-v001.yml`.
- Original attached image **not yet submitted to GitHub staging at the time of this receipt**. Text spec/README are not a substitute for source PNG.
- After original PNG upload to staging, GitHub Actions automatically computes hash/byte count/Git blob and verifies against this receipt; if any mismatch, STOP.

## Hard boundaries
- No candidate 02 generation, no restyling/second image, no extra references.
- No canonical publication, no Story Shot Index write, no formal video edit or main merge.
- When staging exact verification succeeds, prepare the separate canonical release/registration approval gate, not automatic publication.
