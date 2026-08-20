from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
EDIT_DIRS = (
    "transcripts",
    "animations",
    "clips_graded",
    "downloads",
    "verify",
    "qa",
)


def copy_missing_tree(source: Path, target: Path) -> list[Path]:
    copied: list[Path] = []
    for item in source.rglob("*"):
        relative = item.relative_to(source)
        destination = target / relative
        if item.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        elif not destination.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, destination)
            copied.append(destination)
    return copied


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a talking-head edit workspace safely.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--style", choices=("white-editorial-v2",))
    args = parser.parse_args()

    workspace = args.workspace.expanduser().resolve()
    if not workspace.exists() or not workspace.is_dir():
        parser.error(f"workspace is not an existing directory: {workspace}")

    edit = workspace / "edit"
    edit.mkdir(exist_ok=True)
    for name in EDIT_DIRS:
        (edit / name).mkdir(exist_ok=True)

    project = edit / "project.md"
    if not project.exists():
        project.write_text(
            "# Talking-head video project\n\n"
            "## State\n\n"
            "- stage: analysis\n"
            "- approved strategy: none\n"
            "- approved style: none\n"
            "- approved prototype: none\n"
            "- approved preview: none\n\n"
            "## Sessions\n",
            encoding="utf-8",
        )

    copied: list[Path] = []
    if args.style:
        style_source = SKILL_DIR / "assets" / args.style
        style_target = edit / "style-system"
        copied = copy_missing_tree(style_source, style_target)

    print(f"workspace: {workspace}")
    print(f"edit directory: {edit}")
    print(f"style files copied: {len(copied)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
