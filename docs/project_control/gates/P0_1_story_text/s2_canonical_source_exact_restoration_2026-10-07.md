# S2 Canonical Source Exact Restoration｜2026-10-07

Status: `PASS / EXACT SOURCE IDENTITY RESTORED`

Scope: P0.1 source-data integrity repair.

## Problem

During repository cleanup, the following canonical path was found to be missing from GitHub main:

`source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt`

This conflicted with existing locked Project Control facts:

- canonical ID: `S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
- chapter range: 133–164
- format: UTF-8 plain text
- expected SHA-256: `159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`
- expected historical byte size: 204,656 bytes
- locked date: 2026-09-12

Git history showed no prior commit at the intended canonical S2 path.

## Recovery authority

Recovery was allowed only from the already-locked S1 canonical source:

`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`

S1 was re-verified before any extraction:

- bytes: 6,480,028
- SHA-256: `f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e`
- expected: exact match
- Git blob: `f089b5d63ded4be6f90af0ad845f6fdaa4959b84`

## Exact extraction rule

The only accepted output is the byte stream that reproduces the previously locked S2 SHA-256.

Verified rule:

1. start at the first byte of the `第133章 试炼【黑衣夫人】` heading;
2. include all source text through Chapter 164;
3. stop immediately before the `第165章 见面` heading;
4. retain exactly four LF bytes after the final Chapter 164 text.

No content-level rewriting, correction, reflow, substitution, or inferred reconstruction is permitted.

## Verification result

Restored canonical output:

`source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt`

Identity:

- chapter range: 133–164
- chapter count: 32
- encoding: UTF-8
- newline: LF
- BOM: none
- byte size: 204,656
- SHA-256: `159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`
- Git blob: `ef915a77b9663c45dad1de4ba2fcca2f82623aeb`

Result:

`EXPECTED SHA-256 == RESTORED SHA-256`

`EXPECTED BYTE SIZE == RESTORED BYTE SIZE`

Therefore the missing repository file can be restored without changing the previously locked S2 canonical identity.

## Governance effect

This repair does not create S2 V002 and does not revise the story source.

It only restores the previously declared V001 canonical bytes at their intended repository path.

P0.1 source precedence remains unchanged:

`S1 full novel canonical source → S2 Black Lady canonical chapter source → S3 source-audio transcript/index`
