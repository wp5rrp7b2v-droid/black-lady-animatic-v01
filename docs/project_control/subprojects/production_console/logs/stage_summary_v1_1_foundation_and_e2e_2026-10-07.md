# Black Lady Local Production Console
## V1.1 Foundation + End-to-End Qualification｜阶段性总结与落档

**Date:** 2026-10-07  
**Subproject:** BLACK_LADY_PRODUCTION_CONSOLE  
**Parent Project:** BLACK-LADY-001 / 《诡舍·黑衣夫人》  
**Status:** V1.1 ENGINEERING FOUNDATION + E2E QUALIFICATION COMPLETE / PRODUCTION ADOPTION NOT AUTHORIZED

---

## 1. 本阶段原始目标

Production Console 子项目的原始意图，不是单独增加一个“登记后台”，而是逐步把 Story Shot 的生产链路统一到一个可操作 UI 中：

**Director Design → Scene Reference → Bundle → Work 制图 → Product Owner 审核 → Exact Binary Verification → Canonical Publication → Story Shot Registration → Registration Verification → Project Control Closeout**

当前正式 Story Shot 流程在本阶段始终保持不变。Console 只作为工具与工作流资格验证子项目，不是 SSOT，也没有获得 Production Adoption 授权。

---

## 2. 本阶段已经取得的成果

### 2.1 V1.0 Fixed Install 基础能力已建立

已完成并验证：

- 本地固定安装与启动；
- Drive OAuth / Picker；
- GitHub staging；
- Phase E 端到端 TEST_SHOT；
- 本地 UI、Drive、GitHub 之间的最小可运行链路；
- 私有 OAuth / runtime 数据与 GitHub 仓库隔离。

这些成果证明：本地 Production Console 作为独立工程工具是可运行的。

### 2.2 V1.1 Workflow Engine 已实现

V1.1 建立并验证了完整状态机：

**DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT**

已实现并验证的关键能力包括：

- Project Control 自动解析当前 Shot / Design Package；
- Bundle / Run / Artifact / Reference metadata 自动解析；
- 资格模式下的 Preflight；
- Candidate PNG drag-and-drop / file picker intake；
- Candidate 上传幂等保护；
- immutable candidate identity：
  - shot_id
  - candidate_id
  - Drive file ID
  - SHA-256
  - byte size
  - dimensions
- Exact Binary verification；
- qualification-only publication / registration / lock / closeout；
- registration failure 后不重复 publication；
- GitHub qualification evidence + Drive binary 的 External Recovery；
- local Session 丢失后的 authoritative reconstruction；
- stale localStorage 自动恢复；
- Operator View / Diagnostics 分层；
- Project Control freshness 检查；
- qualification path 与 formal main / Story Shot formal records 隔离。

### 2.3 Q4 Formal V1.1 E2E Qualification 已通过

Controlled qualification：

- Session: `V11_Q4_E2E_001`
- Shot: `TEST_UI_V11_Q4_001`
- Branch: `test/local-console-v1-1-e2e-v001`

Final records:

- Publication blob: `4b5981cfdf0971c5448dc52cf3f0b01288cd38a0`
- Registration blob: `47c6e35ef926d73a9c48e619b049f2d38dc6b559`
- Lock blob: `c648edce91863424a9633be34190e82e00f54476`
- Closeout blob: `86d5238b506a108cb2fb1f95d2071ab69f3817f7`
- Qualification branch head at Q4 closeout: `9c6ca33f9f5bede9cc8fdf5074e4062b87321595`

Q4 证明了完整状态链、候选身份绑定、Drive binary verification、publication→registration→lock→closeout binding 和 recovery 机制可以工作。

### 2.4 N26 Shadow End-to-End 已通过

为避免仅在 TEST_SHOT 上成立，本阶段进一步用已经正式完成的真实 Story Shot N26 做 qualification-only shadow rehearsal。

Session:

- `N26_20261007_003`
- Source Shot: `N26`
- Bundle: `N26_REFERENCE_DELIVERY_BUNDLE_V002`
- Run ID: `37553891715`
- Artifact ID: `11453927794`
- Artifact digest: `sha256:f7fdb72eb39aeea743dfd61707a817d5fae8cba34a0b924210985ecf34a3dd10`
- Reference Count: 5

Test candidate binary:

- Drive file ID: `1zjVpuKoJAIEjD6u9xSPFqB-YGDQgJ0U7`
- SHA-256: `8dcd5f5449ad6429f45e7b4f59ce15bfd574eeb8aa45a83d4e4132df3cf436d9`
- Bytes: `2,504,586`
- Dimensions: `941 × 1672`

该 binary 与正式 N26 canonical binary exact match。

Qualification records:

- Publication blob: `5d495f2786bc48d9b56e3fd4586d9adfec6b5d82`
- Registration blob: `906401b96333266a7256031f076e0ce923b920d8`
- Lock blob: `4f3316ab521a542a665a04667d37fee7ddf209fb`
- Closeout blob: `78c774f94603eca787124dbfbbb8b9c9f88eb3ca`
- Final qualification branch head: `173cf6172b4bb06102b9a605cb85225d5cbbfdcd`

Formal safety after shadow E2E:

- Formal Story Shot SOP blob unchanged: `b1751704fe98c866d79633fb7c2c84c9a70f8e9e`
- Story Shot Index blob unchanged: `aca511a8db47bff458682de7db59101195e62206`
- Story Shot Index count unchanged: 32
- N26 canonical Git blob unchanged: `a5ce429689a99437773385e25b9813745e380f74`
- Parent Project Control remains R337 / blob `6895891002447cabdfba7f3771a77696c36845eb`

结论：真实 Story Shot 数据可以通过 qualification-only Console 完整跑通，同时不污染正式 N26。

---

## 3. 本阶段暴露并修复的重要工程问题

本阶段的价值不仅在于“跑通”，也在于真实测试暴露了此前未发现的问题：

1. **Closed-shot resolver compatibility**
   - N26 的正式 Bundle metadata 存在于 nested `formal_build`；
   - 原 resolver 只读取 flattened fields，导致真实 N26 被误报 NOT READY；
   - 已修复并增加 regression test，CI PASS。

2. **Drive folder / Session isolation**
   - Preflight 原本只检查 Drive folder 是否存在；
   - 后增加 `drive_folder_matches_session`，避免测试 Session 写入错误目录；
   - fail-closed 行为已验证。

3. **Candidate upload idempotency**
   - 已修复重复 intake 可能产生重复 Drive binary 的风险。

4. **True External Recovery**
   - 已从“本地 Session 持久化”推进到“本地 Session 缺失时，依据 GitHub qualification evidence + Drive binary 重建”。

5. **Operator freshness**
   - 已修复 UI 可能在没有最新 main SHA 的情况下误显示 CURRENT 的问题。

这些都属于实际工程成果，后续即使重新设计 UI，也可以继续复用。

---

## 4. 当前仍存在的已知问题

以下问题不否定 V1.1 workflow engine 的技术资格通过，但必须保留：

- Session ID 自动生成，而 Drive folder 仍需人工创建 / 重新绑定同名目录；
- PREFLIGHT HTTP action 成功时，顶部 action banner 可能显示 `PREFLIGHT PASS`，即使 persisted status 实际为 `PREFLIGHT_FAILED`；
- launcher 曾出现 Flask 已运行但 health check 报失败的 false-negative，根因尚未独立闭环；
- N26 Shadow E2E 使用 Console 默认 `CANDIDATE_01` 作为 test candidate ID，而正式 N26 来源是 Candidate 03；binary identity exact match，因此不构成 formal identity contamination，但说明 candidate naming UX 仍需重新设计。

---

## 5. 本阶段最重要的产品结论

### 5.1 工程结论

**V1.1 作为 workflow engine / qualification / recovery backend，是成功的。**

它已经证明：

- 状态链可以运行；
- binary identity 可以锁定；
- GitHub / Drive evidence 可以交叉验证；
- recovery 可以不依赖单一本地 Session；
- qualification 与正式 Story Shot 数据可以隔离；
- 真实 N26 可以完成 shadow E2E。

### 5.2 产品结论

**V1.1 当前 UI 不适合作为 Product Owner 的日常生产入口。**

原因不是底层流程失败，而是目前把大量本应属于 Chat / backend 的内部流程暴露给 Product Owner：

- Session ID
- Drive folder binding
- Preflight
- Publication
- Registration
- Lock
- Closeout

原正式流程中，Product Owner 在制图完成后主要只需要：

1. 批准图片；
2. 下载并上传一次文件。

因此，如果 Console 只是把“上传 GitHub”替换为“上传 Console / Drive”，同时增加更多操作步骤，就没有产生 Product Owner 侧的净收益。

这次 N26 Shadow E2E 的最大产品发现是：

> **后台工作流已经具备继续发展的基础，但当前 UI 产品边界偏离了最初目标。**

---

## 6. 原始产品意图重新确认

Production Console 的原始方向应恢复为：

> **从镜头设计开始，到制图、审核、批准、正式落档，主要工作在同一个 UI Workspace 中完成。**

未来统一 Workspace 应覆盖：

**Director Design → Scene Reference → Bundle → Work Generation → Candidate Review / Modification → PO Approval → Formal Closeout**

Product Owner 正常不应直接操作：

- Session ID；
- Run ID / Artifact ID；
- SHA；
- Drive folder；
- Preflight；
- Publish；
- Register；
- Lock；
- Closeout。

这些仍然保留为后台 state / safety / audit mechanism，并在 Diagnostics 中可查看和恢复。

---

## 7. 对下一阶段的建议边界

本阶段不进入 Production Adoption。

### 保留

- V1.0 固定安装基础；
- V1.1 state machine；
- Project Control resolver；
- Drive / GitHub integration；
- exact binary verification；
- immutable identity；
- qualification publication / registration / lock / closeout；
- external recovery；
- audit / diagnostics；
- formal-safety boundary。

### 下一阶段需要重新设计，而不是继续堆按钮

建议后续单独定义：

**Production Console V2｜Unified Story Shot Workspace**

产品验收标准应从“8 个状态都能手工点击”改为：

> **一个 Story Shot 从设计开始，到正式落档结束，Product Owner 不需要在 Chat / Work / Downloads / GitHub / Drive / Console 多个界面之间反复切换来维护流程状态。**

真正需要解决的核心桥接问题是：

**UI ↔ Chat design/decision ↔ GitHub Actions Bundle ↔ Work generation ↔ Candidate return ↔ PO review ↔ backend closeout**

在该架构未明确前，不启动 Q5 Production Adoption。

---

## 8. 阶段性 Closeout Decision

**V1.1 Foundation + Qualification Stage: CLOSED / PASS**

同时：

- Production Adoption: **NOT STARTED**
- Q5: **NOT AUTHORIZED**
- 正式 Story Shot SOP: **UNCHANGED**
- 当前 Console: **保留为已验证 workflow engine / diagnostics / recovery foundation**
- 下一阶段：**仅在 Product Owner 明确授权后启动 V2 Unified Story Shot Workspace 的产品设计**

本阶段不是失败。

它完成了底层基础设施、状态机、身份校验、外部恢复和真实 N26 Shadow E2E；同时通过真实使用明确发现：**后端能力成立，但 Product Owner 操作层需要重新设计。** 这个结论本身就是本阶段必须保留的产品成果。
