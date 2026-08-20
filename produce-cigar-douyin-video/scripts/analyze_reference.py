#!/usr/bin/env python3
"""Extract reproducible technical timing metrics from a reference video."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path


PTS = re.compile(r"pts_time:([0-9.]+)")
FREEZE_DURATION = re.compile(r"freeze_duration:\s*([0-9.]+)")
MEAN_VOLUME = re.compile(r"mean_volume:\s*([-0-9.]+) dB")
MAX_VOLUME = re.compile(r"max_volume:\s*([-0-9.]+) dB")


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_rate(value: str) -> float:
    numerator, denominator = value.split("/", 1)
    return float(numerator) / float(denominator) if float(denominator) else 0.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--scene-threshold", type=float, default=0.25)
    parser.add_argument("--freeze-seconds", type=float, default=0.75)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    video = args.video.resolve()
    if not video.is_file():
        parser.error(f"video does not exist: {video}")

    probe = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size,bit_rate:stream=codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels",
            "-of",
            "json",
            str(video),
        ]
    )
    if probe.returncode:
        raise RuntimeError(probe.stderr.strip() or "ffprobe failed")
    metadata = json.loads(probe.stdout)
    video_stream = next(stream for stream in metadata["streams"] if stream["codec_type"] == "video")
    audio_stream = next((stream for stream in metadata["streams"] if stream["codec_type"] == "audio"), None)
    duration = float(metadata["format"]["duration"])
    sink = "NUL" if os.name == "nt" else "/dev/null"

    scenes = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(video),
            "-filter:v",
            f"select='gt(scene,{args.scene_threshold})',showinfo",
            "-an",
            "-f",
            "null",
            sink,
        ]
    )
    scene_times = [float(value) for value in PTS.findall(scenes.stderr)]

    freezes = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(video),
            "-vf",
            f"freezedetect=n=-50dB:d={args.freeze_seconds}",
            "-an",
            "-f",
            "null",
            sink,
        ]
    )
    freeze_durations = [float(value) for value in FREEZE_DURATION.findall(freezes.stderr)]

    volume = run(
        ["ffmpeg", "-hide_banner", "-i", str(video), "-vn", "-af", "volumedetect", "-f", "null", sink]
    )
    mean_match = MEAN_VOLUME.search(volume.stderr)
    max_match = MAX_VOLUME.search(volume.stderr)

    payload = {
        "source_path": str(video),
        "sha256": sha256(video),
        "width": int(video_stream["width"]),
        "height": int(video_stream["height"]),
        "fps": parse_rate(video_stream.get("avg_frame_rate", "0/1")),
        "duration_seconds": duration,
        "size_bytes": int(metadata["format"]["size"]),
        "video_codec": video_stream.get("codec_name"),
        "audio_codec": audio_stream.get("codec_name") if audio_stream else None,
        "scene_threshold": args.scene_threshold,
        "scene_change_count": len(scene_times),
        "average_shot_seconds": round(duration / max(1, len(scene_times) + 1), 3),
        "scene_change_seconds": scene_times,
        "freeze_threshold_seconds": args.freeze_seconds,
        "freeze_durations": freeze_durations,
        "mean_volume_db": float(mean_match.group(1)) if mean_match else None,
        "max_volume_db": float(max_match.group(1)) if max_match else None,
        "manual_analysis_required": [
            "typography and exact font selection",
            "semantic text reveal and transition behavior",
            "composition, palette, camera, and subject motion",
            "music rights and voice-to-music balance",
        ],
    }

    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
