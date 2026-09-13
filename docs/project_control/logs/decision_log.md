# Decision Log｜BLACK-LADY-001

本文件只记录已经由 Product Owner 明确形成正式结论、会影响后续执行的重大决策。讨论过程、备选方案和未批准推测不进入本文件。

| ID | 日期 | 决策 | 状态 / 影响 |
|---|---|---|---|
| BL-D-020 | 2026-09-13 | Product Owner 批准并锁定 P0.2-02 Entity / Asset Registry Schema V0.3。长期模型固定为 Entity Registry、Asset Registry、Asset Relations、Append-only Audit Event Log 四层；另设只服务旧资产迁移的 Migration Mapping Manifest。正式 `asset_class = ATOMIC / DERIVED_REFERENCE / SHOT`；Entity-bound 与 Shot-bound 分离，正式剧情 Shot 无论包含多少 Character 都以 canonical `shot_id` 归属，人物/场景组成由 Shot Register / Shot Spec 表达。Single Current 按 entity/shot + role + variant + state 唯一；Role 按 asset_class 管理并新增 `SHOT_MASTER`；Asset Registry 增加 `provenance_status = COMPLETE / PARTIAL / UNKNOWN`；Resolver eligibility 动态计算，不维护手工 eligibility 布尔值；Derived Reference 上游失效时计算 `DEPENDENCY_STALE`。命名规则升级为 `<ENTITY_ID>_<ROLE>_<VARIANT>_<STATE>_V###` 与 `<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###`；历史 `REBOOT / approved / final / current / lock` 不进入 canonical filename，`A01_REBOOT…A08_REBOOT` 迁移为 `A01…A08`。LEFT / RIGHT 统一采用 screen-facing convention。V0.3 已通过宁秋水、A04 与 Reference Sheet 逻辑真实 Walkthrough；Schema 锁定不等于 P0.2 Gate PASS。 | LOCKED / P0.2-02 REGISTRY SCHEMA V0.3 |
| BL-D-019 | 2026-09-12 | Product Owner 批准 P0.2-02 Character Asset 采用 Tier 分级标准，而不是所有人物统一固定数量：Tier A 核心角色采用 9-view canonical turnaround；Tier B 重要配角采用 6-view Core Set 并固定 primary side；Tier C 普通角色采用 3-view Minimum Set；Tier D 群演/一次性角色不建立完整 Core Set。Tier 由叙事重要性、出场频率、视角复杂度、连续性敏感度与动画需求共同决定；Production Need 可触发升级。所有同类视图必须统一角度定义、背景、光线、机位和人物比例。Atomic Character Assets 与 Derived Character Reference Sheet 分离；正常生产由 Reference Resolver 自动调用 Sheet，并在需要时追加匹配 Atomic View；缺失关键视角时返回 `REFERENCE_GAP`，不得静默使用废弃资产或将镜像推断当成权威事实。 | LOCKED / P0.2-02 CHARACTER ASSET RULE |
| BL-D-018 | 2026-09-12 | Product Owner 批准 P0.2 的视觉资产管理方向：正式体系不再以人工 Library 挑图和手工命名/存储/登记为标准流程。人物、场景、服装、道具统一采用 `Entity → Atomic Master Asset → Derived Reference Sheet → Reference Resolver → Shot Reference Package` 模型；只有 Product Owner 明确批准的视觉结果进入正式 Asset Registry；Approval 与 Lifecycle 分离，正式生命周期为 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED`；Atomic Master 与 Derived Reference 分离并保留 dependency；正常生产目标为 `Shot / Task Spec → Reference Resolver → Reference Package`，随后生成、PO 审批、Automatic Ingest；所有正式资产必须记录来源、审批、版本、替代、依赖和生产调用 Audit Trail。P0.2 必须用现有《黑衣夫人》资产做真实迁移与自动选图验证后，才可进入 `READY_FOR_APPROVAL`。 | LOCKED / P0.2 VISUAL ASSET MANAGEMENT SYSTEM V1 DIRECTION |
| BL-D-017 | 2026-09-12 | Product Owner 明确：以后所有 Gate / Phase 的正式通过、批准或关闭都必须由 Product Owner 本人审批。即使执行层面的验收条件已经满足，ChatGPT / Codex 也只能标记为 `READY_FOR_APPROVAL`，不得自行写成 `PASS / APPROVED / CLOSED`。只有 Product Owner 在 Chat 中给出明确批准后，Project Control 才能正式更新状态并进入下一 Gate / Phase。 | LOCKED / GOVERNANCE APPROVAL RULE |
| BL-D-016 | 2026-09-12 | P0.1 对 S3 的最低完备标准正式锁定：S3 必须覆盖完整 MVP1，并至少具备可机器检索的 `text / speaker / speaker_type / approx source TC / source_text_ref`；P0.1 不要求全量毫秒级精切或全部 VERIFIED。`S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv` 已扩展至 41 个 segment，9 个 VERIFIED、其余 REVIEWED searchable entries；开头 / 中段 / 后段检索抽查均可唯一命中正确候选原音区域。Product Owner 在 2026-09-12 当前 Chat 明确确认 `P0.1 正式 PASS`。精确的 shot-driven 自动检索、提取、handles 与成片边界 QC 转入 P0.3。 | LOCKED / PRODUCT OWNER APPROVED / P0.1 PASS / P0.3 AUDIO INPUT |
| BL-D-015 | 2026-09-12 | Product Owner 明确：正式生产中不由用户人工搜索“需要哪句话”。应在情节、分镜与镜头画面内容确定后，由后续 Audio Alignment 阶段根据 A1 / Shot Plan 自动识别该镜头或叙事 beat 需要的对白/旁白，自动到 S3 + canonical source audio 中检索对应原音，自动定位 source TC、提取带 handles 的 Audio Clip，并写入 Animatic / Edit Timeline。人工只处理低置信度、匹配冲突、边界异常与最终听审，不承担常规查找时间码。S3 的职责因此是可机器检索的 source-audio index，不要求在前置阶段把整条 canonical audio 全量切成成片级精确小段。 | ACTIVE / DOWNSTREAM AUDIO RESOLVER MODEL LOCKED / P0.3 INPUT |
| BL-D-014 | 2026-09-12 | Product Owner 明确：`AUDIO_MVP1_CANONICAL_V001.m4a` 及 S3 仅作为后续动画的原始配音 / 旁白素材来源与可验证定位层，不作为动画节奏母版。正式硬规则锁定为 `SOURCE AUDIO TC ≠ FINAL EDIT TC`。S3 记录 source audio 中实际说了什么、谁说、旁白/对白类型与 source TC；A1 `ADAPTATION_SCRIPT` 决定成片保留/删除/重组内容；`Animatic / Edit Timeline` 决定镜头节奏、镜头时长、停顿、转场及选中原音在成片中的最终摆放位置。不得为了迁就镜头时长改变原音语速。 | ACTIVE / P0.1-05B RULE LOCKED / SOURCE-AUDIO AND EDIT-TIMELINE SEPARATED |
| BL-D-013 | 2026-09-12 | Product Owner 审核并批准 `AUDIO_MVP1_CANONICAL_CANDIDATE_V002.m4a` 的首尾边界：起点完整保留“欢迎各位来到艾伦古堡”，终点完整保留“而后又匆匆离去备餐”。该文件正式晋级并命名为 `AUDIO_MVP1_CANONICAL_V001.m4a`。其来源为 `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`，以 stream copy 方式裁切，不重新编码；源音频起点约 22.800 sec，终点为当前 RAW_AUDIO_EXTRACT 末尾；正式文件 4,957,338 bytes，359.141995 sec，AAC / 44.1kHz / 2ch，SHA-256=`8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`。P0.1-05A 完成；后续 S3 与剪辑定位以该 canonical audio 为 MVP1 最高音频事实源。 | ACTIVE / P0.1-05A COMPLETE / CANONICAL AUDIO LOCKED |
| BL-D-012 | 2026-09-12 | Product Owner 进一步明确 MVP1 的边界规则：MVP1 从 S2 第134章《【黑衣夫人】参观》开头开始，但不以原文章节结尾作为硬边界。由于有声小说的分集/进度与原文章节划分存在差异，本次实际录制内容跨入 S2 第135章开头。MVP1 应定义为“按真实有声小说连续叙事与音频边界锁定的片段”，原文章节仅用于内容映射；正式音频起止时间以 canonical audio 为最终事实依据。 | ACTIVE / CLARIFIES BL-D-011 / MVP1 AUDIO-SPAN MODEL |
| BL-D-011 | 2026-09-12 | Product Owner 正式锁定第一个 MVP 的故事起点：从 S2 第134章《【黑衣夫人】参观》开始；第133章不属于 MVP1 正式成片范围，仅保留为前置语境。MVP1 所需原音频的获取、准备、登记、转写与校验本身属于项目能力建设的一部分，不要求先准备完整《黑衣夫人》全部有声书。现有 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 仅为历史测试片段，降级为 NON-CANONICAL TEST AUDIO，不得作为 MVP1 canonical audio baseline。BL-D-012 对“第134章”进一步澄清为起始锚点而非唯一内容范围。 | ACTIVE / MVP1 START LOCKED / P0.1-05 REFRAMED |
| BL-D-010 | 2026-09-12 | Product Owner 指定当前上传的完整《诡舍》原文为 S1 唯一 canonical source；正式文件名锁定为 `S1_SOURCE_NOVEL_FULL_V001.txt`，格式 UTF-8 plain text，SHA-256=`f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e`。结构检查发现源文件从第460章直接跳至第462章，该现象登记为 `SOURCE-NATIVE NUMBERING ANOMALY`，不得自行补章或重编号。 | ACTIVE / P0.1-04 COMPLETE / S1 LOCKED |
| BL-D-009 | 2026-09-12 | Product Owner 批准将 `docs/project_control/` 从平铺结构重构为 `core/`、`logs/`、`gates/`、`dashboard/`、`archive/`；生产源数据与 Project Control 分离，统一进入仓库根目录 `source_material/`。 | ACTIVE / PROJECT CONTROL STRUCTURE 1.1 |
| BL-D-008 | 2026-09-12 | Product Owner 指定 2026-09-12 当前 Chat 上传的《黑衣夫人》文本为 S2 唯一 canonical source；正式文件名锁定为 `S2_SOURCE_BLACK_LADY_TEXT_V001.txt`，格式为 UTF-8 plain text，正文保持原始字节不改；范围第133–164章，SHA-256=`159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`。其他同名/近似文本降级为 non-canonical reference。 | ACTIVE / P0.1-03 COMPLETE / S2 LOCKED |
| BL-D-006 | 2026-09-11 | Product Owner 批准 Dashboard V002：必须显示 Overall Gate 完成度、当前 Gate 状态、阶段目标和真实 Blocker；项目控制规则区明确命名为 `Project Control Rules`。 | ACTIVE / DASHBOARD V002 APPROVED |
| BL-D-007 | 2026-09-11 | `wp5rrp7b2v-droid/black-lady-animatic-v01` 被指定为当前 Project Control canonical repo；`docs/project_control/` 写入 `main` 后成为跨 Chat 正式读取入口。 | ACTIVE / CANONICAL REPO LOCKED |
| BL-D-001 | 2026-09-11 | `docs/project_control/` 作为《黑衣夫人》项目正式事实源；Dashboard 只作为派生可视化窗口。 | ACTIVE |
| BL-D-002 | 2026-09-11 | Project Control 采用 GitHub canonical + Local working copy 模型：ChatGPT 在阶段 / Gate / 正式任务完成并形成结论后更新 GitHub；本地工作前 pull 最新 `main`。 | ACTIVE / repo assignment completed by BL-D-007 |
| BL-D-003 | 2026-09-11 | 每次开启新的项目 Chat，先读取 Project Control 了解当前进展、阻塞与下一任务，不以旧聊天 handoff 作为正式状态源。 | ACTIVE |
| BL-D-004 | 2026-09-11 | 项目重启首先处理三项专项：P0.1 故事与文本数据基线；P0.2 人物锚定与 Scene Master 资产治理；P0.3 视频制作与剪辑 Pipeline 再验证。 | ACTIVE / P0 RESTART |
| BL-D-005 | 2026-09-11 | 小说数据未来至少包含：完整《诡舍》用于上下文检索；单独《黑衣夫人》用于改编；有声小说转文字用于与实际音频校对、验证和定位。 | ACTIVE / P0.1 INPUT |

## 当前边界

- P0.1 已由 Product Owner 明确批准 PASS；S1 / S2 / canonical audio / 完整 MVP1 S3 searchable index 构成正式故事与声音事实基线。
- 所有后续 Gate / Phase 必须经过 Product Owner 明确审批；技术完成只能进入 `READY_FOR_APPROVAL`，不得自动 PASS / CLOSED。
- P0.2 的正式方向已锁定为 Visual Asset Management System V1，而不是单纯图库整理；必须实现/验证 Entity/Asset、Reference Resolver、Automatic Ingest 与 Audit Trail 的可执行路径。
- P0.2-02 Character Asset 采用 Tier A/B/C/D 分级；具体角色归属尚未自动认定，下一步进行 9 Character Tier Assignment + Gap Analysis。
- P0.2-02 Entity / Asset Registry Schema V0.3 已由 Product Owner 于 2026-09-13 批准锁定；Schema 锁定不等于 P0.2 Gate PASS。
- 正式 Registry 长期模型固定为 Entity Registry / Asset Registry / Asset Relations / Append-only Audit Event Log；Migration Mapping Manifest 仅服务旧资产迁移。
- canonical Shot ID 不继承历史 `REBOOT` 标签；多人物 Shot 仍为 Shot-bound Asset，人物/场景组成由 Shot Register / Shot Spec 表达。
- P0.1–P0.3 是项目 Gate / 重启专项，不自动占用 Codex D-###。
- MVP1 正式故事起点锁定为 S2 第134章开头；实际终点按有声小说叙事/音频边界锁定，当前录制范围已跨入第135章开头。
- MVP1 canonical audio 已锁定为 `AUDIO_MVP1_CANONICAL_V001.m4a`；它是原音内容与 source extraction 边界的最高音频事实源，但不是动画节奏母版。
- 正式硬规则：`SOURCE AUDIO TC ≠ FINAL EDIT TC`。
- S3 = 可机器检索的原音素材定位/验证层；A1 = 改编取舍；Shot Plan = 镜头叙事与画面需求；Audio Alignment / Resolver = 根据已确定镜头自动检索、定位、提取原音；Animatic / Edit Timeline = 最终画面与声音节奏编排。
- 用户不承担常规“搜索某句话 / 找 source TC”的操作；正式流程必须自动从镜头需求派生音频需求。
- 第133章只作为前置语境，不进入 MVP1 正式成片。
- 旧资产不因重启自动废弃，也不因曾被 APPROVED 自动视为当前 `CURRENT`；以 P0.2 authority audit 和新生命周期规则重新分类。
- P0.2 / P0.3 的最终制度或技术方案仍必须经过专项讨论与验证后再形成 Gate Review。
