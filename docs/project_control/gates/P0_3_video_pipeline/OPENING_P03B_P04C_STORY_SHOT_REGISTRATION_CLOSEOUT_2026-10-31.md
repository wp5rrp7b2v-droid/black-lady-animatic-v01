# Opening Enhance P03-B / P04-C｜Story Shot 登记收尾｜2026-10-31

状态：**COMPLETE / BOTH PO APPROVED / EXACT SOURCE BINARY PUBLISHED / INDEX 35 / INDEPENDENT REGISTRATION PASS**

## 一、审批与来源身份

2026-10-31 PO 通过本对话明确批准两张已上传 PNG，授权进行登记。无额外图像生成或重编码。

| Shot | 原件 | 尺寸 | 字节 | SHA-256 | Git blob |
|---|---|---|---:|---|---|
| OPENING_P03B | `image(20261031-092420).png` | 941×1670 | 3113918 | `ad7ae095a11fcce8772c1d2694683bc0f15336294a35bd7a3d12480c6d58e98e` | `067e60b7ff538700cc71c64d629ec6a80eaccec1` |
| OPENING_P04C | `image(20261031-092459).png` | 941×1672 | 3364032 | `6a00e7a76ed8a7e228dc2ab334e93a7f907b586293a144649773f4f9c29628be` | `926a4a2a4025187fa254ee0cb1a3ac65a0a35e33` |

**尺寸例外（必须保留）：**P03-B PO 批准的**原始文件**实际高度 1670，比推荐 1672 少 2 像素。为遵守 Exact Binary，不缩放、不补边、不重编码，不将原件虚报为 941×1672。未来视频装配如需画幅适配，仅对另行产生的装配派生物操作，并保留本原件和其 SHA。

## 二、实际 GitHub 操作与验证

- 已验证 Bundle：`OPENING_P03B_P04C_SHARED_BLOOD_DOOR_REFERENCE_DELIVERY_BUNDLE_V001`，GitHub Actions run `41187875548`，5/5 exact refs PASS，artifact `13037955694`。P03-A 继续作为唯一受控血门 Scene Anchor。
- P03-B 候选入库：Actions `41189594063` SUCCESS，核验 exact PNG `941×1670`, SHA, Git blob；P04-C 候选入库：Actions `41189935095` SUCCESS，核验 exact PNG `941×1672`、SHA、Git blob。P04-C transport also had verified reconstruction run `41189594066`。
- **正式二进制发布** commit `77d430f9a116c0ae4bb182e02e4320ad1dd55d7a`：原样复用 Git blobs `${p03.blob}` 和 `${p04.blob}`，路径分别为：
  - `production/image_library/approved/story_shots/OPENING_P03B_TASK_MAIN_APPROVED_V001.png`
  - `production/image_library/approved/story_shots/OPENING_P04C_HINTS_MAIN_APPROVED_V001.png`
- 上述发布同时清理临时候选 `staging/story_shot_candidates/OPENING_P03B/`、`OPENING_P04C/` 二进制，不对图像做改动。
- **Story Shot Index 登记** commit `1e80a5485e6da3c5c196701d3513befc8c4bcce7`：`production/story_shots/story_shot_index.jsonl` 由 33 → 35，OPENING_P03B 与 OPENING_P04C 均唯一且 `APPROVED / CURRENT`。
- **独立登记校验** GitHub Actions run `41191180952` **SUCCESS**，验证两个原件的 SHA/Blob/尺寸/大小与登记行一致，P03-A 原受控场景锚点未漂移，临时 staging 已清除，`STORY_SHOT_INDEX_COUNT=35`。

## 三、历史临时校验脚本

- 先前 P03-A 仅针对 33 条索引的临时 workflow 在本次索引增至 35 时再次触发，run `41191180974` FAILED（写死 `len(idx)==33`）。这属于已过时脚本的计数假设失效，**不是** P03-A 或新两图源文件失败；P03-A 既有独立登记 PASS run `41186921151` 保留。
- 本次收尾撤下该过时的一次性 P03-A workflow，亦按 SOP 移除本次 P03-B/C 已完成验证的一次性 workflow，避免随后索引增长触发虚假失败。原各 Actions run 及 Git commits 永久保留证据。
- 候选清理造成的通用候选入库工作流 run `41190970059` 失败不等同于源图 verification FAIL；正式入库使用各自成功 run，正式登记另由本次 run PASS。

## 四、仍有效的生产边界

- P03-A、P03-B、P04-C 现均已 PO Approved、exact canonical Published、Story Shot 登记通过。
- 40.260 秒 P03/P04→尼尔欢迎音频独立 PO Approved，**尚无**新版 Opening 视频本体的 PO Approval。
- 正式 Opening V001 保持已批锁定，正式 Video Index 仍为 3。
- 独立血门木门 A/B 制作依旧 PAUSED，不将本次三张图视为 A/B 视频专项解冻。
- P03-B 2px 高度偏差需在视频装配阶段作为编辑适配事项处理，不倒改原像素。

## 五、本阶段实际证明

已证明：两张经过 PO 视觉批准的原始 PNG 在 GitHub main 的 Git blob 与来源一致；Index 35 唯一登记；登记校验 PASS。尚未证明：三图 + 已批音频拼接后的整体叙事观感、精确镜头时长与成片效果。
