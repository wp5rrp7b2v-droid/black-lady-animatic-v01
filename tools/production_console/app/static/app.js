const STAGES=["DESIGN","PREFLIGHT","GENERATE","REVIEW","PUBLISH","REGISTER","LOCK","CLOSEOUT"];
const STATUS_STAGE={
  DESIGN_PENDING:0,DESIGN_APPROVED:1,PREFLIGHT_FAILED:1,PREFLIGHT_PASS:2,AWAITING_CANDIDATE:2,
  CANDIDATE_VERIFIED_PENDING_PO:3,REJECTED:3,PO_APPROVED_PENDING_PUBLICATION:4,
  PUBLISHED_NOT_REGISTERED:5,REGISTERED_PENDING_LOCK:6,LOCKED_PENDING_CLOSEOUT:7,CLOSED:7
};
let current=null;
let remoteEvidence=null;
let resolvedPackage=null;
let operatorPackage=null;
let currentView=localStorage.getItem("blpc_view")||"diagnostics";
let workspaceEpoch=0;

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
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function withButtonFeedback(button,labels,task){
  const original=button?button.textContent:"";
  try{
    if(button){
      button.disabled=true;
      button.classList.remove("action-success","action-error");
      button.classList.add("action-working");
      button.textContent=labels.working||"Working…";
    }
    showAction(labels.working||"正在执行…","working");
    const result=await task();
    if(button){
      button.classList.remove("action-working");
      button.classList.add("action-success");
      button.textContent=(labels.success||"完成");
    }
    showAction((labels.success||"操作完成"),"success");
    await pause(650);
    return result;
  }catch(e){
    if(button){
      button.classList.remove("action-working","action-success");
      button.classList.add("action-error");
      button.textContent=(labels.error||"失败");
      setTimeout(()=>{
        button.classList.remove("action-error");
        button.disabled=false;
        button.textContent=original;
      },1200);
    }
    showAction((labels.error||"操作失败")+" · "+e.message,"error");
    throw e;
  }
}


function dateStamp(){
  const d=new Date();
  const p=n=>String(n).padStart(2,"0");
  return ""+d.getFullYear()+p(d.getMonth()+1)+p(d.getDate());
}
async function suggestedSessionId(shotId){
  try{
    const s=await refreshSystem();
    const base=(shotId||"SHOT")+"_"+dateStamp()+"_";
    const existing=(s.sessions||[]).map(x=>x.session_id||"");
    let n=1;
    while(existing.includes(base+String(n).padStart(3,"0"))) n++;
    return base+String(n).padStart(3,"0");
  }catch{
    return (shotId||"SHOT")+"_"+dateStamp()+"_001";
  }
}
function resolvedSummaryText(r){
  if(!r)return "";
  const d=r.design_package||{};
  return [
    "Design Package "+(r.package_ready?"READY":"NOT READY")+" from Project Control",
    "Director: "+((d.director_design||{}).status||"NOT STARTED"),
    "Scene Reference: "+((d.scene_reference||{}).status||"NOT STARTED"),
    "Bundle: "+((d.bundle||{}).status||"NOT BUILT")
  ].join("\n");
}
async function applyResolvedPackage(r){
  resolvedPackage=r;
  if(!current){
    el("shotId").value=r.shot_id||"";
    const b=r.bundle||{};
    el("bundleId").value=b.bundle_id||"";
    el("runId").value=b.run_id||"";
    el("artifactId").value=b.artifact_id||"";
    el("artifactDigest").value=b.artifact_digest||"";
    el("referenceCount").value=b.reference_count||"";
    el("referencesExact").checked=b.references_exact===true;
    el("manifestVerified").checked=b.delivery_manifest_verified===true;
    el("generationAllowed").checked=b.generation_allowed===true;
    el("designSummary").value=resolvedSummaryText(r);
    if(!el("sessionId").value.trim()) el("sessionId").value=await suggestedSessionId(r.shot_id);
  }
  const src=r.source||{};
  const sourceBox=el("resolutionSource");
  if(sourceBox){
    sourceBox.innerHTML=
      (src.project_state_blob_sha?'<div class="mono small">Project State blob: '+h(src.project_state_blob_sha)+'</div>':"")+
      (src.main_commit_sha?'<div class="mono small">main commit: '+h(src.main_commit_sha)+'</div>':"");
  }
  setLockedInputs();
  renderOperatorSummary();
}
async function resolveProjectMetadata(shotId="",silent=false){
  const requestEpoch=workspaceEpoch;
  try{
    if(!silent) showAction("正在从 GitHub Project Control 自动解析 Design Package…","working");
    const q=shotId?"?shot_id="+encodeURIComponent(shotId):"";
    const j=await api("/api/v1/design-package/resolve"+q);
    if(requestEpoch!==workspaceEpoch) return null;
    await applyResolvedPackage(j.resolved);
    el("resolveMetadataBtn").classList.remove("next-action");
    if(requestEpoch!==workspaceEpoch) return null;
    if(!silent){
      showAction(
        "Project metadata resolved · "+j.resolved.shot_id+" · "+(j.resolved.package_ready?"Design Package READY":"Design Package NOT READY"),
        j.resolved.package_ready?"success":"working"
      );
    }
    return j.resolved;
  }catch(e){
    if(!silent) showAction("Project metadata resolve FAIL · "+e.message,"error");
    return null;
  }
}

async function refreshOperatorOverview(silent=false){
  try{
    if(!silent) showAction("正在刷新 Operator View Project Control…","working");
    const j=await api("/api/v1/design-package/resolve");
    operatorPackage=j.resolved;
    renderOperatorSummary();
    if(!silent) showAction("Operator View 已刷新 · "+operatorPackage.shot_id,"success");
    return operatorPackage;
  }catch(e){
    if(!silent) showAction("Operator View refresh FAIL · "+e.message,"error");
    return null;
  }
}
function setView(mode){
  currentView=mode==="operator"?"operator":"diagnostics";
  localStorage.setItem("blpc_view",currentView);
  document.body.classList.toggle("operator-view",currentView==="operator");
  el("operatorViewBtn").classList.toggle("active-view",currentView==="operator");
  el("diagnosticViewBtn").classList.toggle("active-view",currentView==="diagnostics");
  setLockedInputs();
  renderOperatorSummary();
  if(currentView==="operator") refreshOperatorOverview(true);
}
function renderOperatorSummary(){
  const box=el("operatorSummaryBody");
  if(!box)return;
  const r=operatorPackage||resolvedPackage||{};
  const s=current||{};
  const b=(current&&current.bundle)||r.bundle||{};
  const candidate=(current&&current.candidate)||{};
  const shot=s.shot_id||r.shot_id||"Resolving…";
  const status=s.status||(r.package_ready?"DESIGN PACKAGE READY":"NO SESSION");
  const stage=s.current_stage||"DESIGN";
  const refs=b.reference_count?String(b.reference_count)+(b.references_exact?" / EXACT":" / CHECK"):"—";
  const artifact=b.artifact_id||"—";
  const generation=current
    ? ((current.preflight||{}).pass===true?"AUTHORIZED":status)
    : (r.generation_authorized?"AUTHORIZED":"WAITING PO AUTHORIZATION");
  const exact=candidate.exact_binary_pass===true?"PASS":(candidate.candidate_id?"NOT VERIFIED":"—");
  let next=((r.project_control||{}).next_action)||"No active Session.";
  if(current) next=status==="CLOSED"?"Workflow complete.":("Continue at "+stage+".");
  else if(r.package_ready&&!r.generation_authorized&&!(r.project_control||{}).next_action) next="Design Package ready; waiting Product Owner generation authorization under the current formal process.";
  else if(r.package_ready&&!(r.project_control||{}).next_action) next="Design Package ready for qualification preflight.";
  box.innerHTML=
    '<div class="operator-grid">'+
      '<div class="operator-cell"><strong>Shot</strong>'+h(shot)+'</div>'+
      '<div class="operator-cell"><strong>Status</strong>'+h(status)+'</div>'+
      '<div class="operator-cell"><strong>Bundle</strong>'+h(b.bundle_id||"—")+'</div>'+
      '<div class="operator-cell"><strong>References</strong>'+h(refs)+'</div>'+
      '<div class="operator-cell"><strong>Artifact</strong>'+h(artifact)+'</div>'+
      '<div class="operator-cell"><strong>Generation</strong>'+h(generation)+'</div>'+
      '<div class="operator-cell"><strong>Candidate</strong>'+h(candidate.candidate_id||"—")+'</div>'+
      '<div class="operator-cell"><strong>Exact Binary</strong>'+h(exact)+'</div>'+
    '</div>'+
    '<div class="operator-next"><strong>Next</strong><br>'+h(next)+'</div>'+
    (r.source?'<div class="readonly-source">Resolved from GitHub Project Control · commit '+h((r.source.main_commit_sha||"").slice(0,12))+'</div>':"")+
    '<div class="actions compact"><button id="operatorRefreshBtn">Refresh Project Control</button><span id="operatorFreshness" class="muted"></span></div>';
  const rb=el("operatorRefreshBtn");
  if(rb) rb.onclick=()=>refreshOperatorOverview(false);
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
  const autoLocked=!has&&!!resolvedPackage;
  const operatorLocked=currentView==="operator";
  el("sessionId").disabled=has||operatorLocked;
  el("shotId").disabled=has||autoLocked||operatorLocked;
  ["bundleId","runId","artifactId","referenceCount","artifactDigest","referencesExact","manifestVerified","generationAllowed","designSummary"]
    .forEach(id=>el(id).disabled=!designEditable||autoLocked||operatorLocked);
  el("startBtn").disabled=has||(!current&&resolvedPackage&&!resolvedPackage.package_ready);
  el("loadBtn").disabled=has;
  el("recoverBtn").disabled=has;
  el("reconcileBtn").disabled=!has;
  el("refreshEvidenceBtn").disabled=!has;
  el("resolveMetadataBtn").disabled=has;
  el("newSessionBtn").disabled=false;
}

function setSession(s){
  current=s;
  remoteEvidence=null;
  resolvedPackage=null;
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

async function resetWorkspace(){
  workspaceEpoch++;
  current=null; remoteEvidence=null; resolvedPackage=null;
  localStorage.removeItem("blpc_session_id");
  ["sessionId","shotId","bundleId","runId","artifactId","artifactDigest","referenceCount","designSummary"]
    .forEach(id=>el(id).value="");
  if(el("resolutionSource")) el("resolutionSource").innerHTML="";
  el("referencesExact").checked=false;
  el("manifestVerified").checked=false;
  el("generationAllowed").checked=false;
  setLockedInputs();
  render();
  showAction("New Session · 正在从 Project Control 准备当前 Shot…","working");
  const resolved=await resolveProjectMetadata("",true);
  if(resolved){
    showAction(
      "New Session ready · "+resolved.shot_id+" · "+(resolved.package_ready?"Design Package READY":"Design Package NOT READY"),
      resolved.package_ready?"success":"working"
    );
  }else{
    showAction("New Session 已清空，但 Project Control 自动解析失败；可在 Diagnostics 中重试 Auto Resolve。","error");
  }
}

function renderWorkflow(){
  const idx=current?(STATUS_STAGE[current.status]??0):-1;
  const closed=!!current&&current.status==="CLOSED";
  el("workflow").innerHTML=STAGES.map((x,i)=>{
    const done=closed||i<idx;
    const active=!closed&&i===idx;
    return '<div class="step '+(active?"active ":"")+(done?"done":"")+'">'+x+'</div>';
  }).join("");
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
  const preflightLabel=p.pass===true?"PASS":p.pass===false?"FAIL":(p.evidence_status||"PENDING");
  let html=row("Status",current.status)+row("Mode",current.mode)+
    row("Preflight",preflightLabel,p.pass===true?"ok":p.pass===false?"bad":"warn")+
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
  b.textContent=name;
  b.className=cls;
  b.onclick=()=>fn(b);
  return b;
}

function renderActive(){
  const a=el("activePanel");
  if(!current){
    el("activeTitle").textContent="Active Stage";
    a.innerHTML='<span class="empty">Start or load a Session.</span>';
    return;
  }
  el("activeTitle").textContent=current.status==="CLOSED"?"Workflow Complete｜CLOSED":"Active Stage｜"+current.current_stage;
  a.innerHTML=row("Session",current.session_id)+row("Shot",current.shot_id)+row("Status",current.status)+'<div class="actions" id="stageActions"></div>';
  const actions=el("stageActions");
  const add=(name,fn,cls="")=>actions.appendChild(actionButton(name,fn,cls));

  switch(current.status){
    case "DESIGN_PENDING":
      a.insertAdjacentHTML("beforeend",'<div class="stage-note">Qualification 模式：确认 Design Package 与测试 metadata 后进入 PREFLIGHT。正式生产中技术 metadata 将自动解析并只读显示。</div>');
      add("Confirm Design Package Ready",approveDesign,"primary"); break;

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
      add("PO Approve",(b)=>review("approve",b),"primary");
      add("PO Reject",(b)=>review("reject",b),"danger"); break;

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
  renderOperatorSummary();
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
    const f=el("operatorFreshness");
    if(f&&operatorPackage&&operatorPackage.source){
      const resolved=(operatorPackage.source.main_commit_sha||"");
      const latest=(j.github_main_sha||"");
      f.textContent=resolved&&latest&&resolved!==latest?"STALE · newer main available":"CURRENT";
      f.className=resolved&&latest&&resolved!==latest?"warn":"ok";
    }
    return j;
  }catch(e){el("system").textContent=e.message; throw e}
}

async function start(){
  try{
    const requestEpoch=workspaceEpoch;
    const j=await post("/api/v1/session/start",{
      session_id:el("sessionId").value.trim(),shot_id:el("shotId").value.trim(),
      mode:"QUALIFICATION",bundle:bundle(),design_summary:el("designSummary").value.trim()
    });
    if(requestEpoch!==workspaceEpoch) return;
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function load(auto=false){
  const requestEpoch=workspaceEpoch;
  try{
    if(!sid()) throw new Error("请输入 Session ID");
    const requestedSessionId=sid();
    const j=await api("/api/v1/session?session_id="+encodeURIComponent(requestedSessionId));
    if(requestEpoch!==workspaceEpoch) return;
    setSession(j.session);
    if(requestEpoch!==workspaceEpoch) return;
    await refreshEvidence();
  }catch(e){
    if(requestEpoch!==workspaceEpoch) return;
    if(auto&&String(e.message||"").includes("Session 不存在")){
      current=null; remoteEvidence=null;
      setLockedInputs(); render();
      showAction("本地 Session 缺失，正在尝试 External Recovery…","working");
      await recoverExternal(null,true);
      return;
    }
    alert(e.message);
  }
}
async function recoverExternal(button=null,silent=false){
  const requestEpoch=workspaceEpoch;
  const b=button||el("recoverBtn");
  try{
    const sessionId=el("sessionId").value.trim();
    if(!sessionId) throw new Error("请输入 Session ID");
    if(b)b.disabled=true;
    showAction("正在仅凭 GitHub qualification evidence + Drive binary 重建本地 Session…","working");
    const j=await post("/api/v1/session/recover",{session_id:sessionId});
    if(requestEpoch!==workspaceEpoch) return;
    setSession(j.session);
    remoteEvidence=j.remote||null;
    renderEvidence();
    await refreshSystem();
    showAction("External Recovery 完成 · Status = "+j.session.status,"success");
  }catch(e){
    showAction("External Recovery · "+e.message,"error");
    if(!silent) alert(e.message);
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
      j.changed
        ? "External Evidence 已重新校准 · Status = "+j.session.status
        : "External Evidence 核对通过 · 状态一致 · Status = "+j.session.status,
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
async function approveDesign(button){
  try{
    const j=await withButtonFeedback(button,{working:"Confirming…",success:"Design Package Ready",error:"Design Gate FAIL"},
      ()=>post("/api/v1/design/approve",{session_id:sid(),bundle:bundle(),design_summary:el("designSummary").value.trim()}));
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function runPreflight(button){
  try{
    const j=await withButtonFeedback(button,{working:"Checking PREFLIGHT…",success:"PREFLIGHT PASS",error:"PREFLIGHT FAIL"},
      ()=>post("/api/v1/preflight",{session_id:sid()}));
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
async function review(action,button){
  try{
    const reason=action==="reject"?(prompt("Reject reason（可选）","")||""):"";
    const j=await withButtonFeedback(
      button,
      action==="approve"
        ? {working:"Approving…",success:"PO Approved",error:"PO Approve FAIL"}
        : {working:"Rejecting…",success:"PO Rejected",error:"PO Reject FAIL"},
      ()=>post("/api/v1/candidate/review",{session_id:sid(),action,reason})
    );
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function newCandidate(button){
  try{
    const j=await withButtonFeedback(button,{working:"Opening…",success:"New Candidate Ready",error:"Open Candidate FAIL"},
      ()=>post("/api/v1/candidate/new",{session_id:sid()}));
    setSession(j.session);
  }catch(e){alert(e.message)}
}
async function publish(button){
  try{
    const j=await withButtonFeedback(button,{working:"Publishing test record…",success:"Publication Record Created",error:"Publication FAIL"},
      ()=>post("/api/v1/publish",{session_id:sid()}));
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function register(button){
  try{
    const j=await withButtonFeedback(button,{working:"Registering…",success:"Registration Complete",error:"Registration FAIL"},
      ()=>post("/api/v1/register",{session_id:sid()}));
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function lock(button){
  try{
    const j=await withButtonFeedback(button,{working:"Locking identity…",success:"LOCK Complete",error:"LOCK FAIL"},
      ()=>post("/api/v1/lock",{session_id:sid()}));
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}
async function closeout(button){
  try{
    const j=await withButtonFeedback(button,{working:"Closing out…",success:"Closeout Complete",error:"Closeout FAIL"},
      ()=>post("/api/v1/closeout",{session_id:sid()}));
    setSession(j.session);await refreshEvidence();
  }catch(e){alert(e.message)}
}

el("startBtn").onclick=start;
el("loadBtn").onclick=()=>load(false);
el("recoverBtn").onclick=()=>recoverExternal(null,false);
el("reconcileBtn").onclick=reconcile;
el("newSessionBtn").onclick=resetWorkspace;
el("refreshEvidenceBtn").onclick=refreshEvidence;
el("resolveMetadataBtn").onclick=()=>resolveProjectMetadata(el("shotId").value.trim(),false);
el("operatorViewBtn").onclick=()=>setView("operator");
el("diagnosticViewBtn").onclick=()=>setView("diagnostics");

const saved=localStorage.getItem("blpc_session_id");
if(saved) el("sessionId").value=saved;
setView(currentView);
refreshSystem();
render();
if(saved) load(true);
