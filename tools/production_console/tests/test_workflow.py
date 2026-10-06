import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"app"))
from state_store import default_session
from workflow import transition,candidate_identity,identity_complete,binding_matches

class WorkflowTests(unittest.TestCase):
    def test_happy_path(self):
        s=default_session("N24_QA_001","N24")
        for status in ["DESIGN_APPROVED","PREFLIGHT_PASS","AWAITING_CANDIDATE","CANDIDATE_VERIFIED_PENDING_PO","PO_APPROVED_PENDING_PUBLICATION","PUBLISHED_NOT_REGISTERED","REGISTERED_PENDING_LOCK","LOCKED_PENDING_CLOSEOUT","CLOSED"]:
            transition(s,status)
        self.assertEqual(s["status"],"CLOSED")

    def test_invalid_transition_fails_closed(self):
        s=default_session("N24_QA_002","N24")
        with self.assertRaises(ValueError):
            transition(s,"PUBLISHED_NOT_REGISTERED")

    def test_rejected_requires_explicit_recovery(self):
        s=default_session("N24_QA_003","N24")
        for status in ["DESIGN_APPROVED","PREFLIGHT_PASS","AWAITING_CANDIDATE","CANDIDATE_VERIFIED_PENDING_PO","REJECTED"]:
            transition(s,status)
        with self.assertRaises(ValueError):
            transition(s,"AWAITING_CANDIDATE")

    def test_identity_binding(self):
        c={"shot_id":"N24","candidate_id":"CANDIDATE_01","drive_file_id":"d1","sha256":"a"*64,"byte_size":12,"width":941,"height":1672,"mime_type":"image/png"}
        self.assertTrue(identity_complete(c))
        self.assertEqual(candidate_identity(c)["shot_id"],"N24")
        self.assertTrue(binding_matches(c,{"candidate_id":"CANDIDATE_01","drive_file_id":"d1","sha256":"a"*64}))
        self.assertFalse(binding_matches(c,{"candidate_id":"CANDIDATE_01","drive_file_id":"d2","sha256":"a"*64}))

if __name__=="__main__": unittest.main()
