---
name: design-md-first-ui
description: Drives a design-first, taste-aware UI workflow for Codex. Use when building, redesigning, polishing, or de-AI-flavoring a webpage, personal site, portfolio, landing page, product page, app screen, or frontend interface where visual quality matters. Triggers include DESIGN.md, reference-based UI, taste-skill workflows, image-to-code, imagegen frontend concepts, high-end animated websites, visual critique, ugly UI fixes, screenshot diagnosis, and cases where Codex must audit tools and design quality before coding.
---

# Design.md First UI

Use this skill to prevent UI work from becoming a generic template or a technically working but visually weak page. The workflow is: audit the method and tools, turn intent and references into `DESIGN.md`, confirm or infer the direction responsibly, implement, visually inspect, diagnose mismatches, and fix before final delivery.

## Non-Negotiable Rule

Do not treat "it runs" as "it is good." For UI work, completion requires visual evidence and an explicit quality pass.

Before coding, identify:

1. What the user wants the page to express.
2. What visual style or reference system should guide the page.
3. Which hard parts are easy to skip: taste, assets, motion, tool dependencies, mobile polish, and ugly-output recovery.
4. What evidence will prove the result is good enough.

If the user already confirmed a design direction, proceed without asking again, but still run the self-critique and visual verification gates before final response.

## Source Method Capture

When the user asks to learn from an article, screenshot, workflow, or expert method, capture the whole method before extracting the easy part.

Create a method map in `DESIGN.md` or working notes:

| Source method item | Easy visible step | Hard dependency | Required tool/skill | Verification gate | Fallback if missing |
| --- | --- | --- | --- | --- | --- |

Rules:

- Do not reduce a method to "write DESIGN.md first" if the method also includes taste checks, subskills, screenshot critique, asset generation, or repair loops.
- Treat named tools and skills as dependencies to verify, not background flavor.
- Treat failure-recovery steps as part of the method, not optional afterthoughts.
- If a method includes "when it looks bad, do X", encode that X as a required workflow gate.

## Dependency And Skill Audit

When the user mentions a method, article, tool, plugin, or skill family, audit dependencies before claiming to use them.

Required steps:

1. Extract every named external tool or skill from the source method.
2. Check whether it is actually available in the current Codex context or local skill folders.
3. If available, read the relevant `SKILL.md` before using it.
4. If missing, say it is missing and choose one:
   - ask whether to install it when installation is part of the user's goal;
   - continue with an explicit fallback and name what quality may be lost;
   - use a local alternative skill only after saying it is a substitute.
5. Never imply that a missing skill was used.

Record dependency evidence:

| Candidate tool/skill | Purpose | Available? | Path or source checked | Action taken | Quality risk |
| --- | --- | --- | --- | --- | --- |

### Subskill Invocation Protocol

For every candidate subskill:

1. Verify availability in the current skill list and local folders.
2. Announce the skill and purpose in one short line, for example: `Using frontend-design to rebuild the animated interface.`
3. Read the full `SKILL.md`; if it references required relative files, read those too.
4. Apply its workflow, not just its name.
5. If absent, record it as missing and choose a fallback before coding.

Prefer local substitutes when taste-skill subskills are absent:

- `frontend-design`: visual build quality, distinctive composition, motion, and anti-template execution.
- `imagegen`: bitmap concepts or assets when visual assets are the bottleneck.
- `web-design-guidelines`: review against interface quality and accessibility rules.
- Browser control: rendered screenshots, desktop/mobile checks, console checks, and motion verification.

For taste-skill style methods, route like this when the corresponding skills exist:

- `design-taste-frontend`: ordinary webpage polish or de-AI-flavoring.
- `image-to-code`: user supplies a reference screenshot or image and wants a page from it.
- `imagegen-frontend-web`: no reference exists and a visual direction mockup is needed first.
- `imagegen-frontend-mobile`: mobile app screen or mobile-first interface.
- `brandkit`: brand visual board, color, type, and identity direction.
- `redesign-existing-projects`: improving an existing project.
- `minimalist-ui`: intentionally minimal visual direction.
- `gpt-taste` or `high-end-visual-design`: strong visual impact and motion-heavy work.

If these skills are absent, document that absence in the working notes or final summary and compensate with stricter `DESIGN.md`, screenshot diagnosis, and manual visual critique.

## Core Workflow

Default sequence for taste-sensitive UI:

1. **Method audit**: cover the user's source method, references, named tools, failure-recovery flow, and success criteria.
2. **Design brief**: draft or update `DESIGN.md` in concrete language.
3. **Confirmation gate**: stop for user confirmation unless the user explicitly says to proceed or the turn objective already authorizes implementation.
4. **Implementation**: build with the relevant frontend/design skills and current project conventions.
5. **Visual inspection**: open the page, take screenshots, check desktop and mobile.
6. **Ugly-output diagnosis**: if the page is weak, list the top problems before changing code.
7. **Repair pass**: fix the root causes: direction, layout, typography, assets, color, motion, or content density.
8. **Completion audit**: prove against `DESIGN.md` and the acceptance checklist before final response.

For tiny UI bug fixes or already-specified implementation edits, keep the change surgical and do not force a full `DESIGN.md`.

## Draft Or Update DESIGN.md

Write `DESIGN.md` for Codex, not for a design-school critique. It must translate taste into executable rules.

Include:

- Page intent: what the page must express and what it must not feel like.
- Audience: who looks at it and what they should remember.
- Reference map: primary reference, local references, what to borrow, what not to borrow, brand/copyright boundary.
- Dependency audit: named tools/skills found, available/missing status, fallback plan.
- Visual direction: mood, color rules, typography feel, layout density, image/assets.
- First view: hero structure, H1 tone, supporting copy, primary visual, hint of next section.
- Components: buttons, cards, nav, sections, forms/inputs.
- Motion: required background motion, scroll motion, micro-interactions, and what to avoid.
- Responsive rules: desktop, mobile, wrapping, overflow risks.
- Anti-AI-flavor rules: exact patterns to avoid.
- Acceptance checklist: concrete evidence needed before final delivery.

Do not let `DESIGN.md` stay vague. Phrases like "high-end," "cool," or "futuristic" must be decomposed into visible rules.

## Implementation Rules

When implementing after the design gate:

- Follow `DESIGN.md` strictly.
- Use the selected or available design/taste skill before coding when it exists.
- Do not introduce a new main color or visual metaphor without updating `DESIGN.md`.
- Do not copy reference logos, brand text, proprietary images, or exact page structure.
- Use real, generated, or code-native visual assets when the page needs imagery; do not leave placeholder-looking visuals.
- Make motion meaningful to the content, not random decoration.
- Match the project framework and style if a project already exists.
- Keep privacy boundaries from source documents; do not publish sensitive contact details unless requested.

## Visual Quality Gate

After implementation, inspect the actual rendered page. Technical checks alone are not enough.

Minimum verification:

- Open the page locally.
- Capture or inspect desktop first view.
- Check a mid-page content section.
- Check mobile width.
- Check for console errors.
- Check that motion is actually visible and not merely declared.
- Check that text does not overlap, overflow, or become unreadable.
- Check that the page expresses the intended identity or offer within the first few seconds.

For motion-heavy pages, verify:

- animated background or scene is nonblank and moving;
- motion does not obscure text;
- mobile reduces complexity if needed;
- hover/scroll interactions exist where promised;
- the result still feels composed when motion is paused mentally.

## Ugly-Output Diagnosis

When the user says the page is ugly, generic, low-quality, "AI-looking," or not aligned with the desired taste, do not immediately patch CSS.

First produce a diagnosis against the screenshot and `DESIGN.md`:

1. Capture or inspect the current rendered screenshot.
2. Compare the screenshot against `DESIGN.md`.
3. List exactly 5 issues.
4. For each issue, include: violated `DESIGN.md` rule, category, root cause, and fix.
5. Decide whether to:
   - revise `DESIGN.md`;
   - replace visual assets;
   - change the motion system;
   - restructure the layout;
   - only do local polish.
6. Then make targeted edits.
7. After fixes, capture or inspect again and state what changed.

Useful checks:

- Does the first view have a strong concept, or only decorative effects?
- Does the hero visual look original, or like a quick demo?
- Are typography and spacing designed, or merely large?
- Are colors intentional, or just neon on dark?
- Are animations integrated with content, or random background movement?
- Are cards and buttons custom to the concept, or generic components?

## Self-Critique Before Final

Before final response, run a short internal review:

- Did I skip any hard part of the source method?
- Did I verify every named tool or skill before claiming it?
- Did I compare the result to `DESIGN.md` and screenshots?
- Did I judge visual quality, not just runtime success?
- Did I inspect mobile and at least one lower section?
- Did I avoid exposing private contact details?
- Is the result good enough that I would show it without apologizing?

If the answer is no, continue fixing instead of finalizing.
