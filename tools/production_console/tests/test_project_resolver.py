import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

from project_resolver import resolve_from_state, infer_current_shot_id


class ProjectResolverTests(unittest.TestCase):
    def sample_state(self):
        return {
            "current_task": "N25｜CANDIDATE 01｜WAITING PRODUCT OWNER FORMAL WORK AUTHORIZATION",
            "n25_director_design_v0_3": {
                "status": "PRODUCT OWNER APPROVED / LOCKED",
                "path": "director.md",
            },
            "n25_scene_reference_design_v0_1": {
                "status": "PRODUCT OWNER APPROVED / LOCKED",
                "path": "scene.md",
            },
            "n25_reference_delivery_bundle_v001": {
                "status": "FORMAL BUILD PASS / ARTIFACT EXACT VERIFIED / 5 OF 5 MATCH",
                "artifact_name": "N25_REFERENCE_DELIVERY_BUNDLE_V001",
                "run_id": 37460860156,
                "artifact_id": 11411667773,
                "artifact_digest": "sha256:abc",
                "direct_image_count": 5,
                "reference_exact_match": "5/5",
                "manifest_result": "PASS",
                "handoff_verified": True,
                "downloaded_zip_digest_match": True,
                "candidate_01_generation_authorized": False,
            },
        }

    def test_infer_current_shot(self):
        self.assertEqual(infer_current_shot_id(self.sample_state()), "N25")

    def test_resolve_package_metadata(self):
        r = resolve_from_state(self.sample_state())
        self.assertEqual(r["shot_id"], "N25")
        self.assertTrue(r["package_ready"])
        self.assertFalse(r["generation_authorized"])
        self.assertEqual(r["bundle"]["run_id"], 37460860156)
        self.assertEqual(r["bundle"]["artifact_id"], 11411667773)
        self.assertEqual(r["bundle"]["reference_count"], 5)
        self.assertTrue(r["bundle"]["references_exact"])
        self.assertTrue(r["bundle"]["delivery_manifest_verified"])
        self.assertFalse(r["bundle"]["generation_allowed"])

    def test_current_shot_without_bundle_returns_partial_state(self):
        state = {
            "current_task": "N26｜DIRECTOR DESIGN｜NOT YET STARTED",
            "session_status": "N25 CLOSED / N26 NEXT",
        }
        r = resolve_from_state(state)
        self.assertEqual(r["shot_id"], "N26")
        self.assertFalse(r["package_ready"])
        self.assertFalse(r["generation_authorized"])
        self.assertEqual(r["resolution_state"], "PARTIAL_CURRENT_SHOT")
        self.assertIsNone(r["bundle"]["bundle_id"])
        self.assertEqual(r["bundle"]["reference_count"], 0)
        self.assertFalse(r["bundle"]["references_exact"])
        self.assertFalse(r["bundle"]["delivery_manifest_verified"])


    def test_resolve_nested_formal_build_metadata_for_closed_shot_replay(self):
        state = {
            "current_task": "N26 CLOSEOUT COMPLETE",
            "n26_director_design_v0_1": {
                "status": "PRODUCT OWNER APPROVED / LOCKED",
                "path": "director.md",
            },
            "n26_scene_reference_design_v0_2": {
                "status": "PRODUCT OWNER APPROVED / LOCKED",
                "path": "scene.md",
            },
            "n26_reference_delivery_bundle_v002": {
                "status": "FORMAL BUILD PASS / ARTIFACT EXACT VERIFIED / CONSUMED BY N26 CANDIDATE 02 GENERATION / FINAL SHOT CLOSED",
                "direct_image_count": 5,
                "candidate_02_generation_authorized": True,
                "formal_build": {
                    "workflow_run_id": 37553891715,
                    "artifact_id": 11453927794,
                    "artifact_name": "N26_REFERENCE_DELIVERY_BUNDLE_V002",
                    "artifact_digest": "sha256:f7fdb72e",
                    "zip_digest_match": True,
                    "reference_exact_match": "5/5",
                    "work_handoff": "PASS",
                    "overall_result": "PASS",
                },
            },
        }
        r = resolve_from_state(state, shot_id="N26")
        self.assertTrue(r["package_ready"])
        self.assertTrue(r["generation_authorized"])
        self.assertEqual(r["resolution_state"], "READY")
        self.assertEqual(r["bundle"]["bundle_id"], "N26_REFERENCE_DELIVERY_BUNDLE_V002")
        self.assertEqual(r["bundle"]["run_id"], 37553891715)
        self.assertEqual(r["bundle"]["artifact_id"], 11453927794)
        self.assertEqual(r["bundle"]["reference_count"], 5)
        self.assertTrue(r["bundle"]["references_exact"])
        self.assertTrue(r["bundle"]["delivery_manifest_verified"])


if __name__ == "__main__":
    unittest.main()
