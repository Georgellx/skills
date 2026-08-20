# Reference style and layout contract

## Deconstruct before designing

Inspect the reference at its opening, representative information scenes, transitions, visual climax, captions, and ending. Create contact sheets or exact-time frames and record:

- canvas, safe area, and dominant negative space;
- portrait scale, crop, alignment, and transitions between full-screen and windowed states;
- type families, size ratios, weight, line height, and label hierarchy;
- palette, surface treatment, borders, shadows, and accent usage;
- caption appearance and vertical placement;
- scene duration, entry order, easing, transition families, and climax intensity;
- reusable visual grammar versus protected identity, logos, watermarks, footage, and wording.

Translate the grammar natively to 9:16. Preserve responsibilities and hierarchy instead of mechanically scaling a horizontal layout.

## Lock the design system

Write `edit/DESIGN.md` before building motion. Define tokens for canvas, text, accents, fonts, spacing, radii, borders, shadows, portrait treatment, captions, safe areas, motion duration, easing, and transitions.

Use a small, coherent scene vocabulary. Every label must communicate real content. Let the content determine scene count and intensity.

## Confirm layouts with ASCII

Show an ASCII wireframe for every distinct scene family. Mark approximate coordinates or proportions for:

- title and supporting information;
- portrait and the protected facial/gesture region;
- topic-defining objects;
- captions;
- platform interaction safe area;
- entry and exit direction.

Example structure, not a fixed design:

```text
┌──────────────────────────┐
│ SECTION            02/05 │
│ ──────────────────────── │
│ 主标题            ┌────┐ │
│ 说明文字          │人物│ │
│                   │窗口│ │
│                   └────┘ │
│                          │
│       当前语义字幕       │
│        平台安全区        │
└──────────────────────────┘
```

## Protect spatial responsibilities

Define independent rectangles for portrait, information, captions, and platform controls. Preserve visible face, meaningful gestures, hands, and the topic object. Recalculate crop and focal point for each source setup; do not inherit a fixed crop from another video.

Use full-screen portrait for hooks, emotional statements, and direct questions. Move to a proportionate portrait window only when information needs dedicated space. Animate that change continuously when both states appear in one sequence.

## Build motion from speech

Reveal elements in the order the viewer should read them. Land the important visual state on the spoken payoff word. Use one high-intensity sequence for the central turn and keep supporting motion restrained.

Use deterministic, finite timelines with registered frame-seekable state. Prefer transform and opacity animation with non-linear easing. Hold the resolved frame long enough to read. Test motion at normal playback speed.

## Use the white-editorial asset conditionally

Use `assets/white-editorial-v2/` when the project selects the bundled baseline. Treat it as a structural template: replace content, portrait media, timings, and focal points. Keep its editorial whitespace, fine rules, black hierarchy, limited yellow marker, semantic metadata, and portrait-safe composition unless the user approves a variation.
