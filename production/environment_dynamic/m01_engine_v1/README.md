# M01 通用烛火引擎 V1｜架构和验收边界

日期：2026-10-17

**状态：** 独立研发分支首轮可执行版本，尚未获批成为正式跨场景可复用引擎。S02-B 全片批量验收、跨场景盲测及 PO 产品验收仍未通过。

## 核心结构

| 文件/目录 | 职责 |
|---|---|
| `scripts/m01_engine_v1.py` | 唯一通用渲染入口，**不包含 N17/N23/NEW-02 的坐标、时间点及源文件名** |
| `production/environment_dynamic/m01_engine_v1/profiles/` | Scene Light Atlas V1 各场景、镜头源身份与光源版本 |
| `scripts/test_m01_engine_v1.py` | 来源哈希、越界拦截、人物保护、独立频率、时序可见度和确定性回归 |
| `.github/workflows/m01-engine-v1-unified-three-profile-pilot.yml` | 同一个 Action 对多个 Atlas 配置执行诊断及视频/左右 A-B |

**运行模式：**
- `--mode diagnostic --profile <profile>.json`：检查实际二进制来源、光源和保护配置；不渲染。
- `--mode pilot --profile <profile>.json --ab`：通过同一个引擎核心渲染候选 MP4 + 左右原版对照；`REVIEW_ONLY`。
- `--profile auto`：尚未实现经验证的未知场景自动定位，**明确返回 `CALIBRATION_REQUIRED`，不假装自动出图**。
- `--mode review_full`：正式批量能力未解锁时拒绝处理。

### 三组迁移参考
1. **N23**：建筑烛光暖光的局部遮罩与已认可节奏，当前配置只代表 ROI 风格参考，不宣称人物 GT 已通过。
2. **NEW-02 V003**：同一通用核心、五个 scene atlas fixture 配置；保留微弱、缓慢、无浮尘特征。
3. **N17**：F601 四支烛火位置已获 PO 批准；随视频帧位跟踪四支火焰，读已留存的377帧人物分割和火焰 bitpack 蒙版，根据 Atlas 时间可见度曲线渐显。

### 通用引擎约束

- 对每组光源单独计算时序 `signal(t,phase,style)`；每组的 `center/track/roi/phase/visibility` 只来自 Scene Light Atlas。
- 源文件必须经过完整 SHA-256 匹配，失败不可渲染。N17 的逐帧原始 RGB 必须与已有377帧审计一致，保护遮罩二进制也要经过 SHA 核验。
- 所有影像变动只落在 Atlas 授权小范围以及不属于已检测人物/人物框不确定区域的像素，变动在编码前核对。
- 原始图、原始视频只读；音轨尽量与原始镜头节奏同步，但 **V1 N17 审核预览使用 AAC 重新编码**，不宣称与正式母版音频包字节完全一致。
- `ROI_ONLY_UNVERIFIED` 允许研发预览，不得将零外溢像素推断成完整人物保护通过。
- 旧的 N23/NEW-02/N17 单镜头脚本及其哈希成果**保留**，做基线对照，不作破坏性替换。

## 严格区分四个里程碑

1. **Core code executes** — 一套公共逻辑同时处理三组不同输入，自动技术检查 PASS。
2. **S02-B pilot visual accepted** — 除三个已认可参考外，至少新增其他 S02-B 镜头，确认定位/人物及风格可用。此阶段才可考虑正式全片实验。
3. **Cross-scene unseen set accepted** — 未参与研发的真正不同古堡环境，在同一代码、同一 Actions 调度下通过；未知场景有真实检测或明确停止待校准能力。
4. **Product release** — 复用接口、缺失源/误定位安全拦截、最终音视频质量、可追踪二进制产物、PO 产品级通过，才可称 `REUSABLE M01 ENGINE`。

**当前本轮仅尝试里程碑 1**。不把三个已用于建模的样例冒充独立跨场景盲测。不得合并 main、修改正式视频、公开发布或办理 Story Shot 登记。
