# AO-06｜Stage 2｜A04 Real Shot Spec V0.1 + Resolver Contract

Status: `APPROVED 2026-09-18 / PARTIALLY SUPERSEDED BY PO-APPROVED REVIEW PATCH 02 ON 2026-09-22`

Date: `2026-09-18`

Depends on: `AO-06 Stage 1 / PRODUCT OWNER APPROVED`

## 1. Purpose

把已锁定的 A04 事实边界转换为一个可机器执行、可 fail-closed、可审计的真实 Shot Spec，并明确：

`Shot Spec → Resolver → Reference Package → generation/use record → audit / reverse trace`

的合同。

本阶段是设计，不创建 Asset、不分配 D-069、不执行生成。

## 2. A04 Real Shot Spec V0.1

Canonical identity:

```json
{
  "shot_spec_id": "A04_SPEC_V001",
  "shot_id": "A04",
  "spec_version": 1,
  "purpose": "AO-06_REAL_SHOT_VALIDATION",
  "narrative_intent": "宁秋水观察并将注意力指向尼尔腰间区域",
  "characters": [
    {
      "entity_id": "CHAR_NING_QIUSHUI",
      "required": true,
      "reference_policy": {
        "role": "CHARACTER_REFERENCE_SHEET",
        "variant": "DEFAULT",
        "state": "DEFAULT",
        "require_dependency_fresh": true,
        "silent_fallback": false
      }
    },
    {
      "entity_id": "CHAR_NEIL",
      "required": true,
      "reference_policy": {
        "role": "CHARACTER_REFERENCE_SHEET",
        "variant": "DEFAULT",
        "state": "DEFAULT",
        "require_dependency_fresh": true,
        "silent_fallback": false
      }
    }
  ],
  "scene": {
    "entity_id": "SCENE_CASTLE_ENTRANCE",
    "required": true,
    "variant": "DEFAULT",
    "required_state": {
      "time_of_day": "DAY",
      "main_door": "OPEN"
    }
  },
  "costume": [
    {
      "entity_id": "COSTUME_NEIL_DEFAULT",
      "required": true,
      "variant": "DEFAULT",
      "state": "DEFAULT",
      "required_components": [
        "BLACK_BUTLER_ATTIRE",
        "WHITE_POCKET_HANDKERCHIEF_VISIBLE"
      ],
      "silent_fallback": false
    }
  ],
  "props": [
    {
      "entity_id": "PROP_NEIL_CROSS",
      "required": true,
      "owner_entity_id": "CHAR_NEIL",
      "variant": "DEFAULT",
      "state": "DEFAULT",
      "silent_fallback": false
    }
  ],
  "action_constraints": [
    {
      "subject": "CHAR_NING_QIUSHUI",
      "action": "OBSERVE",
      "target": "CHAR_NEIL.WAIST_AREA"
    }
  ],
  "negative_continuity": {
    "explicitly_excluded_from_a04": [
      "A05_KEYS_ABSENT_INSERT_FACT"
    ]
  },
  "shot_photography": {
    "authority": "APPROVED_A04_EVIDENCE_ONLY",
    "camera_position": "UNSPECIFIED_UNTIL_EVIDENCE",
    "shot_size": "UNSPECIFIED_UNTIL_EVIDENCE",
    "focal_length": "UNSPECIFIED_UNTIL_EVIDENCE",
    "character_blocking": "UNSPECIFIED_UNTIL_EVIDENCE",
    "screen_left_right": "UNSPECIFIED_UNTIL_EVIDENCE",
    "composition": "UNSPECIFIED_UNTIL_EVIDENCE",
    "depth_of_field": "UNSPECIFIED_UNTIL_EVIDENCE",
    "local_exposure": "UNSPECIFIED_UNTIL_EVIDENCE"
  }
}
```

The JSON above is a semantic contract candidate, not yet a runtime file.

## 3. Resolver Contract

### 3.1 Required Character resolution

For each required Character:

1. resolve exactly one formal `CURRENT + APPROVED` `CHARACTER_REFERENCE_SHEET`;
2. require dependency status `FRESH`;
3. verify canonical file existence and SHA;
4. no Atomic or legacy fallback unless an explicit future policy is added and approved.

Expected current result:

- `CHAR_NING_QIUSHUI → AST_IMG_000060 / RESOLVED`
- `CHAR_NEIL → AST_IMG_000059 / RESOLVED`

### 3.2 Required Scene resolution

Resolver input:

`SCENE_CASTLE_ENTRANCE + {time_of_day=DAY, main_door=OPEN}`

Expected current result:

`AST_IMG_000052 / DAY_DOOR_OPEN / RESOLVED`

A mismatched state such as NIGHT or CLOSED must remain `REFERENCE_GAP`.

### 3.3 Required Costume / Prop resolution

Resolver inputs:

- `COSTUME_NEIL_DEFAULT / DEFAULT / DEFAULT`
- `PROP_NEIL_CROSS / DEFAULT / DEFAULT`

Expected current result:

`REFERENCE_GAP / NO_ELIGIBLE_FORMAL_ASSET`

This is the correct result under current Registry truth.

The resolver must **not**:

- use `CHAR_NEIL` Reference Sheet as if it were a Costume Master;
- infer a standalone cross from a Character image and call it a formal Prop Asset;
- fabricate a handkerchief Prop;
- mark the Shot package generation-ready while either required gap remains.

### 3.4 White handkerchief classification

For A04 V0.1:

`WHITE_POCKET_HANDKERCHIEF_VISIBLE`

is a required component/state of `COSTUME_NEIL_DEFAULT`, not a separate `PROP_*` Entity.

This avoids over-fragmenting a costume-identification feature into a fake standalone Prop asset.

### 3.5 Package status

Reference Package has only two top-level states:

- `READY_FOR_GENERATION`
- `BLOCKED`

If `BLOCKED`, it carries explicit blocker records such as:

- `REQUIRED_REFERENCE_GAP`
- `SHOT_EVIDENCE_GAP`
- `INTEGRITY_FAILURE`
- `AMBIGUOUS_CURRENT`
- `DEPENDENCY_STALE`

`generation_allowed` is computed:

`true` only when every required positive reference resolves and all mandatory Shot evidence is available.

## 4. Expected current A04 Resolver result

Before any Stage 3 gap closure:

```text
RESOLVED
  AST_IMG_000060  CHAR_NING_QIUSHUI / CHARACTER_REFERENCE_SHEET
  AST_IMG_000059  CHAR_NEIL / CHARACTER_REFERENCE_SHEET
  AST_IMG_000052  SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN

REFERENCE_GAP
  COSTUME_NEIL_DEFAULT
  PROP_NEIL_CROSS

SHOT_EVIDENCE_GAP
  approved A04 photography source not yet materialized in current GitHub runtime

PACKAGE
  status = BLOCKED
  generation_allowed = false
```

This blocked result is an expected safety result, not a failure of the design.

## 5. Approved A04 evidence requirement

Stage 1 already locked that exact Shot photography cannot come from Scene Master or chat memory.

Therefore Stage 3 must locate/materialize the actual approved A04 source evidence before any production-like generation proof.

Allowed use of the approved A04 source:

- lock actual framing / blocking / composition evidence;
- validate continuity against the historical approved Shot;
- if formally migrated, register as the historical A04 Shot Master with:
  - `asset_class = SHOT`
  - `role = SHOT_MASTER`
  - `shot_id = A04`
  - `variant = DEFAULT`
  - `state = DEFAULT`
  - `approval_status = APPROVED`
  - `lifecycle = ARCHIVED`
  - `authority_class = CONTINUITY`
  - `resolver_usage = CONDITIONAL`
  - `provenance_status = PARTIAL`

The exact approved binary must be located; it may not be regenerated or guessed.

## 6. Reference Package V0.1

Expected package structure:

```text
A04_REFERENCE_PACKAGE_V001/
├── shot_spec_snapshot.json
├── package_manifest.json
├── visual_refs/
└── evidence/
    └── approved_a04_source_reference
```

`package_manifest.json` minimum fields:

- `package_id`
- `shot_spec_id`
- `shot_id`
- `source_commit`
- `resolver_version`
- `generated_at`
- `resolved_assets[]`
  - asset_id
  - entity_id / shot_id
  - role
  - variant
  - state
  - version_no
  - sha256
  - byte_size
  - canonical storage_uri
  - delivery filename
  - selection reason
- `reference_gaps[]`
- `blockers[]`
- `generation_allowed`

If any required gap exists, the package may still be emitted as a diagnostic package, but generation is blocked.

## 7. Generation / Use Record

A real AO-06 Work proof must create one immutable validation evidence record, for example:

`AO06_A04_USE_V001.json`

Minimum fields:

- `use_record_id`
- `shot_spec_id`
- `shot_id`
- `package_id`
- `source_commit`
- `resolver_version`
- `input_asset_ids[]`
- `input_versions[]`
- `input_sha256[]`
- `input_order[]`
- `delivery_artifact_digest` if fallback transport is used
- `generation_environment`
- `request_or_proof_identifier`
- `manual_product_owner_reference_upload_count`
- `service_input_sha_receipt`
- `result`
- `created_at`

Under current RISK-002:

`service_input_sha_receipt = NOT_AVAILABLE`

The use record is AO-06 validation evidence, not a fifth runtime Registry.

## 8. USES_REFERENCE contract

Direction is:

`formal output SHOT asset → actual reference Asset`

Example:

`AST_IMG_<A04_OUTPUT> USES_REFERENCE AST_IMG_000060`

This direction permits:

- Shot/output → all actual references;
- Asset → all Shot/output uses.

### Critical audit rule

Historical A04 must **not** receive reconstructed `USES_REFERENCE` edges based on memory or current Resolver output.

Why:

- current A04 historical provenance is incomplete;
- Schema V0.3 explicitly forbids inventing historical provenance;
- current formalization target for legacy A04 is `provenance_status=PARTIAL`.

Therefore:

1. if Stage 3 formalizes the historical A04 Shot Master, it receives no invented historical `USES_REFERENCE`;
2. AO-06 real validation records the current proven input set in the immutable validation use record;
3. relation creation / uniqueness / reverse-query / atomic Audit behavior is validated in an isolated registry transaction using the real A04 spec and real reference Asset IDs;
4. a live `USES_REFERENCE` relation is written only when there is a genuinely approved formal output whose actual input use is provable.

This avoids polluting the Formal Registry merely to make AO-06 appear complete.

## 9. Reverse-audit contract

AO-06 must prove the following queries.

### Shot → references

Given:

`shot_id = A04`

Return:

- Shot Spec version;
- package ID;
- use record;
- actual Asset IDs / versions / SHA values;
- Scene state;
- any gaps / blocked conditions;
- output/proof identifier.

### Asset → Shot/use

Given:

`asset_id = AST_IMG_000060` (or another used input)

Return:

- every validation / production use record that includes that Asset;
- corresponding `shot_id`;
- package ID;
- use timestamp;
- output/proof identifier.

### Formal relation query

For a genuinely approved formal output:

- forward: source SHOT asset → `USES_REFERENCE` targets;
- reverse: target reference asset → all source SHOT assets that use it.

## 10. Stage 3 prerequisites

Stage 2 recommends that Stage 3 must clear three real prerequisites before AO-06 can close:

1. **Approved A04 evidence materialization**
   - locate the exact approved A04 source binary;
   - do not recreate it;
   - use it to lock Shot photography evidence;
   - optionally/formally migrate it as historical `SHOT_MASTER / ARCHIVED / CONTINUITY / PARTIAL`.

2. **Costume / Prop gap closure**
   - create or formalize an evidence-backed `COSTUME_NEIL_DEFAULT` reference;
   - create or formalize an evidence-backed `PROP_NEIL_CROSS` reference;
   - white pocket handkerchief remains a Costume component;
   - every new formal visual asset still requires Product Owner approval;
   - no generative invention merely to satisfy the Registry.

3. **Resolver / package / audit implementation**
   - executable Shot Spec reader;
   - Character + Scene + Costume + Prop resolution;
   - fail-closed package;
   - immutable validation use record;
   - reverse-audit queries;
   - isolated `USES_REFERENCE` transaction tests;
   - full regression.

Because this requires multi-file runtime code, tests, possible Entity/Asset Registry additions, and real binary handling, Stage 3 is expected to be the point where `D-069` may be allocated after Product Owner approval.

## 11. Stage 2 Product Owner approval questions

Approval should confirm all of the following:

1. A04 Real Shot Spec V0.1 structure is accepted.
2. Ning / Neil Character Reference Sheets and Castle Entrance DAY_DOOR_OPEN are required resolved references.
3. `COSTUME_NEIL_DEFAULT` and `PROP_NEIL_CROSS` are required; current REFERENCE_GAP must block generation.
4. White pocket handkerchief remains a Costume component, not a standalone Prop.
5. Approved A04 source evidence is mandatory for exact Shot photography and may not be recreated.
6. Diagnostic packages may be emitted while blocked, but `generation_allowed=false`.
7. Historical A04 receives no fabricated historical `USES_REFERENCE`.
8. Current AO-06 use is captured in an immutable validation use record; live `USES_REFERENCE` requires a genuinely approved formal output with provable inputs.
9. Stage 3 may allocate D-069 for implementation only after this design is approved.

No AO-06 completion or P1 Wave 2 release is implied by Stage 2 approval.

## 12. Product Owner approval

Approved on `2026-09-18`.

All nine Stage 2 approval questions are accepted and locked.

Stage 3 engineering is authorized under `D-069`.

This approval does not mark AO-06 complete and does not release P1 Wave 2 or start P0.3.


## Review Patch 02 override — 2026-09-22

The Product Owner approved a narrower evidence boundary after recovery and direct review of the exact approved A04 binary.

The following Stage 2 requirements are superseded for A04:

- standalone formal `COSTUME_NEIL_DEFAULT` is no longer a required positive reference;
- standalone formal `PROP_NEIL_CROSS` is no longer a required positive reference;
- `WHITE_POCKET_HANDKERCHIEF_VISIBLE` is not a required A04 continuity fact.

Current A04 continuity rule:

- Neil black butler attire = required canonical appearance-continuity fact;
- visible chest cross = required canonical appearance-continuity fact;
- these are enforced under `CHAR_NEIL / DEFAULT` continuity plus approved A04 Shot evidence;
- no standalone Costume/Prop visual Asset is fabricated or required merely to close AO-06.

Current A04 Shot evidence rule:

- exact evidence path:
  `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`;
- byte size:
  `2486659`;
- SHA-256:
  `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`;
- approved evidence controls composition / blocking / visible Shot facts;
- historical `USES_REFERENCE` remains non-reconstructable.

All other Stage 2 fail-closed rules remain in force.
