# P0.2｜Approved-but-Open Tasks V1

Status: `LOCKED / MANDATORY PRE-WAVE2 CLOSEOUT`

Approved by: `PRODUCT OWNER`

Date: `2026-09-13`

## Purpose

本文件专门记录已经由 Product Owner 批准/锁定、但尚未执行完成，且存在被后续生产绕过风险的 P0.2 任务。

Product Owner 于 2026-09-13 明确要求：以下 7 项必须作为下一次正式任务完成；在 7 项全部形成可验证完成证据前，不开启：

`P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT`

这不是新的 Gate，也不改变 P0.2 的审批边界；它是 P0.2 内部的强制前置 Closeout。

## Mandatory approved-open tasks

### AO-01｜4 Canonical Registers Final Reconciliation

核对：

- `SHOT_REGISTER.csv`
- `ASSET_REGISTER.csv`
- `IMAGE_REGISTER.csv`
- `IMAGE_RENAME_MANIFEST.csv`

与当前实际图库、canonical storage、Migration Manifest / Runtime Registry 的一致性。

完成标准：

- 明确每份旧 Register 的 current / historical / superseded 职责；
- 发现的冲突、孤儿记录、重复 Current、旧路径或旧命名均有处理结论；
- 形成可追溯 completion evidence。

### AO-02｜Legacy Character Assets → Long-term Registry / Audit

将 D-059 已发布的 48 张 approved legacy Character references 从“Migration Manifest 可读”推进到长期 Registry / Audit 模型的正式可追溯状态。

完成标准：

- 不破坏 Migration Manifest 的历史证据属性；
- 每个正式 legacy asset 具备稳定 Asset identity / Role / Version / Approval / Lifecycle / Authority / Resolver Usage；
- 与 Runtime Registry 不产生重复 Current；
- 后续 Derived Reference dependency 可直接指向正式 Asset IDs。

### AO-03｜Scene Master Structured Facts + Scene/Costume/Prop/Variant Executable Spec

将两张已批准 Scene Master 的可继承事实字段结构化，并把 Scene / Costume / Prop / State / Variant 规则落到可执行 Registry / Spec。

至少包括：

- `CASTLE_ENTRANCE_OPEN_DOOR_DAY`
- `FIRST_HALL_FIREPLACE`

完成标准：

- 区分 Scene fact 与 Shot photography；
- DAY/NIGHT、门开闭、壁炉状态等受控 State / Variant 不得静默漂移；
- 可被后续 Shot/Task Spec 与 Resolver 读取。

### AO-04｜9 Character Derived Reference Sheets

完成当前记录的 `REFERENCE_SHEET_GAP = 9`。

完成标准：

- 9 名正式 Character 均有符合其 Tier / Current Atomic Assets 的 Derived Character Reference Sheet；
- `derived_from` 指向明确 Asset IDs / versions；
- 上游 Current 被 supersede / deprecated 后可计算 `DEPENDENCY_STALE`；
- Reference Sheet 不反向覆盖 Atomic Master 权威。

### AO-05｜Delivery Bridge

完成 D-060 已明确批准的下一验证方向：

`local Reference Package → image-production / generation environment`

目标不是扩大 Resolver 选图复杂度，而是减少 Product Owner 的人工挑图、上传和搬运。

完成标准：

- Reference Package 能稳定送入实际制图环境；
- 输入资产版本可追踪；
- Product Owner 不再需要逐张手工挑选 Reference；
- 对仍不可避免的“最终结果下载到 Mac”环节要明确边界，不把未完成自动化描述为已完成。

### AO-06｜Real Shot Spec Resolver + Shot-level Audit Reverse Trace

选择至少一个真实 Shot Spec，包含：

- Character；
- Scene；
- 关键 Costume / Prop；
- 必要 State / Variant。

完整验证：

`Shot / Task Spec → Reference Resolver → traceable Reference Package → generation/use record → Audit Trail`

完成标准：

- 可从 Shot 反查当次实际使用的 Asset IDs / versions；
- 可从 Asset 反查该 Shot / production use；
- 验证 `USES_REFERENCE` 等 production-use relation；
- 无人工凭记忆挑图作为正式标准路径。

### AO-07｜GitHub Network Resilience / Recovery Method

对应 Project Risk：`RISK-001｜GitHub Connectivity Instability`。

近期项目多次出现 GitHub 连接异常，包括 443 timeout、`Empty reply from server`、HTTP/2 framing error、`unexpected disconnect` 等。该问题目前虽然可通过 HTTP/1.1 等临时方式缓解，但尚没有稳定、标准、可重复的处理方法。

AO-07 目标不是保证公网永不掉线，而是建立一套**不会因为短暂网络故障而导致资产损坏、重复 ingest、版本分叉或 Project Control 状态误判**的执行方法。

完成标准：

- 建立 GitHub connectivity preflight；
- 锁定标准诊断顺序：DNS / HTTPS / Git remote / HTTP version / proxy / VPN / credential / repo reachability；
- 对已知 HTTP/2 异常提供安全 fallback 到 HTTP/1.1；
- 如代理/VPN端口变化会影响 Git，提供可识别、可恢复的方法；
- pull / push 失败后的 retry 必须 idempotent，不重复写 Registry、不重复分配 Asset ID、不重复 ingest；
- GitHub 暂时不可用时，允许本地结果进入明确的 `PENDING_REMOTE_PUBLICATION`，但不得标记 `REMOTE VERIFIED`；
- 网络恢复后可从已有 commit / ingest receipt 继续发布，不重新执行正式 ingest；
- 至少完成一次受控 failure → recovery 验证；
- 输出轻量 GitHub Network Recovery Runbook，供 Product Owner / Chat / Codex 后续统一使用。

详细风险记录：

`docs/project_control/logs/risk_register.md`

## Execution order

建议按依赖顺序执行：

1. AO-01｜4 Registers Final Reconciliation
2. AO-02｜Legacy Character Assets → Long-term Registry / Audit
3. AO-03｜Scene Master / Scene-Costume-Prop-Variant Executable Spec
4. AO-04｜9 Character Derived Reference Sheets
5. AO-05｜Delivery Bridge
6. AO-06｜Real Shot Spec Resolver + Shot-level Audit Reverse Trace
7. AO-07｜GitHub Network Resilience / Recovery Method

AO-07 可在 AO-01～AO-06 的工程执行过程中同步收集真实网络故障证据，但必须在解除 Wave 2 HOLD 前独立完成验证与 Runbook。

如执行中发现依赖关系需要调整顺序，可以调整，但不得跳过任何一项。

## Resume lock

只有以下条件同时满足，才能恢复：

`P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT`

条件：

- AO-01～AO-07 全部 `COMPLETE / VERIFIED`；
- `RISK-001` 已至少从 `OPEN / HIGH OPERATIONAL RISK` 降级为具备已验证恢复方案的受控风险；
- 对应 Execution / Decision / Gate evidence 已写入 Project Control；
- Daily / Step Closeout consistency check 无未解决状态冲突。

## Non-blocking technical debt

Resolver regression test 当前仍有一项旧断言写死 `AST_IMG_000049`。该技术债应在本轮工程 Closeout 中顺手修正为“断言当前有效版本语义”，但它不替代 AO-01～AO-07 中任何一项。
