from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import numpy as np
import torch
from PIL import Image, ImageOps
from transformers import AutoImageProcessor, AutoModelForDepthEstimation

MODEL_ID = "depth-anything/Depth-Anything-V2-Small-hf"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    image = Image.open(input_path).convert("RGB")
    width, height = image.size

    processor = AutoImageProcessor.from_pretrained(MODEL_ID)
    model = AutoModelForDepthEstimation.from_pretrained(MODEL_ID)
    model.eval()

    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)

    depth = outputs.predicted_depth
    depth = torch.nn.functional.interpolate(
        depth.unsqueeze(1),
        size=(height, width),
        mode="bicubic",
        align_corners=False,
    ).squeeze()

    raw = depth.cpu().numpy().astype(np.float32)
    dmin = float(raw.min())
    dmax = float(raw.max())
    if not np.isfinite(raw).all() or dmax <= dmin:
        raise RuntimeError("Invalid predicted depth range")

    # Depth Anything V2 relative depth: larger values are nearer.
    # DepthFlow expects normalized depth with near=white.
    normalized = (raw - dmin) / (dmax - dmin)
    depth_u8 = np.clip(np.rint(normalized * 255.0), 0, 255).astype(np.uint8)

    depth_path = outdir / "A01_DEPTH_DA2_SMALL_PROOF_V001.png"
    Image.fromarray(depth_u8, mode="L").save(depth_path, format="PNG", optimize=False)

    # Simple audit preview: canonical source on left, depth map on right.
    depth_rgb = ImageOps.autocontrast(Image.fromarray(depth_u8, mode="L")).convert("RGB")
    preview = Image.new("RGB", (width * 2, height))
    preview.paste(image, (0, 0))
    preview.paste(depth_rgb, (width, 0))
    preview_path = outdir / "A01_DEPTH_PREVIEW_V001.png"
    preview.save(preview_path, format="PNG", optimize=False)

    p = np.percentile(raw, [1, 5, 25, 50, 75, 95, 99]).tolist()
    report_path = outdir / "DEPTH_GATE_A_REPORT.txt"
    report_path.write_text(
        "\n".join(
            [
                "P03_A01_DEPTHFLOW_PROOF_V001 / GATE_A",
                f"model={MODEL_ID}",
                "estimator=Depth Anything V2 Small",
                "depth_semantics=relative_normalized_near_white",
                f"input={input_path}",
                f"input_dimensions={width}x{height}",
                f"input_sha256={sha256(input_path)}",
                f"raw_depth_min={dmin:.8f}",
                f"raw_depth_max={dmax:.8f}",
                "raw_depth_percentiles_1_5_25_50_75_95_99="
                + ",".join(f"{x:.8f}" for x in p),
                f"depth_output={depth_path.name}",
                f"depth_dimensions={width}x{height}",
                f"depth_sha256={sha256(depth_path)}",
                f"preview_output={preview_path.name}",
                f"preview_sha256={sha256(preview_path)}",
                "GATE_A_GENERATION=PASS",
                "GATE_B_2_5D_RENDER=NOT_RUN",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(report_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
