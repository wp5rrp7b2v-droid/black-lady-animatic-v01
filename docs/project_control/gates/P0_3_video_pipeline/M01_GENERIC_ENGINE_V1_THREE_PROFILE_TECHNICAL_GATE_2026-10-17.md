# M01 通用烛火引擎 V1｜统一核心首轮实测结果

日期：2026-10-17  
执行：GitHub Actions [#39026880994](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39026880994) **SUCCESS**  
分支：`feature/m01-v002-engine-stage-a-20261017`  
状态：**GENERIC_CORE_TECHNICAL_PASS / THREE_REVIEW_VIDEOS_READY / PO_VISUAL_PENDING / S02B_AND_REUSE_RELEASE_HOLD**。

## 实际完成

- `scripts/m01_engine_v1.py`：真正统一的代码执行入口；不包含 N23 / NEW-02 / N17 镜头坐标、剪辑帧号或手工替换专用逻辑。
- `production/environment_dynamic/m01_engine_v1/profiles/`：N23、NEW-02 和 N17 的已知场景光源 Atlas 配置（坐标、灯具身份、ROI、时域可见度、人员排除数据均在配置层）。
- `.github/workflows/m01-engine-v1-unified-three-profile-pilot.yml`：同一 Actions 流程运行 10 项单元和安全回归、三个 exact SHA 输入检查、未知场景返回 CALIBRATION_REQUIRED（fail-closed）、三套渲染和二进制验证。
- 全程保留原始视频、原始 PNG、既有已批准候选和音轨素材不变；无 main 合并或 Canonical Publication。

## 同一引擎实测

| 输入/配置 | 帧数 | RAW改变帧 | RAW最大颜色通道差值 | 结果 MP4 SHA256 | A/B MP4 SHA256 |
|---|---:|---:|---:|---|---|
| N23 | 90 | 85 | 11 | `b83a59622135a33b43f64c3373b76707ac03dbc3d52e4714e62855489d0e1c82` | `f810682b0c3043fde8d63b447d15afc22a4c446444b450d418631ffe61091bd0` |
| NEW-02 | 90 | 88 | 11 | `9db36a8838865768c828f01167d36e65f243686c0c44b1fc42fd4ebcd2433dab` | `5c47006f889da5b6f8c8e882a517e956c854c86b66fec955c45b1db09ad25794` |
| N17 | 377 | 114 | 38 | `238051a55b65ea1481e4241705665a1e8dd0f8fedae131100e836b0c26e89251` | `8d8aa66eeb4fc41a3215bdaff8345bd4ffc7c468e4a355f96825ddcb9658714b` |

候选链接根目录：`production/environment_dynamic/review_candidates/M01_GENERIC_ENGINE_V1_THREE_PROFILE_PILOT/`，每个镜头子目录均含 `M01_ENGINE_V1_PILOT_QC.json`、review MP4 和原始 vs 引擎 A/B MP4。

## Bug 修正履历

首次运行 #39026681049 检出单帧测试假定信号必然可见的错误；修正为时间序列检查。  
第二次 #39026779207 进一步检出 N17 的叠化配置把全片帧号误当成镜头内部帧号；更新 N17 Atlas 为 `[0,261,271,369,376]` 的镜头局部坐标并加入强制范围检查。  
第三次运行 #39026880994：全部单元测试、原始 SHA、未知场景拦截和三段真实 MP4/AB 技术验证通过。

## 尚未达到的产品能力

- 三组样例都用于设计，**不是未见场景 holdout**。不能以此认定跨场景真正复用已验证。
- N23/NEW-02 原来的局部受光 ROI 获得过风格批准，但完整人物 GT 未认证；N17 377帧机器排除遮罩也不等于全部人物无漏检。
- `auto` 目前能安全 `CALIBRATION_REQUIRED`，**不能自主识别任何未知场景**。新场景首次使用需要 Atlas 校准/审核。
- 当前标准化引擎输出是独立版本的预览，不与老三条单镜头脚本的 MP4 二进制相同；尚需 PO 实际视觉审核是否等同或优于已认可风格。
- 统一引擎不代表 S02-B 全片完成。下一道真正有意义的验证是 **一组未用于引擎开发的 S02-B 镜头**（而非继续逐帧 N17），之后再用独立未见过的古堡场景检验。

## 生产门禁

`M01_GENERIC_CORE_TECHNICAL_PASS=TRUE`  
`M01_THREE_NEW_PILOT_VIDEO_PO_VISUAL_APPROVED=FALSE`  
`M01_S02B_PILOT_PASS=FALSE`  
`M01_CROSS_SCENE_REUSABLE_PRODUCT_PASS=FALSE`  
`M01_BATCH_HOLD=TRUE`

本轮写入独立研发分支，禁止在缺乏 PO 视觉认可前把它宣传成完成的一键跨场景产品。
