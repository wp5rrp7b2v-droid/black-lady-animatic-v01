# M01 A1 N17｜PO定位批准后，全镜头377帧烛火轮廓及人物保护候选审计

日期：2026-10-17  
工作分支：`feature/m01-v002-engine-stage-a-20261017`  
状态：**PO_F601_LIGHT_CENTERS_APPROVED / FULL_FRAME_MACHINE_MASKS_BUILT / PEOPLE_AND_FLAME_SHAPE_GT_PENDING / BATCH_HOLD**

## 批准范围

PO 以「批准」通过N17 F601四支烛火中心（720×1280原视频绝对坐标）：
`(618,54), (624,40), (645,22), (688,42)`，同属 `N17_RIGHT_SCONCE_01`。

批准记录：`A1_N17_PO_POSITION_APPROVAL_2026-10-17.json`。这不是全部帧的火焰形状、人物保护，也不是全视频或跨场景 M01 引擎通过。

## 新增云端核验

GitHub Actions [#39020334729](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/39020334729) 已完成；原始 V006 源文件 SHA-256 `7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402` 保持不变。

| 核查项 | 数据与边界 |
|---|---|
| N17源镜头 | F281–F657共 **377帧**，30FPS，精确序号解码 |
| 人物分割候选 | 377帧全部生成位图（YOLO11n-seg 640像素输入，13px扩展），未检出0人的空帧 |
| 人物框内的未分割区域 | 作为独立的 `uncertain_bbox_regions` 按帧保存；不能当作已确认的安全背景 |
| 火焰形态候选 | 已为 F550–F657的108帧 × 4支火焰分别输出机器轮廓位图 |
| 前段与光源开始时间 | F520样本未见烛火、F550已见烛火；具体首次出现帧尚未核定；早期266帧仍为时域光源状态未确定 |
| 火焰轮廓异常 | **35帧**被自动标为尺寸超出候选经验范围，需要检查，不能凭视频输出自行放行 |
| 火焰与人像蒙版交叠 | 在扣除已检测人物和检测框不确定区域后=0；**这是算法排除的结果，不代表人物漏检率为0** |
| 技术核验 | 377张人物位图、377张不确定区域位图、432张火焰候选位图全部归档，并逐文件校验 SHA |
| 正式 GT 与使用授权 | 人物轮廓、火焰完整轮廓未批准；**M01 = HOLD** |

## 项目资产

- `a1_n17_full_frame_masks_v001/M01_A1_N17_ALL_377_FRAMES_PROTECTION_FLAME_QA_V001.json`：逐帧源RGB哈希、分割面积、风险标记、候选火焰数据。
- `a1_n17_full_frame_masks_v001/M01_A1_N17_MACHINE_MASK_PROPOSALS_377_FRAMES_V001.zip`：位图包，`ZIP/bitpack/little-endian`，总计377+377+108×4个候选蒙版；不等于GT。
- `a1_n17_full_frame_masks_v001/M01_A1_N17_377_FRAME_CANDLE_PERSON_PROTECTION_QA_V001.jpg`：原始帧与效果遮罩诊断对照图。

**下一步**：审核35帧轮廓异常、火焰首帧出现边界、人物漏检（尤其发丝、衣物边缘）和框内未分割区域。通过后才能冻结 N17 的逐帧 Ground Truth 子集，再用于通用算法准确率测评。

**治理**：无新MP4、无正式素材修改、无 `main` 合并、无 Production/Story Shot 发布。S02-B不是 M01 跨场景复用验收终点。
