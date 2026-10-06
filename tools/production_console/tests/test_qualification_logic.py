import base64
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

import qualification as q


class QualificationLogicTests(unittest.TestCase):
    def setUp(self):
        self.store = {}
        self.main_sha = "main-fixed-sha"

        self.orig_get_file = q.get_file
        self.orig_exact_create = q.exact_create_or_read
        self.orig_main_meta = q.main_meta
        self.orig_branch_meta = q.branch_meta

        def fake_main_meta():
            return {"commit": {"sha": self.main_sha}}

        def fake_branch_meta(branch):
            return {"name": branch, "commit": {"sha": "qualification-head"}}

        def fake_get_file(branch, path):
            return self.store.get((branch, path))

        def fake_exact_create(branch, path, desired_bytes, message):
            key = (branch, path)
            existing = self.store.get(key)
            if existing:
                decoded = base64.b64decode(existing["content"])
                if decoded != desired_bytes:
                    raise RuntimeError("existing content mismatch")
                return {
                    "outcome": "ALREADY_EXISTS",
                    "github_write": 0,
                    "commit_sha": None,
                    "meta": existing,
                    "readback_exact": True,
                }
            blob = "blob-" + str(len(self.store) + 1)
            meta = {
                "sha": blob,
                "content": base64.b64encode(desired_bytes).decode("ascii"),
            }
            self.store[key] = meta
            return {
                "outcome": "CREATED",
                "github_write": 1,
                "commit_sha": "commit-" + str(len(self.store)),
                "meta": meta,
                "readback_exact": True,
            }

        q.main_meta = fake_main_meta
        q.branch_meta = fake_branch_meta
        q.get_file = fake_get_file
        q.exact_create_or_read = fake_exact_create

        self.session = {
            "session_id": "N24_UI_QA_001",
            "shot_id": "N24",
            "bundle": {
                "bundle_id": "N24_REFERENCE_DELIVERY_BUNDLE_V001",
                "run_id": 1,
                "artifact_id": 2,
                "artifact_digest": "sha256:abc",
                "reference_count": 2,
                "references_exact": True,
                "delivery_manifest_verified": True,
                "generation_allowed": True,
            },
            "candidate": {
                "shot_id": "N24",
                "candidate_id": "CANDIDATE_01",
                "drive_file_id": "drive-file-1",
                "sha256": "a" * 64,
                "byte_size": 1234,
                "width": 941,
                "height": 1672,
                "mime_type": "image/png",
            },
            "approval": {
                "action": "approve",
                "binding": {
                    "candidate_id": "CANDIDATE_01",
                    "drive_file_id": "drive-file-1",
                    "sha256": "a" * 64,
                },
            },
        }

    def tearDown(self):
        q.get_file = self.orig_get_file
        q.exact_create_or_read = self.orig_exact_create
        q.main_meta = self.orig_main_meta
        q.branch_meta = self.orig_branch_meta

    def test_full_remote_chain_reaches_closed(self):
        p = q.publish(self.session)
        self.assertEqual(p["outcome"], "CREATED")

        r = q.register(self.session)
        self.assertEqual(r["outcome"], "CREATED")
        publication_blob = r["publication_blob_before"]

        # ACK-loss style retry: publication must remain byte-identical and registration is idempotent.
        r2 = q.register(self.session)
        self.assertEqual(r2["outcome"], "ALREADY_EXISTS")
        self.assertEqual(r2["publication_blob_before"], publication_blob)
        self.assertEqual(r2["publication_blob_after"], publication_blob)

        l = q.lock(self.session)
        self.assertEqual(l["outcome"], "CREATED")

        c = q.closeout(self.session)
        self.assertEqual(c["outcome"], "CREATED")

        evidence = q.remote_evidence(self.session["session_id"])
        self.assertEqual(evidence["highest_remote_status"], "CLOSED")
        self.assertTrue(evidence["records"]["publication"]["exists"])
        self.assertTrue(evidence["records"]["registration"]["exists"])
        self.assertTrue(evidence["records"]["lock"]["exists"])
        self.assertTrue(evidence["records"]["closeout"]["exists"])

    def test_registration_without_publication_is_rejected(self):
        paths = q.paths_for(self.session["session_id"])
        payload = {"bad": True}
        raw = (json.dumps(payload) + "\n").encode("utf-8")
        self.store[(q.QUALIFICATION_BRANCH, paths["registration"])] = {
            "sha": "bad-reg",
            "content": base64.b64encode(raw).decode("ascii"),
        }
        with self.assertRaises(RuntimeError):
            q.remote_evidence(self.session["session_id"])


if __name__ == "__main__":
    unittest.main()
