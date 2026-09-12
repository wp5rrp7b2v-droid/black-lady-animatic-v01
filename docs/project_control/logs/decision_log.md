# Decision Log｜BLACK-LADY-001

本文件只记录已经由 Product Owner 明确形成正式结论、会影响后续执行的重大决策。讨论过程、备选方案和未批准推测不进入本文件。

| ID | 日期 | 决策 | 状态 / 影响 |
|---|---|---|---|
| BL-D-015 | 2026-09-12 | Product Owner 明确：正式生产中不由用户人工搜索“需要哪句话”。应在情节、分镜与镜头画面内容确定后，由后续 Audio Alignment 阶段根据 A1 / Shot Plan 自动识别该镜头或叙事 beat 需要的对白/旁白，自动到 S3 + canonical source audio 中检索对应原音，自动定位 source TC、提取带 handles 的 Audio Clip，并写入 Animatic / Edit Timeline。人工只处理低置信度、匹配冲突、边界异常与最终听审，不承担常规查找时间码。S3 的职责因此是可机器检索的 source-audio index，不要求在前置阶段把整条 canonical audio 全量切成成片级精确小段。 | ACTIVE / DOWNSTREAM AUDIO RESOLVER MODEL LOCKED / P0.3 INPUT |
| BL-D-014 | 2026-09-12 | Product Owner 明确：`AUDIO_MVP1_CANONICAL_V001.m4a` 及 S3 仅作为后续动画的原始配音 / 旁白素材来源与可验证定位层，不作为动画节奏母版。正式硬规则锁定为 `SOURCE AUDIO TC ≠ FINAL EDIT TC`。S3 记录 source audio 中实际说了什么、谁说、旁白/对白类型与 source TC；A1 `ADAPTATION_SCRIPT` 决定成片保留/删除/重组内容；`Animatic / Edit Timeline` 决定镜头节奏、镜头时长、停顿、转场及选中原音在成片中的最终摆放位置。不得为了迁就镜头时长改变原音语速。 | ACTIVE / P0.1-05B RULE LOCKED / SOURCE-AUDIO AND EDIT-TIMELINE SEPARATED |
| BL-D-013 | 2026-09-12 | Product Owner 审核并批准 `AUDIO_MVP1_CANONICAL_CANDIDATE_V002.m4a` 的首尾边界：起点完整保留“欢迎各位来到艾伦古堡”，终点完整保留“而后又匆匆离去备餐”。该文件正式晋级并命名为 `AUDIO_MVP1_CANONICAL_V001.m4a`。其来源为 `AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`，以 stream copy 方式裁切，不重新编码；源音频起点约 22.800 sec，终点为当前 RAW_AUDIO_EXTRACT 末尾；正式文件 4,957,338 bytes，359.141995 sec，AAC / 44.1kHz / 2ch，SHA-256=`8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`。P0.1-05A 完成；后续 S3 与剪辑定位以该 canonical audio 为 MVP1 最高音频事实源。 | ACTIVE / P0.1-05A COMPLETE / CANONICAL AUDIO LOCKED |
| BL-D-012 | 2026-09-12 | Product Owner 进一步明确 MVP1 的边界规则：MVP1 从 S2 第134章《【黑衣夫人】参观》开头开始，但不以原文章节结尾作为硬边界。由于有声小说的分集/进度与原文章节划分存在差异，本次实际录制内容跨入 S2 第135章开头。MVP1 应定义为“按真实有声小说连续叙事与音频边界锁定的片段”，原文章节仅用于内容映射；正式音频起止时间以 canonical audio 为最终事实依据。 | ACTIVE / CLARIFIES BL-D-011 / MVP1 AUDIO-SPAN MODEL |
| BL-D-011 | 2026-09-12 | Product Owner 正式锁定第一个 MVP 的故事起点：从 S2 第134章《【黑衣夫人】参观》开始；第133章不属于 MVP1 正式成片范围，仅保留为前置语境。MVP1 所需原音频的获取、准备、登记、转写与校验本身属于项目能力建设的一部分，不要求先准备完整《黑衣夫人》全部有声书。现有 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 仅为历史测试片段，降级为 NON-CANONICAL TEST AUDIO，不得作为 MVP1 canonical audio baseline。BL-D-012 对“第134章”进一步澄清为起始锚点而非唯一内容范围。 | ACTIVE / MVP1 START LOCKED / P0.1-05 REFRAMED |
| BL-D-010 | 2026-09-12 | Product Owner 指定当前上传的完整《诡舍》原文为 S1 唯一 canonical source；正式文件名锁定为 `S1_SOURCE_NOVEL_FULL_V001.txt`，格式 UTF-8 plain text，SHA-256=`f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e`。结构检查发现源文件从第460章直接跳至第462章，该现象登记为 `SOURCE-NATIVE NUMBERING ANOMALY`，不得自行补章或重编号。 | ACTIVE / P0.1-04 COMPLETE / S1 LOCKED |
| BL-D-009 | 2026-09-12 | Product Owner 批准将 `docs/project_control/` 从平铺结构重构为 `core/`、`logs/`、`gates/`、`dashboard/`、`archive/`；生产源数据与 Project Control 分离，统一进入仓库根目录 `source_material/`。 | ACTIVE / PROJECT CONTROL STRUCTURE 1.1 |
| BL-D-008 | 2026-09-12 | Product Owner 指定 2026-09-12 当前 Chat 上传的《黑衣夫人》文本为 S2 唯一 canonical source；正式文件名锁定为 `S2_SOURCE_BLACK_LADY_TEXT_V001.txt`，格式为 UTF-8 plain text，正文保持原始字节不改；范围第133–164章，SHA-256=`159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`。其他同名/近似文本降级为 non-canonical reference。 | ACTIVE / P0.1-03 COMPLETE / S2 LOCKED |
| BL-D-006 | 2026-09-11 | Product Owner 批准 Dashboard V002：必须显示 Overall Gate Progress、Current Blockers、Current Gates 及其状态、Current Stage Goal；`Control Rule` 正式更名为 `Project Control Rules`。 | ACTIVE / DASHBOARD V002 APPROVED |
| BL-D-007 | 2026-09-11 | `wp5rrp7b2v-droid/black-lady-animatic-v01` 被指定为当前 Project Control canonical repo；`docs/project_control/` 写入 `main` 后成为跨 Chat 正式读取入口。 | ACTIVE / CANONICAL REPO LOCKED |
| BL-D-001 | 2026-09-11 | `docs/project_control/` 作为《黑衣夫人》项目正式事实源；Dashboard 只作为派生可视化窗口。 | ACTIVE |
| BL-D-002 | 2026-09-11 | Project Control 采用 GitHub canonical + Local working copy 模型：ChatGPT 在阶段 / Gate / 正式任务完成并形成结论后更新 GitHub；本地工作前 pull 最新 `main`。 | ACTIVE / repo assignment completed by BL-D-007 |
| BL-D-003 | 2026-09-11 | 每次开启新的项目 Chat，先读取 Project Control 了解当前进展、阻塞与下一任务，不以旧聊天 handoff 作为正式状态源。 | ACTIVE |
| BL-D-004 | 2026-09-11 | 项目重启首先处理三项专项：P0.1 故事与文本数据基线；P0.2 人物锚定与 Scene Master 资产治理；P0.3 视频制作与剪辑 Pipeline 再验证。 | ACTIVE / P0 RESTART |
| BL-D-005 | 2026-09-11 | 小说数据未来至少包含：完整《诡舍》用于上下文检索；单独《黑衣夫人》用于改编；有声小说转文字用于与实际音频校对、验证和定位。 | ACTIVE / P0.1 INPUT |

## 当前边界

- P0.1–P0.3 是项目 Gate / 重启专项，不自动占用 Codex D-###。
- MVP1 正式故事起点锁定为 S2 第134章开头；实际终点按有声小说叙事/音频边界锁定，当前录制范围已跨入第135章开头。
- MVP1 canonical audio 已锁定为 `AUDIO_MVP1_CANONICAL_V001.m4a`；它是原音内容与 source extraction 边界的最高音频事实源，但不是动画节奏母版。
- 正式硬规则：`SOURCE AUDIO TC ≠ FINAL EDIT TC`。
- S3 = 可机器检索的原音素材定位/验证层；A1 = 改编取舍；Shot Plan = 镜头叙事与画面需求；Audio Alignment / Resolver = 根据已确定镜头自动检索、定位、提取原音；Animatic / Edit Timeline = 最终画面与声音节奏编排。
- 用户不承担常规“搜索某句话 / 找 source TC”的操作；正式流程必须自动从镜头需求派生音频需求。
- 第133章只作为前置语境，不进入 MVP1 正式成片。
- 旧资产不因重启自动废弃，也不因曾被 APPROVED 自动视为最终生产资产；以专项审计结果重新分类。
- 当前不在本文件预判 P0.2 / P0.3 的最终制度或技术方案，必须经过专项讨论与验证后再形成新决策。
