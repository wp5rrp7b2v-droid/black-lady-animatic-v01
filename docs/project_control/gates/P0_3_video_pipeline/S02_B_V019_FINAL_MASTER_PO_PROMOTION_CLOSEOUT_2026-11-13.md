# 《诡舍·黑衣夫人》｜S02-B V019 最终定稿晋升与旧母版归档
Date: 2026-11-13
Status: **PO FINAL MASTER APPROVED / EXACT BINARY PASS / GOOGLE DRIVE PROMOTED / VIDEO INDEX 5-RECORD READBACK PASS / P0.3 IN PROGRESS**

## 1. Product Owner 新决策及与历史 baseline 的变化
- **2026-10-18 原 baseline：**各次经 PO 视觉批准的 S02-B 视频迭代“只增不覆”；V019 已视觉认可为自主导演版，但不得未经授权替换原正式 V001 母版。
- **2026-11-13 新增 PO 明确指令：**“将S02-B V019作为S02-B的最终定稿版本，不再是V001”。
- **失效的前提：**先前尚未获得替换现行 S02-B 主母版的明确 Product Owner 授权。现在明确授权，因此允许更新 **当前正式母版指针**，但不允许删除、重编码或消除旧版历史审批记录。
- **仍然有效：**V001 原始文件、2026-10-09 视觉批准、SHA/视频 ID、所有 V006/V018/V019 原历史迭代证据及独立候选图片审批边界不变；P0.3 Gate 未获整体 PASS。
- 当前 **S02-B 唯一 CURRENT**：`S02_B_ASSEMBLY_V019`；V001 为 `APPROVED / SUPERSEDED`（历史批准事实保留）。

## 2. V019 唯一批准二进制
- GitHub 归档：`production/video_candidates/v019_directors_cut/review/S02_B_V019_DIRECTORS_CUT_FULL_REVIEW_V001.mp4`
- GitHub 历史视觉批准：`docs/project_control/gates/P0_3_video_pipeline/S02_B_AUTONOMOUS_DIRECTOR_V001_VISUAL_APPROVAL_20261018.md`
- 2026-11-13 PO 正式晋升：**当前最终母版，不是新的重新渲染版本**。
- 原件 SHA-256：`b52476fc7201b31d7882475b755c6a41c1e2276690045bb1590e4e351c0bf28d`
- 文件大小：**25,595,015 bytes**。
- 媒体：**H.264 + AAC / 720×1280 / 30fps / 1927 视频帧 / MP4 容器 64.250 秒**（视频帧时长 1927/30 = 64.233333 秒）。
- 动态及剪辑来源：V018 已 PO 视觉批准烛火效果 + 三个 V019 导演插镜 D01/D02/D03；三张来源 PNG 不因视频定稿而自动成为三个独立 Approved Story Shots。
- 本地原 GitHub MP4 与从 Drive **独立重新下载**的 MP4：**size PASS、SHA-256 MATCH、bytewise cmp PASS**。本次仅执行 Drive 元数据移动和重命名，未上传新的编码二进制，不更动 GitHub 原归档 MP4。

## 3. 正式 Google Drive 文件与 V001 历史文件
- **新正式母版**：`Black Lady Project/07_Video/S02_B_V019_APPROVED_FINAL_MASTER.mp4`
- 文件 ID：`1wS5SwuuhPebne2OkY9n0HKI3cjqMRcoT`，URL：https://drive.google.com/file/d/1wS5SwuuhPebne2OkY9n0HKI3cjqMRcoT/view
- **旧版 V001 历史归档**：`Black Lady Project/07_Video/80_历史正式母版_已被取代/S02_B_ASSEMBLY_APPROVED_V001.mp4`
- 旧版文件 ID：`16No99iizefd_dEzIsZcVLeoXNxiuvit4`，SHA-256 原值 `8ec47720b5641412b2ebd1e082bf058244d6b07fbe97500b56a8ef830bf2042a`。
- Drive 父目录/文件名读回检查 PASS：顶层保留 V019；V001 仅移动到“历史正式母版”目录。旧版不归为“未批准试验”也不删除。

## 4. GitHub 正式登记及审核
- `production/video/video_index.jsonl`：保留原有 4 条批准视频身份记录；原 V001 行仅更新 `lifecycle=SUPERSEDED`、后继引用及存放目录。新增 V019 唯一 `S02_B_ASSEMBLY_V019` 正式 `APPROVED/CURRENT` 记录。
- 现共有 **5 条历次正式 APPROVED 视频记录，4 个 CURRENT**：Opening V001、Opening P01 V018、S02-A V001、S02-B **V019**。不得误将 5 条历次批准等同 5 个 CURRENT 母版。
- Registry 更新 commit：`25c58d22c1ffb244fcc7ce8e8555ae258853908e`；更改后由 GitHub API 独立回读确认 5/5 可解析、ID 唯一、S02-B 仅 V019 CURRENT、V001 SUPERSEDED、路径/Drive ID/哈希与实物匹配。
- 迭代账本 `production/video/iteration_history/S02_B_ITERATIONS_V001.json` 中保留历史 V001/V006/V018/V019 条目原本日期及意义，只新增 V019 **current_formal_master_pointer** 与不可删除的 `master_selection_events`。不把 10 月历史“未授权晋升”修改成当时已授权。

## 5. 批准范围和后续工作
- **本阶段实际证明：**既有 GitHub V019 原件和私有 Drive 的相同精确二进制，可在不重渲染、不覆盖历史文件的情况下被 PO 指定为当下唯一 S02-B 正式母版，并完成最新指针及历史追溯。
- **未证明/未授权：**P0.3 整体 Gate PASS、全片最终合成完成、D01/D02/D03 作为独立正式 Story Shot 获批、升级 S02-A/Opening、未来新修改自动发布。
- Mac 本地仓库同步本轮未执行，仍按 RC-029 既定晚间同步策略处理。
