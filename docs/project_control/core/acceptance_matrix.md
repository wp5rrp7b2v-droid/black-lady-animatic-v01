# Acceptance Matrix｜BLACK-LADY-001

> 当前为 **P0 Restart Draft**。Gate 通过只代表该专项已经形成可信输入基线，不代表完整生产 Pipeline 已经验证。
>
> **正式审批规则：**验收条件满足后，Gate / Phase 先进入 `READY_FOR_APPROVAL`；只有 Product Owner 明确批准后，才能正式更新为 `PASS / APPROVED / CLOSED`。ChatGPT / Codex 无权自行完成最终批准。

## P0｜项目重启与基础能力再验证｜ACTIVE

| Gate | 核心问题 | 验收标准 | 当前状态 |
|---|---|---|---|
| P0.1｜故事与文本数据基线 | 以后依据哪套文字与声音事实工作？ | S1 / S2 / canonical audio 固定版本；S3 职责与验证等级锁定；完整 MVP1 建立 machine-searchable source-audio index；抽查可从剧情/台词内容定位到正确候选原音区域；不要求全量毫秒级精切 | **PASS / PRODUCT OWNER APPROVED** |
| P0.2｜人物锚定与 Scene Master 资产治理 | 视觉资产如何标准化、自动选择、自动登记并可追溯地进入生产？ | 完成现有资产 authority audit；建立统一 Entity / Asset Registry；主要人物采用统一 Character Core Set；建立 Scene / Costume / Prop / State / Variant 规范；Approval 与 Lifecycle 分离；定义 Atomic Master / Reference Sheet / dependency；建立 Naming / Version / Storage / Automatic Ingest / Audit Trail；定义并验证 `Shot / Task Spec → Reference Resolver → Reference Package`；使用现有《黑衣夫人》资产做一次真实迁移与自动选图验证 | **PASS / PRODUCT OWNER APPROVED** |
| P0.3｜视频制作与剪辑 Pipeline 再验证 | 从静态视觉和原音到真正可接受成片，什么方法实际可行？ | 复盘已有失败；验证 shot-driven Audio Alignment / Resolver、原音自动检索与提取、Animatic、动态化、剪辑、Remotion 职责；最终以代表性实际视频结果作为可行性证据 | **IN PROGRESS / S02-A ASSEMBLY V001 FORMALLY CLOSED / NOT YET VALIDATED** |

## P0.3 Current Validation Note｜2026-09-25

- 4-shot `A01 → Wide → Tight → A02` 2.5D proof was artistically rejected because character deformation was visible.
- Character-shot single-image 2.5D is no longer the current main route.
- Current representative validation target is an Opening Audio-Comic Proof using canonical audio + approved Story Shots + normal cuts + restrained crop/zoom.
- Acceptance criteria are not lowered or declared satisfied; P0.3 remains NOT YET VALIDATED.

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
| 5 | Asset Registry / Dependency model | **VERIFIED FOR CHARACTER / SCENE / DERIVED; A04 EVIDENCE BOUNDARY EXPLICIT**：当前 Runtime Registry = 83 Assets；Character / Scene / Derived dependency model 已验证。A04 approved legacy Shot binary 作为 exact Shot evidence 单独 materialize，不伪造历史 formal SHOT Registry lineage，也不补造历史 USES_REFERENCE。 |
| 6 | Automatic Ingest | **VERIFIED**：`AST_IMG_000049` 首次 ingest、`AST_IMG_000050` controlled supersession、`AST_IMG_000051` normal ingest 均真实成功；Product Owner 无需手工分配 Asset ID、登记 Registry 或维护替代关系。 |
| 7 | Real Shot Spec Resolver | **VERIFIED END-TO-END / REAL ACTUAL USE COMPLETED**：A04 exact approved binary、Character + Scene Resolver、Neil appearance-continuity boundary、Reference Package 与真实 Actual Production Use 均已验证。Stage 4 GitHub Actions run `35705835709` 生成 `A04_REFERENCE_PACKAGE_V001`，Work 实际完成非模拟 image generation，manual Product Owner reference upload count = 0；service input SHA receipt = `NOT_AVAILABLE` 作为已记录服务限制。 |
| 8 | Shot-level Audit reverse-trace | **VERIFIED END-TO-END / PRODUCT OWNER APPROVED WITH AO-06**：PR #13 已 squash merge；`AO06_A04_USE_V001` immutable use record 已在 main。Shot→inputs 反查 PASS；`AST_IMG_000060 / 000059 / 000052` → A04 production-use 反查 3/3 PASS；duplicate-write rejection PASS；Registry / Relations / Audit Event Log 保持 `83 / 44 / 120` 不变；因 validation output 非 formal SHOT Asset，按边界不创建 `USES_REFERENCE`，也不补造历史关系。targeted `13/13`、full regression `86/86` PASS。Product Owner 于 2026-09-22 正式批准 AO-06。 |

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

AO-06 final validation evidence：

- Stage 4 Actual Production Use：GitHub Actions run `35705835709`；
- Reference Package：`A04_REFERENCE_PACKAGE_V001` / Artifact `10684566525` / SHA-256 `3f1d5fb1b3d54cdfd0ff1c0c6d25df85cd1e78f066e9a8269419943612fc916e`；
- Actual generation proof：`imagegen exec-ae7fde3c-02a5-4106-beaa-69704b9164ea`；
- Final immutable use record：`production/audit/shot_use_records/AO06_A04_USE_V001.json`；
- PR #13 merge SHA：`9ec2975059582bbd279d3a05d4af1284fac3f27a`；
- Final audit validation run：`35709208035`；
- Shot→inputs PASS；Asset→use 3/3 PASS；immutability PASS；
- Registry / Relations / Audit Event Log = `83 / 44 / 120` unchanged；
- `USES_REFERENCE_CREATED = NO` by design for non-production validation output；
- AO-06 current status: `READY_FOR_APPROVAL / WAITING PRODUCT OWNER APPROVAL`.

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


### P0.2 Evidence Status Delta｜2026-09-19 EOD

- P0.2 remains `ACTIVE / P1 CHARACTER PRODUCTION RESUMED / AO-06 PARALLEL CLOSEOUT`; it is **not** READY_FOR_APPROVAL.
- P1 production sequencing resumed under BL-D-039 / RC-020.
- Four new P1 views reached explicit Product Owner visual approval but remain outside formal Registry/Core Coverage because exact-byte publication + Automatic Ingest has not completed:
  - Jun Luyuan `PROFILE_LEFT V002`
  - Jun Luyuan `REAR_3Q_LEFT V001`
  - Neil `PROFILE_RIGHT V001`
  - Neil `REAR_3Q_RIGHT V001`
- Formal live coverage therefore remains `42 / 63 = 66.7%`; formal P1 completion remains `2 / 10`.
- Current production target advanced to Su Xiaoxiao `PROFILE_LEFT V001`; dedicated Delivery Bundle workflow created, artifact build pending.
- AO-06 / D-069 remains the only mandatory system-closeout item before P0.2 can become READY_FOR_APPROVAL.
- P0.3 remains QUEUED / DO NOT START EARLY.


### P0.2 Evidence Status Delta｜2026-09-20 EOD

- P0.2 remains `ACTIVE`; it is **not** READY_FOR_APPROVAL.
- Formal Core Coverage remains `42 / 63 = 66.7%`; formal Core View Gap remains `21`.
- P1 visual production reached `10 / 10 PO APPROVED`, but formal P1 remains `2 / 10` until the remaining 8 approved P1 views are formally ingested.
- P2 visual generation reached `7 / 7`; `6 / 7` have explicit Product Owner approval.
- Castle Young Master `REAR_3Q_LEFT V001` remains `PO REVIEW PENDING / DO NOT INGEST`.
- Total approved Core-view binaries awaiting publication + Automatic Ingest = `14`.
- None of those 14 are counted in formal Registry/Core Coverage yet.
- P3 Black Lady 6-view lateral rebuild remains `NOT STARTED`.
- AO-06 / D-069 remains the only mandatory system-closeout item before P0.2 can become READY_FOR_APPROVAL.
- D-070 remains NOT ALLOCATED.
- TEMP_CLOUD_ONLY_MODE_V1 reaches its pre-approved time-box end at 2026-09-20 EOD; the next local formal production session requires GitHub→Local truth sync first.


### P0.2 Evidence Status Delta｜2026-09-21 EOD

- P0.2 remains `ACTIVE`; it is **not** READY_FOR_APPROVAL.
- Character Core visual production is now `63 / 63 PO APPROVED`; visual-production gap is zero.
- The 21 formerly missing Core PNGs were byte-for-byte published to canonical GitHub paths in commit `b9bafa2af4b9be8aadf2bd2abe79b724837eff88`.
- All 21 committed binaries were independently re-read and verified `21/21 SHA_MATCH` against their approved source identities.
- Formal Core Coverage intentionally remains `42 / 63 = 66.7%` because those 21 published binaries have not yet been admitted to the runtime Asset Registry/Audit.
- Automatic Ingest V0.1 currently rejects an already-existing canonical target; the next proposed Codex Cloud task is `D-070｜Published Binary Adoption + 21-Asset Automatic Ingest`. D-070 is not started and should be consumed only when the Codex task launches.
- D-070 must preserve binary identity, enforce Single Current/version safety, and cross-check Derived Reference Sheet freshness implications after the missing Core slots become formal.
- AO-06 / D-069 remains OPEN and is still mandatory before P0.2 can become READY_FOR_APPROVAL.
- P0.3 remains QUEUED / DO NOT START EARLY.


## 2026-09-22｜D-070 Published Binary Adoption

- D-070 adoption result: **21/21 COMPLETE** on the rescue publication branch.
- Asset IDs: `AST_IMG_000063–AST_IMG_000083`.
- Formal Character Core Coverage: **63 / 63 = 100%**; formal Core gap = **0**.
- Single Current: **63/63 PASS** for mandatory Character Core slots.
- Audit: **42 required events** = 21 `ASSET_APPROVED` + 21 `ASSET_INGESTED`.
- D-070 relations: **0**, expected because the 21 admissions filled empty formal slots.
- Published PNG content remains unchanged; D-070 is Registry/Audit adoption, not image regeneration.
- Automatic Ingest now has a fail-closed `--adopt-existing` path with exact canonical-path, Git-tracked/clean and SHA checks plus explicit contiguous version reservation safety.
- Existing Derived Reference Sheet PNGs are **not regenerated or re-approved by D-070**; only the expected live Core coverage contract is refreshed.
- P0.2 remains **ACTIVE**. AO-06 / D-069 remains the sole mandatory final-closeout requirement.
- P0.3 remains **QUEUED / DO NOT START EARLY**.


## P0.2 Final Readiness Review｜2026-09-22

Result: **READY_FOR_APPROVAL / WAITING PRODUCT OWNER APPROVAL**

Cross-check conclusion:

- Character Core formal coverage = `63/63`, gap = `0`;
- AO-01 = COMPLETE / VERIFIED;
- AO-02 = COMPLETE / VERIFIED / PRODUCT OWNER APPROVED;
- AO-03 = COMPLETE / VERIFIED / PRODUCT OWNER APPROVED;
- AO-04 = COMPLETE / VERIFIED / PRODUCT OWNER APPROVED;
- AO-05 = COMPLETE / VERIFIED / PRODUCT OWNER APPROVED;
- AO-06 = COMPLETE / VERIFIED / PRODUCT OWNER APPROVED;
- AO-07 = COMPLETE / VERIFIED / PRODUCT OWNER APPROVED;
- Automatic Ingest real path verified;
- real A04 Shot Spec → Resolver → Reference Package → Actual Production Use → immutable use record → reverse audit verified;
- Asset Registry / dependency / Scene state / Derived Reference / audit boundaries remain consistent;
- RISK-001 = CONTROLLED / MITIGATION VERIFIED;
- RISK-002 = ACCEPTED / NON-BLOCKING / DEFERRED IMPROVEMENT;
- no mandatory P0.2 engineering evidence gap remains.

P0.2 is therefore eligible for Product Owner Gate approval.

Per governance, this does **not** mark P0.2 PASS automatically. P0.3 remains QUEUED until explicit Product Owner P0.2 approval.


## P0.2 PASS Evidence｜2026-09-22

Product Owner explicitly approved P0.2 on 2026-09-22.

Closeout evidence:
`gates/P0_2_visual_assets/p0_2_closeout_2026-09-22.md`

Final state:
- Character Core formal coverage `63/63`;
- AO-01..AO-07 closeout requirements satisfied;
- real Resolver → Reference Package → Actual Production Use → immutable use record → reverse audit verified;
- P0.2 = `PASS / PRODUCT OWNER APPROVED`.

P0.3 is now eligible to start its own validation work, but remains unvalidated until new P0.3 evidence is produced.

## P0.3 Current Validation Note｜2026-09-28

- Opening V001 remains Product Owner-approved and canonically archived.
- S02-A completed the full image-to-video production lifecycle.
- Final S02-A sequence: `N11 → N12 → A04 → N14 → N15 → A05`.
- Canonical audio boundary: `00:33.020 → 01:18.750`.
- Canonical video: `S02_A_ASSEMBLY_V001`.
- Exact Binary Verification, Canonical Publication, Video Index Registration and Registration Verification all passed.
- S02-A is `PRODUCT_OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / FORMALLY CLOSED`.
- This sequence-level completion does **not** satisfy or auto-approve the whole P0.3 Gate.
- P0.3 remains `IN PROGRESS / NOT YET VALIDATED`.
- Next production work begins after canonical audio `01:18.750` only after Product Owner authorization.

