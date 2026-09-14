# P0.2-04｜AO-07｜GitHub Network Resilience / Recovery Method｜Progress V1

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Date: `2026-09-14`

## 1. Purpose

AO-07 已正式完成。目标不是保证公网永不掉线，而是保证：

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

随后 AO-02 的正式 migration publication 也通过同一网络路径完成并达到 `REMOTE_VERIFIED`。

## 4. What is demonstrated

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

1. DNS：确认 `github.com` 可解析；
2. HTTPS reachability：确认 GitHub HTTPS 链路可达；
3. Git remote：确认 `origin` 指向 canonical repo；
4. HTTP version：优先使用 repo-local / command-level `HTTP/1.1` fallback；
5. Proxy / VPN：动态读取当前系统代理，禁止持久化临时端口；
6. Credential：仅在 reachability 正常但认证失败时检查 credential；
7. Repository reachability：再次执行 `ls-remote`；
8. Publication：仅在以上项正常后执行 pull / push。

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

AO-07 的受控恢复证据采用已发生的真实 transient failure + 后续恢复成功作为等价可复现证据，不再人为破坏当前已恢复的网络环境。

已知真实失败症状包括：443 timeout、`Empty reply from server`、HTTP/2 framing error、`unexpected disconnect`。

后续恢复链：

`transient network failure → dynamic proxy helper + HTTP/1.1 → ls-remote PASS → pull PASS → push PASS → remote SHA == local HEAD → AO-02 publication REMOTE_VERIFIED`

同时 migration idempotency 已证明重复执行返回 `ALREADY_APPLIED / NO CHANGE`，满足 no re-ingest / no duplicate Asset ID 的核心恢复要求。

## 7. Closeout assessment

截至 2026-09-14，AO-07 Definition of Done 全部满足：

- connectivity preflight：SATISFIED；
- standard diagnostic order：SATISFIED；
- HTTP/1.1 fallback：SATISFIED；
- dynamic proxy recovery：SATISFIED；
- retry idempotency / no duplicate ingest：SATISFIED；
- `PENDING_REMOTE_PUBLICATION` workflow：SATISFIED；
- ACK loss / remote mismatch handling：SATISFIED；
- controlled failure → recovery evidence：SATISFIED BY REAL INCIDENT RECOVERY EVIDENCE；
- lightweight recovery runbook：SATISFIED；
- Product Owner explicit approval：APPROVED 2026-09-14。

## 8. Final conclusion

`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

RISK-001 可从 OPEN 降级为 `CONTROLLED / MITIGATION VERIFIED`。该风险不表示公网故障不会再发生，而表示已有经过真实验证、可执行且不破坏资产/Registry一致性的恢复方法。
