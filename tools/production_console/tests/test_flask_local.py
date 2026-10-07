import os
import sys
import tempfile
import unittest
import hashlib
from io import BytesIO
from pathlib import Path

TMP=tempfile.TemporaryDirectory()
os.environ["BLACK_LADY_PRIVATE_DIR"]=TMP.name
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"app"))
import server
import routes_session
import qualification
from state_store import acquire_candidate_lock, release_candidate_lock
from PIL import Image

class FlaskLocalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client=server.app.test_client()

    @classmethod
    def tearDownClass(cls):
        TMP.cleanup()

    def test_health(self):
        r=self.client.get("/health")
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.get_json()["service"],"BLACK_LADY_PRODUCTION_CONSOLE_V1_1")
        self.assertEqual(r.get_json()["production_process_boundary"],"FORMAL_STORY_SHOT_WORKFLOW_UNCHANGED")

    def test_status_exposes_current_main_sha(self):
        orig_gh = routes_session.gh_binary
        orig_main_meta = routes_session.main_meta
        try:
            routes_session.gh_binary = lambda: "/usr/bin/gh"
            routes_session.main_meta = lambda: {"commit": {"sha": "abc123main"}}
            r=self.client.get("/api/v1/status")
            self.assertEqual(r.status_code,200)
            self.assertEqual(r.get_json()["github_main_sha"],"abc123main")
        finally:
            routes_session.gh_binary = orig_gh
            routes_session.main_meta = orig_main_meta

    def test_session_design_flow(self):
        body={"session_id":"N24_QA_LOCAL","shot_id":"N24","mode":"QUALIFICATION","bundle":{"bundle_id":"B","run_id":1,"artifact_id":2,"artifact_digest":"sha256:x","reference_count":2,"references_exact":True,"generation_allowed":True}}
        r=self.client.post("/api/v1/session/start",json=body)
        self.assertEqual(r.status_code,200)
        r=self.client.post("/api/v1/design/approve",json={"session_id":"N24_QA_LOCAL"})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.get_json()["session"]["status"],"DESIGN_APPROVED")

    def test_production_mode_rejected(self):
        r=self.client.post("/api/v1/session/start",json={"session_id":"BAD","shot_id":"N24","mode":"PRODUCTION"})
        self.assertEqual(r.status_code,409)

    def test_design_package_resolver_endpoint(self):
        orig = routes_session.resolve_project_design_package
        try:
            routes_session.resolve_project_design_package = lambda shot_id=None: {
                "shot_id": shot_id or "N25",
                "package_ready": True,
                "generation_authorized": False,
                "bundle": {
                    "bundle_id": "N25_REFERENCE_DELIVERY_BUNDLE_V001",
                    "run_id": 37460860156,
                    "artifact_id": 11411667773,
                    "artifact_digest": "sha256:abc",
                    "reference_count": 5,
                    "references_exact": True,
                    "delivery_manifest_verified": True,
                    "generation_allowed": False,
                },
                "design_package": {},
                "project_control": {"next_action": "WAITING PO"},
                "source": {"project_state_path": "project_state.json"},
            }
            resp = self.client.get("/api/v1/design-package/resolve?shot_id=N25")
            self.assertEqual(resp.status_code, 200)
            data = resp.get_json()["resolved"]
            self.assertEqual(data["shot_id"], "N25")
            self.assertTrue(data["package_ready"])
            self.assertFalse(data["bundle"]["generation_allowed"])
        finally:
            routes_session.resolve_project_design_package = orig

    def test_preflight_rejects_cross_session_drive_folder(self):
        session={
            "session_id":"Q4_SESSION",
            "shot_id":"TEST_Q4",
            "status":"DESIGN_APPROVED",
            "bundle":{
                "bundle_id":"Q4_BUNDLE",
                "run_id":1,
                "artifact_id":1,
                "artifact_digest":"sha256:x",
                "reference_count":1,
                "references_exact":True,
                "delivery_manifest_verified":True,
                "generation_allowed":True,
            },
            "lock":{},
        }
        orig_branch=qualification.branch_meta
        orig_main=qualification.main_meta
        orig_get=qualification.get_file
        try:
            qualification.branch_meta=lambda branch:{"commit":{"sha":"q"}}
            qualification.main_meta=lambda:{"commit":{"sha":"m"}}
            qualification.get_file=lambda branch,path:None
            bad=qualification.preflight(session,True,True,"OTHER_SESSION")
            self.assertFalse(bad["pass"])
            self.assertFalse(bad["checks"]["drive_folder_matches_session"])
            good=qualification.preflight(session,True,True,"Q4_SESSION")
            self.assertTrue(good["pass"])
            self.assertTrue(good["checks"]["drive_folder_matches_session"])
        finally:
            qualification.branch_meta=orig_branch
            qualification.main_meta=orig_main
            qualification.get_file=orig_get

    def test_candidate_upload_lock(self):
        lock = acquire_candidate_lock("LOCK_QA", "CANDIDATE_01")
        try:
            with self.assertRaises(RuntimeError):
                acquire_candidate_lock("LOCK_QA", "CANDIDATE_01")
        finally:
            release_candidate_lock(lock)

    def test_true_external_recovery_without_local_session(self):
        bio=BytesIO()
        Image.new("RGB",(2,3)).save(bio,format="PNG")
        raw=bio.getvalue()
        digest=hashlib.sha256(raw).hexdigest()
        identity={
            "shot_id":"TEST_RECOVER",
            "candidate_id":"CANDIDATE_01",
            "drive_file_id":"drive-recover-1",
            "sha256":digest,
            "byte_size":len(raw),
            "width":2,
            "height":3,
            "mime_type":"image/png",
        }
        evidence={
            "highest_remote_status":"CLOSED",
            "records":{
                "publication":{"exists":True,"path":"p.json","blob_sha":"bp","payload":{
                    "shot_id":"TEST_RECOVER",
                    "bundle":{"bundle_id":"B","run_id":1,"artifact_id":2,"artifact_digest":"sha256:x","reference_count":1,"references_exact":True,"delivery_manifest_verified":True,"generation_allowed":True},
                    "candidate":identity,
                    "approval_binding":{"candidate_id":"CANDIDATE_01","drive_file_id":"drive-recover-1","sha256":digest},
                }},
                "registration":{"exists":True,"path":"r.json","blob_sha":"br","payload":{"candidate_identity":identity}},
                "lock":{"exists":True,"path":"l.json","blob_sha":"bl","payload":{"immutable_identity":identity}},
                "closeout":{"exists":True,"path":"c.json","blob_sha":"bc","payload":{"immutable_identity":identity}},
            },
        }
        orig_remote=routes_session.remote_evidence
        orig_download=routes_session.drive_download_bytes
        try:
            routes_session.remote_evidence=lambda session_id:evidence
            routes_session.drive_download_bytes=lambda file_id:raw
            resp=self.client.post("/api/v1/session/recover",json={"session_id":"RECOVER_ONLY"})
            self.assertEqual(resp.status_code,200)
            data=resp.get_json()
            self.assertTrue(data["recovered"])
            self.assertEqual(data["session"]["status"],"CLOSED")
            self.assertEqual(data["session"]["candidate"]["sha256"],digest)
        finally:
            routes_session.remote_evidence=orig_remote
            routes_session.drive_download_bytes=orig_download

if __name__=="__main__": unittest.main()
