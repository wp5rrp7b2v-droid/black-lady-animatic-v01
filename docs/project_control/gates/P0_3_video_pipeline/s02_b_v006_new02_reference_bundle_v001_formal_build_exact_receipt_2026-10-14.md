# 《诡舍·黑衣夫人》S02-B V006 NEW-02｜Reference Delivery Bundle V001 正式构建与 Artifact 独立二进制核验

日期：2026-10-14

**GATE: FORMAL REFERENCE BUNDLE BUILT / ARTIFACT ORIGINAL ZIP DOWNLOADED / INDEPENDENT EXACT 5/5 PASS / NO WORK PNG / NO STORY SHOT PUBLICATION / NO VIDEO MODIFICATION / NO MAIN MERGE.**

## 1. Product Owner 本轮授权边界

Product Owner 明确批准：

> 批准 V006 NEW-02 Reference Delivery Bundle V001 正式构建，并执行 Artifact 5/5 Exact Binary Verification。保留 N21 已批准的 941×1671 尺寸例外，不修改任何参考 PNG。本次仅授权 Bundle 构建与核验，不授权 Work 出图、视频修改、正式发布、Story Shot 登记或合并 main。

- Task ID: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`.
- Bundle ID: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`.
- Branch: `review/s02b-jun-nod-insert-20261014`.
- Spec: `production/bundle_specs/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001.json`.
- Spec authority at formal-build commit: `build_authorized=true` ONLY for reference Bundle generation, with:
  - `formal_build_authorization.status=PRODUCT_OWNER_AUTHORIZED`
  - `candidate_generation_authorized=false`
  - `publication_authorized=false`
  - `story_shot_registration_authorized=false`
  - `video_edit_authorized=false`
  - `main_merge_authorized=false`
- Validation-only precondition: Run `38551894857` **5/5 PASS / zero artifact**.
- Formal pre-build change: commit `32efcbce31a08ec9a811e61dd744f791251146f0`.
- Dedicated workflow: `.github/workflows/s02b-v006-new02-formal-bundle-v001.yml`.

**重要解释**：仓库通用 Builder 在 `delivery_manifest.json` 中的 `generation_allowed=true` 仅代表已生成可用于下游操作的参考包，不构成 Product Owner 对 Work 生图的授权。本次实际授权以 Spec 的 `candidate_generation_authorized=false` 和 Artifact 随包附带的 `PO_AUTHORIZATION_SCOPE.md` 为准。不可自动执行 Work。

## 2. GitHub Actions 正式构建核验

- Formal Build Run ID: **`38553600591`**
- Job ID: **`115817185391`**
- Workflow trigger commit: **`3738e6d5e94d96230ac12066401da8dd951fc4a5`**
- Run URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38553600591
- Run result: **completed / success**.
- Preupload checker reports:
  - `NEW02_FORMAL_BUNDLE_AUTHORIZATION=PASS`
  - `VALIDATION_ONLY_38551894857_PRECONDITION=PASS`
  - `N21_APPROVED_941x1671_DIMENSION_EXCEPTION=PROTECTED`
  - `CONTROLLED_REFERENCE_MANIFEST_AUTHORITY=ENFORCED`
  - `PASS: 5/5 exact canonical reference binaries verified`
  - `WORK_GENERATION_ALLOWED=FALSE`
  - `EXACT_REFERENCE_PASS=` for five separate assets (SHA-256/Git blob/byte size/geometry each matched).
  - `NEW02_PREUPLOAD_EXACT_BINARY=PASS_5_OF_5`
  - `BUNDLE_IMAGE_COUNT=5`
  - `N21_SOURCE_DIMENSIONS=941x1671`
  - `CANDIDATE_PNG_GENERATED=FALSE`.

## 3. 正式 Artifact 的 GitHub 身份

- Artifact ID: **`11887079610`**
- Artifact name: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
- Original ZIP file size: **`11630182` bytes**
- GitHub-recorded ZIP digest: **`sha256:f3bf0ca2f4de860a4c47ba7276ff2b8653196c0bc1a747a5fbdfb8b9d9f084b7`**
- Expires: **2026-10-21T11:01:28Z** (GitHub Actions retention 7 days).

## 4. GitHub Artifact 下载后独立 Exact Binary Verification

已使用 GitHub Actions Artifact 下载接口取得 Artifact ID `11887079610` 的原始 ZIP，并在执行容器中独立检查压缩包与其中的原始 PNG 字节，无需任何重编码或截图。

- 下载原始 ZIP SHA-256 **`f3bf0ca2f4de860a4c47ba7276ff2b8653196c0bc1a747a5fbdfb8b9d9f084b7`**，与 GitHub digest 完全一致。
- 下载 ZIP 实际大小 **`11630182` bytes**，与 GitHub artifact size 一致。
- ZIP CRC test: **PASS**。
- ZIP 恰好 **8 个文件**：**5 个 PNG** + `delivery_manifest.json` + `WORK_HANDOFF.md` + `PO_AUTHORIZATION_SCOPE.md`，无多余候选 PNG/GIF/MP4。
- Bundle Manifest `overall_result=PASS`，`reference_count=5`，`all_reference_checks_pass=true`；引用顺序与 Bundle Spec 一致。
- 对每个 ZIP 内原始 PNG 均独立重新计算 **SHA-256、Git blob SHA-1**（Git `blob <len>\0<raw bytes>` 计算）、**原始字节数**和 **PNG IHDR 宽高**，与 `delivery_manifest.json` 的 locked identity 完全一致；五项都 PASS。

| # | Reference | 原始尺寸 | Bytes | SHA-256 | Git blob |
|---|---|---|---:|---|---|
| 1 | `N21_APPROVED_STORY_SHOT` | **941×1671** | 2215769 | `4296383dc3fd330240a1107c004ce22d1c0ae730b193fcba495779308ba1ab0c` | `3224760c7e5bb622679d6b4f10f4817050fa6197` |
| 2 | `N22_APPROVED_STORY_SHOT` | 941×1672 | 1834637 | `6d1ed04106bb35943d752113e17d5f36fd2d55b29f4234e13177c7f8b6496f3a` | `a0f38041c10e4eb13a5a915a5d2f7bf22f85a2cf` |
| 3 | `N23_APPROVED_STORY_SHOT` | 941×1672 | 2697400 | `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973` | `649ed97addf97f126a05e12d43325720a624ea19` |
| 4 | `AST_IMG_000108` inner lobby | 1448×1086 | 2541370 | `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3` | `91471e32dab1c7b51b7e718ffd539305d81daf85` |
| 5 | `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q` | 1536×1024 | 2373958 | `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756` | `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400` |

### N21 Approved Dimension Exception

N21 的原始批准 PNG 是 **941×1671**，在正式 Bundle 中保持 941×1671，原始字节数、SHA-256 和 Git blob 均匹配，**未缩放、未裁切、未重新编码**。未来 NEW-02 独立 Candidate PNG 目标仍为 941×1672，但需要新的 PO 对 Work 出图授权。

### Generic Guest Controlled Reference

REAR_3Q 受控人群板按 `production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.manifest.json` 核验身份与来源，不能错误登记成普通 Asset Registry 数据，也不能把参考板 2×5 布局搬到新的 Story Shot 镜头构图中。

## 5. 任务关闭范围与后续门槛

**本轮 NEW-02 正式 Bundle 构建和 Artifact 5/5 独立核验 = CLOSED / PASS。**

当前保留：
- 正式 Bundle Artifact ID `11887079610`，有效期 7 天；
- 本审核分支的 Bundle Spec、工作流和本 Gate 收据；
- 五张原始源 PNG 均未修改。

**本轮没有执行，且没有授权：**
- Work 生图、Candidate 01 或更多图片；
- 改动任一视频母版或音轨；
- 正式 Story Shot 发布、登记；
- 合并 `main`、更改已批准场景或人物资源。

**下一门槛**：等待 Product Owner 独立授权 Work 从 Artifact `11887079610` 读取已验证 Bundle，**只生成 1×941×1672 PNG Candidate 01**，随后立即停止，交 PO 审核。
