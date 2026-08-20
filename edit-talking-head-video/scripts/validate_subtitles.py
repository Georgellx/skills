from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


TIME_RE = re.compile(
    r"^(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s+-->\s+"
    r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})$"
)
SENTENCE_BREAK_RE = re.compile(r"[。！？!?](?=.)")


def seconds(parts: tuple[str, ...]) -> float:
    hours, minutes, secs, millis = map(int, parts)
    return hours * 3600 + minutes * 60 + secs + millis / 1000.0


def display_cells(text: str) -> int:
    return sum(2 if unicodedata.east_asian_width(char) in {"W", "F"} else 1 for char in text)


def parse_srt(path: Path) -> list[dict[str, object]]:
    normalized = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()
    cues: list[dict[str, object]] = []
    for block_number, block in enumerate(re.split(r"\n\s*\n", normalized), start=1):
        lines = [line.rstrip() for line in block.splitlines()]
        if len(lines) < 3:
            raise ValueError(f"block {block_number} has fewer than three lines")
        match = TIME_RE.match(lines[1].strip())
        if not match:
            raise ValueError(f"block {block_number} has an invalid time line: {lines[1]!r}")
        groups = match.groups()
        cues.append(
            {
                "index": lines[0].strip(),
                "start": seconds(groups[:4]),
                "end": seconds(groups[4:]),
                "lines": [line.strip() for line in lines[2:] if line.strip()],
            }
        )
    return cues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SRT timing and vertical-caption fit.")
    parser.add_argument("srt", type=Path)
    parser.add_argument("--max-cells", type=int, default=36)
    parser.add_argument("--max-cells-per-second", type=float, default=20.0)
    parser.add_argument("--allow-two-lines", action="store_true")
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    path = args.srt.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    try:
        cues = parse_srt(path)
    except (OSError, ValueError) as exc:
        cues = []
        errors.append(str(exc))

    previous_end = -1.0
    previous_text = ""
    for position, cue in enumerate(cues, start=1):
        label = f"cue {position}"
        start = float(cue["start"])
        end = float(cue["end"])
        lines = list(cue["lines"])
        text = "".join(str(line) for line in lines)
        if end <= start:
            errors.append(f"{label}: end must follow start")
            continue
        if start < previous_end - 0.001:
            errors.append(f"{label}: overlaps the previous cue by {(previous_end - start) * 1000:.0f}ms")
        if not lines:
            errors.append(f"{label}: text is empty")
        if len(lines) > (2 if args.allow_two_lines else 1):
            errors.append(f"{label}: contains {len(lines)} rendered lines")
        cells = max((display_cells(str(line)) for line in lines), default=0)
        if cells > args.max_cells:
            warnings.append(f"{label}: rendered width is approximately {cells} cells")
        duration = end - start
        rate = display_cells(text) / duration if duration else 0.0
        if duration < 0.25:
            warnings.append(f"{label}: duration is only {duration:.2f}s")
        if duration > 5.0:
            warnings.append(f"{label}: duration is {duration:.2f}s; review semantic hold")
        if rate > args.max_cells_per_second:
            warnings.append(f"{label}: reading rate is {rate:.1f} cells/s")
        if SENTENCE_BREAK_RE.search(text):
            warnings.append(f"{label}: contains a sentence-ending mark before the cue ends")
        if text and text == previous_text:
            warnings.append(f"{label}: duplicates the previous cue")
        previous_end = end
        previous_text = text

    report = {
        "srt": str(path),
        "cue_count": len(cues),
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
