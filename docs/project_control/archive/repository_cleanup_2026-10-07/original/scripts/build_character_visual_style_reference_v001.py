#!/usr/bin/env python3
"""Deterministically build CHARACTER_VISUAL_STYLE_REFERENCE_V001.

This builder performs only exact-source validation, fixed integer crops,
deterministic geometric resampling, and fixed-canvas composition.
It performs no generative or semantic image operation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image, __version__ as PILLOW_VERSION

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_REFERENCE_ID = "CHARACTER_VISUAL_STYLE_REFERENCE_V001"
EXPECTED_SOURCE_SIZE = (941, 1672)
EXPECTED_OUTPUT_SIZE = (1536, 1024)
EXPECTED_MODE = "RGB"
EXPECTED_BACKGROUND = (144, 144, 144)
EXPECTED_ALGORITHM = "PIL.Image.Resampling.LANCZOS"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_plan(path: Path) -> dict:
    plan = json.loads(path.read_text(encoding="utf-8"))
    if plan.get("reference_id") != EXPECTED_REFERENCE_ID:
        fail(f"unexpected reference_id: {plan.get('reference_id')}")
    if plan.get("source_image_dimensions") != {"width": 941, "height": 1672}:
        fail("source_image_dimensions differ from locked contract")

    output = plan.get("output", {})
    if (output.get("width"), output.get("height")) != EXPECTED_OUTPUT_SIZE:
        fail("output dimensions differ from locked contract")
    if output.get("mode") != EXPECTED_MODE:
        fail("output mode differs from locked contract")
    if tuple(output.get("background_rgb", [])) != EXPECTED_BACKGROUND:
        fail("background_rgb differs from locked contract")

    resize = plan.get("resize", {})
    if resize.get("algorithm") != EXPECTED_ALGORITHM:
        fail("resize algorithm differs from locked contract")
    if resize.get("fit_mode") != "contain":
        fail("fit mode differs from locked contract")
    if resize.get("rounding") != "int(round(source_dimension * scale))":
        fail("rounding differs from locked contract")

    panels = plan.get("panels", [])
    if len(panels) != 6:
        fail(f"expected 6 panels, found {len(panels)}")
    if [p.get("panel") for p in panels] != [1, 2, 3, 4, 5, 6]:
        fail("panel IDs/order differ from locked contract")
    return plan


def validate_png_source(panel: dict) -> Image.Image:
    path = Path(panel["source_path"])
    if not path.is_file():
        fail(f"missing source: {path}")

    raw = path.read_bytes()
    if not raw.startswith(PNG_SIGNATURE):
        fail(f"PNG signature mismatch: {path}")
    if len(raw) != int(panel["source_byte_size"]):
        fail(f"byte size mismatch: {path}")
    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != panel["source_sha256"]:
        fail(f"SHA-256 mismatch: {path}")

    with Image.open(path) as im:
        if im.format != "PNG":
            fail(f"not decoded as PNG: {path}")
        if im.size != EXPECTED_SOURCE_SIZE:
            fail(f"source dimensions mismatch: {path} = {im.size}")
        im.load()

        if "A" in im.getbands():
            alpha = im.getchannel("A")
            extrema = alpha.getextrema()
            if extrema != (255, 255):
                fail(f"non-opaque alpha is not allowed: {path}")

        return im.convert("RGB")


def validate_crop_and_geometry(panel: dict) -> tuple[tuple[int, int, int, int], tuple[int, int], tuple[int, int]]:
    xywh = panel["crop_xywh"]
    x = int(xywh["x"])
    y = int(xywh["y"])
    w = int(xywh["width"])
    h = int(xywh["height"])
    ltrb = tuple(int(v) for v in panel["crop_box_ltrb"])

    if ltrb != (x, y, x + w, y + h):
        fail(f"panel {panel['panel']} crop_xywh and crop_box_ltrb disagree")
    if x < 0 or y < 0 or w <= 0 or h <= 0:
        fail(f"panel {panel['panel']} has invalid crop dimensions")
    if x + w > EXPECTED_SOURCE_SIZE[0] or y + h > EXPECTED_SOURCE_SIZE[1]:
        fail(f"panel {panel['panel']} crop extends outside source")

    slot_x, slot_y, slot_w, slot_h = (int(v) for v in panel["panel_slot_xywh"])
    scale = min(slot_w / w, slot_h / h)
    calc_w = int(round(w * scale))
    calc_h = int(round(h * scale))
    locked_size = tuple(int(v) for v in panel["resized_wh"])
    if (calc_w, calc_h) != locked_size:
        fail(
            f"panel {panel['panel']} calculated resized size {(calc_w, calc_h)} "
            f"!= locked {locked_size}"
        )

    calc_x = slot_x + int(round((slot_w - calc_w) / 2))
    calc_y = slot_y + int(round((slot_h - calc_h) / 2))
    locked_paste = tuple(int(v) for v in panel["paste_xy"])
    if (calc_x, calc_y) != locked_paste:
        fail(
            f"panel {panel['panel']} calculated paste {(calc_x, calc_y)} "
            f"!= locked {locked_paste}"
        )

    if calc_x < slot_x or calc_y < slot_y:
        fail(f"panel {panel['panel']} paste starts outside slot")
    if calc_x + calc_w > slot_x + slot_w or calc_y + calc_h > slot_y + slot_h:
        fail(f"panel {panel['panel']} paste extends outside slot")

    return ltrb, locked_size, locked_paste


def build(plan: dict, output_path: Path) -> dict:
    canvas = Image.new(EXPECTED_MODE, EXPECTED_OUTPUT_SIZE, EXPECTED_BACKGROUND)
    source_reports = []

    for panel in plan["panels"]:
        src = validate_png_source(panel)
        ltrb, resized_wh, paste_xy = validate_crop_and_geometry(panel)

        crop = src.crop(ltrb)
        if crop.size != (ltrb[2] - ltrb[0], ltrb[3] - ltrb[1]):
            fail(f"panel {panel['panel']} crop size mismatch")

        resized = crop.resize(resized_wh, resample=Image.Resampling.LANCZOS)
        canvas.paste(resized, paste_xy)

        source_reports.append(
            {
                "panel": panel["panel"],
                "source_asset_id": panel["source_asset_id"],
                "source_path": panel["source_path"],
                "source_sha256": panel["source_sha256"],
                "source_byte_size": panel["source_byte_size"],
                "crop_box_ltrb": list(ltrb),
                "resized_wh": list(resized_wh),
                "paste_xy": list(paste_xy),
            }
        )

    if canvas.size != EXPECTED_OUTPUT_SIZE or canvas.mode != EXPECTED_MODE:
        fail("final canvas properties differ from locked contract")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(
        output_path,
        format="PNG",
        optimize=False,
        compress_level=9,
    )

    raw = output_path.read_bytes()
    if not raw.startswith(PNG_SIGNATURE):
        fail("output PNG signature mismatch")

    with Image.open(output_path) as check:
        if check.format != "PNG":
            fail("output does not decode as PNG")
        if check.size != EXPECTED_OUTPUT_SIZE:
            fail(f"output dimensions mismatch: {check.size}")
        if check.mode != EXPECTED_MODE:
            fail(f"output mode mismatch: {check.mode}")

    return {
        "schema_version": "1.0",
        "reference_id": EXPECTED_REFERENCE_ID,
        "status": "BUILD_PASS",
        "output_path": output_path.as_posix(),
        "output_dimensions": list(EXPECTED_OUTPUT_SIZE),
        "output_mode": EXPECTED_MODE,
        "output_sha256": hashlib.sha256(raw).hexdigest(),
        "output_byte_size": len(raw),
        "pillow_version": PILLOW_VERSION,
        "resampling": EXPECTED_ALGORITHM,
        "png_save_options": {"optimize": False, "compress_level": 9},
        "no_generative_processing": True,
        "sources": source_reports,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--crop-plan", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    crop_plan_path = Path(args.crop_plan)
    output_path = Path(args.output)
    report_path = Path(args.report)

    plan = load_plan(crop_plan_path)
    report = build(plan, output_path)
    report["crop_plan_path"] = crop_plan_path.as_posix()
    report["crop_plan_sha256"] = sha256_file(crop_plan_path)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"PASS: {EXPECTED_REFERENCE_ID} deterministic build completed")
    print(f"OUTPUT_SHA256={report['output_sha256']}")
    print(f"OUTPUT_BYTES={report['output_byte_size']}")
    print(f"OUTPUT_DIMENSIONS={EXPECTED_OUTPUT_SIZE[0]}x{EXPECTED_OUTPUT_SIZE[1]}")
    print(f"PILLOW_VERSION={PILLOW_VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
