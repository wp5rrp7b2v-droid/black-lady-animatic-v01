"""D-064 isolated controller tests. Never write formal asset data."""

import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import automatic_ingest_controller_v0_1 as ctl


def run_git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True)


class Fixture(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        run_git(self.root, "init", "-b", "main")
        run_git(self.root, "config", "user.email", "fixture@example.invalid")
        run_git(self.root, "config", "user.name", "D064 Fixture")
        self.manifest = self.root / ctl.MANIFEST
        self.manifest.parent.mkdir(parents=True)
        self.registry = self.root / ctl.REGISTRY
        self.audit = self.root / ctl.AUDIT
        self.relations = self.root / ctl.RELATIONS
        self.registry.parent.mkdir(parents=True)
        self.registry.write_bytes(b"")
        self.audit.write_bytes(b"")
        self.source = self.root / "input" / "CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png"
        self.source.parent.mkdir()
        self.source.write_bytes(ctl.PNG_MAGIC + b"new-version")
        self.manifest_row = {
            "canonical_entity_id": "CHAR_TEST", "new_role": "PROFILE_LEFT",
            "variant": "DEFAULT", "state": "DEFAULT", "version_no": "1",
            "mapping_status": "PENDING", "lifecycle": "SUPERSEDED",
            "canonical_filename": "", "target_storage_path": "", "sha256": "",
        }
        self.write_manifest()
        run_git(self.root, "add", "--", ctl.MANIFEST.as_posix(), ctl.REGISTRY.as_posix(), ctl.AUDIT.as_posix())
        run_git(self.root, "commit", "-m", "fixture baseline")
        self.args = ["controller", "--from-filename", "--po-approved", "--no-pull", "--no-push"]

    def write_manifest(self):
        with self.manifest.open("w", newline="", encoding="utf-8") as out:
            writer = csv.DictWriter(out, fieldnames=list(self.manifest_row))
            writer.writeheader()
            writer.writerow(self.manifest_row)

    def old_current(self, **changes):
        name = "CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png"
        path = self.root / ctl.entity_dir("CHAR_TEST") / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(ctl.PNG_MAGIC + b"old-version")
        row = {
            "asset_id": "AST_IMG_000001", "entity_id": "CHAR_TEST",
            "role": "PROFILE_LEFT", "variant": "DEFAULT", "state": "DEFAULT",
            "version_no": 1, "approval_status": "APPROVED", "lifecycle": "CURRENT",
            "filename": name, "storage_uri": path.relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        row.update(changes)
        self.registry.write_bytes(ctl.jsonl_bytes([row]))
        run_git(self.root, "add", "--", ctl.REGISTRY.as_posix(), path.relative_to(self.root).as_posix())
        run_git(self.root, "commit", "-m", "old current")
        return row

    def call(self, *extra):
        with patch.object(ctl, "repo_root", return_value=self.root), patch.object(sys, "argv", self.args + ["--source", str(self.source)] + list(extra)):
            return ctl.main()

    def rows(self, path):
        return ctl.load_jsonl(path)

    def assert_clean(self):
        self.assertEqual(run_git(self.root, "status", "--porcelain", "--", "production/image_library", "production/asset_registry").stdout, "")

    def test_normal_ingest_regression(self):
        self.source.rename(self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png"))
        self.source = self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png")
        self.assertEqual(self.call(), 0)
        self.assertEqual(self.rows(self.registry)[0]["lifecycle"], "CURRENT")
        self.assertFalse(self.relations.exists())
        self.assertEqual([r["event_type"] for r in self.rows(self.audit)], ["ASSET_APPROVED", "ASSET_INGESTED"])
        self.assert_clean()

    def test_default_current_blocks(self):
        old = self.old_current()
        with self.assertRaisesRegex(ctl.IngestError, "Single Current conflict"):
            self.call()
        self.assertEqual(self.rows(self.registry), [old])
        self.assert_clean()

    def test_controlled_supersession_relation_and_append_only_audit(self):
        old = self.old_current()
        original_audit = ctl.jsonl_bytes([{"event_id": "PREVIOUS", "event_type": "ASSET_INGESTED"}])
        self.audit.write_bytes(original_audit)
        run_git(self.root, "add", "--", ctl.AUDIT.as_posix())
        run_git(self.root, "commit", "-m", "prior audit")
        self.assertEqual(self.call("--supersede-current"), 0)
        rows = self.rows(self.registry)
        self.assertEqual(rows[0], {**old, "lifecycle": "SUPERSEDED"})
        self.assertEqual(rows[1]["lifecycle"], "CURRENT")
        self.assertEqual(rows[1]["version_no"], 2)
        self.assertEqual((rows[1]["authority_class"], rows[1]["resolver_usage"]), ("AUXILIARY", "DEFAULT"))
        relation = self.rows(self.relations)[0]
        self.assertEqual((relation["source_asset_id"], relation["relation_type"], relation["target_asset_id"]),
                         (rows[1]["asset_id"], "SUPERSEDES", old["asset_id"]))
        self.assertTrue(self.audit.read_bytes().startswith(original_audit))
        events = self.rows(self.audit)[1:]
        self.assertEqual([r["event_type"] for r in events], ["ASSET_APPROVED", "ASSET_INGESTED", "ASSET_SUPERSEDED"])
        self.assertEqual(relation["created_by_event_id"], events[2]["event_id"])
        self.assert_clean()

    def test_duplicate_sha_and_version_skip_block(self):
        old = self.old_current()
        self.source.write_bytes((self.root / old["storage_uri"]).read_bytes())
        with self.assertRaisesRegex(ctl.IngestError, "DUPLICATE_BINARY"):
            self.call("--supersede-current")
        self.source.write_bytes(ctl.PNG_MAGIC + b"different")
        skipped = self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V003.png")
        self.source.rename(skipped)
        self.source = skipped
        with self.assertRaisesRegex(ctl.IngestError, "Filename version"):
            self.call("--supersede-current")
        self.assert_clean()

    def test_multiple_current_and_migration_only_block(self):
        old = self.old_current()
        second = {**old, "asset_id": "AST_IMG_000002"}
        self.registry.write_bytes(ctl.jsonl_bytes([old, second]))
        with self.assertRaisesRegex(ctl.IngestError, "exactly one runtime CURRENT"):
            self.call("--supersede-current")
        self.registry.write_bytes(b"")
        self.manifest_row.update(mapping_status="CONFIRMED", lifecycle="CURRENT")
        self.write_manifest()
        with self.assertRaisesRegex(ctl.IngestError, "LEGACY_CURRENT_NOT_RUNTIME_MANAGED"):
            self.call("--supersede-current")

    def test_no_current_and_missing_approval_block(self):
        with self.assertRaisesRegex(ctl.IngestError, "exactly one runtime CURRENT"):
            self.call("--supersede-current")
        self.old_current()
        with patch.object(ctl, "repo_root", return_value=self.root), patch.object(
            sys, "argv", ["controller", "--source", str(self.source), "--from-filename", "--supersede-current", "--dry-run"]
        ):
            with self.assertRaisesRegex(ctl.IngestError, "--po-approved"):
                ctl.main()

    def test_target_exists_and_contradictory_relation_block(self):
        self.old_current()
        target = self.root / ctl.entity_dir("CHAR_TEST") / self.source.name
        target.write_bytes(ctl.PNG_MAGIC + b"occupied")
        with self.assertRaisesRegex(ctl.IngestError, "Target already exists"):
            self.call("--supersede-current")
        target.unlink()
        self.relations.write_bytes(ctl.jsonl_bytes([{
            "source_asset_id": "AST_IMG_000002", "relation_type": "SUPERSEDES",
            "target_asset_id": "AST_IMG_OTHER",
        }]))
        with self.assertRaisesRegex(ctl.IngestError, "Contradictory"):
            self.call("--supersede-current")

    def test_old_path_escape_and_sha_mismatch_block(self):
        old = self.old_current()
        self.registry.write_bytes(ctl.jsonl_bytes([{**old, "storage_uri": "../escape.png"}]))
        with self.assertRaisesRegex(ctl.IngestError, "escape"):
            self.call("--supersede-current")
        self.registry.write_bytes(ctl.jsonl_bytes([{**old, "sha256": "0" * 64}]))
        with self.assertRaisesRegex(ctl.IngestError, "SHA mismatch"):
            self.call("--supersede-current")

    def test_dry_run_has_zero_writes_and_zero_network(self):
        self.old_current()
        before = {p: p.read_bytes() for p in (self.registry, self.audit)}
        original_git = ctl.git
        def guarded_git(repo, *args, **kwargs):
            if any(arg in ("pull", "push", "add", "commit") for arg in args):
                raise AssertionError("dry run tried network or write")
            return original_git(repo, *args, **kwargs)
        with patch.object(ctl, "git", side_effect=guarded_git):
            self.assertEqual(self.call("--supersede-current", "--dry-run"), 0)
        self.assertEqual(before, {p: p.read_bytes() for p in before})
        self.assertFalse(self.relations.exists())
        self.assert_clean()

    def test_failure_injection_rolls_back_all_formal_files(self):
        self.old_current()
        before = {p: p.read_bytes() for p in (self.registry, self.audit)}
        original = ctl.atomic_bytes
        injected = False
        def fail_audit(path, data):
            nonlocal injected
            if path == self.audit and not injected:
                injected = True
                raise OSError("injected audit failure")
            return original(path, data)
        with patch.object(ctl, "atomic_bytes", side_effect=fail_audit):
            with self.assertRaisesRegex(OSError, "injected audit failure"):
                self.call("--supersede-current")
        self.assertEqual(before, {p: p.read_bytes() for p in before})
        self.assertFalse(self.relations.exists())
        self.assertFalse((self.root / ctl.entity_dir("CHAR_TEST") / self.source.name).exists())
        self.assert_clean()


    def _publish_existing(self, filename):
        target = self.root / ctl.entity_dir("CHAR_TEST") / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.source.read_bytes())
        self.source = target
        run_git(self.root, "add", "--", target.relative_to(self.root).as_posix())
        run_git(self.root, "commit", "-m", "publish canonical binary")
        return target

    def test_adopt_existing_is_byte_preserving(self):
        self.source = self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png")
        self.source.write_bytes(ctl.PNG_MAGIC + b"adopt-v1")
        target = self._publish_existing(self.source.name)
        before = target.read_bytes()
        self.assertEqual(self.call("--adopt-existing"), 0)
        self.assertEqual(target.read_bytes(), before)
        row = self.rows(self.registry)[0]
        self.assertEqual((row["version_no"], row["sha256"]), (1, hashlib.sha256(before).hexdigest()))
        self.assertEqual(
            run_git(self.root, "status", "--porcelain", "--", target.relative_to(self.root).as_posix()).stdout,
            "",
        )

    def test_adopt_existing_requires_exact_tracked_clean_target(self):
        self.source = self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png")
        self.source.write_bytes(ctl.PNG_MAGIC + b"adopt-v1")
        canonical = self.root / ctl.entity_dir("CHAR_TEST") / self.source.name
        canonical.parent.mkdir(parents=True, exist_ok=True)
        canonical.write_bytes(self.source.read_bytes())
        with self.assertRaisesRegex(ctl.IngestError, "exact canonical target"):
            self.call("--adopt-existing")
        self.source = canonical
        with self.assertRaisesRegex(ctl.IngestError, "Git-tracked"):
            self.call("--adopt-existing")
        run_git(self.root, "add", "--", canonical.relative_to(self.root).as_posix())
        run_git(self.root, "commit", "-m", "track canonical")
        canonical.write_bytes(ctl.PNG_MAGIC + b"dirty")
        with self.assertRaisesRegex(ctl.IngestError, "no uncommitted changes"):
            self.call("--adopt-existing")

    def test_adopt_existing_explicit_contiguous_version_reservation(self):
        target = self._publish_existing("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png")
        with self.assertRaisesRegex(ctl.IngestError, "acknowledge every skipped version"):
            self.call("--adopt-existing")
        with self.assertRaisesRegex(ctl.IngestError, "acknowledge every skipped version"):
            self.call("--adopt-existing", "--reserve-version", "2")
        self.assertEqual(self.call("--adopt-existing", "--reserve-version", "1"), 0)
        self.assertEqual(self.rows(self.registry)[0]["version_no"], 2)


    def test_adopt_existing_rejects_inspect_mode_combination(self):
        self.source = self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png")
        self.source.write_bytes(ctl.PNG_MAGIC + b"adopt-v1")
        self._publish_existing(self.source.name)
        with patch.object(
            sys,
            "argv",
            self.args + ["--source", str(self.source), "--adopt-existing", "--inspect-current"],
        ):
            with self.assertRaisesRegex(ctl.IngestError, "cannot be combined"):
                ctl.main()

    def test_adopt_existing_failure_rolls_back_without_touching_binary(self):
        self.source = self.source.with_name("CHAR_TEST_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png")
        self.source.write_bytes(ctl.PNG_MAGIC + b"adopt-v1")
        target = self._publish_existing(self.source.name)
        binary_before = target.read_bytes()
        formal_before = {p: p.read_bytes() for p in (self.registry, self.audit)}
        original = ctl.atomic_bytes
        injected = False
        def fail_audit(path, data):
            nonlocal injected
            if path == self.audit and not injected:
                injected = True
                raise OSError("injected adopt audit failure")
            return original(path, data)
        with patch.object(ctl, "atomic_bytes", side_effect=fail_audit):
            with self.assertRaisesRegex(OSError, "injected adopt audit failure"):
                self.call("--adopt-existing")
        self.assertEqual(binary_before, target.read_bytes())
        self.assertEqual(formal_before, {p: p.read_bytes() for p in formal_before})
        self.assert_clean()


if __name__ == "__main__":
    unittest.main()
