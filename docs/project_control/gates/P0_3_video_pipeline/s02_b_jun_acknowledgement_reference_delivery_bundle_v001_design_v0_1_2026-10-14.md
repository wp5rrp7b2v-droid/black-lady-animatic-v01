# S02-B｜君鹭远认可回应近景｜Reference Delivery Bundle V001 Design V0.1

日期：2026-10-14
正式设计 ID：`S02B_JUN_ACKNOWLEDGEMENT_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
状态：DESIGN PREPARED / VALIDATION-ONLY SPEC STORED / BUILD_AUTHORIZED=false / NO WORK OUTPUT

## 已获 PO 授权范围
- Director Design V0.2 的表达：**近景、下巴微抬、嘴唇自然微张且略含笑意、眼神明亮坚定**，不以静态低头表现“点头动作”。
- 以 V003 已批准完整剪辑为基线：N16/N17 已批准 V004 段落及宁秋水尾部 B V002 均须保留。
- 此授权仅允许 Scene Reference 和 Bundle 设计；不能推导成已授权 Bundle 正式构建、Work 出图或 publication。

## Scene Reference
`docs/project_control/gates/P0_3_video_pipeline/s02_b_jun_acknowledgement_scene_reference_v0_1_2026-10-14.md`

## 直接参考图集合（4/5）
| 优先级 | ID | 来源角色 | 证明边界 |
|---|---|---|---|
| 1 | N20_APPROVED_STORY_SHOT | 上一正式镜头 | 君鹭远浅蓝灰衣着、同行运动、阴暗暖光连续性；不复制 N20 机位 |
| 2 | AST_IMG_000057 | 君鹭远 CHARACTER_REFERENCE_SHEET | 身份、年龄、发型、服装与比例；不参考表排版 |
| 3 | AST_IMG_000072 | 君鹭远 FACE_3Q_LEFT | 面部身份和左 3/4 面五官；具体表情以 PO 本次导演设计为准 |
| 4 | AST_IMG_000108 | CASTLE_ENTRANCE_INNER_LOBBY | 古堡内部材料、灯位家族、克制暗暖光；不制造室外亮光 |

N21 正式镜头作为剪辑下游审阅参考，**不计为直接输入**。
全部资产在 GitHub main Registry/Story Shot Index 为 APPROVED；对应 SHA256、Git blob 和字节数已写入生产 Spec。此处的文档层面对照与 Git blob 取值**不等于 PNG 原始字节 Exact Verification PASS**。

## 技术输入
Spec：`production/bundle_specs/S02B_JUN_ACKNOWLEDGEMENT_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001.json`
- `build_authorized: false`
- Builder：`STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`
- 4 张完整源图；5 张上限。
- 目标：`S02B_JUN_ACKNOWLEDGEMENT_TEST_01 Candidate 01`。
- 候选输出：1×独立 PNG，目标 941×1672（后续单独的 PO 出图授权前不得生成）。
- 身份比对字段：SHA256 + bytes + Git blob，必要的图像格式和尺寸。
- 期望 Validation-only：**4/4**；**当前未运行，不能报 PASS**。

## 任务分解和下一门槛
1. PO 审核 Scene Reference V0.1 和本 Bundle V001 设计；
2. 若 PO 授权，在 GitHub 正式可执行环境运行 Validation-only（`build_authorized=false`），只有 4/4 Exact 才继续；
3. 再单独授权正式 Bundle Build，下载 Artifact 后独立核验；
4. 后续 Work 按已核验 Bundle 生成且仅生成 1× PNG，然后立刻停止，等待 PO；
5. 单图批准后做最小局部剪辑验收，才考虑独立完整 V004 review；不覆盖当前 V003 或已批准 canonical 母版。

## FAIL 处理
- 参考图来源/sha/Git blob 任一不一致：STOP，不改动官方资产；
- 角色身份、明亮坚定眼神、浅笑/嘴唇微张、低调暖光不成立：Candidate FAIL，局部修正，不自动扩量；
- 近景打断 N20→N21 方向、叙事或视觉不自然：暂停新版完整视频，保留 V003 正式审核结论。

未授权时不得写入 main、发布新的 approved binary、Story Shot Index 或 Video Index。
