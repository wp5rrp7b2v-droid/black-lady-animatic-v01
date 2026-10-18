# S02-B｜M01 V018 全片烛火候选｜Product Owner 视觉审核通过

日期：2026-10-18  
分支：`feature/m01-v002-engine-stage-a-20261017`  
决定：**S02-B V018 FULL-LENGTH VISUAL APPROVED**。

## PO 直接批准

Product Owner 于当前对话明确回复：**「V018视觉审核通过」**。

本次决定绑定刚提交的 **V018 全片 1,927 帧 / 30fps / 64.2333 秒** 候选，而非 V017、V006 旧版或未经生成的新版本。该批准确认当前整片烛火观感满足要求，包括原来「C部分不够明显」的 12 段 C 组增强视觉效果。**不再反复修改当前 C 组强度以追求数值统一。**

## 批准的确切媒体及 SHA-256

仓库相对目录：`production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/`

| 范围 | 文件 | SHA-256 |
|---|---|---|
| **PO 视觉批准的 V018 整片视频** | `S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4` | `6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427` |
| 本次 V017 ↔ V018 的审核参考 | `S02_B_M01_V018_FULL_LENGTH_V017_VS_V018_AB_V001.mp4` | `d8606cf08cef31ef3f561818bc93aa0176b8c8b9167669856d42201b52c710d1` |
| 原 V006 ↔ V018 的审核参考 | `S02_B_M01_V018_FULL_LENGTH_V006_VS_V018_AB_V001.mp4` | `850c76d69b5bd69d5674b50d84d70b03698e972cdf371f048f56b555a998161b` |

上面二段 A/B **仅作为审核证据，不是正式剪辑母版**。精确二进制和 1,927 帧、音轨数据已由 GitHub Actions [#39087681027](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39087681027) 技术核验；不重复制造新的转码版本。

## 已批准范围与最终锁定的参数

- 全片 17 段：15 段有可见烛火候选效果，另外 N16_PART_2、N19 两段保留原画面；按 EDL 时间计算动态段覆盖 **88.22%**。
- **N17、N23、NEW-02**：保留原已通过的 A/B 视觉配置及参考二进制。
- 新增的 12 段 C 组：V018 **视觉审核通过**。使用 `core_gain_rgb=[21,15,6]`、`halo_gain_per_flame_rgb=[3.2,1.7,0.45]`。
- C 组的光晕 `sigma_px=[21,33]`、ROI 半径 `[40,52]`、`halo_fast_harmonics_mix=0.22`、每个火苗的独立时间信号与定位沿用 V017，没有扩大整面场景闪动。
- **原音轨 AAC packet 内容、时间戳不变**；原 V006 视频、已批准 Story Shot 的图像二进制均不修改。
- 固定配置：`production/environment_dynamic/m01_engine_v1/M01_S02B_V018_MORE_VISIBLE_C_GROUP_DRAFT_ATLAS.json`；同一渲染核心：`scripts/m01_engine_v1.py`。
- QC：`production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_INTEGRATION_QC.json`。

## 审批边界和下一步

**已批准：**这份 exact V018 全片审片候选的视觉效果，包括 C 组增强强度。V017 尚未取代 V018，V018 后续任何会改变画面的修改均需重新审核。

**尚未授权：**覆盖或替换现行正式视频母版、正式 Canonical Publication、Story Shot 登记、合并 `main`、删除历史成果、认定人物遮挡逐像素 GT 已完整，或者宣布跨场景通用产品通过。

`M01_V018_S02B_FULL_VIDEO_PO_VISUAL = APPROVED`  
`M01_V018_C_12_SHOTS_PO_VISUAL = APPROVED`  
`M01_V018_APPROVED_REFERENCE_BINARY = LOCKED`  
`S02B_CANONICAL_MASTER_REPLACEMENT = NOT_AUTHORIZED`  
`MAIN_MERGE = NOT_AUTHORIZED`  
`M01_CROSS_SCENE_PORTABILITY = NOT_VALIDATED`

**下一任务：**依据项目正式剪辑/发布政策核对现有母版归属，提交一次简明发布方案给 PO 决定；无需再用无关测试拖延 V018 已作出的视觉批准。
