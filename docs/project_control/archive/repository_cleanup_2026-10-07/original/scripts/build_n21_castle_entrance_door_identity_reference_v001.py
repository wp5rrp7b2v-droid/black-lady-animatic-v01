#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--crop-plan", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    plan_path = Path(args.crop_plan)
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    src_info = plan["source"]
    crop_info = plan["crop"]
    out_info = plan["output"]

    src = Path(src_info["path"])
    if not src.is_file():
        raise SystemExit(f"missing source: {src}")

    actual_bytes = src.stat().st_size
    actual_sha = sha256_file(src)
    if actual_bytes != int(src_info["byte_size"]):
        raise SystemExit(f"source byte mismatch: {actual_bytes} != {src_info['byte_size']}")
    if actual_sha != src_info["sha256"]:
        raise SystemExit(f"source sha256 mismatch: {actual_sha} != {src_info['sha256']}")

    with Image.open(src) as im:
        im.load()
        if list(im.size) != [int(src_info["width"]), int(src_info["height"])]:
            raise SystemExit(f"source dimensions mismatch: {im.size}")
        if im.mode != src_info["mode"]:
            raise SystemExit(f"source mode mismatch: {im.mode}")
        box = (
            int(crop_info["x1"]),
            int(crop_info["y1"]),
            int(crop_info["x2"]),
            int(crop_info["y2"]),
        )
        cropped = im.crop(box)
        expected_size = (int(crop_info["width"]), int(crop_info["height"]))
        if cropped.size != expected_size:
            raise SystemExit(f"crop size mismatch: {cropped.size} != {expected_size}")
        if cropped.size != (int(out_info["width"]), int(out_info["height"])):
            raise SystemExit("output dimensions do not match locked crop plan")
        if out_info.get("resize", False):
            raise SystemExit("resize is forbidden for this reference")
        if cropped.mode != out_info["mode"]:
            cropped = cropped.convert(out_info["mode"])

        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        cropped.save(out, format="PNG", optimize=False, compress_level=9)

    out_sha = sha256_file(out)
    out_bytes = out.stat().st_size
    report = {
        "schema_version":"1.0",
        "reference_id":plan["reference_id"],
        "source_path":src.as_posix(),
        "source_sha256":actual_sha,
        "source_bytes":actual_bytes,
        "crop_box_ltrb":[
            int(crop_info["x1"]), int(crop_info["y1"]),
            int(crop_info["x2"]), int(crop_info["y2"])
        ],
        "output_width":int(out_info["width"]),
        "output_height":int(out_info["height"]),
        "output_mode":out_info["mode"],
        "output_sha256":out_sha,
        "output_bytes":out_bytes
    }
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

if __name__ == "__main__":
    main()
