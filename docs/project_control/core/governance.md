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

1. **ChatGPT**：负责项目判断、方案、Gate Review、验收与 Project Control 维护。
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

- **Product Owner**：用户；负责目标、重大决策、Gate Approval。
- **ChatGPT**：项目控制、方案、验证设计、审核、Project Control 维护。
- **Codex**：本地工程执行；按明确 Task Contract 工作。
- **GitHub canonical repo**：正式提交状态、版本历史、备份和跨环境访问层。

## 9. Source Material Storage Boundary

当前 canonical repo 已为 **Private**。文本型源数据可按 `source_material/` 的分类规则提交并版本化；大型原始音频、视频和高容量二进制资产不得无规则直接进入普通 Git，应在 P0.1 / P0.3 中决定 Git LFS、Release/Artifact 或其他私有存储方案。
