# 《诡舍·黑衣夫人》｜Opening P01 V018｜PO 批准、原件归档、Video Index 登记闭环

日期：2026-11-13
状态：**VIDEO-LEVEL PO APPROVED / DRIVE EXACT-BINARY PASS / GITHUB VIDEO INDEX REGISTERED AND READBACK PASS / P0.3 IN PROGRESS**

## 正式审批与范围
- Product Owner 在审看 V018 完整版本后明确回复：“批准V018”。
- 批准对象为 `OPENING_P01_V018_PO_REVIEW_FIXED_SHOTS_720p.mp4` 精确二进制的 **Opening P01 63.375 秒视听剪辑**。
- 保持批准版的 13 个连续画面段、固定构图（移除历史镜头摇晃/推拉）、四处柔和亮度转场与完整原音。正式发行使用相同字节；无重新编码。
- 本次明确的全片批准覆盖早期 V008“26–43 秒局部 PASS”后续的剪辑修正；不等于修改任何既有 Approved PNG 或否定其历史批准事实。
- 不替代既有 `OPENING_V001`；本记录是独立 P01 视频 `OPENING_P01_ASSEMBLY_V001`。不升级 P0.3 Gate 为 PASS。

## 原始字节与技术验证（FACT）
- 用户批准文件：`OPENING_P01_V018_PO_REVIEW_FIXED_SHOTS_720p.mp4`
- 实际文件大小：**6,908,903 bytes**
- SHA-256：`8ae976d15c78dceed9b139ed389c0c46bfe78b89a448cb3e2fe3b6b0850cb445`
- 视频：H.264 Constrained Baseline / yuv420p / **720×1280 / 24 fps / 1521 帧 / 63.375s**
- 音频：AAC-LC / 48 kHz / 双声道 / 2972 音频包；MP4 容器时长 **63.381s**
- FFmpeg 完整解码：**PASS**。
- 原音来源：已获 PO 音频批准的 `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a` 首段，source SHA-256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`；此前 V018 vs V017 音频 AAC 比对技术 PASS。
- 将这份已批准 MP4 精确上传 Google Drive 07_Video（未经转码），又通过 Drive 接口重新下载。在本地对照两份文件：**size 6,908,903 MATCH；SHA-256 MATCH；`cmp` bytewise PASS**。此为本轮新执行的端到端二进制核验。
- 注意：本次注册验证采用 GitHub API 独立回读，不宣称曾运行专用 GitHub Actions 注册核验工作流。

## Canonical Publication（私有媒体与公开元数据分离）
- 视频 ID：`OPENING_P01_ASSEMBLY_V001`。
- 正式媒体：`Black Lady Project/07_Video/OPENING_P01_V018_APPROVED_MASTER_V001.mp4`。
- Drive File ID：`1af5UBDegm-X6Jjq5jq8aJH8JkpOjY7hZ`。
- 精确媒体 URI：`gdrive://1af5UBDegm-X6Jjq5jq8aJH8JkpOjY7hZ`。
- 用户地址：https://drive.google.com/file/d/1af5UBDegm-X6Jjq5jq8aJH8JkpOjY7hZ/view
- 原有版权声源所在的完整视频 **只存私有 Drive**；公开 GitHub 不上传音视频二进制。
- 正式 Registry：`production/video/video_index.jsonl`，新增唯一第 4 行，之前 3 行原样保留。
- Registry 写入 Commit：`53279302d03f51e5feb63a909977bad9a759b1eb`。
- GitHub 独立回读：4/4 JSONL 可解析、video_id 4/4 唯一、新记录匹配视频 SHA256/字节数/Drive ID、`approval_status=APPROVED`：**PASS**。
- 49 Story Shots / 239 Audits / 原有3个正式视频记录均不变；正式视频总数 **4**。

## V018 剪辑结构及本轮 Gate
- 整片 13 段，关键顺序：住宅门 INS00 → 君鹭远坚定 INS07/OPEN02 → 白潇潇劝阻解释 INS05/INS06 → 宁秋水搭肩 INS04 → 君鹭远感激/担忧/纠结 OPEN05/INS08/INS09 → 双人关系 OPEN06 → 白潇潇 INS06 → 三人收束 OPEN07。
- 亮度过渡位置：4.50s、20.50s、50.50s、58.00s；固定画面，不使用摇晃/推拉，不采用前后两张人物叠影式转场。
- **本阶段实际证明：**固定镜头＋有选择的柔和转场＋不更动原音，可以形成 PO 认可、能解码、可精确归档、可回溯的 P01 完整声画序列。
- **未证明：**整个 Opening P01–P04 整片已完成；P0.3 总体 Pipeline Gate 可关闭；动态人物动画达到量产标准。
- **后续：**使用 V018 作为独立已批准 P01 母版，衔接 P02 时从真实音频边界/镜头空间关系进行最小连续性验证，不返工 V018 不改其文件。
- 日常 Mac 本地同步按 RC-029 夜间周期统一快进；本轮未执行新的 Mac 同步，不冒称已同步。

审批依据：用户 2026-11-13 消息“批准V018”。登记核验依据：本轮 Drive roundtrip exact `cmp` 与 GitHub Index API 读回。
