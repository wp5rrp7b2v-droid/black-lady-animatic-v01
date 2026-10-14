# NEW-02｜环境动态测试反馈与 N23 节奏对齐 V003｜2026-10-14

状态：**V002 PO REJECTED AS TOO FAST / V003 RENDERED TECHNICALLY VERIFIED / V003 PO VISUAL REVIEW PENDING**。

## PO 的明确视觉反馈

- NEW-02 V001 烛光+浮尘：**「感觉这次变化不太明显」**（视觉强度不足，不自动批准）。
- NEW-02 V002 烛光+浮尘：**「这次又太夸张了，速度太快了，像刚才N23那样的效果就正好」**。
- 权威观感参考是此前 PO 明确认可的 **N23 Stage A** 3 秒烛光动态样片；不是让 NEW-02 在 V001/V002 两种参数之间机械取平均。

## V003 已执行的针对性修正

**V003 只保留 M01 烛光，不包含 M03 浮尘。** 相较 V002：
- 删除快速飘动的全部 21 粒浮尘，`dust_particles=0`；
- 完整复用 `scripts/n23_candlelight_motion_control_test_v001.py` 的 **3 秒/90 帧、N23 正弦频率、N23 首尾柔和包络、RGB 暖色变化比例 12:7:1.7**；
- NEW-02 具体烛台的局部遮罩仍由已批准 NEW-02 V001 配置适配；**不照搬 N23 的空间坐标**，不覆盖人物区域；
- 将 V002 最大通道差 32/255 恢复为 **11/255**，不全图提高曝光；
- 只输出 1× 720×1280、30fps、3.000 秒 MP4，无音轨，不做真实人物行走或摄影机运动；
- 原始已批准 NEW-02 PNG、已批准 N23 PNG、历史 V001/V002 试片和 S02-B V006 候选均未修改。

## 唯一原始测试产物

- 制图/视频脚本：`scripts/new02_m01_n23_paced_candlelight_v003.py`
- GitHub Actions: `38586682106` **SUCCESS**。
- 审核分支：`review/s02b-jun-nod-insert-20261014`。
- 审核 MP4：`production/environment_dynamic/review_candidates/NEW02_M01_N23_PACED_TEST_V003/NEW02_M01_N23_PACED_CANDLELIGHT_TEST_V003.mp4`
- 同文件夹技术验证 JSON：`NEW02_M01_N23_PACED_CANDLELIGHT_TEST_V003_EVIDENCE.json`
- MP4 SHA256：`64993bca4c0531e86012c6d1a2ec7842c7f82b50a319909c73bb6599e5287ef0`
- MP4 Git blob：`7dc15c6cbea57b7ebeec5b653e31708e8a42d71f`
- MP4 **175,626 bytes**，90 帧，3.000 秒，720×1280。
- 原已批 NEW-02 SHA256：`d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`，Git blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`。
- 编码前 RAW RGB 指定烛台遮罩外变更像素数：**0**；最大通道变化：**11**；首尾帧与初始视频基准一致。
- V006 原候选 Git blob：`d92d23ac6b5a542e07572e29a9e648e2c4141854`，未改变。
- 重新获得 PO 视觉认可之前，V003 只能称作独立审核视频，不能加入 V006 或替代 M01 基线。

## 操作权限界限

本轮没有新 Story Shot 生图、没有修改批准的 PNG、没有修改正式视频与原始音轨、没有合并 main、没有将 V003 认定为 PO-approved 环境动态模块。**等待 PO 观看 V003 后决定。**
