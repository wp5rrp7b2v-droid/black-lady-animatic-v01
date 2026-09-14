# P0.2｜人物锚定与 Scene Master 资产治理

Status: `ACTIVE / APPROVED-OPEN CLOSEOUT BEFORE P1 WAVE 2`

## 当前目标

P0.2 不再只做“图库整理”，而是建立可规模化的 **Visual Asset Management System V1**，并把现有《黑衣夫人》视觉资产迁移到统一治理模型中。

当前锁定的系统方向：

`Entity → Atomic Master Assets → Derived Reference Sheet → Reference Resolver → Shot Reference Package → Generation → Product Owner Approval → Automatic Ingest → Asset Registry / Audit Trail`

目标是在正常生产中取消 Product Owner 的例行人工挑图、下载、命名、存储、登记与版本维护；Product Owner 只保留创意判断、异常处理与正式审批。

## 已锁定项目级规则

- 只有 Product Owner 明确批准的视觉结果才能进入正式 Asset Registry；
- 人物 / 场景 / 服装 / 道具统一采用 Entity → Asset 模型；
- Approval 与 Lifecycle 分离；正式生命周期为 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；
- Authority / Lifecycle / Resolver Usage 分离；
- Atomic Asset 与 Derived Reference Sheet 分离；Derived Reference 必须可追踪上游依赖；
- 正常生产目标为 `Shot / Task Spec → Reference Resolver → Reference Package`；
- 正式资产的来源、审批、版本、替代、依赖与生产调用必须有 Audit Trail；
- Entity / Asset Registry Schema V0.3 已由 Product Owner 于 2026-09-13 批准锁定；
- canonical Shot ID 不继承历史 `REBOOT` 标签；多人物 Shot 仍为 Shot-bound Asset，人物组成由 Shot Register / Shot Spec 表达；
- Entity-bound / Shot-bound filename 均包含 Role + Variant + State + Version；
- 9 名正式角色 Tier Assignment V1 已锁定；
- Character Asset Gap Mapping V1 已完成实图核对并落档；
- Character Atomic / Auxiliary production reference 目标画幅锁定为 9:16；
- 图片生成后由 Product Owner 发送 `【审核】` 触发 Fixed Standard Review；
- D-059 Character Asset Migration V1 已完成并远端验证：48 张 canonical PNG + CSV/JSON Migration Mapping Manifest 已发布；
- D-060 Reference Package Exporter V0.1 已验证自动选图 + 本地 Reference Package；
- D-061～D-065 已接通 Character ingest、P1 role 泛化、Migration + Runtime asset resolution、受控 Current supersession 与 macOS launcher；
- AO-01 已 COMPLETE / VERIFIED；
- AO-02 已 COMPLETE / VERIFIED / PRODUCT OWNER APPROVED：48 个 legacy Character assets 已正式进入长期 Registry / Audit；
- RC-015 已锁定项目级 Execution Routing：Chat 优先，Terminal 负责轻量本地执行，只有真正需要本地工程环境时才交给 Codex。

详细规则与当前基线见：

- `visual_asset_management_system_v1.md`
- `character_asset_rules_v1.md`
- `character_tier_assignment_v1.md`
- `character_asset_gap_mapping_v1.md`
- `character_gap_live_progress_v1.md`
- `character_gap_priority_v1.md`
- `asset_naming_rules_v1.md`
- `asset_authority_audit.md`
- `entity_asset_registry_schema_v0_3.md`
- `d059_character_asset_migration_v1_completion.md`
- `d060_reference_package_exporter_v0_1_test.md`
- `automatic_ingest_controller_v0_1_first_live_ingest.md`
- `approved_open_tasks_v1.md`
- `ao01_4_registers_reconciliation_v1.md`
- `ao01_register_disposition_v1.csv`
- `ao02_legacy_asset_registry_migration_v1.md`
- `../../logs/risk_register.md`

## 当前任务

### P0.2-01｜Visual Asset Authority Audit

Authority Mini-Close 已锁定。D-059 已将 48 张 approved Character references 迁入 canonical GitHub storage，并发布 Migration Mapping Manifest。

AO-01 已按 BL-D-028 完成可取得证据的旧表对账，四份旧表退出 Current authority。AO-02 已把 48 个 confirmed legacy Character assets 纳入长期 Asset Registry / Audit identity。

P0.2 Gate Review 前仍需：

1. AO-03：两张 Scene Master 的事实字段结构化，并落实 Scene / Costume / Prop / State / Variant 可执行 Spec；
2. AO-04：9 个 Derived Character Reference Sheets 与 dependency / staleness；
3. AO-05：Delivery Bridge；
4. AO-06：真实 Shot Spec Resolver + Shot-level Audit reverse-trace；
5. AO-07：GitHub Network Resilience / Recovery Method 正式完成与验证。

### P0.2-02｜Visual Asset Management System V1 Design

已完成并锁定：

- Character Tier A/B/C/D；
- Asset ID / Naming；
- Authority Mini-Close；
- Entity / Asset Registry Schema V0.3；
- Single Current；
- Asset Relations；
- Provenance Status；
- Resolver Eligibility；
- Append-only Audit Event Log；
- Legacy Migration Mapping Manifest；
- Shot-bound / Entity-bound 归属与命名边界；
- Controlled Current Supersession；
- Character image 9:16 Format Compliance；
- Fixed Standard Review。

### P0.2-03｜Character Tier Assignment + Gap Analysis + P1 Production

Tier Assignment：

- Tier A：宁秋水 / 君鹭远 / 尼尔 / 黑衣夫人；
- Tier B：温倾雅 / 苏小小 / 廖健 / 古堡小主人；
- Tier C：光勇；
- Tier D：当前 9 名正式角色中无。

Character Asset Gap Mapping V1 历史基线：

- Mandatory Core Slots = `63`
- Confirmed Coverage baseline = `40`
- Core View Gap baseline = `23`
- Core Coverage baseline = `63.5%`
- Reference Sheet Gap = `9`

当前 live production progress：

- Confirmed Core Coverage = `42 / 63`
- Core View Gap = `21`
- Core Coverage = `66.7%`
- P1 completed = `2 / 10`
- P1 remaining = `8 / 10`

宁秋水：

- `PROFILE_LEFT` = COMPLETE / APPROVED / CURRENT `V002 / AST_IMG_000050`
- `REAR_3Q_LEFT` = COMPLETE / APPROVED / CURRENT `V001 / AST_IMG_000051`
- Tier A current Core Coverage = `8 / 9`
- Remaining non-P1 Core Gap = `FACE_3Q_LEFT`

P1 Wave 2 `CHAR_JUN_LUYUAN PROFILE_LEFT` 继续 HOLD，直到 Approved-but-Open Resume Lock 解除。

### P0.2-04｜Approved-but-Open System Closeout

Status: `ACTIVE / AO-01 + AO-02 COMPLETE / AO-03 NEXT / MANDATORY BEFORE P1 WAVE 2`

1. AO-01｜4 Canonical Registers Final Reconciliation — `COMPLETE / VERIFIED`；
2. AO-02｜48 legacy Character assets → Long-term Registry / Audit — `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`；
3. AO-03｜Scene Master Structured Facts + Scene / Costume / Prop / State / Variant executable Spec — `NEXT / NOT STARTED`；
4. AO-04｜9 Derived Character Reference Sheets + dependency / staleness；
5. AO-05｜Delivery Bridge；
6. AO-06｜Real Shot Spec Resolver + Shot-level Audit reverse-trace；
7. AO-07｜GitHub Network Resilience / Recovery Method。

AO-02 completion evidence：`ao02_legacy_asset_registry_migration_v1.md`。

## AO-02｜Legacy Registry Migration

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-14`

- 48 / 48 eligible D-059 legacy Character assets migrated；
- deterministic Asset ID range = `AST_IMG_000001–000048`；
- Runtime `AST_IMG_000049–000051` preserved；
- Asset Registry = `51` records；
- Asset Relations = `2` records；
- Audit Event Log = `56` records；
- Single Current / SHA / storage validation PASS；
- D-059 Manifest and Character PNGs unchanged；
- idempotency / rollback tests = `5/5 PASS`；
- migration commit = `4803b928baaa38d875e9c6edd46f4a458e627b61` / REMOTE VERIFIED；
- Product Owner explicitly approved AO-02 on 2026-09-14；
- AO-02 used Chat + Terminal and therefore consumed no new Codex D-### number。

## Risk Alert｜RISK-001 GitHub Connectivity Instability

Status: `OPEN / AO-07 NOT YET FORMALLY CLOSED`

动态 `git-proxy-auto` 已在本仓库完成 `ls-remote / pull / push / SHA truth check` 成功验证，说明网络恢复方向有效；但 AO-07 的正式 Runbook、受控 failure→recovery evidence 与 Product Owner closeout 尚未完成，因此不得把风险写成 CLOSED。

## D-059～D-065｜Character Automation Baseline

- D-059｜Character Asset Migration V1 — COMPLETE / REMOTE VERIFIED
- D-060｜Reference Package Exporter V0.1 — TEST APPROVED / PO APPROVED
- D-061｜One-click Character Ingest + Cleanup — COMPLETE / REMOTE VERIFIED
- D-062｜P1 Character Reference Package Generalization — COMPLETE / REMOTE VERIFIED
- D-063｜Unified Migration + Runtime Character Asset Resolution — COMPLETE / REMOTE VERIFIED
- D-064｜Controlled Current Supersession — COMPLETE / REMOTE VERIFIED
- D-065｜macOS Bash Launcher Fix — COMPLETE / REMOTE VERIFIED
- D-066｜AO-01 Four Registers Final Reconciliation — COMPLETE / VERIFIED

下一 Codex 工程编号仅在确实需要 Codex 执行时使用：`D-067`。

## 当前执行基线

P1 按人物整组推进：

1. 宁秋水：`PROFILE_LEFT + REAR_3Q_LEFT` = **COMPLETE**
2. 君鹭远：`PROFILE_LEFT + REAR_3Q_LEFT` = **HOLD UNTIL AO-01～AO-07 COMPLETE**
3. 尼尔：`PROFILE_RIGHT + REAR_3Q_RIGHT`
4. 苏小小：`PROFILE_LEFT + REAR_3Q_LEFT`
5. 廖健：`PROFILE_LEFT + REAR_3Q_LEFT`

当前日常 Character 生产链：

`Reference Resolver / Package → Generation → 【审核】→ PO Approval → local final PNG → Black_Lady_Ingest.command → Registry / Audit / Git publication`

真正的 generation environment → local/GitHub Delivery Bridge 尚未完成，由 AO-05 负责。

## 下一步

下一正式任务：

`P0.2-04｜AO-03｜Scene Master Structured Facts + Scene/Costume/Prop/Variant Executable Spec`

首先在 Chat 内完成事实边界、数据模型、Definition of Done 与实现需求判断；只有确实需要本地多文件工程实现时才交给 Codex。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。
