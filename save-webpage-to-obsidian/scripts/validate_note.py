#!/usr/bin/env python3
"""Validate local image embeds in an Obsidian webpage archive."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


IMAGE_EXTENSIONS = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}

OBSIDIAN_EMBED = re.compile(r"!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
SOURCE_PROPERTY = re.compile(r"(?m)^source\s*:\s*.+$")
HEADING = re.compile(r"(?m)^#{1,6}\s+\S")


def find_vault_root(note: Path) -> Path | None:
    for parent in (note.parent, *note.parents):
        if (parent / ".obsidian").is_dir():
            return parent
    return None


def clean_markdown_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith(("http://", "https://", "data:")):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    else:
        target = re.split(r'\s+["\']', target, maxsplit=1)[0]
    return unquote(target.replace("\\", "/"))


def is_image_target(target: str) -> bool:
    return Path(target.split("#", 1)[0]).suffix.lower() in IMAGE_EXTENSIONS


def resolve_target(note: Path, vault_root: Path | None, target: str) -> Path | None:
    normalized = target.split("#", 1)[0]
    candidates = [note.parent / normalized]
    if vault_root is not None:
        candidates.append(vault_root / normalized)
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    return None


def validate(note: Path) -> tuple[dict[str, object], bool]:
    text = note.read_text(encoding="utf-8")
    vault_root = find_vault_root(note)

    targets = [unquote(value.strip()) for value in OBSIDIAN_EMBED.findall(text)]
    for raw in MARKDOWN_IMAGE.findall(text):
        target = clean_markdown_target(raw)
        if target is not None:
            targets.append(target)

    image_targets = [target for target in targets if is_image_target(target)]
    missing: list[str] = []
    resolved: list[str] = []
    for target in image_targets:
        path = resolve_target(note, vault_root, target)
        if path is None or path.stat().st_size == 0:
            missing.append(target)
        else:
            resolved.append(str(path))

    frontmatter_match = FRONTMATTER.search(text)
    has_frontmatter = frontmatter_match is not None
    has_source = bool(
        frontmatter_match and SOURCE_PROPERTY.search(frontmatter_match.group(1))
    )
    result: dict[str, object] = {
        "note": str(note.resolve()),
        "vault_root": str(vault_root.resolve()) if vault_root else None,
        "has_frontmatter": has_frontmatter,
        "has_source": has_source,
        "heading_count": len(HEADING.findall(text)),
        "image_reference_count": len(image_targets),
        "resolved_image_count": len(resolved),
        "missing_count": len(missing),
        "missing": missing,
    }
    ok = has_frontmatter and has_source and not missing
    return result, ok


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an Obsidian note produced from a webpage."
    )
    parser.add_argument("note", type=Path, help="Path to the Markdown note")
    args = parser.parse_args()

    if not args.note.is_file():
        print(json.dumps({"error": f"Note not found: {args.note}"}, ensure_ascii=False))
        return 2

    result, ok = validate(args.note)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
