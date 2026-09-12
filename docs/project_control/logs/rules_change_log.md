# Rules Change Log｜BLACK-LADY-001

| ID | 日期 | 规则变化 | 状态 |
|---|---|---|---|
| RC-007 | 2026-09-12 | Project Control 目录升级为 1.1：`core/`、`logs/`、`gates/`、`dashboard/`、`archive/`；生产源数据移出 Project Control，统一进入 `source_material/`。 | ACTIVE |
| RC-005 | 2026-09-11 | Dashboard V002 获批：必须可视化总体 Gate 完成度、当前 Gate 状态、阶段目标和真实 Blocker；项目控制规则区明确命名为 `Project Control Rules`。 | ACTIVE |
| RC-006 | 2026-09-11 | canonical repo 锁定为 `wp5rrp7b2v-droid/black-lady-animatic-v01`；新的项目 Chat 以其 `main/docs/project_control/` 为正式读取入口。 | ACTIVE |
| RC-001 | 2026-09-11 | 项目从依赖 Chat handoff / 分散记录，切换为 `docs/project_control/` 作为正式事实源。 | ACTIVE |
| RC-002 | 2026-09-11 | Dashboard 明确降级为 Project Control 的派生可视化，不再承担项目状态源职责。 | ACTIVE |
| RC-003 | 2026-09-11 | 新 Chat 的标准启动方式改为：先读取 Project Control，再继续项目。 | ACTIVE |
| RC-004 | 2026-09-11 | 重启阶段先完成 P0.1 / P0.2 / P0.3 三项基础专项，再根据验证结果设计正式生产 Roadmap。 | ACTIVE |

后续若规则被替代，不删除历史；新增记录并标记旧规则 `SUPERSEDED`。
