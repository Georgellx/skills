# Xiaohongshu Profile Spider Runbook

Assume Windows PowerShell unless the current environment clearly differs.

## Prepare Spider_XHS

Use a local working folder chosen by the user, for example:

```powershell
Set-Location 'D:\George\自媒体\小红书'
git clone https://github.com/cv-cat/Spider_XHS
Set-Location '.\Spider_XHS'
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm ci
.\.venv\Scripts\python.exe -m pip install Pillow
.\.venv\Scripts\python.exe -c "from apis.xhs_pc_apis import XHS_Apis; from spider.spider import Data_Spider; print('ok')"
```

If Python 3.13 is unavailable, use the newest available `py -3` interpreter.

## Manual Cookie file flow

Use this when QR login expires, when QR validation succeeds but Spider_XHS still reports login info is empty, or when the user is already logged in through the browser.

Tell the user:

1. Open the Xiaohongshu profile page in Chrome.
2. Open DevTools → Network → Fetch/XHR.
3. Click a profile-data request such as `query?source=UserPage...` or `entry?user_id=...`.
4. In Headers → Request Headers, copy only the `cookie:` header value.
5. Save it locally, for example `D:\George\自媒体\小红书\xhs_cookie.txt`.

Do not ask the user to paste Cookie values into chat. Do not print the Cookie file contents. The crawler script strips a leading `cookie:` prefix if the user copied it.

## Run the crawler

Use the Codex skill script with the Spider_XHS virtualenv:

```powershell
& 'D:\George\自媒体\小红书\Spider_XHS\.venv\Scripts\python.exe' `
  'C:\Users\waiti\.codex\skills\xiaohongshu-profile-spider\scripts\crawl_profile.py' `
  --repo 'D:\George\自媒体\小红书\Spider_XHS' `
  --user-url '<FULL_PROFILE_URL>' `
  --output-dir 'D:\George\自媒体\小红书\<USER_ID>' `
  --cookie-file 'D:\George\自媒体\小红书\xhs_cookie.txt' `
  --delete-cookie-file `
  --delay 2.2
```

The script:

- fetches all note IDs from the profile URL;
- skips notes already represented by an existing `info.json`;
- downloads note details and media through Spider_XHS;
- writes `<USER_ID>.xlsx` in the output folder;
- writes `crawl_failures.jsonl` if individual notes fail;
- deletes the Cookie file only when `--delete-cookie-file` is passed.

## Monitor progress

Use file counts instead of inspecting secrets:

```powershell
$out = 'D:\George\自媒体\小红书\<USER_ID>'
Get-ChildItem -LiteralPath $out -Recurse -File |
  Group-Object Extension |
  Sort-Object Name |
  Select-Object Name,Count
Test-Path -LiteralPath (Join-Path $out '<USER_ID>.xlsx')
```

For a running process check:

```powershell
Get-CimInstance Win32_Process |
  Where-Object { ($_.Name -eq 'python.exe' -or $_.Name -eq 'pythonw.exe') -and $_.CommandLine -like '*Spider_XHS*' } |
  Select-Object ProcessId,Name,CommandLine
```

## Resume after interruption

If Excel is missing but note folders exist:

1. Ask the user to save a fresh Cookie file if the previous temporary file was deleted.
2. Rerun the same `crawl_profile.py` command.
3. The script will skip completed notes with existing `info.json` and rebuild the Excel from all collected `info.json` files.

## Common failures

- `无登录信息，或登录信息为空`: Cookie is missing, stale, copied from the wrong request, or QR login did not persist a usable session.
- QR code expired: regenerate the QR and scan again, or switch to manual Cookie file flow.
- `web_session` or `a1` missing: ask the user to copy the Cookie from a profile API request, not a static asset/tracking request.
- Many note failures but profile list succeeds: wait and rerun later with the same output folder and a fresh Cookie; do not increase request speed.
