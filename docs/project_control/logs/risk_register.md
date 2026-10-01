# Risk Register｜BLACK-LADY-001

本文件记录会影响项目连续执行、资产安全或交付稳定性的当前风险。风险记录不等于 Blocker；只有当风险已经实际阻止当前任务继续执行时，才同步升级为 Project State blocker。

| ID | 日期 | 风险 | 影响 | 当前缓解 | 状态 |
|---|---|---|---|---|---|
| RISK-003 | 2026-09-30 | N21 多人物 Story Shot 连续三轮生成出现可重复的质量权衡：群像构图、未知/危险氛围、角色身份连续性与身体姿态无法同时稳定保持。C01→C03 中每次改善一部分维度时，其他维度出现明显退化。当前不能把根因正式认定为“模型降智/模型退化”。 | 继续直接生成仍可能在氛围、人物风格、群像自然度与身体表现之间发生质量交换。 | 2026-10-01 已批准并锁定 Scene Reference V0.4：单帧职责降为门槛转换 + 未知空间氛围；16 人不再要求单帧计数；人物视觉风格连续性升级为硬 Gate；V002 Bundle 创意职责被取代，下一步先设计 V003 Bundle，Candidate 04 仍暂停。 | **ACTIVE / MITIGATION DESIGN LOCKED / CANDIDATE EVIDENCE STILL REQUIRED / ROOT CAUSE NOT PROVEN** |
| RISK-002 | 2026-09-18 | Image-generation service 不返回独立的 consumed-input SHA / cryptographic receipt。当前只能证明送入 generation call 前的正式 reference bytes、Asset IDs、SHA 与实际 reference file paths，无法从生成服务自身取得“最终实际消费输入”的密码学回执。 | 严格端到端 provenance 存在最后一跳审计缺口；未来若发生 identity drift / service-side caching / preprocessing 异常，无法仅凭服务回执证明模型内部消费的原始输入字节。 | AO-05 已建立多层证据链：GitHub canonical Asset SHA → GitHub Actions canonical-byte verification → artifact ZIP digest → Work 独立 SHA verification → actual 4-reference generation call；RUN A / RUN B 输入集合一致且均成功。要求所有正式生成继续记录 Asset IDs、SHA、调用文件路径/顺序、时间与 output/proof identifier。 | **ACCEPTED / NON-BLOCKING / DEFERRED IMPROVEMENT** |
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

## RISK-002 Improvement Trigger

RISK-002 当前不阻塞生产，也不推翻 AO-05 验收。未来出现以下任一能力时重新开启改进：

1. image-production API 返回 uploaded-file digest / input digest；
2. generation request 返回 immutable request manifest；
3. service-side input file ID 可与上传 bytes 的 SHA256 做可验证绑定；
4. 平台提供等价的 cryptographic consumed-input receipt。

届时将目标证据链升级为：

`Asset SHA → Delivery SHA → Service Input Receipt SHA / immutable file ID → Output ID`。


## RISK-003 Exit Criteria

RISK-003 解除当前 hard-blocker 状态，需要满足：

1. N21 简化后的单帧叙事职责经 Director Review / Product Owner 明确锁定；
2. 新职责不再要求单帧同时证明完整 16 人、自然群像、宁/君高身份一致性、复杂动作与强氛围；
3. 确认现有 V002 Bundle 是否仍适配；若不适配则先做受控 Bundle revision；
4. 至少一张 N21 candidate 在空间、氛围、人物结构/姿态与连续性上达到可接受平衡；
5. Product Owner 明确批准后，RISK-003 才可从 hard blocker 降级。

不得将“模型降智”记录为已证实 root cause，除非未来有独立、可复现的跨任务证据。
