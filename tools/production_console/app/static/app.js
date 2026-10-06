const STAGES=["DESIGN","PREFLIGHT","GENERATE","REVIEW","PUBLISH","REGISTER","LOCK","CLOSEOUT"];
const STATUS_STAGE={
  DESIGN_PENDING:0,DESIGN_APPROVED:1,PREFLIGHT_FAILED:1,PREFLIGHT_PASS:2,AWAITING_CANDIDATE:2,
  CANDIDATE_VERIFIED_PENDING_PO:3,REJECTED:3,PO_APPROVED_PENDING_PUBLICATION:4,
  PUBLISHED_NOT_REGISTERED:5,REGISTERED_PENDING_LOCK:6,LOCKED_PENDING_CLOSEOUT:7,CLOSED:7
};
let current=null;
let remoteEvidence=null;

const el=id=>document.getElementById(id);
const h=v=>String(v==null?"":v).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
async function api(url,opt={}){
  const r=await fetch(url,opt); let j={};
  try{j=await r.json()}catch{}
  if(!r.ok||j.ok===false) throw new Error(j.error||("HTTP "+r.status));
  return j;
}
const post=(url,body)=>api(url,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
const sid=()=>el("sessionId").value.trim()||localStorage.getItem("blpc_session_id")||"";
const row=(k,v,cls="")=>'<div class="row"><span>'+h(k)+'</span><span class="'+cls+'">'+h(v)+'</span></div>';
const pill=(label,pass)=>'<span class="mini-pill '+(pass===true?"pass":pass===false?"fail":"")+'">'+h(label)+'</span>';

function localTime(value){
  if(!value) return "";
  const d=new Date(value);
  if(Number.isNaN(d.getTime())) return String(value);
  try{
    return new Intl.DateTimeFormat(undefined,{
      year:"numeric",month:"2-digit",day:"2-digit",
      hour:"2-digit",minute:"2-digit",second:"2-digit",
      hour12:false,timeZoneName:"short"
    }).format(d);
  }catch{return d.toLocaleString();}
}
function showAction(message,type=""){
  const box=el("actionStatus");
  if(!box)return;
  box.hidden=false;
  box.className="action-status"+(type?" "+type:"");
  box.textContent=message;
}

function bundle(){
  return {
    bundle_id:el("bundleId").value.trim(),
    run_id:Number(el("runId").value)||null,
    artifact_id:Number(el("artifactId").value)||null,
    artifact_digest:el("artifactDigest").value.trim(),
    reference_count:Number(el("referenceCount").value)||0,
    references_exact:el("referencesExact").checked,
    delivery_manifest_verified:el("manifestVerified").checked,
    generation_allowed:el("generationAllowed").checked
  };
}

function displayDesign(v){
  if(v==null) return "";
  if(typeof v==="string") return v;
  try{return JSON.stringify(v,null,2)}catch{return String(v)}
}

function setLockedInputs(){
  const has=!!current;
  const designEditable=!has||current.status==="DESIGN_PENDING";
  el("sessionId").disabled=has;
  el("shotId").disabled=has;
  ["bundleId","runId","artifactId","referenceCount","artifactDigest","referencesExact","manifestVerified","generationAllowed","designSummary"]
    .forEach(id=>el(id).disabled=!designEditable);
  el("startBtn").disabled=has;
  el("loadBtn").disabled=has;
  el("recoverBtn").disabled=has;
  el("reconcileBtn").disabled=!has;
  el("refreshEvidenceBtn").disabled=!has;
}

function setSession(s){
  current=s;
  remoteEvidence=null;
  if(s&&s.session_id){
    localStorage.setItem("blpc_session_id",s.session_id);
    el("sessionId").value=s.session_id;
    el("shotId").value=s.shot_id||"";
    const b=s.bundle||{};
    el("bundleId").value=b.bundle_id||"";
    el("runId").value=b.run_id||"";
    el("artifactId").value=b.artifact_id||"";
    el("artifactDigest").value=b.artifact_digest||"";
    el("referenceCount").value=b.reference_count||"";
    el("referencesExact").checked=b.references_exact!==false;
    el("manifestVerified").checked=b.delivery_manifest_verified!==false;
    el("generationAllowed").checked=b.generation_allowed!==false;
    el("designSummary").value=displayDesign(s.design_summary);
  }
  setLockedInputs();
  render();
  refreshSystem();
}

function resetWorkspace(){
  current=null; remoteEvidence=null;
  localStorage.removeItem("blpc_session_id");
  ["sessionId","shotId","bundleId","runId","artifactId","artifactDigest","referenceCount","designSummary"]
    .forEach(id=>el(id).value="");
  el("referencesExact").checked=true;
  el("manifestVerified").checked=true;
  el("generationAllowed").checked=true;
  setLockedInputs();
  render();
}

function renderWorkflow(){
  const idx=current?(STATUS_STAGE[current.status]??0):-1;
  el("workflow").innerHTML=STAGES.map((x,i)=>
    '<div class="step '+(i===idx?"active ":"")+(i<idx?"done":"")+'"><span>'+(i+1)+'</span>'+x+'</div>'
  ).join("");
  el("sessionState").textContent=current?current.status:"NO SESSION";
}

function renderIdentity(){
  const c=(current&&current.candidate)||{};
  const preview=el("candidatePreview");
  if(c.candidate_id){
    const src="/api/v1/candidate/media?session_id="+encodeURIComponent(current.session_id)+"&v="+encodeURIComponent(current.updated_at||"");
    preview.innerHTML='<img class="candidate-img" src="'+src+'" alt="Candidate preview">';
    el("identity").innerHTML=
      row("Shot",c.shot_id)+
      row("Candidate",c.candidate_id)+
      row("Drive File ID",c.drive_file_id,"mono")+
      row("SHA-256",c.sha256,"mono")+
      row("Bytes",c.byte_size)+
      row("Dimensions",(c.width||"")+" × "+(c.height||""))+
      row("Exact Binary",c.exact_binary_pass?"PASS":"NOT VERIFIED",c.exact_binary_pass?"ok":"warn")+
      row("PO",(current.approval||{}).action||"PENDING");
  }else{
    preview.innerHTML="";
    el("identity").innerHTML='<span class="empty">Candidate 尚未建立。</span>';
  }
}

function renderCheckGrid(checks){
  if(!checks||!Object.keys(checks).length) return "";
  return '<div class="check-grid">'+Object.entries(checks).map(([k,v])=>
    '<div class="check-row"><span>'+h(k)+'</span>'+pill(v===true?"PASS":v===false?"FAIL":String(v),v===true?true:v===false?false:null)+'</div>'
  ).join("")+'</div>';
}

function renderRemote(){
  const r=remoteEvidence;
  if(!r||!r.records) return '<div class="muted">Remote qualification evidence not loaded.</div>';
  const records=["publication","registration","lock","closeout"].map(k=>{
    const x=r.records[k]||{};
    return '<div class="remote-card"><strong>'+h(k.toUpperCase())+'</strong>'+
      '<div>'+pill(x.exists?"EXISTS":"NONE",x.exists?true:null)+'</div>'+
      (x.exists?'<div class="mono small">'+h(x.blob_sha||"")+'</div><div class="mono small">'+h(x.path||"")+'</div>':"")+
      '</div>';
  }).join("");
  return '<div class="remote-head">'+row("Qualification branch",r.branch||"","mono")+row("Highest remote status",r.highest_remote_status||"NONE")+'</div>'+
    '<div class="remote-grid">'+records+'</div>';
}

function renderEvidence(){
  if(!current){
    el("evidence").innerHTML='<span class="empty">No evidence yet.</span>';
    el("history").innerHTML="";
    return;
  }
  const p=current.preflight||{};
  let html=row("Status",current.status)+row("Mode",current.mode)+
    row("Preflight",p.pass===true?"PASS":p.pass===false?"FAIL":"PENDING",p.pass===true?"ok":p.pass===false?"bad":"warn")+
    row("Process Boundary","FORMAL WORKFLOW UNCHANGED","ok");
  if(p.checks){
    const summary=Object.values(p.checks).filter(v=>v===true).length+"/"+Object.keys(p.checks).length;
    html+='<details '+(p.pass===false?'open':'')+'><summary>Preflight checks · '+h(summary)+' PASS</summary>'+renderCheckGrid(p.checks)+'</details>';
  }
  html+='<h3>Remote evidence</h3>'+renderRemote();
  el("evidence").innerHTML=html;
  el("history").innerHTML=(current.history||[]).slice().reverse().map(x=>
    '<div class="history-item"><strong>'+h(x.action)+'</strong><span class="mono">'+h(localTime(x.at||""))+'</span></div>'
  ).join("");
}

function actionButton(name,fn,cls=""){
  const b=document.createElement("button");
  b.textContent=name;b.className=cls;b.onclick=fn;return b;
}

function renderActive(){
  const a=el("activePanel");
  if(!current){
    el("activeTitle").textContent="Active Stage";
    a.innerHTML='<span class="empty">Start or load a Session.</span>';
    return;
  }
  el("activeTitle").textContent="Active Stage｜"+current.current_stage;
  a.innerHTML=row("Session",current.session_id)+row("Shot",current.shot_id)+row("Status",current.status)+'<div class="actions" id="stageActions"></div>';
  const actions=el("stageActions");
  const add=(name,fn,cls="")=>actions.appendChild(actionButton(name,fn,cls));

  switch(current.status){
    case "DESIGN_PENDING":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">确认上方 Design Summary 与 Bundle metadata 后，由 Product Owner 批准进入 PREFLIGHT。</div>');
      add("Approve Design",approveDesign,"primary"); break;

    case "DESIGN_APPROVED":
    case "PREFLIGHT_FAILED":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">PREFLIGHT 会检查 Bundle、Drive、GitHub qualification branch 与远端测试路径冲突。</div>');
      if((current.preflight||{}).checks) a.insertAdjacentHTML("beforeend",renderCheckGrid(current.preflight.checks));
      add("Run PREFLIGHT",runPreflight,"primary"); break;

    case "PREFLIGHT_PASS":
    case "AWAITING_CANDIDATE":
      a.insertAdjacentHTML("beforeend",
        '<div class="stage-note"><strong>Work Handoff READY</strong><br><span class="muted">正式生产中由 Console 自动准备执行包；手工下载仅保留为诊断导出。</span></div>'+
        '<div class="drop" id="drop" tabindex="0"><strong>拖拽 1 张 Candidate PNG 到这里</strong>'+
        '<p class="muted">或使用文件选择。只接受 PNG；同一 Session + Candidate ID 重复请求会被幂等保护。</p>'+
        '<div class="actions"><input id="candidateId" placeholder="CANDIDATE_01" value="CANDIDATE_01">'+
        '<input id="candidateFile" type="file" accept="image/png">'+
        '<button id="candidateUpload" class="primary">Upload + Drive Exact Verify</button>'+
        '<a id="handoffLink" class="btn" href="#">Diagnostic: Export Handoff</a></div></div>');
      bindDrop(); break;

    case "CANDIDATE_VERIFIED_PENDING_PO":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">Candidate 已完成 Drive readback exact verification。PO 决策会绑定 Candidate ID + Drive File ID + SHA256。</div>');
      add("PO Approve",()=>review("approve"),"primary");
      add("PO Reject",()=>review("reject"),"danger"); break;

    case "REJECTED":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">Rejected Candidate 保留为不可变历史；新图必须使用新的 Candidate ID。</div>');
      add("Open New Candidate",newCandidate,"primary"); break;

    case "PO_APPROVED_PENDING_PUBLICATION":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">仅向 qualification branch 写测试 publication metadata；不会写正式 Story Shot。</div>');
      add("Publish Qualification Metadata",publish,"primary"); break;

    case "PUBLISHED_NOT_REGISTERED":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">Publication 已存在。Registration 失败时只能 Retry Registration，不重写 publication。</div>');
      add("Register / Retry Registration Only",register,"primary"); break;

    case "REGISTERED_PENDING_LOCK":
      add("LOCK Identity",lock,"primary"); break;

    case "LOCKED_PENDING_CLOSEOUT":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">Closeout 将写 qualification-only closeout evidence，并再次确认 main 未变化。</div>');
      add("Closeout Qualification",closeout,"primary"); break;

    case "CLOSED":
      actions.innerHTML='<a class="btn primary-link" href="/api/v1/receipt?session_id='+encodeURIComponent(current.session_id)+'">Download Qualification Receipt</a>';
      break;
  }
}

function render(){
  renderWorkflow();
  renderIdentity();
  renderActive();
  renderEvidence();
}

async function refreshSystem(){
  try{
    const j=await api("/api/v1/status");
    el("system").innerHTML=
      row("Release",j.release)+
      row("Drive",j.drive_connected?"CONNECTED":"NOT CONNECTED",j.drive_connected?"ok":"warn")+
      row("Drive Folder",j.drive_folder_bound?(j.drive_folder_name||"BOUND"):"NOT BOUND")+
      row("GitHub CLI",j.github_cli?"READY":"NOT READY",j.github_cli?"ok":"warn")+
      row("Boundary",j.production_process_boundary,"mono")+
      row("Local Sessions",(j.sessions||[]).length);
  }catch(e){el("system").textContent=e.message}
}

async function start(){
  try{
    const j=await post("/api/v1/session/start",{
      session_id:el("sessionId").value.trim(),shot_id:el("shotId").value.trim(),
      mode:"QUALIFICATION",bundle:bundle(),design_summary:el("designSummary").value.trim()
    });
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function load(){
  try{
    if(!sid()) throw new Error("请输入 Session ID");
    const j=await api("/api/v1/session?session_id="+encodeURIComponent(sid()));
    setSession(j.session);
    await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function recoverExternal(){
  const b=el("recoverBtn");
  try{
    const sessionId=el("sessionId").value.trim();
    if(!sessionId) throw new Error("请输入 Session ID");
    if(b)b.disabled=true;
    showAction("正在仅凭 GitHub qualification evidence + Drive binary 重建本地 Session…","working");
    const j=await post("/api/v1/session/recover",{session_id:sessionId});
    setSession(j.session);
    remoteEvidence=j.remote||null;
    renderEvidence();
    await refreshSystem();
    showAction("External Recovery 完成 · Status = "+j.session.status,"success");
  }catch(e){
    showAction("External Recovery FAIL · "+e.message,"error");
    alert(e.message);
  }finally{
    if(b)b.disabled=false;
  }
}

async function reconcile(){
  const b=el("reconcileBtn");
  try{
    if(!current) throw new Error("请先 Load Session");
    if(b)b.disabled=true;
    showAction("正在从 GitHub qualification evidence + Drive binary 核对 Session…","working");
    const j=await post("/api/v1/session/reconcile",{session_id:sid()});
    setSession(j.session);
    remoteEvidence=j.remote||null;
    renderEvidence();
    await refreshSystem();
    showAction(
      "External Evidence Reconcile 完成 · "+(j.changed?"已按外部证据重新校准":"外部证据一致，无需改变状态")+" · Status = "+j.session.status,
      "success"
    );
  }catch(e){
    showAction("External Evidence Reconcile FAIL · "+e.message,"error");
    alert(e.message);
  }finally{
    if(b)b.disabled=false;
  }
}
async function refreshEvidence(){
  if(!current) return;
  try{
    const j=await api("/api/v1/qualification/evidence?session_id="+encodeURIComponent(sid()));
    remoteEvidence=j.remote;
    renderEvidence();
  }catch(e){
    remoteEvidence={error:e.message};
    renderEvidence();
  }
}
async function approveDesign(){
  try{
    const j=await post("/api/v1/design/approve",{session_id:sid(),bundle:bundle(),design_summary:el("designSummary").value.trim()});
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function runPreflight(){
  try{
    const j=await post("/api/v1/preflight",{session_id:sid()});
    setSession(j.session);
    await refreshEvidence();
  }catch(e){alert(e.message)}
}
function bindDrop(){
  const d=el("drop"),f=el("candidateFile"),b=el("candidateUpload"),link=el("handoffLink"),cid=el("candidateId");
  if(!d)return;
  const updateLink=()=>{link.href="/api/v1/work-handoff?session_id="+encodeURIComponent(sid())+"&candidate_id="+encodeURIComponent((cid.value||"CANDIDATE_01").trim())};
  cid.oninput=updateLink;updateLink();
  b.onclick=()=>upload(f.files[0]);

  const stop=e=>{e.preventDefault();e.stopPropagation()};
  ["dragenter","dragover","dragleave","drop"].forEach(name=>d.addEventListener(name,stop,false));
  ["dragenter","dragover"].forEach(name=>d.addEventListener(name,()=>d.classList.add("drag"),false));
  ["dragleave","drop"].forEach(name=>d.addEventListener(name,()=>d.classList.remove("drag"),false));
  d.addEventListener("drop",e=>{
    const files=e.dataTransfer&&e.dataTransfer.files;
    if(files&&files.length) upload(files[0]);
    else showAction("Drag & Drop FAIL · 未检测到文件","error");
  },false);
}
async function upload(file){
  try{
    if(!file)throw new Error("请选择 PNG");
    if(file.type&&file.type!=="image/png")throw new Error("Candidate 必须是 PNG");
    const fd=new FormData();
    fd.append("session_id",sid());
    fd.append("candidate_id",(el("candidateId").value||"CANDIDATE_01").trim());
    fd.append("file",file);
    const j=await api("/api/v1/candidate/upload",{method:"POST",body:fd});
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function review(action){
  try{
    const reason=action==="reject"?(prompt("Reject reason（可选）","")||""):"";
    const j=await post("/api/v1/candidate/review",{session_id:sid(),action,reason});
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function newCandidate(){
  try{
    const j=await post("/api/v1/candidate/new",{session_id:sid()});
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function publish(){
  try{
    const j=await post("/api/v1/publish",{session_id:sid()});
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function register(){
  try{
    const j=await post("/api/v1/register",{session_id:sid()});
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function lock(){
  try{
    const j=await post("/api/v1/lock",{session_id:sid()});
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function closeout(){
  try{
    const j=await post("/api/v1/closeout",{session_id:sid()});
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}

el("startBtn").onclick=start;
el("loadBtn").onclick=load;
el("recoverBtn").onclick=recoverExternal;
el("reconcileBtn").onclick=reconcile;
el("newSessionBtn").onclick=resetWorkspace;
el("refreshEvidenceBtn").onclick=refreshEvidence;

const saved=localStorage.getItem("blpc_session_id");
if(saved) el("sessionId").value=saved;
setLockedInputs();
refreshSystem();
render();
if(saved) load();
