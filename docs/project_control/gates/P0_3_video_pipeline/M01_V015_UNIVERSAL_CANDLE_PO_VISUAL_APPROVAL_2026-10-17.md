# M01｜V1.5 单一通用烛火引擎双镜头 A/B｜Product Owner 视觉批准

日期：2026-10-17  
Canonical repo：`wp5rrp7b2v-droid/black-lady-animatic-v01`  
研发分支：`feature/m01-v002-engine-stage-a-20261017`  
Build：[GitHub Actions #39046576395](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39046576395) = **SUCCESS**  
Decision：**N23 V015 + NEW-02 V015 PO VISUAL APPROVED — SINGLE CONFIGURABLE ENGINE KNOWN-SHOT PILOT**。

## 1. PO 原话和准确授权范围

本次 PO 在观看 V012 已认可自然版与新增火焰核心动态 V015 A/B 后确认：「**视觉审核OK**」。

按最近上下文和当时提交的两组 A/B，此决定只覆盖：

- **N23**：先前已通过的五支火苗位置，`V015` 新增的真实源像素火焰核心与局部环境联动视觉效果。
- **NEW-02**：先前已通过的十一支火苗位置，`V015` 同样的通用核心+光晕联动视觉效果。
- 两张已批准原图、已认可 V012 视频均保持 **exact 原二进制**；N17 已批准的单镜头视觉参考不变。
- PO 已认可 V015 视频中火苗外观及强弱观感，但并未逐像素批准人物 GT、全部遮罩的历史真实性、不可见/被裁切火苗，也未批准 S02-B 批量、正式剪辑母版替换、Story Shot 发布或合并 `main`。

## 2. 已通过视频 exact identity

Source：`production/environment_dynamic/review_candidates/M01_V015_UNIVERSAL_CANDLE_AB`

| 镜头 | V015 效果 MP4 SHA-256 | V012 与 V015 A/B MP4 SHA-256 |
|---|---|---|
| N23 | `2b5dd22ea0e0a845107963c3a274f1e54d89d546ff01cd5fdcbfc210e9eff801` | `9063b774aea4fc58cdb404f1c98a6e18593c07d2b4947e472358479ea4b5c730` |
| NEW-02 | `db55f740f0fa659c87978dd63cade34443e44365be989c791a27ba08b0e2168a` | `015badfba29dc6da366b583e89f4953920e6d3e81e59a381c7d1d891a4d0d74b` |

具体文件：
- N23：`N23/M01_N23_UNIFIED_CANDLE_PO_REVIEW_V015_REVIEW_V001.mp4`，对比 `N23/M01_N23_V012_BASELINE_VS_UNIFIED_FLAME_V015_AB_V001.mp4`。
- NEW-02：`NEW02/M01_NEW02_UNIFIED_CANDLE_PO_REVIEW_V015_REVIEW_V001.mp4`，对比 `NEW02/M01_NEW02_V012_BASELINE_VS_UNIFIED_FLAME_V015_AB_V001.mp4`。
- Technical QC：`M01_V015_TWO_AB_REVIEW_QC.json`，两镜头 90 帧 / 30fps / 3 秒，来源 SHA 锁定，仅已核准火焰中心对应区域有新增像素变化，未修改 V012 其他原始区域；person ground truth 仍未完成。

## 3. 通用核心成果及产品完成度

- 两个镜头均由 `scripts/m01_engine_v1.py` **同一个渲染核心**生成；区别存在于版本化 Scene Light Atlas / 独立灯具定位、遮罩与参数，而不是两套烛火算法。
- `N23_UNIFIED_CANDLE_PO_REVIEW_V015.json` 与 `NEW02_UNIFIED_CANDLE_PO_REVIEW_V015.json`：前者五个、后者十一个确实可见的火苗中心及机器生成、来源像素约束的核心遮罩；所有被裁切或仍不明的亮点继续排除。
- 已通过：三个**参与研发的已知镜头**的视觉参考（N17、N23、NEW-02）；本轮 N23/NEW-02 的同一核心 A/B 得到 PO 认可。
- 尚未通过：事前未参与调参的镜头 **holdout**、另一个独立古堡环境 **cross-scene**，以及人物和遮挡的完整保护验证。因此 **M01 完整可复用产品 = 未通过**。

## 4. 下一步最小必要工作

1. 在**未参与 M01 V015 调参**的 S02-B 镜头里，先挑一个火苗可见且来源清楚的对象。用**同一引擎、仅配置独立 atlas 和必要遮罩**生成 A/B，PO 确认自然程度。失败时调整证据/配置，不把特定镜头写回核心代码。
2. 再选不同古堡场景的独立可见火苗镜头重复一次，验证跨场景复用。禁止直接拿三个已参与研发的样例冒充 holdout。
3. 仅在前述证据足够和 Product Owner 分别批准后更新引擎产品 gate；批次、正式镜头/视频发布与 `main` 合并均另行授权。**不继续无意义的逐帧点位审查。**

## 5. 项目状态

`N23_V015_PO_VISUAL = APPROVED`  
`NEW02_V015_PO_VISUAL = APPROVED`  
`N17_VISUAL_REFERENCE = PREVIOUSLY_APPROVED_UNCHANGED`  
`M01_UNIFIED_CORE_KNOWN_SHOTS = PROVEN_THREE_EXAMPLES`  
`M01_UNSEEN_S02B_HOLDOUT = NOT_DONE`  
`M01_CROSS_SCENE_REUSE = NOT_DONE`  
`M01_BATCH_GATE = HOLD`  
`M01_CANONICAL_PUBLICATION = NOT_AUTHORIZED`  
`MAIN_MERGE = NOT_AUTHORIZED`
