# S02-B｜M01 V017 全片烛火集成候选｜技术通过，待 Product Owner 视觉审核

日期：2026-10-18

## 执行结果

- GitHub Actions：[#39084848061](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39084848061) = **SUCCESS**。
- 输入：`production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4`；SHA-256 `7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402`。
- 输入性质：V006 **重构审片候选**；此前 V005 完整来源无法证实，不能声称对 V005 exact continuation。
- EDL：`production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json`，17 段，1,927 帧，30 FPS，720×1280，全长 **64.25 秒**。
- 单一渲染核心：`scripts/m01_engine_v1.py`，所有候选火苗均通过同一 `calculate_frame()`；烛台坐标、光照 ROI、真实 RGB 连通核心按 Atlas 独立登记，不使用以前被 PO 否决的 V007 错位 mask。
- 本轮执行程序：`scripts/s02b_m01_v017_full_15_shot_candle_review.py`。
- 候选 Atlas：`production/environment_dynamic/m01_engine_v1/M01_S02B_V017_REAL_SOURCE_DRAFT_ATLAS.json`（`CHAT_VISUAL_REAL_VIDEO_MIDFRAME_SOURCE_CENTERS_PREVIEW_ONLY_NOT_PO_APPROVED`）。

## 覆盖与质量

- 既有 PO 已批准视觉样例镜头：N17、N23、NEW-02（均不改动既有通过视频二进制与参考遮罩、配置）。
- 新增本次候选动态镜头（**12 段，未由 PO 视觉审核**）：
  `N16_PART_1`、`N18`、`N20_FIRST`、`V006_NEW_01`、`JUN_APPROVED_REACTION`、`N21`、`N22_FIRST`、`A06`、`N24`、`N25`、`NING_REACTION_APPROVED`、`N26`。
- 未加入烛火效果：`N16_PART_2`、`N19`，原画面保留。
- 15/17 剪辑段有 M01 烛火候选，处理片长 **88.22%**；原片其他内容未强行添加虚假光源。
- 逐镜头源火苗候选检查、原始视频 SHA、视频/音频解码、时序连续性、RAW 区域变更规则、整片双视频二进制 SHA 全部通过。
- 音频 **3013 个 AAC packet** 的内容哈希、PTS、duration 与输入视频一致。
- 保持 **N17 已批准参考**不变；N23 / NEW-02 已通过 V015 参考不变。
- 本轮修改通用核心的 soft fade 边界实现：对非整次幂归零端点返回严格 0，修复 53 帧镜头的浮点 `sin(pi)<0` 导致的复数崩溃；增加覆盖 53 帧及 377 帧的回归测试。已经测试通过。未改动火焰参数或已批准视频。

## 审片媒体 exact SHA-256

根目录：`production/environment_dynamic/review_candidates/S02_B_M01_V017_FULL_LENGTH_ALL_CANDLE_SOURCES_REVIEW`

| 媒体 | 文件 | SHA-256 |
|---|---|---|
| V017 全片候选，720×1280，64.25s | `S02_B_M01_V017_FULL_LENGTH_REGISTERED_CANDLE_PREVIEW_V001.mp4` | `2f12fd18000f8f515f62b7e1d79bd9456d897e69ce22a20398480039e6446327` |
| V006 原片 / V017 烛火候选 A/B，1440×1352，64.25s | `S02_B_M01_V017_FULL_LENGTH_V006_VS_M01_AB_V001.mp4` | `e3f56cd5d07a175384485b272a13a91614e1aaae9deeadea00a89ba114bc1cff` |

核验数据：`S02_B_M01_V017_INTEGRATION_QC.json`。

## 当前判断与后续

- `M01_S02B_FULL_LENGTH_TECHNICAL_GATE = PASS`
- `M01_S02B_NEW_12_CANDLE_LOCATIONS_AND_VISUAL_EFFECT_PO_APPROVED = FALSE`
- `M01_S02B_V017_PO_FULL_VIDEO_VISUAL_APPROVED = FALSE`
- `M01_PERSON_FULL_SEGMENTATION_GROUND_TRUTH = FALSE`
- `M01_CROSS_SCENE_PORTABLE_PRODUCT = NOT_PROVEN`
- `M01_BATCH_RELEASE = HOLD`
- `MAIN_MERGE / MASTER_REPLACEMENT / CANONICAL_STORY_SHOT_REGISTRATION = NOT_AUTHORIZED`

下一步仅请 PO 观看全片 MP4 / A-B，评判是否自然、有无局部跳闪、光源对位穿帮。若 PO 发现缺陷，聚焦具体片段修正，而不是无目的重建整条制图流水线。审片通过也不自动等于跨场景完成。

**禁止**将本次 GitHub Actions 成功误写为用户视觉批准或电影母版已经替换。
