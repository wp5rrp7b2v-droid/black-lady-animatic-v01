import hashlib, json, shutil, struct, subprocess
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent
TIMELINE = json.loads((PROJECT / 'src/timeline.json').read_text())
AUDIO_PATH = 'staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a'
AUDIO_SHA = '8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0'
OUTPUT_NAME = 'P03_OPENING_V2_PROOF_REVIEW_V002'
OUT = PROJECT / 'out' / OUTPUT_NAME

def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args], text=True).strip()

def identity(relative):
    path = REPO / relative
    require(path.is_file() and not path.is_symlink(), f'not regular file: {relative}')
    data = path.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    require(blob == git('rev-parse', f'HEAD:{relative}'), f'Git blob mismatch: {relative}')
    return data, hashlib.sha256(data).hexdigest(), blob

def probe(path):
    return json.loads(subprocess.check_output([
      'ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)
    ], text=True))

sequence = ['A01','A02','N06','N02','N07','N03','N04','N08','N09','N10','N05','N01']
frame_map = [(0,98),(98,99),(197,71),(268,68),(336,60),(396,63),(459,132),(591,58),(649,84),(733,82),(815,86),(901,90)]

require([s['shot_id'] for s in TIMELINE['shots']] == sequence, 'sequence mismatch')
require([(s['start_frame'],s['duration_frames']) for s in TIMELINE['shots']] == frame_map, 'frame map mismatch')
require(TIMELINE['duration_frames'] == 991 and TIMELINE['fps'] == 30, 'composition timing mismatch')
require(git('merge-base', TIMELINE['source_baseline'], 'HEAD') == TIMELINE['source_baseline'], 'HEAD not descended from source baseline')

state = json.loads((REPO/'docs/project_control/core/project_state.json').read_text())
require(state['state_revision'] == 'R092', f"expected R092, got {state.get('state_revision')}")
require(state['current_task'] == 'P0.3｜OPENING V2 CONTEXTUAL PROOF REVIEW', 'unexpected current task')

records = [json.loads(x) for x in (REPO/'production/story_shots/story_shot_index.jsonl').read_text().splitlines() if x.strip()]
registry = {r['shot_id']:r for r in records}
require(len(registry) >= 17, 'Story Shot registry unexpectedly incomplete')

runtime = PROJECT/'public/inputs'
runtime.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

manifest_shots=[]
for shot in TIMELINE['shots']:
    sid=shot['shot_id']
    rec=registry[sid]
    require(rec['approval_status']=='APPROVED' and rec['lifecycle']=='CURRENT', f'{sid} not approved/current')
    require(rec['canonical_path']==shot['canonical_path'], f'{sid} canonical path mismatch')
    data,sha,blob=identity(shot['canonical_path'])
    require(data[:8]==b'\x89PNG\r\n\x1a\n' and data[12:16]==b'IHDR', f'{sid} invalid PNG')
    width,height=struct.unpack('>II',data[16:24])
    require((width,height)==(941,1672), f'{sid} dimensions {width}x{height}')
    require(len(data)==rec['byte_size'], f'{sid} byte size mismatch')
    require(blob==rec['github_blob_sha'], f'{sid} Git blob mismatch vs index')
    if rec.get('sha256_locked_identity'):
        require(sha==rec['sha256_locked_identity'], f'{sid} SHA256 mismatch')
    dst=runtime/f'{sid}.png'
    shutil.copyfile(REPO/shot['canonical_path'],dst)
    require(hashlib.sha256(dst.read_bytes()).hexdigest()==sha, f'{sid} runtime copy mismatch')
    manifest_shots.append({
      **shot,'sha256':sha,'byte_size':len(data),'github_blob_sha':blob,
      'dimensions':{'width':width,'height':height},
      'start_time_sec':shot['start_frame']/30,
      'end_time_sec':(shot['start_frame']+shot['duration_frames'])/30
    })

adata,asha,ablob=identity(AUDIO_PATH)
require(asha==AUDIO_SHA,'canonical audio SHA mismatch')
meta=probe(REPO/AUDIO_PATH)
audio=[s for s in meta['streams'] if s['codec_type']=='audio']
require(len(audio)==1,'audio stream mismatch')
require(abs(float(meta['format']['duration'])-359.141995)<0.01,'audio duration mismatch')
shutil.copyfile(REPO/AUDIO_PATH,runtime/'opening_audio.m4a')
require(hashlib.sha256((runtime/'opening_audio.m4a').read_bytes()).hexdigest()==asha,'audio runtime copy mismatch')

manifest={
  'source_commit':git('rev-parse','HEAD'),
  'source_baseline':TIMELINE['source_baseline'],
  'status':'TRANSITION_MOTION_ENRICHED / CONTEXTUAL REVIEW ONLY / TIMING NOT LOCKED',
  'sequence':sequence,
  'fps':30,'duration_frames':991,'duration_sec':991/30,
  'shots':manifest_shots,
  'audio':{'canonical_path':AUDIO_PATH,'sha256':asha,'byte_size':len(adata),'github_blob_sha':ablob,'source_start_sec':0,'source_end_sec':991/30},
  'audio_alignment_evidence':TIMELINE['audio_alignment_evidence'],
  'editorial_rule':TIMELINE['editorial_rule'],
  'overall_input_validation':'PASS'
}
(OUT/'opening_v2_v002_input_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(OUT/'timeline.json').write_text(json.dumps(TIMELINE,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
