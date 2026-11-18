# 《诡舍·黑衣夫人》｜P02 C03/C05 V002｜Work 正式定向整改交接

日期：2026-11-18
状态：**DIRECTOR REPAIR V002 / REFERENCE BUNDLES 2/2 PASS / WORK CANDIDATE_02 PENDING / PO VISUAL APPROVAL NOT GRANTED**

## 事实与授权
PO 明确否决上一批 C03/C05 Candidate_01：人物面对镜头、C05 重复站姿神情、顶部额外暖色灯违反 D02 空间；要求“继续”定向整改。原 V001 Reference Bundle 技术 PASS 历史有效，候选图视觉 FAIL 也有效。

已正式复核 GitHub Actions V002：
- C03：Run **44236746325**，`completed/success`，Job **134574604265**，日志 `PASS: 4/4 exact canonical reference binaries verified` / `GENERATION_ALLOWED=TRUE`，Artifact **14397458368**，6,866,228 bytes，上传 ZIP SHA-256 `96f4194ade2bfc707e90c496c0f80cbe7296e94787e1e0b32886d15ade1eee86`。链接：https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44236746325/artifacts/14397458368
- C05：Run **44236779206**，`completed/success`，Job **134574710824**，日志 `PASS: 4/4 exact canonical reference binaries verified` / `GENERATION_ALLOWED=TRUE`，Artifact **14397347522**，6,866,522 bytes，上传 ZIP SHA-256 `0547585fc0dc94db2e31c215447ce8b7165a436fd533dbc84e3e210a3cf1a56b`。链接：https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44236779206/artifacts/14397347522

Spec：
- `production/bundle_specs/OPENING_P02_C03_CONTRACT_CONTINUITY_REFERENCE_DELIVERY_BUNDLE_V002.json`
- `production/bundle_specs/OPENING_P02_C05_CONTRACT_CONTINUITY_REFERENCE_DELIVERY_BUNDLE_V002.json`

两份 Bundle 均为相同四份合法正式参考：`OPENING_P02_D02`（诡舍三楼空间与照明），`OPENING_P02_D03`（同一木门结构与旧血迹）、`AST_IMG_000057`（君鹭远身份）、`AST_IMG_000019`（君鹭远右后 3/4 姿态辅助）。本次增加 D02 是为阻止新增与三楼设计不符的顶灯；没有新增 Scene Master。完整拒审报告：`OPENING_P02_C03_C05_PO_REJECTION_AND_V002_REDESIGN_2026-11-18.md`。

## Work 实施

Work 读取上述两份 GitHub Actions Artifacts，分别核验 ZIP、`delivery_manifest.json`、`WORK_HANDOFF.md` 和每个原图 byte-size、SHA/格式。文件缺失或不符即停止，不能从公开仓库另行猜选图片。任何候选图均应作为 Work 的新生成输出，不使用失败的 Candidate_01 作正向图片参考。

**只生成两张 941×1672 9:16 PNG，全部完成后一次性向 PO 提交：**
1. `OPENING_P02_C03_BLOOD_PALM_CONTACT_CANDIDATE_02.png`：君鹭远身/头/视线面向木门、偏侧后摄影轴、右掌少量血贴于关闭的 D03 木门；身体前倾以表现谨慎接触，**不朝镜头摆拍**。要能看清袖口与完整手臂、门框及木纹。
2. `OPENING_P02_C05_DOOR_GAP_WRIST_GRIP_CANDIDATE_02.png`：同一木门、同一君鹭远、同一右腕；门仅狭缝，一只腐手从内侧伸出抓腕。相比 C03 **可见的戏剧动作变化**：上身后撤、肩背紧绷、右臂被抓受限、左手自然防御、目光急转被抓腕，眼睛惊恐睁大、唇微张；稍宽景别保留受力关系。禁止简单复制 C03 再加鬼手。

空间/灯光：D02 的三楼光源逻辑锁定，不新增显眼暖色吸顶灯/吊灯/壁灯；D03 门框/木板结构和低调光影需匹配，不提前显现 P03 试炼血字。**右手**仅是本双状态一致性工作假设，非小说明确事实。孟军未有正式正脸图，保持画外。P03A 带字门受控正向引用范围仅 P03B/P04C，不能作为本次正向图参。

## V002 验收 Gate
**PASS**（必须由 PO 实际审核图像）：C03 明确面门贴掌，C05 反应与身体动作明显改变；两镜之间身份/右腕/袖口/门体与 D02 灯光逻辑延续，没有新增顶灯、异形手、门外伸鬼手、凭空人物或提前任务血字。

**FAIL**：C03/C05 看向观众，C05 与 C03 几乎相同动作和情绪，只新增一只腐手；门与 D02/D03 不同，照明灯具凭空出现，肢体融合或左右腕不一致。Work 若无法解决关键拓扑问题，则停止并提交可复查的 FAIL 说明，不得无限自修后冒称通过。

**完成边界**：两张 Candidate_02 在本记录日尚未确认 Work 生成或交付；不能称已审核/已入库。正式 P01 V018、P01→P02 D V005、D01–D03、P03A/P03B/P04C、原音和 Video Index 不变；正式 52 Story Shots、248 Audits；P0.3 IN PROGRESS。Work 生成后依序 PO 审核 → Chat exact binary → Canonical publication → Story Shot registration → Registration verification；未审批不发布。
