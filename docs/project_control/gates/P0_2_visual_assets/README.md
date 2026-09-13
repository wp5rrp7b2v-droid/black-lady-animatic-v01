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
- Entity-bound / Shot-bound filename 均包含 Role + Variant + State + Version，状态词不进入 filename；
- 9 名正式角色 Tier Assignment V1 已由 Product Owner 于 2026-09-13 批准锁定；
- Character Asset Gap Mapping V1 已完成实图核对并落档；
- Gap Priority Classification / P1 Execution V1 已落档；
- Character Atomic / Auxiliary production reference 目标画幅锁定为 9:16 竖版；Fixed Standard Review 以 Format Compliance 作为第一道硬检查；
- 图片生成后由 Product Owner 发送 `【审核】` 触发固定标准审核，不再把普通 Chat 流程描述为“自动审核”；
- D-059 Character Asset Migration V1 已完成并远端验证：48 张 canonical PNG + CSV/JSON Migration Mapping Manifest 已发布到 GitHub；
- D-060 Reference Package Exporter V0.1 已由 Product Owner 批准测试：自动选图 + 本地 Reference Package 生成链路已验证成立；
- D-061～D-063 已将一键 Character ingest、P1 role 泛化、Migration + Runtime asset resolution 接通；
- D-064 已验证受控 Current supersession；
- D-065 已修复 macOS Bash 3.2 普通新增路径兼容问题。

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
- `../../logs/risk_register.md`

## 当前任务

### P0.2-01｜Visual Asset Authority Audit

Authority Mini-Close 已锁定。D-059 已将 48 张 approved Character references 迁入 canonical GitHub storage，并发布 Migration Mapping Manifest。

P0.2 Gate Review 前仍需：

1. 旧 4 份 canonical register 与实际图库实体完成最终工程对账；
2. 两张 Scene Master 的事实字段结构化；
3. 将 Scene / Costume / Prop / Variant 规则落实到可执行 Registry / Spec；
4. 用真实 Shot Spec（至少人物 + 场景 + 关键服装/道具）验证 Reference Resolver 与 Audit reverse-trace。

原先“将 Migration Manifest 接入长期 Asset Registry / Audit Event 实现”和“验证 Character 自动选图”的主要 Character-level 链路已由 D-060～D-065 与真实 ingest 部分完成，不再作为未开始事项描述。

### P0.2-02｜Visual Asset Management System V1 Design

已完成并锁定：

- Character Tier A/B/C/D 规则；
- Asset ID / Naming 基线；
- Authority Mini-Close；
- Entity / Asset Registry Schema V0.3；
- Single Current；
- Asset Relations；
- Provenance Status；
- Resolver Eligibility 计算原则；
- Append-only Audit Event Log 结构；
- Legacy Migration Mapping Manifest；
- Shot-bound / Entity-bound 归属与命名边界；
- Controlled Current Supersession；
- Character image 9:16 Format Compliance；
- Fixed Standard Review 触发与审核顺序。

### P0.2-03｜Character Tier Assignment + Gap Analysis + P1 Production

Tier Assignment 已锁定：

- Tier A：宁秋水 / 君鹭远 / 尼尔 / 黑衣夫人；
- Tier B：温倾雅 / 苏小小 / 廖健 / 古堡小主人；
- Tier C：光勇；
- Tier D：当前 9 名正式角色中无。

Character Asset Gap Mapping V1 实图核对后的正式历史基线：

- Mandatory Core Slots = `63`
- Confirmed Coverage baseline = `40`
- Core View Gap baseline = `23`
- Core Coverage baseline = `63.5%`
- Reference Sheet Gap = `9`（Derived Asset Gap，单独统计）

当前 live production progress：

- Confirmed Core Coverage = `42 / 63`
- Core View Gap = `21`
- Core Coverage = `66.7%`
- P1 completed = `2 / 10`
- P1 remaining = `8 / 10`

宁秋水：

- `PROFILE_LEFT` = COMPLETE / APPROVED / INGESTED / CURRENT `V002 / AST_IMG_000050`
- `REAR_3Q_LEFT` = COMPLETE / APPROVED / INGESTED / CURRENT `V001 / AST_IMG_000051`
- Tier A current Core Coverage = `8 / 9`
- Remaining non-P1 Core Gap = `FACE_3Q_LEFT`

Tier B 四人均锁定 `primary_side = LEFT`。

黑衣夫人旧 `three_quarter_half_body_angle_reference_v001` 因人物 likeness 不足，迁移目标为：`DEPRECATED / resolver NEVER`；历史 approval 事实保留，未作为 Current canonical Character asset 发布。

Gap Priority Classification V1：

- P1 = 10
- P2 = 7
- P3 = 6

P1/P2/P3 仅表示 Character Gap Production Priority，不是项目 Gate / Phase 编号。

### P0.2-04｜Approved-but-Open System Closeout

Status: `NEXT / MANDATORY BEFORE P1 WAVE 2`

Product Owner 于 2026-09-13 明确要求：以下 7 项已经批准/锁定但尚未执行完成的任务必须先补齐；在全部形成 `COMPLETE / VERIFIED` 证据前，不开启 `P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT`。

1. AO-01｜旧 4 份 canonical register 与实际图库最终对账；
2. AO-02｜D-059 的 48 张 legacy Character assets 进入长期 Registry / Audit 模型；
3. AO-03｜两张 Scene Master 事实字段结构化，并落实 Scene / Costume / Prop / State / Variant 可执行 Spec；
4. AO-04｜完成 9 个 Derived Character Reference Sheets 与 dependency / staleness 验证；
5. AO-05｜完成 D-060 后已批准的 Delivery Bridge：Reference Package → 实际制图环境；
6. AO-06｜完成真实 Shot Spec Resolver + Shot-level Audit reverse-trace；
7. AO-07｜建立并验证 GitHub Network Resilience / Recovery Method，解决频繁 GitHub 连接失败时的诊断、fallback、幂等重试、离线安全与恢复发布问题。

详细完成标准与依赖顺序见：`approved_open_tasks_v1.md`。

## Risk Alert｜RISK-001 GitHub Connectivity Instability

Status: `OPEN / HIGH OPERATIONAL RISK / AO-07 MANDATORY`

近期项目已多次出现 GitHub 443 timeout、`Empty reply from server`、HTTP/2 framing error、`unexpected disconnect` 等连接异常。由于 Project Control、Automatic Ingest、Codex Git 操作与正式资产发布都依赖 GitHub，该问题如果只靠临时手工处理，会带来本地已完成但远端未发布、重复 ingest、Asset ID / Registry 重复写入、版本分叉与状态误判风险。

当前已知 HTTP/1.1 能缓解部分问题，但尚不足以视为正式解决方案。

AO-07 必须建立一套可验证恢复方法，使：

`GitHub transient failure ≠ asset corruption / duplicate ingest / project-state divergence`

详细风险登记：`docs/project_control/logs/risk_register.md`。

## D-059｜Character Asset Migration V1

Status: `COMPLETE / REMOTE VERIFIED`

- Remote commit: `d9fb763fb63e57023aa2cf11119c9be1bef037d6`
- Canonical PNG: `48`
- Migration Manifest: `CSV + JSON`
- Character storage root: `production/image_library/character_references/`
- Migration evidence root: `docs/project_control/gates/P0_2_visual_assets/migration_evidence/`
- Neil `CHAR_neil_rear_turn_45_full_body_aux_reference_v001.png`: `MAPPING_REQUIRED / NOT MIGRATED`

## D-060｜Reference Package Exporter V0.1

Status: `TEST APPROVED / PRODUCT OWNER APPROVED`

测试对象：`CHAR_NING_QIUSHUI → PROFILE_LEFT`

验证结果：

- 自动从正式 Character assets 选出 4 张参考图；
- 选择为 `FACE_FRONT / PROFILE_RIGHT / FACE_3Q_RIGHT / BODY_FRONT`；
- canonical source / APPROVED / CONFIRMED / CURRENT 条件全部满足；
- SHA source / copy / manifest = `4/4 PASS`；
- 正确识别目标 `PROFILE_LEFT = REFERENCE_GAP`；
- 无 Duplicate CURRENT 冲突；
- 未修改任何正式源图。

正式结论：

`Canonical Character Assets → automatic selection → local Reference Package`

已经通过真实测试验证。

## D-061～D-065｜Character Production Automation / Ingest Hardening

Status: `COMPLETE / REMOTE VERIFIED`

- D-061｜one-click Character ingest + reference cleanup；commit `200cb06ce366c650b4f1389108765996b8f15332`
- D-062｜P1 target role generalized reference package exporter；commit `a480dc0a64b2e63221122dce238d5c35634a77b1`
- D-063｜Migration Manifest + Runtime Registry unified Character asset resolution；commit `e85f749ef72fb722c631472eb0af8bb2b0b7bc7e`
- D-064｜Controlled Current Supersession；commit `6735c44374713d7470888dfb4d20e52af804cb42`
- D-065｜macOS Bash launcher normal-ingest compatibility fix；commit `57495a7b0a9e189098e2b8310e76d98f7b0beb2d`

真实生产验证：

- `PROFILE_LEFT V001 / AST_IMG_000049` 首次 Automatic Ingest 成功；
- 发现该版本画幅不符合项目 9:16 标准后，使用受控 supersession 将 `PROFILE_LEFT V002 / AST_IMG_000050` 设为 CURRENT，V001 保留为 SUPERSEDED；
- `REAR_3Q_LEFT V001 / AST_IMG_000051` 通过 NORMAL_INGEST 成功入库；
- Registry / Audit Event 均产生真实记录；
- supersession relation 使用 `NEW SUPERSEDES OLD`；
- 旧版本文件保留，不做静默覆盖或删除。

当前仍有一项非阻塞测试技术债：一个既有 Resolver regression assertion 写死 `AST_IMG_000049`，而合法 supersession 后 CURRENT 已为 `AST_IMG_000050`。该测试应后续改为断言当前有效版本语义，不应固定旧 Asset ID。

## 当前执行基线

P1 按人物整组推进：

1. 宁秋水：`PROFILE_LEFT + REAR_3Q_LEFT` = **COMPLETE**
2. 君鹭远：`PROFILE_LEFT + REAR_3Q_LEFT` = **LOCKED NEXT WAVE / BLOCKED BY P0.2-04 CLOSEOUT**
3. 尼尔：`PROFILE_RIGHT + REAR_3Q_RIGHT`
4. 苏小小：`PROFILE_LEFT + REAR_3Q_LEFT`
5. 廖健：`PROFILE_LEFT + REAR_3Q_LEFT`

制图与主流程分离：图片制作对话框负责生成 + 固定标准审核 + 迭代收敛；只有内部审核通过且 Product Owner 明确批准的最终候选进入 Automatic Ingest / canonical registration / GitHub publication。

当前日常 Character 生产链已经验证到：

`Reference Resolver / Package → Generation → 【审核】→ PO Approval → local final PNG → Black_Lady_Ingest.command → Registry / Audit / Git commit / push`

其中 Product Owner 仍需将最终 PNG 下载到 Mac 后触发本地 launcher；真正的 Chat / generation environment → local / GitHub 文件自动桥接尚未实现，因此“零手工下载”的长期目标尚未完全达到。

## 下一步

下一正式任务保持：

`P0.2-04｜Approved-but-Open System Closeout`

必须完成 AO-01～AO-07 并形成验证证据后，才恢复：

`P0.2-03｜P1 Wave 2｜君鹭远 PROFILE_LEFT`

原则：不得因为 P1 补图容易继续推进，就再次绕过已经批准但尚未完成的系统建设任务；同时不得把 GitHub 临时可连接误判为网络风险已经解决。

## Gate Approval

P0.2 条件满足后只能进入：

`READY_FOR_APPROVAL / WAITING_PO_APPROVAL`

必须由 Product Owner 明确审批后才可标记 `PASS`。
