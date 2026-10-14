# 《诡舍·黑衣夫人》｜S02-B V006 NEW-02｜Candidate 01 GitHub Staging Exact Intake Receipt

Date: 2026-10-14

**GATE: PRODUCT OWNER VISUAL APPROVAL PASS / GITHUB ORIGINAL PNG EXACT INTAKE PASS / STAGING COMPLETE / CANONICAL PUBLICATION, STORY SHOT REGISTRATION, VIDEO CHANGES AND MAIN MERGE NOT AUTHORIZED.**

## 1. Product Owner 批准与身份

- PO 已对 Work 所生成 NEW-02「人群内部侧向机位」唯一 Candidate 01 表示“批准该图”。
- Task ID: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`.
- 会话原始上传名：`城堡幽暗拱廊中的穿行人群(1).png`。
- GitHub 原始上传名：`城堡幽暗拱廊中的穿行人群.png`，仅**文件名**不同。
- Canonical Candidate Delivery Spec: `production/candidate_delivery_specs/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_CANDIDATE_01_DELIVERY_V001.json`.
- GitHub branch: `review/s02b-jun-nod-insert-20261014`.
- Verified original staging path: `staging/story_shot_candidates/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01/城堡幽暗拱廊中的穿行人群.png`.
- 用户原始 PNG：**941×1672**，**1,963,410 bytes**。
- 锁定 SHA-256：**`d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`**。
- 锁定 Git blob SHA-1：**`d8feba3692ebe25afd0e51f5e3ab32358ea19ded`**。
- GitHub 用户上传时审阅的 commit: **`531a9ca805f9ac3975308e9ae284fffc1ac36971`**。

## 2. GitHub Actions 独立 Original Candidate Intake

- Workflow: `.github/workflows/s02b-v006-new02-po-candidate-intake-v001.yml`.
- Run: **`38558807970`** / Job: **`115834485174`**。
- https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38558807970
- Run: **completed / success**。
- 确定参考图读取边界：文件名白名单中恰好一张 PNG；验证器在 runner *临时工作目录*接受没有 `(1)` 的别名，不对 GitHub 源原图重写。
- 运行日志原文关键结果：
  - `VALIDATION_WORKSPACE_ONLY_PATH_ALIAS_SELECTED=TRUE`
  - `PO_APPROVED_CANDIDATE_SCOPE=TRUE`
  - `EXACTLY_ONE_STAGING_IMAGE=TRUE`
  - `CANDIDATE_PATH=staging/story_shot_candidates/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01/城堡幽暗拱廊中的穿行人群.png`
  - `BYTE_SIZE=1963410`
  - `SHA256=d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`
  - `GIT_BLOB=d8feba3692ebe25afd0e51f5e3ab32358ea19ded`
  - `DIMENSIONS=941x1672`
  - `CANDIDATE_INTAKE_VERIFIED=TRUE`
  - `NEW02_PO_CANDIDATE_EXACT_INTAKE=PASS`
  - `CANONICAL_PUBLICATION=NOT_AUTHORIZED`
  - `STORY_SHOT_REGISTRATION=NOT_AUTHORIZED`
  - `VIDEO_MODIFICATION=NOT_AUTHORIZED`.

### Evidence Artifact

- Artifact ID: **`11890872274`**
- Name: `S02B_V006_NEW02_PO_CANDIDATE_01_EXACT_INTAKE_EVIDENCE`
- ZIP size: **841 bytes**
- GitHub ZIP digest: **`sha256:3eeb303da4d180672ac26c6cb3caa83a0bfa4db8c61c86547a83c35e02c9b18f`**.

## 3. 上游 Bundle provenance

- Reference Delivery Bundle: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`.
- Validation-only Run: `38551894857`, **5/5 PASS**.
- Formal Bundle Run: `38553600591`, **5/5 PASS**.
- Bundle Artifact ID: `11887079610`.
- Artifact SHA-256: `f3bf0ca2f4de860a4c47ba7276ff2b8653196c0bc1a747a5fbdfb8b9d9f084b7`.
- N21 approval exception `941×1671` remained untouched in Bundle.

## 4. 完成范围与下道权限门槛

**PO APPROVED CANDIDATE 01 / ORIGINAL PNG STAGING EXACT INTAKE = PASS / CLOSED.**

- Original source is safely in GitHub review branch staging, not yet in `production/image_library/approved/story_shots/`.
- No canonical Story Shot file published, no Story Shot Index registration or registration verification yet.
- No video, original audio, N21/N22/N23, NEW-01 or approved masters were modified.
- No main merge.

Next strict approval gate: PO must separately authorize **Exact Binary Canonical Publication → Story Shot Registration → Registration Verification** of this exact approved image and preserve SHA-256/Git blob. If approved, move using exact Git blob SHA without PNG processing; independently verify and log results.
