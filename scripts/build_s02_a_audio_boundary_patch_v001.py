import json, pathlib, subprocess, wave, hashlib, math, audioop

ROOT=pathlib.Path.cwd()
SRC=ROOT/"staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a"
OUT=ROOT/"S02_A_AUDIO_BOUNDARY_PATCH_V001"
OUT.mkdir(exist_ok=True)

# Extract an intentionally wider PCM window around the S02-A narration.
wav=OUT/"s02_a_boundary_review_0028_0127.wav"
subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-ss","28.000","-to","87.000","-i",str(SRC),"-ac","1","-ar","16000","-c:a","pcm_s16le",str(wav),"-y"],check=True)

# Use silencedetect only as objective pause evidence; semantic boundaries remain tied to canonical transcript.
p=subprocess.run(["ffmpeg","-hide_banner","-i",str(wav),"-af","silencedetect=noise=-38dB:d=0.18","-f","null","-"],capture_output=True,text=True)
(OUT/"silencedetect.txt").write_text(p.stderr,encoding="utf-8")

report={
 "patch_id":"S02_A_AUDIO_BOUNDARY_PATCH_V001",
 "status":"BOUNDARY_REVIEW_EVIDENCE",
 "canonical_audio":"AUDIO_MVP1_CANONICAL_V001",
 "review_window":{"in":"00:28.000","out":"01:27.000"},
 "previous_assembly":{"in":"00:32.900","out":"01:18.750"},
 "canonical_transcript_evidence":{
  "preceding_verified":{"in":"00:30.030","out":"00:33.020","text":"静静等待着众人进入"},
  "target_first_reviewed":{"approx_in":"00:33.000","approx_out":"00:45.000","text":"他是一个皮肤苍白到不带一丝血色的男人，大约五十来岁，脖子上挂着一个十字架，脸上的笑容有些说不出的僵硬","note":"approx TC; not extraction boundary"},
  "target_last_verified":{"in":"01:10.900","out":"01:18.750","text":"但宁秋水失望地发现，管家尼尔的腰间空空如也"},
  "following_verified":{"in":"01:18.750","out":"01:24.200","speaker":"君鹭远","text":"秋水哥，姐姐以前也是在这样的地方工作吗？"}
 },
 "boundary_conclusion":{
  "semantic_start":"00:33.020",
  "semantic_end":"01:18.750",
  "reason_start":"00:32.900 intrudes into the tail of the preceding verified sentence; the clean transcript boundary is after S3-MVP1-0005 at 00:33.020.",
  "reason_end":"01:18.750 is already the verified end of the A05 narration and exact start of Jun Luyuan's next dialogue; keep unchanged.",
  "patched_duration_s":45.730
 },
 "timeline_patch":{
  "N11":{"in":"00:33.020","out":"00:39.100","duration_s":6.080},
  "N12":{"in":"00:39.100","out":"00:46.360","duration_s":7.260},
  "A04":{"in":"00:46.360","out":"00:56.260","duration_s":9.900},
  "N14":{"in":"00:56.260","out":"01:03.520","duration_s":7.260},
  "N15":{"in":"01:03.520","out":"01:10.940","duration_s":7.420},
  "A05":{"in":"01:10.940","out":"01:18.750","duration_s":7.810}
 },
 "qc_rule":"Do not claim narrative completeness from sample identity alone. Final proof must be listened to from at least 2 s before first intended sentence through at least 2 s after last intended sentence before trimming, then PO auditory QC remains authoritative."
}
(OUT/"audio_boundary_patch_v001.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("PATCH_START=00:33.020")
print("PATCH_END=01:18.750")
print("PATCH_DURATION=45.730")
print("END_BOUNDARY_UNCHANGED=YES")
print("START_BOUNDARY_CHANGED=YES")
