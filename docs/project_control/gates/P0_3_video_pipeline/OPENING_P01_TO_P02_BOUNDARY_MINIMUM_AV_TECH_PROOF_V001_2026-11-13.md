# 《诡舍·黑衣夫人》｜Opening P01 → P02｜最小声画过门验证 V001

日期：2026-11-13
状态：**EXACT SOURCE PASS / AUDIO ALIGNMENT TECHNICAL PASS / 20S TEMP PROOF DECODE PASS / VISUAL CONTINUITY UNPROVEN / PO REVIEW PENDING**
权威基准：GitHub `main` at test start `62d7733015a197993447086ec70bac609a709bdd`；此前已批准的 `OPENING_P01_ASSEMBLY_V001`（画面版 V018）保持锁定。

## 验证目标与范围
仅验证 P01 已批母版最后 8 秒与 P02 首 12 秒的时间、原声音轨与空间换景节奏。**不是正式 P02 Story Shot，不替换 P01，不晋升 P0.3 Gate**。

## 输入二进制直接验证（FACT）
1. `OPENING_P01_V018_APPROVED_MASTER_V001.mp4`：Drive ID `1af5UBDegm-X6Jjq5jq8aJH8JkpOjY7hZ`；6908903 bytes；本轮重新算 SHA-256 `8ae976d15c78dceed9b139ed389c0c46bfe78b89a448cb3e2fe3b6b0850cb445`，与批准登记完全匹配；视频720×1280 / 24fps、时长63.375s（容器63.381s）。
2. `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a`：Drive ID `1xFkf3sC20yWVt_a3SJy9OrJ6KpWJ8bTV`；本轮重新算 SHA-256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`，与已批准源音匹配；192.257s / AAC 48kHz 双声道。
3. 以实际解码单声道 PCM 16kHz 对比源音同一时间段和 V018 的 56–63.2s，交叉相关峰出现在零偏移，Pearson 相关系数约 `0.9997244`。证明两条轨道在此时间段声学上高度一致，**不证明全段逐样本完全一致**。
4. 在正式源音中，63.250s及63.375s起算0.25s窗口的 RMS 分别约 -60.8/-60.6 dBFS，63.50s起算0.25s窗口约 -29.4 dBFS。切点位于相对低音量区。时间戳提示而非逐字锁定的音节定位。
5. P01 最后数秒实查画面：白潇潇住所三人关系收束，近63s保持稳定构图，没有提前变成诡舍门镜头。

## 实际制作的临时核查片（FACT）
- 文件：`OPENING_P01_TO_P02_BOUNDARY_TEMP_PROOF_V001.mp4`
- 画面 `00:00–00:08`：V018 原母版正式时间 `55.375–63.375`；预览文件需要重新编码，**不宣称预览与母版视频帧字节相等**。
- 画面 `00:08–00:20`：明确标记 NON-CANONICAL 的 P02 闭门示意图，仅验证位置切换、切点，不表示批准的门体、走廊、场景、镜头。
- 声音：使用已批准192.257s原声中正式时间 `55.375–75.375` 的一个**连续**20秒片段，没有添加配音、额外静音或改变故事顺序。输出预览需 AAC 再编码，**不宣称预览音频和源 AAC 字节一致**。
- 技术输出：720×1280、24fps、480帧、20.000s、690350 bytes；SHA-256 `c60c3c3ad32375cf2e11e438cbbc341aaee35d40673003455b088d9b94b43ccd`；FFmpeg 完整解码 PASS。临时视频只交会话内 PO 审看，**未上传正式私有 Drive/公开 GitHub，不登记 Video Index**。
- 预览 8.000s 处有实际视频帧边界，P01→占位P02采用直接切镜，未触及 P01 正式文件。

## 结论及最小后续 Gate
**PASS（技术边界）**：批准源文件同一性、P01尾部对齐、低音量切点、20s连续有声预览的解码和视频帧边界。

**UNKNOWN/WAITING（艺术与最终画面）**：PO 对从住所三人收束到诡舍三楼的突然换景是否自然；P02的正式场景/木门参考、人物位置、声音与首镜的逐句一致性；无同门无字/血字合法双状态证明。示意图不能作为这些结论的证据。

**下一步最小证明**：仅针对 P02-V1 的诡舍三楼封闭木门及空间轴线准备 Director Design / Scene Reference；以已批准 P03A 为连续性约束而非把带字PNG反向去字。经必要视觉 Gate 后按 Chat → GitHub Actions → Work → PO → Chat 执行。实际 P02 第一镜未通过前，不批量生产后续抓腕动作，不改变 P01 V018。

此记录是已经实际执行的核查结果，**不是新增总流程、Master或批准机制**。
