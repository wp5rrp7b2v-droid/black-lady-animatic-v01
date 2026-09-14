# P0.2-04｜AO-07｜GitHub Network Resilience / Recovery Method｜Progress V1

Status: `PARTIAL / CONNECTIVITY METHOD TECHNICALLY VERIFIED / FINAL CLOSEOUT PENDING`

Date: `2026-09-14`

## 1. Purpose

本文件记录 AO-07 在正式完成前已经取得的真实技术证据。它不等于 AO-07 `COMPLETE / VERIFIED`，也不解除 `RISK-001` 或 P1 Wave 2 HOLD。

AO-07 的目标不是保证公网永不掉线，而是保证：

`GitHub transient failure ≠ asset corruption / duplicate ingest / duplicate Asset ID / project-state divergence`

## 2. Dynamic Git helper adopted

当前《黑衣夫人》仓库复用已存在的动态 Git helper：

`$HOME/.local/bin/git-proxy-auto`

该 helper 的已验证行为：

- 每次运行动态读取 macOS `scutil --proxy`；
- 优先识别当前 HTTPS / HTTP proxy，不持久化动态代理端口；
- Git 命令级使用 `http.version=HTTP/1.1`；
- push 时只临时使用需要的 `http.postBuffer`，不把动态值写入 repo/global config；
- push 返回异常时以远端 `main` SHA 与本地 HEAD 对比判断是否属于 ACK loss，避免盲目重复 push。

Black Lady repo 当前原则：

- 保留 repo-local `http.version=HTTP/1.1`；
- 不持久化 `http.proxy` / `https.proxy`；
- 不持久化动态 proxy port；
- 不依赖固定 `postBuffer` 作为长期网络方案；
- GitHub 网络操作优先经 `git-proxy-auto` 执行。

## 3. Real connectivity verification｜2026-09-14

本轮检测到的 macOS proxy：

`http://127.0.0.1:15236`

真实验证链：

1. `git-proxy-auto ls-remote origin refs/heads/main` → PASS；
2. `git-proxy-auto pull --ff-only origin main` → PASS / `Already up to date`；
3. `git-proxy-auto push origin main` → PASS / `PUSH_STATUS=SUCCESS`；
4. Local HEAD 与 remote `refs/heads/main` SHA 比对 → MATCH。

该轮最终技术状态：

`SUCCESS`

随后 AO-02 的正式 migration publication 也通过同一网络路径完成，最终 Terminal 检查返回：

`FINAL_STATUS=REMOTE_VERIFIED`

这进一步证明：本地正式事务完成后，可以将“数据事务”和“远端 publication”分离，并在网络可用时安全完成发布与 SHA 核验，而不需要重新执行 migration。

## 4. What is already demonstrated

当前已经有真实证据支持：

- 动态代理端口可被自动识别；
- `ls-remote / pull / push` 可通过统一 helper 执行；
- HTTP/1.1 可作为当前 GitHub HTTPS 链路的稳定 fallback；
- Registry migration 与 Git publication 可以分离；
- migration 本身具备 idempotency，二次执行返回 `ALREADY_APPLIED / NO CHANGE`；
- 远端 publication 可通过最终 SHA truth check 独立确认；
- 临时网络问题不要求重新分配 Asset ID 或重新执行正式 migration。

## 5. Remaining AO-07 Definition of Done

AO-07 尚未正式完成，至少仍需：

- 将 connectivity preflight 与标准诊断顺序写成正式轻量 Runbook；
- 明确 DNS / HTTPS / remote / HTTP version / proxy / VPN / credential / repository reachability 的统一诊断顺序；
- 把 `PENDING_REMOTE_PUBLICATION` 的进入、退出和恢复发布规则写成可执行流程；
- 对 push ACK loss / remote mismatch 等分支写出明确处理规则；
- 至少完成一次受控 failure → recovery 验证，或以等价、可复现证据满足该项验收；
- 完成 AO-07 cross-file closeout；
- 由 Product Owner 最终批准 AO-07。

因此当前不得将 AO-07 写成 `COMPLETE / VERIFIED`。

## 6. Current conclusion

当前正式建议状态：

`PARTIAL / CONNECTIVITY METHOD TECHNICALLY VERIFIED / RUNBOOK + FINAL CLOSEOUT PENDING`

`RISK-001` 仍保持 OPEN，直到 AO-07 全部 Definition of Done 满足并经 Product Owner 批准后再正式降级。
