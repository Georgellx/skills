---
name: xiaohongshu-profile-spider
description: "Install and run cv-cat/Spider_XHS for Xiaohongshu/XHS/小红书 user profile crawls. Use when the user asks to download/crawl a Xiaohongshu user homepage, save note media and Excel locally, resume an interrupted Spider_XHS crawl, or handle the QR/Cookie login workflow safely."
---

# Xiaohongshu Profile Spider

## Overview

Use this skill to turn a Xiaohongshu user profile URL into a local archive of note details, images/videos, and an Excel summary via `cv-cat/Spider_XHS`.

This skill is for profile/user-homepage crawling only. Do not mix it with Xiaohongshu video-production or content-planning workflows.

## Ground rules

- Confirm or infer three inputs before running: the full profile URL, the local save folder, and whether the user wants media, Excel, or both.
- Use this only for pages the user is authorized to access. Do not bypass access controls, CAPTCHAs, or rate limits.
- Keep crawl speed conservative: default to at least `2.2` seconds between note detail requests.
- Never ask the user to paste Cookie values into chat. Ask them to save the request Cookie into a local temporary file, then read it without printing it.
- Do not inspect Chrome cookies, local storage, or browser secrets programmatically. If manual Cookie capture is needed, guide the user through DevTools.
- Delete temporary Cookie files after the run when they are no longer needed.

## Workflow

1. Prepare `Spider_XHS`.
   - If the repo is missing, clone `https://github.com/cv-cat/Spider_XHS`.
   - Create/use `.venv`, install `requirements.txt`, run `npm ci`, and verify Python can import `XHS_Apis` and `Data_Spider`.

2. Get authenticated access.
   - Try the project QR login if appropriate.
   - If QR expires or the project reports success but later says login is empty, switch to the manual Cookie-file flow.
   - In DevTools, the useful request is usually `query?source=UserPage...` or `entry?user_id=...`, not tracking calls like `pj` or `collect`.

3. Run the bundled crawler script.
   - Use `scripts/crawl_profile.py` so interrupted runs can resume by skipping note folders that already contain `info.json`.
   - Pass `--delete-cookie-file` only for a temporary file created for this run.

4. Monitor and verify.
   - Count `info.json` files for completed notes.
   - Count media files by extension.
   - Verify the final `.xlsx` exists.
   - If the run stops before Excel is created and the Cookie file was deleted, ask the user to save a fresh Cookie file and rerun; existing completed notes will be skipped.

5. Hand off the result.
   - Report the output folder, completed note count, media count, Excel path, and whether the temporary Cookie file was removed.
   - Do not include Cookie values or request headers in the response.

## Resources

- Read `references/runbook.md` when executing the full workflow, troubleshooting login, or resuming a crawl.
- Use `scripts/crawl_profile.py` to perform the actual profile crawl and Excel export.

Create only the resource directories this skill actually needs. Delete this section if no resources are required.

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Codex for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Codex's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Codex should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Codex produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Not every skill requires all three types of resources.**
