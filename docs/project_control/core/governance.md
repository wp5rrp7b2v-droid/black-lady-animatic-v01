# Governance｜诡舍·黑衣夫人 Project Control System 1.1

## 1. 核心原则

**Project Control 文件集是项目正式事实源；Dashboard 只是派生的可视化窗口。**

- GitHub repo `wp5rrp7b2v-droid/black-lady-animatic-v01` 的 `main/docs/project_control/`：canonical committed state。
- 本地对应目录：working copy。
- Dashboard 可重建或暂时缺失；如与 Project Control 冲突，以 Project Control 为准。

## 2. 目录职责

| 路径 | 唯一职责 |
|---|---|
| `core/project_state.json` | 当前 Phase、Gate、Current Task、Blocker、Next Action、基线状态 |
| `core/acceptance_matrix.md` | Gate / 验收标准、状态、通过依据、限制 |
| `core/governance.md` | 项目治理、角色、SSOT、同步、审批与版本规则 |
| `logs/decision_log.md` | 已批准、影响后续执行的重大决策 |
| `logs/execution_log.md` | 实际工程执行结果、失败、证据摘要；Codex 工程任务沿用 D-### |
| `logs/rules_change_log.md` | 管理机制本身的变更历史与被替代规则 |
| `gates/` | P0.1 / P0.2 / P0.3 等专项 Gate 的工作记录与盘点 |
| `dashboard/dashboard.html` | Project Control 派生可视化；非事实源 |
| `archive/` | Phase 关闭后的压缩总结 |

生产源数据统一放在仓库根目录 `source_material/`，不得与 Project Control 混放。

## 3. 新 Chat 启动规则

1. 先读取 `docs/project_control/core/project_state.json`；
2. 再按需读取 `core/governance.md`、当前 Gate 对应 `gates/`、`logs/` 与 `core/acceptance_matrix.md`；
3. 先复述当前 Phase、Gate、Current Task、Blocker、Next Action；
4. 不依赖旧 Chat handoff 作为正式状态来源；
5. 若聊天记忆与 Project Control 冲突，以 GitHub `main` 最新正式 Project Control 为准。

## 4. 同步模型

1. **ChatGPT**：负责项目判断、方案、Gate Review、验收建议、Project Control 维护，以及可通过当前 GitHub 能力直接完成的文本 / 轻量代码写入。
2. 每完成明确阶段 / Gate / 正式任务并形成结论后，由 ChatGPT 更新 canonical repo。
3. **Local sync**：本地工程开始前执行 `git pull --ff-only origin main`；若 GitHub 网络需要动态代理，则按当前已验证的网络规则使用 `git-proxy-auto`。
4. **Codex**：只负责确实需要访问或修改本地项目文件、代码库、脚本、Remotion 工程、音视频处理、测试 / 调试或其他本地工程环境的执行工作；只有 Task Contract 明确授权时才修改 Project Control。
5. ChatGPT 与 Codex 不并行修改同一 Project Control 文件。
6. 遇到 non-fast-forward、未知 tracked changes 或状态冲突时停止，不 force、不覆盖。
7. **GitHub write reminder**：每次 ChatGPT 对 canonical GitHub repo 完成实际写入 / 更新后，用户可见回复必须明确提醒 Product Owner 同步本地 working copy；默认命令为：

```bash
cd "/Users/caroline/诡舍/黑衣夫人/black_lady_short_01"
git pull --ff-only origin main
```

8. 若当次存在本地 tracked changes、二进制资产、Codex 并行工作或潜在冲突风险，提醒同步时应先要求检查 `git status`，不得机械执行覆盖。

### 4.1 Execution Routing Rule｜Chat / Terminal / Codex 分工

本规则适用于《诡舍·黑衣夫人》整个项目，不限于任何单一 Gate、AO 任务或当前阶段。

执行工具选择以**最小必要执行面**为原则，不因为任务带有“工程”“脚本”“Git”字样就默认交给 Codex。

#### Chat 优先

以下工作默认由 Chat 完成：

- 讨论、分析、方案设计、架构与流程设计；
- 导演判断、Gate Review、风险判断、验收与决策支持；
- Task Contract / Prompt / DoD / Rule 的设计与锁定；
- Project Control、Governance、Decision / Rules Log 等可直接维护的 canonical 文档；
- 当前 GitHub 能力可以直接安全完成的文本文件或轻量代码新增 / 修改；
- 对终端输出、测试结果、Git 状态、脚本 dry-run 的判断与复核。

如果 Chat 已能可靠完成设计、写入或 GitHub 同步，不得为了“使用 Codex”而把同一工作重复交给 Codex。

#### Terminal 优先

以下本地动作优先由 Product Owner 在 Chat 给出的明确命令下，通过 Terminal 执行，不单独创建 Codex 工程任务：

- `git status / diff / rev-parse / ls-remote` 等状态检查；
- `git-proxy-auto pull / fetch / push` 等已经验证的 Git 网络操作；
- local working copy 同步；
- 运行已有脚本、dry-run、validator、unit tests；
- 已经在 Chat 完成设计、无需本地代码修改的确定性一次性执行；
- 在变更范围明确且无复杂冲突时的 `git add / commit / push`。

Terminal 只承担明确执行，不替代 Chat 的方案判断与结果审核。

#### Codex 仅在确有本地工程必要时使用

只有以下情况才默认进入 Codex：

- 必须读取、创建、修改多个本地工程文件；
- 需要理解本地代码库后进行实质代码实现或重构；
- 需要 Remotion、媒体处理、Blender、本地脚本链或其他工程环境执行；
- 需要多轮本地测试、调试、修复；
- 需要 Git / 文件系统 / 本机应用环境的连续工程操作，且用 Chat + Terminal 会明显增加错误风险或人工操作成本。

即使必须使用 Codex，也必须遵循：

`Chat 完成思考 / 设计 / 边界 / 验收标准 → Codex 只执行明确工程任务 → Chat 审核结果并作项目判断`

不得把开放式方案设计、产品判断或 Gate 决策外包给 Codex。

#### 编号规则

- 只有**实际交给 Codex 执行**的工程任务才占用 `D-###` 编号。
- Chat 完成的代码设计 / GitHub 写入、Terminal 执行、审核、决策、Gate Review 均不占 `D-###`。
- 已起草但最终未交给 Codex 执行的任务，不因为曾出现过候选编号而视为正式已消耗的 Codex 工程编号。

#### GitHub / Local Sync 特别规则

- Chat 能直接更新 canonical GitHub 的内容，优先由 Chat 写入。
- 写入后需要本地同步时，优先由 Terminal 使用 `git-proxy-auto pull --ff-only origin main`。
- 仅为 pull / push / SHA 核验 / 网络诊断而调用 Codex，原则上属于过度升级；除非出现必须依赖本地工程自动化或复杂故障定位的情况。

Product Owner 可随时基于效率、风险或实际体验调整当次执行方式；本规则目标是减少不必要的 Codex 介入，同时保留其在真正本地工程任务中的价值。

## 5. Dashboard 规则

- Dashboard 只展示当前管理和决策需要的信息。
- Dashboard 不保存正式历史，不承担 SSOT 职责。
- Dashboard 的数据必须来自 Project Control。

## 6. 任务与编号

- **P0.x**：重启阶段的项目 Gate / 专项，不等同于 Codex 工程任务。
- **D-###**：只用于实际交给 Codex 执行的工程任务。
- ChatGPT 的讨论、审核、项目控制、Prompt 设计、Gate Review、GitHub 直接写入和 Terminal 指导执行不占 D 编号。
- Governance 不硬编码“当前已到哪个 D-### / 下一编号”。实际下一 D-### 以 `core/project_state.json`、`logs/execution_log.md` 与已真实执行的 Codex 任务为准，避免项目推进后规则文档产生过期编号。

## 7. 当前重启边界

2026-09-11 启动 P0 时的原始边界是：先完成 P0.1 / P0.2 / P0.3，不直接恢复 A08 之后的全片量产。

当前解释已随 P0.3 的真实验证推进而收敛为：

- P0.1｜故事与文本数据基线；
- P0.2｜人物锚定与 Scene Master 资产治理；
- P0.3｜视频制作与剪辑 Pipeline 再验证；
- **P0.3 允许为了代表性真实 Proof 制作、批准和登记必要的 Story Shots**，包括 Opening V2 所需补充镜头；
- 这不等于恢复全章节 / 全片规模化生产。正式量产 Roadmap 仍须等 P0.3 形成代表性证据并由 Product Owner 明确批准后再决定。

因此，“P0 不继续生产 A08 或后续正式镜头”只保留为 P0 启动时的历史边界，不再解释为禁止 P0.3 为验证目的制作必要 Story Shots。

## 8. 角色

- **Product Owner**：用户；负责目标、重大决策，以及所有 Gate / Phase 的最终批准。
- **ChatGPT**：项目控制、方案、验证设计、审核、Gate / Phase Review、Project Control 维护；无权自行完成最终批准。
- **Codex**：本地工程执行；按明确 Task Contract 工作；无权自行完成 Gate / Phase 最终批准。
- **GitHub canonical repo**：正式提交状态、版本历史、备份和跨环境访问层。

## 9. Source Material Storage Boundary

当前 canonical repo 的可见性以 `core/project_state.json` 为准；截至 2026-09-27 为 **public**。文本型源数据可按 `source_material/` 的分类规则提交并版本化；大型原始音频、视频和高容量二进制资产不得无规则直接进入普通 Git，应按已批准的 Git LFS、Release / Artifact 或其他受控存储方案处理。

## 10. Gate / Phase Approval Rule

正式审批权只属于 **Product Owner**。

- 当 Gate 或 Phase 的验收条件在执行层面已经满足时，ChatGPT / Codex 只能将其建议状态标记为 `READY_FOR_APPROVAL`，不得自行写成 `PASS`、`APPROVED`、`CLOSED` 或进入下一 Phase 的正式关闭状态。
- 只有 Product Owner 在 Chat 中给出明确批准（例如“批准”“PASS”“正式通过”“可以关闭该 Phase / Gate”）后，Project Control 才能把对应 Gate / Phase 更新为正式 `PASS / APPROVED / CLOSED`。
- 若验收条件满足但尚未获得 Product Owner 批准，状态必须保持 `READY_FOR_APPROVAL / WAITING_PO_APPROVAL`，不得因技术完成自动晋级。
- Product Owner 批准后，ChatGPT 负责把批准事实、日期和后续 Current Gate / Phase 写入 canonical Project Control。
- 本规则同样适用于重启 Gate（如 P0.1 / P0.2 / P0.3）和后续正式 Phase；不得因层级命名不同绕过审批。

## 11. Visual Asset Governance Rule

视觉资产统一采用 `Entity → Asset → Derived Reference → Shot Reference Package` 的治理模型。人物、场景、服装、道具采用同一底层规则，不再分别依赖人工记忆或临时挑图。

### 11.1 正式资产准入

- 只有 Product Owner 在 Chat 中明确批准的视觉结果，才允许进入正式 Asset Registry。
- `DRAFT / CANDIDATE / REVIEWED / REJECTED` 属于生成任务或审核日志，不属于正式 Asset Registry 生命周期。
- 未经 Product Owner 批准的图片不得因为“曾生成”“曾审核”或“看起来可用”而自动进入正式生产资产库。

### 11.2 Entity 与 Asset 分离

- 人物、场景、服装、道具等叙事对象必须具有稳定唯一的 `entity_id`。
- 具体图片、Reference Sheet、Scene Master、Prop Master 等属于 `asset_id`；一个 Entity 可以拥有多个 Asset。
- 不允许用文件名、文件路径或单张图片本身代替 Entity 身份。

### 11.3 Approval 与 Lifecycle 分离

正式资产保留“曾被批准”这一历史事实；生命周期单独管理。

正式 Asset Registry 的生命周期统一为：

- `CURRENT`：当前允许作为生产权威或生产参考调用；
- `SUPERSEDED`：已有新的正式 Approved 资产明确替代；
- `DEPRECATED`：不再允许用于新生产，但未必已有直接替代品；
- `ARCHIVED`：历史保留，不属于当前 Active Production Set。

被替代、废弃或归档的资产不得删除其审批与历史使用记录。

### 11.4 Atomic Master 与 Derived Reference 分离

- Face / Body / Profile / Back / Scene Master / Prop Master 等 Atomic Master 是事实层或权威输入层。
- Character Reference Sheet、Scene Reference Sheet、Costume / Prop Sheet 等是由 Atomic Assets 派生的生产便利层，不得反向覆盖底层 Master 的权威事实。
- Derived Reference 必须记录其依赖的 source asset IDs；当上游 Master 被替换或 Deprecated 时，系统必须能够识别受影响的 Derived Reference。

### 11.5 正常生产目标：零手工资产管理

正式生产的目标流程为：

`Shot / Task Spec → Reference Resolver → Reference Package → Generation → PO Approval → Automatic Ingest → Asset Registry / Audit Trail`

正常路径中，Product Owner 不承担例行的：

- 手工挑选参考图；
- 手工下载 / 搬运到指定目录；
- 手工命名；
- 手工登记 Asset Registry；
- 手工维护版本替代关系。

以上机械动作应由系统自动完成。人工只保留创意判断、异常处理与正式审批。

**Story Shot 当前输出发布例外（RC-024 / RC-025）**：

- “零手工资产管理”仍是 Entity / Asset Registry 的长期目标；
- 当前 P0.3 `STORY_SHOT` 流程在 **Product Owner 已批准最终 Candidate 之后**，允许 Product Owner 执行一次“原始最终 PNG → canonical GitHub intake 目录”的二进制发布动作；
- 该动作是 **final output publication**，不是 RC-022 / RC-023 所说的 reference upload；正式参考图交付仍保持 `manual Product Owner reference upload = 0`；
- Product Owner 不负责正式命名、Asset ID、Story Shot Index 登记、hash 计算、版本关系或验证；这些机械步骤继续由 Chat / GitHub / Actions 完成；
- 该例外只适用于当前已验证的 Story Shot 注册桥接，直到后续有经真实验证并由 Product Owner 批准的 automatic output ingest 规则取代。

### 11.6 Reference Resolver

- 生产任务应优先从结构化 Shot / Task Spec 推导需要的人物、视角、场景、服装、道具及状态。
- Reference Resolver 必须根据 `entity_id / asset_role / lifecycle / authority / variant / shot requirement` 自动返回当前有效的参考资产。
- 正常生产不得依赖“进入 Library 后人工凭印象选择几张图”作为标准流程。
- Resolver 输出必须形成唯一可追踪的 `reference_package_id`，记录当次实际使用的资产版本。

### 11.7 Audit Trail

每一项正式资产及其生产调用至少必须可追溯：

- 来源：generation task、model、prompt / instruction version、reference assets；
- 身份：entity_id、asset_id、asset_role、version；
- 审批：approved_by、approved_at；
- 生命周期：supersedes / superseded_by / deprecation / archive reason；
- 依赖：Derived Reference 依赖哪些 Atomic Assets；
- 使用：被哪些 Reference Package、Shot、Generation Task 调用；
- 完整性：重要字段变更必须留下历史，不允许静默覆盖。

P0.2 的详细字段、人物标准视图、场景/服装/道具模板、存储方案、Reference Resolver 规则和 Production Readiness 计算方式在专项规范中定义；本节只锁定项目级硬规则。

## 11.8 Work Formal Image Generation Delivery Rule

凡由 ChatGPT Work 执行的正式视觉制图 / Story Shot 制图，正式生产基线固定为：

`GitHub canonical assets → Resolver / Registry validation → Reference Delivery Bundle → Work automatic PNG acquisition → image generation`

这是正式生产路径，不是可选建议。

硬规则：

- **GitHub canonical assets** 是正式视觉输入的唯一 canonical binary authority；Work 不以聊天附件、Library 临时副本、浏览器预览图或人工记忆取代 canonical source。
- **Resolver / Registry validation** 必须先于制图发生。只允许满足当次 Shot / Task Spec 的正式有效资产进入 Reference Delivery Bundle；不得静默使用 `SUPERSEDED / DEPRECATED / REJECTED / CANDIDATE / WIP` 资产。
- **Reference Delivery Bundle** 是 GitHub canonical binary 到 Work 图像输入层之间的正式 transport layer。标准实现为：GitHub Actions / repo-native automated runner 在 canonical repo 内完成 checkout、Resolver / Registry 校验、exact-binary copy、manifest 生成，并通过 `actions/upload-artifact` 发布短期 workflow artifact。Bundle 必须记录实际输入的 canonical path、asset / role identity、SHA-256、byte size、source commit 与必要的 authority / continuity responsibility。
- **Work automatic PNG acquisition** 的标准实现为：Work 通过已连接 GitHub 能力自动定位并下载该 workflow artifact，在 Work 环境内解包、重新校验 manifest / SHA / byte size 后，将实际 PNG 直接送入 image generation。Product Owner manual reference upload 的正常目标为 `0`。
- Reference Delivery Bundle 的 ZIP 是 GitHub Actions 内部 transport artifact，不是要求 Product Owner 本地制作或上传到 ChatGPT Project 的交付文件；不得仅为了建立 Bundle 而把任务升级给 Codex / Local Terminal。
- 不得把“直接通过 private GitHub raw URL / browser 打开 PNG”作为正式 baseline，也不得要求 Product Owner 例行手工逐张挑选、下载、打包或上传 canonical references。
- **image generation** 只有在 Bundle 的实际 PNG 已成功物化并完成必要校验后才允许开始。若 binary materialization / delivery 失败，必须 fail closed，明确报告失败层级，不得在缺少正式参考图时继续生成。
- 用户直接上传的非 canonical 源图仅可在任务明确要求“以该用户提供原图为直接编辑底图”时作为显式 intake；它不得绕过正式身份 / 场景 authority，也不得被误登记为 canonical asset。
- 任何偏离该正式链路的临时 fallback，必须明确记录原因、输入来源、完整性校验和 Product Owner 授权；fallback 不能静默升级为新的默认生产模式。

本规则锁定的是**正式制图的数据交付链路**，不改变 Product Owner-only approval，不改变 Asset Registry / Story Shot admission 规则，也不要求 Work 自行承担 GitHub canonical 状态判断；Reference Resolver / Registry 层负责先完成正式参考选择与校验。

## 11.9 Story Shot Operational Layer / Precedence

为避免 P0.2 Asset Registry 的 `asset_class = SHOT` 与 P0.3 的 `asset_class = STORY_SHOT` 混为同一数据层，正式边界如下：

- **P0.2 Asset Registry `SHOT`**：属于 Entity / Asset Registry Schema V0.3，使用 `asset_id`、`SHOT_MASTER` 等受控 metadata，并遵循 `<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>` 命名与 Automatic Ingest 规则；
- **P0.3 `STORY_SHOT`**：当前是服务叙事、构图、剪辑和连续性检索的正式 Story Shot operational layer，权威索引为 `production/story_shots/story_shot_index.jsonl`，由 RC-021 / RC-024 管理；
- 两者不允许静默双重登记，也不允许因为名称相近而自动假定一条 Story Shot 记录已经是 Asset Registry `SHOT` 记录；
- 当前已批准 N01–N10 Story Shot 的既有 canonical filename 不做追溯性大规模重命名；其正式 binary identity 由 canonical path + SHA-256 + byte size + Git blob + Story Shot Index 共同锁定；
- P0.2 Naming Rule 中“文件名不得包含 approved”等限制，适用于 **Asset Registry-managed SHOT assets**，不追溯覆盖 RC-024 已锁定的 Story Shot operational filenames；
- 若未来决定把某个 `STORY_SHOT` 正式提升 / 迁移为 Asset Registry `SHOT`，必须建立显式 migration / ingest 事务，分配 Asset ID、使用 P0.2 compliant filename、保留 source SHA / provenance，并记录 mapping；不得静默覆盖原 Story Shot identity。

Story Shot 的当前操作权威为：

`RC-024 + story_shot_production_registration_sop_v1.md`

如通用 P0.2 资产规则与 Story Shot 专项 SOP 在 **Story Shot 操作步骤** 上发生表述差异，以较新且更具体的 RC-024 / RC-025 为准；P0.2 Schema 对 Entity / Asset Registry 本身继续有效。
## 12. Project Control Step Closeout / Daily Consistency Check

Project Control 维护必须跟随实际项目推进，不允许只更新单一进度文件而让核心状态、Gate 记录和日志长期互相矛盾。

### 12.1 Important Step Closeout

每完成一个会改变正式项目事实的重要 Step、正式任务、工程任务、Product Owner 决策或规则变更后，ChatGPT 必须先判断本次变化影响哪些 Project Control 文件，并在进入下一重要 Step 前同步所有受影响的 canonical 文件。

至少逐项检查：

- `core/project_state.json`：Current Phase / Gate / Task / Blocker / Next Action / checkpoint；
- 当前 `gates/` README、专项 progress / evidence 文件；
- `logs/decision_log.md`：新的 Product Owner 正式决策；
- `logs/execution_log.md`：实际工程完成、失败、修复与验证结果；
- `logs/rules_change_log.md`：治理或生产规则变化；
- `core/acceptance_matrix.md`：新增 Gate evidence 是否改变验收进度；
- `dashboard/dashboard.html`：若当前状态、进度、下一动作发生变化，应从 Project Control 同步派生显示。

更新一个 progress 文件不能视为完整 Step Closeout。

### 12.2 Mandatory Daily Closeout Consistency Check

每天结束工作前必须执行一次 Project Control 一致性核对。至少确认：

1. `project_state.json` 与当前 Gate README / live progress 对 Phase、Gate、Current Task、Blocker、Next Action 的描述一致；
2. 当天已完成的 Codex / 工程任务均已进入 `execution_log.md`；
3. 当天由 Product Owner 明确形成的重大决策均已进入 `decision_log.md`；
4. 当天新增或修改的治理 / 生产规则均已进入 `rules_change_log.md`，并在对应规范文件中体现；
5. `acceptance_matrix.md` 已反映当天新增的真实 Gate evidence，但不得越权把 Gate 自动标记为 PASS；
6. Dashboard 与 canonical Project Control 的当前状态一致；如不一致，以 Project Control 为准并在收尾时更新 Dashboard；
7. 检查是否存在过期的 Current Task、Next Action、旧 Asset ID、旧版本号、旧 D-### 编号或已经完成却仍标记 NEXT 的内容；发现后必须在当天收尾中纠正或明确标记为 historical baseline。

Daily Closeout 只负责事实一致性与记录完整性，不改变 Product Owner-only 的 Gate / Phase 审批权。
