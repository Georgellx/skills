from __future__ import annotations

import argparse
import json
import math
import subprocess
import tempfile
from pathlib import Path


def probe_duration(video: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(video),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def edl_boundary_times(edl_path: Path, duration: float, offset: float) -> list[float]:
    data = json.loads(edl_path.read_text(encoding="utf-8"))
    cursor = 0.0
    result = [0.0]
    ranges = data.get("ranges", []) if isinstance(data, dict) else []
    for item in ranges[:-1]:
        cursor += float(item["end"]) - float(item["start"])
        result.extend((cursor - offset, cursor + offset))
    result.append(max(0.0, duration - 0.20))
    return result


def overview_times(duration: float, count: int) -> list[float]:
    if count <= 1:
        return [duration / 2]
    safe_end = max(0.0, duration - 0.20)
    return [safe_end * index / (count - 1) for index in range(count)]


def extract_frame(video: Path, time_s: float, output: Path, width: int, height: int) -> None:
    label = f"{time_s:08.3f}s"
    windows_font = Path("C:/Windows/Fonts/arial.ttf")
    font_option = ""
    if windows_font.exists():
        escaped_font = windows_font.as_posix().replace(":", r"\:")
        font_option = f":fontfile='{escaped_font}'"
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-ss",
            f"{time_s:.3f}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-vf",
            f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:black,"
            f"drawtext=text='{label}':x=10:y=h-th-10:fontsize=22:fontcolor=white:"
            f"box=1:boxcolor=black@0.65:boxborderw=6{font_option}",
            "-y",
            str(output),
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an overview or cut-boundary contact sheet.")
    parser.add_argument("video", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--edl", type=Path)
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--boundary-offset", type=float, default=0.12)
    parser.add_argument("--thumb-width", type=int, default=270)
    args = parser.parse_args()

    video = args.video.resolve()
    if not video.exists():
        parser.error(f"video not found: {video}")
    duration = probe_duration(video)
    thumb_width = args.thumb_width
    thumb_height = round(thumb_width * 16 / 9)

    if args.edl:
        raw_times = edl_boundary_times(args.edl.resolve(), duration, args.boundary_offset)
    else:
        raw_times = overview_times(duration, args.count)
    times = sorted({round(min(max(time_s, 0.0), max(0.0, duration - 0.20)), 3) for time_s in raw_times})

    columns = max(1, args.columns)
    rows = math.ceil(len(times) / columns)

    with tempfile.TemporaryDirectory(prefix="talking-head-qa-") as temp_name:
        temp = Path(temp_name)
        for index, time_s in enumerate(times):
            frame_path = temp / f"frame_{index:04d}.png"
            extract_frame(video, time_s, frame_path, thumb_width, thumb_height)
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-framerate",
                "1",
                "-i",
                str(temp / "frame_%04d.png"),
                "-frames:v",
                "1",
                "-vf",
                f"tile={columns}x{rows}:padding=0:margin=0",
                "-pix_fmt",
                "yuvj420p" if output.suffix.lower() in {".jpg", ".jpeg"} else "rgb24",
                "-strict",
                "unofficial",
                "-y",
                str(output),
            ],
            check=True,
        )
    print(f"created {output} with {len(times)} frames")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
