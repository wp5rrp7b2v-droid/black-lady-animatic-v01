# P0.2｜Approved-but-Open Tasks V1

Status: `LOCKED / MANDATORY PRE-WAVE2 CLOSEOUT`

Approved by: `PRODUCT OWNER`

Date: `2026-09-13`

Latest closeout update: `2026-09-18`

## Purpose

本文件专门记录已经由 Product Owner 批准/锁定、但尚未执行完成，且存在被后续生产绕过风险的 P0.2 任务。

Product Owner 于 2026-09-13 明确要求：以下 7 项必须作为正式前置 Closeout；在全部形成可验证完成证据前，不开启：

`P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT`

这不是新的 Gate，也不改变 P0.2 的审批边界；它是 P0.2 内部的强制前置 Closeout。

## Mandatory approved-open tasks

### AO-01｜4 Canonical Registers Final Reconciliation

Status: `COMPLETE / VERIFIED` (BL-D-028; remote decision/evidence commit `43d8fa4` verified by fetch).

四份旧 CSV 当前均不可取得，Product Owner 决定其退出 Current authority。旧表内部孤儿行、重复行、旧路径/命名一律 `UNKNOWN / SOURCE UNAVAILABLE`；不重建旧表。Current Shot composition 由正式 Shot Spec 重建并在 AO-06 验证。

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

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-14`

Completion evidence:

`ao02_legacy_asset_registry_migration_v1.md`

结果：

- D-059 的 48 张 `CONFIRMED + APPROVED` legacy Character assets 已确定性回填为 `AST_IMG_000001–000048`；
- 既有 Runtime `AST_IMG_000049–000051` 保持不变；
- post-migration Asset Registry = `51` 条；
- Single Current / SHA / storage validation PASS；
- D-059 Manifest 与人物 PNG 未修改；
- migration idempotency / rollback tests PASS；
- migration commit `4803b928baaa38d875e9c6edd46f4a458e627b61` 已 `REMOTE VERIFIED`；
- Product Owner 于 2026-09-14 明确批准 AO-02。

完成标准：

- 不破坏 Migration Manifest 的历史证据属性；
- 每个正式 legacy asset 具备稳定 Asset identity / Role / Version / Approval / Lifecycle / Authority / Resolver Usage；
- 与 Runtime Registry 不产生重复 Current；
- 后续 Derived Reference dependency 可直接指向正式 Asset IDs。

### AO-03｜Scene Master Structured Facts + Scene/Costume/Prop/Variant Executable Spec

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-17`

AO-03A｜Fact Boundary + Executable Spec Design V0.1 已由 Product Owner 于 2026-09-15 明确批准并落档：

`ao03_scene_executable_spec_design_v0_1.md`

AO-03B｜Two Scene Master Structured Facts Definition 已由 Product Owner 于 2026-09-17 批准。

D-067 已完成：

- `SCENE_CASTLE_ENTRANCE` / `SCENE_FIRST_HALL` executable Entity；
- approved legacy/source alias 保留；
- Stable Scene Facts / Controlled State / Shot Photography 分离；
- `AST_IMG_000052` / `AST_IMG_000053` formal Scene Master mapping；
- multidimensional Scene State Profile；
- state-aware Resolver；
- state mismatch / absent state → `REFERENCE_GAP`；
- Character resolver / ingest / supersession / reference-package regression 保持通过；
- full test suite：`54 tests / OK`；
- 两张 Scene Master 原图 SHA 保持不变，仅 100% Git rename/move。

Completion evidence:

- `ao03_closeout_2026-09-17.md`
- PR `#6｜AO-03: add executable Scene registry and state-aware resolver`
- merge SHA `b16ffdd5f1c57f0b2c28acdee3caac656afb91a3`
- closeout evidence commit `6d87401984b7dfe5f4a75db7b262f4fc684de9e5`

至少包括：

- legacy/source alias `CASTLE_ENTRANCE_OPEN_DOOR_DAY` → `SCENE_CASTLE_ENTRANCE`
- legacy/source alias `FIRST_HALL_FIREPLACE` → `SCENE_FIRST_HALL`

完成标准已验证：

- Scene fact 与 Shot photography 分离；
- DAY/NIGHT、门开闭、壁炉状态等受控 State / Variant 不得静默漂移；
- 可被后续 Shot/Task Spec 与 Resolver 读取；
- Castle Entrance + DAY + OPEN → eligible Scene Master；
- Castle Entrance + CLOSED / NIGHT → `REFERENCE_GAP`；
- First Hall + FIREPLACE_EXTINGUISHED → eligible Scene Master；
- First Hall + FIREPLACE_BURNING → `REFERENCE_GAP`；
- explicit required state 不被 `UNSPECIFIED` 静默满足。

### AO-04｜9 Character Derived Reference Sheets

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-18`

AO-04A approval evidence: PR #8, merge SHA `a336cc46e3d81045e990ade7c67e0ec3eea50485`. Stage A produced nine deterministic Candidate Sheets from 42 live CURRENT/APPROVED/DEFAULT Atomic inputs with 21 explicit gaps; Product Owner visually approved all 9 on 2026-09-18. Stage B then formalized `AST_IMG_000054–000062` as 9 formal CURRENT / APPROVED `DERIVED_REFERENCE / CHARACTER_REFERENCE_SHEET` assets, created 42 `DERIVED_FROM` relations and 9 `ASSET_FORMALIZED` events, and published the 9 canonical PNG binaries atomically with Registry / lineage / audit in commit `09b9e2c44f8f2f78c1d102f3d141263074316310`. GitHub Actions validation confirmed all 9 dependency states `FRESH`, resolver resolution PASS, second formalizer run `ALREADY_FORMALIZED`, and full suite `68 tests / OK`. Product Owner completed final AO-04 DoD acceptance on 2026-09-18. AO-04 is now COMPLETE / VERIFIED / PRODUCT OWNER APPROVED.

完成当前记录的 `REFERENCE_SHEET_GAP = 9`。

完成标准：

- 9 名正式 Character 均有符合其 Tier / Current Atomic Assets 的 Derived Character Reference Sheet；
- `derived_from` 指向明确 Asset IDs / versions；
- 上游 Current 被 supersede / deprecated 后可计算 `DEPENDENCY_STALE`；
- Reference Sheet 不反向覆盖 Atomic Master 权威。

### AO-05｜Delivery Bridge

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-18`

完成 D-060 已明确批准的下一验证方向：

`local Reference Package → image-production / generation environment`

目标不是扩大 Resolver 选图复杂度，而是减少 Product Owner 的人工挑图、上传和搬运。


Primary Delivery Path Proof（2026-09-18）已 PASS：

- Work 从 GitHub `main` 自动取得 `AST_IMG_000056 / CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`；
- 475,761 bytes；SHA256 与 Formal Asset Registry 完全一致；
- reference binary 已真实加载进入 Work 的 image-production environment；
- 成功生成一张 `AO05_DELIVERY_PROOF_ONLY` NON-PRODUCTION 验证图；
- Product Owner 手工 reference file selection / upload count = `0`；
- 未修改 GitHub、Registry、正式 Asset；未分配 D-069。

当前仍需验证多文件交付与重复运行稳定性，之后才可提交 AO-05 最终验收。

Robustness Proof（2026-09-18）结果：

- RUN A 在 canonical binary materialization 阶段 fail closed；
- `AST_IMG_000056` 的 Reference Sheet 可返回 Base64，但未完成本轮统一 materialization；
- `AST_IMG_000011 / 000009 / 000008` 三张较大的 Atomic PNG 经当前 Work GitHub file/blob/raw API 无法取得可哈希的二进制内容；
- 因此 0/4 完成独立 SHA 校验，generation environment 未被调用；
- RUN B 未启动；Product Owner manual upload count 仍为 `0`；
- 该失败只定位于 binary transport，不证明 multi-reference generation 不受支持。

下一步按 AO-05 V0.1 已定义 fallback：
`GitHub Actions → manifest-verified short-lived Delivery Bundle artifact → Work`。

Fallback Artifact Bridge（2026-09-18）已成功建立：

- GitHub Actions workflow：`.github/workflows/ao05-fallback-artifact-bridge.yml`；
- successful run：`35319662012`；
- artifact：`AO05_GUANG_YONG_DELIVERY_BUNDLE_V001`；
- artifact ID：`10536850548`；
- artifact size：`9,094,747 bytes`；
- artifact digest：`sha256:a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`；
- retention：7 days，expires `2026-09-25`；
- source commit：`775238d05278af963d6e673063ce71ae522c18d1`；
- Bundle 内 4/4 formal reference binaries 在 GitHub runner 中已按 Registry ID / state / SHA256 / byte size 验证并在 upload 前再次验证。

当前下一步：Work 自动下载该 artifact，解包后独立复核 manifest + 4 个 reference bytes，再执行 RUN A / RUN B 多图 + repeatability proof。Product Owner reference upload count 仍必须为 0。

Fallback Robustness Proof（2026-09-18）已 PASS：

- Work 自动下载 artifact `10536850548`，Product Owner 无需上传 ZIP 或 reference；
- ZIP digest 独立验证为 `a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`；
- RUN A：4/4 binaries materialized，4/4 SHA match，loaded_reference_count=4，proof generated，manual upload=0；
- RUN B：独立重新读取同一 ZIP、解包到独立目录并重算 4/4 SHA；输入 Asset IDs / SHA 与 RUN A 完全一致；loaded_reference_count=4，proof generated，manual upload=0；
- multi-reference delivery = PASS；repeatability = PASS；
- 两张 proof 均为 NON-PRODUCTION；未修改 GitHub / Registry / Core Coverage；未分配 D-069。

证据边界：image generation service 未返回独立 input-SHA receipt；现有证据链为 GitHub Actions canonical-byte verification + artifact ZIP digest + Work 侧独立 SHA verification + 实际 4-reference generation call。两轮重复证明当前路径可重复，但不宣称无限期长期稳定。

完成标准：

- Reference Package 能稳定送入实际制图环境；
- 输入资产版本可追踪；
- Product Owner 不再需要逐张手工挑选 Reference；
- 对仍不可避免的“最终结果下载到 Mac”环节要明确边界，不把未完成自动化描述为已完成。

### AO-06｜Real Shot Spec Resolver + Shot-level Audit Reverse Trace

Status: `IN PROGRESS / STAGE 3 ENGINEERING FOUNDATION COMPLETE / BLOCKED_ON_APPROVED_A04_BINARY / BLOCKED_ON_COSTUME_PROP_EVIDENCE`

Stage 1 recommendation（2026-09-18）：

- canonical validation Shot: `A04`;
- formal Character anchors: `AST_IMG_000060 / CHAR_NING_QIUSHUI CHARACTER_REFERENCE_SHEET` + `AST_IMG_000059 / CHAR_NEIL CHARACTER_REFERENCE_SHEET`;
- formal Scene anchor: `AST_IMG_000052 / SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`;
- current runtime gaps independently verified: `SHOT assets=0 / PROP assets=0 / COSTUME assets=0`;
- therefore Stage 1 does not pretend A04 Shot Asset, Neil costume, cross or handkerchief are already formal runtime assets;
- A04 is used to test two-character + scene + costume/prop boundary without the crowd complexity of A01 or the scene-thin framing of A05;
- exact camera/lens/shot-size fields are not promoted to stable Scene Facts and must be taken only from the approved A04 Shot source when that source is formally materialized for Stage 2/3.

Detailed evidence:
`ao06_stage1_shot_selection_fact_boundary_v0_1.md`.

Stage 1 Product Owner approval（2026-09-18）：

- canonical AO-06 validation Shot = `A04`；
- Scene = `SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`；
- Characters = `CHAR_NING_QIUSHUI + CHAR_NEIL`；
- Neil default butler costume + cross + white handkerchief are valid continuity requirements but remain current formal runtime gaps；
- A04 does not inherit A05's keys-absent insert fact；
- exact Shot photography must come from approved A04 evidence and may not be inferred from Scene Master or chat memory。

Stage 2 next：`A04 Real Shot Spec V0.1 + Resolver Contract`。

Stage 2 design candidate（2026-09-18）：

- A04 Shot Spec 把 Character / Scene / Costume / Prop / action / photography-evidence 分开表达；
- required Character：`CHAR_NING_QIUSHUI + CHAR_NEIL`，默认解析各自 CURRENT/FRESH `CHARACTER_REFERENCE_SHEET`；
- required Scene：`SCENE_CASTLE_ENTRANCE` + `DAY_DOOR_OPEN`；
- required Costume/Prop：`COSTUME_NEIL_DEFAULT`（含 white pocket handkerchief continuity）+ `PROP_NEIL_CROSS`；当前预期均返回 `REFERENCE_GAP`；
- 任何 required gap 都使 package `generation_allowed=false`，不得用 Character image 静默替代；
- approved A04 evidence 必须在 Stage 3 materialize 后才能锁定 exact Shot photography；
- Historical A04 不允许事后编造 `USES_REFERENCE`；AO-06 当前真实 use 先写 immutable validation use record，并在隔离事务中验证 relation/reverse-query 逻辑；只有存在可证明的新 formal output 时才写 live `USES_REFERENCE`。

Detailed design：`ao06_stage2_a04_real_shot_spec_resolver_contract_v0_1.md`。

Stage 3 D-069 first-run checkpoint（2026-09-18）：

- executable `A04_SPEC_V001`、fail-closed Shot resolver/package、immutable use-record/reverse-audit tooling 已实现；
- formal anchors `AST_IMG_000060 / 000059 / 000052` resolve；
- stable Costume/Prop Entities 已创建，但没有伪造 visual Assets；
- current truthful package remains `BLOCKED / generation_allowed=false`；
- current tree、`git log --all --name-only` 与 `git rev-list --objects --all` 未找到可证明为 exact approved A04 的 binary；
- 未找到 dedicated approved Costume/Cross reference；Character Sheet 中可见内容不被冒充为 formal Costume/Prop Asset；
- live `USES_REFERENCE` unchanged；isolated transaction validates direction/reverse query/duplicate rejection/rollback。

Stage 2 Product Owner approval（2026-09-18）：

- A04 Real Shot Spec V0.1 structure approved；
- Ning / Neil Character Reference Sheets + Castle Entrance DAY_DOOR_OPEN are required resolved references；
- COSTUME_NEIL_DEFAULT + PROP_NEIL_CROSS are required and any REFERENCE_GAP blocks generation；
- white pocket handkerchief remains a Costume component；
- approved A04 source evidence is mandatory for exact Shot photography and may not be recreated；
- blocked diagnostic package may be emitted but `generation_allowed=false`；
- historical A04 receives no fabricated historical `USES_REFERENCE`；
- current AO-06 actual use goes to immutable validation use record；live `USES_REFERENCE` requires a genuinely approved formal output with provable inputs；
- Stage 3 engineering may allocate `D-069`。

Next：`D-069｜AO-06 Stage 3 implementation + real validation`。


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

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-14`

对应 Project Risk：`RISK-001｜GitHub Connectivity Instability`。

已完成并验证：

- GitHub connectivity preflight；
- 标准诊断顺序：DNS / HTTPS / Git remote / HTTP version / proxy / VPN / credential / repo reachability；
- HTTP/1.1 安全 fallback；
- 动态代理端口识别与恢复；
- pull / push 失败后的 idempotent retry 规则；
- `PENDING_REMOTE_PUBLICATION` 进入、退出与恢复发布流程；
- push ACK loss / remote mismatch 处理；
- 真实 transient failure → recovery 等价受控恢复证据；
- lightweight GitHub Network Recovery Runbook；
- Product Owner 于 2026-09-14 明确批准 AO-07。

Completion evidence:

`ao07_github_network_resilience_progress_v1.md`

RISK-001 正式降级为 `CONTROLLED / MITIGATION VERIFIED`。

## Execution order

当前依赖顺序：

1. AO-01｜COMPLETE / VERIFIED
2. AO-02｜COMPLETE / VERIFIED / PO APPROVED
3. AO-03｜COMPLETE / VERIFIED / PO APPROVED
4. AO-04｜COMPLETE / VERIFIED / PRODUCT OWNER APPROVED
5. AO-05｜COMPLETE / VERIFIED / PRODUCT OWNER APPROVED
6. AO-06｜IN PROGRESS / STAGE 2 PO APPROVED / D-069 STAGE 3 NEXT
7. AO-07｜COMPLETE / VERIFIED / PO APPROVED

AO-07 已提前完成；AO-03 于 2026-09-17 完成。当前剩余主依赖链：

`AO-06`

如执行中发现依赖关系需要调整顺序，可以调整，但不得跳过任何一项。

## Resume lock

只有以下条件同时满足，才能恢复：

`P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT`

条件：

- AO-01～AO-07 全部 `COMPLETE / VERIFIED`；
- `RISK-001` 已至少从 `OPEN / HIGH OPERATIONAL RISK` 降级为具备已验证恢复方案的受控风险；
- 对应 Execution / Decision / Gate evidence 已写入 Project Control；
- Daily / Step Closeout consistency check 无未解决状态冲突。

当前 AO-01、AO-02、AO-03、AO-04、AO-05、AO-07 已满足；Wave 2 仅由 AO-06 阻塞。

## Non-blocking technical debt

Resolver regression test 已在 AO-01 改为断言 `AST_IMG_000050` 为 CURRENT V002、`AST_IMG_000049` 为 SUPERSEDED，但它不替代 AO-01～AO-07 中任何一项。

## Execution Routing

根据 RC-015，Approved-but-Open 任务不因带有“工程”属性就自动交给 Codex。方案、判断、Task Contract、GitHub 可直接更新内容优先由 Chat 完成；pull / status / test / dry-run / 已有脚本执行 / SHA 验证等由 Terminal 完成；只有确实需要本地多文件工程修改、环境交互或持续调试时才交给 Codex。只有实际交给 Codex 执行的任务才占用 D-###。

## AO-05 Accepted Residual Limitation

- `SERVICE_INPUT_SHA_RECEIPT = NOT AVAILABLE`.
- 当前 image-generation service 不返回独立的 consumed-input SHA / cryptographic receipt。
- 该限制不阻塞 AO-05，因为现有证据链为：GitHub canonical SHA → GitHub Actions canonical-byte verification → artifact ZIP digest → Work 独立 SHA → actual multi-reference generation call。
- Product Owner 于 2026-09-18 明确接受该限制作为 non-blocking residual audit risk，并要求未来服务能力允许时补齐。
- 正式风险记录：`RISK-002 / ACCEPTED / NON-BLOCKING / DEFERRED IMPROVEMENT`。
