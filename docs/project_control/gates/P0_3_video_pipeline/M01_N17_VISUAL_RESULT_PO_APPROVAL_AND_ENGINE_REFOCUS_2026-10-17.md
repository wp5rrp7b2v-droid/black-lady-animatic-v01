# M01｜N17 动态效果视觉批准 & 重返跨场景引擎研发

日期：2026-10-17  
仓库：`wp5rrp7b2v-droid/black-lady-animatic-v01`  
分支：`feature/m01-v002-engine-stage-a-20261017`

## 1. PO 已批准事项与严格边界

PO 查看 N17 原始版与烛火动态版的左右对比 MP4 后明确说：**「批准，但这个结果可以作为烛火引擎复用吗？之前A1是因为N17遗漏了，怎么到了后来变成单独看N17了？」**

正式裁定：**N17 M01 单镜头动态测试 V001 = PO VISUAL APPROVED / ENGINE REUSE = NOT APPROVED**。

所审核素材与二进制：
- M01 效果 MP4：`production/environment_dynamic/review_candidates/M01_N17_CANDLE_MOTION_RESULT_V001/M01_N17_CANDLE_ENGINE_RESULT_REVIEW_V001.mp4`
  - SHA-256：`46eb426b0f01ded40b749d892ec4b85b8f3715450a25fee748779e7185bcdd62`
  - 2,565,913 bytes，377 帧，720×1280，30fps，12.5667s，含 N17 音频。
- N17 左右对照 MP4：`production/environment_dynamic/review_candidates/M01_N17_CANDLE_MOTION_RESULT_V001/M01_N17_ORIGINAL_VS_CANDLE_RESULT_AB_V001.mp4`
  - SHA-256：`bc265e735c07f3d200906bddbd34c737a90f02a829abc48a4b093c6302f48c8f`
  - 2,936,436 bytes，377 帧，左右对照，保留音频。
- GitHub Actions #39021685049 = SUCCESS；候选 QC JSON `M01_N17_CANDLE_ENGINE_RESULT_QC_V001.json` 显示 RAW 人物保护及其检测框不确定区内差异像素=0（**并非证明所有人物像素均被正确识别**）。
- 原始 V006 SHA-256：`7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402`，原视频、原图片、Video Index 均未修改。

**未获准事项：** 不能把这次单镜头视觉认可扩大为 S02-B 全片、自动定位、人像完整 GT、跨场景一键复用通过；不发布正式 Story Shot、不覆盖原视频、不合并 `main`。

## 2. 发现的偏航与纠正措施

A1 原计划是建立 **11镜头共33帧** 的可复核光源与人物验证集，N17 漏定位只是其中一个需要纠正的缺口。后来投入 377 帧和35帧传统尺寸门槛复核、另造 N17 专属视频，属于推进时过度深入。PO 要求停止在 N17 上继续细扣，回到引擎产品目标。

N17 现有试片能证明：在**已知源点**和分帧保护遮罩条件下，独立烛火动态+局部暖光+镜头叠化可以产生 PO 接受的观感。**它还没有证明自动发现烛台或跨镜头零修改复用。**

尤其须明确，试片脚本 `scripts/m01_n17_direct_video_preview_v001.py` 中的 N17 镜头范围、F542–552叠化权重、烛光ROI `x=525..720/y=0..320`、4光源及相应时间设置为**场景专属试验常量**，不得原封不动升级为通用引擎 API。

## 3. 恢复 M01 主线（不增加无意义逐帧门禁）

1. **就地完成 N17 缺口收尾：** 以本视觉批准登记为最终参考样例，不再新增 N17 人工审核或无关阈值修补任务。
2. **通用引擎最小可用版本：** 从已认可的 N23、NEW-02 V003、N17 三种输入迁移共同代码。把静态 ROI/烛火位置/可见度变化从效果核心拆出为版本化 Scene Light Atlas；效果层只读结构化灯具/单火焰/人物排除区域/原始帧，适配新场景无需再写新脚本。
3. **批次验证：** 利用已有 S02-B A0/A1 11镜头测试集确认能自动匹配已登记光源、对未登记或低置信场景明确 `CALIBRATION_REQUIRED`，只修复确实影响视觉的错误；给 PO 看一份有明显变化的短 A/B/批量效果，而不是大量标注图。
4. **跨场景验收：** 从未参与调参的另一个古堡环境中选择真实有烛火的素材，用**同一引擎代码和同一 GitHub Actions 入口**运行；不允许使用 N17 坐标/时码硬编码。只有独立场景获得 PO 认可后才可称为可复用引擎。

**核心目标**：通用定位与可复用动态模板 → S02-B 可用 → 未见场景可用 → 单入口重复执行，别再用无休止的样本级精密审核替代产品开发。

## 4. 状态锁

`N17_M01_VISUAL_RESULT = APPROVED_PO`  
`M01_GENERAL_REUSABLE_ENGINE = NOT_YET_PROVEN`  
`S02B_BATCH = HOLD`  
`CROSS_SCENE_RELEASE = NOT_STARTED`

所有变更仅保存于独立 M01 研发分支。