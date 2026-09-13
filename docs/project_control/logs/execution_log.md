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

- P0.1：ACTIVE / BUILDING
- P0.2：QUEUED
- P0.3：QUEUED
- 新 Codex D-###：NONE

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
- 正式范围规则修正：MVP1 从 S2 第134章开头起，终点按真实有声小说连续音频边界锁定；原文章节只作为映射锚点。当前映射终点在 S2 第135章开头。
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
