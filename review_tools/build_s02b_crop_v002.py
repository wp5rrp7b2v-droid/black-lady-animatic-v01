#!/usr/bin/env python3
"""N16/N17 six-node review preview. Noncanonical; originals are read-only."""
import hashlib,json,os,pathlib,subprocess
R=pathlib.Path(__file__).resolve().parents[1]
OUT=pathlib.Path(os.environ.get('RUNNER_TEMP','/tmp'))/'S02B_N16_N17_V002_CROP_TEST'
OUT.mkdir(parents=True,exist_ok=True)
IDX={x['shot_id']:x for x in map(json.loads,(R/'production/story_shots/story_shot_index.jsonl').read_text().splitlines())}
A=R/'staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a'
ASHA='8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0'
N=[
('N16','ESTABLISH','scale=720:1280:flags=lanczos',69),
('N16','JUN_QUESTION','crop=616:1095:325:120,scale=720:1280:flags=lanczos',95),
('N16','NING_REPLY','crop=625:1111:0:110,scale=720:1280:flags=lanczos',117),
('N17','RULE_TWO_SHOT','scale=720:1280:flags=lanczos',91),
('N17','NING_RULE_CLOSE','crop=620:1102:0:110,scale=720:1280:flags=lanczos',175),
('N16','JUN_ACK_CLOSE','crop=511:908:430:110,scale=720:1280:flags=lanczos',111)]
def sh(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def blob(p):
 z=p.read_bytes()
 return hashlib.sha1(('blob '+str(len(z))+'\0').encode()+z).hexdigest()
def run(args):
 print('RUN',' '.join(map(str,args))[:250],flush=True)
 subprocess.run(list(map(str,args)),check=True,stdout=subprocess.DEVNULL)
def probe(p):
 return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,nb_frames,width,height','-of','json',str(p)],text=True))
assert A.stat().st_size==4957338 and sh(A)==ASHA,'source audio identity'
source={}
for sid in ('N16','N17'):
 d=IDX[sid];p=R/d['canonical_path']
 assert d['approval_status']=='APPROVED' and d['lifecycle']=='CURRENT'
 assert p.stat().st_size==d['byte_size'] and sh(p)==d['sha256_locked_identity'] and blob(p)==d['github_blob_sha'],sid
 dims=probe(p)['streams'][0]; assert (dims['width'],dims['height'])==(941,1672),sid
 source[sid]={'path':d['canonical_path'],'sha256':sh(p),'blob':blob(p),'size':p.stat().st_size}
files=[];nodes=[];pos=0
for i,(sid,label,vf,frames) in enumerate(N,1):
 path=OUT/f'{i:02d}_{sid}_{label}.mp4'
 run(['ffmpeg','-hide_banner','-loglevel','error','-y','-loop','1','-framerate','30','-i',R/IDX[sid]['canonical_path'],'-vf',vf+',setsar=1,format=yuv420p','-frames:v',str(frames),'-an','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p',path])
 files.append(path)
 run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',path,'-frames:v','1',OUT/f'{i:02d}_{sid}_{label}.png'])
 nodes.append({'node':i,'shot':sid,'role':label,'start_frame':pos,'end_frame_exclusive':pos+frames,'frames':frames,'transform':vf})
 pos+=frames
assert pos==658
(OUT/'concat.txt').write_text(''.join("file '"+str(x.resolve())+"'\n" for x in files))
joined=OUT/'joined.mp4'
run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',OUT/'concat.txt','-c','copy',joined])
mp4=OUT/'S02B_N16_N17_V002_CROP_TEST.mp4'
run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',joined,'-i',A,'-filter_complex','[1:a:0]atrim=start=78.750:duration=21.950,asetpts=PTS-STARTPTS[a]','-map','0:v:0','-map','[a]','-t','21.950','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',mp4])
run(['ffmpeg','-hide_banner','-loglevel','error','-xerror','-i',mp4,'-f','null','-'])
p=probe(mp4)
assert p['streams'][0]['nb_frames']=='658' and abs(float(p['format']['duration'])-21.95)<0.06
report={'status':'RENDER QC PASS / REVIEW ONLY / NOT CANONICAL','source_originals':source,'audio_sha256':ASHA,'audio_window_original_sec':[78.75,100.70],'nodes':nodes,'video_sha256':sh(mp4),'video_bytes':mp4.stat().st_size,'ffprobe':p,'note':'V001 remains approved; no new registered Story Shot'}
(OUT/'RENDER_MANIFEST.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'result':'PASS','sha256':sh(mp4),'size':mp4.stat().st_size,'duration':p['format']['duration']},ensure_ascii=False))
