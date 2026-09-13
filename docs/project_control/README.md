# Project Control｜BLACK-LADY-001

本目录是《诡舍·黑衣夫人》的正式项目控制入口（SSOT）。

## 目录

- `core/`：当前状态、治理规则、Gate 验收矩阵
- `logs/`：重大决策、工程执行、规则变更历史与正式 Risk Register
- `gates/`：按 P0.1 / P0.2 / P0.3 分开的专项工作记录
- `dashboard/`：派生可视化 Dashboard；非事实源
- `archive/`：阶段关闭后的压缩总结

## 新 Chat 读取顺序

1. `core/project_state.json`
2. `core/governance.md`
3. 按当前 Gate 读取对应 `gates/` 内容
4. 必要时读取 `logs/` 与 `core/acceptance_matrix.md`
5. 若 `project_state.json` 存在 active risk，读取 `logs/risk_register.md` 后再开始相关工程任务

## Project Control Closeout

- 每完成一个会改变正式项目事实的重要 Step / 正式任务 / 工程任务 / Product Owner 决策 / 规则变更，必须检查并同步所有受影响的 Project Control 文件，不能只更新单一 progress 文件。
- 每天结束工作前必须执行一次 cross-file consistency check，核对 `project_state.json`、当前 Gate README / progress、decision / execution / rules / risk logs、acceptance matrix 与 Dashboard。
- 收尾重点检查 Current Task、Blocker、Next Action、Asset ID / Version、D-### 编号、active risks，以及“已经完成但仍被标记 NEXT”的过期状态。
- 完整规则见 `core/governance.md` Section 12；一致性核对不改变 Product Owner-only Gate / Phase approval rule。

源小说、音频转写等生产源数据不放在 Project Control；统一进入仓库根目录 `source_material/`。
