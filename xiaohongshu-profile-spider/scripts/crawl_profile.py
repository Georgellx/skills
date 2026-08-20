#!/usr/bin/env python
"""Resume-safe Xiaohongshu profile crawler for cv-cat/Spider_XHS."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl a Xiaohongshu user profile with Spider_XHS.")
    parser.add_argument("--repo", required=True, help="Path to the local Spider_XHS repository.")
    parser.add_argument("--user-url", required=True, help="Full Xiaohongshu user profile URL.")
    parser.add_argument("--output-dir", required=True, help="Folder where note folders and Excel will be saved.")
    parser.add_argument("--cookie-file", help="Local text file containing the Cookie header value.")
    parser.add_argument("--cookie-env", default="XHS_COOKIE", help="Environment variable fallback for Cookie text.")
    parser.add_argument("--delay", type=float, default=2.2, help="Seconds to wait between note detail requests.")
    parser.add_argument("--save-choice", default="all", choices=["all", "media", "media-image", "media-video", "excel"], help="Spider_XHS media/export mode.")
    parser.add_argument("--delete-cookie-file", action="store_true", help="Delete --cookie-file after the script reads it.")
    parser.add_argument("--limit", type=int, default=0, help="Optional max notes to process; 0 means all.")
    return parser.parse_args()


def user_id_from_url(user_url: str) -> str:
    parsed = urlparse(user_url)
    user_id = parsed.path.rstrip("/").split("/")[-1]
    if not user_id:
        raise ValueError("Could not infer user_id from --user-url.")
    return user_id


def read_cookie(args: argparse.Namespace) -> str:
    cookie_text = ""
    if args.cookie_file:
        cookie_path = Path(args.cookie_file)
        if not cookie_path.exists():
            raise FileNotFoundError(f"Cookie file does not exist: {cookie_path}")
        cookie_text = cookie_path.read_text(encoding="utf-8-sig").strip()
    if not cookie_text:
        cookie_text = os.environ.get(args.cookie_env, "").strip()
    if cookie_text.lower().startswith("cookie:"):
        cookie_text = cookie_text.split(":", 1)[1].strip()
    if not cookie_text:
        raise ValueError("Cookie is empty. Save it to --cookie-file or set the cookie environment variable.")
    missing = [name for name in ("a1=", "web_session=") if name not in cookie_text]
    if missing:
        print(f"Warning: Cookie does not appear to contain {', '.join(missing)}; login may fail.", flush=True)
    return cookie_text


def delete_cookie_file(args: argparse.Namespace) -> None:
    if not args.delete_cookie_file or not args.cookie_file:
        return
    cookie_path = Path(args.cookie_file)
    try:
        cookie_path.unlink(missing_ok=True)
        print(f"Deleted temporary Cookie file: {cookie_path}", flush=True)
    except Exception as exc:
        print(f"Warning: could not delete temporary Cookie file: {exc}", flush=True)


def load_existing_details(output_dir: Path) -> dict[str, dict]:
    details: dict[str, dict] = {}
    for info_path in output_dir.rglob("info.json"):
        try:
            text = info_path.read_text(encoding="utf-8").strip()
            if not text:
                continue
            data = json.loads(text.splitlines()[0])
            note_id = str(data.get("note_id") or "")
            if note_id:
                details[note_id] = data
        except Exception as exc:
            print(f"Warning: skipped unreadable info.json: {info_path} ({exc})", flush=True)
    return details


def note_url_from_summary(note: dict) -> tuple[str, str]:
    note_id = str(note.get("note_id") or note.get("id") or "")
    xsec_token = str(note.get("xsec_token") or "")
    if not note_id:
        raise ValueError(f"Profile note item is missing note_id: {note}")
    return note_id, f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}"


def write_failure(output_dir: Path, payload: dict) -> None:
    failure_path = output_dir / "crawl_failures.jsonl"
    with failure_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if not repo.exists():
        raise FileNotFoundError(f"Spider_XHS repository not found: {repo}")
    sys.path.insert(0, str(repo))

    cookie = read_cookie(args)
    delete_cookie_file(args)

    from apis.xhs_pc_apis import XHS_Apis
    from spider.spider import Data_Spider
    from xhs_utils.data_util import download_note, save_to_xlsx

    user_id = user_id_from_url(args.user_url)
    excel_path = output_dir / f"{user_id}.xlsx"

    existing = load_existing_details(output_dir)
    print(f"Existing completed notes: {len(existing)}", flush=True)

    api = XHS_Apis()
    success, msg, all_notes = api.get_user_all_notes(args.user_url, cookie)
    if not success:
        raise RuntimeError(f"Could not fetch profile note list: {msg}")
    if args.limit > 0:
        all_notes = all_notes[: args.limit]
    print(f"Profile notes found: {len(all_notes)}", flush=True)

    spider = Data_Spider()
    processed = 0
    failed = 0

    for index, summary in enumerate(all_notes, start=1):
        try:
            note_id, note_url = note_url_from_summary(summary)
            if note_id in existing:
                print(f"[{index}/{len(all_notes)}] skip existing {note_id}", flush=True)
                continue

            success, msg, note_info = spider.spider_note(note_url, cookie)
            if not success or not note_info:
                failed += 1
                write_failure(output_dir, {"note_id": note_id, "note_url": note_url, "message": str(msg)})
                print(f"[{index}/{len(all_notes)}] failed {note_id}: {msg}", flush=True)
            else:
                if args.save_choice in ("all", "media", "media-image", "media-video"):
                    download_note(note_info, str(output_dir), args.save_choice)
                existing[str(note_info["note_id"])] = note_info
                processed += 1
                print(f"[{index}/{len(all_notes)}] saved {note_id}", flush=True)
        except Exception as exc:
            failed += 1
            write_failure(output_dir, {"summary": summary, "message": str(exc)})
            print(f"[{index}/{len(all_notes)}] failed: {exc}", flush=True)
        finally:
            if index < len(all_notes) and args.delay > 0:
                time.sleep(args.delay)

    final_details = list(existing.values())
    if args.save_choice in ("all", "excel") and final_details:
        save_to_xlsx(final_details, str(excel_path))
        print(f"Excel saved: {excel_path}", flush=True)
    print(f"Done. New notes: {processed}; total completed: {len(final_details)}; failures: {failed}", flush=True)
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
