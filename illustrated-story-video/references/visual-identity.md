# Visual identity modes

## Existing IP

Require owned or authorized references. Record immutable traits:

- silhouette and proportions
- face, hair, fur, or defining marks
- fixed clothing and accessories
- palette
- age/scale relationship
- personality shown through posture
- forbidden changes

Use the same approved reference in every relevant generation call.

## Series IP bootstrap

Use when the user intends repeated publication. Create the smallest reusable package that can stabilize generation:

1. Character brief: role, species/person type, age impression, body proportions, five immutable traits, fixed wardrobe, palette, and forbidden choices.
2. Neutral character sheet: front, three-quarter, side/back, head close-up, and three expressions on a clean background.
3. Optional companion scale comparison if two characters recur.
4. One first-scene consistency test.
5. User approval before any batch generation.

Do not spend time on logos, biographies, merchandise, or lore unless requested.

## Project character

Use for a one-off story. Create one anchor rather than a full brand system:

- one protagonist, or at most one protagonist plus one necessary companion
- fixed clothing and palette
- recognizable silhouette
- front/three-quarter reference and one expression close-up
- scene-specific age and scale relationship

Favor simple shapes and limited accessories to reduce drift.

## Characterless mode

Use when the user does not want a mascot or person. Keep continuity through at least three anchors:

- one recurring object or material
- one stable environment or paper/background system
- one palette transition
- one light direction or time-of-day progression
- one repeated compositional motif

Hands, backs, silhouettes, rooms, letters, cups, doors, plants, paper, and light can carry narrative actions. If dialogue or facial reaction is essential, explain that `project-character` will communicate it more clearly.

## Supplied images

Check:

- ownership or permission
- sufficient resolution
- compatible aspect ratio and subtitle safe zones
- stable crop across grayscale and color layers
- consistent visual style across scenes
- no embedded watermarks or unwanted text

## Prompt-ready anchor block

For every scene-image prompt, prepend a stable block:

```text
VISUAL IDENTITY
- Character/visual anchor: [approved immutable description]
- Wardrobe/props: [fixed details]
- Environment anchor: [recurring scene details]
- Style: [approved medium, line, paper, palette]
- Continuity: match the supplied anchor references exactly

COMPOSITION
- [project aspect ratio]
- reserve [top/bottom] subtitle and title safe zones
- one dominant action, clean background, readable silhouette

EXCLUDE
- text, captions, logos, watermarks
- extra characters or props
- identity, wardrobe, architecture, or style changes
```

Append only the current scene's action, emotion, camera distance, and necessary environment change.

## Image review checklist

- Identity matches the anchor.
- Action matches the approved scene event.
- Hands, face, limbs, and object interactions are usable.
- Character count and wardrobe are correct.
- Environment continuity is intact.
- Required empty space remains available.
- No generated text or watermark appears.
- The image does not try to depict two different scenes at once.
