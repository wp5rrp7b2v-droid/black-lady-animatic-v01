# 《诡舍·黑衣夫人》｜S02-B V005 Review｜A06 改在「管家转身」及转场处理

日期：2026-10-14

## 决策、问题与范围

Product Owner 在 S02-B Full Review V004 后指出：

1. **「镜头之间又使用未被批准的简单切换」**；
2. **「尼尔转身」这个时候就可以切换到A06的镜头了**。

状态：**REVIEW CORRECTION RENDERED / TECHNICAL QC PASS / PRODUCT OWNER APPROVAL PENDING**。

- 此版为独立 **V005 review-only**，并非 V004 经审批的正式继承或 Canonical Publication。
- 不改旧版 V003/V004、本项目正式批准 V001 视频母版，不改变现有 Story Shot 二进制或登记。
- 保留 2026-10-14 PO 批准的君鹭远局部 B V002（frame 1078:1114 的 1.2s 近景），之前已批准的 N16–N17 V004 开头和片尾宁秋水 B V002 继续使用。
- 正片旁白整体音频不重排、不调速、不裁剪、不重编码。

## 叙事时间定位与镜头改动

参考 `source_material/S3_audio_transcript/S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv`，标记 `S3-MVP1-0018` 的 Reviewed Transcript 给出：

> 管家转身带着众人直接朝大厅走去

其源音频估计开始时间 02:07.000；减去 S02-B 原音频起点 01:18.750，得到视频约 48.250 秒（此为 reviewed approximate TC，不是 verified exact word boundary）。

**新 A06 起点：frame 1448 / 30 = 48.266667s**，与该「转身」动作提示相邻，以自然声画接续为目标，精确语义对齐需由 PO 正片听感判定；**不将该估值冒充逐字验证 PASS**。

新的画面段落：

| 全片帧段（尾不含） | 全片位置 | 镜头 | 来源 |
|---|---|---|---|
| frame 0:1448 | 0:00–0:48.267 | V004 既有已批画面，包括君鹭远局部 B V002 | V004 对应帧（保留镜头） |
| frame 1448:1566 | 0:48.267–0:52.200 | A06 门仍打开、尼尔在门前 | V004 中同一已批准 A06 画面的 frame 1583，静止延长 118 帧 |
| frame 1566:1694 | 0:52.200–0:56.467 | N24 光勇提问 | V004 中同一已批准 N24 画面的 frame 1652，静止延长 128 帧 |
| frame 1694:1927 | 0:56.467–0:64.233（视频末帧） | N25、宁秋水 B V002、N26 | V004 对应帧（保留镜头） |

由此 `N23 → A06 → N24 → N25` 有清晰叙事功能：尼尔转身→看见尚未关的门→光勇问门为何不关→尼尔回答。

以上是当前导演层面 **local review derivative** 的时长分配，不修改已登记 Story Shot 的原始图片。

## 对「未经批准的简单切换」的本次修正（仍待 PO 审核）

采用受已批 N16–N17 V004 的 5-frame reaction dissolve 启发、但在本镜头区间**尚未获得 PO 批准**的短时柔和过渡；不声称已经正式批准这些新过渡。只在此次改变的 3 个边界使用，无全片机械重复：
- frame 1448（N23→A06）
- frame 1566（A06→N24）
- frame 1694（N24→N25）

各边界在 `b-2..b+2` 五帧内平滑合成，最后一帧 100% 新画面；其余时间保持每个镜头自然静止，不叠加循环推拉、数码缩放、旋转、遮盖或炫目滤镜。保留已有 Jun B V002 获批镜头切换处理，不篡改先前局部审批结果。

该转场系**新试剪导演提案**，由 PO 看实际视频评估，不将“技术剪辑完成”标成“镜头转场审批通过”。

## 新 Review V005 输出及核验

主视频：`S02_B_ASSEMBLY_REVIEW_V005_JUN_APPROVED_A06_ON_TURN_CINEMATIC_TRANSITIONS.mp4`

- SHA-256：**`ffd811370e77293e5f519020d611aeaef37590979d5922d5ce715a1cb508d63c`**
- bytes：**9,859,731**
- 画面：720×1280 / 30fps / **1927 frames**，视频时长 64.233333 秒
- AAC：2ch / 48kHz / **3013 audio packets**，音轨总时长 **64.250000s**
- Container duration：**64.250000s**
- 全文件解码：**PASS**
- 与 V004 的 AAC ADTS stream hash 完全一致：`d1e12748ce836c6c191148c3abf10b3a5144a932042c6474512303c79b87e5e9`
- 与 V004 的 decoded 48kHz stereo PCM hash 完全一致：`1952b8abb045aeccb25f4205078b83f66e4d3f62767ee6cdf9b375efe5d78cd8`
- 21 个非转场取样点映射到 V004 相同画面或既有 A06/N24 画面；解码像素采样平均绝对误差 1.837–2.322 8-bit/channel（来自 H264 再编码，不能称像素级完全相同；原始 PNG 本体未修改）。

本轮用户可观看 28.322 秒宽上下文审核片 `S02_B_REVIEW_V005_JUN_TO_END_CONTEXT.mp4`（SHA256 `7c5147f9e2c4911e0c442a9da15b22e9d49f65353cb4f8c1bc3f76cb0ef58ede`，849 帧，全解码 PASS），覆盖君鹭远近景直至本节收尾，并非新的源音频权威。

## 下一步门槛

1. Product Owner 观看 V005 后审核 A06 新切点及三处过渡。未审批，不发布。
2. 若需要改切点或转场质感，可就该区域继续微调，不重新生成已批准 PNG。
3. 只有完整新视频审批后，才依独立授权进行正式版视频存储、精确核验、Video Index 和 Project Control Closeout。
4. 新增的 Jun 原图现仅在 GitHub staging，其正式 Story Shot 发布/登记须另行批准；此视频试剪无权直接登记。
