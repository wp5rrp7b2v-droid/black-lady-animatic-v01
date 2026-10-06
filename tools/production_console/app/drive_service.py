import hashlib
import json
import os
import re
import subprocess
from io import BytesIO
from pathlib import Path

from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2.credentials import Credentials
from PIL import Image

from config import TOKEN, SCOPES, BINDING, FOLDER_MIME
from state_store import read_json, write_json


def _parse_scutil_proxy():
    try:
        output = subprocess.check_output(["/usr/sbin/scutil", "--proxy"], text=True, stderr=subprocess.DEVNULL, timeout=3)
    except Exception:
        return {}
    values = {}
    for line in output.splitlines():
        m = re.match(r"\s*([A-Za-z0-9_]+)\s*:\s*(.*?)\s*$", line)
        if m:
            values[m.group(1)] = m.group(2)
    return values


def configure_proxy_from_macos():
    info = _parse_scutil_proxy()
    if not (os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")) and info.get("HTTPEnable") == "1" and info.get("HTTPProxy") and info.get("HTTPPort"):
        value = f"http://{info['HTTPProxy']}:{info['HTTPPort']}"
        os.environ["HTTP_PROXY"] = os.environ["http_proxy"] = value
    if not (os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")) and info.get("HTTPSEnable") == "1" and info.get("HTTPSProxy") and info.get("HTTPSPort"):
        value = f"http://{info['HTTPSProxy']}:{info['HTTPSPort']}"
        os.environ["HTTPS_PROXY"] = os.environ["https_proxy"] = value
    no_proxy = os.environ.get("NO_PROXY") or os.environ.get("no_proxy") or ""
    parts = [p.strip() for p in no_proxy.split(",") if p.strip()]
    for host in ("127.0.0.1", "localhost"):
        if host not in parts:
            parts.append(host)
    os.environ["NO_PROXY"] = os.environ["no_proxy"] = ",".join(parts)


configure_proxy_from_macos()


def load_creds():
    if not TOKEN.exists():
        return None
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        write_json(TOKEN, json.loads(creds.to_json()))
    return creds if creds.valid else None


def connected() -> bool:
    try:
        return bool(load_creds())
    except Exception:
        return False


def authorized_session(creds=None):
    creds = creds or load_creds()
    if not creds:
        raise RuntimeError("Google Drive 尚未连接")
    return AuthorizedSession(creds)


def drive_get_metadata(file_id, creds=None, fields="id,name,mimeType,webViewLink,parents,size"):
    s = authorized_session(creds)
    r = s.get(f"https://www.googleapis.com/drive/v3/files/{file_id}", params={"fields": fields}, timeout=20)
    r.raise_for_status()
    return r.json()




def resolve_picker_selection(picked_id, creds):
    selected = drive_get_metadata(picked_id, creds)
    if selected.get("mimeType") == FOLDER_MIME:
        return selected, {
            "picker_selected_id": selected.get("id"),
            "picker_selected_name": selected.get("name"),
            "picker_selected_type": "folder",
            "binding_resolution": "direct_folder_selection",
        }
    parents = selected.get("parents") or []
    if not parents:
        raise RuntimeError("Picker 返回的是文件，但 Drive 未返回其父文件夹。请直接选择目标文件夹。")
    parent = drive_get_metadata(parents[0], creds)
    if parent.get("mimeType") != FOLDER_MIME:
        raise RuntimeError("Picker 返回文件的父项不是 Google Drive 文件夹。")
    return parent, {
        "picker_selected_id": selected.get("id"),
        "picker_selected_name": selected.get("name"),
        "picker_selected_type": "file",
        "binding_resolution": "parent_folder_of_selected_file",
    }

def drive_upload_bytes(folder_id, file_name, mime_type, raw, creds=None):
    s = authorized_session(creds)
    boundary = "blackladyconsoleboundary"
    meta = json.dumps({"name": file_name, "parents": [folder_id]}, ensure_ascii=False).encode("utf-8")
    body = (
        f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n".encode()
        + meta
        + f"\r\n--{boundary}\r\nContent-Type: {mime_type}\r\n\r\n".encode()
        + raw
        + f"\r\n--{boundary}--\r\n".encode()
    )
    r = s.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name,mimeType,webViewLink,size",
        data=body,
        headers={"Content-Type": f"multipart/related; boundary={boundary}"},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def drive_download_bytes(file_id, creds=None):
    s = authorized_session(creds)
    r = s.get(f"https://www.googleapis.com/drive/v3/files/{file_id}", params={"alt": "media"}, timeout=60)
    r.raise_for_status()
    return r.content


def image_meta(data: bytes):
    with Image.open(BytesIO(data)) as im:
        return {"width": im.width, "height": im.height, "format": im.format, "mode": im.mode}


def sha256(data: bytes):
    return hashlib.sha256(data).hexdigest()


def get_bound_folder():
    binding = read_json(BINDING, {})
    folder_id = binding.get("folder_id") or binding.get("id")
    return binding, folder_id


def exact_upload(file_name: str, mime_type: str, raw: bytes):
    binding, folder_id = get_bound_folder()
    if not folder_id:
        raise RuntimeError("Google Drive 目标文件夹尚未绑定")
    creds = load_creds()
    if not creds:
        raise RuntimeError("Google Drive 尚未连接")
    created = drive_upload_bytes(folder_id, file_name, mime_type, raw, creds)
    returned = drive_download_bytes(created["id"], creds)
    src_sha, dst_sha = sha256(raw), sha256(returned)
    src_meta, dst_meta = image_meta(raw), image_meta(returned)
    checks = {
        "sha256_match": src_sha == dst_sha,
        "byte_size_match": len(raw) == len(returned),
        "dimensions_match": (src_meta["width"], src_meta["height"]) == (dst_meta["width"], dst_meta["height"]),
        "drive_file_id_recorded": bool(created.get("id")),
    }
    if not all(checks.values()):
        raise RuntimeError(f"Drive exact-binary verification FAIL: {checks}")
    return {
        "drive_file_id": created.get("id"),
        "drive_file_name": created.get("name"),
        "drive_file_url": created.get("webViewLink") or f"https://drive.google.com/file/d/{created.get('id')}/view",
        "sha256": src_sha,
        "byte_size": len(raw),
        "width": src_meta["width"],
        "height": src_meta["height"],
        "mime_type": mime_type,
        "exact_binary_pass": True,
        "exact_binary_checks": checks,
    }
