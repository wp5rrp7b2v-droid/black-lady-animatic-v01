# Project Control｜BLACK-LADY-001

本目录是《诡舍·黑衣夫人》的正式项目控制入口（SSOT）。

## 目录

- `core/`：当前状态、治理规则、Gate 验收矩阵
- `logs/`：重大决策、工程执行、规则变更历史
- `gates/`：按 P0.1 / P0.2 / P0.3 分开的专项工作记录
- `dashboard/`：派生可视化 Dashboard；非事实源
- `archive/`：阶段关闭后的压缩总结

## 新 Chat 读取顺序

1. `core/project_state.json`
2. `core/governance.md`
3. 按当前 Gate 读取对应 `gates/` 内容
4. 必要时读取 `logs/` 与 `core/acceptance_matrix.md`

源小说、音频转写等生产源数据不放在 Project Control；统一进入仓库根目录 `source_material/`。
