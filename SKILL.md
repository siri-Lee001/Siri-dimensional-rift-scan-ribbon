---
name: dimensional-rift-scan-ribbon
description: "Generate production-ready bilingual text-to-video prompts for hand-controlled geometric dimensional rifts: sharp linear neon energy borders, a flat taut semi-transparent holographic membrane, synchronized alternate identities, spatial twisting and hard-crease folding, with total visible projected rift area strictly capped at 25% of the video frame. Use for 次元裂隙、几何全息窗口、手势操控、异世界人物同步、锐角折叠、扫描与高反差身份短视频。"
---

# Geometric Dimensional Rift Prompt Generator

Generate bilingual prompts for a **hand-controlled geometric holographic rift**. Prioritize the rift's physical appearance and motion before character lore.

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

- `sharp-edged geometric dimensional window`
- `flat smooth taut semi-transparent holographic membrane`
- `the total visible projected area of all rift surfaces never exceeds 25% of the full video frame`

The rift is a nonphysical spatial image field suspended between the subject and camera:

- A thin, crisp, linear cyan-magenta-violet energy contour defines its perimeter.
- The contour is narrow and controlled, not a broad glow cloud.
- The interior is a flat, smooth, taut, semi-transparent holographic membrane carrying the alternate world image.
- Straight states have perfectly straight top and bottom edges and sharp corners.
- Folded states use hard geometric crease lines and planar triangular or trapezoid facets.
- The membrane has no black backface. Every visible face continues to show alternate imagery.
- It has zero paper, fabric, rubber, tape, scarf, ribbon, filmstrip, glass, or card material cues.

Do not call the rift a `ribbon` in the generated prompt. Use `dimensional window`, `holographic membrane`, `image plane`, or `energy-bounded spatial aperture`.

## 4. Enforce the 25% projected-area cap

This is the highest-priority geometry rule:

> The sum of the screen-space projected areas of every visible rift face must remain at or below 25% of the full frame area on every frame.

- Measure area, not only height or width.
- A suggested hero state is approximately 70–82% of frame width by 22–28% of frame height, provided the product stays at or below 25%.
- A narrow scan state may be approximately 75–88% wide by 6–10% high.
- When folded or split, add the projected area of all visible facets; the combined total still remains ≤25%.
- Foreshortening may reduce projected area as a plane turns toward camera depth.
- Never expand into a half-frame or full-frame portal.
- Never let the rift cover most of the person or environment.

Repeat the 25% cap in the mechanism section, timeline, and negative constraints.

## 5. Alternate image and identity synchronization

- Show the alternate version of the same person on the membrane, with matching facial structure, gaze, expression timing, head angle, pose, and hand gesture.
- The alternate character is not an unrelated portrait and does not act independently.
- Show the alternate environment behind that person on the same membrane.
- Let the complete alternate face appear only when the rift's legal ≤25% geometry crosses the real face; do not resize it into a chest card.
- The membrane image deforms with the surface during stretching, twisting, folding, and foreshortening.
- Preserve temporal synchronization and recognizable identity rather than demanding software-like pixel-perfect UV registration.

## 6. Hand interaction and spatial behavior

- Keep both hands beside the left/right edges or near the upper corners. Never place both hands underneath as if supporting an object.
- Hands act like a puppeteer controlling invisible tension lines. No visible strings.
- The rift responds immediately and causally: pull apart → widen; opposite vertical movement → twist or diagonal shear; push/pull → move in depth; inward diagonal gesture → hard-crease fold; pinch together → contract.
- Hands need not maintain physical contact with the edge. They hover beside it and control it through gestures.
- Include one strong foreground palm and clear hand depth, but do not let hands obscure the rift for long.
- Keep fingers expressive and moving; no prolonged corner-holding pose.

## 7. Compact 11-second motion grammar

Use 6 continuous beats; do not overload the clip:

1. Activate a 2–3 pixel cyan-magenta energy line
2. Expand into a legal ≤25% sharp rectangular holographic window
3. Push one side into depth and perform one controlled S-shear
4. Fold along one or two hard diagonal creases into connected acute triangular facets
5. Reopen, lift across the face, and perform one short scan while the alternate identity mirrors the subject
6. Snap flat, contract to the energy line, and close

Keep the rift visible and active through most of the clip. Each phase must flow directly into the next with no reset, no second opening, and no idle hold longer than 0.25 seconds.

## 8. Light interaction

- The cyan-magenta-violet edge casts a subtle matching rim onto nearby fingertips, cheeks, hair, and clothing.
- Keep spill localized and physically plausible.
- Add a faint internal parallax or refractive shimmer to establish holographic depth.
- Avoid smoke, sparks, lightning, explosive particles, or broad bloom that hides the geometry.

## 9. Mandatory exclusions

Explicitly ban:

- black fabric, black ribbon, silk, scarf, rubber strip, tape, paper, card, photo, filmstrip, sprocket holes, rigid glass, or screen bezel
- rounded corners, soft organic outline, drooping, fluttering, cloth wrinkles, cloth folds, sagging, or an opaque black backface
- hands holding or supporting an object from below
- a chest-level portrait card or independently composed portrait
- disconnected stacked strips or separate photo panels
- a portal larger than 25% of the frame, full-frame takeover, or background replacement
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
