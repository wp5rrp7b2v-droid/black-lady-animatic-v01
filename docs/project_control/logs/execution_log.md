# Execution Log｜BLACK-LADY-001

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
