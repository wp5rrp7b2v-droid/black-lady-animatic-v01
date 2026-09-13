"""D-062 role selection and package cleanup checks, isolated from production assets."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reference_package_exporter_v0_1 as exporter


class ExporterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        root_patch = patch.object(exporter, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.entity = "CHAR_TEST"
        self.package_root = self.root / exporter.OUTPUT_ROOT
        self.package_root.mkdir(parents=True)
        self.manifest_path = self.root / exporter.MANIFEST
        self.manifest_path.parent.mkdir(parents=True)
        self.source_dir = self.root / exporter.ASSET_ROOT / "test"
        self.source_dir.mkdir(parents=True)
        self.rows = []

    def add_role(self, role, **changes):
        name = f"{self.entity}_{role}_DEFAULT_DEFAULT_V001.png"
        source = self.source_dir / name
        source.write_bytes((role + " png content").encode())
        row = {
            "canonical_entity_id": self.entity, "new_role": role,
            "variant": "DEFAULT", "state": "DEFAULT",
            "approval_status": "APPROVED", "mapping_status": "CONFIRMED",
            "lifecycle": "CURRENT", "resolver_usage": "DEFAULT",
            "canonical_filename": name,
            "target_storage_path": source.relative_to(self.root).as_posix(),
            "sha256": exporter.sha256(source),
        }
        row.update(changes)
        self.rows.append(row)
        return row

    def save(self):
        self.manifest_path.write_text(json.dumps(self.rows), encoding="utf-8")

    def output(self, role, wave="P1_WAVE1"):
        return self.package_root / exporter.package_name(wave, self.entity, role)

    def test_four_target_role_selection(self):
        for role in {r for anchors in exporter.ANCHORS_BY_TARGET.values() for r, _ in anchors}:
            self.add_role(role)
        for target, anchors in exporter.ANCHORS_BY_TARGET.items():
            with self.subTest(target=target):
                target_rows = [r for r in self.rows if r["new_role"] != target]
                self.manifest_path.write_text(json.dumps(target_rows), encoding="utf-8")
                output = self.output(target)
                package = exporter.export(self.entity, target, output)
                self.assertEqual([x["role"] for x in package["selected_assets"]],
                                 [r for r, _ in anchors])
                self.assertTrue(all(x["selection_reason"] for x in package["selected_assets"]))
                self.assertTrue(package["generated_at"])
                exporter.verify_package(output, package)

    def test_missing_anchor_warns_and_never_uses_never(self):
        self.add_role("FACE_FRONT")
        self.add_role("PROFILE_LEFT", resolver_usage="NEVER")
        self.save()
        package = exporter.export(self.entity, "PROFILE_RIGHT", self.output("PROFILE_RIGHT"))
        self.assertEqual([x["role"] for x in package["selected_assets"]], ["FACE_FRONT"])
        self.assertTrue(any("PROFILE_LEFT" in w for w in package["warnings"]))

    def test_unsupported_target_blocks(self):
        with self.assertRaisesRegex(ValueError, "Unsupported target role"):
            exporter.export(self.entity, "BODY_FRONT", self.package_root / "wrong")

    def test_existing_current_target_blocks(self):
        self.add_role("PROFILE_LEFT")
        self.save()
        with self.assertRaisesRegex(ValueError, "already has a CURRENT"):
            exporter.export(self.entity, "PROFILE_LEFT", self.output("PROFILE_LEFT"))

    def test_duplicate_eligible_current_blocks(self):
        self.add_role("FACE_FRONT")
        self.rows.append(dict(self.rows[0]))
        self.save()
        with self.assertRaisesRegex(ValueError, "Duplicate eligible CURRENT"):
            exporter.export(self.entity, "PROFILE_LEFT", self.output("PROFILE_LEFT"))

    def test_cleanup_across_roles_preserves_unknown_and_production(self):
        self.add_role("FACE_FRONT")
        self.save()
        old_left = self.output("PROFILE_LEFT")
        old_right = self.output("REAR_3Q_RIGHT")
        current = self.output("REAR_3Q_LEFT")
        exporter.export(self.entity, "PROFILE_LEFT", old_left)
        exporter.export(self.entity, "REAR_3Q_RIGHT", old_right)
        package = exporter.export(self.entity, "REAR_3Q_LEFT", current)
        unknown = self.package_root / "personal_notes"
        unknown.mkdir()
        production = self.root / "production" / "keep.txt"
        production.write_text("untouched")
        self.assertEqual(exporter.cleanup_old_reference_packages(current), 2)
        self.assertFalse(old_left.exists())
        self.assertFalse(old_right.exists())
        self.assertTrue(current.exists())
        self.assertTrue(unknown.exists())
        self.assertEqual(production.read_text(), "untouched")
        exporter.verify_package(current, package)

    def test_cleanup_rejects_unverified_current_and_symlink_escape(self):
        self.add_role("FACE_FRONT")
        self.save()
        old = self.output("PROFILE_LEFT")
        current = self.output("REAR_3Q_LEFT")
        exporter.export(self.entity, "PROFILE_LEFT", old)
        exporter.export(self.entity, "REAR_3Q_LEFT", current)
        (current / "package.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "failed exporter verification"):
            exporter.cleanup_old_reference_packages(current)
        self.assertTrue(old.exists())
        outside = self.root / "production" / "outside"
        outside.mkdir(parents=True)
        link = self.package_root / "P1_WAVE1_TEST_REAR_3Q_RIGHT"
        link.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "outside"):
            exporter.cleanup_old_reference_packages(link)
        self.assertTrue(outside.is_dir())

    def test_symlink_old_package_blocks_cleanup_without_deleting_verified_old(self):
        self.add_role("FACE_FRONT")
        self.save()
        old = self.output("PROFILE_LEFT")
        current = self.output("REAR_3Q_LEFT")
        exporter.export(self.entity, "PROFILE_LEFT", old)
        exporter.export(self.entity, "REAR_3Q_LEFT", current)
        outside = self.root / "production" / "outside"
        outside.mkdir(parents=True)
        (self.package_root / "suspicious_link").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            exporter.cleanup_old_reference_packages(current)
        self.assertTrue(old.exists())
        self.assertTrue(current.exists())
        self.assertTrue(outside.exists())

    def test_output_path_escape_blocks(self):
        self.add_role("FACE_FRONT")
        self.save()
        outside = self.root / "production" / "P1_WAVE1_TEST_PROFILE_LEFT"
        with self.assertRaisesRegex(ValueError, "direct child"):
            exporter.export(self.entity, "PROFILE_LEFT", outside)
        self.assertFalse(outside.exists())


if __name__ == "__main__":
    unittest.main()
