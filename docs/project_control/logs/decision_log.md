# Decision Log｜BLACK-LADY-001

本文件只记录已经由 Product Owner 明确形成正式结论、会影响后续执行的重大决策。讨论过程、备选方案和未批准推测不进入本文件。

| ID | 日期 | 决策 | 状态 / 影响 |
|---|---|---|---|
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
- 旧资产不因重启自动废弃，也不因曾被 APPROVED 自动视为最终生产资产；以专项审计结果重新分类。
- 当前不在本文件预判 P0.2 / P0.3 的最终制度或技术方案，必须经过专项讨论与验证后再形成新决策。
