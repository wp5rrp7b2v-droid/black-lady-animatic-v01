# Risk Register｜BLACK-LADY-001

本文件记录会影响项目连续执行、资产安全或交付稳定性的当前风险。风险记录不等于 Blocker；只有当风险已经实际阻止当前任务继续执行时，才同步升级为 Project State blocker。

| ID | 日期 | 风险 | 影响 | 当前缓解 | 状态 |
|---|---|---|---|---|---|
| RISK-001 | 2026-09-13 | GitHub 网络连接不稳定：项目近期多次出现 `443 timeout`、`Empty reply from server`、HTTP/2 framing error、`unexpected disconnect` 等，导致 pull / fetch / push / Automatic Ingest publication 可能随机失败。 | Project Control 同步、Automatic Ingest、Codex Git 操作与正式资产发布都依赖 GitHub；若没有稳定恢复方案，可能出现“本地已完成但远端未发布”、重复执行、版本分叉或误判完成状态。 | 2026-09-14 已真实验证动态 helper `$HOME/.local/bin/git-proxy-auto`：可动态读取当前 macOS proxy、不持久化动态端口，命令级使用 HTTP/1.1，并完成 `ls-remote / pull / push / local-vs-remote SHA match`。AO-02 正式 migration publication 亦通过该链路达到 `REMOTE_VERIFIED`，同时 migration 二次执行返回 `ALREADY_APPLIED / NO CHANGE`，证明数据事务与远端 publication 可安全分离。当前仍需 AO-07 正式 Runbook、`PENDING_REMOTE_PUBLICATION` 恢复规则、受控 failure→recovery 验证与最终 PO 审批。进展证据：`gates/P0_2_visual_assets/ao07_github_network_resilience_progress_v1.md`。 | **OPEN / MITIGATION TECHNICALLY VERIFIED / AO-07 RUNBOOK + FINAL CLOSEOUT PENDING** |

## RISK-001 Exit Criteria

RISK-001 只有在 AO-07 完成并验证后才能从 `OPEN` 降级。

AO-07 至少需要形成：

1. GitHub connectivity preflight：在 pull / ingest / push 前快速判断 GitHub 是否可用；
2. 标准诊断顺序：DNS / HTTPS / Git remote / HTTP version / proxy / VPN / credential / repository reachability；
3. 自动或半自动 fallback：已知 HTTP/2 异常时可安全切换 HTTP/1.1；必要时识别并处理变化的代理端口；
4. Safe retry：push/pull 失败时不得重复写 Registry、重复分配 Asset ID 或制造重复 commit；
5. Offline-safe behavior：GitHub 不可用时保留本地已完成结果与明确 `PENDING_REMOTE_PUBLICATION` 状态，不把远端未成功的任务标记为 `REMOTE VERIFIED`；
6. Recovery procedure：网络恢复后能从已有 commit / receipt 继续发布，而不是重跑正式 ingest；
7. 至少一次受控故障/恢复测试，证明方案可执行；
8. 将操作方法写成轻量 runbook，供 Chat / Codex / Product Owner 后续统一使用。

## 2026-09-14 Progress Note

以下 AO-07 能力已获得真实技术证据，但尚不构成正式 Exit：

- 动态代理发现：PASS；
- HTTP/1.1 command-level fallback：PASS；
- `ls-remote`：PASS；
- `pull --ff-only`：PASS；
- `push`：PASS；
- Local HEAD vs remote main SHA truth check：PASS；
- AO-02 publication 经同一链路 `REMOTE_VERIFIED`：PASS；
- AO-02 migration idempotency：`ALREADY_APPLIED / NO CHANGE`。

因此当前风险已具备一套**技术上有效的缓解路径**，但正式风险状态仍保持 `OPEN`，直到 AO-07 剩余 Definition of Done 与 Product Owner 审批完成。

风险解决目标不是保证公网永不掉线，而是确保：

`GitHub transient failure ≠ asset corruption / duplicate ingest / project-state divergence`。