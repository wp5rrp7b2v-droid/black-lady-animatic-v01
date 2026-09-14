"""D-063 isolated unified-source tests; formal registries are read-only."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reference_package_exporter_v0_1 as exporter
import resolver_asset_source_v0_1 as source


class UnifiedSourceFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.entity = "CHAR_TEST"
        self.migration = []
        self.runtime = []
        self.asset_dir = self.root / source.ASSET_ROOT / "test"
        self.asset_dir.mkdir(parents=True)
        (self.root / source.MANIFEST).parent.mkdir(parents=True)
        (self.root / source.REGISTRY).parent.mkdir(parents=True)

    def add_migration(self, role="FACE_FRONT", **overrides):
        name = f"{self.entity}_{role}_DEFAULT_DEFAULT_V001.png"
        path = self.asset_dir / name
        path.write_bytes((name + " original").encode())
        row = {
            "canonical_entity_id": self.entity, "new_role": role,
            "variant": "DEFAULT", "state": "DEFAULT", "version_no": 1,
            "approval_status": "APPROVED", "lifecycle": "CURRENT",
            "resolver_usage": "DEFAULT", "mapping_status": "CONFIRMED",
            "authority_class": "MASTER", "canonical_filename": name,
            "target_storage_path": path.relative_to(self.root).as_posix(),
            "sha256": source.sha256(path),
        }
        row.update(overrides)
        self.migration.append(row)
        return row

    def add_runtime(self, role="FACE_FRONT", **overrides):
        name = f"{self.entity}_{role}_DEFAULT_DEFAULT_V001.png"
        path = self.asset_dir / name
        if not path.exists():
            path.write_bytes((name + " original").encode())
        row = {
            "asset_id": "AST_IMG_TEST", "entity_id": self.entity,
            "asset_class": "ATOMIC", "role": role,
            "variant": "DEFAULT", "state": "DEFAULT", "version_no": 1,
            "approval_status": "APPROVED", "lifecycle": "CURRENT",
            "resolver_usage": "DEFAULT", "authority_class": "AUXILIARY",
            "filename": name, "storage_uri": path.relative_to(self.root).as_posix(),
            "sha256": source.sha256(path),
        }
        row.update(overrides)
        self.runtime.append(row)
        return row

    def save(self):
        (self.root / source.MANIFEST).write_text(json.dumps(self.migration), encoding="utf-8")
        (self.root / source.REGISTRY).write_text(
            "".join(json.dumps(row) + "\n" for row in self.runtime), encoding="utf-8")

    def view(self):
        self.save()
        return source.eligible_current_assets(self.root, self.entity)

    def test_normalization_and_migration_only(self):
        migration = self.add_migration()
        view = self.view()
        self.assertEqual(len(view), 1)
        self.assertEqual(view[0]["source_layer"], "MIGRATION_MANIFEST")
        self.assertIsNone(view[0]["asset_id"])
        self.assertEqual(view[0]["entity_id"], migration["canonical_entity_id"])
        self.assertEqual(view[0]["role"], migration["new_role"])
        self.assertEqual(view[0]["filename"], migration["canonical_filename"])
        self.assertEqual(view[0]["storage_uri"], migration["target_storage_path"])
        self.assertEqual(view[0]["mapping_status"], "CONFIRMED")

    def test_runtime_only_and_exporter_anchor_selection(self):
        runtime = self.add_runtime()
        view = self.view()
        self.assertEqual(len(view), 1)
        self.assertEqual(view[0]["source_layer"], "RUNTIME_REGISTRY")
        self.assertEqual(view[0]["asset_id"], runtime["asset_id"])
        self.assertEqual(view[0]["mapping_status"], "RUNTIME_NATIVE")
        package_dir = self.root / exporter.OUTPUT_ROOT
        package_dir.mkdir(parents=True)
        with patch.object(exporter, "ROOT", self.root):
            output = package_dir / exporter.package_name("P1_WAVE1", self.entity, "PROFILE_RIGHT")
            package = exporter.export(self.entity, "PROFILE_RIGHT", output)
            exporter.verify_package(output, package)
        self.assertEqual([item["role"] for item in package["selected_assets"]], ["FACE_FRONT"])
        self.assertEqual(package["selected_assets"][0]["source_layer"], "RUNTIME_REGISTRY")

    def test_exact_cross_source_duplicate_runtime_wins(self):
        self.add_migration()
        runtime = self.add_runtime()
        view = self.view()
        self.assertEqual(len(view), 1)
        self.assertEqual(view[0]["source_layer"], "RUNTIME_REGISTRY")
        self.assertEqual(view[0]["asset_id"], runtime["asset_id"])

    def test_cross_source_different_sha_blocks(self):
        migration = self.add_migration()
        runtime = self.add_runtime()
        runtime["sha256"] = "0" * 64
        self.save()
        with self.assertRaisesRegex(ValueError, "CROSS_SOURCE_SINGLE_CURRENT_CONFLICT"):
            source.eligible_current_assets(self.root, self.entity)
        self.assertNotEqual(migration["sha256"], runtime["sha256"])

    def test_ineligible_lifecycle_usage_mapping_and_asset_class(self):
        self.add_migration("FACE_FRONT", mapping_status="PENDING")
        self.add_runtime("PROFILE_LEFT", lifecycle="SUPERSEDED")
        self.add_runtime("BODY_FRONT", resolver_usage="NEVER")
        self.add_runtime("FACE_3Q_RIGHT", asset_class="COMPOSITE")
        self.assertEqual(self.view(), [])

    def test_absolute_traversal_and_symlink_escape_block(self):
        row = self.add_runtime()
        original = row["storage_uri"]
        for uri in ("/tmp/foreign.png", "../foreign.png", "production/../foreign.png"):
            with self.subTest(uri=uri):
                row["storage_uri"] = uri
                self.save()
                with self.assertRaisesRegex(ValueError, "escape"):
                    source.eligible_current_assets(self.root, self.entity)
        row["storage_uri"] = original
        outside = self.root / "outside.png"
        outside.write_bytes(b"outside")
        link = self.asset_dir / row["filename"]
        link.unlink()
        link.symlink_to(outside)
        self.save()
        with self.assertRaisesRegex(ValueError, "symlink"):
            source.eligible_current_assets(self.root, self.entity)

    def test_sha_mismatch_blocks_runtime(self):
        row = self.add_runtime()
        row["sha256"] = "0" * 64
        self.save()
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            source.eligible_current_assets(self.root, self.entity)


class LiveReadOnlyTests(unittest.TestCase):
    def test_ning_runtime_profile_left_visibility_and_block(self):
        root = Path(__file__).resolve().parents[1]
        view = source.eligible_current_assets(root, "CHAR_NING_QIUSHUI")
        profile = [a for a in view if a["role"] == "PROFILE_LEFT"]
        self.assertEqual(len(profile), 1)
        self.assertEqual(profile[0]["source_layer"], "RUNTIME_REGISTRY")
        self.assertEqual(profile[0]["asset_id"], "AST_IMG_000050")
        self.assertEqual(profile[0]["version_no"], 2)
        self.assertEqual(profile[0]["lifecycle"], "CURRENT")
        self.assertEqual(profile[0]["sha256"],
                         "c53549b0b70de7fdc9da123b351aa37dcf433801b431479750287c73b84440fd")
        registry = [json.loads(line) for line in
                    (root / source.REGISTRY).read_text().splitlines() if line.strip()]
        older = [a for a in registry if a["asset_id"] == "AST_IMG_000049"]
        self.assertEqual(len(older), 1)
        self.assertEqual(older[0]["lifecycle"], "SUPERSEDED")
        with self.assertRaisesRegex(ValueError, "already has a CURRENT asset"):
            exporter.export("CHAR_NING_QIUSHUI", "PROFILE_LEFT",
                            root / exporter.OUTPUT_ROOT / "P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT")

    def test_ning_rear_left_anchor_view(self):
        root = Path(__file__).resolve().parents[1]
        view = source.eligible_current_assets(root, "CHAR_NING_QIUSHUI")
        by_key = {(a["role"], a["variant"], a["state"]): a for a in view}
        expected = ["FACE_FRONT", "REAR_3Q_RIGHT", "FACE_3Q_RIGHT", "BODY_BACK"]
        for role in expected:
            asset = by_key[(role, "DEFAULT", "DEFAULT")]
            self.assertEqual(source.sha256(source.source_path(asset, root)), asset["sha256"])


if __name__ == "__main__":
    unittest.main()
