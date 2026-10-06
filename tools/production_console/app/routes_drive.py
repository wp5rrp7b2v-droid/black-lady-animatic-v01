import json
import os
import secrets
import traceback
from flask import Blueprint, request, redirect, session
from google_auth_oauthlib.flow import Flow

from common import ok, fail
from config import HOST, PORT, SCOPES, CREDENTIALS, TOKEN, BINDING
from state_store import write_json
from drive_service import exact_upload, resolve_picker_selection

bp = Blueprint("drive_routes", __name__)

@bp.get("/connect")
def connect():
    if not CREDENTIALS.exists():
        return fail(f"OAuth credentials 缺失: {CREDENTIALS}", 404)
    code_verifier = secrets.token_urlsafe(64)
    flow = Flow.from_client_secrets_file(str(CREDENTIALS), scopes=SCOPES, code_verifier=code_verifier)
    flow.redirect_uri = f"http://{HOST}:{PORT}/oauth2callback"
    authorization_url, state = flow.authorization_url(
        access_type="offline", prompt="consent", include_granted_scopes="false",
        trigger_onepick="true", allow_folder_selection="true",
    )
    session["oauth_state"] = state
    session["oauth_code_verifier"] = code_verifier
    return redirect(authorization_url)


@bp.get("/oauth2callback")
def oauth2callback():
    if request.args.get("error"):
        return redirect("/?oauth_error=" + request.args.get("error", "unknown"))
    state = session.get("oauth_state")
    if not state or request.args.get("state") != state:
        return fail("OAuth state 丢失或不匹配，请重新连接", 400)
    picked = [x for x in request.args.get("picked_file_ids", "").split(",") if x]
    if not picked:
        return redirect("/?picker_error=no_item_selected")
    code = request.args.get("code")
    code_verifier = session.get("oauth_code_verifier")
    if not code or not code_verifier:
        return fail("OAuth callback 缺少 authorization code 或 PKCE verifier", 400)
    try:
        flow = Flow.from_client_secrets_file(str(CREDENTIALS), scopes=SCOPES, state=state, code_verifier=code_verifier)
        flow.redirect_uri = f"http://{HOST}:{PORT}/oauth2callback"
        os.environ.setdefault("OAUTHLIB_INSECURE_TRANSPORT", "1")
        flow.fetch_token(code=code)
        creds = flow.credentials
        write_json(TOKEN, json.loads(creds.to_json()))
        folder_meta, resolution = resolve_picker_selection(picked[0], creds)
        write_json(BINDING, {
            "folder_id": folder_meta["id"],
            "folder_name": folder_meta.get("name"),
            "folder_url": folder_meta.get("webViewLink") or f"https://drive.google.com/drive/folders/{folder_meta['id']}",
            **resolution,
        })
        session.pop("oauth_state", None); session.pop("oauth_code_verifier", None)
        return redirect("/?connected=1")
    except Exception as e:
        traceback.print_exc()
        return fail(f"OAuth callback failed: {type(e).__name__}: {e}", 500)


@bp.post("/api/v1/drive/verify-upload")
def drive_verify_upload():
    f = request.files.get("file")
    if not f:
        return fail("未收到文件", 400)
    raw = f.read()
    if not raw:
        return fail("空文件", 400)
    if len(raw) > 50 * 1024 * 1024:
        return fail("测试限制为 50 MB 以下", 400)
    try:
        result = exact_upload(f.filename or "candidate.png", f.mimetype or "application/octet-stream", raw)
        return ok(result=result, production_writes={"github":0,"project_control":0,"formal_story_shots":0})
    except Exception as e:
        traceback.print_exc()
