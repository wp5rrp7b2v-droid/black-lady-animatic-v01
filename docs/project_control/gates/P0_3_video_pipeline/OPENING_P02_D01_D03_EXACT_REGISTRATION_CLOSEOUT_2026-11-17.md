# 《诡舍·黑衣夫人》｜Opening P01→P02 D01/D02/D03｜Exact Binary Canonical Publication & Story Shot Registration Closeout

日期：2026-11-17
状态：**3/3 PO VISUAL APPROVED / 3/3 GITHUB INTAKE PASS / 3/3 EXACT CANONICAL PUBLISHED / 3 UNIQUE STORY SHOTS REGISTERED / INDEPENDENT POST-REG VERIFICATION PASS / P0.3 STILL IN PROGRESS**

## 1. 结果与不可改变的正式基线

- D 版顺序：诡舍外景（由远）→ 三楼安静空旷环境（向内）→ 紧闭旧血色木门（近景）。
- 三张视觉均由 PO 明确审批，并由 PO 按指定路径上传精确交付 PNG 到 GitHub main。
- P01 V018 63.375 秒已批准视频母版不变；原音不变。此处是**静图资产登记完成**，不代表 D 转场视频已经剪辑、听审或 P0.3 整体 Gate PASS。
- 原始 2026-11-17 入库 Gate 报告（先前未完成阶段，现由本报告完成收尾）：`OPENING_P02_D01_D03_PO_APPROVAL_AND_BINARY_INTAKE_GATE_2026-11-17.md`。

## 2. 真实文件、精确原件与 Canonical 映射

| Shot | Staging 原始 PNG | Canonical 正式名 | 实际尺寸 | Bytes | SHA-256 | Git Blob SHA-1 | GitHub 入库 CI |
|---|---|---|---|---:|---|---|---|
| `OPENING_P02_D01` | `OPENING_P02_D01_GHOST_HOUSE_EXTERIOR_CONVERTED_PNG_REVIEW.png` | `OPENING_P02_D01_GHOST_HOUSE_EXTERIOR_APPROVED_V001.png` | 940×1672 | 2,339,571 | `7732555dde7f3395f08854b9f56ea3e857a4e58248dec3c2ce108b76b6f44dde` | `66e561b3a23f0356db55239a8d2c6de22d62afc2` | [44044324515](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44044324515) SUCCESS |
| `OPENING_P02_D02` | `OPENING_P02_D02_THIRD_FLOOR_ENVIRONMENT_PO_APPROVED_ORIGINAL.png` | `OPENING_P02_D02_THIRD_FLOOR_ENVIRONMENT_APPROVED_V001.png` | 941×1672 | 1,645,509 | `4098fc1fe5af158b459b2d2575ccbd4db648a4fee6ce8b05f6eb69f3d58b51dc` | `837a62335fccdcef5c076ddd2313a42127846310` | [44044329337](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44044329337) SUCCESS |
| `OPENING_P02_D03` | `OPENING_P02_D03_CLOSED_BLOOD_WOODEN_DOOR_PO_APPROVED_ORIGINAL.png` | `OPENING_P02_D03_CLOSED_BLOOD_WOODEN_DOOR_APPROVED_V001.png` | 941×1672 | 1,805,752 | `f1c706e7ed60accf169e75a8b1d131974489c438bf179b093847ec3860fd43c3` | `75dd1c13fdf31a4794c9a8f5dd10aff101ee3811` | [44044335597](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44044335597) SUCCESS |

所有 Canonical 均位于 `production/image_library/approved/story_shots/`，原图与正式图为**完全相同 Git Blob**，无补像素、无上传后重编码、无改名以外内容变化。

### D01 原格式异常的证据边界
初次 PO 批准的视觉源文件名虽为 .png，实际为 WEBP，940×1672、1,787,658 bytes、SHA-256 `4b36a7579fcf108885e225e5c092d91992a160338f59145475f032fbe02800e9`。2026-11-17 Chat 建立已解码 RGB 逐像素一致的 PNG 候选（新 SHA `7732555...44dde`），在告知差异后 PO **亲自上传了这一特定 PNG 文件并要求继续正式登记**。本次正式锁定的是该 **PO 选定并实际上传的 PNG 二进制**，不是假称最初 WEBP 与 PNG 字节相同。尺寸 940×1672 保留，后续视频统一画布时只可在派生剪辑中调整。

## 3. 真正执行的 GitHub 提交与独立 Gate

1. PO 上传三张至 `staging/story_shot_candidates/`，Commit `d183a0e1864dd9b168c5ca9d6574e71e6ada7d7e`；GitHub Blob 与前述源文件身份完全吻合。
2. GitHub `production/candidate_delivery_specs/OPENING_P02_D0*_DELIVERY_V001.json` 三份实际规格补齐；通用 Candidate Intake CI **3/3 SUCCESS**。原上传时通用 CI 曾因缺规格失败 Run `44043932149`；后来三次独立 PASS 取代该配置失败，图片未因此改变。
3. Canonical exact-blob 发表、3 条 `APPROVED / CURRENT` Story Shot Index、9 条审计事件、独立后验 CI workflow 同一个正式发布提交完成：`4ae3d799cb9eb01ba58300793fb2705144678d09`。Story Shots **49→52**；Audit Events **239→248**。
4. 首次后验 `44044789351` FAILURE：审计新增事件 ID 被写成 `D1`、`D2`、`D3`，而验证按 `D01`、`D02`、`D03` 比对；照片 SHA、Git Blob 和 Registry 记录已成功通过，到 audit cardinality 才报错。
5. 只修改 9 条新增审计事件 ID，不更改二进制或索引，修正 Commit `1af4d774a446f1089c599613ad2c366a62c2450b`。
6. **独立登记后复验 [GitHub Actions 44044933964](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44044933964) SUCCESS**；三条输出 `P02_D_EXACT_REGISTRATION_PASS`，总标记 `OPENING_P02_D_THREE_EXACT_REGISTRATION_PASS__AT_LEAST_52_SHOTS_248_AUDITS`。逐字节 Staging↔Canonical、SHA-256、PNG 签名/尺寸、Git Blob、索引唯一性/内容和每张 3 条审批/发布/登记 Audit Event 全 PASS。
7. 同次正式索引回归：P01 OPEN01、OPEN02–07、P01 11/03 七张补镜、白潇潇正脸及两种侧脸的 CI 全部 SUCCESS。为适应合法的追加增长，旧 P01 七镜回归流程固定 `==49/239` 门槛在事先以 Commit `0e7f0d0` 改为 `>=49/239`，其 7 张精确哈希核查逻辑不变。

## 4. 真实制图来源与流程一致性限制

三张选定概念图**确实由 Chat 中的图像生成创建**，不是由 Work 读取 Actions Bundle 制作。后续的 PO 审批、原件上传、GitHub exact CI、Canonical publication 和 registration 都有独立实证。此次正式登记把 `generation_provenance_status=CHAT_IMAGE_GENERATED__WORK_REFERENCE_BUNDLE_NOT_VERIFIED` 保存在各条 Index 中，**不倒填假 Work Run/Bundle**。因此严格意义上不能宣称这批次完整遵守了标准「Director → Reference Bundle → Work」图像生成前置步骤；这里的已通过验收仅指 SOP 列明的四项**静图登记**硬 Gate。后续新镜头恢复用户锁定的 GitHub Actions → Work 制图链，不能把本次个案扩展为普遍跳过 Work 的惯例。

P03-A 已批准门体参考的既有 scope（只对 P03B/P04C 正向引用）不被本批登记隐式扩大；D03 是本轮独立 approved Story Shot 而非替代 P03-A Canonical Master。未来做 P02 贴门/血字动作需检查同一门体连续性，不能仅因登记完成推断两资产门面形制完全相同。

## 5. 收尾与下一步最小验证

- **PASS**：三张 PO 批准图片的 3×完整四门闭环，52 唯一 Story Shots / 248 唯一审计事件，独立 GitHub CI 通过；旧正式资产无覆盖。
- **NOT DONE**：新的 P01→P02 D版 20 秒声音与三镜过门的视频 PO 观感审核；V018 母版不动；没有批准新正式视频。
- **Next minimal proof**：仅用已批准 D01→D02→D03 和与 A/C 同一段连续原声制作最短 D 转场样片，验证空间转移与声音事件时序，并向 PO 提交对照试听。通过前不扩大后续血门动作批量生成。
- GitHub main 为状态源；本次没有用户 Mac 最新同步终端证据，不声明 Mac 本地 PASS。
