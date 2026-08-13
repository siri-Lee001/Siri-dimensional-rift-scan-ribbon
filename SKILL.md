---
name: dimensional-rift-scan-ribbon
description: "Generate production-ready bilingual text-to-video prompts for hand-controlled horizontal dimensional image slits: border-to-border alternate imagery, single-pixel chromatic seams, asymmetrical depth folding, synchronized alternate identities, and a strict 25% total visual-footprint cap. Use for 次元裂隙、横向时空切面、手势操控、异世界人物同步、扫描、透视折叠，以及必须避免HUD屏幕、展开书页、玻璃面板和黑色丝带的高反差短视频。"
---

# Geometric Dimensional Rift Prompt Generator

Generate bilingual prompts for a **hand-controlled horizontal dimensional image slit**. Prioritize its silhouette, screen footprint, and occlusion before character lore.

## 1. Collect inputs

Require fields 1–6. Field 7 is optional.

1. Duration
2. Real scene
3. Real subject
4. Alternate scene
5. Alternate identity
6. Art style
7. Ending action, default: close and restrained smile

If the user grants creative freedom, choose a strong visual contrast. Never prescribe an output ratio; the user chooses it in the generation tool.

## 2. Load references

Read before generating:

- `references/prompt-template.md` — bilingual material-first template
- `references/checklist.md` — mandatory quality gate
- `references/target-effect-spec.md` — observed effect mechanics and failure corrections
- `references/preset-dict.md` — optional identity, palette, and gesture ideas

## 3. Define the rift before its content

Use these exact English phrases:

- `horizontal borderless dimensional image slit`
- `alternate-world imagery reaches every edge with no transparent glass margin`
- `the complete visual footprint of the rift, including edge light and every folded facet, never exceeds 25% of the full video frame`

The rift is a nonphysical horizontal cut in the camera image:

- Alternate-world color and texture fill the slit from edge to edge; there is no transparent glass margin, empty center, frame body, bezel, or interface decoration.
- The perimeter is only a single-pixel chromatic seam, visible as a subtle cyan-magenta color split where the two realities meet. It is not a neon outline or luminous frame.
- The straight state is a long, shallow horizontal rectangle or slight trapezoid with two parallel long edges.
- Folded states use one off-center diagonal crease, creating two unequal connected planes. Never use a centered vertical spine or symmetrical left/right wings.
- Every visible face continues to show the same alternate person and environment; there is no black backface.
- The effect has zero glass, HUD, dashboard, interface, book, butterfly, paper, fabric, rubber, tape, scarf, ribbon, filmstrip, or card cues.

Do not call it a `window`, `screen`, `panel`, `HUD`, `membrane`, `ribbon`, or `portal` in the generated prompt. Use `dimensional image slit`, `reality cut`, or `spatial image slice`.

## 4. Enforce the 25% projected-area cap

This is the highest-priority geometry rule:

> The complete visual footprint—including alternate imagery, seams, glow, distortion, protruding corners, and all folded faces—must remain at or below 25% of the full frame on every frame.

- Measure the entire visible envelope, not only the filled center.
- Keep the complete rift envelope inside one horizontal bounding box no wider than 78% of frame width and no taller than 22% of frame height. This conservative box occupies at most 17.16% and leaves room for motion blur while preserving the 25% hard cap.
- A narrow scan state may be approximately 68–78% wide by 5–8% high.
- When folded, add the projected area of all visible facets; the combined total still remains ≤25%, and every facet remains inside the same 78% × 22% bounding box.
- Foreshortening may reduce projected area as a plane turns toward camera depth.
- No seam, glow ray, corner, or distortion may escape the bounding box.
- Never expand into a half-frame or full-frame display.

Repeat the 25% cap in the mechanism section, timeline, and negative constraints.

## 5. Alternate image and identity synchronization

- Show one alternate version of the same person inside the slit, at approximately the same face scale as the real subject, with matching facial structure, gaze, expression timing, head angle, pose, and hand gesture.
- The alternate character is not an unrelated portrait and does not act independently.
- Show the alternate environment behind that person, filling all remaining slit pixels.
- Never show a miniature full-body character, multiple mecha figures, or a distant person standing inside a hangar.
- Let the alternate face appear at life-size only when the legal slit crosses the real face; do not resize it into a chest display.
- The alternate image deforms with the spatial cut during shear, folding, and foreshortening.
- Preserve temporal synchronization and recognizable identity rather than demanding software-like pixel-perfect UV registration.

## 6. Hand interaction and spatial behavior

- Keep hands separated from the slit by visible air gaps whenever possible. One hand may pass in front of the slit while the other controls from behind; avoid both hands gripping matching corners.
- Hands act like a puppeteer controlling invisible tension lines. No visible strings.
- The rift responds immediately and causally: pull apart → widen; opposite vertical movement → twist or diagonal shear; push/pull → move in depth; inward diagonal gesture → hard-crease fold; pinch together → contract.
- Hands do not maintain physical contact with any edge. They hover beside or pass across the slit and control it through gestures.
- Include one strong foreground palm and clear hand depth, but do not let hands obscure the rift for long.
- Keep fingers expressive and moving; no prolonged corner-holding pose.

## 7. Compact 11-second motion grammar

Use 6 continuous beats; do not overload the clip:

1. Activate a 1–2 pixel chromatic reality seam
2. Expand into a long shallow legal slit containing edge-to-edge alternate imagery
3. Push one side into depth and perform one controlled oblique shear
4. Make one off-center diagonal fold into two unequal connected planes
5. Flatten and scan across the face while the life-size alternate identity mirrors the subject
6. Contract to the chromatic seam and close

Keep the rift visible and active through most of the clip. Each phase must flow directly into the next with no reset, no second opening, and no idle hold longer than 0.25 seconds.

## 8. Light interaction

- The single-pixel chromatic seam casts only a faint matching tint onto fingertips or cheek where they come very close.
- Keep spill localized and physically plausible.
- Add faint internal parallax to establish depth without glass reflections.
- Avoid radiating neon lines, circuit graphics, corner brackets, smoke, sparks, lightning, explosive particles, or bloom.

## 9. Mandatory exclusions

Explicitly ban:

- HUD, holographic dashboard, transparent monitor, digital interface, screen bezel, circuit border, corner brackets, targeting reticle, book, open book, butterfly wings, central spine, glass panel, black fabric, ribbon, paper, card, photo, or filmstrip
- rounded corners, soft organic outline, drooping, fluttering, cloth wrinkles, cloth folds, sagging, or an opaque black backface
- hands holding or supporting an object from below
- a chest-level portrait card or independently composed portrait
- disconnected stacked strips or separate photo panels
- any visual footprint larger than 25% of the frame, any geometry outside the 78% × 22% bounding box, full-frame takeover, or background replacement
- uncontrolled glow, lightning, laser sword, explosive particles, text, logos, subtitles, cuts, zooms, or random camera motion

## 10. Write and validate

- For 11 seconds, target 650–1050 English words.
- Use concrete visual and motion commands.
- Write Chinese independently and naturally.
- Include 6 timestamps, material stack, projected-area cap, gesture causality, identity synchronization, and exclusions.
- Replace every placeholder and avoid copyrighted character names unless the user explicitly supplies one.

Run `references/checklist.md`. If saved, run:

```bash
python scripts/validate_prompt.py <prompt-file>
```

Fix every `FAIL`. Deliver English prompt, Chinese prompt, and measured self-check unless the user asks for one language only.
