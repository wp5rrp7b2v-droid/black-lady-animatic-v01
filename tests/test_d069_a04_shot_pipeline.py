import copy, hashlib, importlib.util, json, shutil, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
import resolver_asset_source_v0_1 as source
import shot_reference_resolver_v0_1 as resolver
import shot_reference_package_exporter_v0_1 as exporter
import shot_use_audit_v0_1 as audit

class Fixture(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(); self.addCleanup(self.t.cleanup); self.root=Path(self.t.name)
  for rel in [source.MANIFEST,source.REGISTRY,source.SCENE_PROFILES,Path('production/asset_registry/entity_registry.jsonl'),Path('production/asset_registry/asset_relations.jsonl'),Path('production/asset_registry/audit_event_log.jsonl'),resolver.SPEC]:
   p=self.root/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,p)
  for row in source.read_runtime_registry(ROOT):
   try: p=source.source_path(source.normalize(row,'RUNTIME_REGISTRY'),ROOT)
   except ValueError: continue
   if p.is_file(): d=self.root/row['storage_uri'];d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,d)
 def rows(self): return [json.loads(x) for x in (self.root/source.REGISTRY).read_text().splitlines() if x.strip()]
 def write_rows(self,rows): (self.root/source.REGISTRY).write_text(''.join(json.dumps(x)+'\n' for x in rows))
 def add_asset(self,entity,kind,role,shot=False):
  data=(entity+kind).encode(); folder={'COSTUME':'costume_references/neil','PROP':'prop_references/neil','SHOT':'shots/a04'}[kind]; name=f'{entity}_{role}_DEFAULT_DEFAULT_V001.png'; path=self.root/'production/image_library'/folder/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
  row={"approval_status":"APPROVED","asset_class":"SHOT" if shot else "ATOMIC","asset_id":f"AST_TEST_{kind}","authority_class":"CONTINUITY" if shot else "MASTER","byte_size":len(data),"entity_id":None if shot else entity,"filename":name,"lifecycle":"ARCHIVED" if shot else "CURRENT","resolver_usage":"CONDITIONAL" if shot else "DEFAULT","role":role,"sha256":hashlib.sha256(data).hexdigest(),"shot_id":"A04" if shot else None,"state":"DEFAULT","storage_uri":path.relative_to(self.root).as_posix(),"variant":"DEFAULT","version_no":1}
  rows=self.rows();rows.append(row);self.write_rows(rows);return row

class LiveTests(unittest.TestCase):
 def test_spec_and_truthful_baseline(self):
  spec=resolver.load_spec();self.assertEqual(spec['shot_spec_id'],'A04_SPEC_V001'); self.assertNotIn('PROP_NEIL_KEYS', [x.get('entity_id') for x in spec['props']])
  r=resolver.resolve();self.assertEqual(r['status'],'BLOCKED');self.assertFalse(r['generation_allowed']);self.assertEqual([x['asset']['asset_id'] for x in r['resolved']],['AST_IMG_000060','AST_IMG_000059','AST_IMG_000052']);self.assertEqual({x['entity_id'] for x in r['reference_gaps']},{'COSTUME_NEIL_DEFAULT','PROP_NEIL_CROSS'});self.assertEqual(r['shot_evidence']['status'],'SHOT_EVIDENCE_GAP')
 def test_entities_exist_without_assets(self):
  self.assertEqual(resolver.resolve_atomic('COSTUME_NEIL_DEFAULT','COSTUME','COSTUME_MASTER','DEFAULT','DEFAULT')['reason'],'NO_ELIGIBLE_FORMAL_ASSET');self.assertEqual(resolver.resolve_atomic('PROP_ARBITRARY','PROP','PROP_MASTER','DEFAULT','DEFAULT')['reason'],'UNKNOWN_ENTITY')
 def test_no_live_historical_use_relations(self): self.assertEqual(audit.query_relations('AST_IMG_000060','reverse'),[])

class ResolverFixtureTests(Fixture):
 def test_scene_mismatches(self):
  spec=resolver.load_spec(root=self.root)
  for k,v in [('time_of_day','NIGHT'),('main_door','CLOSED')]:
   s=copy.deepcopy(spec);s['scene']['required_state'][k]=v;p=self.root/f'{k}.json';p.write_text(json.dumps(s));self.assertEqual(next(x for x in resolver.resolve(p,self.root)['reference_gaps'] if x['kind']=='SCENE')['status'],'REFERENCE_GAP')
 def test_character_stale_corrupt_missing_duplicate(self):
  for mode in ('stale','corrupt','missing','duplicate'):
   with self.subTest(mode=mode):
    rows=self.rows(); target=next(x for x in rows if x['asset_id']=='AST_IMG_000060')
    if mode=='stale':
     rel=self.root/'production/asset_registry/asset_relations.jsonl'; rel.write_text('\n'.join(x for x in rel.read_text().splitlines() if 'AST_IMG_000060' not in x)+'\n')
    elif mode=='corrupt': (self.root/target['storage_uri']).write_bytes(b'bad')
    elif mode=='missing': (self.root/target['storage_uri']).unlink()
    else: target=copy.deepcopy(target);target['asset_id']='AST_DUP';rows.append(target);self.write_rows(rows)
    r=resolver.resolve(root=self.root);self.assertFalse(r['generation_allowed']);self.assertTrue(any(x.get('entity_id')=='CHAR_NING_QIUSHUI' for x in r['reference_gaps']))
    self.setUp()
 def test_complete_fixture_ready_and_package_hashes(self):
  self.add_asset('COSTUME_NEIL_DEFAULT','COSTUME','COSTUME_MASTER');self.add_asset('PROP_NEIL_CROSS','PROP','PROP_MASTER');self.add_asset('A04','SHOT','SHOT_MASTER',True)
  r=resolver.resolve(root=self.root);self.assertEqual(r['status'],'READY_FOR_GENERATION');self.assertTrue(r['generation_allowed'])
  out=self.root/'packages'/'A04_REFERENCE_PACKAGE_V001';out.parent.mkdir();m=exporter.export(out,root=self.root,generated_at='2026-09-18T12:00:00Z');self.assertTrue(m['generation_allowed'])
  for x in m['resolved_assets']:
   matches=list(out.rglob(x['delivered_filename']));self.assertEqual(len(matches),1);self.assertEqual(source.sha256(matches[0]),x['sha256'])
 def test_character_cannot_satisfy_costume_or_prop(self):
  rows=self.rows(); neil=next(x for x in rows if x['asset_id']=='AST_IMG_000059')
  for entity,kind,role in [('COSTUME_NEIL_DEFAULT','COSTUME','COSTUME_MASTER'),('PROP_NEIL_CROSS','PROP','PROP_MASTER')]:
   fake=copy.deepcopy(neil);fake['entity_id']=entity;fake['role']=role;rows.append(fake)
  self.write_rows(rows);r=resolver.resolve(root=self.root);self.assertEqual({x['entity_id'] for x in r['reference_gaps']},{'COSTUME_NEIL_DEFAULT','PROP_NEIL_CROSS'})
 def test_blocked_diagnostic_package(self):
  out=self.root/'packages'/'A04_REFERENCE_PACKAGE_V001';out.parent.mkdir();m=exporter.export(out,root=self.root);self.assertFalse(m['generation_allowed']);self.assertEqual(m['status'],'BLOCKED');self.assertEqual(len(list((out/'visual_refs').glob('*.png'))),3)

class AuditTests(Fixture):
 def record(self): return {"use_record_id":"AO06_A04_USE_V001","shot_spec_id":"A04_SPEC_V001","shot_id":"A04","package_id":"A04_REFERENCE_PACKAGE_V001","source_commit":"abc","resolver_version":"v","input_asset_ids":["AST_IMG_000060"],"input_versions":[1],"input_sha256":["a"*64],"input_order":[1],"delivery_artifact_digest":None,"generation_environment":"NON_PRODUCTION_TEST","request_or_proof_identifier":"proof-1","manual_product_owner_reference_upload_count":0,"service_input_sha_receipt":"NOT_AVAILABLE","result":"PASS","created_at":"2026-09-18T12:00:00Z","scene_state":{"time_of_day":"DAY","main_door":"OPEN"},"blockers":[]}
 def test_use_record_append_only_and_reverse_queries(self):
  audit.write_use_record(self.record(),self.root)
  with self.assertRaises(FileExistsError): audit.write_use_record(self.record(),self.root)
  self.assertEqual(audit.query_shot('A04',self.root)[0]['input_asset_ids'],['AST_IMG_000060']);self.assertEqual(audit.query_asset('AST_IMG_000060',self.root)[0]['shot_id'],'A04')
 def test_uses_reference_direction_duplicate_reverse_and_rollback(self):
  rows=self.rows();rows.append({"asset_id":"AST_SHOT","asset_class":"SHOT"});self.write_rows(rows)
  rel=audit.add_uses_reference('AST_SHOT','AST_IMG_000060',self.root);self.assertEqual(rel['source_asset_id'],'AST_SHOT');self.assertEqual(audit.query_relations('AST_SHOT','forward',self.root)[0]['target_asset_id'],'AST_IMG_000060');self.assertEqual(audit.query_relations('AST_IMG_000060','reverse',self.root)[0]['source_asset_id'],'AST_SHOT')
  with self.assertRaises(ValueError): audit.add_uses_reference('AST_SHOT','AST_IMG_000060',self.root)
  before=((self.root/audit.RELATIONS).read_bytes(),(self.root/audit.AUDIT).read_bytes())
  with self.assertRaises(RuntimeError): audit.add_uses_reference('AST_SHOT','AST_IMG_000059',self.root,True)
  self.assertEqual(before,((self.root/audit.RELATIONS).read_bytes(),(self.root/audit.AUDIT).read_bytes()))
 def test_invalid_relation_sources(self):
  with self.assertRaises(ValueError): audit.add_uses_reference('AST_IMG_000060','AST_IMG_000059',self.root)
  with self.assertRaises(ValueError): audit.add_uses_reference('AST_IMG_000060','AST_IMG_000060',self.root)
if __name__=='__main__':unittest.main()
