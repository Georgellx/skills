from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_words(path: Path) -> list[dict[str, float | str]]:
    data = load_json(path)
    words = data.get("words", []) if isinstance(data, dict) else []
    result: list[dict[str, float | str]] = []
    for item in words:
        if not isinstance(item, dict) or "start" not in item or "end" not in item:
            continue
        result.append(
            {
                "start": float(item["start"]),
                "end": float(item["end"]),
                "text": str(item.get("text", "")),
            }
        )
    return sorted(result, key=lambda word: (float(word["start"]), float(word["end"])))


def find_transcript(directory: Path, source_id: str, source_path: str) -> Path | None:
    candidates = (
        directory / f"{source_id}.json",
        directory / f"{Path(source_path).stem}.json",
    )
    return next((candidate for candidate in candidates if candidate.exists()), None)


def inside_word(time_s: float, words: list[dict[str, float | str]], tolerance: float) -> str | None:
    for word in words:
        start = float(word["start"])
        end = float(word["end"])
        if start + tolerance < time_s < end - tolerance:
            return str(word["text"])
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an ordered talking-head EDL.")
    parser.add_argument("edl", type=Path)
    parser.add_argument("--transcripts-dir", type=Path)
    parser.add_argument("--tolerance-ms", type=float, default=15.0)
    parser.add_argument("--max-padding-ms", type=float, default=250.0)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    edl_path = args.edl.resolve()
    edl = load_json(edl_path)
    errors: list[str] = []
    warnings: list[str] = []

    sources = edl.get("sources") if isinstance(edl, dict) else None
    ranges = edl.get("ranges") if isinstance(edl, dict) else None
    if not isinstance(sources, dict) or not sources:
        errors.append("sources must be a non-empty object")
        sources = {}
    if not isinstance(ranges, list) or not ranges:
        errors.append("ranges must be a non-empty array")
        ranges = []

    tolerance = args.tolerance_ms / 1000.0
    max_padding = args.max_padding_ms / 1000.0
    transcript_dir = args.transcripts_dir.resolve() if args.transcripts_dir else None
    word_cache: dict[str, list[dict[str, float | str]]] = {}
    intervals_by_source: dict[str, list[tuple[float, float, int]]] = {}
    total = 0.0

    for index, item in enumerate(ranges, start=1):
        label = f"range {index}"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be an object")
            continue
        source_id = str(item.get("source", ""))
        if source_id not in sources:
            errors.append(f"{label}: unknown source {source_id!r}")
            continue
        try:
            start = float(item["start"])
            end = float(item["end"])
        except (KeyError, TypeError, ValueError):
            errors.append(f"{label}: start and end must be numbers")
            continue
        if start < 0 or end <= start:
            errors.append(f"{label}: invalid interval {start:.3f}..{end:.3f}")
            continue
        if not str(item.get("quote", "")).strip():
            warnings.append(f"{label}: quote is empty")
        if not str(item.get("beat", "")).strip():
            warnings.append(f"{label}: beat is empty")

        total += end - start
        intervals_by_source.setdefault(source_id, []).append((start, end, index))

        if transcript_dir:
            if source_id not in word_cache:
                transcript = find_transcript(transcript_dir, source_id, str(sources[source_id]))
                if transcript:
                    word_cache[source_id] = load_words(transcript)
                else:
                    word_cache[source_id] = []
                    warnings.append(f"{label}: transcript not found for {source_id}")
            words = word_cache[source_id]
            if not words:
                continue
            start_word = inside_word(start, words, tolerance)
            end_word = inside_word(end, words, tolerance)
            if start_word:
                errors.append(f"{label}: start {start:.3f}s falls inside word {start_word!r}")
            if end_word:
                errors.append(f"{label}: end {end:.3f}s falls inside word {end_word!r}")

            kept = [word for word in words if float(word["end"]) > start and float(word["start"]) < end]
            if kept:
                before = float(kept[0]["start"]) - start
                after = end - float(kept[-1]["end"])
                if before < -tolerance:
                    errors.append(f"{label}: first word begins {-before * 1000:.0f}ms before the cut")
                elif before > max_padding:
                    warnings.append(f"{label}: leading padding is {before * 1000:.0f}ms")
                if after < -tolerance:
                    errors.append(f"{label}: last word ends {-after * 1000:.0f}ms after the cut")
                elif after > max_padding:
                    warnings.append(f"{label}: trailing padding is {after * 1000:.0f}ms")
            else:
                warnings.append(f"{label}: interval contains no transcript words")

    for source_id, intervals in intervals_by_source.items():
        ordered = sorted(intervals)
        for previous, current in zip(ordered, ordered[1:]):
            if current[0] < previous[1] - tolerance:
                warnings.append(
                    f"source {source_id}: ranges {previous[2]} and {current[2]} overlap in source time"
                )

    declared = edl.get("total_duration_s") if isinstance(edl, dict) else None
    if declared is not None:
        try:
            difference = abs(float(declared) - total)
            if difference > 0.1:
                errors.append(
                    f"declared total {float(declared):.3f}s differs from range sum {total:.3f}s"
                )
        except (TypeError, ValueError):
            errors.append("total_duration_s must be numeric")

    report = {
        "edl": str(edl_path),
        "range_count": len(ranges),
        "computed_duration_s": round(total, 3),
        "errors": errors,
        "warnings": warnings,
        "passed": not errors,
    }
    if args.json_output:
        output = args.json_output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
