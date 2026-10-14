# 《诡舍·黑衣夫人》｜N23 单镜头动态试验 Stage A 控制样片｜Exact Closeout

日期：2026-10-14

**FINAL: STAGE A TECHNICAL PASS / GITHUB REVIEW-BRANCH OUTPUT PRESERVED / PO VISUAL REVIEW PENDING / HUMAN MOTION STAGE B NOT EXECUTED / N23 V006 AND MAIN UNCHANGED.**

## Product Owner 决策

完成 S02-B V006 候选版登记后，用户同意「N23｜尼尔站在敞开的古堡门边」作为视频动态技术测试首个镜头。测试从原始已批准 PNG 出发，而非重新生成 Story Shot。

GitHub Repo `wp5rrp7b2v-droid/black-lady-animatic-v01`; 审核分支 `review/s02b-jun-nod-insert-20261014`。

## 原始批准图 N23 验证

- 路径：`production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png`。
- 原尺寸：941×1672；源字节：2,697,400。
- SHA-256：`2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`。
- Git blob：`649ed97addf97f126a05e12d43325720a624ea19`。
- PNG 从既有 NEW-02 经过 5/5 Exact Verification 的正式参考 Bundle 中读取并核验，与 canonical 权威 SHA/bytes/blob 匹配。
- **源 N23 原图未修改、未重新编码，也未改 Story Shot Index**。

## Stage A 控制样片——严格限定

- **只有局部烛光暖度与光强波动**；非真实人体/烛焰形态运动。不产生新的视觉角色或门/石墙形态。
- 尼尔、经过的人群保持静止，摄影机锁定。
- 通过原图解码后视频专用重采样至 720×1280，制作 90 帧，30 fps，3.000s，无音轨。
- 中间 RAW RGB 帧，灯光变化区域之外修改像素数严格为 **0**；最大通道差 **11/255**，不做全图提亮。
- 首尾强度平滑回到原始亮度。H.264 编码有正常压缩误差，不能把视频压缩后的像素描述为逐像素完全一致；像素保护指编码前 RAW RGB 画面。
- User 本地直接可看的预览文件 `N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001.mp4` 与 GitHub Actions 云端输出采用相同运动设计，但底层 H.264 编码环境不同，因此**不主张两个 MP4 SHA-256 必然一致**。

## GitHub Actions 云端原始试验产物

- 设计：`docs/project_control/gates/P0_3_video_pipeline/n23_approved_story_shot_single_motion_pilot_design_v0_1_2026-10-14.md`。
- 可复现代码：`scripts/n23_candlelight_motion_control_test_v001.py`。
- 生产工作流：`.github/workflows/n23-candlelight-motion-control-v001.yml`。
- GitHub Actions Run **`38577595269`**：completed / **SUCCESS**，构建及原 PNG 完整性检查 PASS；MP4 和 QC Manifest 在审核分支存储成功。
- 原始云端测试 MP4：`production/motion_tests/n23_candlelight_control_v001/N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001.mp4`。
- 云端 MP4 SHA-256：**`6e8f7411cf40f957bd87c3b69a4304004501a1a6dd103900f574c047a6e830a4`**。
- MP4 字节数：**169,206**。
- Git blob：**`accb833152ee68e687c67558dae8f21c8d7f72f3`**。
- 机器验证 JSON：`production/motion_tests/n23_candlelight_control_v001/N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001_EVIDENCE.json`。
- 原始二进制提交（只有 MP4 + 证据 JSON）：**`55f7b51dd8a0f60118191c8c8e5843f5299dd3f6`**。
- 原始 N23 PNG Blob、V006 视频候选 Blob、正式 Video Index Blob 均未改变。

## 独立 Exact Verification

- 工作流：`.github/workflows/n23-candlelight-motion-control-exact-verify-v001.yml`。
- 初次 Run `38578001723` 在引用 Git 提交差分时因 runner 默认 shallow checkout 缺少历史对象失败；与视频 SHA、原图内容、视频解码无关。
- 修正 `fetch-depth: 0` 后重验 Run **`38578211199`** completed / **SUCCESS**。
- https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38578211199
- 结果日志：
  - `N23_CONTROL_INDEPENDENT_EXACT=PASS`
  - `N23_SOURCE_ORIGINAL_IMAGE=UNCHANGED`
  - `N23_LIGHT_MASK_PROTECTION=PASS`
  - `N23_CANDIDATE_SHA256_AND_BLOB=PASS`
  - `N23_90_FRAMES_DECODE=PASS`
  - `STAGE_B_HUMAN_ANIMATION=NOT_IMPLEMENTED`
  - `V006_CANDIDATE_AND_VIDEO_INDEX=UNCHANGED`
  - `MAIN_NOT_MERGED=TRUE`

## Stage B 人物真实动作仍未实现

已经准备单独的 Work 测试交接，**并未生成视频**：
`docs/project_control/gates/P0_3_video_pipeline/n23_people_and_neil_micro_motion_stage_b_work_test_handoff_v0_1_2026-10-14.md`。

- 目标是在完全同一 N23 机位、开门及人物身份前提下，让**至少两位前/中景诡客真正缓步行进**，而尼尔只做一次极轻微视线/头部调整，维持头颈、十字架、服装一致。
- 目前连接的 Runway 账户查验 `availableVideoModels=[]`，无法通过此连接实际生成 Stage B。不可假称已做或把光线微闪当成人物行走通过。
- 当前正式状态：**Stage A TECHNICAL PASS / PO VISUAL REVIEW PENDING；Stage B BLOCKED / NOT GENERATED**。

## 后续与硬限制

交 PO 先看 Stage A 烛光控制样片，决定变化是否过弱/过强及是否值得纳入以后的动态镜头。若视觉接受并找到可用视频引擎，再依据 Stage B Work 交接生成恰好 **1 条**人物真实动态测试 MP4；生成后停下审核。N23 正式批准 PNG、V006 候选视频、正式 Video Index、main 仍不可变更。

本轮不合并 main、不正式发布动态替换镜头、不修改现有 N23/V006 音轨。
