# Acceptance Matrix｜BLACK-LADY-001

> 当前为 **P0 Restart Draft**。Gate 通过只代表该专项已经形成可信输入基线，不代表完整生产 Pipeline 已经验证。
>
> **正式审批规则：**验收条件满足后，Gate / Phase 先进入 `READY_FOR_APPROVAL`；只有 Product Owner 明确批准后，才能正式更新为 `PASS / APPROVED / CLOSED`。ChatGPT / Codex 无权自行完成最终批准。

## P0｜项目重启与基础能力再验证｜ACTIVE

| Gate | 核心问题 | 验收标准 | 当前状态 |
|---|---|---|---|
| P0.1｜故事与文本数据基线 | 以后依据哪套文字与声音事实工作？ | S1 / S2 / canonical audio 固定版本；S3 职责与验证等级锁定；完整 MVP1 建立 machine-searchable source-audio index；抽查可从剧情/台词内容定位到正确候选原音区域；不要求全量毫秒级精切 | **PASS / PRODUCT OWNER APPROVED** |
| P0.2｜人物锚定与 Scene Master 资产治理 | 视觉资产如何标准化、自动选择、自动登记并可追溯地进入生产？ | 完成现有资产 authority audit；建立统一 Entity / Asset Registry；主要人物采用统一 Character Core Set；建立 Scene / Costume / Prop / State / Variant 规范；Approval 与 Lifecycle 分离；定义 Atomic Master / Reference Sheet / dependency；建立 Naming / Version / Storage / Automatic Ingest / Audit Trail；定义并验证 `Shot / Task Spec → Reference Resolver → Reference Package`；使用现有《黑衣夫人》资产做一次真实迁移与自动选图验证 | **ACTIVE / P1 CHARACTER PRODUCTION RESUMED / AO-06 PARALLEL CLOSEOUT** |
| P0.3｜视频制作与剪辑 Pipeline 再验证 | 从静态视觉和原音到真正可接受成片，什么方法实际可行？ | 复盘已有失败；验证 shot-driven Audio Alignment / Resolver、原音自动检索与提取、Animatic、动态化、剪辑、Remotion 职责；最终以代表性实际视频结果作为可行性证据 | **QUEUED** |

## P0.1 PASS Evidence｜2026-09-12

- `S1_SOURCE_NOVEL_FULL_V001.txt`：CANONICAL / LOCKED / REMOTE VERIFIED。
- `S2_SOURCE_BLACK_LADY_TEXT_V001.txt`：CANONICAL / LOCKED。
- `AUDIO_MVP1_CANONICAL_V001.m4a`：CANONICAL / LOCKED / Product Owner QC PASSED。
- `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv`：完整覆盖 MVP1 searchable content，41 个 segment；9 个 VERIFIED，其他为 REVIEWED searchable entries。
- 开头 / 中段 / 后段检索抽查均可唯一命中正确候选 segment。
- S3 明确只承担 source-audio index / transcript / verification；`SOURCE AUDIO TC ≠ FINAL EDIT TC`。
- 精确的 shot-driven 自动音频检索 / 提取能力移交 P0.3 验证。
- **Product Owner 于 2026-09-12 明确批准 P0.1 正式 PASS。**

## P0.2 Required Evidence Before Approval

P0.2 不能仅凭文档设计进入 PASS。至少需要：

1. Asset Authority Audit 完成；
2. `Visual Asset Management System V1` schema 与规则锁定；
3. 主要人物统一 Reference 规范可执行；
4. 场景 / 服装 / 道具 / Variant 规则可执行；
5. 正式 Asset Registry 能区分 Entity、Asset、Role、Version、Approval、Lifecycle、Dependency；
6. Product Owner 批准后，至少验证一条 Automatic Ingest 路径，不要求 Product Owner 手工命名或登记；
7. 至少选择一个包含人物 + 场景 + 关键道具/服装的真实 Shot Spec，验证 Reference Resolver 能自动生成可追踪 Reference Package；
8. Audit Trail 能从生成镜头反查当次实际使用的 Asset IDs / versions，并能从资产反查批准、替代、依赖和生产使用关系。

### P0.2 Evidence Status｜2026-09-18 EOD

| # | Evidence | 当前证据状态 |
|---|---|---|
| 1 | Asset Authority Audit | **PARTIAL / MAJOR BASELINE LOCKED**：Authority Mini-Close、A-Series / SH 边界、Character migration authority 已锁定；AO-01 按 BL-D-028 完成可取得证据的对账；原表内部项 UNKNOWN / SOURCE UNAVAILABLE；AO-01 COMPLETE / VERIFIED。 |
| 2 | System schema / rules | **VERIFIED DESIGN BASELINE**：Visual Asset Management System V1、Schema V0.3、Naming、Single Current、Lifecycle、Relations、Character Tier/Gap 规则已锁定。 |
| 3 | Character Reference 规范可执行 | **VERIFIED IN REAL P1 PRODUCTION**：9:16 Format Compliance、Fixed Standard Review、P1 role definitions 已用于宁秋水真实补图。 |
| 4 | Scene / Costume / Prop / Variant 规则可执行 | **VERIFIED / AO-03 COMPLETE / PRODUCT OWNER APPROVED**：AO-03A+B 均获 Product Owner 批准；D-067 已实现两个 Stable Scene Entity、多维 State Profile、formal Scene Master 映射及显式 state-aware Resolver；DAY+OPEN / FIREPLACE_EXTINGUISHED 正向案例与 NIGHT / CLOSED / BURNING / missing-state / UNSPECIFIED 负向案例通过。AO-03 最终 DoD 已审核通过，PR #6 已合并。 |
| 5 | Asset Registry / Dependency model | **VERIFIED FOR CHARACTER / SCENE / DERIVED; SHOT MIGRATION GAP EXPOSED**：当前 Runtime Registry = 62 Assets；Character / Scene / Derived dependency model 已验证。历史 A-Series Shot 尚未迁入当前 Runtime Registry，Formal SHOT=0；该缺口在 D-069 A04 real validation 中暴露。 |
| 6 | Automatic Ingest | **VERIFIED**：`AST_IMG_000049` 首次 ingest、`AST_IMG_000050` controlled supersession、`AST_IMG_000051` normal ingest 均真实成功；Product Owner 无需手工分配 Asset ID、登记 Registry 或维护替代关系。 |
| 7 | Real Shot Spec Resolver | **ENGINEERING FOUNDATION COMPLETE / REAL VALIDATION BLOCKED**：D-069 已实现 A04 executable Shot Spec、fail-closed Resolver、Reference Package exporter；PR #10 已 merge。当前 approved A04 binary 未 materialize 到 Runtime，且 Costume/Cross 模型/证据边界待复核，因此尚未完成 real generation validation。 |
| 8 | Shot-level Audit reverse-trace | **ENGINEERING FOUNDATION VERIFIED / END-TO-END PENDING**：immutable use record、Shot→inputs、Asset→use、sandbox USES_REFERENCE forward/reverse query 与 rollback 已实现并测试；live USES_REFERENCE 仍为 0，待真实 Work generation receipt 后完成 end-to-end evidence。 |

AO-02 completion evidence：

- `gates/P0_2_visual_assets/ao02_legacy_asset_registry_migration_v1.md`
- 48 / 48 eligible legacy Character assets migrated；
- `AST_IMG_000001–000048` deterministic backfill；
- Runtime `AST_IMG_000049–000051` preserved；
- Registry 51 / Relations 2 / Audit 56；
- idempotency + rollback tests `5/5 PASS`；
- migration commit `4803b928baaa38d875e9c6edd46f4a458e627b61` remote verified；
- Product Owner 于 2026-09-14 明确批准 AO-02。

AO-03 completion evidence：

- `gates/P0_2_visual_assets/ao03_scene_executable_spec_design_v0_1.md`
- `gates/P0_2_visual_assets/ao03_closeout_2026-09-17.md`
- AO-03A approved：2026-09-15；AO-03B approved：2026-09-17；AO-03 final approval：2026-09-17。
- `SCENE_CASTLE_ENTRANCE` / `SCENE_FIRST_HALL` 作为 Stable Scene Entities。
- Scene Master Asset IDs：`AST_IMG_000052` / `AST_IMG_000053`。
- Scene Master locks Scene Facts, not Shot Photography；required state 不匹配时返回 `REFERENCE_GAP`。
- D-067 full regression：`54 tests / OK`。
- PR #6：`AO-03: add executable Scene registry and state-aware resolver`。
- Merge SHA：`b16ffdd5f1c57f0b2c28acdee3caac656afb91a3`。

AO-07 completion evidence：

- `gates/P0_2_visual_assets/ao07_github_network_resilience_progress_v1.md`
- connectivity preflight / standard diagnosis order documented；
- dynamic proxy + HTTP/1.1 fallback verified；
- `ls-remote / pull / push / SHA truth check` verified；
- `PENDING_REMOTE_PUBLICATION` / ACK loss / remote mismatch recovery rules documented；
- transient failure → recovery satisfied by real incident evidence；
- Product Owner 于 2026-09-14 明确批准 AO-07；
- `RISK-001` 已降级为 `CONTROLLED / MITIGATION VERIFIED`。

Cloud-only publication evidence：

- `gates/P0_2_visual_assets/cloud_pr_workflow_drill_2026-09-15.md`
- `CLOUD-DRILL-001` 未占用 D-###；
- Codex Cloud native PR publication 已由 GitHub PR #5 真实验证；
- PR independently reviewed；Product Owner approved merge；
- merge SHA：`774a6abed34b81e5558dbfeba3846380fb1ff26e`；
- 不改变 P0.2 Gate 技术验收条件，仅验证 2026-09-16～09-20 临时云端执行通路。

当前结论：**P0.2 仍为 ACTIVE，不满足 READY_FOR_APPROVAL。AO-01、AO-02、AO-03、AO-04、AO-05、AO-07 已完成；仅 AO-06 剩余。D-069 engineering foundation 已通过 PR #10 merge 进入 main，但真实 A04 end-to-end validation 仍被 approved A04 binary 与 Costume/Cross 模型/证据问题阻塞。**

### Approved-but-Open Closeout｜BL-D-026 + BL-D-027; sequencing updated by BL-D-039 / RC-020

Product Owner 已把以下 7 项提升为 P1 Wave 2 前必须完成的正式前置任务：

1. AO-01｜4 Canonical Registers Final Reconciliation — **COMPLETE / VERIFIED**；
2. AO-02｜48 legacy Character assets → Long-term Registry / Audit — **COMPLETE / VERIFIED / PO APPROVED**；
3. AO-03｜2 Scene Masters + Scene / Costume / Prop / State / Variant executable Spec — **COMPLETE / VERIFIED / PRODUCT OWNER APPROVED**；
4. AO-04｜9 Derived Character Reference Sheets + dependency/staleness — **COMPLETE / VERIFIED / PRODUCT OWNER APPROVED**；
5. AO-05｜Delivery Bridge：Reference Package → image-production environment — **COMPLETE / VERIFIED / PRODUCT OWNER APPROVED**；
6. AO-06｜Real Shot Spec Resolver + Shot-level Audit reverse-trace — **D-069 ENGINEERING FOUNDATION MERGED / EVIDENCE BLOCKED / EOD PAUSED**；
7. AO-07｜GitHub Network Resilience / Recovery Method — **COMPLETE / VERIFIED / PO APPROVED**。

详细完成标准见：`gates/P0_2_visual_assets/approved_open_tasks_v1.md`；正式风险见 `logs/risk_register.md`。

**当前 AO-01、AO-02、AO-03、AO-04、AO-05、AO-07 已完成；AO-06 仍是唯一 final closeout 缺口，但自 2026-09-19 起不再阻塞 P1 Character production sequencing。P1 已恢复，下一目标为君鹭远 PROFILE_LEFT。**

满足全部技术条件后，P0.2 状态仍只能进入 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`，由 Product Owner 决定是否正式 PASS。

## P0 Gate Boundary

P0 完成前只允许形成：

1. 已有 / 已验证 / 未验证或失败 / 缺失的事实基线；
2. 三项专项各自的可执行制度或已验证方法；
3. 后续正式生产 Roadmap 的输入。

P0 不以“完成更多 A 系列镜头”作为进度指标。
