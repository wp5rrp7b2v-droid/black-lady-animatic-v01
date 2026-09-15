# Acceptance Matrix｜BLACK-LADY-001

> 当前为 **P0 Restart Draft**。Gate 通过只代表该专项已经形成可信输入基线，不代表完整生产 Pipeline 已经验证。
>
> **正式审批规则：**验收条件满足后，Gate / Phase 先进入 `READY_FOR_APPROVAL`；只有 Product Owner 明确批准后，才能正式更新为 `PASS / APPROVED / CLOSED`。ChatGPT / Codex 无权自行完成最终批准。

## P0｜项目重启与基础能力再验证｜ACTIVE

| Gate | 核心问题 | 验收标准 | 当前状态 |
|---|---|---|---|
| P0.1｜故事与文本数据基线 | 以后依据哪套文字与声音事实工作？ | S1 / S2 / canonical audio 固定版本；S3 职责与验证等级锁定；完整 MVP1 建立 machine-searchable source-audio index；抽查可从剧情/台词内容定位到正确候选原音区域；不要求全量毫秒级精切 | **PASS / PRODUCT OWNER APPROVED** |
| P0.2｜人物锚定与 Scene Master 资产治理 | 视觉资产如何标准化、自动选择、自动登记并可追溯地进入生产？ | 完成现有资产 authority audit；建立统一 Entity / Asset Registry；主要人物采用统一 Character Core Set；建立 Scene / Costume / Prop / State / Variant 规范；Approval 与 Lifecycle 分离；定义 Atomic Master / Reference Sheet / dependency；建立 Naming / Version / Storage / Automatic Ingest / Audit Trail；定义并验证 `Shot / Task Spec → Reference Resolver → Reference Package`；使用现有《黑衣夫人》资产做一次真实迁移与自动选图验证 | **ACTIVE / APPROVED-OPEN CLOSEOUT BEFORE P1 WAVE 2** |
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

### P0.2 Evidence Status｜2026-09-15

| # | Evidence | 当前证据状态 |
|---|---|---|
| 1 | Asset Authority Audit | **PARTIAL / MAJOR BASELINE LOCKED**：Authority Mini-Close、A-Series / SH 边界、Character migration authority 已锁定；AO-01 按 BL-D-028 完成可取得证据的对账；原表内部项 UNKNOWN / SOURCE UNAVAILABLE；AO-01 COMPLETE / VERIFIED。 |
| 2 | System schema / rules | **VERIFIED DESIGN BASELINE**：Visual Asset Management System V1、Schema V0.3、Naming、Single Current、Lifecycle、Relations、Character Tier/Gap 规则已锁定。 |
| 3 | Character Reference 规范可执行 | **VERIFIED IN REAL P1 PRODUCTION**：9:16 Format Compliance、Fixed Standard Review、P1 role definitions 已用于宁秋水真实补图。 |
| 4 | Scene / Costume / Prop / Variant 规则可执行 | **PARTIAL / AO-03 IN PROGRESS**：AO-03A｜Fact Boundary + Executable Spec Design V0.1 已由 Product Owner 于 2026-09-15 批准；Stable Scene Entity / controlled State / Shot Photography 边界已锁定。AO-03B 尚需逐项定义两张 approved Scene Master 的具体事实字段，随后仍需 Runtime / Resolver / machine-verifiable tests，故本项尚未 VERIFIED。 |
| 5 | Asset Registry / Dependency model | **CHARACTER REGISTRY VERIFIED / DERIVED + SCENE DEPENDENCY PENDING**：AO-02 已将 48 legacy Character assets 以 `AST_IMG_000001–000048` 正式迁入长期 Registry / Audit；现有 Runtime `AST_IMG_000049–000051` 保持不变；总 Registry 51 条，无 duplicate Current。Derived dependency 与 broader Scene/Prop/Costume 数据仍需 AO-03/AO-04 验证。 |
| 6 | Automatic Ingest | **VERIFIED**：`AST_IMG_000049` 首次 ingest、`AST_IMG_000050` controlled supersession、`AST_IMG_000051` normal ingest 均真实成功；Product Owner 无需手工分配 Asset ID、登记 Registry 或维护替代关系。 |
| 7 | Real Shot Spec Resolver | **PENDING AO-06**：尚未用至少一个“人物 + 场景 + 关键服装/道具”的真实 Shot Spec 完成完整 Reference Package 验证。 |
| 8 | Shot-level Audit reverse-trace | **PARTIAL / PENDING AO-06**：Asset-level approval / ingest / supersession / legacy migration audit 已验证；从生成 Shot 反查实际 Reference Asset IDs / versions 及反向 production use relation尚未完整验证。 |

AO-02 completion evidence：

- `gates/P0_2_visual_assets/ao02_legacy_asset_registry_migration_v1.md`
- 48 / 48 eligible legacy Character assets migrated；
- `AST_IMG_000001–000048` deterministic backfill；
- Runtime `AST_IMG_000049–000051` preserved；
- Registry 51 / Relations 2 / Audit 56；
- idempotency + rollback tests `5/5 PASS`；
- migration commit `4803b928baaa38d875e9c6edd46f4a458e627b61` remote verified；
- Product Owner 于 2026-09-14 明确批准 AO-02。

AO-03A approval evidence：

- `gates/P0_2_visual_assets/ao03_scene_executable_spec_design_v0_1.md`
- Product Owner 于 2026-09-15 明确批准 AO-03A；
- `SCENE_CASTLE_ENTRANCE` / `SCENE_FIRST_HALL` 作为 stable Scene identity；
- DAY/NIGHT、door OPEN/CLOSED、fireplace EXTINGUISHED/BURNING 为 controlled State dimensions；
- Scene Master locks Scene Facts, not Shot Photography；
- required state 无正式 eligible asset 时必须返回 `REFERENCE_GAP`。

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

当前结论：**P0.2 仍为 ACTIVE，不满足 READY_FOR_APPROVAL。AO-03 已进入 IN PROGRESS，下一正式步骤为 AO-03B。**

### Approved-but-Open Pre-Wave2 Closeout｜BL-D-026 + BL-D-027

Product Owner 已把以下 7 项提升为 P1 Wave 2 前必须完成的正式前置任务：

1. AO-01｜4 Canonical Registers Final Reconciliation — **COMPLETE / VERIFIED**；
2. AO-02｜48 legacy Character assets → Long-term Registry / Audit — **COMPLETE / VERIFIED / PO APPROVED**；
3. AO-03｜2 Scene Masters + Scene / Costume / Prop / State / Variant executable Spec — **IN PROGRESS / AO-03A APPROVED / AO-03B NEXT**；
4. AO-04｜9 Derived Character Reference Sheets + dependency/staleness；
5. AO-05｜Delivery Bridge：Reference Package → image-production environment；
6. AO-06｜Real Shot Spec Resolver + Shot-level Audit reverse-trace；
7. AO-07｜GitHub Network Resilience / Recovery Method — **COMPLETE / VERIFIED / PO APPROVED**。

详细完成标准见：`gates/P0_2_visual_assets/approved_open_tasks_v1.md`；正式风险见 `logs/risk_register.md`。

**当前 AO-01、AO-02、AO-07 已完成；AO-03 正在推进，AO-04～AO-06 仍未完成，因此 `P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT` 继续 HOLD。**

满足全部技术条件后，P0.2 状态仍只能进入 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`，由 Product Owner 决定是否正式 PASS。

## P0 Gate Boundary

P0 完成前只允许形成：

1. 已有 / 已验证 / 未验证或失败 / 缺失的事实基线；
2. 三项专项各自的可执行制度或已验证方法；
3. 后续正式生产 Roadmap 的输入。

P0 不以“完成更多 A 系列镜头”作为进度指标。
