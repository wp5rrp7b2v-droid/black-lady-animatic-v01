# P0.2-04｜AO-07｜GitHub Network Resilience / Recovery Method｜Progress V1

Status: `CLOSEOUT IN PROGRESS`

Date: `2026-09-14`

## 1. Purpose

本文件记录 AO-07 在正式完成前已经取得的真实技术证据。AO-07 的目标不是保证公网永不掉线，而是保证：

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

## 5. Formal lightweight recovery runbook

### 5.1 Preflight

在任何正式 pull / push / publication 前：

1. 确认当前仓库路径正确；
2. 检查 working tree，避免未识别的 tracked changes 与 publication 混在一起；
3. 通过 `git-proxy-auto ls-remote origin refs/heads/main` 验证 repo reachability；
4. 只有 reachability 通过后，再进行 pull / push；
5. publication 后以 remote `main` SHA 与本地 HEAD 比对作为最终 truth check。

### 5.2 Standard diagnosis order

遇到连接异常时，统一按以下顺序诊断，不跳步、不盲目重跑正式 ingest：

1. **DNS**：确认 `github.com` 可解析；
2. **HTTPS reachability**：确认 GitHub HTTPS 链路可达；
3. **Git remote**：确认 `origin` 指向 canonical repo；
4. **HTTP version**：优先使用 repo-local / command-level `HTTP/1.1` fallback；
5. **Proxy / VPN**：动态读取当前系统代理，禁止持久化临时端口；
6. **Credential**：仅在 reachability 正常但认证失败时检查 credential；
7. **Repository reachability**：再次执行 `ls-remote`；
8. **Publication**：仅在以上项正常后执行 pull / push。

### 5.3 PENDING_REMOTE_PUBLICATION

当本地正式事务已成功、但 GitHub 暂时不可达时：

- 保留本地正式 commit / ingest receipt；
- 状态仅可标记为 `PENDING_REMOTE_PUBLICATION`；
- 不得标记 `REMOTE VERIFIED`；
- 不得重新执行正式 ingest；
- 不得重新分配 Asset ID；
- 不得为同一正式结果创建第二套版本；
- 网络恢复后，从已有 commit / receipt 继续 publication；
- publication 后执行 remote SHA truth check；
- SHA 匹配后才退出 `PENDING_REMOTE_PUBLICATION` 并进入 `REMOTE VERIFIED`。

### 5.4 Push ACK loss

如果 push 返回网络错误、超时、unexpected disconnect 或类似 ACK 丢失症状：

1. 禁止立即重复正式 ingest；
2. 先查询 remote `main` SHA；
3. 若 remote SHA == local HEAD：视为 publication 已成功，只是 ACK 丢失；
4. 若 remote SHA != local HEAD：进入 `PENDING_REMOTE_PUBLICATION`，恢复连接后只重试 push；
5. 不因 ACK loss 重新写 Registry、重新分配 Asset ID 或重新生成正式资产。

### 5.5 Remote mismatch

若 remote SHA 与 local HEAD 不一致：

- 先确认是否存在预期之外的远端提交；
- 禁止 force push；
- 禁止覆盖远端 truth；
- 先 pull / fetch 并判定是否可 fast-forward；
- 如无法 fast-forward，停止 publication，进入人工审查；
- 在冲突解决前不得把状态写成 `REMOTE VERIFIED`。

## 6. Controlled failure → recovery evidence

AO-07 的受控恢复证据采用“已发生的真实 transient failure + 后续恢复成功”作为等价可复现证据，不再人为破坏当前已恢复的网络环境。

已知真实失败症状包括：

- 443 timeout；
- `Empty reply from server`；
- HTTP/2 framing error；
- `unexpected disconnect`。

后续恢复链已经完成：

- 采用动态 proxy helper；
- 使用 HTTP/1.1 fallback；
- `ls-remote` PASS；
- `pull --ff-only` PASS；
- `push` PASS；
- remote SHA == local HEAD；
- AO-02 migration publication 完成 `REMOTE VERIFIED`；
- migration idempotency 已证明重复执行返回 `ALREADY_APPLIED / NO CHANGE`。

因此，AO-07 的 failure → recovery 核心验收点已经由真实故障恢复链覆盖：

`transient network failure → no re-ingest → no duplicate Asset ID → connectivity recovery → publication → SHA verification`

## 7. Closeout assessment

截至 2026-09-14，AO-07 Definition of Done 技术项已满足：

- connectivity preflight：SATISFIED；
- standard diagnostic order：SATISFIED；
- HTTP/1.1 fallback：SATISFIED；
- dynamic proxy recovery：SATISFIED；
- retry idempotency / no duplicate ingest：SATISFIED；
- `PENDING_REMOTE_PUBLICATION` workflow：SATISFIED；
- ACK loss / remote mismatch handling：SATISFIED；
- controlled failure → recovery evidence：SATISFIED BY REAL INCIDENT RECOVERY EVIDENCE；
- lightweight recovery runbook：SATISFIED。

Remaining governance step:

- Product Owner explicit approval in Chat；
- after approval, cross-file status must be updated to `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED` and `RISK-001` downgraded to controlled risk.

## 8. Current conclusion

当前正式建议状态：

`READY_FOR_APPROVAL / TECHNICALLY VERIFIED`

在 Product Owner 明确批准前，不得写成 `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`。
