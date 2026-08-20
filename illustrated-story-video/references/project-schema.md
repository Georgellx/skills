# Project schema

Use `project.json` as the single production source for canvas, reveal timing, scene duration, crop, and subtitle text. Generate Remotion timing and SRT from it.

## Schema example

```json
{
  "title": "Example story",
  "canvas": {
    "width": 1080,
    "height": 1920,
    "fps": 30,
    "background": "#f8f3e9"
  },
  "reveal": {
    "blankSeconds": 0.2,
    "grayscaleEndSeconds": 1.65,
    "colorEndSeconds": 2.85,
    "featherPercent": 10,
    "zoomEnd": 1.022
  },
  "subtitles": {
    "insetStartSeconds": 0.2,
    "insetEndSeconds": 0.1
  },
  "scenes": [
    {
      "id": "01",
      "image": "images/scene-01.png",
      "durationSeconds": 6.4,
      "imageFit": "contain",
      "imagePosition": "center center",
      "chinese": "第一幕中文字幕。",
      "english": "Natural English adaptation for scene one."
    }
  ]
}
```

## Rules

- Keep `fps`, width, height, and scene durations numeric.
- Store image paths relative to `remotion/public/`.
- Keep scene IDs unique and ordered.
- Make every scene longer than `colorEndSeconds` plus a readable full-color hold.
- Set `imagePosition` per scene; do not assume all images can use the same crop.
- Use `contain` when the generated image already includes its intended negative space. Use `cover` only when an intentional crop is approved.
- Leave `english` empty for Chinese-only delivery. Leave `chinese` empty only when an English-only project is explicitly requested.
- Change duration in this file first, then regenerate SRT and video.

## Timing policy

For manual voice editing, start with 6.4 seconds per scene or a duration justified by subtitle length. After real narration exists, use:

```text
scene duration = max(project minimum, actual narration duration + ending hold)
```

Use a 0.55-second ending hold as a starting point, then adjust by ear. Do not estimate final timing from character count when real audio is available.

## Reveal defaults

The validated hand-drawn reveal defaults are:

- blank: 0.2 seconds
- grayscale sweep: 0.2 to 1.65 seconds
- color sweep: 1.65 to 2.85 seconds
- feather: 10 percent
- scale: 1 to 1.022 over the scene

Treat these as a preset, not a universal law. Change them at project level when the reference or audience requires different pacing.
