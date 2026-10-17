#!/usr/bin/env python3
"""Technical regression for reusable M01 engine, no external model inference."""
import argparse,copy,importlib.util,json,pathlib,subprocess,sys,tempfile,unittest
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("m01_engine_v1",ROOT/"scripts/m01_engine_v1.py")
eng=importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)
PROFILE="NEW02_STYLE_REFERENCE_V001.json"

class M01EngineCoreTests(unittest.TestCase):
 def get(self):
  return eng.read_profile(PROFILE)
 def test_three_configurations_are_valid_and_have_no_coded_scene_name(self):
  ids=[]
  for name in ["N23_STYLE_REFERENCE_V001.json",PROFILE,"N17_APPROVED_VISUAL_RESULT_V001.json"]:
   p=eng.read_profile(name);ids.append(p["profile_id"])
   self.assertGreaterEqual(len(p["fixtures"]),3)
   self.assertFalse(p["release_allowed"])
   self.assertTrue(p["protection"]["do_not_claim_complete_person_protection"])
  self.assertEqual(len(ids),len(set(ids)))
 def test_fails_closed_for_unregistered_or_auto(self):
  for name in ("auto","NONEXISTENT_PROFILE.json","../secret.json"):
   with self.assertRaises(ValueError):
    eng.read_profile(name)
 def test_duplicate_source_identity_cannot_register(self):
  p=self.get()
  p["fixtures"][1]["individual_source_id"]=p["fixtures"][0]["individual_source_id"]
  with self.assertRaises(AssertionError):
   eng.validate(p)
 def test_out_of_bounds_light_roi_cannot_register(self):
  p=self.get()
  p["fixtures"][0]["region"]["roi_px"]=[-1,0,200,200]
  with self.assertRaises(AssertionError):
   eng.validate(p)
 def test_static_frame_determinism_person_exclusion_and_negative_areas(self):
  p=self.get()
  rgb=np.ones((eng.H,eng.W,3),dtype=np.uint8)*75
  # overlap an actual wall-light ROI with a protected region
  person=np.zeros((eng.H,eng.W),bool)
  person[120:250,300:380]=True
  uncertain=np.zeros_like(person)
  uncertain[160:270,420:450]=True
  first,report=eng.calculate_frame(rgb,p,19,19,person,uncertain)
  second,report2=eng.calculate_frame(rgb,p,19,19,person,uncertain)
  self.assertTrue(np.array_equal(first,second))
  self.assertEqual(report,report2)
  self.assertTrue(np.array_equal(first[person|uncertain],rgb[person|uncertain]))
  self.assertTrue(np.array_equal(first[1000:,:,:],rgb[1000:,:,:]))
  self.assertGreater(report["changed"],0)
 def test_visible_flame_guard_and_temporal_gate(self):
  p=eng.read_profile("N17_APPROVED_VISUAL_RESULT_V001.json")
  p["fixtures"]=p["fixtures"][:1]
  rgb=np.ones((eng.H,eng.W,3),dtype=np.uint8)*130
  fl=np.zeros((eng.H,eng.W),bool);fl[50:60,614:624]=True
  protected=np.zeros((eng.H,eng.W),bool);protected[50:54,614:624]=True
  before,stats0=eng.calculate_frame(rgb,p,540,259,protected,None,{1:fl})
  self.assertEqual(stats0["changed"],0)
  visible,stats1=eng.calculate_frame(rgb,p,590,309,protected,None,{1:fl})
  self.assertGreater(stats1["changed"],0)
  self.assertTrue(np.array_equal(visible[protected],rgb[protected]))
  self.assertTrue(np.array_equal(visible[500:,:,:],rgb[500:,:,:]))
 def test_spectral_signals_are_independent_and_deterministic(self):
  a=[eng.signal(i/30,0.3,"unsynced_independent") for i in range(30)]
  b=[eng.signal(i/30,2.0,"unsynced_independent") for i in range(30)]
  self.assertTrue(all(x==y for x,y in zip(a,a)))
  self.assertFalse(all(x==y for x,y in zip(a,b)))
 def test_input_source_and_mask_binary_pinned(self):
  for p in (self.get(),eng.read_profile("N17_APPROVED_VISUAL_RESULT_V001.json")):
   source,mask=eng.load_inputs(p)
   self.assertEqual(eng.sha(source),p["source"]["sha256"])
   if mask:self.assertEqual(eng.sha(mask["path"]),mask["sha256"])
 def test_protected_all_false_positive_light_all_blocked(self):
  p=self.get()
  rgb=np.ones((eng.H,eng.W,3),dtype=np.uint8)*90
  protected=np.ones((eng.H,eng.W),dtype=bool)
  result,q=eng.calculate_frame(rgb,p,22,22,protected)
  self.assertTrue(np.array_equal(result,rgb))
  self.assertEqual(q["changed"],0)

if __name__=="__main__":
 unittest.main(verbosity=2)
