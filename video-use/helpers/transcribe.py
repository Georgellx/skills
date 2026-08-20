"""Transcribe a video with Doubao Speech ASR.

Extracts mono 16kHz MP3 audio via ffmpeg, sends it to Doubao's BigModel
recording recognition turbo endpoint, and writes a normalized word-level
transcript to <edit_dir>/transcripts/<video_stem>.json.

Cached: if the output file already exists, the API call is skipped.

Usage:
    python helpers/transcribe.py <video_path>
    python helpers/transcribe.py <video_path> --edit-dir /custom/edit
    python helpers/transcribe.py <video_path> --language en-US
    python helpers/transcribe.py --check-key
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path
from typing import Any

import requests


DOUBAO_ASR_URL = "https://openspeech.bytedance.com/api/v3/auc/bigmodel/recognize/flash"
DOUBAO_RESOURCE_ID = "volc.bigasr.auc_turbo"
DOUBAO_SUCCESS_CODE = "20000000"
MAX_AUDIO_BYTES = 100 * 1024 * 1024


def load_api_key() -> str:
    for candidate in [Path(__file__).resolve().parent.parent / ".env", Path(".env")]:
        if candidate.exists():
            for line in candidate.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                if key.strip() == "DOUBAO_API_KEY":
                    value = value.strip().strip('"').strip("'")
                    if value:
                        return value
    value = os.environ.get("DOUBAO_API_KEY", "")
    if not value:
        sys.exit("DOUBAO_API_KEY not found in .env or environment")
    return value


def extract_audio(video_path: Path, dest: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-i", str(video_path),
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "libmp3lame", "-b:a", "48k",
        str(dest),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def _request_headers(api_key: str) -> dict[str, str]:
    return {
        "X-Api-Key": api_key,
        "X-Api-Resource-Id": DOUBAO_RESOURCE_ID,
        "X-Api-Request-Id": str(uuid.uuid4()),
        "X-Api-Sequence": "-1",
    }


def _parse_additions(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return {}
        if isinstance(parsed, dict):
            return parsed
    return {}


def _speaker_id(utterance: dict[str, Any]) -> str | None:
    additions = _parse_additions(utterance.get("additions"))
    speaker = utterance.get("speaker_id")
    if speaker is None:
        speaker = utterance.get("speaker")
    if speaker is None:
        speaker = additions.get("speaker_id")
    if speaker is None:
        speaker = additions.get("speaker")
    if speaker is None or str(speaker).strip() == "":
        return None
    speaker = str(speaker).strip()
    return speaker if speaker.startswith("speaker_") else f"speaker_{speaker}"


def _milliseconds_to_seconds(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return round(float(value) / 1000.0, 3)
    except (TypeError, ValueError):
        return None


def normalize_doubao_response(payload: dict[str, Any]) -> dict[str, Any]:
    """Convert Doubao's nested millisecond response to video-use's word schema."""
    result = payload.get("result")
    if not isinstance(result, dict):
        raise ValueError("Doubao ASR response is missing result")

    utterances = result.get("utterances") or []
    if not isinstance(utterances, list):
        raise ValueError("Doubao ASR response has invalid utterances")

    normalized_words: list[dict[str, Any]] = []
    utterances_without_words: list[str] = []

    for utterance in utterances:
        if not isinstance(utterance, dict):
            continue
        speaker = _speaker_id(utterance)
        words = utterance.get("words") or []
        if not isinstance(words, list):
            words = []

        kept_word = False
        for word in words:
            if not isinstance(word, dict):
                continue
            text = str(word.get("text") or "")
            start = _milliseconds_to_seconds(word.get("start_time"))
            end = _milliseconds_to_seconds(word.get("end_time"))
            if not text or start is None or end is None:
                continue
            item: dict[str, Any] = {
                "type": "word",
                "text": text,
                "start": start,
                "end": end,
                "speaker_id": speaker,
            }
            if word.get("confidence") is not None:
                item["confidence"] = word["confidence"]
            normalized_words.append(item)
            kept_word = True

        utterance_text = str(utterance.get("text") or "").strip()
        if utterance_text and not kept_word:
            utterances_without_words.append(utterance_text)

    full_text = str(result.get("text") or "")
    if utterances_without_words:
        raise ValueError(
            "Doubao ASR returned speech without word timestamps: "
            + " | ".join(utterances_without_words[:3])
        )
    if full_text and not normalized_words:
        raise ValueError("Doubao ASR returned text without word timestamps")

    audio_info = payload.get("audio_info")
    duration_ms = audio_info.get("duration") if isinstance(audio_info, dict) else None
    return {
        "provider": "doubao",
        "text": full_text,
        "words": normalized_words,
        "metadata": {
            "resource_id": DOUBAO_RESOURCE_ID,
            "audio_duration": _milliseconds_to_seconds(duration_ms),
        },
    }


def _raise_for_response(response: requests.Response) -> None:
    code = response.headers.get("X-Api-Status-Code", "")
    if response.status_code == 200 and code == DOUBAO_SUCCESS_CODE:
        return
    message = response.headers.get("X-Api-Message", "unknown error")
    log_id = response.headers.get("X-Tt-Logid", "unavailable")
    raise RuntimeError(
        f"Doubao ASR failed (HTTP {response.status_code}, code {code or 'missing'}, "
        f"message {message}, log_id {log_id})"
    )


def call_doubao(
    audio_path: Path,
    api_key: str,
    language: str | None = None,
    num_speakers: int | None = None,
) -> dict[str, Any]:
    del num_speakers  # Doubao auto-detects speakers; retained for CLI compatibility.
    size_bytes = audio_path.stat().st_size
    if size_bytes > MAX_AUDIO_BYTES:
        raise ValueError("Extracted audio exceeds Doubao's 100 MB request limit")

    request_options: dict[str, Any] = {
        "model_name": "bigmodel",
        "enable_itn": False,
        "enable_punc": True,
        "enable_ddc": False,
        "enable_speaker_info": True,
    }
    if language:
        request_options["language"] = language

    body = {
        "user": {"uid": "video-use"},
        "audio": {"data": base64.b64encode(audio_path.read_bytes()).decode("ascii")},
        "request": request_options,
    }
    response = requests.post(
        DOUBAO_ASR_URL,
        headers=_request_headers(api_key),
        json=body,
        timeout=1800,
    )
    _raise_for_response(response)
    try:
        payload = response.json()
    except requests.JSONDecodeError as exc:
        raise RuntimeError("Doubao ASR returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("Doubao ASR returned an invalid response body")
    return normalize_doubao_response(payload)


def check_api_key(api_key: str) -> tuple[bool, str]:
    """Validate routing/auth with a zero-frame WAV that consumes no audio quota."""
    empty_wav = bytes.fromhex(
        "524946462400000057415645666d74201000000001000100803e0000007d0000"
        "020010006461746100000000"
    )
    response = requests.post(
        DOUBAO_ASR_URL,
        headers=_request_headers(api_key),
        json={
            "user": {"uid": "video-use-key-check"},
            "audio": {"data": base64.b64encode(empty_wav).decode("ascii")},
            "request": {"model_name": "bigmodel"},
        },
        timeout=30,
    )
    code = response.headers.get("X-Api-Status-Code", "")
    message = response.headers.get("X-Api-Message", "unknown response")
    expected_empty_audio = code == "45000000" and "empty audio" in message.lower()
    if response.status_code == 200 and (
        code in {"45000001", "45000002", "20000003"} or expected_empty_audio
    ):
        return True, f"Doubao API key accepted (expected empty-audio response {code})"
    return False, (
        f"Doubao API key check failed (HTTP {response.status_code}, "
        f"code {code or 'missing'}, message {message})"
    )


def transcribe_one(
    video: Path,
    edit_dir: Path,
    api_key: str,
    language: str | None = None,
    num_speakers: int | None = None,
    verbose: bool = True,
) -> Path:
    """Transcribe a single video and return its cached transcript path."""
    transcripts_dir = edit_dir / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    out_path = transcripts_dir / f"{video.stem}.json"

    if out_path.exists():
        if verbose:
            print(f"cached: {out_path.name}")
        return out_path

    if verbose:
        print(f"  extracting audio from {video.name}", flush=True)

    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        audio = Path(tmp) / f"{video.stem}.mp3"
        extract_audio(video, audio)
        size_mb = audio.stat().st_size / (1024 * 1024)
        if verbose:
            print(f"  sending {video.stem}.mp3 ({size_mb:.1f} MB)", flush=True)
        payload = call_doubao(audio, api_key, language, num_speakers)

    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    elapsed = time.time() - t0

    if verbose:
        kb = out_path.stat().st_size / 1024
        print(f"  saved: {out_path.name} ({kb:.1f} KB) in {elapsed:.1f}s")
        print(f"    words: {len(payload['words'])}")

    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description="Transcribe a video with Doubao Speech ASR")
    ap.add_argument("video", nargs="?", type=Path, help="Path to video file")
    ap.add_argument(
        "--edit-dir",
        type=Path,
        default=None,
        help="Edit output directory (default: <video_parent>/edit)",
    )
    ap.add_argument(
        "--language",
        type=str,
        default=None,
        help="Optional language code (e.g., 'en-US'). Omit to auto-detect.",
    )
    ap.add_argument(
        "--num-speakers",
        type=int,
        default=None,
        help="Compatibility option; Doubao auto-detects the speaker count.",
    )
    ap.add_argument(
        "--check-key",
        action="store_true",
        help="Validate the configured key without transcribing audio.",
    )
    args = ap.parse_args()

    api_key = load_api_key()
    if args.check_key:
        ok, message = check_api_key(api_key)
        print(message)
        if not ok:
            sys.exit(1)
        return

    if args.video is None:
        ap.error("video is required unless --check-key is used")
    video = args.video.resolve()
    if not video.exists():
        sys.exit(f"video not found: {video}")

    edit_dir = (args.edit_dir or (video.parent / "edit")).resolve()
    transcribe_one(
        video=video,
        edit_dir=edit_dir,
        api_key=api_key,
        language=args.language,
        num_speakers=args.num_speakers,
    )


if __name__ == "__main__":
    main()
