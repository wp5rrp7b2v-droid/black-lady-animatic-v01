import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"app"))
from state_store import default_session
from qualification import publication_payload,registration_payload,lock_payload

class PayloadTests(unittest.TestCase):
    def setUp(self):
        self.s=default_session("N24_QA_001","N24")
        self.s["bundle"]={"bundle_id":"B","run_id":1,"artifact_id":2,"artifact_digest":"sha256:x","reference_count":2,"references_exact":True,"generation_allowed":True}
        self.s["candidate"]={"shot_id":"N24","candidate_id":"CANDIDATE_01","drive_file_id":"d","sha256":"a"*64,"byte_size":10,"width":941,"height":1672,"mime_type":"image/png"}
        self.s["approval"]={"binding":{"candidate_id":"CANDIDATE_01","drive_file_id":"d","sha256":"a"*64}}

    def test_publication_is_qualification_only(self):
        _,p=publication_payload(self.s)
        self.assertTrue(p["qualification_only"])
        self.assertFalse(p["safety"]["formal_story_shot"])
        self.assertFalse(p["safety"]["main_branch_write"])
        self.assertFalse(p["safety"]["project_control_write"])

    def test_registration_binds_publication(self):
        _,p=registration_payload(self.s,{"sha":"blob1"})
        self.assertEqual(p["publication_binding"]["blob_sha"],"blob1")

    def test_lock_binds_both(self):
        _,p=lock_payload(self.s,{"sha":"blob1"},{"sha":"blob2"})
        self.assertEqual(p["publication_binding"]["blob_sha"],"blob1")
        self.assertEqual(p["registration_binding"]["blob_sha"],"blob2")

if __name__=="__main__": unittest.main()
