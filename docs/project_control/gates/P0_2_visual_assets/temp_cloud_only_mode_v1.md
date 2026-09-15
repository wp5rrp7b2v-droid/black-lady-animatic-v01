# TEMP_CLOUD_ONLY_MODE_V1｜2026-09-16—2026-09-20

Status: `APPROVED / PRE-EFFECTIVE / TIME-BOXED`

Approved by: `PRODUCT OWNER`

Approved on: `2026-09-14`

Effective period: `2026-09-16 00:00` → `2026-09-20 23:59`

Rules changes: `RC-018 + RC-019`

## 1. Purpose

在 Product Owner 暂时无法稳定使用本地 Mac 的 2026-09-16～2026-09-20 期间，保持《诡舍·黑衣夫人》项目连续推进，同时不降低 P0.2 Approved-but-Open 的正式验收标准。

本临时模式唯一主目标：

`AO-03 → AO-04 → AO-05 → AO-06`

完成上述剩余 P0.2 Closeout 后，才允许解除：

`P0.2-03｜P1 Wave 2｜CHAR_JUN_LUYUAN PROFILE_LEFT`

本模式不提前启动 P0.3，不新增与当前 Gate 无关的旁支任务。

## 2. Authority and precedence

- GitHub `main/docs/project_control/` 继续作为唯一正式 SSOT；
- 本规则是有失效日期的临时执行覆盖，不替代项目长期规则；
- `RC-015` 继续作为长期 Execution Routing 基线，不被 supersede；
- `RC-012` 本地同步提醒规则不被删除或 supersede，但在本规则有效期内执行 `LOCAL_SYNC_DEFERRED / GITHUB_MAIN_CANONICAL` 临时例外；
- Product Owner-only approval authority 不变。

## 3. Daily startup truth check

16～20 日每天开始正式工作前，优先读取：

1. `docs/project_control/core/project_state.json`
2. `docs/project_control/gates/P0_2_visual_assets/README.md`
3. `docs/project_control/gates/P0_2_visual_assets/approved_open_tasks_v1.md`
4. 最新 Decision / Execution / Rules logs

Chat 历史、Codex Cloud workspace、GitHub App 本地缓存均不得独立改变正式项目事实。

## 4. Temporary execution routing

### ChatGPT App

负责：

- 讨论与分析；
- 数据模型 / Schema / Task Contract / Definition of Done；
- 导演判断与审核；
- Prompt 设计；
- Product Owner 决策与审批；
- Project Control 的轻量文本更新。

### Codex Cloud

负责：

- GitHub repo 内需要多文件工程修改的实现；
- Registry / Resolver / scripts / tests / JSON / Markdown 工程变更；
- Reference Package / Derived Reference Sheet 等工程产物；
- 必要的自动化测试；
- commit + remote publication through the verified Codex Cloud native PR workflow。

Codex Cloud 仍必须由 Chat 先锁定任务边界与验收标准。只有实际交给 Codex 执行的工程任务占用新的 D-###。

### GitHub Web / App

负责：

- SSOT 阅读；
- commit / 文件 / diff 审核；
- 远端 publication 确认；
- 必要的 Product Owner 结果查看。

### Local Mac / Terminal

在本规则有效期内按：

`TEMPORARILY UNAVAILABLE / DO NOT ASSUME LOCAL ACCESS`

任何当天任务不得把 `/Users/caroline/...` 本地路径作为必须可访问的执行前提。

### 4.1 Codex Cloud native PR publication verification

2026-09-15 已通过 `CLOUD-DRILL-001` 完成真实演练并远端核验。

验证成立的路径为：

`GitHub source snapshot → Codex Cloud checkout → controlled change → Cloud commit/work reference → native PR publication → GitHub PR review → Product Owner approval → merge`

正式证据：

`docs/project_control/gates/P0_2_visual_assets/cloud_pr_workflow_drill_2026-09-15.md`

关键边界：

- Cloud shell 内可没有可用于直接 `git push` 的 GitHub 凭据；
- `origin/main`、`git fetch`、`gh`、shell-level direct push 不作为 TEMP_CLOUD_ONLY_MODE 的必要 baseline；
- Codex Cloud native PR / `make_pr` 是当前已验证的远端 publication 路径；
- Codex task UI 未返回 PR number / URL 时，不得仅据此判断失败，必须回到 GitHub 远端事实核对；
- GitHub PR 的 base / head / changed files / diff 必须由 ChatGPT 或 Product Owner 独立核对后，才允许进入 merge；
- Product Owner-only merge / approval authority 不变。

`CLOUD-DRILL-001` 最终结果：`PASS / NATIVE PR PUBLICATION VERIFIED / PR #5 MERGED`。

该演练不占 D-###，也不构成 AO-03、AO-04、AO-05、AO-06、P0.2、P1 Wave 2 或 P0.3 的完成证据。

## 5. AO-03 temporary-mode rule

AO-03 可推进：

- Scene Fact 与 Shot Photography 分离；
- Scene / Costume / Prop / State / Variant Schema；
- DAY/NIGHT、门开/闭、壁炉状态等受控 State / Variant；
- Registry / Resolver 可读结构；
- validation tests。

正式对象至少包括：

- `CASTLE_ENTRANCE_OPEN_DOOR_DAY`
- `FIRST_HALL_FIREPLACE`

只允许结构化已有正式批准事实。

如正式 Scene Master 原图无法从云端取得，不得：

- 凭 Chat 记忆重新推断视觉细节；
- 重新生成替代 Scene Master；
- 将缺少原图核验的字段标记为 VERIFIED。

此类字段必须明确记录：

`SOURCE_ASSET_VALIDATION_PENDING`

## 6. AO-04 temporary-mode rule

AO-04 原则上应优先在纯云端阶段完整完成。

9 名 Character Derived Reference Sheet 必须依据 GitHub 当前 `CURRENT` Atomic Assets 自动生成。

必须记录：

- `derived_from Asset IDs`
- upstream versions
- dependency status

必须验证：

`DEPENDENCY_STALE`

不得由 Product Owner 人工重新挑选一套图片作为正式 Reference Sheet 的标准来源；Derived Reference Sheet 不得反向覆盖 Atomic Master 权威。

## 7. AO-05 temporary-mode rule

AO-05 验收核心不是“代码写完”，而是：

`Reference Package → actual image-production / generation environment`

建议状态语义：

- `ENGINEERING COMPLETE`：工程实现已完成，但尚未经过真实制图环境验证；
- `VALIDATION PASSED`：真实 handoff 成功，输入 Asset ID / version 可追踪；
- `COMPLETE / VERIFIED`：真实 handoff 稳定，且 Product Owner 不再需要例行逐张挑选 Reference。

如果纯云端环境无法完成最后一段真实交付，只能保持：

`ENGINEERING COMPLETE / VALIDATION PENDING`

不得为了进度提前判 COMPLETE。

## 8. AO-06 temporary-mode rule

AO-06 必须使用至少一个真实 Shot Spec，完整验证：

`Shot Spec → Reference Resolver → traceable Reference Package → Actual Production Use → USES_REFERENCE → Audit Trail`

必须同时满足：

- Shot → 可反查实际使用的 Asset IDs / versions；
- Asset → 可反查该 Shot / production use；
- 正式路径不依赖人工凭记忆挑图。

如缺少真实 generation/use 环节，只能保持：

`ENGINEERING COMPLETE / END-TO-END VALIDATION PENDING`

不得以模拟测试替代正式 end-to-end validation。

## 9. Blocked local asset rule

无 Mac 本身不自动构成 Blocker。

只有某项正式 DoD 明确依赖当前无法取得的 local-only asset 时，才登记：

`BLOCKED_LOCAL_ASSET`

禁止通过以下方式绕过：

- 重新生成缺失正式资产；
- 凭记忆重建文件；
- 建立 duplicate Asset / duplicate Version；
- 重新分配 Asset ID；
- 将模拟结果写成真实生产验证。

## 10. Local sync temporary exception

2026-09-16～2026-09-20：

`LOCAL_SYNC_DEFERRED / GITHUB_MAIN_CANONICAL`

期间 ChatGPT 对 GitHub 的正式写入不要求 Product Owner 当天执行本地 pull。

重新取得 Mac 后，在任何本地正式生产之前，必须先执行：

1. `git status`
2. GitHub connectivity preflight
3. `git pull --ff-only origin main`
4. local HEAD / remote main truth check

完成该同步前，禁止从旧 local working copy 继续正式生产。

## 11. Target cadence

- 2026-09-16：AO-03
- 2026-09-17：AO-04
- 2026-09-18：AO-05
- 2026-09-19：AO-06
- 2026-09-20：P0.2 Closeout Review

日期是执行目标，不是验收豁免。任何 AO 未达到 DoD 时必须停留在真实状态，不得为符合日期计划而提前 PASS。

## 12. Exit conditions

以下任一条件发生时退出本规则：

1. 2026-09-20 23:59 到期；
2. Product Owner 提前恢复稳定本地 Mac 使用，并明确结束临时模式；
3. AO-03～AO-06 全部完成且 P1 Wave 2 Resume Lock 正式解除。

退出后恢复 RC-015 正常路由与 RC-012 本地同步提醒规则；重新使用本地工程前必须先完成 GitHub → Local truth sync。
