from __future__ import annotations

import math
from importlib.metadata import version
from pathlib import Path

from depthflow.scene import DepthScene


class A01DepthFlowProof(DepthScene):
    def update(self):
        # Normalized timeline, 0 -> 1.
        t = max(0.0, min(1.0, float(self.tau)))
        # Smoothstep for a restrained, cinematic push-in.
        e = t * t * (3.0 - 2.0 * t)

        # Keep the move deliberately subtle: DepthFlow supplies the parallax,
        # while a small zoom helps sell a forward camera move.
        self.state.height = 0.10 + 0.10 * e
        self.state.zoom = 1.00 - 0.055 * e
        self.state.steady = 0.28
        self.state.isometric = 0.18


def main() -> None:
    root = Path(__file__).resolve().parent
    input_dir = root / "input"
    out_dir = root / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    image = Path("production/image_library/approved/A_Series/A01_REBOOT_approved_v001.png")
    depth = input_dir / "A01_DEPTH_DA2_SMALL_PROOF_V001.png"
    output = out_dir / "A01_DEPTHFLOW_CAMERA_PROOF_V001.mp4"

    scene = A01DepthFlowProof(backend="headless")
    scene.input(image=image, depth=depth)

    # H.264 is the required proof codec.
    scene.ffmpeg.h264(preset="medium", crf=20)

    scene.main(
        output=output,
        fps=30,
        time=2.5,
        width=720,
        height=1280,
        ssaa=1.0,
    )

    print(f"depthflow_version={version('depthflow')}")
    print(f"output={output}")


if __name__ == "__main__":
    main()
