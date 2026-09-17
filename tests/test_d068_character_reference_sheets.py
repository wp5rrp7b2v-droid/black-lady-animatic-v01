import copy, hashlib, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
 s=importlib.util.spec_from_file_location(name,ROOT/path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
builder=load('ao04_builder','scripts/character_reference_sheet_builder_v0_1.py')
resolver=load('ao04_resolver','scripts/resolver_asset_source_v0_1.py')

class AO04Tests(unittest.TestCase):
 def test_character_entities(self):
  rows=builder.read_jsonl(ROOT/builder.ENTITIES); scenes=[r for r in rows if r['entity_type']=='SCENE']; chars=[r for r in rows if r['entity_type']=='CHARACTER']
  self.assertEqual(2,len(scenes)); self.assertEqual(9,len(chars)); self.assertEqual(11,len({r['entity_id'] for r in rows}))
  self.assertEqual({'A':4,'B':4,'C':1},{t:sum(r['character_tier']==t for r in chars) for t in 'ABC'})
  self.assertTrue(all(r['primary_side']=='LEFT' for r in chars if r['character_tier']=='B'))
 def test_layouts(self):
  self.assertEqual(9,len(builder.layout({'character_tier':'A'})[0]))
  b=builder.layout({'character_tier':'B','primary_side':'LEFT'})[0]; self.assertEqual(6,len(b)); self.assertIn(('PROFILE_PRIMARY','PROFILE_LEFT'),b)
  self.assertEqual(builder.TIER_C,[('FACE_IDENTITY','FACE_FRONT'),('BODY_FRONT','BODY_FRONT'),('REAR_OR_BACK','BODY_BACK')])
 def test_live_truth_exact(self):
  entities=[e for e in builder.read_jsonl(ROOT/builder.ENTITIES) if e['entity_type']=='CHARACTER']
  self.assertEqual(builder.EXPECTED,{e['entity_id']:len(builder.select_atomic_assets(ROOT,e)) for e in entities})
 def test_filters_nondefault_and_supplementary(self):
  e={'entity_id':'CHAR_NING_QIUSHUI','character_tier':'A','primary_side':None}; selected=builder.select_atomic_assets(ROOT,e)
  self.assertEqual('AST_IMG_000037',selected['REAR_3Q_RIGHT']['asset_id']); self.assertNotIn('STRUCTURE_FRONT_3Q_BODY_RIGHT',selected)
 def test_manifests_have_lineage_and_gaps_no_fake_dependency(self):
  for p in (ROOT/builder.CANDIDATE_ROOT).glob('*/*.manifest.json'):
   m=json.loads(p.read_text()); self.assertNotIn('asset_id',m)
   self.assertEqual(builder.STATUS,m['candidate_status'])
   self.assertEqual((builder.CANDIDATE_ROOT/m['entity_id'].lower()/m['sheet_filename']).as_posix(),m['expected_candidate_path'])
   self.assertTrue(all({'asset_id','version_no','role','sha256'} <= set(s) for s in m['sources']))
   self.assertEqual(len(builder.layout({'character_tier':m['character_tier'],'primary_side':m['primary_side']})[0]),len(m['sources'])+len(m['explicit_gap_slots']))
 def test_deterministic_png(self):
  entity=next(e for e in builder.read_jsonl(ROOT/builder.ENTITIES) if e.get('entity_id')=='CHAR_GUANG_YONG')
  with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
   ma,pa,_=builder.build_one(ROOT,entity,a); mb,pb,_=builder.build_one(ROOT,entity,b)
   self.assertEqual(pa.read_bytes(),pb.read_bytes()); self.assertEqual(ma['sheet_sha256'],mb['sheet_sha256'])
 def _fixture(self,lifecycle='CURRENT',bad_sha=False):
  td=tempfile.TemporaryDirectory(); root=Path(td.name); (root/'production/asset_registry').mkdir(parents=True); (root/'production/image_library/character_references/x').mkdir(parents=True)
  img=root/'production/image_library/character_references/x/a.png'; Image.new('RGB',(2,2)).save(img); sha=hashlib.sha256(img.read_bytes()).hexdigest()
  atomic={'asset_id':'AST_IMG_000001','asset_class':'ATOMIC','entity_id':'CHAR_X','role':'FACE_FRONT','variant':'DEFAULT','state':'DEFAULT','version_no':1,'approval_status':'APPROVED','lifecycle':lifecycle,'resolver_usage':'DEFAULT','filename':'a.png','storage_uri':'production/image_library/character_references/x/a.png','sha256':'0'*64 if bad_sha else sha}
  sheet={'asset_id':'AST_IMG_000002','asset_class':'DERIVED_REFERENCE','entity_id':'CHAR_X','role':'CHARACTER_REFERENCE_SHEET','approval_status':'APPROVED','lifecycle':'CURRENT'}
  (root/resolver.REGISTRY).write_text(json.dumps(atomic)+'\n'+json.dumps(sheet)+'\n'); (root/'production/asset_registry/asset_relations.jsonl').write_text(json.dumps({'source_asset_id':'AST_IMG_000002','relation_type':'DERIVED_FROM','target_asset_id':'AST_IMG_000001'})+'\n')
  return td,root,sheet
 def test_dependency_fresh(self):
  td,r,s=self._fixture(); self.addCleanup(td.cleanup); self.assertEqual('FRESH',resolver.dependency_status(s,r)['status'])
 def test_dependency_superseded(self):
  td,r,s=self._fixture('SUPERSEDED'); self.addCleanup(td.cleanup); self.assertEqual('DEPENDENCY_STALE',resolver.dependency_status(s,r)['status'])
 def test_dependency_deprecated(self):
  td,r,s=self._fixture('DEPRECATED'); self.addCleanup(td.cleanup); self.assertEqual('DEPENDENCY_STALE',resolver.dependency_status(s,r)['status'])
 def test_dependency_invalid_sha(self):
  td,r,s=self._fixture(bad_sha=True); self.addCleanup(td.cleanup); self.assertEqual('DEPENDENCY_STALE',resolver.dependency_status(s,r)['status'])
 def test_no_formal_candidate_or_relations(self):
  assets=builder.read_jsonl(ROOT/builder.REGISTRY); rels=builder.read_jsonl(ROOT/'production/asset_registry/asset_relations.jsonl')
  self.assertFalse(any(r.get('asset_class')=='DERIVED_REFERENCE' for r in assets)); self.assertFalse(any(r.get('relation_type')=='DERIVED_FROM' for r in rels))
 def test_formalizer_fails_closed(self):
  p=subprocess.run([sys.executable,str(ROOT/'scripts/character_reference_sheet_formalizer_v0_1.py')],capture_output=True,text=True)
  self.assertNotEqual(0,p.returncode); self.assertIn('FAIL_CLOSED',p.stderr)

if __name__=='__main__': unittest.main()
