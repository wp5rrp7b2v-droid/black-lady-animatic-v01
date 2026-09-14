# Risk Register｜BLACK-LADY-001

本文件记录会影响项目连续执行、资产安全或交付稳定性的当前风险。风险记录不等于 Blocker；只有当风险已经实际阻止当前任务继续执行时，才同步升级为 Project State blocker。

| ID | 日期 | 风险 | 影响 | 当前缓解 | 状态 |
|---|---|---|---|---|---|
| RISK-001 | 2026-09-13 | GitHub 网络连接不稳定：项目近期多次出现 `443 timeout`、`Empty reply from server`、HTTP/2 framing error、`unexpected disconnect` 等，导致 pull / fetch / push / Automatic Ingest publication 可能随机失败。 | Project Control 同步、Automatic Ingest、Codex Git 操作与正式资产发布都依赖 GitHub；若没有稳定恢复方案，可能出现“本地已完成但远端未发布”、重复执行、版本分叉或误判完成状态。 | 2026-09-14 已完成并验证 AO-07：动态 helper `$HOME/.local/bin/git-proxy-auto` 可动态读取 macOS proxy、不持久化动态端口，命令级使用 HTTP/1.1；真实完成 `ls-remote / pull / push / local-vs-remote SHA match`；AO-02 migration publication 通过该链路达到 `REMOTE_VERIFIED`，migration 二次执行返回 `ALREADY_APPLIED / NO CHANGE`。正式 lightweight recovery runbook、`PENDING_REMOTE_PUBLICATION`、ACK loss / remote mismatch、failure→recovery 规则均已落档并经 Product Owner 批准。 | **CONTROLLED / MITIGATION VERIFIED / AO-07 COMPLETE** |

## RISK-001 Exit Criteria

RISK-001 的 OPEN exit criteria 已于 2026-09-14 满足：

1. GitHub connectivity preflight：已建立；
2. 标准诊断顺序：DNS / HTTPS / Git remote / HTTP version / proxy / VPN / credential / repository reachability — 已锁定；
3. HTTP/2 异常安全 fallback 到 HTTP/1.1 — 已验证；
4. Safe retry：失败不重复写 Registry、分配 Asset ID 或 ingest — 已验证并形成规则；
5. Offline-safe behavior：`PENDING_REMOTE_PUBLICATION` — 已建立；
6. Recovery procedure：从已有 commit / receipt 继续发布 — 已建立；
7. failure→recovery：由真实 transient failure → recovery 证据满足；
8. lightweight runbook：已完成；
9. Product Owner approval：2026-09-14 已明确批准 AO-07。

## 2026-09-14 Final Closeout

正式状态：

`CONTROLLED / MITIGATION VERIFIED / AO-07 COMPLETE`

该状态不是“GitHub 网络以后不会再发生故障”。它表示：

- 网络故障已不再是当前 hard blocker；
- 项目具备经过真实验证的恢复路径；
- 网络失败不会要求重新 ingest 或重新分配 Asset ID；
- 未发布结果有明确 `PENDING_REMOTE_PUBLICATION` 状态；
- publication 最终以 remote SHA truth check 判定；
- ACK loss 与 remote mismatch 有明确分支处理。

AO-07 completion evidence：

`gates/P0_2_visual_assets/ao07_github_network_resilience_progress_v1.md`

风险控制目标继续保持：

`GitHub transient failure ≠ asset corruption / duplicate ingest / project-state divergence`。
