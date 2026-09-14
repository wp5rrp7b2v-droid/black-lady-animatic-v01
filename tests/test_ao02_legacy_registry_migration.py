import csv
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "legacy_registry_migration_controller_v1.py"
spec = importlib.util.spec_from_file_location("ao02", MODULE_PATH)
ao02 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(ao02)


def write_jsonl(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(r, sort_keys=True) + "\n" for r in rows),
        encoding="utf-8",
    )


def runtime_rows():
    base = {
        "shot_id": None,
        "media_code": "IMG",
        "asset_class": "ATOMIC",
        "variant": "DEFAULT",
        "state": "DEFAULT",
        "approval_status": "APPROVED",
        "authority_class": "AUXILIARY",
        "resolver_usage": "DEFAULT",
        "provenance_status": "COMPLETE",
        "mime_type": "image/png",
        "byte_size": 100,
        "approved_at": "2026-09-13T00:00:00Z",
        "ingested_at": "2026-09-13T00:00:00Z",
    }
    return [
        {
            **base,
            "asset_id": "AST_IMG_000049",
            "entity_id": "CHAR_RUNTIME",
            "role": "PROFILE_LEFT",
            "version_no": 1,
            "lifecycle": "SUPERSEDED",
            "filename": "runtime49.png",
            "storage_uri": "production/runtime49.png",
            "sha256": "a" * 64,
        },
        {
            **base,
            "asset_id": "AST_IMG_000050",
            "entity_id": "CHAR_RUNTIME",
            "role": "PROFILE_LEFT",
            "version_no": 2,
            "lifecycle": "CURRENT",
            "filename": "runtime50.png",
            "storage_uri": "production/runtime50.png",
            "sha256": "b" * 64,
        },
        {
            **base,
            "asset_id": "AST_IMG_000051",
            "entity_id": "CHAR_RUNTIME",
            "role": "REAR_3Q_LEFT",
            "version_no": 1,
            "lifecycle": "CURRENT",
            "filename": "runtime51.png",
            "storage_uri": "production/runtime51.png",
            "sha256": "c" * 64,
        },
    ]


class AO02MigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        (self.repo / ao02.MANIFEST).parent.mkdir(parents=True, exist_ok=True)
        (self.repo / ao02.REGISTRY).parent.mkdir(parents=True, exist_ok=True)

        rows = []
        # Reverse input order intentionally; deterministic allocation must ignore source order.
        for i in reversed(range(48)):
            entity = f"CHAR_TEST_{i:02d}"
            filename = f"{entity}_FACE_FRONT_DEFAULT_DEFAULT_V001.png"
            rel = Path("production/image_library/character_references") / f"test_{i:02d}" / filename
            path = self.repo / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            payload = ao02.PNG_MAGIC + f"fixture-{i}".encode("ascii")
            path.write_bytes(payload)
            rows.append({
                "legacy_asset_id": f"LEGACY_{i:02d}",
                "legacy_filename": f"old_{i:02d}.png",
                "uploaded_filename": f"old_{i:02d}.png",
                "canonical_entity_id": entity,
                "new_role": "FACE_FRONT",
                "variant": "DEFAULT",
                "state": "DEFAULT",
                "version_no": "1",
                "approval_status": "APPROVED",
                "authority_class": "MASTER",
                "lifecycle": "CURRENT",
                "resolver_usage": "DEFAULT",
                "mapping_status": "CONFIRMED",
                "canonical_filename": filename,
                "target_storage_path": rel.as_posix(),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "byte_size": str(len(payload)),
                "mime_type": "image/png",
                "legacy_review_date": "2026-08-01",
                "legacy_review_result": "approved",
                "evidence": "fixture",
                "notes": "",
            })

        rows.append({
            "legacy_asset_id": ao02.EXCLUDED_LEGACY_ID,
            "legacy_filename": "neil_old.png",
            "uploaded_filename": "neil_old.png",
            "canonical_entity_id": "CHAR_NEIL",
            "new_role": "",
            "variant": "DEFAULT",
            "state": "DEFAULT",
            "version_no": "1",
            "approval_status": "APPROVED",
            "authority_class": "LEGACY_SUPPLEMENTARY",
            "lifecycle": "ARCHIVED",
            "resolver_usage": "NEVER",
            "mapping_status": "MAPPING_REQUIRED",
            "canonical_filename": "",
            "target_storage_path": "",
            "sha256": "",
            "byte_size": "",
            "mime_type": "image/png",
            "legacy_review_date": "2026-08-01",
            "legacy_review_result": "approved",
            "evidence": "fixture",
            "notes": "excluded",
        })

        fields = list(rows[0].keys())
        with (self.repo / ao02.MANIFEST).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

        write_jsonl(self.repo / ao02.REGISTRY, runtime_rows())
        write_jsonl(
            self.repo / ao02.RELATIONS,
            [{
                "source_asset_id": "AST_IMG_000050",
                "relation_type": "SUPERSEDES",
                "target_asset_id": "AST_IMG_000049",
                "created_at": "2026-09-13T00:00:00Z",
                "created_by_event_id": "EVT_EXISTING",
            }],
        )
        write_jsonl(self.repo / ao02.AUDIT, [])

    def tearDown(self):
        self.tmp.cleanup()

    def test_deterministic_id_plan_is_sorted_not_manifest_order(self):
        result = ao02.plan(self.repo)
        self.assertEqual(result["status"], "READY_TO_APPLY")
        self.assertEqual(result["eligible_count"], 48)
        registry_data = result["files"][self.repo / ao02.REGISTRY].decode("utf-8")
        planned = [json.loads(line) for line in registry_data.splitlines()]
        legacy = planned[:48]
        self.assertEqual(legacy[0]["asset_id"], "AST_IMG_000001")
        self.assertEqual(legacy[0]["entity_id"], "CHAR_TEST_00")
        self.assertEqual(legacy[-1]["asset_id"], "AST_IMG_000048")
        self.assertEqual(legacy[-1]["entity_id"], "CHAR_TEST_47")
        self.assertEqual([r["asset_id"] for r in planned[-3:]], [
            "AST_IMG_000049", "AST_IMG_000050", "AST_IMG_000051"
        ])

    def test_injected_write_failure_rolls_back_all_controlled_files(self):
        result = ao02.plan(self.repo)
        paths = list(result["files"].keys())
        before = {p: p.read_bytes() if p.exists() else None for p in paths}
        with self.assertRaises(ao02.MigrationError):
            ao02.commit_files_atomically(result["files"], inject_failure_after=2)
        after = {p: p.read_bytes() if p.exists() else None for p in paths}
        self.assertEqual(before, after)

    def test_successful_apply_is_idempotent(self):
        result = ao02.plan(self.repo)
        ao02.commit_files_atomically(result["files"])
        second = ao02.plan(self.repo)
        self.assertEqual(second["status"], "ALREADY_APPLIED")
        self.assertEqual(second["change"], "NO CHANGE")

    def test_partial_migration_is_blocked_without_self_repair(self):
        current = runtime_rows()
        current.append({
            "asset_id": "AST_IMG_000001",
            "entity_id": "CHAR_TEST_00",
            "role": "FACE_FRONT",
            "variant": "DEFAULT",
            "state": "DEFAULT",
            "version_no": 1,
            "lifecycle": "CURRENT",
            "storage_uri": "production/fake.png",
        })
        write_jsonl(self.repo / ao02.REGISTRY, current)
        with self.assertRaisesRegex(ao02.MigrationError, "PARTIAL_OR_CONFLICTING_MIGRATION"):
            ao02.plan(self.repo)

    def test_wrong_eligible_count_stops_before_plan(self):
        rows = ao02.load_csv(self.repo / ao02.MANIFEST)
        rows[0]["mapping_status"] = "MAPPING_REQUIRED"
        fields = list(rows[0].keys())
        with (self.repo / ao02.MANIFEST).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        with self.assertRaisesRegex(ao02.MigrationError, "exactly 48"):
            ao02.plan(self.repo)


if __name__ == "__main__":
    unittest.main()
