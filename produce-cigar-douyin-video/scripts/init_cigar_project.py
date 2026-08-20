#!/usr/bin/env python3
"""Create an isolated cigar Douyin video project without overwriting work."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--project-id", required=True)
    args = parser.parse_args()

    if not PROJECT_ID.fullmatch(args.project_id):
        parser.error("--project-id must contain lowercase letters, digits, and hyphens")

    workspace = args.workspace.resolve()
    if not workspace.is_dir():
        parser.error(f"workspace does not exist: {workspace}")

    project = workspace / "projects" / args.project_id
    if project.exists():
        parser.error(f"refusing to overwrite existing project: {project}")

    skill_root = Path(__file__).resolve().parent.parent
    template_agents = skill_root / "assets" / "project-template" / "AGENTS.md"
    style_lock = skill_root / "assets" / "reference-style-lock.json"
    if not template_agents.is_file() or not style_lock.is_file():
        parser.error("skill assets are incomplete")

    directories = [
        "input/user-assets",
        "input/voice",
        "work/research",
        "work/editorial",
        "work/storyboard",
        "work/voice",
        "work/scenes",
        "work/preview",
        "work/final",
        "output",
    ]
    for relative in directories:
        (project / relative).mkdir(parents=True, exist_ok=False)

    shutil.copy2(template_agents, project / "AGENTS.md")
    shutil.copy2(style_lock, project / "input" / "reference-style-lock.json")

    now = datetime.now(timezone.utc).isoformat()
    write_json(
        project / "input" / "brief.json",
        {
            "version": 1,
            "project_id": args.project_id,
            "created_at": now,
            "platform": "douyin",
            "aspect_ratio": "9:16",
            "topic": None,
            "user_inputs": [],
            "rights_declaration": None,
            "voice": {
                "strategy": "auto",
                "preferred": "authorized_stable_clone",
                "fallback_provider": "minimax-official",
                "fallback_voice_id": "junlang_nanyou",
            },
            "music": {
                "mode": "undecided",
                "source_path": None,
                "authorization_record": None,
            },
            "character": {
                "host_face_visible": False,
                "visible_virtual_character_requested": False,
                "policy_review_required": False,
            },
        },
    )
    write_json(
        project / "work" / "job-state.json",
        {
            "version": 1,
            "project_id": args.project_id,
            "created_at": now,
            "updated_at": now,
            "state": "initialized",
            "content": {
                "status": "draft",
                "approved": False,
                "approved_at": None,
                "fingerprint": None,
            },
            "voice": {
                "strategy": None,
                "voice_id": None,
                "full_audio": None,
                "duration_seconds": None,
            },
            "music": {"mode": "undecided", "source_path": None},
            "preview": {
                "max_seconds": 15,
                "status": "not_started",
                "approved": False,
                "approved_at": None,
                "output": None,
            },
            "paid_plan": {
                "status": "not_created",
                "approved": False,
                "plan_fingerprint": None,
                "maximum_cost_cny": None,
            },
            "outputs": {"final_video": None, "publish_ready": False},
            "last_successful_state": "initialized",
            "last_error": None,
        },
    )
    write_json(
        project / "work" / "research-sources.json",
        {"version": 1, "sources": [], "claims": []},
    )
    write_json(
        project / "work" / "asset-manifest.json",
        {"version": 1, "assets": []},
    )
    write_json(
        project / "work" / "scene-plan.json",
        {"version": 1, "status": "draft", "duration_seconds": None, "scenes": []},
    )

    print(json.dumps({"created": str(project), "state": "initialized"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
