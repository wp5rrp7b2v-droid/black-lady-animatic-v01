# Governance｜诡舍·黑衣夫人 Project Control System 1.0

## 1. 核心原则

**Project Control 文件集是项目正式事实源；Dashboard 只是派生的可视化窗口。**

- GitHub repo `wp5rrp7b2v-droid/black-lady-animatic-v01` 的 `main` 上最新正式提交的 `docs/project_control/`：定义为 **canonical committed state**。
- 本地 `docs/project_control/`：日常 **working copy**。
- Dashboard 可以重建、替换或暂时缺失；如与 Project Control 冲突，以 Project Control 为准。

建议本地路径：

`/Users/caroline/诡舍/黑衣夫人/black_lady_short_01/docs/project_control/`

## 2. 文件职责

| 文件 | 唯一职责 |
|---|---|
| `project_state.json` | 当前 Phase、Gate、Current Task、Blocker、Next Action、基线状态 |
| `decision_log.md` | 已批准、会影响后续执行的重大决策 |
| `execution_log.md` | 实际工程执行结果、失败、证据摘要；Codex 工程任务沿用 D-### |
| `acceptance_matrix.md` | Gate / 验收标准、状态、通过依据、限制 |
| `governance.md` | 项目治理、角色、SSOT、同步、审批与版本规则 |
| `rules_change_log.md` | 管理机制本身的变更历史与被替代规则 |
| `phase_archive/` | Phase 关闭后的压缩总结 |
| `dashboard.html` | 从 Project Control 派生的可视化快照；非事实源 |

## 3. 新 Chat 启动规则

每次开启新的项目 Chat：

1. 先读取 `docs/project_control/`；
2. 优先读取 `project_state.json`，再按需读取 Governance / Decision / Acceptance / Execution；
3. 先复述当前 Phase、Gate、Current Task、Blocker、Next Action；
4. 不依赖旧 Chat handoff 作为正式状态来源；
5. 若聊天记忆与 Project Control 冲突，以 GitHub `main` 上最新正式 Project Control 为准。

## 4. 同步模型

1. **ChatGPT**：负责项目判断、方案、Gate Review、验收，以及决定哪些事实应进入 Project Control。
2. 每完成一个明确阶段 / Gate / 正式任务并形成结论后，由 ChatGPT 更新 Project Control，并提交到 GitHub canonical repo。
3. **Local sync**：本地工程工作开始前执行 `git pull --ff-only origin main`。
4. **Codex**：负责本地工程、脚本、Remotion、音视频处理、文件与 Git 操作；只有 Task Contract 明确授权时才修改 Project Control。
5. ChatGPT 与 Codex 不得并行修改同一 Project Control 文件。
6. 遇到 non-fast-forward、未知 tracked changes 或状态冲突时停止，不 force、不覆盖。

## 5. Dashboard 规则

- Dashboard 只展示当前管理和决策需要的信息。
- Dashboard 不保存正式历史，不承担 SSOT 职责。
- Dashboard 的数据必须来自 Project Control。
- Dashboard 错误、缺失或过期不得阻塞项目继续工作；应以 Project Control 为准。

## 6. 任务与编号

- **P0.x**：重启阶段的项目 Gate / 专项，不等同于 Codex 工程任务。
- **D-###**：只用于实际交给 Codex 执行的工程任务。
- ChatGPT 的讨论、审核、项目控制、Prompt 设计、Gate Review 不占 D 编号。
- 当前历史工程编号已到 D-056；只有出现新的实际 Codex 工程任务时再继续编号。

## 7. 当前重启边界

本次 P0 不继续生产 A08 或后续正式镜头；先重建三项基础能力的可信基线：

- P0.1｜故事与文本数据基线
- P0.2｜人物锚定与 Scene Master 资产治理
- P0.3｜视频制作与剪辑 Pipeline 再验证

P0 的目标不是推翻旧资产，而是判定：**什么真实存在、什么已验证可用、什么未验证 / 已失败、什么仍缺失。**

## 8. 角色

- **Product Owner**：用户；负责目标、重大决策、Gate Approval。
- **ChatGPT**：项目控制、方案、验证设计、审核、Project Control 维护。
- **Codex**：本地工程执行；按明确 Task Contract 工作。
- **GitHub canonical repo**：正式提交状态、版本历史、备份和跨环境访问层。

## 9. Source Material Privacy Boundary

当前 canonical repo 为 public。Project Control 可提交；但完整小说原文、有声小说全文转写、原音频等可能受版权约束的源材料，在未迁移到 private repo / private storage 前，不得直接提交到该 public repo。P0.1 必须单独决定其私有存储方式。
