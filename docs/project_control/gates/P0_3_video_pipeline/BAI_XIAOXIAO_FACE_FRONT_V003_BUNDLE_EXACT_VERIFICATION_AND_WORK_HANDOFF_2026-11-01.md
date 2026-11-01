# 白潇潇 FACE_FRONT V003｜2.5D动漫风格 Reference Bundle 完整验证与 Work 交接
Date: 2026-11-01

**状态：正式 Bundle BUILT / EXACT BINARY VERIFIED / Work ONLY ONE Candidate 03 AUTHORIZED / PO VISUAL REVIEW PENDING / NO APPROVED CHARACTER MASTER.**

## 为什么重新构建

PO 在 C01/C02 实测后明确锁定：**所有角色必须在与已批准的其他人物一致的 2.5D 动漫风格中呈现；白潇潇不能是真人摄影写实风格。** 旧 `CHARACTER_VISUAL_STYLE_REFERENCE_V001` 局部材质板以真人高写实为主，C01 和 C02 的整体风格检验均 FAIL。独立 V003 重新选择两个已批准角色完整 `FACE_FRONT` 参考，严格作为风格和构图约束，而不是白潇潇身份锚点。

用户已经要求「准备新的 Reference Bundle并提供work制图指令」。此前仅在聊天提供设计和指令，但没有创建 V003 Spec，导致 Work 查到404并停止。**此次实质完成缺失的仓库构建、Actions和交付二进制检验，纠正此前错误声明。**

## 正式输入

Repository: `wp5rrp7b2v-droid/black-lady-animatic-v01`
Spec: `production/bundle_specs/BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V003_REFERENCE_DELIVERY_BUNDLE_V001.json`
Spec commit: `58f1aee64f51d362b88d91f463f33f93ee30a1ec`
Bundle ID: `BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V003_REFERENCE_DELIVERY_BUNDLE_V001`
Authorization: `build_authorized=true`, **one FACE_FRONT candidate only**.

| Reference | Approved Registry ID | Canonical path | Intended use | Size | SHA-256 | Git Blob | PNG |
|---|---|---|---|---:|---|---|---|
| 苏小小 FACE_FRONT | `AST_IMG_000044` | `production/image_library/character_references/su_xiaoxiao/CHAR_SU_XIAOXIAO_FACE_FRONT_DEFAULT_DEFAULT_V001.png` | STYLE_AND_COMPOSITION_ONLY, not identity | 3,057,346 | `1ecf8d82a1346b08da5a5530d39a1492e14427439b3630facf436369f1e59403` | `140bd21af2a25cf016eb7d07f6cf5253dfa02b78` | 941×1672 |
| 温倾雅 FACE_FRONT | `AST_IMG_000048` | `production/image_library/character_references/wen_qingya/CHAR_WEN_QINGYA_FACE_FRONT_DEFAULT_DEFAULT_V001.png` | STYLE_AND_COMPOSITION_ONLY, not identity | 2,930,534 | `2e387afeea665b04568dc718f3b4dafa2e5c5ecd7d8385c779cd72ef40381d0b` | `0e2f10b62994113cfa1070e077075daafb3156c6` | 941×1672 |

两者的 `Asset Registry` 中 `approval_status=APPROVED`、`lifecycle=CURRENT`、`authority_class=MASTER`、`role=FACE_FRONT`，Source type `ASSET`。引用是**只对视觉风格和画面比例生效**，**严禁 face blending、复制他人面容、换装或把苏小小/温倾雅作为白潇潇身份资产**。本次**不包含旧局部 Style Board，也不包含 C01/C02 失败图**。

## GitHub Actions / 原始核验

- Run: [41273039771](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41273039771) — **completed / success**.
- Job: `124749544081` — completed / success.
- Original log: `BUILD_AUTHORIZED=true`; `PASS: 2/2 exact canonical reference binaries verified`; `GENERATION_ALLOWED=TRUE`; Bundle ID matches V003.
- Artifact: [13069309141](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41273039771/artifacts/13069309141).
- Artifact name: `BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_V003_REFERENCE_DELIVERY_BUNDLE_V001`
- Artifact ZIP downloaded independently via GitHub connector (not trusting only Actions status): `5,992,988 bytes`.
- ZIP SHA-256 independently recalculated: `042ea8e898ed0ce7b16b711ad5db2343d01018ab08775cf74d0b54248c8a64e8`; equals GitHub Artifact service digest **EXACT PASS**.
- ZIP CRC: `PASS`; four expected entries (manifest / handoff / two PNG), no unexpected files.
- `delivery_manifest.json`: `reference_count=2`, `all_reference_checks_pass=true`, `generation_allowed=true`, `overall_result=PASS`.
- Inside ZIP, BOTH actual PNGs were individually re-read; independently recomputed SHA256, Git Blob SHA1, exact bytes and PNG dimensions. **All 2/2 pass**; each PNG is 941×1672.
- GitHub reported Artifact expiry `2026-11-08T04:25:42Z`; after expiry stop and rebuild / verify, not quietly use an old Bundle.

## Work 交付和停止规则

Work 从**本次 V003 Artifact**读取 `delivery_manifest.json`、`WORK_HANDOFF.md` 和两张正式风格参考，并独立核对两张 PNG 的 SHA256、byte sizes、Git blobs 和尺寸；发现任何不一致立即停止，不能使用 V001 Bundle 或 C01/C02 代替。

Work 生成**仅一张** `CHAR_BAI_XIAOXIAO_FACE_FRONT_IDENTITY_SEED_CANDIDATE_03.png`，目标 `941×1672` 9:16：新独立白潇潇脸，成熟美艳，红唇自然醒目、深色略微波浪长发、从容有神；**本项目已批角色一样的2.5D动漫画风**，中性背景，眼平正面0°，画幅中保留头、肩、上胸。禁真人摄影肖像、毛孔级写实、写真摄影、Q版、塑料3D、脸部混合/撞脸、P01红裙以及其他视角。

**当前没有 Candidate03，没有视觉 PASS。** 一张图生成后立即停止，交 PO 实际并排视觉审核。不自动出第二张、不开始 Tier A 九视图、不登记 Character Master/Asset Registry、不更新 Story Shot Index、视频或 Approved Audio。

## Gate

- **TECHNICAL PASS：** 完整而真实的 V003 Actions Artifact 存在、双资产已按正式 Registry 作 Exact 验证、下载 ZIP 与文件独立逐位检验通过。
- **ARTISTIC / IDENTITY UNKNOWN：** 新白潇潇 FACE_FRONT 是否匹配现有2.5D风格，尚无真实出图；需 PO 看图验收。
- **Next minimum proof：** 使用此验证的 Artifact 在 Work 制作唯一 Candidate03，PO 审核。如果 FAIL，只纠正有实际证据支持的具体问题。
