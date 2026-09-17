#!/usr/bin/env python3
"""AO-04 Stage B formalizer, gated by explicit Product Owner approval."""
import argparse, datetime, json, os, shutil, tempfile
from pathlib import Path
from character_reference_sheet_builder_v0_1 import CANDIDATE_ROOT, digest, read_jsonl

ROOT=Path(__file__).resolve().parents[1]
REG=Path('production/asset_registry/asset_registry.jsonl')
REL=Path('production/asset_registry/asset_relations.jsonl')
AUD=Path('production/asset_registry/audit_event_log.jsonl')
FORMAL_ROOT=Path('production/image_library/derived_reference_sheets')

def require_approval(po_approved):
    if not po_approved: raise PermissionError('FAIL_CLOSED: explicit --po-approved is required')

def next_asset_ids(rows,count):
    high=max((int(r['asset_id'].rsplit('_',1)[1]) for r in rows),default=0)
    return [f'AST_IMG_{i:06d}' for i in range(high+1,high+count+1)]

def validate_candidates(root):
    manifests=sorted((root/CANDIDATE_ROOT).glob('*/*.manifest.json'))
    if len(manifests)!=9: raise ValueError('Exactly nine candidate manifests are required')
    result=[]
    for p in manifests:
        m=json.loads(p.read_text(encoding='utf-8')); png=p.with_name(m['sheet_filename'])
        if m.get('candidate_status')!='WAITING_PRODUCT_OWNER_VISUAL_APPROVAL' or digest(png)!=m['sheet_sha256'] or png.stat().st_size!=m['byte_size']: raise ValueError(f'Invalid candidate: {p}')
        if not m.get('sources'): raise ValueError(f'Candidate has no dependencies: {p}')
        result.append((p,m,png))
    return result

def _lines(rows): return ''.join(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n' for r in rows)

def formalize(root=ROOT,po_approved=False):
    require_approval(po_approved); root=Path(root); candidates=validate_candidates(root)
    assets=read_jsonl(root/REG); relations=read_jsonl(root/REL); audits=read_jsonl(root/AUD)
    existing={(r.get('entity_id'),r.get('role')):r for r in assets if r.get('asset_class')=='DERIVED_REFERENCE' and r.get('lifecycle')=='CURRENT'}
    if existing:
        if len(existing)==9 and all(existing.get((m['entity_id'],'CHARACTER_REFERENCE_SHEET'),{}).get('sha256')==m['sheet_sha256'] for _,m,_ in candidates): return {'status':'ALREADY_FORMALIZED','asset_ids':[r['asset_id'] for r in existing.values()]}
        raise ValueError('Single Current conflict: a formal CURRENT Sheet already exists')
    ids=next_asset_ids(assets,len(candidates)); now=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
    copies=[]
    for aid,(_,m,png) in zip(ids,candidates):
        folder=m['entity_id'].removeprefix('CHAR_').lower(); relpath=FORMAL_ROOT/folder/m['sheet_filename']
        assets.append({'approval_status':'APPROVED','approved_at':now,'asset_class':'DERIVED_REFERENCE','asset_id':aid,'authority_class':'DERIVED','byte_size':m['byte_size'],'controller_version':'0.1','entity_id':m['entity_id'],'filename':m['sheet_filename'],'ingested_at':now,'lifecycle':'CURRENT','media_code':'IMG','mime_type':'image/png','provenance_status':'COMPLETE','resolver_usage':'DEFAULT','role':'CHARACTER_REFERENCE_SHEET','sha256':m['sheet_sha256'],'shot_id':None,'state':'DEFAULT','storage_uri':relpath.as_posix(),'task_id':'D-068/AO-04','variant':'DEFAULT','version_no':1})
        copies.append((png,root/relpath))
        event_id=f"EVT_{now.replace('-','').replace(':','')}_AO04_{aid.rsplit('_',1)[1]}"
        audits.append({'actor_id':'CHARACTER_REFERENCE_SHEET_FORMALIZER_V0_1','actor_type':'SYSTEM','asset_id':aid,'entity_id':m['entity_id'],'event_id':event_id,'event_time':now,'event_type':'ASSET_FORMALIZED','new_value':{'lifecycle':'CURRENT','sha256':m['sheet_sha256'],'storage_uri':relpath.as_posix()},'previous_value':{'candidate_manifest':str(_)},'reason':'Product Owner explicitly approved the AO-04 Candidate Sheet for Stage B formalization.','source_reference':'AO-04 Product Owner visual approval','task_id':'D-068/AO-04'})
        for n,src in enumerate(m['sources'],1):
            rel={'created_at':now,'created_by_event_id':event_id,'relation_type':'DERIVED_FROM','source_asset_id':aid,'target_asset_id':src['asset_id']}
            if rel not in relations: relations.append(rel)
    tmp=Path(tempfile.mkdtemp(prefix='.ao04-formalize-',dir=root)); backups=[]; created=[]
    try:
        for src,dst in copies:
            dst.parent.mkdir(parents=True,exist_ok=True)
            if dst.exists(): raise ValueError(f'Canonical destination exists: {dst}')
            staged=tmp/dst.relative_to(root); staged.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(src,staged)
            if digest(staged)!=digest(src): raise ValueError('Staged copy SHA mismatch')
        for target,rows in ((root/REG,assets),(root/REL,relations),(root/AUD,audits)):
            staged=tmp/(target.name+'.new'); staged.write_text(_lines(rows),encoding='utf-8')
        for _,dst in copies:
            os.replace(tmp/dst.relative_to(root),dst); created.append(dst)
        for target in (root/REG,root/REL,root/AUD):
            backup=tmp/(target.name+'.bak'); shutil.copyfile(target,backup); backups.append((backup,target)); os.replace(tmp/(target.name+'.new'),target)
    except Exception:
        for b,t in reversed(backups):
            if b.exists(): os.replace(b,t)
        for p in created:
            p.unlink(missing_ok=True)
        raise
    finally: shutil.rmtree(tmp,ignore_errors=True)
    return {'status':'FORMALIZED','asset_ids':ids}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',type=Path,default=ROOT); p.add_argument('--po-approved',action='store_true'); a=p.parse_args()
    try: print(json.dumps(formalize(a.root,a.po_approved),indent=2))
    except (PermissionError,RuntimeError,ValueError) as e: p.error(str(e))
if __name__=='__main__': main()
