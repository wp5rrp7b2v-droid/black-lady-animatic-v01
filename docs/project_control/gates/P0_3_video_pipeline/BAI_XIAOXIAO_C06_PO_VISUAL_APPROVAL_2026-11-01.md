# 白潇潇 C02 保脸 2.5D 转绘｜Candidate 06｜PO 视觉批准记录
日期：2026-11-01
项目：诡舍·黑衣夫人
PO 决定：**批准这张**（Product Owner 在 Chat 中对所附候选 PNG 明确批准）

## 决定范围
- 对 **本次用户实际展示的图像**作视觉审核，结论 **PO VISUAL PASS**。
- 对应计划任务：V006 C02 人物脸部身份保持、2.5D 风格转绘最小试验；目标候选名 `CHAR_BAI_XIAOXIAO_FACE_FRONT_C02_RESTYLE_CANDIDATE_06.png`。
- 不重新设计已获认可的白潇潇 C02 面部身份。
- 本次视觉批准**不等于**图像已入 GitHub，不代表 Canonical Publication / Registry 已完成。

## 已核对的 PO 上传图二进制
- 上传文件名（会话附件）：`image(20261101-111634).png`
- 格式：PNG；色彩：RGBA（8-bit）
- 尺寸：**941 × 1672**（9:16 竖构图）
- 大小：**2,747,575 bytes**
- SHA-256：`d9d62dd4c3168ec587b50e2cf30782a5c816de3ad081c1c434e659156807f5eb`

## 上游 V006 输入链状态
- GitHub Actions Run：`41279299878`，**SUCCESS**。
- Artifact：`13072228815`，V006 单一 C02 正向身份参考 Bundle，独立 Exact 1/1 PASS。
- C02 原始身份输入 SHA-256：`7603d142927e0c90773b225d6e840e000f1f7a6906f136b3bebdb67733560e07`。
- 上游 Bundle 验证只证明身份源正确，不证明本次候选输出的 Work 生产来源。对用户上传 PNG 与 Work 实际输出是否为同一字节流尚待文件级比对。

## 剩余阻塞与下一个最小动作
1. 将**被 PO 实际批准的同一份 PNG 原始二进制**摄入 GitHub 候选图 staging；禁止重编码、重新压缩、替代生成或按视觉相似推定同一文件。
2. GitHub Actions 从 staging 读取该文件，复核尺寸、大小、SHA-256；必须全部与上文一致；同时如可得，核查 Work 输出来源/生成记录与该文件的关联。
3. Exact PASS 后按现有人物身份资产流程进行 Canonical Publication 和相应资产 Registry；需区分 PO-Approved Candidate 与正式发布 Complete。任何身份锚点正式取代/登记必须完成所需门槛。
4. 发布后独立核验 Registry 指向的 GitHub 二进制 SHA-256 与上述 PO 批准字节一致，并更新 Project Control / Dashboard。

**当前状态：PO VISUAL PASS / OUTPUT BINARY MEASURED / CANONICAL INGEST & EXACT VERIFICATION PENDING**。

禁止：重新生成 C06、进行额外候选/九视图、Story Shot 登记、修改视频、冒称已完成 Canonical 入库。

## 2026-11-01｜注册执行授权与前置阻塞

- PO 随后明确指令：**「批准按照流程登记」**。授权仅针对已批准的 C06 同一原始二进制，允许按正式人物 Atomic FACE_FRONT 流程完成 Exact Intake → Canonical Publication → Entity/Asset Registry → Audit → Registration Verification → Project Control。
- 用户在 Chat 中上传的 C06 图片已在当前执行环境直接读取并进行 SHA-256 检查：PNG、941×1672、2,747,575 bytes、SHA-256 `d9d62dd4c3168ec587b50e2cf30782a5c816de3ad081c1c434e659156807f5eb`、Git Blob SHA-1 `38761350f926c30358cb98e55d6f4d603d8825f1`（本地源字节计算）。
- GitHub main 当前正式 Entity Registry **无** `CHAR_BAI_XIAOXIAO`；Asset Registry **无**白潇潇角色资产。新建实体/首个 `FACE_FRONT` 版本时必须与真实 PNG 的 canonical publication、Audit 同一已核验事务完成。不得提前虚构 Asset ID 或 CURRENT。
- 参照既有人物图集命名，预定候选审批后的正式目标：`production/image_library/character_references/bai_xiaoxiao/CHAR_BAI_XIAOXIAO_FACE_FRONT_DEFAULT_DEFAULT_V001.png`（**仅预定目标，文件尚未创建**）。源入库应使用 C06 完整未改动原始字节，不能复用 C02 身份输入做输出，也不能重编码/转格式。
- 本执行环境可读取 Chat 附件并计算真实 checksum，但 GitHub 连接器的写入接口目前只接受 UTF-8 文本或者调用方直接提供的 Base64 Blob 文本，不支持将本地聊天附件文件路径/指针直接传给 GitHub；云端 GitHub Actions 也不能直接访问聊天附件。已经检查，**尚未**将该原图传入 GH；不可将 SHA/Manifest 文本当成实际图像上传。
- 因此：**PO 授权有效，但二进制摄入被传输能力阻塞**。后续 Work/有权访问原始图字节的执行端应向 GitHub 候选 Staging 交付同一 PNG；Chat 复核上述 SHA-256、byte_size、dimensions、Git Blob 全部相符后，再执行 GitHub exact canonical promotion、资产登记和登记核验。不能因本记录/PO 批准就标记为 Atomic Master 已完成。

**最新执行状态：PO APPROVED FOR REGISTRATION / SOURCE BYTES LOCALLY VERIFIED / GITHUB BINARY INGEST BLOCKED / NO REGISTRY MUTATION**。
