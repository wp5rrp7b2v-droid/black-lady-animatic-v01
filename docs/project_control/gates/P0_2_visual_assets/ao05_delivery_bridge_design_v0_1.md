# AO-05｜Delivery Bridge V0.1 Design

Status: `DRAFT / CHAT DESIGN / READY_FOR_PRODUCT_OWNER_REVIEW`

Date: `2026-09-18`

Project: `BLACK-LADY-001 / 诡舍·黑衣夫人`

Gate: `P0.2｜人物锚定与 Scene Master 资产治理`

Task: `AO-05｜Delivery Bridge`

## 1. Purpose

AO-05 验证并建立：

`Reference Resolver / Reference Package → traceable delivery bundle → actual image-production environment`

核心目标不是增加 Resolver 复杂度，而是减少 Product Owner 的人工挑图、逐张上传和版本核对。

AO-05 不改变 AO-04 已锁定的 Character / Scene / Asset authority，也不新增人物事实。

## 2. Delivery authority boundary

Delivery Bridge 只消费上游已经解析完成的正式参考资产。

它不得：

- 自己决定替换 Resolver 已选中的资产；
- 静默使用 SUPERSEDED / DEPRECATED / NEVER 资产；
- 重新编码、重绘、镜像或修改参考 PNG；
- 因传输方便而制造第二套 Asset identity；
- 将 Delivery Proof 输出自动晋级为正式生产资产。

正式选择权仍属于 Resolver / formal Reference Package。

## 3. Delivery unit

AO-05 新增轻量 `Reference Delivery Bundle`，不是新的正式 Asset class。

每个 Bundle 至少包含：

1. `delivery_manifest.json`
   - delivery_id
   - purpose
   - source branch / commit
   - Asset ID
   - entity_id
   - role
   - version_no
   - lifecycle / approval_status
   - canonical storage_uri
   - SHA256
   - byte_size
   - delivery order / responsibility

2. `visual_refs/`
   - 与 formal canonical bytes 完全一致的视觉参考文件；
   - 不重命名为无法反查 Asset 的临时名称；
   - 不修改像素内容。

3. `WORK_HANDOFF.md`
   - 告诉 image-production environment 每张参考图的职责；
   - 明确本轮任务是 delivery validation 还是正式 production；
   - 明确禁止把 `REFERENCE_GAP` 当作已有事实。

Bundle 本身属于 transport / execution artifact，不进入 Formal Asset Registry。

## 4. Primary delivery path

V0.1 首选路径：

`GitHub canonical assets → Delivery Bundle → ChatGPT Work → image-production environment`

原因：

- 当前 TEMP_CLOUD_ONLY_MODE_V1 下本地 Mac 不可作为前提；
- GitHub main 是 SSOT；
- Work 适合读取多份 Project / GitHub 资料并执行真实多步骤交付验证；
- Product Owner 不应再逐张寻找并上传 canonical reference PNG。

Bridge 成功的关键不是“生成了图片”，而是 Work 能够根据 Bundle 自动取得正确 reference bytes，并在生成前验证 Asset ID / SHA /职责。

## 5. Fallback transport

如果 Work 无法直接从 GitHub 私有仓库把 canonical binary materialize 为视觉输入，则允许使用：

`GitHub Actions → short-lived Delivery Bundle artifact → Work`

Fallback 仍必须由 manifest 驱动，且 artifact 中 reference bytes 必须与 canonical SHA 完全一致。

不得回退为 Product Owner 手工挑选多张正式参考图作为 AO-05 的完成标准。

## 6. V0.1 real validation object

首个真实 Delivery Proof 使用：

`CHAR_GUANG_YONG`

理由：

- Tier C Core Set 已完整；
- formal Character Reference Sheet 已存在；
- 不属于当前 P1 Wave 2 production target；
- 可避免 AO-05 delivery test 被误解为提前启动君鹭远正式生产。

Primary visual carrier：

`AST_IMG_000056 / CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

若 Work / image-production environment 需要拆分 Atomic references，必须由 manifest 指明并自动取得，不由 Product Owner 手工挑图。

Delivery Proof 输出：

`AO05_DELIVERY_PROOF_ONLY`

它仅用于证明 reference delivery 已真实进入制图环境；不得 ingest、不得登记为正式 Character Asset、不得影响 Core Coverage。

## 7. Required receipt

真实 delivery 后必须形成 `delivery_receipt.json` 或等价结构化回执，至少记录：

- delivery_id
- environment
- source commit
- received Asset IDs
- received filenames
- received SHA256
- validation result
- generated proof identifier（如实际生成）
- completion timestamp
- manual Product Owner file-upload count

成功标准要求：

`manual Product Owner reference file selection/upload count = 0`

Product Owner 可以做最终视觉确认，但不得承担 routine reference picking / version matching。

## 8. Fail-closed rules

以下任一情况必须停止并标记 validation failure：

- source commit 与 manifest 不一致；
- Asset lifecycle / approval 不满足；
- reference SHA 不一致；
- canonical file 缺失；
- Work 无法确认实际收到的 reference bytes；
- 需要 Product Owner 逐张手工挑选或上传正式参考图才能继续；
- generation environment 无法证明使用的是 manifest 指定输入。

不允许以“看起来像用了参考图”替代 delivery evidence。

## 9. Definition of Done

AO-05 只有以下全部满足才可提交最终验收：

1. 至少一个真实 Reference Delivery Bundle 由 GitHub SSOT 生成；
2. Bundle 中的 Asset IDs / versions / paths / SHA 可精确追踪；
3. Bundle 稳定进入真实 image-production environment；
4. Product Owner 不需要逐张手工挑选或上传正式参考图；
5. image-production environment 对收到的 reference bytes 形成可核验 receipt；
6. 若生成 Delivery Proof，明确保持 NON-PRODUCTION，不进入 Formal Asset Registry；
7. 失败路径 fail closed，不静默换图、不降级为旧版或未批准资产；
8. 明确记录仍然不可自动化的边界，不把部分自动化写成全自动。

## 10. Execution routing

设计阶段继续使用 Chat，不占 D 编号。

真实交付验证建议切换到 ChatGPT Work，因为需要：

- 读取 GitHub / Project 多份资料；
- 获取并核对 reference binaries；
- 执行多步骤 handoff；
- 在实际 image-production environment 中形成 Delivery Proof 和 receipt。

如果需要新增 Bundle builder / workflow / tests，再分配下一 Codex 工程编号 `D-069`。

D-069 在 Product Owner 批准本设计并确认需要工程实现前保持：

`RESERVATION ONLY / NOT ALLOCATED / NOT EXECUTED`

## 11. Boundaries

AO-05 完成不等于：

- AO-06 完成；
- P0.2 PASS；
- P1 Wave 2 自动解除 HOLD；
- P0.3 启动。

AO-05 完成后仍必须执行 AO-06 的真实 Shot Spec Resolver + production-use reverse audit。
