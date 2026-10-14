# S02-B V006｜NEW-02 内厅人流侧向机位｜Reference Delivery Bundle V001 Validation-only Exact Verification Receipt

日期：2026-10-14
状态：**DIRECTOR AND SCENE DESIGN COMPLETE / 5 OF 5 VALIDATION-ONLY EXACT PASS / ZERO ARTIFACT / FORMAL BUNDLE NOT BUILT / WORK NOT AUTHORIZED**

## 0. 任务与权限
- PO 新任务：「开始NEW-02｜人群内部侧向机位制作」。
- Shot ID：`S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`
- Bundle ID：`S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
- Branch：`review/s02b-jun-nod-insert-20261014`
- NEW-01：独立正式批准并关闭；此任务完全不更动 NEW-01 原始 PNG、登记或其他已批资源。
- NEW-02 Director design: `docs/project_control/gates/P0_3_video_pipeline/s02_b_v006_cinematic_language_director_design_v0_2_2026-10-14.md`
- NEW-02 Scene Reference V0.2: `docs/project_control/gates/P0_3_video_pipeline/s02_b_v006_new02_crowd_interior_side_depth_scene_reference_v0_2_2026-10-14.md`
- Spec: `production/bundle_specs/S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001.json`，**`build_authorized=false`**。
- Independent workflow: `.github/workflows/s02b-v006-new02-five-reference-validation-only.yml`。

## 1. GitHub Actions 实际验收结果
- Validation-only Run: **`38551894857`**
- Job: **`115811580012`**
- Trigger commit: **`5d5135e5bff69fe11518b8d7c7a4278b87feb920`**
- Run URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38551894857
- Run status: **completed / success**
- Validator: `scripts/story_shot_reference_bundle_builder_v1.py --validate-only`。
- Log evidence:
  - `NEW02_VALIDATION_ONLY_AUTHORIZATION=PASS`
  - `EXPECTED_DIRECT_REFERENCES=5`
  - `CONTROLLED_CROWD_MANIFEST_AUTHORITY=ENFORCED`
  - `N21_DIMENSION_EXCEPTION_941x1671=PROTECTED`
  - `VALIDATION_PASS: 5/5 exact canonical references verified`
  - `BUILD_AUTHORIZED=FALSE`
  - `GENERATION_ALLOWED=FALSE`
  - `BUNDLE_BUILD=SKIPPED`
  - `ARTIFACT_UPLOAD=NONE`
  - `WORK_IMAGE_GENERATION=NONE`
  - `NEW02_VALIDATION_ONLY=COMPLETE`
- GitHub run Artifacts listing: **0**.

## 2. 五张受控原图的精确身份

| # | Reference ID | Authority | Bytes | Width×Height | Locked SHA-256 | Git blob |
|---|---|---|---:|---|---|---|
| 1 | N21_APPROVED_STORY_SHOT | Story Shot Index APPROVED/CURRENT | 2215769 | 941×1671 | `4296383dc3fd330240a1107c004ce22d1c0ae730b193fcba495779308ba1ab0c` | `3224760c7e5bb622679d6b4f10f4817050fa6197` |
| 2 | N22_APPROVED_STORY_SHOT | Story Shot Index APPROVED/CURRENT | 1834637 | 941×1672 | `6d1ed04106bb35943d752113e17d5f36fd2d55b29f4234e13177c7f8b6496f3a` | `a0f38041c10e4eb13a5a915a5d2f7bf22f85a2cf` |
| 3 | N23_APPROVED_STORY_SHOT | Story Shot Index APPROVED/CURRENT | 2697400 | 941×1672 | `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973` | `649ed97addf97f126a05e12d43325720a624ea19` |
| 4 | AST_IMG_000108 | Asset Registry APPROVED/CURRENT (SCENE MASTER) | 2541370 | 1448×1086 | `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3` | `91471e32dab1c7b51b7e718ffd539305d81daf85` |
| 5 | BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q | Controlled Reference Manifest PRODUCT_OWNER_APPROVED/CURRENT | 2373958 | 1536×1024 | `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756` | `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400` |

**核验依据**：从 GitHub checkout 的 PNG 逐张读取并计算真实 SHA256、尺寸、字节数、Git hash-object SHA1；Story Shot Index/Asset Registry/Controlled Reference Manifest 的路径、生命周期和适用角色元数据要求一致。

N21 的 **941×1671 为历史 PO 明确批准例外**，不得重采样；仅将未来新的 Candidate PNG 设为 941×1672。

Generic Guest REAR_3Q 是项目层受控参考，不是常规 Asset Registry 项目；检验其独立 Manifest 完全合规。

## 3. 导演镜头交付意图
- 保留前段 N22 与后段 N23 空间运动轴；真实机位在人流内部侧后方，一到两人近距离过镜带自然轻虚焦；三四位诡客在中景纵深错位行进；远处阴暗拱廊。
- 不以人群全人数可见性或正面合影替代镜头成立；门允许不出镜，不能出现蓝天涌入内厅、第二外部出口、背包行李、过量暖光或抠图感。
- EDL 临时 43.300–45.533s，**不是精确语音边界证明**。
- 实际取景空间轴须由未来 Work 在已核验 Bundle 的五张**真实像素**上复查，不得把此处文件身份核验视为视觉机位验收。

## 4. 下一生产门槛
- 当前正式 Bundle `build_authorized=false`：**不得将验证通过误认作正式 Bundle 已产生**。
- 可申请下一道 PO 审批：只构建 **Formal Bundle V001 + GitHub Actions Artifact 5/5 Exact Verification**；不意味着准许 Work 出图。
- 之后另行授权 Work 恰好 **1 张 PNG 941×1672**；完成后立即停止待 PO 审图。
- Canonical Publication、Story Shot Registration、Registration Verification、视频剪辑、main merge 均是独立后续事务，未经批准不执行。

**Gate: V006 NEW-02 reference validation-only = CLOSED/PASS; formal Bundle build awaiting authorization.**
