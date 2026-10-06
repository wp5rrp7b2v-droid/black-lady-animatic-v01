
const STAGES=["DESIGN","PREFLIGHT","GENERATE","REVIEW","PUBLISH","REGISTER","LOCK","CLOSEOUT"];
const STATUS_STAGE={DESIGN_PENDING:0,DESIGN_APPROVED:1,PREFLIGHT_FAILED:1,PREFLIGHT_PASS:2,AWAITING_CANDIDATE:2,CANDIDATE_VERIFIED_PENDING_PO:3,REJECTED:3,PO_APPROVED_PENDING_PUBLICATION:4,PUBLISHED_NOT_REGISTERED:5,REGISTERED_PENDING_LOCK:6,LOCKED_PENDING_CLOSEOUT:7,CLOSED:7};
let current=null;
const el=id=>document.getElementById(id);
const h=v=>String(v==null?"":v).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
async function api(url,opt={}){const r=await fetch(url,opt);let j={};try{j=await r.json()}catch{}if(!r.ok||j.ok===false)throw new Error(j.error||("HTTP "+r.status));return j}
const post=(url,body)=>api(url,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
const sid=()=>el("sessionId").value.trim()||localStorage.getItem("blpc_session_id")||"";
function bundle(){return {bundle_id:el("bundleId").value.trim(),run_id:Number(el("runId").value)||null,artifact_id:Number(el("artifactId").value)||null,artifact_digest:el("artifactDigest").value.trim(),reference_count:Number(el("referenceCount").value)||0,references_exact:true,generation_allowed:true}}
function row(k,v,cls=""){return '<div class="row"><span>'+h(k)+'</span><span class="'+cls+'">'+h(v)+'</span></div>'}
function setSession(s){current=s;if(s&&s.session_id){localStorage.setItem("blpc_session_id",s.session_id);el("sessionId").value=s.session_id;el("shotId").value=s.shot_id||"";const b=s.bundle||{};el("bundleId").value=b.bundle_id||"";el("runId").value=b.run_id||"";el("artifactId").value=b.artifact_id||"";el("artifactDigest").value=b.artifact_digest||"";el("referenceCount").value=b.reference_count||""}render()}
function render(){
 const idx=current?(STATUS_STAGE[current.status]??0):-1;
 el("workflow").innerHTML=STAGES.map((x,i)=>'<div class="step '+(i===idx?"active ":"")+(i<idx?"done":"")+'">'+x+'</div>').join("");
 if(!current){el("activePanel").innerHTML='<span class="empty">Start or load a Session.</span>';el("identity").innerHTML='<span class="empty">Candidate 尚未建立。</span>';return}
 el("activeTitle").textContent="Active Stage｜"+current.current_stage;
 const c=current.candidate||{}, p=current.preflight||{};
 el("identity").innerHTML=c.candidate_id?row("Shot",c.shot_id)+row("Candidate",c.candidate_id)+row("Drive File ID",c.drive_file_id,"mono")+row("SHA-256",c.sha256,"mono")+row("Bytes",c.byte_size)+row("Dimensions",(c.width||"")+" × "+(c.height||""))+row("Exact Binary",c.exact_binary_pass?"PASS":"NOT VERIFIED",c.exact_binary_pass?"ok":"warn")+row("PO",(current.approval||{}).action||"PENDING"):'<span class="empty">Candidate 尚未建立。</span>';
 el("evidence").innerHTML=row("Status",current.status)+row("Mode",current.mode)+row("Preflight",p.pass===true?"PASS":p.pass===false?"FAIL":"PENDING",p.pass===true?"ok":p.pass===false?"bad":"warn")+row("Process Boundary","FORMAL WORKFLOW UNCHANGED","ok");
 el("history").innerHTML=(current.history||[]).slice().reverse().map(x=>row(x.action,x.at||"","mono")).join("");
 const a=el("activePanel");a.innerHTML=row("Session",current.session_id)+row("Shot",current.shot_id)+row("Status",current.status)+'<div class="actions" id="stageActions"></div>';
 const actions=el("stageActions"), add=(name,fn,cls="")=>{const b=document.createElement("button");b.textContent=name;b.className=cls;b.onclick=fn;actions.appendChild(b)};
 switch(current.status){
  case "DESIGN_PENDING": add("Approve Design",approveDesign,"primary"); break;
  case "DESIGN_APPROVED": case "PREFLIGHT_FAILED": add("Run PREFLIGHT",runPreflight,"primary"); break;
  case "PREFLIGHT_PASS": case "AWAITING_CANDIDATE":
    a.insertAdjacentHTML("beforeend",'<div class="drop" id="drop"><strong>GENERATE in Work → upload exactly one Candidate</strong><br><span class="muted">Console 不替代 Work 制图。</span><div class="actions"><input id="candidateId" placeholder="CANDIDATE_01"><input id="candidateFile" type="file" accept="image/png"><button id="candidateUpload" class="primary">Upload + Exact Verify</button></div></div>');bindDrop(); break;
  case "CANDIDATE_VERIFIED_PENDING_PO": add("PO Approve",()=>review("approve"),"primary");add("PO Reject",()=>review("reject"),"danger");break;
  case "REJECTED": add("Open New Candidate",newCandidate,"primary");break;
  case "PO_APPROVED_PENDING_PUBLICATION": add("Publish Qualification Metadata",publish,"primary");break;
  case "PUBLISHED_NOT_REGISTERED": add("Register / Retry Registration Only",register,"primary");break;
  case "REGISTERED_PENDING_LOCK": add("LOCK Identity",lock,"primary");break;
  case "LOCKED_PENDING_CLOSEOUT": add("Closeout Qualification",closeout,"primary");break;
  case "CLOSED": actions.innerHTML='<a class="btn" href="/api/v1/receipt?session_id='+encodeURIComponent(current.session_id)+'">Download Receipt</a>';break;
 }
}
async function refreshSystem(){try{const j=await api("/api/v1/status");el("system").innerHTML=row("Release",j.release)+row("Drive",j.drive_connected?"CONNECTED":"NOT CONNECTED",j.drive_connected?"ok":"warn")+row("Drive Folder",j.drive_folder_bound?(j.drive_folder_name||"BOUND"):"NOT BOUND")+row("GitHub CLI",j.github_cli?"READY":"NOT READY",j.github_cli?"ok":"warn")+row("Boundary",j.production_process_boundary,"mono")}catch(e){el("system").textContent=e.message}}
async function start(){try{const j=await post("/api/v1/session/start",{session_id:el("sessionId").value.trim(),shot_id:el("shotId").value.trim(),mode:"QUALIFICATION",bundle:bundle(),design_summary:el("designSummary").value.trim()});setSession(j.session)}catch(e){alert(e.message)}}
async function load(){try{if(!sid())throw new Error("请输入 Session ID");const j=await api("/api/v1/session?session_id="+encodeURIComponent(sid()));setSession(j.session)}catch(e){alert(e.message)}}
async function approveDesign(){try{const j=await post("/api/v1/design/approve",{session_id:sid(),bundle:bundle(),design_summary:el("designSummary").value.trim()});setSession(j.session)}catch(e){alert(e.message)}}
async function runPreflight(){try{const j=await post("/api/v1/preflight",{session_id:sid()});setSession(j.session)}catch(e){alert(e.message)}}
function bindDrop(){const d=el("drop"),f=el("candidateFile"),b=el("candidateUpload");if(!d)return;b.onclick=()=>upload(f.files[0]);["dragenter","dragover"].forEach(x=>d.addEventListener(x,e=>{e.preventDefault();d.classList.add("drag")}));["dragleave","drop"].forEach(x=>d.addEventListener(x,e=>{e.preventDefault();d.classList.remove("drag")}));d.addEventListener("drop",e=>upload(e.dataTransfer.files[0]))}
async function upload(file){try{if(!file)throw new Error("请选择 PNG");const fd=new FormData();fd.append("session_id",sid());fd.append("candidate_id",(el("candidateId").value||"CANDIDATE_01").trim());fd.append("file",file);const j=await api("/api/v1/candidate/upload",{method:"POST",body:fd});setSession(j.session)}catch(e){alert(e.message)}}
async function review(action){try{const reason=action==="reject"?(prompt("Reject reason（可选）","")||""):"";const j=await post("/api/v1/candidate/review",{session_id:sid(),action,reason});setSession(j.session)}catch(e){alert(e.message)}}
async function newCandidate(){try{const j=await post("/api/v1/candidate/new",{session_id:sid()});setSession(j.session)}catch(e){alert(e.message)}}
async function publish(){try{const j=await post("/api/v1/publish",{session_id:sid()});setSession(j.session)}catch(e){alert(e.message)}}
async function register(){try{const j=await post("/api/v1/register",{session_id:sid()});setSession(j.session)}catch(e){alert(e.message)}}
async function lock(){try{const j=await post("/api/v1/lock",{session_id:sid()});setSession(j.session)}catch(e){alert(e.message)}}
async function closeout(){try{const j=await post("/api/v1/closeout",{session_id:sid()});setSession(j.session)}catch(e){alert(e.message)}}
el("startBtn").onclick=start;el("loadBtn").onclick=load;
const saved=localStorage.getItem("blpc_session_id");if(saved)el("sessionId").value=saved;
refreshSystem();render();if(saved)load();
