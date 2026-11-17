# 《诡舍·黑衣夫人》｜Opening P01→P02 D版 V005 正式批准与精确发布登记收尾

日期：2026-11-17

状态：**PO APPROVED / GOOGLE DRIVE EXACT-BINARY PASS / VIDEO INDEX REGISTERED + INDEPENDENT READBACK PASS / P0.3 STILL IN PROGRESS**

## 一、审批范围与正式版本

- Product Owner 实际审看 D版 V005 后明确回复：「批准V005」。
- 获批对象为独立的 **14.250 秒过门验证片**，而不是整段 P02、血门动作或完整 Opening 成片。
- 视频 ID：`OPENING_P01_P02_D_TRANSITION_V001`；获批剪辑源 `OPENING_P01_P02_D_AV_CONTINUITY_PROOF_V005.mp4`。
- 正式媒体文件：`OPENING_P01_P02_D_AV_CONTINUITY_V005_PO_APPROVED_V001.mp4`，Google Drive 私有 `07_Video` 文件夹，**源候选与归档 MP4 字节完全相同，无重编码**。
- 链接：https://drive.google.com/file/d/1v4WP7-czwbNi1Sxx36fk3jvphE4M7vct/view
- Drive file ID：`1v4WP7-czwbNi1Sxx36fk3jvphE4M7vct`。
- 正式 P01 V018（`OPENING_P01_ASSEMBLY_V001`）保持原批准二进制不变，不被本过门片替代。

## 二、精确二进制与技术验证（FACT）

| 属性 | 实测 / 核对值 |
|---|---|
| SHA-256 | `2f5220c7afb9519ecbc5e5dc6f1464b49dfe423c1ff31dee538300ec0421d641` |
| 字节数 | 2,319,943 |
| 视频 | H.264 / 720×1280 / 24fps / **342 帧** |
| 时长 | 14.250s |
| 音频 | AAC / 48 kHz / 双声道 |
| 原候选完整解码 | FFmpeg PASS |
| Drive 独立回读 | 2,319,943 bytes、SHA-256 MATCH、`cmp` EXACT PASS |
| Drive 回读完整解码 | FFmpeg PASS |

已批准连续音频源：`OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a`，SHA-256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`。P01 V018 来源 SHA-256 `8ae976d15c78dceed9b139ed389c0c46bfe78b89a448cb3e2fe3b6b0850cb445`。

视频画面 Canonical 来源由已登记 D01–D03 三张 PNG 构成：
- D01 `7732555dde7f3395f08854b9f56ea3e857a4e58248dec3c2ce108b76b6f44dde`；
- D02 `4098fc1fe5af158b459b2d2575ccbd4db648a4fee6ce8b05f6eb69f3d58b51dc`；
- D03 `f1c706e7ed60accf169e75a8b1d131974489c438bf179b093847ec3860fd43c3`。

## 三、V005 获批声画节奏

| 输出时间 | 画面及动作 |
|---|---|
| 00:00–00:08 | 锁定 P01 V018 末 8 秒（源片 55.375–63.375s） |
| 00:08–00:09.75 | D01 诡舍外景 **固定画面、不摇晃** |
| 00:09.75–00:11.50 | D02 三楼环境，缓慢数码推进至约 1.24× |
| 00:11.50–00:14.25 | D03 旧血木门，缓慢数码推进至约 1.20× |

声轨采取获批编辑边界：输出 00:08–00:11.9 使用 Compact Audio 63.6–67.5s 的“想要参与试炼”过门原声，使该句从外景开始并允许跨 D01–D03；末 2.35 秒是**有意插入的编辑留白**。后续“孟军让君鹭远伸出手”没有出现在三张建立镜中。**不能把此剪辑称为从头到尾无间断播放的原音，也不能把临时语义时间点称为独立逐字转写证据**。

## 四、正式 Video Index 登记与读回验证

- 正式登记位置：`production/video/video_index.jsonl`，Video ID `OPENING_P01_P02_D_TRANSITION_V001`。
- 登记 Commit：`1b1831631eab4848d0fa455cbb4aa3191993acf0`。
- 通过 GitHub 独立重新调用 `fetch_file` 读回，而非仅相信写入结果：**JSONL 6/6 可解析、Video ID 唯一、V005 精确 SHA/字节数/Drive ID/PO Approved/Current 均匹配**。
- 旧 P01 V018 的 SHA-256 未变，旧五条登记记录未修改；新增后 **6 条历史 Approved、5 条 CURRENT、1 条 SUPERSEDED**。
- 本次未新登记 Story Shot，因此仍为 **52 Story Shots、248 Audit Events**。
- GitHub 本次仅记录媒体元数据；版权原声视频二进制仅保存于私有 Drive。

## 五、保留事项 / 下一步

- **PASS**：V005 PO 过门声画审核、正式 MP4 精确二进制、Drive 云端保存与回读验证、Video Index 唯一注册回读。
- **未批准**：整段 P02 血门人物动作、进一步契约音频续接、完整 Opening 最终片、P0.3 生产 Gate 整体完成。
- **下一最小 Gate**：以 V005 结尾木门为衔接基准，核查后续真实契约台词入点和木门动作画面，不擅自增加或覆盖其他母版。
- **未执行**：用户 Mac 本地工作区同步；没有当前 Mac 终端三方 SHA 证据，不声明同步 PASS。
