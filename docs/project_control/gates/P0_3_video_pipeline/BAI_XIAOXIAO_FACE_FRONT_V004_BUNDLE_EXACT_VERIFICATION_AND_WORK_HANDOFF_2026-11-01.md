# 《诡舍·黑衣夫人》｜白潇潇 FACE_FRONT V004｜正式 Bundle Exact 核验与 Work 单图交接

Date: 2026-11-01  
**Gate: BUNDLE BUILT / INDEPENDENT EXACT BINARY PASS / ONLY ONE WORK CANDIDATE 04 AUTHORIZED / PO VISUAL REVIEW PENDING.**

## 1. 调整原因与审批

PO 审核上一轮正式 V003 画面指出：「感觉有点太像苏小小了」。候选的 2.5D 动漫画风较 C01/C02 有明显改善，但与已批苏小小身份易混淆；PO 紧接批准 V004 针对这一差异重新设计人物面容、保留项目统一2.5D画风并准备新 Reference Bundle/Work 单图指令。

- 本轮用户提交的 C03 审片源 `image(20261101-043010).png`：PNG RGBA, `941×1672`, `2,729,577 bytes`, SHA-256 `35819644c11e140ff255f88c4427ca4d6ce8f1975b511d30661d17a141312710`。这是审片文件的摘要，不宣称为正式 Work 二进制 Canonical Publication。
- **Verdict C03**: `STYLE_DIRECTION_PARTIALLY_PASS / IDENTITY_DISTINCTNESS_FAIL / NOT APPROVED`。不得作为已批准人脸基底或进入 Asset Registry。
- 原导演执行稿在第15节追加 V004 具体差异、保留和否决范围：`docs/project_control/gates/P0_3_video_pipeline/BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V001_DIRECTOR_EXECUTION_2026-11-01.md`。
- 初步假设：移除苏小小 FACE_FRONT 作为正向输入，保留其他 Approved/Current 全身/整脸构图示例，同时用男性角色反向分离人物身份；此假设需要 Work V004 实图后由 PO 证伪，**不是技术已证实的视觉改进**。

## 2. 正式输入

- Repo: `wp5rrp7b2v-droid/black-lady-animatic-v01`
- Spec: `production/bundle_specs/BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V004_REFERENCE_DELIVERY_BUNDLE_V001.json`
- Spec commit: `9fe947ee35e64a1d9f769f43697a472593369cff`
- Bundle ID: `BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V004_REFERENCE_DELIVERY_BUNDLE_V001`
- `build_authorized=true`; `generation_allowed=true`, **1 Work candidate only**.
- `target_candidate=CHAR_BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_CANDIDATE_04.png`; `target_shot_id=BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V004` (Builder 兼容字段，**不是** Story Shot)。

## 3. 参考资产与使用权

| 参考角色 | Asset ID | Canonical role | APPROVED/CURRENT | Bytes | SHA-256 | Git Blob |
|---|---|---|---|---:|---|---|
| 温倾雅 | `AST_IMG_000048` | `FACE_FRONT` | Yes | `2930534` | `2e387afeea665b04568dc718f3b4dafa2e5c5ecd7d8385c779cd72ef40381d0b` | `0e2f10b62994113cfa1070e077075daafb3156c6` |
| 宁秋水 | `AST_IMG_000034` | `FACE_FRONT` | Yes | `2613947` | `5d62423ef9f1abcd349a3736079c77f3f56416cade8991a966fd925e5817ec8c` | `58663e76c353918025736064c7e25741f51e4864` |

- 两张均为 `941×1672` PNG；`source_type=ASSET`，正式 Asset Registry 检查 `APPROVED / CURRENT / ATOMIC / MASTER / FACE_FRONT`。
- **两张图只充当 `STYLE_AND_COMPOSITION_ONLY`。** 模型不可复制、混合或用任何一个已批准角色的五官或脸作白潇潇身份模板。
- 明确排除 `CHAR_SU_XIAOXIAO` 正向画面输入、旧 C01/C02/C03 失败身份图及旧六格偏真人写实的 Style Board。审核时仍应与苏小小并排比较，不能把“不输入苏小小”误当作“绝不撞脸”的证明。

## 4. Actions / Artifact 核验事实

- Actions Run **[41273671483](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41273671483)** — `COMPLETED/SUCCESS`
- Job `124751396146` — `COMPLETED/SUCCESS`
- 工作流原始日志：`BUILD_AUTHORIZED=true` / `PASS: 2/2 exact canonical reference binaries verified` / `GENERATION_ALLOWED=TRUE`
- Artifact **[13069849870](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41273671483/artifacts/13069849870)** — `BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V004_REFERENCE_DELIVERY_BUNDLE_V001`
- ZIP `5,549,774 bytes`；Artifact service SHA-256 `2c300ec96aeeb6069199abb445bb2ffd0b92051625389750ac83ddda06df36df`
- **独立再次下载**到检查环境，实际重算 ZIP SHA-256 与 Artifact Metadata 完全一致；ZIP CRC 全部通过。
- ZIP 四个文件，且仅此四个：`delivery_manifest.json`, `WORK_HANDOFF.md`, `style_and_composition_only/AST_IMG_000034__CHAR_NING_QIUSHUI_FACE_FRONT_DEFAULT_DEFAULT_V001.png`, `style_and_composition_only/AST_IMG_000048__CHAR_WEN_QINGYA_FACE_FRONT_DEFAULT_DEFAULT_V001.png`。
- Manifest: `reference_count=2 / all_reference_checks_pass=true / generation_allowed=true / overall_result=PASS`，目标文件名与 C04 一致。
- 实际从 ZIP 逐张读取二进制：两张 PNG 的 SHA256、Git Blob、bytes、PNG signature、`941×1672` 均与 Spec/Registry 完全一致，**2/2 Exact PASS**。
- Artifact expiry: `2026-11-08T04:35:31Z`；到期后需重建/重新验证，不能假定链接仍有效。

## 5. Work 唯一授权边界与最小测试

**可执行：** Work 读取上面真实 Artifact/Manifest/HandOff，复核2张 STYLE_AND_COMPOSITION_ONLY图的 Exact 信息，读取导演执行稿第14/15节，创建仅 `CHAR_BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_CANDIDATE_04.png` 一张 `941×1672` 9:16 FACE_FRONT 0°，2.5D动漫统一风格，独立成熟美艳新脸、观察力与轻微危险感、红唇与长深色发、素净深色上装、灰色低干扰背景，完成后立即停止，交 PO 看。

**禁止：** 复用苏小小/V003原脸；代替正式输入用 C01/C02；进一步生成候选、其它角度、九视图、剧情红色睡裙；自动 Approved 资产发布、Registry/Story Shot/音视频修改。

**PASS**：PO 视觉并排确认在项目统一 2.5D 动漫风格下，白潇潇与苏小小的脸型/眉眼/气质明显不同，且符合白潇潇原著。**FAIL**：仍有撞脸、滑向真人写实、过度成熟反派/塑胶CG/过分稚嫩；停止后只针对被证明的问题纠偏。**当前仅 Bundle 技术 PASS，不代表 C04 已经生成或视觉通过。**

P0.3 `IN PROGRESS`，Story Shots `35`、Video Index `3`、Opening 192.257秒已批准音频、所有已批准人物 Master 均不变。
