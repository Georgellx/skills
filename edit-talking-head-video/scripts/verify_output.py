from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


BLACK_RE = re.compile(
    r"black_start:(?P<start>[0-9.]+)\s+black_end:(?P<end>[0-9.]+)\s+black_duration:(?P<duration>[0-9.]+)"
)
LOUDNESS_RE = re.compile(r"\bI:\s*(-?[0-9.]+)\s+LUFS")
PEAK_RE = re.compile(r"\bPeak:\s*(-?[0-9.]+)\s+dBFS")


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(video: Path) -> dict[str, Any]:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(video),
        ]
    )
    return json.loads(result.stdout)


def measure_audio(video: Path) -> tuple[float | None, float | None]:
    result = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(video),
            "-filter_complex",
            "ebur128=peak=true",
            "-f",
            "null",
            "-",
        ]
    )
    matches_loudness = LOUDNESS_RE.findall(result.stderr)
    matches_peak = PEAK_RE.findall(result.stderr)
    loudness = float(matches_loudness[-1]) if matches_loudness else None
    peak = float(matches_peak[-1]) if matches_peak else None
    return loudness, peak


def detect_black(video: Path) -> list[dict[str, float]]:
    result = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(video),
            "-vf",
            "blackdetect=d=0.10:pix_th=0.10",
            "-an",
            "-f",
            "null",
            "-",
        ]
    )
    return [
        {key: float(value) for key, value in match.groupdict().items()}
        for match in BLACK_RE.finditer(result.stderr)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a vertical talking-head deliverable.")
    parser.add_argument("video", type=Path)
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--fps", type=float, default=30.0)
    parser.add_argument("--duration", type=float)
    parser.add_argument("--lufs-min", type=float, default=-16.0)
    parser.add_argument("--lufs-max", type=float, default=-13.0)
    parser.add_argument("--true-peak-max", type=float, default=-1.0)
    parser.add_argument("--allow-black-seconds", type=float, default=0.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    video = args.video.resolve()
    if not video.exists():
        parser.error(f"video not found: {video}")

    errors: list[str] = []
    warnings: list[str] = []
    media = probe(video)
    streams = media.get("streams", [])
    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    if len(video_streams) != 1:
        errors.append(f"expected one video stream, found {len(video_streams)}")
    if not audio_streams:
        errors.append("audio stream is missing")

    width = height = None
    fps = None
    video_codec = None
    if video_streams:
        stream = video_streams[0]
        width = int(stream.get("width", 0))
        height = int(stream.get("height", 0))
        video_codec = stream.get("codec_name")
        try:
            fps = float(Fraction(stream.get("avg_frame_rate", "0/1")))
        except (ValueError, ZeroDivisionError):
            fps = 0.0
        if (width, height) != (args.width, args.height):
            errors.append(f"frame size is {width}x{height}, expected {args.width}x{args.height}")
        if abs(fps - args.fps) > 0.01:
            errors.append(f"frame rate is {fps:.3f}, expected {args.fps:.3f}")

    duration = float(media.get("format", {}).get("duration", 0.0))
    if args.duration is not None and abs(duration - args.duration) > 0.1:
        errors.append(f"duration is {duration:.3f}s, expected {args.duration:.3f}s")

    loudness = peak = None
    if audio_streams:
        loudness, peak = measure_audio(video)
        if loudness is None:
            warnings.append("integrated loudness could not be parsed")
        elif not args.lufs_min <= loudness <= args.lufs_max:
            errors.append(f"integrated loudness is {loudness:.1f} LUFS")
        if peak is None:
            warnings.append("true peak could not be parsed")
        elif peak > args.true_peak_max:
            errors.append(f"true peak is {peak:.1f} dBFS")

    black_intervals = detect_black(video)
    black_total = sum(item["duration"] for item in black_intervals)
    if black_total > args.allow_black_seconds + 0.001:
        errors.append(f"black intervals total {black_total:.3f}s")

    report = {
        "video": str(video),
        "passed": not errors,
        "media": {
            "duration_s": round(duration, 3),
            "width": width,
            "height": height,
            "fps": round(fps, 3) if fps is not None else None,
            "video_codec": video_codec,
            "audio_codecs": [stream.get("codec_name") for stream in audio_streams],
            "integrated_lufs": loudness,
            "true_peak_dbfs": peak,
        },
        "black_intervals": black_intervals,
        "errors": errors,
        "warnings": warnings,
    }
    if args.output:
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
