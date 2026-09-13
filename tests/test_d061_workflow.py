"""Isolated D-061 safety checks; never writes the production registry."""

import contextlib
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import automatic_ingest_controller_v0_1 as ingest
import reference_package_exporter_v0_1 as exporter


class ReferenceCleanupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.patch_root = patch.object(exporter, "ROOT", self.root)
        self.patch_root.start()
        self.addCleanup(self.patch_root.stop)
        self.packages = self.root / exporter.OUTPUT_ROOT
        self.packages.mkdir(parents=True)
        self.source = self.root / exporter.ASSET_ROOT / "ning_qiushui" / "anchor.png"
        self.source.parent.mkdir(parents=True)
        self.source.write_bytes(exporter.sha256.__name__.encode())
        self.digest = hashlib.sha256(self.source.read_bytes()).hexdigest()
        manifest = self.root / exporter.MANIFEST
        manifest.parent.mkdir(parents=True)
        self.row = {
            "canonical_entity_id": "CHAR_NING_QIUSHUI", "new_role": "FACE_FRONT",
            "variant": "DEFAULT", "state": "DEFAULT", "approval_status": "APPROVED",
            "mapping_status": "CONFIRMED", "lifecycle": "CURRENT",
            "resolver_usage": "DEFAULT", "canonical_filename": "anchor.png",
            "target_storage_path": self.source.relative_to(self.root).as_posix(),
            "sha256": self.digest,
        }
        manifest.write_text(json.dumps([self.row]), encoding="utf-8")

    def old_package(self, name):
        old = self.packages / name
        old.mkdir()
        (old / "anchor.png").write_bytes(self.source.read_bytes())
        (old / "package.json").write_text(json.dumps({
            "entity_id": "CHAR_NING_QIUSHUI",
            "target_role": "PROFILE_LEFT",
            "source_manifest": exporter.MANIFEST.as_posix(),
            "selected_assets": [{"canonical_filename": "anchor.png", "sha256": self.digest}],
        }), encoding="utf-8")
        return old

    def test_new_verified_package_cleans_two_old_packages_only(self):
        old1 = self.old_package("P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT")
        old2 = self.old_package("P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT_20260913T120000000000Z")
        unrelated = self.packages / "personal_notes"
        unrelated.mkdir()
        output = self.packages / "P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT_20260913T130000000000Z"
        before = self.source.read_bytes()
        package = exporter.export("CHAR_NING_QIUSHUI", "PROFILE_LEFT", output)
        self.assertEqual(exporter.cleanup_old_reference_packages(output), 2)
        self.assertFalse(old1.exists())
        self.assertFalse(old2.exists())
        self.assertTrue(unrelated.exists())
        self.assertTrue((output / "package.json").is_file())
        self.assertTrue((output / "anchor.png").is_file())
        self.assertEqual(len(package["selected_assets"]), 1)
        self.assertEqual(self.source.read_bytes(), before)

    def test_failed_export_preserves_old_package(self):
        old = self.old_package("P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT")
        self.row["sha256"] = "wrong"
        (self.root / exporter.MANIFEST).write_text(json.dumps([self.row]), encoding="utf-8")
        output = self.packages / "P1_WAVE1_NING_QIUSHUI_PROFILE_LEFT_new"
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            exporter.export("CHAR_NING_QIUSHUI", "PROFILE_LEFT", output)
        self.assertTrue(old.is_dir())
        self.assertFalse(output.exists())

    def test_cleanup_rejects_path_outside_root(self):
        outside = self.root / "production" / "asset"
        outside.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "outside"):
            exporter.cleanup_old_reference_packages(outside)
        self.assertTrue(outside.is_dir())


class FilenameAndDryRunTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = [{"canonical_entity_id": "CHAR_NING_QIUSHUI",
                          "variant": "DEFAULT", "state": "DEFAULT",
                          "mapping_status": "CONFIRMED"}]

    def test_canonical_filename_parser(self):
        for role in ("PROFILE_LEFT", "REAR_3Q_LEFT"):
            name = f"CHAR_NING_QIUSHUI_{role}_DEFAULT_DEFAULT_V001.png"
            self.assertEqual(ingest.parse_canonical_filename(name, self.manifest, []),
                             ("CHAR_NING_QIUSHUI", role, "DEFAULT", "DEFAULT", 1))
        for name in ("CHAR_NING_QIUSHUI_UNKNOWN_DEFAULT_DEFAULT_V001.png",
                     "CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V1.png",
                     "CHAR_UNKNOWN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png"):
            with self.assertRaises(ingest.IngestError):
                ingest.parse_canonical_filename(name, self.manifest, [])

    def run_dry(self, version):
        source = self.root / f"CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V{version:03d}.png"
        source.write_bytes(ingest.PNG_MAGIC + b"test")
        calls = []

        def fake_git(_repo, *args, **_kwargs):
            calls.append(args)
            self.assertEqual(args, ("diff", "--cached", "--name-only"))
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

        argv = ["ingest", "--source", str(source), "--from-filename",
                "--po-approved", "--dry-run"]
        with patch.object(sys, "argv", argv), patch.object(ingest, "repo_root", return_value=self.root), \
                patch.object(ingest, "load_manifest", return_value=self.manifest), \
                patch.object(ingest, "load_jsonl", return_value=[]), \
                patch.object(ingest, "git", side_effect=fake_git), \
                contextlib.redirect_stdout(io.StringIO()) as output:
            if version == 1:
                self.assertEqual(ingest.main(), 0)
                self.assertEqual(json.loads(output.getvalue())["status"], "DRY_RUN")
            else:
                with self.assertRaisesRegex(ingest.IngestError, "does not match next version"):
                    ingest.main()
        self.assertEqual(calls, [("diff", "--cached", "--name-only")])
        self.assertFalse((self.root / ingest.REGISTRY).exists())

    def test_dry_run_has_no_network_or_writes(self):
        self.run_dry(1)

    def test_filename_version_mismatch_blocks(self):
        self.run_dry(2)


if __name__ == "__main__":
    unittest.main()
