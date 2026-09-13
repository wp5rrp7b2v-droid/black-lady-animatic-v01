# D-059｜CHARACTER_ASSET_MIGRATION_V1｜人物锚定图正式迁移入库

Status: `COMPLETE / REMOTE VERIFIED`

Completed on: `2026-09-13`

## 1. Result

D-059 已完成旧人物锚定图的 canonical storage migration，并已成功发布到 canonical GitHub repository。

Remote commit:

`d9fb763fb63e57023aa2cf11119c9be1bef037d6`

Commit message:

`P0.2 migrate approved character reference images`

## 2. Published assets

正式发布：

- `48` 张 canonical PNG
- `1` 份 CSV Migration Mapping Manifest
- `1` 份 JSON Migration Mapping Manifest

总新增文件：`50`

Character asset root:

`production/image_library/character_references/`

按 9 个 Character Entity 分目录：

- `black_lady/`
- `castle_young_master/`
- `guang_yong/`
- `jun_luyuan/`
- `liao_jian/`
- `neil/`
- `ning_qiushui/`
- `su_xiaoxiao/`
- `wen_qingya/`

Migration evidence:

- `docs/project_control/gates/P0_2_visual_assets/migration_evidence/character_asset_migration_manifest_v1.csv`
- `docs/project_control/gates/P0_2_visual_assets/migration_evidence/character_asset_migration_manifest_v1.json`

## 3. Validation

Codex execution and remote verification confirmed:

- canonical filenames validated;
- file count validated;
- SHA-256 values validated;
- no canonical filename collision;
- remote `main` contains commit `d9fb763fb63e57023aa2cf11119c9be1bef037d6`;
- GitHub compare against previous Project Control head confirms exactly `48 PNG + 2 manifest` files added;
- all 9 Character directories are present remotely.

## 4. Pending / excluded asset

Neil legacy asset:

`CHAR_neil_rear_turn_45_full_body_aux_reference_v001.png`

remains `MAPPING_REQUIRED` and was intentionally **not** migrated into canonical Character storage. Its supplementary Role must be formally defined before any future ingest.

Black Lady legacy 3/4 asset previously judged likeness-insufficient was also not promoted into current canonical storage; the locked migration policy remains `DEPRECATED / resolver NEVER`.

## 5. Important boundary

D-059 completes:

`canonical file storage + Migration Mapping Manifest publication`

It does **not** by itself mean that the full long-term Asset Registry / Audit Event database and Automatic Ingest implementation are complete. Those remain P0.2 engineering work.

## 6. Network execution note

The final HTTPS push succeeded after using a one-time larger Git HTTP post buffer:

`http.postBuffer=524288000`

The temporary value was not persisted. The repo-local proxy remained as configured during D-059. A future dynamic Git Network Helper may be implemented separately if recurring VPN proxy-port changes create operational friction; this does not block current P1 production.

## 7. Next production action

Resume:

`P0.2-03｜P1 Wave 1｜宁秋水 PROFILE_LEFT + REAR_3Q_LEFT`

The image-production chat may use the approved Character references as production inputs; only internally-approved final candidates return to the main project-control chat for canonical registration and GitHub publication.
