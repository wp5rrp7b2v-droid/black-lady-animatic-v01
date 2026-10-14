# 《诡舍·黑衣夫人》｜NEW-02 M01 烛光动态 V003｜PO 视觉审核落档

日期：2026-10-14

**决定：PO VISUAL APPROVED — NEW02 V003 CANDLELIGHT ONLY。**
**不代表：已授权替换 V006、N23/N22/NEW-02 正式图片、正式 Video Index、或合并 main。**

## 1. 产品负责人意见和裁定

按连续审核顺序：

1. NEW-02 V001（烛光+13 粒浮尘）：PO 反馈「感觉这次变化不太明显」，不作视觉通过。
2. NEW-02 V002（强化烛光+21 粒浮尘）：PO 反馈「这次又太夸张了，速度太快了，像刚才N23那样的效果就正好」，不作视觉通过。
3. NEW-02 V003：直接复用先前 N23 已认可的烛光速度/节奏/幅度，将动态范围限制在 NEW-02 对应的烛台局部；**完全移除浮尘**。PO 观看后确认「对，这样就可以了」。

此次明确批准的是 **NEW-02 V003 的 M01 烛光环境动态视觉效果**，且该动态策略与 N23 已认可的风格一致。可以将 N23 + NEW-02 V003 作为 M01 模块跨场景应用的两项已通过样例。对新场景仍须单独画遮罩、技术核验和视觉审核，禁止一键批量无审应用。

M03 浮尘模块暂不采用；两版浮尘混合试片的失败不能仅归因于浮尘，但用户对最终**无浮尘**的 V003 认可，后续不得默认开启 M03。

## 2. 被批准的候选 MP4 身份

- GitHub repo：`wp5rrp7b2v-droid/black-lady-animatic-v01`
- 审核分支：`review/s02b-jun-nod-insert-20261014`
- MP4：`production/environment_dynamic/review_candidates/NEW02_M01_N23_PACED_TEST_V003/NEW02_M01_N23_PACED_CANDLELIGHT_TEST_V003.mp4`
- **SHA-256：`64993bca4c0531e86012c6d1a2ec7842c7f82b50a319909c73bb6599e5287ef0`**
- **Git blob：`7dc15c6cbea57b7ebeec5b653e31708e8a42d71f`**
- 字节：175,626；720×1280；30fps；90 帧；3.000 秒；无音轨。
- 原始图：`production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png`
- 原图 SHA-256 `d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`、Git blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`，未经修改。
- 技术验证 JSON：`production/environment_dynamic/review_candidates/NEW02_M01_N23_PACED_TEST_V003/NEW02_M01_N23_PACED_CANDLELIGHT_TEST_V003_EVIDENCE.json`。
- 云端构建 GitHub Actions Run **38586682106** SUCCESS。
- **独立二进制核验 GitHub Actions Run 38587113938 SUCCESS**；检验原始 PNG、V001/V002/V003 MP4、N23 已批准对照、V006 候选和官方 Video Index 均保持原二进制身份。
- 原始视频编码前，限定烛光遮罩以外像素改变量 **0**，最大通道差 **11/255**；首尾 RAW 帧恢复原始画面。
- 参考渲染脚本：`scripts/n23_candlelight_motion_control_test_v001.py`；NEW-02 适配脚本：`scripts/new02_m01_n23_paced_candlelight_v003.py`。

## 3. 后续可复用准则

- **M01 动态模板：N23 PACING / N23 AMPLITUDE**。微弱、自然、不急促、不整幅闪光、不改变整体阴暗氛围。
- **M03 默认关闭**；未经单独设计及批准不得附加浮尘。不要再自动加速或放大环境变化追求“明显”。
- 每个镜头的光源范围单独确认，人物/服装不得运动或变形；原图只读。
- 本次**仅 PO 视觉 APPROVED**，尚未批准作为 V006/未来视频的正式剪辑替换。未来剪辑集成须另行授权。
- M02 阴影、M04 淡雾、M05 音效依然未经测试和批准。

## 4. 发布与同步边界

此记录与必要的模块注册状态更新仅保存至 GitHub 审核分支；不触发新视频渲染、不修改正式 Story Shot / Video Index / V006、无 main merge。PO 对单镜头 V003 的视觉审核至此关闭，其他项目状态不扩大。
