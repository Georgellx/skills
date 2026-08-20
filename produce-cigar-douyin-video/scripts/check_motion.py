#!/usr/bin/env python3
"""Check a preview or final render for frozen/black intervals and sampled motion."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path


FREEZE_DURATION = re.compile(r"freeze_duration:\s*([0-9.]+)")
BLACK_DURATION = re.compile(r"black_duration:([0-9.]+)")


def run(command: list[str], *, binary: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        capture_output=True,
        text=not binary,
        encoding=None if binary else "utf-8",
        errors=None if binary else "replace",
    )


def probe(path: Path) -> dict:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration:stream=codec_type,codec_name,width,height",
            "-of",
            "json",
            str(path),
        ]
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "ffprobe failed")
    return json.loads(result.stdout)


def sampled_motion(path: Path, sample_fps: float, delta_threshold: float) -> tuple[float, float, int]:
    width = 96
    height = 96
    frame_size = width * height
    result = run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-i",
            str(path),
            "-an",
            "-vf",
            f"fps={sample_fps},scale={width}:{height}:flags=fast_bilinear,format=gray",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "gray",
            "-",
        ],
        binary=True,
    )
    if result.returncode:
        stderr = result.stderr.decode("utf-8", errors="replace") if result.stderr else ""
        raise RuntimeError(stderr.strip() or "video decode failed")

    data = result.stdout
    frames = len(data) // frame_size
    if frames < 2:
        return 0.0, 0.0, frames

    moving = 0
    static_run = 0
    longest_static_run = 0
    previous = data[:frame_size]
    for index in range(1, frames):
        current = data[index * frame_size : (index + 1) * frame_size]
        mean_delta = sum(abs(a - b) for a, b in zip(previous, current)) / frame_size
        if mean_delta >= delta_threshold:
            moving += 1
            static_run = 0
        else:
            static_run += 1
            longest_static_run = max(longest_static_run, static_run)
        previous = current

    comparisons = frames - 1
    return moving / comparisons, longest_static_run / sample_fps, frames


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--min-moving-ratio", type=float, default=0.90)
    parser.add_argument("--max-freeze-seconds", type=float, default=0.75)
    parser.add_argument("--max-black-seconds", type=float, default=0.25)
    parser.add_argument("--sample-fps", type=float, default=6.0)
    parser.add_argument("--delta-threshold", type=float, default=1.0)
    parser.add_argument("--expected-duration", type=float)
    parser.add_argument("--duration-tolerance", type=float, default=0.15)
    parser.add_argument("--allow-no-audio", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    video = args.video.resolve()
    if not video.is_file():
        parser.error(f"video does not exist: {video}")

    metadata = probe(video)
    streams = metadata.get("streams", [])
    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    duration = float(metadata["format"]["duration"])
    failures: list[str] = []

    if not video_streams:
        failures.append("missing video stream")
    if not audio_streams and not args.allow_no_audio:
        failures.append("missing audio stream")
    if duration <= 0:
        failures.append("duration is zero")
    if args.expected_duration is not None and abs(duration - args.expected_duration) > args.duration_tolerance:
        failures.append(
            f"duration {duration:.3f}s differs from expected {args.expected_duration:.3f}s"
        )

    moving_ratio, sampled_static_seconds, sampled_frames = sampled_motion(
        video, args.sample_fps, args.delta_threshold
    )
    if moving_ratio < args.min_moving_ratio:
        failures.append(
            f"moving-frame ratio {moving_ratio:.3f} is below {args.min_moving_ratio:.3f}"
        )

    sink = "NUL" if os.name == "nt" else "/dev/null"
    freeze_result = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(video),
            "-vf",
            f"freezedetect=n=-50dB:d={args.max_freeze_seconds}",
            "-an",
            "-f",
            "null",
            sink,
        ]
    )
    freeze_durations = [float(value) for value in FREEZE_DURATION.findall(freeze_result.stderr)]
    longest_freeze = max(freeze_durations, default=0.0)
    if longest_freeze > args.max_freeze_seconds:
        failures.append(
            f"frozen interval {longest_freeze:.3f}s exceeds {args.max_freeze_seconds:.3f}s"
        )

    black_result = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(video),
            "-vf",
            f"blackdetect=d={args.max_black_seconds}:pic_th=0.98:pix_th=0.10",
            "-an",
            "-f",
            "null",
            sink,
        ]
    )
    black_durations = [float(value) for value in BLACK_DURATION.findall(black_result.stderr)]
    longest_black = max(black_durations, default=0.0)
    if longest_black > args.max_black_seconds:
        failures.append(
            f"black interval {longest_black:.3f}s exceeds {args.max_black_seconds:.3f}s"
        )

    payload = {
        "video": str(video),
        "pass": not failures,
        "duration_seconds": duration,
        "video_streams": len(video_streams),
        "audio_streams": len(audio_streams),
        "moving_frame_ratio": round(moving_ratio, 6),
        "sampled_longest_static_seconds": round(sampled_static_seconds, 3),
        "sampled_frames": sampled_frames,
        "longest_freeze_seconds": longest_freeze,
        "longest_black_seconds": longest_black,
        "thresholds": {
            "min_moving_ratio": args.min_moving_ratio,
            "max_freeze_seconds": args.max_freeze_seconds,
            "max_black_seconds": args.max_black_seconds,
            "sample_fps": args.sample_fps,
            "delta_threshold": args.delta_threshold,
        },
        "manual_review_required": True,
        "manual_review_note": "Passing motion metrics does not prove semantic action or exclude a Ken Burns effect.",
        "failures": failures,
    }

    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
