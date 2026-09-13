# D-060｜REFERENCE_PACKAGE_EXPORTER_V0.1｜人物制图最小参考包导出试验

Status: `TEST APPROVED / PRODUCT OWNER APPROVED`

Date: `2026-09-13`

## 目标

验证能否根据 `Character Entity + Target Role`，自动从 canonical Character asset storage 与 Migration Manifest 中选择正式可用参考资产，并生成用于后续制图的最小 Reference Package。

本轮不实现完整 Reference Resolver，不自动上传到 ChatGPT，不调用图片生成，也不修改正式 Character assets。

## 测试对象

- Entity: `CHAR_NING_QIUSHUI`
- Target Role: `PROFILE_LEFT`
- Target Role Status: `REFERENCE_GAP`
- Exporter: `scripts/reference_package_exporter_v0_1.py`
- Command: `python3 -B scripts/reference_package_exporter_v0_1.py --entity CHAR_NING_QIUSHUI --target-role PROFILE_LEFT`

## 输出

Local test package:

`tmp/reference_packages/P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT/`

输出包含 4 张 PNG + `package.json`。

## 自动选中的参考资产

1. `CHAR_NING_QIUSHUI_FACE_FRONT_DEFAULT_DEFAULT_V001.png`
   - Role: `FACE_FRONT`
   - Reason: 身份与正面五官主锚点

2. `CHAR_NING_QIUSHUI_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`
   - Role: `PROFILE_RIGHT`
   - Reason: 相反方向侧脸结构

3. `CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
   - Role: `FACE_3Q_RIGHT`
   - Reason: 头脸立体结构辅助

4. `CHAR_NING_QIUSHUI_BODY_FRONT_DEFAULT_DEFAULT_V001.png`
   - Role: `BODY_FRONT`
   - Reason: 体型、服装与整体结构

## 验证结果

- Selected asset count: `4`
- Canonical source only: `PASS`
- Approval / Mapping / Lifecycle filters: `PASS`
- SHA-256 source / copy / manifest consistency: `4 / 4 PASS`
- Duplicate CURRENT conflict: `NONE`
- Formal source asset modification: `NONE`
- Target Role `PROFILE_LEFT` correctly identified as `REFERENCE_GAP`
- `REAR_3Q_RIGHT` 存在两个不同 variant 的 CURRENT 资产，但本包未使用，不构成 Single Current 冲突。

## Product Owner 审批

Product Owner 于 2026-09-13 明确批准本次测试。

正式结论：

`REFERENCE PACKAGE AUTO-SELECTION + LOCAL PACKAGING = VALIDATED FOR V0.1`

这只证明：

`Canonical Character Assets → automatic selection → local Reference Package`

可行。

本测试**不证明**：制图 Chat 已能自动从 GitHub 接收并读取这些图片作为视觉参考输入。

## 下一验证方向

建议后续进入 Delivery Bridge V0.2，单独验证：

`GitHub canonical references / local synced assets → Reference Package → image-production environment delivery`

V0.2 的成功标准应以“减少 Product Owner 人工上传、挑图、搬运”为核心，而不是继续扩大选图规则。

D-060 V0.1 已经 Product Owner 批准；是否启动后续工程任务需由主流程另行决定。
