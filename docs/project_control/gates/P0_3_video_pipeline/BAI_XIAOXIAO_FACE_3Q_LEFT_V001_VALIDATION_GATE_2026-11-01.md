# 白潇潇 FACE_3Q_LEFT｜V001 Reference Validation Gate

Date: 2026-11-01
Subject: `CHAR_BAI_XIAOXIAO` / `FACE_3Q_LEFT`
Gate: **REFERENCE VALIDATION PASS / BUNDLE BUILD NOT AUTHORIZED / WORK NOT AUTHORIZED**

## Canonical baseline

- Existing approved facial reference: `AST_IMG_000109` (`FACE_FRONT / V001 / APPROVED / CURRENT / MASTER`).
- Canonical: `production/image_library/character_references/bai_xiaoxiao/CHAR_BAI_XIAOXIAO_FACE_FRONT_DEFAULT_DEFAULT_V001.png`.
- SHA-256: `d9d62dd4c3168ec587b50e2cf30782a5c816de3ad081c1c434e659156807f5eb`.
- File size: `2747575` bytes; dimensions: `941×1672`; Git Blob: `38761350f926c30358cb98e55d6f4d603d8825f1`.
- New validation-only Spec: `production/bundle_specs/BAI_XIAOXIAO_FACE_3Q_LEFT_REFERENCE_DELIVERY_BUNDLE_V001.json`.
- Spec commit: `5273f8130861bc9f97b75af6b53828bbd5886552`.

## GitHub Actions evidence

- Workflow: `Story Shot Reference Bundle Builder`.
- Trigger: push to `main`; run: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41303915149
- Job ID: `124840320904`.
- Run status: `completed`; conclusion: **success**.
- Raw validation output: `VALIDATION_PASS: 1/1 exact canonical references verified`.
- Raw authorization output: `BUILD_AUTHORIZED=FALSE`; `GENERATION_ALLOWED=FALSE`.
- `Validate references without building`: success.
- `Build verified reference bundle`, `Read bundle ID`, `Upload verified bundle`: skipped.

## Gate decision

**FACT:** Input validation completed 1/1 with success and source integrity checks against the approved C06 canonical reference.

**NOT PROVEN:** Artifact build, Work consumption, correct 45° face geometry, identity consistency in a new viewpoint, PO visual acceptance.

**SCOPE LOCK:** No approved asset overwritten; no new candidate output; no Registry, Story Shot or video mutation. Do not claim Bundle ready merely from this validation success.

**Next distinct gate:** Upon explicit PO authorization to build and make one candidate, set `build_authorized=true`, re-run exact Bundle verification, independently check resulting Artifact and hand off **only one** `CHAR_BAI_XIAOXIAO_FACE_3Q_LEFT_CANDIDATE_01.png` to Work. Candidate remains unapproved until PO reviews it.


## 2026-11-01｜PO 批准正式 Bundle 构建｜Exact Artifact Verification PASS

Product Owner 后续明确指令「开始正式 Bundle 构建」。该授权**仅限**把本验证成功的 Bundle Spec 切换为 `build_authorized=true`、执行 GitHub Actions 构建、独立验证 Artifact；未授权 Work 生成任何 Candidate。

- Spec 修改后 Commit：`ec98c096a79cb4106f9d270ca7d54fcb384de4e8`，保持唯一 `AST_IMG_000109` 正向图像引用；`work_generation_authorized=false`。
- Workflow：`Story Shot Reference Bundle Builder`；GitHub Actions Run [41304720791](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41304720791)，Job `124842671048`，`completed / success`。
- 原始日志：`BUILD_AUTHORIZED=true`、`PASS: 1/1 exact canonical reference binaries verified`、`GENERATION_ALLOWED=TRUE`、`BUNDLE_ID=BAI_XIAOXIAO_FACE_3Q_LEFT_REFERENCE_DELIVERY_BUNDLE_V001`。
- Build、Read Bundle ID、Upload Artifact 三步均 `success`。
- Artifact：`13082701393`；[正式下载链接](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41304720791/artifacts/13082701393)，大小 `2,750,556 bytes`；SHA-256 `9c15d9a7dddb7c794e82ee42c243124750f79bdbafe6c5fe5656775823d3e3a0`。
- Artifact 下载后在独立检查环境重新计算 ZIP SHA-256，与 Actions 日志及 Artifact metadata digest 完全一致；ZIP CRC `PASS`。
- ZIP 恰有三个文件：`WORK_HANDOFF.md`、`delivery_manifest.json`、`identity_authority/AST_IMG_000109__CHAR_BAI_XIAOXIAO_FACE_FRONT_DEFAULT_DEFAULT_V001.png`。
- delivery manifest：`reference_count=1`、`all_reference_checks_pass=true`、`overall_result=PASS`，`byte_identical_copy=PASS`。
- ZIP 内 Canonical PNG 经独立重算：`2,747,575 bytes`、`941×1672`、SHA-256 `d9d62dd4c3168ec587b50e2cf30782a5c816de3ad081c1c434e659156807f5eb`、Git Blob `38761350f926c30358cb98e55d6f4d603d8825f1`，均 **MATCH**。
- `WORK_HANDOFF.md` 中明确禁止在获得独立 PO 授权前出图。上述 `GENERATION_ALLOWED=TRUE` 是 Builder 技术信号，不构成 Work 授权。
- Artifact retention：GitHub 返回 `expires_at=2026-11-08T12:04:45Z`。若过期必须重新构建并重新验证，不可凭旧 Artifact ID 宣称可用。

**Gate conclusion：FORMAL BUNDLE BUILD PASS / INDEPENDENT EXACT ARTIFACT PASS / WORK GENERATION NOT AUTHORIZED**。

此前本文的 Validation-only 阶段结论作为历史基准保留；本条记录 supersedes 其中「尚未构建 Bundle」的当前时态表述。

**Next distinct Gate：** 必须取得 PO 对 `CHAR_BAI_XIAOXIAO_FACE_3Q_LEFT_CANDIDATE_01.png` **仅 1 张** Work 制图的明确授权；生成后立即停止供 PO 视觉审核。禁止自动发布 Asset、登记 Story Shot、修改正式视频。
