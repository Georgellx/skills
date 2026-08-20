# Render, subtitle, and QA rules

## Environment

Require:

- Node.js and npm
- FFmpeg and ffprobe for silent export and final inspection
- the generated project's pinned Remotion dependencies

Run `scripts/check-environment.mjs` before the first project on a machine.

## SRT generation

Generate SRT from `project.json`, not from a separately maintained timing file.

Verify:

- UTF-8 output
- monotonic cue numbers and times
- no overlap
- last cue ends before or at video end
- cue text contains only Chinese/English subtitle content
- no titles, labels, markdown, or production instructions

Desktop Jianying/CapCut can import SRT. If a target editor cannot, also provide the approved scene table for manual paste.

## Render sequence

From the project `remotion` folder:

```powershell
npm install
npm run render:preview
npm run render
```

Approve the preview before full render when character, crop, or pacing is unproven.

## Visual QA

Inspect at least four frames per scene:

1. blank/reset frame
2. grayscale sweep in progress
3. color sweep in progress
4. full-color hold

Confirm:

- every scene resets correctly
- grayscale and color layers use the exact same file and geometry
- mask direction and feather are stable
- no face or object jumps during color reveal
- per-scene crop preserves the intended subject and safe zones
- final frame has sufficient hold

## Technical QA

For the final MP4, verify:

- expected width, height, fps, duration, and frame count
- H.264 video stream
- no audio stream for silent handoff
- duration matches the sum of `durationSeconds` within normal frame rounding
- file opens from beginning to end

Use `scripts/validate-project.mjs project.json --video final.mp4`. If ffprobe is unavailable or returns incomplete data, state that technical QA is incomplete.

For the first-scene preview, add `--preview` so duration is checked against scene one rather than the complete project.

## Editor handoff

Tell the editor:

- import the silent MP4 without recropping it
- import the SRT and style subtitles manually
- add voice and music after visual timing is approved
- if narration overruns a scene, update `project.json` and rerender instead of speeding up the voice blindly
- listen to the complete result on a phone speaker before publishing
