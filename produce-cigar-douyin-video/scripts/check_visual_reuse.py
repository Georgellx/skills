#!/usr/bin/env python3
"""Validate full-timeline source continuity and shot-reuse evidence."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
REQUIRED_MANUAL_EVIDENCE = {
    "normal_speed_full_video",
    "scene_boundary_contact_sheet",
    "non_adjacent_scene_comparison",
}


def _number(interval: dict[str, Any], key: str, failures: list[str]) -> float | None:
    value = interval.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        failures.append(f"{interval.get('scene_id', '<unknown>')}: {key} must be numeric")
        return None
    return float(value)


def _approved_reuse_exception(interval: dict[str, Any]) -> bool:
    exception = interval.get("reuse_exception")
    return bool(
        isinstance(exception, dict)
        and exception.get("approved") is True
        and str(exception.get("approval_ref") or "").strip()
        and str(exception.get("reason") or "").strip()
    )


def validate_audit(payload: dict[str, Any], *, require_manual_pass: bool = False) -> list[str]:
    failures: list[str] = []
    intervals = payload.get("intervals")
    if not isinstance(intervals, list) or not intervals:
        return ["intervals must be a non-empty list"]

    allowed_overlap = float(payload.get("allowed_transition_overlap_seconds", 0.20))
    tolerance = 0.002
    normalized: list[dict[str, Any]] = []
    for index, interval in enumerate(intervals):
        if not isinstance(interval, dict):
            failures.append(f"interval[{index}] must be an object")
            continue
        scene_id = str(interval.get("scene_id") or "").strip()
        lineage = str(interval.get("source_lineage_id") or "").strip()
        shot_signature = str(interval.get("shot_signature") or "").strip()
        start_hash = str(interval.get("rendered_start_frame_sha256") or "").strip()
        if not scene_id:
            failures.append(f"interval[{index}]: scene_id is required")
        if not lineage:
            failures.append(f"{scene_id or f'interval[{index}]'}: source_lineage_id is required")
        if not shot_signature:
            failures.append(f"{scene_id or f'interval[{index}]'}: shot_signature is required")
        if not SHA256.fullmatch(start_hash):
            failures.append(
                f"{scene_id or f'interval[{index}]'}: rendered_start_frame_sha256 must be SHA-256"
            )
        timeline_start = _number(interval, "timeline_start_seconds", failures)
        timeline_end = _number(interval, "timeline_end_seconds", failures)
        source_start = _number(interval, "source_start_seconds", failures)
        source_end = _number(interval, "source_end_seconds", failures)
        if None in (timeline_start, timeline_end, source_start, source_end):
            continue
        if timeline_end <= timeline_start:
            failures.append(f"{scene_id}: timeline range must move forward")
        if source_end <= source_start:
            failures.append(f"{scene_id}: source range must move forward")
        normalized.append(
            {
                **interval,
                "scene_id": scene_id,
                "source_lineage_id": lineage,
                "shot_signature": shot_signature,
                "rendered_start_frame_sha256": start_hash.lower(),
                "timeline_start_seconds": timeline_start,
                "timeline_end_seconds": timeline_end,
                "source_start_seconds": source_start,
                "source_end_seconds": source_end,
            }
        )

    normalized.sort(key=lambda item: item["timeline_start_seconds"])
    for previous, current in zip(normalized, normalized[1:]):
        gap = current["timeline_start_seconds"] - previous["timeline_end_seconds"]
        if abs(gap) > tolerance:
            failures.append(
                f"timeline is not contiguous between {previous['scene_id']} and {current['scene_id']}"
            )

    for left_index, left in enumerate(normalized):
        for right_index in range(left_index + 1, len(normalized)):
            right = normalized[right_index]
            adjacent = right_index == left_index + 1
            same_lineage = left["source_lineage_id"] == right["source_lineage_id"]
            same_continuation = bool(
                adjacent
                and left.get("continuation_group_id")
                and left.get("continuation_group_id") == right.get("continuation_group_id")
            )

            if left["rendered_start_frame_sha256"] == right["rendered_start_frame_sha256"]:
                failures.append(
                    f"{left['scene_id']} and {right['scene_id']} reuse the same rendered start frame"
                )

            if left["shot_signature"] == right["shot_signature"] and not same_continuation:
                failures.append(
                    f"{left['scene_id']} and {right['scene_id']} repeat the same shot signature"
                )

            if not same_lineage:
                continue
            if same_continuation:
                source_delta = right["source_start_seconds"] - left["source_end_seconds"]
                if source_delta < -allowed_overlap - tolerance:
                    failures.append(
                        f"{right['scene_id']} restarts or overlaps an already consumed source range"
                    )
                elif source_delta > tolerance:
                    failures.append(
                        f"{right['scene_id']} does not resume at the prior source cursor"
                    )
                continue
            if not (_approved_reuse_exception(left) and _approved_reuse_exception(right)):
                failures.append(
                    f"{left['scene_id']} and {right['scene_id']} reuse one source lineage without approved evidence"
                )

    if require_manual_pass:
        review = payload.get("manual_review")
        if not isinstance(review, dict) or review.get("status") != "pass":
            failures.append("manual_review.status must be pass")
        else:
            if not str(review.get("reviewer") or "").strip():
                failures.append("manual_review.reviewer is required")
            evidence = set(review.get("evidence") or [])
            missing = sorted(REQUIRED_MANUAL_EVIDENCE - evidence)
            if missing:
                failures.append(f"manual review evidence is missing: {', '.join(missing)}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit", type=Path)
    parser.add_argument("--require-manual-pass", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.audit.read_text(encoding="utf-8"))
    failures = validate_audit(payload, require_manual_pass=args.require_manual_pass)
    result = {
        "audit": str(args.audit.resolve()),
        "pass": not failures,
        "interval_count": len(payload.get("intervals") or []),
        "manual_review_required": not args.require_manual_pass,
        "failures": failures,
    }
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
