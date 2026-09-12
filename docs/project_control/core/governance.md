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

1. **ChatGPT**：负责项目判断、方案、Gate Review、验收建议与 Project Control 维护。
2. 每完成明确阶段 / Gate / 正式任务并形成结论后，由 ChatGPT 更新 canonical repo。
3. **Local sync**：本地工程开始前执行 `git pull --ff-only origin main`。
4. **Codex**：负责本地工程、脚本、Remotion、音视频处理、文件与 Git 操作；只有 Task Contract 明确授权时才修改 Project Control。
5. ChatGPT 与 Codex 不并行修改同一 Project Control 文件。
6. 遇到 non-fast-forward、未知 tracked changes 或状态冲突时停止，不 force、不覆盖。

## 5. Dashboard 规则

- Dashboard 只展示当前管理和决策需要的信息。
- Dashboard 不保存正式历史，不承担 SSOT 职责。
- Dashboard 的数据必须来自 Project Control。

## 6. 任务与编号

- **P0.x**：重启阶段的项目 Gate / 专项，不等同于 Codex 工程任务。
- **D-###**：只用于实际交给 Codex 执行的工程任务。
- ChatGPT 的讨论、审核、项目控制、Prompt 设计、Gate Review 不占 D 编号。
- 当前历史工程编号已到 D-056；只有出现新的实际 Codex 工程任务时再继续编号。

## 7. 当前重启边界

P0 不继续生产 A08 或后续正式镜头；先重建：

- P0.1｜故事与文本数据基线
- P0.2｜人物锚定与 Scene Master 资产治理
- P0.3｜视频制作与剪辑 Pipeline 再验证

## 8. 角色

- **Product Owner**：用户；负责目标、重大决策，以及所有 Gate / Phase 的最终批准。
- **ChatGPT**：项目控制、方案、验证设计、审核、Gate / Phase Review、Project Control 维护；无权自行完成最终批准。
- **Codex**：本地工程执行；按明确 Task Contract 工作；无权自行完成 Gate / Phase 最终批准。
- **GitHub canonical repo**：正式提交状态、版本历史、备份和跨环境访问层。

## 9. Source Material Storage Boundary

当前 canonical repo 已为 **Private**。文本型源数据可按 `source_material/` 的分类规则提交并版本化；大型原始音频、视频和高容量二进制资产不得无规则直接进入普通 Git，应在 P0.1 / P0.3 中决定 Git LFS、Release/Artifact 或其他私有存储方案。

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
