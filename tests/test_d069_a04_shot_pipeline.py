import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import resolver_asset_source_v0_1 as source
import shot_reference_resolver_v0_1 as resolver
import shot_reference_package_exporter_v0_1 as exporter
import shot_use_audit_v0_1 as audit

EVIDENCE = Path("staging/d069_a04_intake/A04_REBOOT_approved_v001.png")
EXPECTED_SHA = "8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398"
EXPECTED_SIZE = 2486659


class Fixture(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.addCleanup(self.t.cleanup)
        self.root = Path(self.t.name)

        for rel in [
            source.MANIFEST,
            source.REGISTRY,
            source.SCENE_PROFILES,
            Path("production/asset_registry/entity_registry.jsonl"),
            Path("production/asset_registry/asset_relations.jsonl"),
            Path("production/asset_registry/audit_event_log.jsonl"),
            resolver.SPEC,
        ]:
            p = self.root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, p)

        evidence_target = self.root / EVIDENCE
        evidence_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / EVIDENCE, evidence_target)

        for row in source.read_runtime_registry(ROOT):
            try:
                p = source.source_path(source.normalize(row, "RUNTIME_REGISTRY"), ROOT)
            except ValueError:
                continue
            if p.is_file():
                d = self.root / row["storage_uri"]
                d.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(p, d)

    def rows(self):
        return [
            json.loads(x)
            for x in (self.root / source.REGISTRY).read_text().splitlines()
            if x.strip()
        ]

    def write_rows(self, rows):
        (self.root / source.REGISTRY).write_text(
            "".join(json.dumps(x) + "\n" for x in rows)
        )


class LiveTests(unittest.TestCase):
    def test_spec_locks_approved_evidence_boundary(self):
        spec = resolver.load_spec()
        self.assertEqual(spec["shot_spec_id"], "A04_SPEC_V001")
        self.assertEqual(spec["costumes"], [])
        self.assertEqual(spec["props"], [])
        self.assertEqual(len(spec["appearance_continuity"]), 1)
        continuity = spec["appearance_continuity"][0]
        self.assertEqual(continuity["entity_id"], "CHAR_NEIL")
        self.assertFalse(continuity["formal_asset_required"])
        self.assertEqual(
            continuity["constraints"],
            ["BLACK_BUTLER_ATTIRE", "VISIBLE_CHEST_CROSS"],
        )
        self.assertNotIn(
            "WHITE_POCKET_HANDKERCHIEF_VISIBLE",
            continuity["constraints"],
        )
        self.assertEqual(spec["shot_evidence"]["sha256"], EXPECTED_SHA)
        self.assertEqual(spec["shot_evidence"]["byte_size"], EXPECTED_SIZE)

    def test_live_a04_is_ready_with_three_formal_refs_plus_approved_evidence(self):
        r = resolver.resolve()
        self.assertEqual(r["status"], "READY_FOR_GENERATION")
        self.assertTrue(r["generation_allowed"])
        self.assertEqual(
            [x["asset"]["asset_id"] for x in r["resolved"]],
            ["AST_IMG_000060", "AST_IMG_000059", "AST_IMG_000052"],
        )
        self.assertEqual(r["reference_gaps"], [])
        self.assertEqual(r["shot_evidence"]["status"], "RESOLVED")
        self.assertEqual(r["shot_evidence"]["evidence"]["sha256"], EXPECTED_SHA)
        self.assertEqual(r["shot_evidence"]["evidence"]["byte_size"], EXPECTED_SIZE)

    def test_legacy_costume_prop_entities_do_not_block_a04(self):
        entities = [
            json.loads(x)
            for x in (ROOT / "production/asset_registry/entity_registry.jsonl")
            .read_text()
            .splitlines()
            if x.strip()
        ]
        ids = {x["entity_id"] for x in entities}
        self.assertIn("COSTUME_NEIL_DEFAULT", ids)
        self.assertIn("PROP_NEIL_CROSS", ids)
        r = resolver.resolve()
        self.assertEqual(r["reference_gaps"], [])
        self.assertTrue(r["generation_allowed"])

    def test_no_live_historical_use_relations(self):
        self.assertEqual(audit.query_relations("AST_IMG_000060", "reverse"), [])


class ResolverFixtureTests(Fixture):
    def test_character_sheet_with_never_usage_is_not_eligible(self):
        rows = self.rows()
        sheet = next(x for x in rows if x["asset_id"] == "AST_IMG_000060")
        sheet["resolver_usage"] = "NEVER"
        self.write_rows(rows)
        result = resolver.resolve(root=self.root)
        gap = next(
            x
            for x in result["reference_gaps"]
            if x.get("entity_id") == "CHAR_NING_QIUSHUI"
        )
        self.assertEqual(gap["reason"], "NOT_ELIGIBLE")
        self.assertFalse(result["generation_allowed"])

    def test_scene_mismatch_still_blocks(self):
        spec = resolver.load_spec(root=self.root)
        for key, value in [("time_of_day", "NIGHT"), ("main_door", "CLOSED")]:
            with self.subTest(key=key):
                altered = copy.deepcopy(spec)
                altered["scene"]["required_state"][key] = value
                p = self.root / f"{key}.json"
                p.write_text(json.dumps(altered))
                result = resolver.resolve(p, self.root)
                self.assertFalse(result["generation_allowed"])
                self.assertTrue(
                    any(x["kind"] == "SCENE" for x in result["reference_gaps"])
                )

    def test_missing_or_corrupt_a04_evidence_blocks(self):
        evidence = self.root / EVIDENCE

        evidence.unlink()
        result = resolver.resolve(root=self.root)
        self.assertEqual(result["shot_evidence"]["status"], "SHOT_EVIDENCE_GAP")
        self.assertEqual(
            result["shot_evidence"]["reason"],
            "APPROVED_A04_SOURCE_NOT_MATERIALIZED",
        )
        self.assertFalse(result["generation_allowed"])

        shutil.copyfile(ROOT / EVIDENCE, evidence)
        evidence.write_bytes(b"corrupt")
        result = resolver.resolve(root=self.root)
        self.assertEqual(result["shot_evidence"]["reason"], "INTEGRITY_FAILURE")
        self.assertFalse(result["generation_allowed"])

    def test_spec_cannot_reintroduce_costume_prop_blockers(self):
        spec = resolver.load_spec(root=self.root)
        spec["costumes"] = [
            {
                "entity_id": "COSTUME_NEIL_DEFAULT",
                "required": True,
            }
        ]
        p = self.root / "bad.json"
        p.write_text(json.dumps(spec))
        with self.assertRaises(ValueError):
            resolver.load_spec(p, self.root)

    def test_white_handkerchief_cannot_be_reintroduced_as_required_constraint(self):
        spec = resolver.load_spec(root=self.root)
        spec["appearance_continuity"][0]["constraints"].append(
            "WHITE_POCKET_HANDKERCHIEF_VISIBLE"
        )
        p = self.root / "bad-handkerchief.json"
        p.write_text(json.dumps(spec))
        with self.assertRaises(ValueError):
            resolver.load_spec(p, self.root)

    def test_package_contains_formal_refs_and_separate_exact_a04_evidence(self):
        out = self.root / "packages" / "A04_REFERENCE_PACKAGE_V001"
        out.parent.mkdir()
        manifest = exporter.export(
            out,
            root=self.root,
            generated_at="2026-09-22T08:00:00Z",
        )
        self.assertTrue(manifest["generation_allowed"])
        self.assertEqual(len(manifest["resolved_assets"]), 3)
        self.assertEqual(manifest["shot_evidence"]["sha256"], EXPECTED_SHA)
        self.assertEqual(manifest["shot_evidence"]["byte_size"], EXPECTED_SIZE)

        visual_refs = list((out / "visual_refs").glob("*.png"))
        self.assertEqual(len(visual_refs), 3)

        delivered = (
            out
            / "evidence"
            / "approved_a04_source_reference"
            / "A04_REBOOT_approved_v001.png"
        )
        self.assertTrue(delivered.is_file())
        self.assertEqual(source.sha256(delivered), EXPECTED_SHA)
        self.assertEqual(delivered.stat().st_size, EXPECTED_SIZE)


class AuditTests(Fixture):
    def record(self):
        return {
            "use_record_id": "AO06_A04_USE_V001",
            "shot_spec_id": "A04_SPEC_V001",
            "shot_id": "A04",
            "package_id": "A04_REFERENCE_PACKAGE_V001",
            "source_commit": "abc",
            "resolver_version": "v",
            "input_asset_ids": ["AST_IMG_000060"],
            "input_versions": [1],
            "input_sha256": ["a" * 64],
            "input_order": [1],
            "delivery_artifact_digest": None,
            "generation_environment": "NON_PRODUCTION_TEST",
            "request_or_proof_identifier": "proof-1",
            "manual_product_owner_reference_upload_count": 0,
            "service_input_sha_receipt": "NOT_AVAILABLE",
            "result": "PASS",
            "created_at": "2026-09-18T12:00:00Z",
            "scene_state": {"time_of_day": "DAY", "main_door": "OPEN"},
            "blockers": [],
        }

    def test_use_record_append_only_and_reverse_queries(self):
        audit.write_use_record(self.record(), self.root)
        with self.assertRaises(FileExistsError):
            audit.write_use_record(self.record(), self.root)
        self.assertEqual(
            audit.query_shot("A04", self.root)[0]["input_asset_ids"],
            ["AST_IMG_000060"],
        )
        self.assertEqual(
            audit.query_asset("AST_IMG_000060", self.root)[0]["shot_id"],
            "A04",
        )

    def test_uses_reference_direction_duplicate_reverse_and_rollback(self):
        live_before = (
            (ROOT / audit.RELATIONS).read_bytes(),
            (ROOT / audit.AUDIT).read_bytes(),
        )
        rows = self.rows()
        rows.append({"asset_id": "AST_SHOT", "asset_class": "SHOT"})
        self.write_rows(rows)

        rel = audit.add_uses_reference(
            "AST_SHOT",
            "AST_IMG_000060",
            self.root,
        )
        self.assertEqual(rel["source_asset_id"], "AST_SHOT")
        self.assertEqual(
            audit.query_relations("AST_SHOT", "forward", self.root)[0][
                "target_asset_id"
            ],
            "AST_IMG_000060",
        )
        self.assertEqual(
            audit.query_relations("AST_IMG_000060", "reverse", self.root)[0][
                "source_asset_id"
            ],
            "AST_SHOT",
        )

        self.assertIn("created_by_event_id", rel)
        events = [
            json.loads(x)
            for x in (self.root / audit.AUDIT).read_text().splitlines()
            if x.strip()
        ]
        event = next(x for x in events if x["event_id"] == rel["created_by_event_id"])
        self.assertEqual(
            event["new_value"]["created_by_event_id"],
            event["event_id"],
        )

        with self.assertRaises(ValueError):
            audit.add_uses_reference(
                "AST_SHOT",
                "AST_IMG_000060",
                self.root,
            )

        before = (
            (self.root / audit.RELATIONS).read_bytes(),
            (self.root / audit.AUDIT).read_bytes(),
        )
        with self.assertRaises(RuntimeError):
            audit.add_uses_reference(
                "AST_SHOT",
                "AST_IMG_000059",
                self.root,
                True,
            )
        self.assertEqual(
            before,
            (
                (self.root / audit.RELATIONS).read_bytes(),
                (self.root / audit.AUDIT).read_bytes(),
            ),
        )
        self.assertEqual(
            live_before,
            (
                (ROOT / audit.RELATIONS).read_bytes(),
                (ROOT / audit.AUDIT).read_bytes(),
            ),
        )

    def test_invalid_relation_sources(self):
        with self.assertRaises(ValueError):
            audit.add_uses_reference(
                "AST_IMG_000060",
                "AST_IMG_000059",
                self.root,
            )
        with self.assertRaises(ValueError):
            audit.add_uses_reference(
                "AST_IMG_000060",
                "AST_IMG_000060",
                self.root,
            )


if __name__ == "__main__":
    unittest.main()
