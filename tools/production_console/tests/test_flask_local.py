import os
import sys
import tempfile
import unittest
from pathlib import Path

TMP=tempfile.TemporaryDirectory()
os.environ["BLACK_LADY_PRIVATE_DIR"]=TMP.name
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"app"))
import server

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

if __name__=="__main__": unittest.main()
