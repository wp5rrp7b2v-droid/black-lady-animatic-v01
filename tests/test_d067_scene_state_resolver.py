"""D-067 executable Scene registry and explicit state-resolution tests."""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import resolver_asset_source_v0_1 as source


ROOT = Path(__file__).resolve().parents[1]


class LiveSceneResolverTests(unittest.TestCase):
    def test_castle_day_open_resolves(self):
        result = source.resolve_scene(
            "SCENE_CASTLE_ENTRANCE", {"time_of_day": "DAY", "main_door": "OPEN"})
        self.assertEqual(result["status"], "RESOLVED")
        self.assertEqual(result["asset"]["asset_id"], "AST_IMG_000052")
        self.assertEqual(result["state_profile"], "DAY_DOOR_OPEN")

    def test_first_hall_extinguished_resolves(self):
        result = source.resolve_scene(
            "SCENE_FIRST_HALL",
            {"fireplace_state": "EXTINGUISHED", "fire_visible": False})
        self.assertEqual(result["status"], "RESOLVED")
        self.assertEqual(result["asset"]["asset_id"], "AST_IMG_000053")

    def test_castle_closed_is_gap(self):
        result = source.resolve_scene("SCENE_CASTLE_ENTRANCE", {"main_door": "CLOSED"})
        self.assertEqual(result["status"], "REFERENCE_GAP")

    def test_castle_night_is_gap(self):
        result = source.resolve_scene("SCENE_CASTLE_ENTRANCE", {"time_of_day": "NIGHT"})
        self.assertEqual(result["status"], "REFERENCE_GAP")

    def test_missing_required_state_does_not_select_a_default(self):
        for required_state in (None, {}):
            with self.subTest(required_state=required_state):
                result = source.resolve_scene("SCENE_CASTLE_ENTRANCE", required_state)
                self.assertEqual(result["status"], "REFERENCE_GAP")

    def test_first_hall_burning_is_gap(self):
        result = source.resolve_scene(
            "SCENE_FIRST_HALL", {"fireplace_state": "BURNING"})
        self.assertEqual(result["status"], "REFERENCE_GAP")

    def test_profile_id_can_be_requested_explicitly(self):
        result = source.resolve_scene("SCENE_FIRST_HALL", "FIREPLACE_EXTINGUISHED")
        self.assertEqual(result["status"], "RESOLVED")

    def test_absent_prop_or_costume_is_reference_gap(self):
        for entity_id in ("PROP_UNAVAILABLE", "COSTUME_UNAVAILABLE"):
            with self.subTest(entity_id=entity_id):
                result = source.resolve_entity_reference(entity_id, {"state": "DEFAULT"})
                self.assertEqual(result["status"], "REFERENCE_GAP")

    def test_formalized_files_preserve_approved_source_hashes(self):
        expected = {
            "SCENE_CASTLE_ENTRANCE": "d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961",
            "SCENE_FIRST_HALL": "ce043c8adb244ce8f07a34f1a2b047b4d7ba41f72cdf777e3cd1877f4ac8b413",
        }
        for entity_id, digest in expected.items():
            assets = source.eligible_current_assets(ROOT, entity_id)
            self.assertEqual(len(assets), 1)
            self.assertEqual(assets[0]["sha256"], digest)
            self.assertEqual(source.sha256(source.source_path(assets[0], ROOT)), digest)


class ExplicitUnspecifiedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / source.MANIFEST).parent.mkdir(parents=True)
        (self.root / source.MANIFEST).write_text("[]", encoding="utf-8")
        model = json.loads((ROOT / source.SCENE_PROFILES).read_text(encoding="utf-8"))
        scene = model["scene_entities"][0]
        scene["state_profiles"][0]["facts"]["time_of_day"] = "UNSPECIFIED"
        (self.root / source.SCENE_PROFILES).parent.mkdir(parents=True, exist_ok=True)
        (self.root / source.SCENE_PROFILES).write_text(json.dumps(model), encoding="utf-8")

        live_rows = [json.loads(line) for line in (ROOT / source.REGISTRY).read_text().splitlines()]
        row = next(item for item in live_rows if item["asset_id"] == "AST_IMG_000052")
        destination = self.root / row["storage_uri"]
        destination.parent.mkdir(parents=True)
        shutil.copyfile(ROOT / row["storage_uri"], destination)
        (self.root / source.REGISTRY).write_text(json.dumps(row) + "\n", encoding="utf-8")

    def test_unspecified_does_not_satisfy_explicit_day(self):
        result = source.resolve_scene(
            "SCENE_CASTLE_ENTRANCE", {"time_of_day": "DAY"}, self.root)
        self.assertEqual(result["status"], "REFERENCE_GAP")


if __name__ == "__main__":
    unittest.main()
