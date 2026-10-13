# S02-B｜宁秋水反应插镜｜N25→N26 已批准母版画面连续性复核

日期：2026-10-13

**状态：CANONICAL VIDEO EDITORIAL REVIEW COMPLETE / CAMERA PROPOSAL DEFINED / ORIGINAL N25-N26 SOURCE PNG PIXEL GATE STILL PENDING / NO WORK GENERATION**

## 1｜证据级别和来源

- 已批准视频来源：Google Drive `S02_B_ASSEMBLY_APPROVED_V001.mp4`，文件 ID `16No99iizefd_dEzIsZcVLeoXNxiuvit4`。
- 此次由已登记 Drive URL 取得视频的原始文件：3,393,713 bytes；重新计算 SHA-256：`8ec47720b5641412b2ebd1e082bf058244d6b07fbe97500b56a8ef830bf2042a`，与批准母版登记 **EXACT MATCH**。
- 视频信息：720×1280；30 fps；1927 video frames；duration 64.250 sec。
- 本次通过 ffmpeg 解帧观察正式视频的 **实际像素**；从 54s 处运行镜头切换检测，检测到 `54.366667s`, `56.466667s`, `60.333333s`（时间点为检测器输出，非原语音精确分词点）。
- 观察帧：`N25` at `59.8s`；`N26` at `60.6s`；辅以 `58.0/59.4/60.1/60.8/61.4/62.5/63.5s` 接续观测。
- **重要限定：** Github 连接器可确认 N25/N26 canonical PNG 路径和 Git blob，但本轮无法单独取出这两张原始 PNG 的像素供 independent exact-source visual review。此次观察为**由已批准且哈希匹配的视频母版解码获得的画面**，不是已批准 PNG 原文件的独立画质/原图核验，不得冒称原 PNG 的 pixel review 完整 PASS。

## 2｜视频画面观察（FACT：可见、可回查）

### N25（约 56.467–60.333s）
- 尼尔位于人群靠前处、背对镜头向内侧尖拱深处前行；有 2–4 名其他诡客可见，前后错位。
- 构图机位位于队伍后方，朝古堡更深处拍摄；室内为有尖拱、石柱与壁灯的暖光走廊/内厅。
- 左右墙面与地面橙琥珀色高光偏强，地面暖光反射明显。

### N26（约 60.333–64.250s）
- 镜头切换至队伍行进路径的前侧/斜前侧；尼尔前景朝画面左侧自然迈步，宁秋水穿深色外套在尼尔画面右后方，可辨认的黑发与脸部；其他诡客在更深背景。
- 角色从前一镜背影视角，转为前/侧前观察视角：属于**显著反打/机位切换**，不能简单以“左右位移相同”概括空间轴。
- 建筑材料仍为石质柱、尖拱、壁灯、暗色石地面，属于同类古堡内部空间，没有必须新增主入口/户外/大厅结构的证据。
- N26 明显比 N25 更暗，橙色反光更克制；镜头切换处存在观感可辨的亮度/暖橙饱和度落差。此为**光色连续性风险**，不等于源文件身份错误。

### 参考关系
- 反应插镜本轮 3 图 Bundle 已独立 3/3 EXACT：`AST_IMG_000060` Ning sheet、`AST_IMG_000071` Ning FACE_3Q_LEFT、`AST_IMG_000108` Castle Entrance Inner Lobby。
- 本次已查看 Bundle 中的宁秋水 3/4 左侧脸参考、Scene Master。参考宁秋水：深色立领外套/黑衬衫、短黑发、左侧 3/4 五官；Scene Master：尖拱、暖壁灯、石柱、暗色镜面地面。
- N26 已批准视频里宁秋水服装家族与参考相符。受 720×1280 视频尺寸与压缩限制，**不将其视为完成了独立 PNG 原始五官 exact review**。

## 3｜导演判断与风险（INFERENCE）

- 从背后跟随的 N25 → 前侧斜角 N26 可以由摄影机在同一队伍前方反向拍摄解释，**不自动判定为错误跨轴**；但在缺少正式原始 PNG 和完整 3D 场景轴线时，不能把空间几何连续性标成无条件 PASS。
- 插入真正的新宁秋水 3/4 反应近景具有潜在叙事价值，但不能伪装原本群体同机位裁切。
- 因 N25/N26 光色差异，新增插镜**优先沿用 N26 的受控暗暖光**，而不是复用 N25 强橙色地面反光；人物应有同一空间的边缘光/背景光，不得棚拍、抠图感、提亮肤色。
- 镜头选择应靠近 N26 的队伍斜前方摄影机轴，将宁秋水置于唯一视觉主语、面部 3/4 左侧朝向，头和视线略向人物的行进方向/尼尔，不看摄影机；背景保留 N26 相符的内厅石柱与暗壁灯，避免在画中凭空建立新的过道或大厅。
- 如新候选与 N26 人物运动方向相冲突、宁秋水身份偏移或建筑背景不符，则 FAIL / STOP，不凭人工剪切掩盖错误。

## 4｜Gate 结论

- `CANONICAL VIDEO FILE IDENTITY`：**PASS**（size + SHA256 与已有批准记录 exact match）。
- `N25/N26 EDITED VIDEO PIXEL VISUAL REVIEW`：**COMPLETE**（后机位转斜前机位、内部空间家族、明显光色落差已观察）。
- `NEW INSERT CAMERA DIRECTOR GUIDANCE`：**PROVISIONAL / N26-ALIGNED 3Q LEFT CLOSE SHOT**。
- `N25/N26 ORIGINAL APPROVED PNG BYTE-IDENTICAL IMAGE VISUAL GATE`：**PENDING**，未直接取得原二进制。
- `EDITORIAL AXIS MATHEMATICAL CONTINUITY`：**NOT PROVEN / NO AUTOMATIC PASS CLAIM**。
- `WORK GENERATION AUTHORIZATION`：**FALSE**，必须取得 Product Owner 另行授权；此前正式 Bundle V001 Artifact 技术核验 PASS 不改变这一点。
- `S02_B_ASSEMBLY_V001`：**UNCHANGED / APPROVED / CANONICAL**。
- `VIDEO_INDEX / STORY_SHOT_INDEX`：**UNCHANGED**。

## 5｜最小后续步骤

若坚持既有 Scene Reference V0.1 的原始 PNG 审核门槛，应以**只读、可回查、不增加 Work 直接参考、不改变 canonical**的方式取出 N25/N26 原 PNG，完成像素级视觉对照与可能的画面轴线建议后，再征得 PO 对 `TAIL_NING_REACTION_TEST_01 Candidate 01` 的单图 Work 授权。不得因为正式视频画面已审过，就悄悄将这项未通过的原图核验门槛标记为 PASS。
