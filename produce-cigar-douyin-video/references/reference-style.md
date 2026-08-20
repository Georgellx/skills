# Locked Reference Style

## Source analysis

The approved style was derived from the local reference video whose SHA-256 is `363d59b4015a7904486692ab33adc410961093c21318ae973ec84833551a415a`.

- Source: 1920×1080, 30 fps, 221.267 seconds, full-frame 16:9.
- Strong scene changes detected: 71 at a `0.25` scene threshold; overall average is about 3.1 seconds per shot.
- Opening scene changes: approximately 2.833, 5.100, 9.000, 11.000, 13.367, and 14.433 seconds.
- The first 15 seconds therefore use about seven shots and average about 2.1 seconds per shot.
- Visual language: realistic documentary footage, active cigar production and inspection, macro texture, shallow depth of field, warm brown/black neutrals, practical light, and restrained contrast.

Use `assets/reference-style-lock.json` as the machine-readable source of truth.

## Native vertical reconstruction

Recreate the style natively at 1080×1920 and 30 fps. Never center-crop the 16:9 reference. Stage people, hands, props, and negative space for vertical composition so typography remains readable and no subject is cut off.

Preserve the reference's grammar rather than its copyrighted expression:

- match shot rhythm, camera language, color relationships, typography hierarchy, text motion, subtitle modes, and transition behavior;
- do not reuse its footage, people, text, logos, or audio without documented permission;
- do not source visually similar clips from social creators.

## Realism gate

All production scenes default to photorealistic live-action-style video. Cartoons, illustrations, vector graphics, flat graphics, diagrams, schematic cutaways, infographics, icon animations, and explanatory motion-graphic pages fail the style gate even when their meaning and motion metrics are correct. Use realistic hands, cigar macro details, hygrometers, humidors, transport containers, changing practical light, focus shifts, and environmental movement to explain abstract concepts. A non-realistic visual is allowed only after the user explicitly requests and approves that exception.

## Opening 15-second grammar

Use these beats unless the approved narration has a shorter total duration:

1. `0.000–2.833`: moving close-up or work action; build the hook in semantic chunks.
2. `2.833–5.100`: use a short distressed/glitch replacement into the second proposition; keep the background action continuous.
3. `5.100–9.000`: change location or scale; reveal the channel promise or core answer in two to four chunks.
4. `9.000–11.000`: switch from central headline to cinematic detail and one-line lower subtitle.
5. `11.000–13.367`: use a different cigar or hand action with a direct or match-action cut.
6. `13.367–15.000`: close on a tactile hero detail, tool action, gauge, leaf, humidor, or environmental movement.

Do not force title words onto these exact beats when the narration meaning disagrees. Preserve the beat density and hierarchy while aligning text to spoken meaning.

## Typography

Use these decisions:

- Main kinetic headline: `Microsoft YaHei`, then `Microsoft YaHei UI` fallback; weight 900; compact line height; white base.
- Numeric emphasis: warm yellow and approximately 1.30–1.45 times the surrounding character size.
- Semantic warning or contrast word: deep red.
- Lower narration subtitle: `SimSun`, then `Songti SC` or `Noto Serif CJK SC`; white with a dark stroke and soft shadow.
- Health notice: the same serif family as the lower subtitle, smaller and quieter.

For 1080×1920 output, start with:

- headline: 96–132 px, maximum two deliberately composed lines;
- enlarged number: 132–178 px;
- lower subtitle: 46–54 px, one line only;
- health notice: 22–28 px, top-right within the safe area.

Lower narration subtitles use a transparent background by default. Do not place them on opaque or translucent black rectangles, pills, or cards unless the user explicitly approves that exception. Use only the declared dark stroke and soft shadow for separation from the picture.

Never auto-wrap a lower subtitle. Shorten the spoken-caption page or split it at an aligned natural pause. A designed central headline may use two lines. Ordinary subtitles must reproduce the currently spoken words; do not replace them with editorial paraphrases.

## Headline motion

Do not use karaoke highlighting as the main title behavior. Animate semantic chunks:

- reveal one phrase or key unit every 0.25–0.50 seconds;
- enter over 2–4 frames with opacity, a subtle 106–110% to 100% scale settle, and no elastic bounce;
- keep previously revealed chunks visible until the complete proposition lands;
- color the keyword or number from its first visible frame rather than changing it later;
- hold a complete statement for roughly 0.8–1.6 seconds when speech permits;
- use a 6–10-frame distressed breakup or horizontal glitch only at selected opening proposition changes, not on every cut;
- remove the outgoing headline before the lower narration subtitle appears.

When a central headline is on screen, do not show a duplicate lower subtitle. The headline may condense only the meaning being spoken at that moment. After the opening title section, use the lower subtitle alone except for occasional short keyword cards.

## Layout and color

- Keep the health notice persistently near the upper-right safe area.
- Place opening headlines through the middle 55% of the vertical canvas; favor left-center alignment for long phrases and centered alignment for short declarations.
- Place lower subtitles above the Douyin control-safe zone, around 78–83% of canvas height.
- Reserve right-side interaction space and the lower caption/navigation zone.
- Use warm near-white, yellow `#f6d000`, deep red `#b20b18`, tobacco brown, charcoal black, and muted cream.

## Transitions and sound

Favor direct cuts, action matches, scale changes, and occasional short dissolves. Reserve the distressed/glitch transition for opening headline changes. Do not use slideshow swipes, card flips, template zoom transitions, or decorative particle wipes.

Do not include background music unless the user supplies a file and permission. When supplied, keep narration dominant, duck music under speech, and limit the final master safely instead of copying the reference's 0 dB peak.
