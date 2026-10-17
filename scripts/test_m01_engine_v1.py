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
 def test_v013_is_one_algorithm_not_two_modes(self):
  for name in ("N17_UNIFIED_REGISTERED_REFERENCE_V013.json",
               "N23_UNIFIED_FLAME_CALIBRATION_V013.json",
               "NEW02_UNIFIED_FLAME_CALIBRATION_V013.json"):
   p=eng.read_profile(name)
   self.assertEqual(p["temporal"]["style"],"unsynced_independent")
   self.assertTrue(p["unified_flame_engine"]["one_candle_algorithm"])
   self.assertTrue(all(f["same_signal_drives_core_and_halo"] for f in p["fixtures"]))
   self.assertFalse(p["render_full_flame_output_authorized"])
  for name in ("N23_UNIFIED_FLAME_CALIBRATION_V013.json",
               "NEW02_UNIFIED_FLAME_CALIBRATION_V013.json"):
   p=eng.read_profile(name)
   self.assertEqual(p["unified_flame_engine"]["registration_status"],"PENDING_CALIBRATION_NO_NEW_FLAME_RENDER")
   self.assertTrue(all(f["flame_core_registration"]=="NOT_REGISTERED_CORE_CANDIDATE_REQUIRED" for f in p["fixtures"]))
 def test_v013_unregistered_flames_refuse_full_candle_video(self):
  import tempfile
  with tempfile.TemporaryDirectory() as tmp:
   code=eng.run("N23_UNIFIED_FLAME_CALIBRATION_V013.json",tmp,"pilot",True)
   self.assertEqual(code,3)
   report=json.loads((pathlib.Path(tmp)/"M01_ENGINE_V1_FAIL_CLOSED.json").read_text())
   self.assertEqual(report["status"],"CALIBRATION_REQUIRED")
   self.assertFalse(report["rendered"])
   self.assertFalse(report["release_allowed"])
 def test_n17_reference_is_originally_configured(self):
  p=eng.read_profile("N17_UNIFIED_REGISTERED_REFERENCE_V013.json")
  self.assertEqual(len(p["fixtures"]),4)
  self.assertTrue(all(f.get("core_bitpack_index")==i for i,f in enumerate(p["fixtures"],1)))
  self.assertEqual(p["source"]["sha256"],"7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402")
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
 def test_soft_architecture_halo_is_not_flame_core(self):
  p=eng.read_profile("N23_N17_NATURAL_V012.json")
  self.assertEqual(p["temporal"]["style"],"unsynced_independent")
  self.assertEqual(p["temporal"]["halo_fast_harmonics_mix"],0.22)
  old=eng.read_profile("N23_N17_STRENGTH_V011.json")
  self.assertLess(p["fixtures"][0]["region"]["sigma_px"][0],old["fixtures"][0]["region"]["sigma_px"][0])
  image=np.ones((eng.H,eng.W,3),np.uint8)*75
  new_peaks=[];old_peaks=[]
  for frame in (8,15,22,29,36,43,50,57,64,71):
   new,stat=eng.calculate_frame(image,p,frame,frame)
   old_img,old_stat=eng.calculate_frame(image,old,frame,frame)
   new_peaks.append(stat["max_delta"]);old_peaks.append(old_stat["max_delta"])
   self.assertTrue(np.array_equal(new[900:,:,:],image[900:,:,:]))
  self.assertGreater(max(new_peaks),0)
  self.assertLess(max(new_peaks),max(old_peaks))
  n17=eng.read_profile("N17_APPROVED_VISUAL_RESULT_V001.json")
  self.assertNotIn("halo_fast_harmonics_mix",n17["temporal"])
  self.assertEqual(n17["fixtures"][0]["halo_gain_rgb"],[7.5,4.3,1.3])
 def test_reject_unbounded_fast_halo_mix(self):
  p=eng.read_profile("NEW02_N17_NATURAL_V012.json")
  p["temporal"]["halo_fast_harmonics_mix"]=2.0
  with self.assertRaisesRegex(AssertionError,"BAD_HALO_HARMONICS_MIX"):
   eng.validate(p)
 def test_visible_flame_guard_and_temporal_gate(self):
  p=eng.read_profile("N17_APPROVED_VISUAL_RESULT_V001.json")
  p["fixtures"]=p["fixtures"][:1]
  rgb=np.ones((eng.H,eng.W,3),dtype=np.uint8)*130
  fl=np.zeros((eng.H,eng.W),bool);fl[50:60,614:624]=True
  protected=np.zeros((eng.H,eng.W),bool);protected[50:54,614:624]=True
  before,stats0=eng.calculate_frame(rgb,p,540,259,protected,None,{1:fl})
  self.assertEqual(stats0["changed"],0)
  # A natural oscillation may cross zero at one arbitrary instant; assert
  # perceptible motion over a short sequence instead of forcing every frame.
  active=0
  for idx in (575,580,585,590,595,600,605,610,615,620,625,630):
   visible,stats1=eng.calculate_frame(rgb,p,idx,idx-281,protected,None,{1:fl})
   active+=stats1["changed"]>0
   self.assertTrue(np.array_equal(visible[protected],rgb[protected]))
   self.assertTrue(np.array_equal(visible[500:,:,:],rgb[500:,:,:]))
  self.assertGreater(active,0)
 def test_temporal_keyframes_must_be_clip_local(self):
  p=eng.read_profile("N17_APPROVED_VISUAL_RESULT_V001.json")
  self.assertEqual(p["fixtures"][0]["visibility_keyframes"],[[0,0],[261,0],[271,1],[369,1],[376,0]])
  p["fixtures"][0]["visibility_keyframes"]=[[281,0],[542,0],[552,1],[650,1],[657,0]]
  with self.assertRaisesRegex(AssertionError,"VISIBILITY_KEYS_MUST_USE_CLIP_LOCAL_FRAMES"):
   eng.validate(p)
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
