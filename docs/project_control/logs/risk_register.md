# Risk Register｜BLACK-LADY-001

本文件记录会影响项目连续执行、资产安全或交付稳定性的当前风险。风险记录不等于 Blocker；只有当风险已经实际阻止当前任务继续执行时，才同步升级为 Project State blocker。

| ID | 日期 | 风险 | 影响 | 当前缓解 | 状态 |
|---|---|---|---|---|---|
| RISK-003 | 2026-10-02 | N21 多人物 Story Shot 已完成 Candidate 08 新一轮实证。V006 使用已批准的 Threshold Environment Reference + Crowd Body/Wardrobe Reference；C08 显示成年人比例、普通现代服装、无包具控制与总体向古堡深处的运动方向明显改善，且未被 Human Reference 强制成四人阵容。但群体仍呈较规整的纵深队列 / 中央运动轴，环境重新漂移为高拱、巨大双门、强消失点的宏伟哥特式建筑展示，未知空间的遮挡、威胁与不确定性不足。当前不能把根因归结为 Human Reference 失败，也不能认定为模型整体退化。 | 若继续无差别生成，可能在已经改善的人体/服装上反复返工，同时持续出现组织化 crowd blocking、中央轴构图和 monumental environment drift，延长 N21 收敛时间。 | 保留 V006 Human Body/Wardrobe 与人物前进方向的成功结论；下一轮不得重开已改善的人体比例规则。Candidate 09 前只允许先做窄范围策略复盘，目标限定为：打散中央轴与规整队列、削弱宏伟对称门户、增加局部遮挡与未知空间；Candidate 09 仍需独立 PO 授权。 2026-10-02 Product Owner 明确决定暂停 N21，先完成 N22–N27 后再评估如何处理 N21；因此本风险继续保留全部既有证据，但仅作用于 N21，不再阻塞后续 Story Shot 制图。Candidate 09 仍未授权。 | **RESOLVED / CLOSED 2026-10-03** |
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


## 2026-10-02 Hold Scope Decision

- Product Owner explicitly placed `N21` on HOLD.
- This is a production-priority decision, not evidence that `RISK-003` is solved.
- Existing Candidate 08 findings remain valid baseline evidence.
- `RISK-003` is now N21-scoped and does not block `N22 → N23 → N24 → A06 → N25 → N26 → N27`.
- `N21 Candidate 09` remains NOT AUTHORIZED until Product Owner explicitly reopens N21.

## Risk Status Delta｜2026-10-03 EOD

### RISK-003｜N21 multi-person Story Shot

Status remains:

`ACTIVE / N21-SCOPED / DEFERRED BY PRODUCT OWNER / CURRENTLY NON-BLOCKING OUTSIDE N21`

Update:

- `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001` is now formally CLOSED with four exact-verified canonical orientations: FRONT / LEFT_PROFILE / REAR_3Q / BACK.
- This materially improves reusable anonymous-Guest identity continuity inputs for future N21 work.
- It does **not** establish that N21's remaining crowd-blocking / central-axis / monumental-environment issues are solved.
- Existing Candidate 08 evidence and N21-specific mitigation remain valid.
- Before any new N21 candidate, perform a narrow re-entry strategy review using the completed Generic Guest Core Set as an available controlled identity input; do not reopen already-resolved body/wardrobe rules without new evidence.
- No new N21 candidate is authorized by this risk update.

### N23 dependency update

N23 Candidate 02 was previously paused pending Generic Guest Crowd Core Set progress.

That dependency is now satisfied because V001 is formally CLOSED.

N23 Candidate 02 remains:

`PAUSED / PRODUCT OWNER RE-ENTRY AUTHORIZATION REQUIRED`

This is no longer an asset-readiness blocker; it is now a governance/authorization gate.


## 2026-10-03 RISK-003 Final Closure

This section supersedes older current-state wording that described N21 as HOLD or Candidate 09 as not authorized. Those earlier entries remain historical evidence only.

- N21 Candidate 09: PRODUCT OWNER APPROVED.
- Exact-binary intake: PASS.
- Canonical exact-blob publication: PASS.
- Story Shot registration: COMPLETE.
- Registration verification: PASS.
- N21: FORMALLY CLOSED / CANONICAL / REGISTERED / VERIFIED.
- RISK-003: RESOLVED / CLOSED 2026-10-03.
- No N21 production blocker remains.
- N24 is the next unstarted Story Shot node.

Closure authority: docs/project_control/gates/P0_3_video_pipeline/p0_3_daily_closeout_2026-10-03.md
