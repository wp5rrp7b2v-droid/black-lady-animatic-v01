# 《诡舍·黑衣夫人》｜NEW-02 环境微动态 V001 反馈及 V002 候选审核收据

日期：2026-10-14  
状态：**V001 VISUAL FEEDBACK = TOO SUBTLE / V002 TECHNICAL PASS / V002 PO VISUAL REVIEW PENDING / NO MAIN MERGE**

## PO 反馈

Product Owner 观看 `NEW02_M01_M03_ENVIRONMENT_MOTION_TEST_V001.mp4` 后表示：「感觉这次变化不太明显」。

此反馈不等于 V001 视觉通过，亦不影响 N23 单独已经确认的 M01 烛光视觉基线。V001 继续保留技术验证结果及原视频供历史审计，不升级为通过的 M03 通用基线。

## V002 调整

只做这一轮 1 条新的独立审核 MP4，不改变 V001 或原批准图片：
- NEW-02 原 PNG 唯一输入：`production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png`，**1,963,410 bytes**，SHA256 `d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`，Git blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`。
- 局部烛光强度相较 V001 增至约 2.75–3.2 倍，光强渐入渐出从整段大幅收缩至 **0.32 秒**；不同烛光不同步。
- 浮尘从 **13** 粒到 **21** 粒，扩大但仍受控制的半径与速度，严格限制在上方无人建筑受光区域。
- V001 编码前 RAW RGB 最大通道差 **11** → V002 **32**；允许变化区域占视频画面约 **10.43%**，区域外编码前像素变化为 **0**。
- 禁止人物/服装/门/建筑几何变形；不动画人物，不加音频，不改 V006 或正式 Video Index。
- V002 保持 4 秒，720×1280，30fps，120帧；首尾编码前 RGB 帧回归源图基准。
- V001 渲染脚本及候选 MP4 不覆盖，新增 `scripts/environment_dynamic_render_v002.py`、`production/environment_dynamic/shot_profiles/NEW02_M01_M03_TEST_V002.json`。

## 云端生成与锁定结果

- Workflow：`.github/workflows/new02-environment-motion-m01-m03-test-v002.yml`。
- GitHub Actions Run **`38585438537`** SUCCESS；来源 PNG Exact、单测试 MP4、全片解码、仅两个测试目录新文件提交 PASS。
- Artifact ID **`11906135519`**；Artifact ZIP **286,833 bytes**，sha256 **`4424fe6737468f7a448648889dd627f43c706990ce5c6b270204dfc303913b4f`**。
- GitHub 审核视频：`production/environment_dynamic/review_candidates/NEW02_M01_M03_TEST_V002/NEW02_M01_M03_ENVIRONMENT_MOTION_TEST_V002.mp4`。
- 原始云端 MP4 **287,168 bytes**，SHA256 **`f87a7ac14c10c643b6b0e83f80181865caec83211a2ab8cc18d21a0b85210a97`**，Git blob **`2520fa25cbf0fac4e80eafc13076d6002c6f39cf`**。
- 随附 QC JSON：`production/environment_dynamic/review_candidates/NEW02_M01_M03_TEST_V002/NEW02_M01_M03_ENVIRONMENT_MOTION_TEST_V002_EVIDENCE.json`。
- 独立下载实际 Artifact ZIP 后 CRC PASS、ZIP SHA256 与 GitHub 匹配；提取 MP4 的 SHA256 和字节数与 GitHub 原始候选和机器证据完全匹配。独立 ffprobe：4.0s / 120f / 30fps / 720×1280。
- N23 已批准烛光自然度标准保持有效；V002 视觉效果尚待 PO 观看评判。
- NEW-02 批准原 PNG Git blob、V001 测试 MP4、V006 候选 MP4 Git blob 均保持不变；正式 Video Index 未修改；main 未合并。

**结论：V001 视觉增强不足，V002 已交付审核；仅技术通过，不宣称 PO 视觉通过。**
