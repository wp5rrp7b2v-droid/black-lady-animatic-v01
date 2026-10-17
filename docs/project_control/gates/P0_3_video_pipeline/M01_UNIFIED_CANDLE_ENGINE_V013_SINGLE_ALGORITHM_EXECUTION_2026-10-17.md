# M01 统一烛火引擎 V013｜单一算法落地执行记录

日期：2026-10-17  
GitHub Actions：[#39043964649](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39043964649) **SUCCESS**  
分支：`feature/m01-v002-engine-stage-a-20261017`  
结论：**UNIFIED_CORE_AND_CALIBRATION_FLOW_TECHNICAL_PASS；NEW_FLAME_LOCATIONS_UNVERIFIED；NO_PRODUCTION_RENDER**。

## Product Owner 决策与纠偏

- PO 明确指出：N17 / N23 / NEW-02 的真实烛火无本质区别。**不允许把输入资产定位程度不同，误解释成两种烛火引擎。**
- N17 原批准视频和 N23 / NEW-02 V012 接受的自然效果是基线；V011 强推 37 RGB 到建筑墙面被拒，永久保留为失败反例。
- 一套算法始终包含相同的独立火苗时间信号、火焰核心控制与局部环境响应；当可视火苗缺少可靠定位，状态为**待校准**，而非激活另一种动画模式。

## 本轮实做成果

1. **基线固定**：`production/environment_dynamic/m01_engine_v1/M01_STYLE_BASELINE_V012.json`，三条参考 MP4 的 exact SHA256；所有旧视频只读、不重新编码。
2. **同一算法的三个 V013 配置**：
   - `profiles/N17_UNIFIED_REGISTERED_REFERENCE_V013.json`：原四支火苗逐帧机器遮罩+PO审过的 F601 中心；保留 GT 不足与非产品化标记。
   - `profiles/N23_UNIFIED_FLAME_CALIBRATION_V013.json`：从现有 V012 ROI 出发，火苗核心尚未登记。
   - `profiles/NEW02_UNIFIED_FLAME_CALIBRATION_V013.json`：同上。
   三组配置均使用 `unsynced_independent` 和同一个引擎 `scripts/m01_engine_v1.py`；差别仅是实际灯具证据与各自的局部受光范围。
3. **安全边界修正**：若 V013 配置声称需要烛火核心但未登记，`--mode pilot` 明确拒绝生成并返回 `CALIBRATION_REQUIRED`；不能把人工猜测的暖点当成实际火苗。
4. **真实像素线索筛选**：`scripts/m01_unified_flame_locator_v013.py` 对两张 source-SHA 锁定的 PNG 原图，在历史已登记的局部 ROI 内用暖色、亮度和局部对比检测提出候选。
5. **可复查图示**：
   - `review_candidates/M01_UNIFIED_FLAME_LOCATOR_V013/N23/N23_UNIFIED_FLAME_CALIBRATION_V013_SOURCE_CANDIDATE_OVERLAY_V001.jpg`
   - `review_candidates/M01_UNIFIED_FLAME_LOCATOR_V013/NEW02/NEW02_UNIFIED_FLAME_CALIBRATION_V013_SOURCE_CANDIDATE_OVERLAY_V001.jpg`
   黄色框＝旧 Atlas 受光搜索区域，紫红圈＝暖亮像素线索（**不等于真火苗**）。无需 PO 逐个手工打点，先作为校准参考。
6. **本次机器结果**：N23：3组灯具ROI，11个亮点候选；NEW02：5组灯具ROI，22个亮点候选。候选重复、火焰个数、人物亮点误识别尚未验证，故仍为 `CALIBRATION_REQUIRED`。

## 下一步严格最小必要工作

- 将同一烛台附近的暖点候选合并、过滤人物与墙面假阳性；依据原图判定实际可见烛火数量，保存可用 core masks。无法确认的灯具标记待校准，不猜位置。
- 在已验证的真实火苗上，用当前统一引擎实现**同一 signal 同时驱动 flame core 和 wall halo**，局部强度以 V012 视觉基线为上限；绝不把 N17 的火苗本体峰值直接施加到整面墙。
- 生成 N23、NEW-02 全新 3秒自然速度 A/B 供 PO 整体观感审核；不因 Actions PASS 直接视为视觉通过。
- 新镜头无需再改公共核心。最后再做未参与研发的 S02-B 和跨古堡场景 holdout，分别通过 PO 审查。

## 治理锁定

- `STYLE_BASELINE_V012 = PO_ACCEPTABLE_REFERENCE`
- `V013_SHARED_CANDLE_ALGORITHM_CONFIG = VERIFIED`
- `N23_NEW02_FLAME_CORE_LOCATION_GT = PENDING`
- `UNIFIED_CORE+HALO_NEW_AB = NOT_RENDERED`
- `S02B_PILOT = HOLD`
- `CROSS_SCENE_REUSABLE_ENGINE = NOT_APPROVED`
- `MAIN_MERGE / STORY_SHOT_REGISTRATION / MASTER_REPLACE = NOT_AUTHORIZED`

本次只执行必要阶段，不把候选热像素的搜集包装为“已经完成跨场景烛火引擎”。
