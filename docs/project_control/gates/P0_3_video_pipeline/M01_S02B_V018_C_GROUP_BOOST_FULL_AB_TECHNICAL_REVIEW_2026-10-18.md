# S02-B｜M01 V018 C 组适度增强｜全片 A/B 技术验收 / 待 PO 视觉审核

**日期：**2026-10-18  
**用户反馈：**「C部分感觉还是不够明显」，随后明确「继续」。  
**范围：**仅增强 12 个 V017 C 组镜头的火苗本体与局部受光幅度；已批准 N17、N23、NEW-02 和不含可登记火苗的 N16 第二段、N19 不变。

## 执行与证据

- GitHub Actions：[#39087681027](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39087681027) = **SUCCESS**。
- 核心仍为 `scripts/m01_engine_v1.py`；V018 调用 V017 已验证 1,927 帧渲染链：`scripts/s02b_m01_v018_c_strength_full_video.py`。
- 未修改剪辑 EDL、17 镜头排序、96 处 C 组光源坐标、RGB 连通火焰检测、受光 ROI、光晕大小、波动时间信号、原音轨。
- V018 配置：`production/environment_dynamic/m01_engine_v1/M01_S02B_V018_MORE_VISIBLE_C_GROUP_DRAFT_ATLAS.json`。
- 对照来源：V017 已交付 64.23s 全片 MP4，SHA-256 `2f12fd18000f8f515f62b7e1d79bd9456d897e69ce22a20398480039e6446327`，原 V017 QC Git blob SHA `dba82d4dc540f0cfb179d2cdc913c30b8d64d899`。

## C 组仅修改两项

| 参数 | V017 | V018 |
|---|---|---|
| 每支火苗 RGB 变化系数 | `[14, 10, 4]` | **`[21, 15, 6]`** |
| 周围局部暖光 RGB 系数 | `[1.6, 0.85, 0.22]` | **`[3.2, 1.7, 0.45]`** |
| 光晕 Gaussian σ | `[21,33]` | **不变** |
| ROI 半径 | `[40,52]` | **不变** |
| 快速高频混合比例 | `0.22` | **不变** |
| 火苗中心、数量、真实像素遮罩检出法 | V017 | **不变** |

修改未将原 N17 火苗最大变化直接复制到建筑墙面；未新增整体画面波动。

## 实际最大单通道变化（源帧 vs 烛光帧）

| C 组镜头 | V017 | V018 |
|---|---:|---:|
| N16 第一段 | 14 | **21** |
| N18 | 15 | **21** |
| N20 第一段 | 13 | **22** |
| NEW-01 | 17 | **24** |
| 君鹭远反应 | 11 | **16** |
| N21 | 16 | **24** |
| N22 第一段 | 15 | **22** |
| A06 | 16 | **24** |
| N24 | 15 | **24** |
| N25 | 15 | **24** |
| 宁秋水反应 | 13 | **20** |
| N26 | 14 | **21** |

12 / 12 个 C 组镜头实际增幅均为正，平均 +7.42 个 RGB 单通道差值。**该指标只表明变化增大，不等于 PO 已认可其自然观感。**

三个既有批准镜头 N17、N23、NEW-02 及两个保留原样镜头，与 V017 的实际原始像素统计（变化帧数、峰值）一致。源视频仍为 SHA `7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402` 的 V006 重构审片候选，不自动等于更早 V005 母版。

## 视频审片文件与 exact SHA-256

目录：`production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/`。

| 视频 | SHA-256 |
|---|---|
| `S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4` | `6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427` |
| `S02_B_M01_V018_FULL_LENGTH_V017_VS_V018_AB_V001.mp4` | `d8606cf08cef31ef3f561818bc93aa0176b8c8b9167669856d42201b52c710d1` |
| `S02_B_M01_V018_FULL_LENGTH_V006_VS_V018_AB_V001.mp4` | `850c76d69b5bd69d5674b50d84d70b03698e972cdf371f048f56b555a998161b` |

三份文件均通过完整 1,927 帧解码、SHA 核对；三份输出音轨 AAC packet 数据与时间戳均与原片一致。

## 未批准项目边界

- `V018_C_GROUP_INTENSITY_ADJUSTMENT_TECHNICAL_PASS = TRUE`
- `V018_C_GROUP_PO_VISUAL_APPROVED = FALSE`
- `V018_FULL_VIDEO_PO_APPROVED = FALSE`
- `V017_ORIGINAL_BINARY_AND_PROJECT_STATE_PRESERVED = TRUE`
- `FULL_PERSON_GT_VERIFIED = FALSE`
- `V018_CANONICAL_VIDEO_REPLACEMENT = NOT_AUTHORIZED`
- `STORY_SHOT_REGISTRATION / MAIN_MERGE = NOT_AUTHORIZED`
- `M01_CROSS_SCENE_PRODUCT_RELEASE = NOT_PROVEN`

**下一步：**PO 审核 **V017 vs V018 全片 A/B**，确认增强是否刚好足够且保持自然；明确确认后方可再按授权进入母片替换或后续环节。
