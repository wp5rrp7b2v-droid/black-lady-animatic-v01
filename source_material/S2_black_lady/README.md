# S2｜《黑衣夫人》篇章原著

Canonical ID: `S2_SOURCE_BLACK_LADY_TEXT_V001.txt`

Canonical file: `S2_SOURCE_BLACK_LADY_TEXT_V001.txt`

Status: `CANONICAL / LOCKED / EXACT SOURCE RESTORED`

- Chapter range: 133–164
- Chapter count: 32
- Format: UTF-8 plain text
- BOM: none
- Newline: LF
- File size: 204,656 bytes
- SHA-256: `159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`
- Git blob: `ef915a77b9663c45dad1de4ba2fcca2f82623aeb`
- Locked on: 2026-09-12
- Exact-source restoration verified on: 2026-10-07

本目录保存唯一正式 S2 文本。其他同名/近似文本均为 NON-CANONICAL，不得作为正式剧情依据。

## Exact-source restoration

2026-10-07 repository cleanup review identified that the canonical path was declared and locked in Project Control but the text file itself had never been committed at that path.

Restoration used the already-locked S1 canonical source:

`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`

S1 was first re-verified before extraction:

- byte size: 6,480,028
- SHA-256: `f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e`
- result: EXACT MATCH

The S2 byte identity was then reproduced from S1 using the locked chapter scope:

- start: first byte of the `第133章` heading
- end: immediately before the `第165章` heading
- trailing LF count: 4
- output byte size: 204,656
- output SHA-256: `159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`
- result: EXACT MATCH with the S2 SHA-256 recorded on 2026-09-12

No prose was rewritten, normalized, corrected, inferred, or regenerated. The restoration is accepted only because the reconstructed byte stream exactly reproduces the previously locked S2 identity.
