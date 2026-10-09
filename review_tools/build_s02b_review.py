#!/usr/bin/env python3
"""Noncanonical S02-B director review export. No repo writes; no original PNG mutations."""
import hashlib, json, os, pathlib, subprocess
from decimal import Decimal
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = pathlib.Path(os.environ.get('RUNNER_TEMP', '/tmp')) / 'S02_B_REVIEW_V001'
OUT.mkdir(parents=True, exist_ok=True)
INDEX = {x['shot_id']:x for x in map(json.loads, (ROOT/'production/story_shots/story_shot_index.jsonl').read_text().splitlines())}
AUDIO=ROOT/'staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a'
AUDIO_HASH='8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0'
# Candidate editorial timings; S3 search timestamps are NOT exact micro-cut authority.
CUTS=[
 ('N16','0.00','9.37'),('N17','9.37','21.95'),('N18','21.95','27.97'),
 ('N19','27.97','31.65'),('N20','31.65','35.95'),
 ('N21','35.95','40.75'),('N22','40.75','45.55'),
 ('N23','45.55','52.23'),('N24','52.23','54.40'),('A06','54.40','56.49'),
 ('N25','56.49','60.34'),('N26','60.34','64.25')]
assert CUTS[0][1]=='0.00' and CUTS[-1][2]=='64.25'
assert all(Decimal(CUTS[i][2])==Decimal(CUTS[i+1][1]) for i in range(len(CUTS)-1))
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def gitblob(path):
 data=path.read_bytes();return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
def run(args):
 print('RUN',' '.join(map(str,args))[:450],flush=True)
 subprocess.run(list(map(str,args)),check=True,stdout=subprocess.DEVNULL)
assert AUDIO.exists(), 'missing canonical audio'
assert AUDIO.stat().st_size==4957338, 'audio byte length mismatch'
assert sha(AUDIO)==AUDIO_HASH, 'canonical audio SHA256 mismatch'
provenance=[];segments=[]
for i,(sid,begin,end) in enumerate(CUTS,1):
 info=INDEX[sid]
 assert info['approval_status']=='APPROVED' and info['lifecycle']=='CURRENT',sid
 image=ROOT/info['canonical_path'];assert image.is_file(),str(image)
 assert image.stat().st_size==info['byte_size'],f'{sid} bytes mismatch'
 assert gitblob(image)==info['github_blob_sha'],f'{sid} blob mismatch'
 if info.get('sha256_locked_identity'):
  assert sha(image)==info['sha256_locked_identity'],f'{sid} sha mismatch'
 length=float(Decimal(end)-Decimal(begin));frames=round(length*30)
 clip=OUT/f'{i:02d}_{sid}.mp4'
 zoom='1' if sid=='A06' else "min(zoom+0.00010,1.035)"
 vf=f"scale=720:1280:flags=lanczos,zoompan=z='{zoom}':d=1:s=720x1280:fps=30,setsar=1"
 run(['ffmpeg','-hide_banner','-loglevel','error','-y','-loop','1','-framerate','30','-i',image,
      '-vf',vf,'-frames:v',str(frames),'-an','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',clip])
 segments.append(clip)
 provenance.append({'shot':sid,'relative_start_sec':begin,'relative_end_sec':end,'frames':frames,
                    'canonical_path':info['canonical_path'],'git_blob':info['github_blob_sha'],'sha256':sha(image)})
(OUT/'concat.txt').write_text(''.join('file '+str(p.resolve())+'\n' for p in segments))
JOIN=OUT/'joined.mp4'
run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',OUT/'concat.txt','-c','copy',JOIN])
FINAL=OUT/'S02_B_DIRECTOR_REVIEW_V001.mp4'
run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',JOIN,'-ss','78.750','-i',AUDIO,
    '-map','0:v:0','-map','1:a:0','-t','64.250','-c:v','copy','-c:a','aac','-b:a','192k',
    '-ar','48000','-ac','2','-movflags','+faststart',FINAL])
run(['ffmpeg','-hide_banner','-loglevel','error','-xerror','-i',FINAL,'-f','null','-'])
p=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,r_frame_rate','-of','json',FINAL],text=True)
report={'review_status':'RENDERED / DIRECTOR REVIEW ONLY / NOT CANONICAL',
       'audio_source_sha256':AUDIO_HASH,'source_audio_start_sec':78.75,'source_audio_end_sec':143.0,
       'candidate_cut_policy':'EDITORIAL PROVISIONAL / NOT EXACT SPEECH ALIGNMENT',
       'output_sha256':sha(FINAL),'output_size_bytes':FINAL.stat().st_size,
       'ffprobe':json.loads(p),'clips':provenance}
(OUT/'REVIEW_MANIFEST.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'result':'PASS','file':str(FINAL),'sha256':sha(FINAL),
                  'size':FINAL.stat().st_size,'duration':json.loads(p)['format']['duration']},ensure_ascii=False))
