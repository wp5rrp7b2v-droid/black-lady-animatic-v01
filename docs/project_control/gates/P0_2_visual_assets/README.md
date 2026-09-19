# P0.2｜人物锚定与 Scene Master 资产治理

Status: `ACTIVE / P1 CHARACTER PRODUCTION RESUMED / AO-06 PARALLEL CLOSEOUT`

## 当前目标

P0.2 建立可规模化的 **Visual Asset Management System V1**，并把现有《黑衣夫人》视觉资产迁移到统一治理模型中。

当前锁定的系统方向：

`Entity → Atomic Master Assets → Derived Reference Sheet → Reference Resolver → Shot Reference Package → Generation → Product Owner Approval → Automatic Ingest → Asset Registry / Audit Trail`

目标是在正常生产中取消 Product Owner 的例行人工挑图、下载、命名、存储、登记与版本维护；Product Owner 只保留创意判断、异常处理与正式审批。

## 当前正式状态｜2026-09-18 EOD

- AO-01：`COMPLETE / VERIFIED`
- AO-02：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- AO-03：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- AO-04：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- AO-05：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- AO-06：`D-069 ENGINEERING FOUNDATION MERGED / EVIDENCE BLOCKED / EOD PAUSED`
- AO-07：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`
- RISK-001：`CONTROLLED / MITIGATION VERIFIED`
- P1 Character Production：`RESUMED BY PRODUCT OWNER 2026-09-19`；next = `CHAR_JUN_LUYUAN PROFILE_LEFT`；AO-06 remains mandatory before P0.2 final closeout

当前正式任务：

`P0.2-03｜P1 Character Production resumed｜NEXT: CHAR_JUN_LUYUAN PROFILE_LEFT`\n\nParallel closeout track: `D-069｜AO-06 remains OPEN; A04 binary substep waits for MacBook access`

AO-03 已于 2026-09-17 完成最终 DoD 验收并由 Product Owner 明确批准；正式 Closeout：

`ao03_closeout_2026-09-17.md`

## TEMP_CLOUD_ONLY_MODE_V1

Status: `APPROVED / EFFECTIVE / 2026-09-16—2026-09-20`

Product Owner 于 2026-09-14 批准临时纯云端执行模式；正式生效时间为 `2026-09-16 00:00`。

正式规则文件：

`temp_cloud_only_mode_v1.md`

Decision：`BL-D-031`

Rules Change：`RC-018 + RC-019`

### 临时模式目标

16～20 日只推进剩余 P0.2 主依赖链：

`AO-04 → AO-05 → AO-06`

不得因为本地 Mac 暂不可稳定使用而：

- 提前进入 P0.3；
- 提前解除 P1 Wave 2 HOLD；
- 降低 AO-04～AO-06 Definition of Done；
- 重建、猜测或伪造当前无法取得的 local-only 正式资产。

### 临时工具分工

**ChatGPT App**

- 分析、方案、Schema、Task Contract、DoD；
- 审核、Prompt、Product Owner 决策；
- Project Control 轻量文本维护。

**Codex Cloud**

- 确有必要的 repo 多文件工程修改；
- Registry / Resolver / scripts / tests / JSON / Markdown；
- Reference Package / Derived Reference Sheet 工程产物；
- commit + Codex Cloud native PR publication。

**GitHub Web / App**

- SSOT 阅读；
- diff / commit / remote publication 核验；
- PR base/head/changed-files 独立审核；
- Product Owner 批准后 merge。

**Local Mac / Terminal**

有效期内：

`TEMPORARILY UNAVAILABLE / DO NOT ASSUME LOCAL ACCESS`

### Cloud PR workflow verification｜2026-09-15

`CLOUD-DRILL-001` 已真实验证：

`GitHub source snapshot → Codex Cloud checkout → controlled change → Cloud commit/work reference → native PR publication → GitHub PR review → Product Owner approval → merge`

验证证据：

- GitHub PR：`#5`
- Source baseline：`a6db067927e26d19d5566d64fe04d3cb72a24961`
- PR Head：`codex/-codex-cloud-pr`
- Merge SHA：`774a6abed34b81e5558dbfeba3846380fb1ff26e`
- Evidence：`cloud_pr_workflow_drill_2026-09-15.md`

Cloud shell 内直接 `git push` 所需 GitHub credential 不作为临时模式 baseline；已验证的正式远端 publication 路径是 Codex Cloud native PR。若 Codex task UI 未返回 PR number / URL，必须以 GitHub 远端事实核对为准。

### RC-015 与本地同步

`RC-015` 保持 `ACTIVE / PROJECT-WIDE EXECUTION ROUTING LOCKED`，本临时模式不替代 RC-015。

`RC-012` 亦不被删除或 supersede，但 2026-09-16～2026-09-20 临时执行：

`LOCAL_SYNC_DEFERRED / GITHUB_MAIN_CANONICAL`

恢复本地 Mac 后，在任何正式本地生产前必须先完成：

`git status → connectivity preflight → git pull --ff-only origin main → local/remote truth check`

## 已锁定项目级规则

- 只有 Product Owner 明确批准的视觉结果才能进入正式 Asset Registry；
- 人物 / 场景 / 服装 / 道具统一采用 Entity → Asset 模型；
- Approval 与 Lifecycle 分离；正式生命周期为 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；
- Authority / Lifecycle / Resolver Usage 分离；
- Atomic Asset 与 Derived Reference Sheet 分离；Derived Reference 必须可追踪上游依赖；
- 正常生产目标为 `Shot / Task Spec → Reference Resolver → Reference Package`；
- 正式资产的来源、审批、版本、替代、依赖与生产调用必须有 Audit Trail；
- Entity / Asset Registry Schema V0.3 已由 Product Owner 于 2026-09-13 批准锁定；
- canonical Shot ID 不继承历史 `REBOOT` 标签；
- Character Atomic / Auxiliary production reference 目标画幅为 9:16；
- 图片生成后由 Product Owner 发送 `【审核】` 触发 Fixed Standard Review；
- D-059 Character Asset Migration V1 已完成并远端验证；
- D-060 Reference Package Exporter V0.1 已验证自动选图 + 本地 Reference Package；
- D-061～D-065 已接通 Character ingest、P1 role 泛化、Migration + Runtime resolution、Controlled Current Supersession 与 macOS launcher；
- AO-03 已完成 Scene Registry / State Profile / state-aware Resolver 验证；
- RC-015 长期 Execution Routing 保持锁定；
- RC-017 GitHub Network Recovery Runbook 已锁定并经 AO-07 验证；
- RC-019 已补充 Codex Cloud native PR 作为 TEMP_CLOUD_ONLY_MODE 的已验证 publication 路径。

## P0.2-01｜Visual Asset Authority Audit

Authority Mini-Close 已锁定。D-059 已将 48 张 approved Character references 迁入 canonical GitHub storage，并发布 Migration Mapping Manifest。

AO-01 已按 BL-D-028 完成可取得证据的旧表对账，四份旧表退出 Current authority。AO-02 已把 48 个 confirmed legacy Character assets 纳入长期 Asset Registry / Audit identity。

P0.2 Gate Review 前仍需：

1. AO-06：完成真实 Shot Spec Resolver + Shot-level Audit reverse-trace 的 end-to-end real validation。

AO-01、AO-02、AO-03、AO-04、AO-05、AO-07 已完成，不再属于 remaining checks。

## P0.2-02｜Visual Asset Management System V1 Design

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
- Fixed Standard Review；
- AO-03 Stable Scene identity / State separation + executable Scene rules + state-aware Resolver。

## P0.2-03｜Character Tier Assignment + Gap Analysis + P1 Production

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

P1 Character production 已由 Product Owner 于 2026-09-19 恢复。当前从 `CHAR_JUN_LUYUAN PROFILE_LEFT` 继续；AO-06 仍须在 P0.2 final closeout 前完成，但不再阻塞 P1 production sequencing。

## P0.2-04｜Approved-but-Open System Closeout

Status: `ACTIVE / ONLY AO-06 REMAINS FOR P0.2 FINAL CLOSEOUT / P1 PRODUCTION RESUMED`

1. AO-01｜4 Canonical Registers Final Reconciliation — `COMPLETE / VERIFIED`；
2. AO-02｜48 legacy Character assets → Long-term Registry / Audit — `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`；
3. AO-03｜Scene Master Structured Facts + Scene / Costume / Prop / State / Variant executable Spec — `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`；
4. AO-04｜9 Derived Character Reference Sheets + dependency / staleness — `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`；
5. AO-05｜Delivery Bridge — `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`；
6. AO-06｜Real Shot Spec Resolver + Shot-level Audit reverse-trace — `D-069 ENGINEERING FOUNDATION MERGED / EVIDENCE BLOCKED / EOD PAUSED`；
7. AO-07｜GitHub Network Resilience / Recovery Method — `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`。

AO-06 当前事实：
- PR #10 已经独立 cross-check 后 merge，merge SHA `68716eae9e73a1ee1891dfde6ac5c7ea4d578cce`；
- D-069 工程基础已进入 main，但 AO-06 **未 COMPLETE / 未 APPROVED**；
- A04 approved binary 尚未 materialize 到当前 GitHub runtime；
- Neil Costume/Cross 是否继续要求独立 formal Asset，或应改为 Character canonical appearance continuity，留待下一工作日由 Product Owner 审核设计边界；
- 在该模型/证据问题解决前，不启动 Work real validation，不分配 D-070。

## AO-03 Closeout

稳定 Scene Entity：

- `SCENE_CASTLE_ENTRANCE`
- `SCENE_FIRST_HALL`

legacy/source alias：

- `CASTLE_ENTRANCE_OPEN_DOOR_DAY`
- `FIRST_HALL_FIREPLACE`

正式 Scene Master：

- `AST_IMG_000052`
- `AST_IMG_000053`

D-067 已完成 Entity Registry、Scene State Profiles 与 state-aware Resolver；原图 SHA 保持不变，54 项完整测试通过。AO-03 最终 DoD 已由 Product Owner 于 2026-09-17 批准。

Completion evidence：

- `ao03_closeout_2026-09-17.md`
- PR `#6｜AO-03: add executable Scene registry and state-aware resolver`
- Merge SHA：`b16ffdd5f1c57f0b2c28acdee3caac656afb91a3`

## AO-04 Temporary-mode boundary

9 名 Character Derived Reference Sheet 必须基于 GitHub 当前 `CURRENT` Atomic Assets 自动生成，并记录明确 `derived_from Asset IDs / versions`，验证 `DEPENDENCY_STALE`。

## AO-05 Temporary-mode boundary

只有真实 `Reference Package → actual image-production environment` 验证通过后才能 `COMPLETE / VERIFIED`。

仅工程实现完成时必须保留：

`ENGINEERING COMPLETE / VALIDATION PENDING`

## AO-06 Temporary-mode boundary

必须真实完成：

`Shot Spec → Resolver → traceable Reference Package → Actual Production Use → USES_REFERENCE → Audit Trail`

缺少真实 generation/use 时必须保持：

`ENGINEERING COMPLETE / END-TO-END VALIDATION PENDING`

## Risk Alert｜RISK-001 GitHub Connectivity Instability

Status: `CONTROLLED / MITIGATION VERIFIED`

AO-07 已完成并经 Product Owner 批准。动态 `git-proxy-auto`、HTTP/1.1 fallback、`PENDING_REMOTE_PUBLICATION`、ACK loss / remote mismatch 与真实 failure→recovery 均已有正式 Runbook 与验证证据。

## D-059～D-067｜Engineering Baseline

- D-059｜Character Asset Migration V1 — COMPLETE / REMOTE VERIFIED
- D-060｜Reference Package Exporter V0.1 — TEST APPROVED / PO APPROVED
- D-061｜One-click Character Ingest + Cleanup — COMPLETE / REMOTE VERIFIED
- D-062｜P1 Character Reference Package Generalization — COMPLETE / REMOTE VERIFIED
- D-063｜Unified Migration + Runtime Character Asset Resolution — COMPLETE / REMOTE VERIFIED
- D-064｜Controlled Current Supersession — COMPLETE / REMOTE VERIFIED
- D-065｜macOS Bash Launcher Fix — COMPLETE / REMOTE VERIFIED
- D-066｜AO-01 Four Registers Final Reconciliation — COMPLETE / VERIFIED
- D-067｜AO-03 Scene Registry + State-Aware Resolver — `COMPLETE / REMOTE VERIFIED / PRODUCT OWNER APPROVED`

`CLOUD-DRILL-001` 是 operations workflow drill，不占 D-###。

下一新的 Codex 工程编号仅在确实交给 Codex 的新工程任务启动时使用：`D-068`。

## 当前执行基线

P1 按人物整组推进：

1. 宁秋水：`PROFILE_LEFT + REAR_3Q_LEFT` = **COMPLETE**
2. 君鹭远：`PROFILE_LEFT + REAR_3Q_LEFT` = **HOLD UNTIL AO-04～AO-06 COMPLETE**
3. 尼尔：`PROFILE_RIGHT + REAR_3Q_RIGHT`
4. 苏小小：`PROFILE_LEFT + REAR_3Q_LEFT`
5. 廖健：`PROFILE_LEFT + REAR_3Q_LEFT`

## 下一步

下一正式任务：

`D-068｜AO-04｜Stage A Candidate Build + Dependency Staleness Engineering｜WAITING_PRODUCT_OWNER_VISUAL_APPROVAL`

目标：基于 9 名正式 Character 的 `CURRENT / APPROVED` Atomic Assets 自动生成/验证 Derived Character Reference Sheets，记录明确上游 Asset IDs / versions，并验证 `DEPENDENCY_STALE` 行为。

AO-04 完成前不得启动 AO-05；P1 Wave 2 继续 HOLD。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。

## 2026-09-19｜P1 Production Resume Override

Product Owner 明确调整执行顺序：AO-06 / D-069 保持打开并继续作为 P0.2 最终 Closeout 必做项，但不再作为 P1 Character production 的前置阻塞。剩余 P1 8 项按 BL-D-022 原顺序继续：君鹭远左侧 Profile + Rear 3Q → 尼尔右侧 Profile + Rear 3Q → 苏小小左侧 Profile + Rear 3Q → 廖健左侧 Profile + Rear 3Q。P0.3 继续 QUEUED。


## P1｜Jun Luyuan PROFILE_LEFT delivery status｜2026-09-19

- Direct Work binary materialization: `FAIL CLOSED / known transport limitation`.
- GitHub Actions fallback bundle: `READY`.
- Run: `35422665719 / SUCCESS`.
- Artifact: `10577930931 / P1_JUN_LUYUAN_PROFILE_LEFT_DELIVERY_BUNDLE_V001`.
- ZIP digest: `sha256:a4cd646a66f7925089be869178efe255ce1e0612e36633358e883bf86a290075`.
- 4/4 canonical references validated by Asset ID / Role / CURRENT / APPROVED / DEFAULT / byte size / SHA256.
- Next: Work artifact download → independent 4/4 verification → PROFILE_LEFT generation → Fixed Standard Review.
- No Registry mutation; D-070 not allocated.


## P1｜Jun Luyuan PROFILE_LEFT approval｜2026-09-19

- Status: `PRODUCT OWNER APPROVED / FORMAL INGEST PENDING`.
- Target: `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Approved source: PNG / 941×1672 / 1,933,426 bytes.
- Approved source SHA-256: `00915474a52a29df753542b916503998c450b056d2ef59d98279841fdc9ad9be`.
- Work did not return the candidate PNG SHA, so no claim is made that this upload was cryptographically compared to a prior Work-candidate digest; this exact upload is now the Product Owner-approved source identity.
- Next: exact-byte canonical publication + Automatic Ingest + Registry/Audit verification; then Jun Luyuan `REAR_3Q_LEFT`.


## P1｜Jun Luyuan PROFILE_LEFT V002 visual candidate｜2026-09-19

- V001 visual approval withdrawn before formal ingest due to neck-proportion concern.
- V001: `DO NOT INGEST`.
- Preferred revised image: `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002 / VISUAL CANDIDATE`.
- V002 was generated in Chat outside the formal four-reference Delivery Bundle path, so it is not yet a formal Asset.
- Required before ingest: canonical 4-reference rerun → Fixed Standard Review → explicit Product Owner approval → exact-byte canonical publication → Automatic Ingest.


## P1｜Jun Luyuan PROFILE_LEFT V002 Work output rejection｜2026-09-19

- Work bundle/reference validation: `PASS`.
- Work returned image: `REJECTED BY PRODUCT OWNER / WRONG IMAGE`.
- Formal V002 revalidation remains incomplete.
- Rerun must explicitly target the Product Owner-selected strict left-profile short-neck candidate; do not confuse it with the earlier REAR_3Q visual direction image.
- No ingest.


## P1｜Jun Luyuan PROFILE_LEFT V002 rerun status｜2026-09-19

- Work rerun: `INTERNAL APPROVED FINAL CANDIDATE`.
- Correct short-neck strict-left-profile target reportedly used.
- Canonical four-reference identity authority retained.
- Main Chat has not yet visually reviewed the actual final image.
- No Product Owner approval yet; no ingest.


## P1｜Jun Luyuan PROFILE_LEFT V002 PO approval｜2026-09-19

- Formal filename: `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png`
- Status: `PRODUCT OWNER APPROVED / FORMAL INGEST PENDING`
- Exact approved PNG: 941×1672 / 1,938,522 bytes
- SHA-256: `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c`
- V001: `DO NOT INGEST`.
- Required next step: exact-byte canonical publication + remote SHA verification + Automatic Ingest + Registry/Audit verification.
