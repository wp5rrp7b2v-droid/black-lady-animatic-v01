# Execution Log｜BLACK-LADY-001

## 2026-09-21｜Character Visual Completion + 21 Binary Canonical Publication

- Product Owner approved Castle Young Master `REAR_3Q_LEFT V001` and all six Black Lady P3 lateral views; Character Core visual production therefore reached `63/63 PO APPROVED` with visual gap `0`.
- The 21 pending approved PNGs were consolidated outside the repo, UUID/unrelated files were separated, canonical filenames were verified, and source→repo copies passed `21/21 exact-byte SHA_MATCH` before staging.
- Git staging was restricted to exactly the 21 Character Core PNGs; unrelated untracked `black_lady_character_asset_migration_v1.zip` and `production/audio/` were not staged.
- Local publication commit: `b9bafa2af4b9be8aadf2bd2abe79b724837eff88` — `Publish 21 approved character core view PNGs`.
- First standard push failed with `Empty reply from server`; retry using temporary `http.postBuffer=524288000` succeeded. GitHub main independently verified at the same commit.
- GitHub commit contains the intended 21 PNG additions; all 21 committed binaries were re-read via Git object and independently verified `21/21 SHA_MATCH` against approved source identities.
- No Asset Registry/Audit mutation was performed. Formal Core Coverage remains `42/63 = 66.7%`.
- Engineering boundary identified: `automatic_ingest_controller_v0_1.py` expects canonical target not to exist, so direct ingest of these already-published binaries would fail closed with `Target already exists`.
- Next proposed Codex Cloud task: `D-070｜Published Binary Adoption + 21-Asset Automatic Ingest`; NOT STARTED tonight and D-number is consumed only when execution actually launches.
- AO-06 / D-069 remains OPEN and mandatory for P0.2 final closeout. P0.2 remains ACTIVE; P0.3 remains QUEUED / DO NOT START EARLY.

## 2026-09-18｜Daily Closeout / D-069 Engineering Foundation Merge

- PR #10 reviewed head `7cf9e82cf937bc4150c83bcf0fc04e57e334e824` merged to `main` as `68716eae9e73a1ee1891dfde6ac5c7ea4d578cce`.
- Merge scope = D-069 engineering foundation + Review Patch 01 only; AO-06 remains IN PROGRESS and is not Product Owner approved.
- Post-merge Registry truth cross-check: Asset 62 / Entity 13 / Relations 44 / Audit 78 / Formal SHOT 0 / COSTUME 0 / PROP 0 / live USES_REFERENCE 0.
- Project Control advanced to R054 and end-of-day state is `PAUSED / RESUME SAME D-069`.
- Current hard evidence gap: approved A04 binary is not materialized in current Runtime Registry.
- Historical A-Series registration indicates a likely legacy Shot migration/recovery gap; do not regenerate A04.
- Neil Costume/Cross modeling boundary was questioned by Product Owner today; no new model decision locked. Review next session before creating any new visual Asset.
- P1 Wave 2 remains HOLD; P0.3 remains QUEUED; D-070 remains unallocated.
- Daily cross-file consistency closeout recorded in `gates/P0_2_visual_assets/daily_closeout_2026-09-18.md`.


## 2026-09-18｜D-069 Review Patch 01

- Corrected R053 nested checkpoint/AO-06 state; resume remains the same D-069 after evidence is supplied.
- Recorded PR #10 / `codex/a04` / review-start remote head `351a41b9452eafc01e724fd6f36f9edb6793c627`; PR remains open and must not be merged.
- Enforced Character Sheet `resolver_usage != NEVER`, exact A04 evidence `DEFAULT/DEFAULT`, and Schema V0.3 `created_by_event_id` relation/audit cross-reference.
- No live Registry mutation and no live `USES_REFERENCE` write.


## 2026-09-18｜D-069 AO-06 Stage 3 first-run engineering checkpoint

- Baseline `0208a31f...` / R052 verified; 68 tests / OK.
- Added executable A04 spec, fail-closed resolver/package, immutable use-record and reverse audit, plus isolated `USES_REFERENCE` transaction proof.
- Added Costume/Prop semantic Entities only; no visual Asset was fabricated.
- Search found no provenance-verifiable approved A04 binary and no dedicated approved Costume/Cross reference.
- Truthful state: `ENGINEERING FOUNDATION COMPLETE / BLOCKED_ON_APPROVED_A04_BINARY / BLOCKED_ON_COSTUME_PROP_EVIDENCE`; `generation_allowed=false`; no live `USES_REFERENCE`.


## 2026-09-18｜AO-06 Stage 2 Product Owner Approval

Status: `APPROVED / D-069 STAGE 3 NEXT`

- Product Owner 明确批准 `AO-06 Stage 2｜A04 Real Shot Spec V0.1 + Resolver Contract`。
- A04 executable Shot Spec structure 正式锁定。
- Required resolved anchors：`CHAR_NING_QIUSHUI / AST_IMG_000060`、`CHAR_NEIL / AST_IMG_000059`、`SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN / AST_IMG_000052`。
- Required current gaps：`COSTUME_NEIL_DEFAULT`、`PROP_NEIL_CROSS`；任一 required gap 存在时必须 `generation_allowed=false`。
- White pocket handkerchief 锁定为 `COSTUME_NEIL_DEFAULT` required component，不建立独立 fabricated Prop。
- Exact Shot photography 必须来自真实 approved A04 source evidence，不得从 Scene Master 或聊天记忆猜测。
- Historical A04 不允许重建/补造历史 `USES_REFERENCE`。
- AO-06 当前真实 use 必须进入 immutable validation use record；live `USES_REFERENCE` 只允许指向真实、可证明输入的已批准 formal output。
- Product Owner 授权下一 Codex 工程任务编号：`D-069`，用于 AO-06 Stage 3 implementation + real validation。
- P1 Wave 2 / P0.3 继续 HOLD / QUEUED。

## 2026-09-18｜AO-06 Stage 2｜A04 Real Shot Spec + Resolver Contract Ready

Status: `READY_FOR_PRODUCT_OWNER_REVIEW`

- Stage 2 design follows Product Owner-approved Stage 1 without changing A04 narrative facts.
- A04 executable Shot Spec candidate separates required Characters, state-aware Scene, required Costume/Prop continuity, action semantics, negative-continuity boundary, and Shot-photography evidence.
- Current expected Resolver result:
  - `CHAR_NING_QIUSHUI → AST_IMG_000060 / RESOLVED`;
  - `CHAR_NEIL → AST_IMG_000059 / RESOLVED`;
  - `SCENE_CASTLE_ENTRANCE + DAY_DOOR_OPEN → AST_IMG_000052 / RESOLVED`;
  - `COSTUME_NEIL_DEFAULT → REFERENCE_GAP`;
  - `PROP_NEIL_CROSS → REFERENCE_GAP`.
- White pocket handkerchief is modeled as a required component of `COSTUME_NEIL_DEFAULT`, not a separate fabricated Prop.
- Any required REFERENCE_GAP blocks generation; no Character asset may silently satisfy a Costume/Prop requirement.
- Exact A04 Shot photography remains evidence-bound and may only be populated after the approved A04 source is materialized.
- Historical A04 provenance must remain honest: if A04 Shot Master is formalized with `provenance_status=PARTIAL`, no historical `USES_REFERENCE` relations may be backfilled from memory.
- AO-06 actual use will be captured in an immutable validation use record. `USES_REFERENCE` direction is locked candidate as `formal output SHOT asset → actual reference asset`; relation/reverse-query behavior can be tested in an isolated registry transaction without polluting live history. Live relation write requires a genuinely approved formal output with provable input use.
- No D-069 allocated by Stage 2 design.

## 2026-09-18｜AO-06 Stage 1 Product Owner Approval

Status: `APPROVED / STAGE 2 NEXT`

- Product Owner 明确批准 AO-06 Stage 1。
- Canonical validation Shot 锁定为 `A04`。
- A04 Scene requirement 锁定为 `SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`。
- Required Characters 锁定为 `CHAR_NING_QIUSHUI + CHAR_NEIL`。
- Neil default butler costume、cross、white handkerchief 被确认是 AO-06 的 Costume/Prop continuity requirements；当前正式 Runtime 仍无 `COSTUME_*` / `PROP_*` assets，因此 Stage 2 必须显式处理 REFERENCE_GAP，不得冒充已正式化资产。
- A04 不承载 A05 的 `keys absent` insert fact；若未来需要，必须建模为 negative continuity / forbidden presence，而不是 fabricated Prop asset。
- Exact Shot photography 仅能来自 approved A04 evidence；不得从 Scene Master 或 chat memory 推断为正式 camera metadata。
- Stage 2 next：`A04 Real Shot Spec V0.1 + Resolver Contract`。
- No D-069 allocated.

## 2026-09-18｜AO-06 Stage 1｜A04 Selection + Fact Boundary Ready

Status: `READY_FOR_PRODUCT_OWNER_REVIEW`

- AO-06 Stage 1 compared A01–A07 and recommends canonical Shot `A04`.
- A04 is preferred because it covers two Characters + state-aware Castle Entrance + Neil Costume/Prop continuity without A01 crowd complexity or A05 detail-insert over-specialization.
- Current Registry independently verified: `SHOT=0 / PROP=0 / COSTUME=0`.
- Formal anchors available now: `AST_IMG_000060 / CHAR_NING_QIUSHUI Reference Sheet`, `AST_IMG_000059 / CHAR_NEIL Reference Sheet`, `AST_IMG_000052 / SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`.
- Proposed A04 executable gaps: `COSTUME_NEIL_DEFAULT`, `PROP_NEIL_CROSS`; white pocket handkerchief treated as a required Costume component proposal. None are claimed formal yet.
- A04 does not inherit A05's “keys absent” insert fact. Any absence rule must be represented as negative continuity, not a fabricated Prop asset.
- Scene Facts vs Shot Photography boundary remains locked; camera/lens/composition cannot be invented from the Scene Master or chat memory.
- No D-069 allocated; no Registry/Relation/Audit production mutation performed.

## 2026-09-18｜AO-05 Final Product Owner Acceptance

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

- Product Owner 于 2026-09-18 明确批准 AO-05 最终验收。
- Primary single-reference Delivery Path 已 PASS；Fallback Artifact Bridge 已完成 RUN A / RUN B 多 reference + repeatability 真实验证。
- 两轮均使用同一 formal input set：`AST_IMG_000056 / 000011 / 000009 / 000008`，4/4 SHA match，loaded_reference_count=`4`，proof generated，manual Product Owner reference upload=`0`。
- 所有 proof 均为 `NON-PRODUCTION`；未 ingest、未登记 Asset ID、未改变 Character Core Coverage。
- D-069 未分配；AO-05 不需要额外 Codex 工程任务即可完成 DoD。
- 残余审计限制：image-generation service 当前不返回独立 consumed-input SHA / cryptographic receipt。Product Owner 明确接受该限制为 non-blocking residual audit risk，并要求未来能力允许时补齐。
- 该限制登记为 `RISK-002 / ACCEPTED / NON-BLOCKING / DEFERRED IMPROVEMENT`。
- 临时 `.github/workflows/ao05-fallback-artifact-bridge.yml` 在 AO-05 closeout 中删除；已生成 artifact 按 GitHub retention policy 自动过期。
- AO-06 成为下一正式任务；P1 Wave 2 与 P0.3 继续 HOLD / QUEUED。
- Closeout evidence：`docs/project_control/gates/P0_2_visual_assets/ao05_closeout_2026-09-18.md`。

## 2026-09-18｜AO-05 Fallback Robustness Proof｜PASS

Status: `ROBUSTNESS PASS / READY_FOR_FINAL_PRODUCT_OWNER_ACCEPTANCE`

- Work 自动下载 GitHub Actions artifact `10536850548`；Product Owner 未手工下载或上传 reference。
- Received ZIP bytes: `9,094,747`.
- ZIP SHA256 independently verified: `a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`.
- Environment: `ChatGPT Work / built-in image generation`.
- RUN A exact inputs: `AST_IMG_000056 / 000011 / 000009 / 000008`; 4/4 binaries materialized; 4/4 SHA matched; loaded_reference_count=`4`; proof `AO05_FALLBACK_MULTIREF_RUN_A` generated; manual Product Owner reference uploads=`0`.
- RUN B independently re-read the same ZIP, extracted to an independent directory, recalculated all four hashes, confirmed the same four Asset IDs and SHA values, loaded_reference_count=`4`, and generated `AO05_FALLBACK_MULTIREF_RUN_B`; manual Product Owner reference uploads=`0`.
- `input_set_identical_between_runs=YES`.
- `multi_reference_delivery=PASS`.
- `repeatability=PASS`.
- Both proofs are `NON-PRODUCTION`; neither was ingested or registered; Core Coverage unchanged.
- No GitHub / Registry mutation occurred in Work; D-069 remains reservation-only and was not allocated.
- Evidence boundary: image generation did not emit an independent input-SHA receipt; evidence is canonical GitHub runner verification + artifact digest + Work-side independent byte/SHA validation + actual four-reference generation calls.
- Two consecutive successful runs prove repeatability for this validated path; they do not assert indefinite long-term service stability.
- AO-05 remains `IN PROGRESS` until explicit Product Owner final acceptance.

## 2026-09-18｜AO-05 Fallback Artifact Bridge｜READY

Status: `FALLBACK ARTIFACT READY / WORK ROBUSTNESS VALIDATION PENDING`

- Product Owner authorized establishment of AO-05 Fallback Artifact Bridge.
- Temporary workflow created at `.github/workflows/ao05-fallback-artifact-bridge.yml`.
- Initial workflow revision had a YAML block-scalar syntax error and failed before jobs started; it was corrected immediately without any production mutation.
- Corrected workflow commit: `775238d05278af963d6e673063ce71ae522c18d1`.
- Successful workflow run: `35319662012`.
- Bundle ID / artifact name: `AO05_GUANG_YONG_DELIVERY_BUNDLE_V001`.
- Artifact ID: `10536850548`.
- Artifact size: `9,094,747 bytes`.
- Artifact ZIP digest: `sha256:a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`.
- Artifact expires: `2026-09-25T07:29:39Z`.
- Source set exactly: `AST_IMG_000056 / 000011 / 000009 / 000008`.
- GitHub runner verified Registry identity/state, canonical file existence, exact SHA256 and byte size for all 4; copied bundle bytes were re-hashed; a second pre-upload verification passed `4/4 exact binaries`.
- Bundle contains 6 files: 4 visual references + `delivery_manifest.json` + `WORK_HANDOFF.md`.
- No Product Owner reference upload was required; no Registry or formal Asset mutation occurred; D-069 remains unallocated.
- Next validation occurs in Work: artifact download/materialization → manifest + byte verification → multi-reference RUN A → independent repeatability RUN B.

## 2026-09-18｜AO-05 Multi-reference Robustness Proof｜CANONICAL_BINARY_MATERIALIZATION_FAILED

Status: `FAIL CLOSED / FALLBACK REQUIRED / AO-05 REMAINS IN PROGRESS`

- Work 读取 main 四份事实源并确认 R044 / ROBUSTNESS VALIDATION PENDING。
- RUN A 在 binary acquisition 阶段停止；generation environment 未调用。
- `AST_IMG_000056`：GitHub file API 返回 Reference Sheet Base64；本轮未以统一多文件路径完成 materialization / SHA receipt。
- `AST_IMG_000011 / AST_IMG_000009 / AST_IMG_000008`：file API 返回空 binary content / metadata only；blob read 触发 UnicodeDecodeError；raw blob path 被 UTF-8-only interface 拒绝。
- 因无法取得四张可独立哈希的 bytes，`sha256_verified=0/4`，`loaded_reference_count=0`，proof 未生成。
- RUN B：NOT STARTED，因此 repeatability 未测试。
- Product Owner manual reference upload count = `0`；未通过人工上传规避失败。
- 失败边界明确定位为 Work 当前 GitHub binary materialization transport；不等于 multi-reference image generation unsupported。
- 未修改 GitHub/Registry/正式 Asset；未分配 D-069；AO-06 / P1 Wave 2 / P0.3 均未启动。
- 下一步采用 AO-05 已预定义 fallback：`GitHub Actions → short-lived manifest-verified Delivery Bundle artifact → Work`。

## 2026-09-18｜AO-05 Primary Delivery Path Proof｜PASS

Status: `PRIMARY DELIVERY PATH PASS / ROBUSTNESS VALIDATION PENDING`

- Work 读取 GitHub main / Project Control，确认 source revision R043 / AO-05 DESIGN IN PROGRESS。
- 验证对象：`AST_IMG_000056 / CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`。
- GitHub / Registry 独立事实：`APPROVED / CURRENT / DERIVED / DEFAULT`；canonical path 正确；byte_size=`475761`；SHA256=`2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`。
- Work 从 GitHub 自动 materialize 正式 PNG，无 Product Owner 手工挑图或上传。
- Work receipt：received byte size `475761`，received SHA256 与 expected 完全一致。
- 正式 reference binary 已通过 Work 的 image-production path 作为真实视觉参考输入，并成功生成 `AO05_DELIVERY_PROOF_ONLY`。
- Proof 明确为 `NON-PRODUCTION`；未进入 Asset Registry；未改变 Core Coverage；未启动 P1 Wave 2。
- Product Owner manual reference file upload count = `0`。
- 能力边界：单文件路径已证明；生成服务未给出独立 input-SHA receipt，因此证据链为 GitHub canonical bytes + Work 本地 SHA 核验 + 实际 reference path 调用 + proof generation。
- 尚未验证 multi-file delivery 与 repeated-run stability；AO-05 不标记 COMPLETE。
- D-069 仍 `RESERVATION ONLY / NOT ALLOCATED / NOT EXECUTED`。

## 2026-09-18｜AO-05 Delivery Bridge Design Start

Status: `DESIGN IN PROGRESS / CHAT / NO D-NUMBER ALLOCATED`

- Product Owner 明确启动 AO-05。
- AO-05 继续遵守既有完成标准：Reference Package 必须稳定进入实际 image-production / generation environment；输入 Asset ID / version / SHA 可追踪；减少 Product Owner 逐张挑图、上传和搬运；不得把仍需人工的环节描述为自动化完成。
- 本阶段先由 Chat 完成 Delivery Bridge V0.1 设计，不分配 D-069。
- 设计原则：AO-05 不新增 Resolver 选图权威，不修改 AO-04 Formal Assets；Delivery Bridge 只消费既有 Resolver / Reference Package 输出并负责可验证交付。
- 当前无 blocker；AO-06、P1 Wave 2、P0.3 继续保持原有 HOLD / PENDING / QUEUED 边界。

## 2026-09-18｜AO-04 Final Product Owner Acceptance

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

- Product Owner 于 2026-09-18 明确批准 AO-04 最终验收。
- 最终 DoD 基线：9 个 Character Entity；9 张 formal Derived Character Reference Sheets；42 个实际 Atomic dependencies；21 个明确 `REFERENCE_GAP`；63 个 Tier Core slots。
- Formal Asset IDs：`AST_IMG_000054–AST_IMG_000062`。
- Stage B publication commit：`09b9e2c44f8f2f78c1d102f3d141263074316310`，已 remote verified。
- 9 张 canonical PNG 与已批准 Candidate SHA / byte size 一致；全部 dependency status `FRESH`；Resolver 9/9 RESOLVED；Single Current 与 idempotency 验证通过。
- 完整仓库回归：`68 tests / OK`。
- AO-04 不改变 Character Core Coverage：`42/63 = 66.7%`；`REFERENCE_GAP=21`。
- 临时 D-068 Stage A review workflow 与 Stage B publication workflow 在最终验收后删除，避免进入最终 merge。
- AO-05 成为下一正式任务，但尚未启动；AO-06 仍 PENDING；P1 Wave 2 继续 HOLD；P0.3 继续 QUEUED。
- Completion evidence：`docs/project_control/gates/P0_2_visual_assets/ao04_closeout_2026-09-18.md`。

## 2026-09-18｜D-068 Stage B Engineering Complete / Remote Verified

- Product Owner 已于 2026-09-18 视觉批准全部 9 张 Stage A Candidate Character Reference Sheets，并授权 Stage B。
- GitHub Actions workflow `D-068 Stage B Publication`（run `35308216933`）在真实 `codex/ao-04` 分支执行并成功完成。
- Stage B publication commit：`09b9e2c44f8f2f78c1d102f3d141263074316310`；PR #9 远端 head 已独立核对为同一 SHA，PR 保持 OPEN / NOT MERGED。
- 同一 formal transaction commit 原子发布 12 个文件：9 张 canonical formal PNG + `asset_registry.jsonl` + `asset_relations.jsonl` + `audit_event_log.jsonl`。
- 正式结果：Asset Registry `62` 条；其中 AO-04 formal `DERIVED_REFERENCE=9`（`AST_IMG_000054–000062`）；AO-04 `DERIVED_FROM=42`；D-068/AO-04 `ASSET_FORMALIZED=9`。
- 9 张正式 PNG 的 SHA256 / byte size 与 Product Owner 已批准 Candidate manifests 逐一一致；Character Core Coverage 保持 `42/63 = 66.7%`，`REFERENCE_GAP=21`，未生成任何新人物视角。
- 9 张 Sheet 均验证为 `CURRENT / APPROVED / DERIVED / DEFAULT`，dependency status 全部 `FRESH`，Character Reference Sheet Resolver 9/9 RESOLVED。
- Idempotency：第二次执行 formalizer 返回 `ALREADY_FORMALIZED`，Registry / Relations / Audit / 9 PNG hashes 无变化。
- 完整仓库回归：`68 tests / OK`。
- Binary publication blocker 已解除。AO-04 仍保持 `IN PROGRESS`，当前状态为 `STAGE B ENGINEERING COMPLETE / REMOTE VERIFIED / READY_FOR_FINAL_PRODUCT_OWNER_ACCEPTANCE`。
- 未启动 AO-05；D-069 仍为 reservation only；P1 Wave 2 继续 HOLD；P0.3 继续 QUEUED；PR #9 不得 merge，等待 Product Owner 最终 AO-04 DoD 验收。
- Completion evidence：`docs/project_control/gates/P0_2_visual_assets/d068_stage_b_engineering_complete_2026-09-18.md`。

## 2026-09-18｜D-068 Stage B authorization and publication preflight

- Product Owner visually approved all 9 Stage A Candidate Sheets and authorized D-068 Stage B.
- Rehydration preflight passed: `9 manifests / 9 PNGs / 9/9 filename / 9/9 SHA256 / 9/9 byte size / 42 dependencies / 21 REFERENCE_GAP / 63 slots`.
- Stage B stopped before formalizer execution because the recorded Codex PR publisher cannot publish the nine required canonical formal PNG binaries and this checkout cannot verify supplied remote head `ebed801fdc5b35ceb000516b7352fd7241ceebf5`.
- Status: `BLOCKED_ON_FORMAL_BINARY_PUBLICATION`. D-068 formal state remains `DERIVED_REFERENCE=0 / DERIVED_FROM=0 / D-068 ASSET_FORMALIZED=0`; no prospective Asset ID was allocated.
- The temporary Candidate review workflow remains present because cleanup is authorized only after successful Stage B formalization and validation.
- AO-04 remains `IN PROGRESS`; D-069 remains reservation-only; AO-05 remains not started; PR #9 remains `OPEN / DO NOT MERGE`.
- Blocker evidence: `docs/project_control/gates/P0_2_visual_assets/d068_stage_b_formal_binary_publication_blocker_2026-09-18.md`.

## 2026-09-18｜D-068 Stage A Review Patch 01

- Continued the existing D-068 / AO-04 Stage A task; D-069 remains reservation-only and was not allocated or executed.
- Enforced `variant=DEFAULT` and `state=DEFAULT` in Atomic Candidate input selection, with negative regression coverage for non-default required-role rows, duplicate/default-slot ambiguity, and false Core-slot satisfaction.
- Complete repository suite: `68 tests / OK`.
- Rebuilt all 9 Candidate PNGs into a temporary review directory without overwriting the locked baseline: `9/9 SHA256 MATCH`; `42 selected dependencies / 21 explicit REFERENCE_GAP / 63 Tier Core slots`.
- Formal registry remains unchanged: `DERIVED_REFERENCE=0 / DERIVED_FROM=0`. AO-04 remains `IN PROGRESS`; Stage B and AO-05 were not started.
- Final state: `D-068 STAGE A ENGINEERING CLEAN / WAITING_PRODUCT_OWNER_VISUAL_APPROVAL / PR #9 OPEN / DO NOT MERGE`.

## 2026-09-17｜D-068 AO-04 Stage A engineering

- Project Control advanced `R039 → R040`; Dashboard advanced `V018 → V019`.
- AO-04 state: `IN PROGRESS / AO-04A PRODUCT OWNER APPROVED / D-068 STAGE A ENGINEERING COMPLETE / WAITING_PRODUCT_OWNER_VISUAL_APPROVAL`.
- Registered exactly nine stable Character Entities and appended nine `ENTITY_CREATED` audit events; both existing Scene Entities remain unchanged.
- Live preflight reconciled exactly `42 / 63` selected Atomic Core dependencies and `21` explicit gaps.
- Generated exactly nine deterministic, non-generative Candidate PNGs plus manifests outside the Formal Asset Registry.
- Implemented computed `FRESH / DEPENDENCY_STALE`, separate derived-reference resolution, fail-closed Stage B formalizer, and AO-04 tests. Full suite: `66 tests / OK`.
- No formal Derived Asset IDs or `DERIVED_FROM` relations were created. Stage B was not executed.
- AO-05 remains PENDING; P1 Wave 2 remains HOLD; P0.3 remains QUEUED.
- Publication transport boundary: Candidate PNG binary files are `CLOUD_REVIEW_ARTIFACT / NOT FORMAL ASSET / NOT INCLUDED IN STAGE A PR DUE TO CODEX PR BINARY TRANSPORT LIMITATION`. The nine PNGs remain byte-identical in the Codex Cloud workspace for Product Owner visual review; their filenames, expected logical paths, SHA256, byte sizes, dependency lineage, populated slots and explicit gaps remain recorded in the nine version-controlled manifests. This transport boundary does not alter Candidate approval status, dependency lineage, AO-04A authority, or the mandatory Product Owner approval stop.
本文件记录实际工程执行结果。只保留足以追溯结论的关键事实、证据、失败原因和最终结果；完整脚本、媒体文件、Commit 和工程资产由 GitHub / Local project 保存。

## Restart Baseline｜2026-09-11

- 项目进入 P0｜项目重启与基础能力再验证。
- 通过 `arch3d-reconstruction` 的 Project Control System 2.0 作为参考，继承 SSOT / Gate / Decision / Execution / Acceptance / Dashboard 派生化的管理思想。
- 旧《黑衣夫人》工程执行历史不在本次雏形中重写；后续只迁移仍会影响当前生产判断的必要事实。

## Historical Carry-forward｜PRE-AUDIT

以下只作为重启审计输入，不等于新的正式 Gate 结论：

- 历史 Codex 工程编号已到 D-056。
- D-056｜SOURCE_AUDIO_INDEX_V001 已建立原音频导航索引；历史使用证明不能直接把 ASR segment 时间边界当正式剪辑边界。
- A01–A07 存在已批准静态视觉版本；是否进入最终镜头序列待重新验证。
- A08_REBOOT 当前保持 HOLD。
- Remotion 已验证能够完成静态图、音频、帧级时间线到 MP4 的工程合成；过往 Animatic / 剪辑结果未达到成片要求。

## Current Execution State

- P0.1：PASS / PRODUCT OWNER APPROVED
- P0.2：ACTIVE / APPROVED-OPEN CLOSEOUT / AO-01 + AO-02 + AO-03 + AO-07 COMPLETE / AO-04 NEXT
- P0.3：QUEUED / DO NOT START EARLY
- 当前实际 Codex 工程编号：D-067；D-067 已 `COMPLETE / REMOTE VERIFIED / PRODUCT OWNER APPROVED`
- 下一 Codex 工程编号仅在新的 Codex 工程任务实际启动时使用：D-068；本次 Project Control consistency closeout 不占 D-###
- RISK-001：CONTROLLED / MITIGATION VERIFIED
- P1 Wave 2：HOLD UNTIL AO-04～AO-06 COMPLETE / VERIFIED
- TEMP_CLOUD_ONLY_MODE_V1：APPROVED / EFFECTIVE / TIME-BOXED THROUGH 2026-09-20
- Current formal task：AO-04｜9 Derived Character Reference Sheets + dependency/staleness｜NEXT

## AO-03 Product Owner Closeout｜2026-09-17

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Execution route: `CHAT REVIEW + GITHUB MERGE + PROJECT CONTROL CLOSEOUT / NO NEW D-NUMBER`

- AO-03 final DoD reviewed against approved AO-03A/B contract and D-067 implementation.
- `SCENE_CASTLE_ENTRANCE` and `SCENE_FIRST_HALL` verified as executable Stable Scene Entities.
- `AST_IMG_000052` and `AST_IMG_000053` verified as approved/current/master Scene Masters with source SHA preserved.
- Scene Facts / controlled State / Shot-variable Photography separation verified.
- State-aware Resolver verified to resolve DAY+OPEN and FIREPLACE_EXTINGUISHED and return `REFERENCE_GAP` for CLOSED / NIGHT / BURNING / missing-state / explicit-vs-UNSPECIFIED mismatches.
- D-067 full regression evidence: `54 tests / OK`; no implementation or regression blocker remained.
- Product Owner explicitly approved AO-03 on 2026-09-17.
- GitHub PR `#6｜AO-03: add executable Scene registry and state-aware resolver` merged.
- Merge SHA：`b16ffdd5f1c57f0b2c28acdee3caac656afb91a3`。
- Closeout evidence：`docs/project_control/gates/P0_2_visual_assets/ao03_closeout_2026-09-17.md`。
- Closeout evidence commit：`6d87401984b7dfe5f4a75db7b262f4fc684de9e5`。
- AO-03 final status：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`。
- P0.2 remains ACTIVE；P1 Wave 2 remains HOLD；P0.3 remains QUEUED。
- Next formal dependency：`AO-04 → AO-05 → AO-06`。

## D-067｜AO-03 Scene Registry + State-Aware Resolver｜ENGINEERING IMPLEMENTED / 2026-09-17

- Source checkout：`15ab19dd4c28257b47f7b6d79f852429ca772e7c`；work reference：`work`。
- 开始前确认 live Asset Registry 最大编号为 `AST_IMG_000051`；为两张既有 approved Scene Master 分配 `AST_IMG_000052`、`AST_IMG_000053`，未创建重复版本。
- 两个源 PNG 仅作 canonical rename / move，图像内容未修改；formalized SHA-256 分别保持 `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961` 与 `ce043c8adb244ce8f07a34f1a2b047b4d7ba41f72cdf777e3cd1877f4ac8b413`。
- 新增 executable Entity / Scene State Profile 数据；State facts 为多维显式字段，Shot Photography 只保留字段边界而不写入 Stable Scene Facts。
- Resolver 保留 Character migration/runtime、SHA、canonical path 与 Single Current 行为，并新增 Scene Master 显式 state subset match；NIGHT / CLOSED / BURNING / explicit-vs-UNSPECIFIED 均返回 `REFERENCE_GAP`。
- 完整测试：`python -m unittest discover -s tests -p 'test_*.py'` → `54 tests / OK`，覆盖既有 Character resolver、ingest、supersession、reference-package 与 AO-02 migration regression。
- 本节记录工程交付时的历史状态；AO-03 最终完成与 Product Owner 批准见上方 `AO-03 Product Owner Closeout｜2026-09-17`。

## Project Control Baseline Commit｜APPROVED / 2026-09-11

- Product Owner 批准 Dashboard V002。
- canonical repo 指定为 `wp5rrp7b2v-droid/black-lady-animatic-v01`。
- 本次 Project Control 建立属于项目管理落档，不占用新的 Codex D-###。

## Project Control Structure 1.1｜2026-09-12

- `docs/project_control/` 从平铺结构重构为 `core/`、`logs/`、`gates/`、`dashboard/`、`archive/`。
- `source_material/` 从 Project Control 中独立出来，用于正式源数据。
- 仓库已确认处于 Private 状态。
- 本次属于项目控制结构维护，不占用 Codex D-###。

## P0.1-04｜S1 Full Novel Lock｜COMPLETE / 2026-09-12

- Product Owner 指定当前上传的完整《诡舍》原文为唯一 S1 canonical source。
- 正式文件名：`S1_SOURCE_NOVEL_FULL_V001.txt`。
- 文件规格：UTF-8 plain text、BOM none、LF、6,480,028 bytes、2,289,031 characters。
- 章节标题范围：第1章至第1002章《新世界（结局）》；检测到 1001 个章节标题。
- SHA-256：`f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e`。
- 源文件未检测到 `第461章` 标题；登记为 `SOURCE-NATIVE NUMBERING ANOMALY`，保持正文原样，不补写、不重编号。
- P0.1 当前推进至 P0.1-05：原始有声小说音频实体登记与 S3 转写/校验体系建立。

## AM Checkpoint｜2026-09-12｜PAUSED / RESUME AFTERNOON

上午阶段工作已完成并在此收口，下午从 P0.1-05 继续，不回退重做已完成步骤。

### 1. Project Control / Repo

- `docs/project_control/` 已完成 Structure 1.1 重构：`core/`、`logs/`、`gates/`、`dashboard/`、`archive/`。
- 正式源数据与 Project Control 分离，进入仓库根目录 `source_material/`。
- canonical repo：`wp5rrp7b2v-droid/black-lady-animatic-v01`，Private。
- 本地正式工作目录：`/Users/caroline/诡舍/黑衣夫人/black_lady_short_01`。
- 本地目录已完成迁移并重新与远程 `main` 对齐。

### 2. Local Git cleanup / network handling

- 仓库级 `.gitignore` 已加入 `.DS_Store`，避免 macOS 元数据污染版本库。
- 本地 commit 已正常 rebase 到远程最新 Project Control 基线并 push。
- GitHub HTTPS 链路曾出现 443 timeout / `Empty reply from server` / `unexpected disconnect while reading sideband packet`。
- 当前仓库使用 `HTTP/1.1`；为提高上传稳定性，将 `http.postBuffer` 调整为 `16777216`（16 MiB）。
- 最终 S1 push 成功；本轮网络问题不再作为当前 blocker。

### 3. S1 canonical source

- `S1_SOURCE_NOVEL_FULL_V001.txt` 已完成 canonical lock。
- 本地与 GitHub `main` 正式路径：`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`。
- GitHub 远程文件大小核验：6,480,028 bytes。
- GitHub blob SHA：`f089b5d63ded4be6f90af0ad845f6fdaa4959b84`。
- S1 正文已真正进入远程仓库，不再只是元数据登记。
- P0.1-04：COMPLETE。

### 4. Source baseline at checkpoint

- S1：CANONICAL / LOCKED / REMOTE VERIFIED。
- S2：CANONICAL / LOCKED。
- S3：NOT ESTABLISHED。
- 原始有声小说音频：已知存在，但 canonical 文件名、路径、格式、时长、SHA-256 尚未登记。
- D-056 `SOURCE_AUDIO_INDEX_V001`：仅作为导航索引，不作为正式剪辑时间边界。

### 5. Gate / blocker / hold

- P0.1：ACTIVE / BUILDING。
- P0.2：QUEUED。
- P0.3：QUEUED。
- Overall Gate Progress：0 / 3 PASS。
- 当前 blocker：NONE。
- A08_REBOOT：继续 HOLD。
- 新 Codex D-###：NONE；如后续需要工程执行，下一编号仍为 D-057。

### 6. Resume point

下午唯一恢复点：

`P0.1-05｜登记原始有声小说音频实体，并建立 S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001 的结构、验证等级与小样校验方法。`

恢复顺序：

1. 盘点《黑衣夫人》原始有声小说音频文件；
2. 锁定 canonical 音频实体：文件名、格式、时长、SHA-256、存储路径；
3. 选取一小段真实音频；
4. 建立 S3 数据结构；
5. 对小样进行真实音频逐段校验；
6. 再判断 P0.1 是否达到 PASS 条件。

## PM Scope Lock｜2026-09-12｜MVP1 Start = S2 Chapter 134

- Product Owner 明确：第一个 MVP 的正式故事起点从 S2 第134章《【黑衣夫人】参观》开始。
- 第133章不进入 MVP1 正式成片，只保留为前置语境。
- 因此 P0.1-05 不再以“准备完整《黑衣夫人》全部有声书”为前提，而改为先建立服务 MVP1 的原音获取、准备、登记、转写与校验能力。
- 历史 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 经核验为 2,636,183 bytes、195.844989 sec、AAC 2ch 44.1kHz，SHA-256=`abaaab1c0c8362e6d61268ba09b0f0ce6cb915cf49c046fd3b32c49405746551`；Product Owner 确认其仅为测试片段。
- 上述音频正式降级为 `NON-CANONICAL TEST AUDIO`，不得作为 MVP1 canonical audio baseline。

## PM Audio Capture Verification｜2026-09-12｜MVP1 crosses into Chapter 135

- Product Owner 提供新的正式候选录屏：`ScreenRecording_09-12-2026 13-40-39_1.MP4`。
- RAW_CAPTURE 规格：235,987,834 bytes；381.958333 sec；视频 H.264 1284×2778 / 60fps；音频 AAC 2ch / 44.1kHz；SHA-256=`9bab514775f0771987b094cdd9394b81d6a49a7bace995ef9ad4dbcce448abd1`。
- 录屏画面确认对应有声小说 `097【黑衣夫人】主人`。
- 录屏开头显示“欢迎各位来到艾伦古堡”等内容，与 S2 第134章开头一致。
- 对照录屏画面与 S2：约在有声小说播放器 05:05–05:10 左右，内容已由第134章进入第135章开头；后续出现黑裙、黑色高跟鞋、红色指甲油、莫妮卡夫人入座等第135章早段内容。
- 录屏末段约播放器 06:20，已经到莫妮卡夫人入座、众人开始跟随入座附近。因此 MVP1 的实际内容跨度不是“第134章 only”。
- 已从 RAW_CAPTURE 中以 stream copy 方式无重编码提取原 AAC 音轨：`AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`。
- RAW_AUDIO_EXTRACT 规格：5,244,616 bytes；381.941995 sec；AAC 2ch / 44.1kHz；SHA-256=`d9a297b275a2fc42b85fa7b26407c4824c17efc63d1b9d148470f224d96be7f2`。
- 当前状态：`RAW_AUDIO_EXTRACT / CANONICAL CANDIDATE`。由于录屏本身可能含极短的起止操作冗余，尚未直接晋级为 `CANONICAL_AUDIO`。
- 正式范围规则修正：MVP1 从 S2 第134章开头起，终点按真实有声小说连续音频边界锁定；原文章节只作为内容映射锚点。当前映射终点在 S2 第135章开头。
- 下一步：锁定 canonical audio 的精确起止内容与时间码，再建立覆盖该完整音频跨度的 S3。

## P0.1 Final Closeout｜2026-09-12｜PASS / PRODUCT OWNER APPROVED

- `AUDIO_MVP1_CANONICAL_V001.m4a` 完成正式边界锁定；起点完整保留“欢迎各位来到艾伦古堡”，终点完整保留“而后又匆匆离去备餐”。
- S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv` 建立完整 MVP1 searchable index：41 segments，其中 9 VERIFIED、32 REVIEWED searchable entries。
- 开头 / 中段 / 后段检索抽查均可唯一命中正确候选原音区域。
- Product Owner 明确批准 P0.1 正式 PASS；精确 shot-driven audio retrieval / extraction 转入 P0.3。

## P0.2 Character Asset System Build｜2026-09-13

### D-059｜Character Asset Migration V1

Status: `COMPLETE / REMOTE VERIFIED`

- 48 张 approved Character PNG 迁入 `production/image_library/character_references/`。
- CSV + JSON Migration Manifest 发布到 `docs/project_control/gates/P0_2_visual_assets/migration_evidence/`。
- Remote commit: `d9fb763fb63e57023aa2cf11119c9be1bef037d6`。
- Neil `rear_turn_45` legacy asset 保持 `MAPPING_REQUIRED / NOT MIGRATED`。

### D-060｜Reference Package Exporter V0.1

Status: `TEST APPROVED / PRODUCT OWNER APPROVED`

- 测试对象：`CHAR_NING_QIUSHUI → PROFILE_LEFT`。
- 自动选出 `FACE_FRONT / PROFILE_RIGHT / FACE_3Q_RIGHT / BODY_FRONT`。
- 4/4 SHA source/copy/manifest PASS；正确识别目标 `PROFILE_LEFT = REFERENCE_GAP`。
- 验证结论：`Canonical Character Assets → automatic selection → local Reference Package` 成立。
- Approval record commit: `7142ddf9c82c63f0a479f56d57de9e2996b540de`。

### Automatic Ingest Controller V0.1｜First Live Ingest

- Automatic Ingest Controller 与 Runtime Registry 建立并投入真实 Character asset ingest。
- 首个真实资产：`CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`。
- Asset ID：`AST_IMG_000049`；首次 ingest commit：`65e7fbec9acbe970797479ae523abf9f9e4f55df`。
- Registry 写入 `APPROVED / CURRENT / AUXILIARY / DEFAULT`；Audit 写入 `ASSET_APPROVED + ASSET_INGESTED`。
- 后续发现该 V001 画幅不符合项目 9:16 Character reference 标准，因此保留历史记录但不作为最终现行版本。

### D-061｜One-click Character Ingest + Cleanup

Status: `COMPLETE / REMOTE VERIFIED`

- 提供 `Black_Lady_Ingest.command` 一键入口；Product Owner 确认后选择 canonical PNG，即可调用 controller 完成正式 ingest。
- 加入 Reference Package cleanup、staging safety、dry-run/network boundary 等保护。
- Commit: `200cb06ce366c650b4f1389108765996b8f15332`。

### D-062｜P1 Character Reference Package Generalization

Status: `COMPLETE / REMOTE VERIFIED`

- Exporter 泛化至 P1 `PROFILE_LEFT / PROFILE_RIGHT / REAR_3Q_LEFT / REAR_3Q_RIGHT`。
- opposite-side 仅作为 reference selection，不允许 silent mirror inference。
- Commit: `a480dc0a64b2e63221122dce238d5c35634a77b1`。

### D-063｜Unified Migration + Runtime Character Asset Resolution

Status: `COMPLETE / REMOTE VERIFIED`

- Migration Manifest 与 Runtime Registry 统一进入 Character current/reference resolution。
- Runtime 新资产可立即参与 Current detection / reference selection。
- Exact duplicate 跨源时仅同 filename/version/SHA 允许 runtime wins；不同 Current 仍视为冲突。
- Commit: `e85f749ef72fb722c631472eb0af8bb2b0b7bc7e`。

### D-064｜Controlled Current Supersession

Status: `COMPLETE / REMOTE VERIFIED`

- 新增受控 CURRENT 替换能力；必须同时显式满足 `--supersede-current` 与 `--po-approved`。
- 正常 ingest 发现已有 CURRENT 仍默认 BLOCK。
- Supersession 写入 Registry lifecycle 更新、`NEW SUPERSEDES OLD` Relation、Audit `ASSET_SUPERSEDED`，旧文件保留。
- Commit: `6735c44374713d7470888dfb4d20e52af804cb42`。

### Ning PROFILE_LEFT V002｜Real Controlled Supersession

- GitHub HTTPS 初次运行出现 `Empty reply from server`；进一步测试发现默认 HTTP/2 链路报 `curl: (16) Error in the HTTP2 framing layer`。
- 对该仓库切换 Git HTTP/1.1 后链路恢复；网络问题不再作为 blocker。
- `CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png` 正式 ingest：`AST_IMG_000050`。
- V002 设为 CURRENT；V001 `AST_IMG_000049` 转为 SUPERSEDED。
- Supersession commit: `eba06283cccd10a22addd02307c9012cc06d3ac0`。

### D-065｜macOS Bash Launcher Fix

Status: `COMPLETE / REMOTE VERIFIED`

- 真实普通新增路径暴露 macOS Bash 3.2 + `set -u` + empty array expansion：`supersede_args[@]: unbound variable`。
- 修复方式：保留 `set -u`，拆分 CURRENT_FOUND supersede 与 NO_CURRENT normal ingest 两条明确 controller 调用路径。
- macOS `/bin/bash` NO_CURRENT / SUPERSEDE runtime 均 PASS；controller regression 10 项 PASS。
- Commit: `57495a7b0a9e189098e2b8310e76d98f7b0beb2d`。
- 全量 39 项测试存在 1 项既有 Resolver assertion failure：测试仍期待旧 `AST_IMG_000049`，而合法 supersession 后 CURRENT 已为 `AST_IMG_000050`；该问题登记为 non-blocking stale test expectation。

### Ning REAR_3Q_LEFT V001｜Real Normal Ingest

- `CHAR_NING_QIUSHUI_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png` 正式 ingest 成功。
- Asset ID：`AST_IMG_000051`。
- 状态：`APPROVED / CURRENT / AUXILIARY / DEFAULT`。
- Audit：`ASSET_APPROVED + ASSET_INGESTED`。
- Commit: `a90854dee5f2cef736b622650a2120b22bc8279e`。

## P0.2-03｜P1 Wave 1 Closeout｜2026-09-13

Status: `COMPLETE / CONTINUE P1`

- 宁秋水 `PROFILE_LEFT`：COMPLETE；CURRENT = `AST_IMG_000050 / V002`。
- 宁秋水 `REAR_3Q_LEFT`：COMPLETE；CURRENT = `AST_IMG_000051 / V001`。
- Live Core Coverage：`42 / 63 = 66.7%`。
- Remaining Core View Gap：`21`。
- P1 progress：`2 / 10 complete`，`8 / 10 remaining`。
- 宁秋水 Tier A current coverage：`8 / 9`；剩余 `FACE_3Q_LEFT` 属于非当前 P1 target。
- 下一正式 P1 target：`CHAR_JUN_LUYUAN PROFILE_LEFT`，随后 `REAR_3Q_LEFT`。

## End-of-Day Engineering State｜2026-09-13

- P0.1：PASS / PRODUCT OWNER APPROVED。
- P0.2：ACTIVE / P1 CHARACTER GAP PRODUCTION。
- P0.3：QUEUED。
- 当前 Codex 工程编号已到 D-065；下一新的工程任务编号从 D-066 继续。
- Current blocker：NONE。
- 非阻塞技术债：Resolver regression test 仍写死旧 Asset ID；后续应改为断言当前有效版本语义。

## D-066｜AO-01 Four Registers Final Reconciliation｜2026-09-14

Status: `COMPLETE / PENDING_REMOTE_PUBLICATION`

- Four named legacy CSVs unavailable in current worktree, untracked files, and reachable Git history; no reconstruction. Baseline evidence commit `0bdb5798f4cd8c9ce82d4c9d9ae65d5a9503d67c` published to origin/main after an initial network failure.
- BL-D-028 locks all four out of Current authority; old-row orphan/duplicate/path/naming checks remain `UNKNOWN / SOURCE UNAVAILABLE`.
- Available 48 D-059 canonical PNGs and 3 Runtime PNGs verified; 39 tests pass; no duplicate Current. Current Shot Spec validation remains AO-06.
- Project Control cross-file closeout recorded; updated evidence publication and HEAD/origin-main verification still required. AO-02 not started; P1 Wave 2 HOLD.

### D-066｜AO-01 remote verification

- Product Owner decision and pending closeout commit `43d8fa4f8e4068298058f1aad0bc410193b6c0d3` pushed; fresh fetch confirmed `HEAD == origin/main`.
- AO-01 updated to `COMPLETE / VERIFIED` in Project Control revision R032. AO-02 remains NEXT / NOT STARTED; P1 Wave 2 HOLD.

## AO-02｜Legacy Character Assets → Long-term Registry / Audit｜2026-09-14

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Execution route: `CHAT + TERMINAL / NO CODEX D-NUMBER`

- AO-02 Design V1 was completed and locked in Chat before implementation.
- Dedicated migration controller: `scripts/legacy_registry_migration_controller_v1.py`.
- Automated tests: `tests/test_ao02_legacy_registry_migration.py`.
- Pre-apply dry-run: 48 eligible / 48 migrated planned; Single Current PASS; SHA/storage PASS; one provable SUPERSEDES relation.
- Formal migration backfilled `AST_IMG_000001–000048` for 48 D-059 `CONFIRMED + APPROVED` legacy Character assets.
- Existing Runtime `AST_IMG_000049–000051` preserved unchanged.
- Neil `CHAR_NEIL_REAR_TURN_45_SUPPLEMENTARY` remained `MAPPING_REQUIRED / NOT MIGRATED`。
- Post-migration counts: Asset Registry `51`; Asset Relations `2`; Audit Event Log `56`; migration map `48` rows + header.
- Character PNGs and D-059 CSV/JSON Manifest remained unchanged.
- Automated migration tests: `5/5 PASS` including deterministic mapping, rollback, partial-migration block, idempotency, and eligible-count guard.
- Real second run returned `ALREADY_APPLIED / NO CHANGE`.
- Migration commit: `4803b928baaa38d875e9c6edd46f4a458e627b61`.
- Terminal publication check: `FINAL_STATUS=REMOTE_VERIFIED`; GitHub main independently confirmed the same commit.
- Completion evidence: `docs/project_control/gates/P0_2_visual_assets/ao02_legacy_asset_registry_migration_v1.md`.
- Product Owner explicitly approved AO-02 on 2026-09-14.
- Project Control advanced to revision `R033`; AO-03 is NEXT; P1 Wave 2 remains HOLD.

AO-02 does not consume D-067. Per RC-015, only work actually executed by Codex consumes a D-### number.

## AO-07｜GitHub Network Resilience / Recovery Method｜2026-09-14

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Execution route: `CHAT + TERMINAL EVIDENCE + GITHUB CLOSEOUT / NO CODEX D-NUMBER`

- Existing dynamic helper `$HOME/.local/bin/git-proxy-auto` validated on the Black Lady repo.
- Real verification chain completed: `ls-remote` PASS → `pull --ff-only` PASS → `push` PASS → local HEAD / remote main SHA MATCH.
- HTTP/1.1 retained as safe fallback; dynamic proxy port is discovered at runtime and not persisted.
- AO-02 migration publication used the same connectivity path and reached `REMOTE_VERIFIED`.
- Real second migration run returned `ALREADY_APPLIED / NO CHANGE`, proving publication retry must not trigger re-ingest or duplicate Asset IDs.
- Formal lightweight Recovery Runbook completed with connectivity preflight and diagnosis order: DNS → HTTPS → remote → HTTP version → proxy/VPN → credential → repo reachability.
- `PENDING_REMOTE_PUBLICATION` entry/exit/recovery rules locked.
- Push ACK loss and remote mismatch handling locked; force push is prohibited for recovery.
- Controlled failure→recovery requirement satisfied by real transient incidents (`443 timeout`, `Empty reply from server`, HTTP/2 framing error, unexpected disconnect) followed by verified recovery/publication.
- Product Owner explicitly approved AO-07 on 2026-09-14.
- Decision: `BL-D-030`。
- Completion evidence: `docs/project_control/gates/P0_2_visual_assets/ao07_github_network_resilience_progress_v1.md`。
- `RISK-001` downgraded from OPEN to `CONTROLLED / MITIGATION VERIFIED`。
- Project Control advanced to revision `R034`; AO-03 remains NEXT; P1 Wave 2 is now blocked only by AO-03～AO-06。

AO-07 does not consume D-067. Per RC-015, only work actually executed by Codex consumes a D-### number.

## AO-03A｜Fact Boundary + Executable Spec Design V0.1｜2026-09-15

Status: `APPROVED / PRODUCT OWNER APPROVED`

Execution route: `CHAT DESIGN + GITHUB CLOSEOUT / NO CODEX D-NUMBER`

- Product Owner explicitly approved AO-03A on 2026-09-15; decision `BL-D-032`。
- Stable Scene identity locked as `SCENE_CASTLE_ENTRANCE` and `SCENE_FIRST_HALL`。
- Legacy/source aliases retained for traceability: `CASTLE_ENTRANCE_OPEN_DOOR_DAY` and `FIRST_HALL_FIREPLACE`。
- Controlled State dimensions include DAY/NIGHT, door OPEN/CLOSED and fireplace EXTINGUISHED/BURNING; State change does not create a new Scene identity。
- Scene Master locks Scene Facts, not Shot Photography; camera / shot size / focal length / blocking / occlusion / depth of field / local exposure / composition remain shot-variable。
- Costume / Prop executable model follows Entity / Asset / Variant / State; missing required eligible formal asset remains `REFERENCE_GAP`, not fabricated completion。
- AO-03 requires Runtime / Resolver + machine-verifiable tests; documentation-only closeout is prohibited。
- Formal design evidence: `docs/project_control/gates/P0_2_visual_assets/ao03_scene_executable_spec_design_v0_1.md`。
- 本节为历史设计阶段记录；AO-03 最终完成状态见 2026-09-17 Closeout。

## CLOUD-DRILL-001｜Codex Cloud native PR workflow｜2026-09-15

Status: `PASS / REMOTE VERIFIED / PR MERGED`

Execution route: `OPERATIONS WORKFLOW DRILL / NO D-NUMBER`

- Purpose: verify the temporary no-Mac path without touching Project Control, production, AO-03 engineering, scripts/tests or workflows.
- Canonical source baseline at drill start: `a6db067927e26d19d5566d64fe04d3cb72a24961`。
- A first shell-level direct `git fetch/push` path failed because the Cloud shell had no GitHub credential; this was treated as diagnostic evidence, not as proof that native Cloud publication was unavailable.
- Cloud checkout retained a drill-only commit/work reference; preflight confirmed exactly one committed file: `docs/drills/CODEX_CLOUD_BRANCH_PR_DRILL_2026-09-15.md`。
- Codex Cloud native PR / `make_pr` request was accepted; although the task UI did not return PR number/URL, independent GitHub remote verification found actual PR `#5`。
- Actual PR head: `codex/-codex-cloud-pr`; base: `main`。
- PR scope audit: exactly one changed file, 12 additions, 0 deletions; no Project Control / production / AO-03 change.
- Traceability text was corrected before merge so drill metadata matched the actual PR head and remote publication outcome.
- Product Owner approved merge after independent review.
- Merge SHA: `774a6abed34b81e5558dbfeba3846380fb1ff26e`。
- Completion evidence: `docs/project_control/gates/P0_2_visual_assets/cloud_pr_workflow_drill_2026-09-15.md`。
- Resulting rule supplement: `RC-019` — Codex Cloud native PR publication is the verified remote publication path for TEMP_CLOUD_ONLY_MODE; shell-level direct push credential is not a baseline requirement.

## End-of-Day Project Control Closeout｜2026-09-15

- `project_state.json` advanced to `R036`。
- P0.2 remains `ACTIVE / APPROVED-OPEN CLOSEOUT BEFORE P1 WAVE 2`。
- AO-03 historical state at this checkpoint = `IN PROGRESS / AO-03A+B APPROVED / ENGINEERING IMPLEMENTATION`。
- AO-04 / AO-05 / AO-06 remained pending; P1 Wave 2 remained HOLD。
- `TEMP_CLOUD_ONLY_MODE_V1` was approved but pre-effective on 2026-09-15; it became effective at 2026-09-16 00:00。
- Codex Cloud native PR publication was verified for the 09/16–09/20 cloud-only window。
- Current blocker at that checkpoint: NONE。
- Current live Character coverage remained `42 / 63 = 66.7%`; P1 remained `2 / 10`。
- D-### baseline at that checkpoint: last actual Codex engineering task `D-066`; next formal Codex engineering task when needed = `D-067`。
- Historical next step at that checkpoint: `AO-03B｜Two Scene Master Structured Facts Definition`。


## D-069｜A04 Binary Delivery Deferral｜2026-09-19

Status: `DEFERRED BY PRODUCT OWNER / RESUME SAME D-069`

- Product Owner chose to pause the A04 binary-delivery step until GitHub/local access is available.
- Source attachment `A04_REBOOT_approved_v001.png` was successfully read in Work as the original PNG bytes: 2,486,659 bytes, 941 × 1672.
- Computed SHA-256 matched the expected approved identity exactly: `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`.
- Transport branch `work/d069-a04-binary-intake` exists remotely, but no A04 staging binary has been committed; branch still points at the current main baseline.
- Multiple Work attempts to encode/upload the 2.49 MB PNG were interrupted by streaming failures before the GitHub commit completed.
- No Asset Registry, Entity Registry, Asset Relations, Audit Event Log, Shot Spec, Costume Asset, Prop Asset, or live USES_REFERENCE mutation occurred.
- Do not retry the Work direct-upload loop for now.
- Resume gate: when access is available, deliver the byte-exact original to `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`, re-read from GitHub, verify the same SHA-256, then resume the same D-069 formalization path.
- AO-06 remains IN PROGRESS.
- D-070 remains NOT ALLOCATED.


## D-069｜A04 Binary Deferral Scope Correction｜2026-09-19

Status: `D-069 ACTIVE / ONLY A04 BINARY SUBSTEP DEFERRED UNTIL MACBOOK ACCESS`

- Product Owner clarified the previous deferral scope.
- The deferred item is only retrieval of the formal `A04_REBOOT_approved_v001.png` from the MacBook and its byte-exact delivery/formalization path.
- This is **not** a GitHub-access deferral and **not** a pause of the whole D-069.
- GitHub Web/App, ChatGPT, Codex Cloud, Project Control work, model review, resolver/package engineering, cross-checks, and any other work that does not require the local A04 binary may continue normally.
- When MacBook access returns, retrieve the formal A04 source, verify SHA-256 against `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`, then continue the binary-dependent formalization/real-validation substep.
- D-070 remains NOT ALLOCATED.


## P0.2 P1 Character Production Resume｜2026-09-19

Status: `ACTIVE / PRODUCT OWNER REPRIORITIZATION`

- Product Owner explicitly chose to resume the remaining P1 Character production before AO-06 is fully closed.
- This supersedes only the sequencing HOLD created by BL-D-026 / BL-D-027 / BL-D-031; AO-06 remains mandatory before P0.2 final closeout / READY_FOR_APPROVAL.
- P1 live state at resume: `2 / 10 complete`, Core Coverage `42 / 63 = 66.7%`.
- Remaining P1 targets (8):
  1. `CHAR_JUN_LUYUAN / PROFILE_LEFT`
  2. `CHAR_JUN_LUYUAN / REAR_3Q_LEFT`
  3. `CHAR_NEIL / PROFILE_RIGHT`
  4. `CHAR_NEIL / REAR_3Q_RIGHT`
  5. `CHAR_SU_XIAOXIAO / PROFILE_LEFT`
  6. `CHAR_SU_XIAOXIAO / REAR_3Q_LEFT`
  7. `CHAR_LIAO_JIAN / PROFILE_LEFT`
  8. `CHAR_LIAO_JIAN / REAR_3Q_LEFT`
- Next production target: `CHAR_JUN_LUYUAN PROFILE_LEFT`.
- Existing production rules remain: 9:16 target, Fixed Standard Review, Product Owner approval before formal Registry entry, Automatic Ingest after approval.
- D-069 remains open as a parallel AO-06 closeout track; its byte-exact A04 binary substep waits for MacBook access.
- D-070 remains NOT ALLOCATED.
- P0.3 remains QUEUED / DO NOT START EARLY.


## P1｜Jun Luyuan PROFILE_LEFT Delivery Bundle｜2026-09-19

Status: `READY / WORK GENERATION NEXT`

- Initial Work generation attempt correctly returned `BLOCKED_ON_REQUIRED_REFERENCE_BINARIES`: Registry metadata resolved, but the four required Atomic PNG bodies were empty through the direct Work GitHub file/blob transport path.
- This reproduces the already-known AO-05 transport limitation and does not invalidate the Character Resolver or canonical assets.
- Required exact inputs:
  - `AST_IMG_000017 / FACE_FRONT / V001 / 7bf1f211743fb9f071d427c1404ea04dfd71c3804b5b526c2dca8b258ed4b96f`
  - `AST_IMG_000018 / PROFILE_RIGHT / V001 / 7a04169daed3034ed9d37a508670dce995d2dc2cb75a11148006f9e821321c92`
  - `AST_IMG_000016 / FACE_3Q_RIGHT / V001 / f9ddbb18d4b548bf4887d09d1e0a9eba8be2dde7d61275a8c09a1a5d639f9929`
  - `AST_IMG_000015 / BODY_FRONT / V001 / f9960466266f08d79fde32435f542bd47ed0f8ab26af99bbb2928bd8d3957e92`
- Chat created a temporary GitHub Actions transport workflow:
  `.github/workflows/p1-jun-luyuan-profile-left-delivery-bundle.yml`
- Workflow run `35422665719`: `SUCCESS`.
- Runner log: `PASS: 4/4 exact canonical reference binaries verified`.
- Artifact: `P1_JUN_LUYUAN_PROFILE_LEFT_DELIVERY_BUNDLE_V001`.
- Artifact ID: `10577930931`.
- Artifact size: `11,348,718 bytes`.
- Artifact ZIP digest: `sha256:a4cd646a66f7925089be869178efe255ce1e0612e36633358e883bf86a290075`.
- Source commit: `ebd22de616ebbae5be5b822575020a4fe4892b8c`.
- Expires: `2026-09-26T04:57:51Z`.
- This is a transport artifact only; it is not a formal Asset and causes no Registry / Audit mutation.
- Next: Work automatically downloads the artifact, independently validates manifest + 4 file SHA/bytes, then generates the `PROFILE_LEFT` candidate and performs Fixed Standard Review.
- Product Owner manual reference upload count remains `0`.
- D-070 remains NOT ALLOCATED.


## P1｜Jun Luyuan PROFILE_LEFT V001 Product Owner Approval｜2026-09-19

Status: `PO APPROVED / FORMAL INGEST PENDING`

- Final candidate visually reviewed in main Chat: `PASS`.
- Product Owner explicitly approved the candidate as Jun Luyuan `PROFILE_LEFT V001`.
- Canonical target filename: `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Exact uploaded approved source identity:
  - format: `PNG`
  - dimensions: `941 × 1672`
  - byte size: `1,933,426`
  - SHA-256: `00915474a52a29df753542b916503998c450b056d2ef59d98279841fdc9ad9be`
- Important audit boundary: Work's final report did not include the candidate PNG SHA, so there is no prior candidate SHA against which to cryptographically compare this upload. The current uploaded PNG is therefore locked as the PO-approved source identity for formalization.
- Do not re-encode, resize, screenshot, or substitute this source during formal publication.
- Core Coverage / P1 completion remain unchanged until exact-byte canonical publication + Automatic Ingest + Registry/Audit verification succeeds.
- After ingest: continue `CHAR_JUN_LUYUAN REAR_3Q_LEFT`.
- D-069 remains open in parallel; D-070 remains NOT ALLOCATED.


## P1｜Jun Luyuan PROFILE_LEFT V002 Visual Candidate｜2026-09-19

Status: `V001 APPROVAL WITHDRAWN PRE-INGEST / V002 VISUAL CANDIDATE / FORMAL REVALIDATION PENDING`

- Product Owner re-reviewed V001 before formal ingest and identified the neck as proportionally too long.
- A revised Chat-generated image with a shorter, more natural neck/shoulder relationship was selected as the preferred visual direction.
- V001 had not entered canonical storage/Registry, so its earlier approval is withdrawn without formal supersession.
- Do **not** publish or ingest V001.
- The revised image is designated only as `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002 / VISUAL CANDIDATE`.
- It is not yet a formal Asset because it was generated outside the locked 4-reference Delivery Bundle execution path.
- Formal next step: rerun with the same verified canonical four-reference set; use the V002 candidate only as target appearance/neck-proportion guidance; then Fixed Standard Review → Product Owner final approval → exact-byte publication → Automatic Ingest.
- D-069 remains parallel; D-070 remains NOT ALLOCATED.


## P1｜Jun Luyuan PROFILE_LEFT V002 Work Revalidation Rejected｜2026-09-19

Status: `REJECTED BY PRODUCT OWNER / WRONG IMAGE / RERUN REQUIRED`

- Work successfully revalidated the Delivery Bundle and canonical 4-reference input set.
- Work nevertheless returned the wrong image for the intended V002 target.
- Product Owner explicitly rejected the image.
- Therefore Work's internal `INTERNAL APPROVED FINAL CANDIDATE` label is overridden by Product Owner authority and has no formal effect.
- Reference delivery evidence remains valid; the failure is at target-candidate selection/use or generation-result level.
- Correct visual target to use on rerun: the strict 90° left-profile image selected after V001 neck-length rejection, with shorter neck and more natural shoulder-neck proportion.
- Do not use the earlier REAR_3Q visual direction image as V002 target guidance.
- No ingest / Registry / Audit mutation occurred.


## P1｜Jun Luyuan PROFILE_LEFT V002 Work Rerun Internal Pass｜2026-09-19

Status: `WORK INTERNAL APPROVED FINAL CANDIDATE / MAIN CHAT VISUAL REVIEW PENDING`

- Work rerun explicitly confirmed it used the correct Product Owner-selected short-neck strict 90° left-profile visual target.
- The target candidate was used only as `NON-AUTHORITATIVE VISUAL TARGET GUIDANCE`.
- Identity authority remained the verified four canonical references.
- The previously rejected Work image was not used.
- Work reported PASS for Format, Identity, Role Accuracy, Continuity, Production Utility, Reference Type Purity, Problem Check, and Neck / Shoulder Proportion.
- No ingest / Registry / Audit / Project Control mutation was performed by Work.
- Formal status is still pending main-Chat visual review of the actual image and explicit Product Owner approval.


## P1｜Jun Luyuan PROFILE_LEFT V002 Product Owner Approval｜2026-09-19

Status: `PRODUCT OWNER APPROVED / FORMAL INGEST PENDING`

- Main Chat visually reviewed the actual Work rerun output and passed it.
- Product Owner explicitly approved `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png`.
- Exact approved source:
  - format: PNG
  - dimensions: 941 × 1672
  - byte_size: 1,938,522
  - SHA-256: `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c`
- This exact PNG is now the sole PO-approved source for formalization.
- Next: byte-for-byte canonical publication → remote SHA verification → Automatic Ingest → Registry/Audit verification.
- V001 remains `DO NOT INGEST`.
- No Registry/Audit mutation has occurred yet.


## P1｜Jun Luyuan PROFILE_LEFT V002 Transport Pending / REAR_3Q_LEFT Resume｜2026-09-19

Status: `PROFILE_LEFT V002 PO APPROVED / TRANSPORT-INGEST PENDING / REAR_3Q_LEFT PRODUCTION RESUMED`

- PROFILE_LEFT V002 remains the Product Owner-approved visual result.
- Exact source identity remains locked: 941×1672 / 1,938,522 bytes / SHA-256 `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c`.
- GitHub binary upload repeatedly remained too slow/unreliable.
- Product Owner approved continuing P1 production without waiting for that transport/ingest.
- Formal P1 progress remains 2/10 until PROFILE_LEFT V002 exact-byte publication + Automatic Ingest completes.
- Next production target: `CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001`.


## P1｜Jun Luyuan REAR_3Q_LEFT V001 Product Owner Approval｜2026-09-19

Status: `PRODUCT OWNER APPROVED / TRANSPORT-INGEST PENDING`

- Main Chat reviewed the actual Work output and passed it.
- Product Owner explicitly approved `CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`.
- Exact approved source:
  - format: PNG
  - dimensions: 941 × 1672
  - byte_size: 1,941,468
  - SHA-256: `97ad38c259274eced5be61035cda4c28df72babe084fc452fbbc927a2a6da21e`
- Geometry review: rear/back dominant; left face exposure approximately 1/4; no PROFILE or front-3Q drift; head/ear/neck/shoulder-back structures usable.
- Jun PROFILE_LEFT V002 and REAR_3Q_LEFT V001 both remain outside formal progress until exact-byte publication + Automatic Ingest succeeds.
- Formal P1 progress remains `2/10`.
- Next production target: `CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001`.


## P1｜Neil PROFILE_RIGHT V001 + REAR_3Q_RIGHT V001 Product Owner Approval｜2026-09-19

Status: `BOTH PRODUCT OWNER APPROVED / TRANSPORT-INGEST PENDING`

- `CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`
  - PNG / 941×1672 / 1,693,697 bytes
  - SHA-256: `17dff7f50b7392915db6d74f1d04b506f2de884e9069ba11f9013bbe2fce8262`
- `CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
  - PNG / 941×1672 / 1,656,490 bytes
  - SHA-256: `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6`
- Both passed main-Chat visual review and explicit Product Owner approval.
- Both remain outside formal Registry/Core Coverage/P1 progress until exact-byte publication + Automatic Ingest succeeds.
- Jun Luyuan PROFILE_LEFT V002 and REAR_3Q_LEFT V001 remain in the same transport-ingest-pending state.
- Formal P1 progress therefore remains `2/10`.
- Next production target: `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001`.


## P1｜Su Xiaoxiao PROFILE_LEFT V001 Delivery Workflow｜2026-09-19

Status: `WORKFLOW CREATED / ARTIFACT BUILD PENDING`

- Target: `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Dedicated workflow created: `.github/workflows/p1-su-xiaoxiao-profile-left-delivery-bundle.yml`.
- Source commit: `bcfe78f973f6221845ffbc80affb2cd99b5a09e6`.
- Canonical atomic set:
  - AST_IMG_000044 — FACE_FRONT / V001
  - AST_IMG_000043 — FACE_3Q_LEFT / V001
  - AST_IMG_000042 — BODY_FRONT / V001
  - AST_IMG_000041 — BODY_BACK / V001
- Su Xiaoxiao has no authoritative profile view. FACE_FRONT + FACE_3Q_LEFT are therefore the primary facial authorities; BODY_FRONT/BODY_BACK support body, neck and hair continuity.
- Next: successful artifact build → 4/4 exact-byte verification → Work generation → main-Chat review → Product Owner approval.


## Daily Closeout Cross-Check｜2026-09-19

Status: `COMPLETE / CROSS-CHECKED / EOD PAUSED`

Cross-checked and synchronized:

- `core/project_state.json`
- `core/acceptance_matrix.md`
- `gates/P0_2_visual_assets/README.md`
- `gates/P0_2_visual_assets/character_gap_live_progress_v1.md`
- `gates/P0_2_visual_assets/approved_open_tasks_v1.md`
- `logs/decision_log.md`
- `logs/execution_log.md`
- `logs/rules_change_log.md`
- `logs/risk_register.md`
- Dashboard
- four approved Jun/Neil canonical target paths on GitHub main

No new project-wide rule was added beyond existing RC-020. Risk Register statuses remain unchanged. Four approved PNGs are still not present at canonical GitHub paths; therefore no formal progress increment is recorded.

Resume point: Su Xiaoxiao PROFILE_LEFT delivery artifact verification / formal generation; exact-byte ingest of four approved Jun/Neil views when transport is stable; AO-06/D-069 remains parallel final-closeout work. D-070 remains NOT ALLOCATED.


## P1｜Su Xiaoxiao PROFILE_LEFT V001 Product Owner Approval｜2026-09-20

Status: `PRODUCT OWNER APPROVED / TRANSPORT-INGEST PENDING`

- Work generation used verified canonical reference delivery.
- Artifact ID: `10584448292`.
- Artifact actual SHA-256: `583294d5ac2acca71278a8d5cc02c1a628560623cdf9ec4fb2691604f06d42a0` / MATCH.
- Canonical references: AST_IMG_000044 FACE_FRONT, AST_IMG_000043 FACE_3Q_LEFT, AST_IMG_000042 BODY_FRONT, AST_IMG_000041 BODY_BACK; 4/4 MATCH.
- Main Chat Fixed Standard Review: PASS.
- Product Owner explicitly approved `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Exact approved source:
  - format: PNG
  - dimensions: 941 × 1672
  - byte_size: 2,088,722
  - SHA-256: `3af763a5d96d043ccce061459b16af93114e0bcf59d44a98c9df17130c97868c`
- No ingest / Registry / Audit / Core Coverage mutation has occurred.
- Formal P1 progress remains `2/10`.
- Next production target: `CHAR_SU_XIAOXIAO_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001`.
- Dedicated delivery workflow created at commit `2dcf38869f684add4a1424b1b60b6438229628a7`.


## Daily Closeout Cross-Check｜2026-09-20

Status: `COMPLETE / CROSS-CHECKED / EOD PAUSED / R070`

- P1 visual production = `10/10 PO APPROVED`; formal P1 remains `2/10`.
- P2 generated = `7/7`; explicit PO approvals = `6/7`.
- Castle Young Master `REAR_3Q_LEFT V001` = `PO REVIEW PENDING / DO NOT INGEST`.
- Total PO-approved Core-view binaries awaiting formal publication + ingest = `14`.
- Formal Core Coverage remains `42/63 = 66.7%`.
- No new Asset ID was allocated; Asset Registry / Audit were not mutated by visual approval alone.
- P3 Black Lady 6-view lateral rebuild remains NOT STARTED.
- AO-06 / D-069 remains open and mandatory before P0.2 final closeout.
- D-070 remains NOT ALLOCATED.
- TEMP_CLOUD_ONLY_MODE_V1 reaches its pre-approved time-box end at 2026-09-20 EOD; next local formal production requires GitHub→Local truth sync.
- Updated: project_state R070, acceptance matrix, P0.2 README/live progress/approved-open tasks, decision log BL-D-049..057, execution log, Dashboard V046, daily closeout.
- Reviewed unchanged: rules_change_log (no new rule); risk_register (RISK-001 CONTROLLED, RISK-002 ACCEPTED/NON-BLOCKING).

Resume: Castle Rear-3Q PO decision → exact-byte publication / remote SHA / Automatic Ingest for approved views → formal coverage refresh → GitHub→Local truth sync → AO-06/D-069 separate closeout.


## 2026-09-22｜D-070 Published Binary Adoption｜Rescue Publication

- Source baseline: `3d3aebba8ca458dcdb133c77e3611f037f2fc49a / R071`.
- Original Codex Cloud result was complete but not remotely published; rescue branch created directly on GitHub.
- Added fail-closed `--adopt-existing` controller mode and focused version-reservation safety.
- Formally admitted 21 previously published PO-approved Character Core binaries as `AST_IMG_000063–AST_IMG_000083`.
- Registry count advanced `62 → 83`.
- Audit count advanced `78 → 120`; D-070 contributes exactly 42 events.
- Formal Character Core Coverage advanced `42/63 → 63/63`; Single Current `63/63 PASS`.
- D-070 relation count = `0`; no existing CURRENT slot was replaced.
- Published PNGs were not changed by the rescue transaction.
- Existing Derived Reference Sheet PNGs remain unchanged; builder expected live coverage updated to complete Tier distribution.
- AO-06 / D-069 remains OPEN and mandatory before P0.2 final approval. P0.3 remains QUEUED.


## 2026-09-22｜D-070 PR #11 Formal Review

- PR #11 underwent code, Registry/Audit, binary-integrity and Project Control consistency review.
- Review Patch fixed post-commit invariant rollback ordering, scoped version reservation to adopt-existing only, and corrected rescue audit provenance/time semantics.
- First temporary validation run exposed a normal-supersession regression in the reservation logic; the regression was fixed before approval.
- Final GitHub Actions validation run `35678375411` passed:
  - targeted tests `15/15`;
  - full regression `86/86`;
  - all 21 D-070 canonical PNG SHA/byte/path checks;
  - Registry/Audit/Relations `83/120/44`;
  - D-070 `21 assets / 42 events / 0 relations`;
  - mandatory Character Core Single Current `63/63`;
  - Derived Reference Sheet live-coverage contract;
  - Project Control JSON and diff hygiene.
- Temporary review workflow removed after PASS; final PR changed-file scope = `13`, with no PNG, `production/audio/`, or ZIP change.
- Review conclusion: `PASS / READY_FOR_PRODUCT_OWNER_MERGE_APPROVAL`.
- Required merge method: `SQUASH` so rescue/review intermediate commits do not enter canonical main history.
- P0.2 remains ACTIVE; AO-06 / D-069 remains OPEN; P0.3 remains QUEUED.


## 2026-09-22｜D-070 PR #11 Merge Closeout

- Product Owner explicitly approved merge.
- PR #11 transitioned from Draft to Ready for Review and was squash-merged.
- Merge SHA: `6dc3171bba701c22a97580eadc06f62f391b5fe1`.
- Post-merge GitHub remote verification passed:
  - Registry `83`;
  - Audit `120`;
  - Relations `44`;
  - D-070 `21 assets / 42 events / 0 relations`;
  - Character Core `63/63`;
  - mandatory Single Current `63/63 PASS`;
  - AO-06 / D-069 still OPEN.
- Project Control advanced to R073 to remove the pre-merge waiting state and set AO-06 / D-069 as the current task.
