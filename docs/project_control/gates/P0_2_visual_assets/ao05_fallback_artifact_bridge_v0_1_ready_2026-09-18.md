# AO-05｜Fallback Artifact Bridge V0.1｜Ready｜2026-09-18

Status: `READY / WORK ROBUSTNESS VALIDATION PENDING`

Workflow: `.github/workflows/ao05-fallback-artifact-bridge.yml`

Successful run: `35319662012`

Source commit: `775238d05278af963d6e673063ce71ae522c18d1`

Artifact name: `AO05_GUANG_YONG_DELIVERY_BUNDLE_V001`

Artifact ID: `10536850548`

Artifact size: `9094747 bytes`

Artifact digest: `sha256:a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`

Expires: `2026-09-25T07:29:39Z`

## Exact reference set

1. `AST_IMG_000056`
   - `CHARACTER_REFERENCE_SHEET`
   - SHA256 `2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`
   - bytes `475761`

2. `AST_IMG_000011`
   - `FACE_FRONT`
   - SHA256 `7f88a3f8d68dbfea0058ff0379d0164380722d96ae1774364bcd8b79367ad6f5`
   - bytes `2903455`

3. `AST_IMG_000009`
   - `BODY_FRONT`
   - SHA256 `60005a45f2c89bceb463183c9fa4acee2b6ad0eebabadf8b825bc5e877b85b6e`
   - bytes `2852067`

4. `AST_IMG_000008`
   - `BODY_BACK`
   - SHA256 `63034c8deabef693321e5a3eadb4ffdbfdf69378527767d31852fd4ae45b621b`
   - bytes `2857476`

## GitHub-side validation

The workflow:

- checked out canonical `main`;
- required the runner checkout SHA to equal the triggering commit SHA;
- verified each Asset ID belongs to `CHAR_GUANG_YONG`;
- verified expected role;
- verified `APPROVED / CURRENT / resolver_usage=DEFAULT`;
- verified Registry SHA256 and byte size;
- hashed the canonical file bytes;
- copied exact bytes to the Delivery Bundle;
- re-hashed copied files;
- performed a second complete pre-upload hash/byte verification;
- uploaded only after `4/4 exact binaries` passed.

## Bundle contents

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- four files under `visual_refs/`, each prefixed by its Asset ID

The bundle is a transport artifact only. It is not a formal Asset and must not enter the Asset Registry.

## Next proof

ChatGPT Work must obtain artifact ID `10536850548` without Product Owner reference-file upload, independently validate the manifest and all four binaries, then execute RUN A and RUN B using the exact same four references.

AO-05 remains IN PROGRESS until that proof passes.
