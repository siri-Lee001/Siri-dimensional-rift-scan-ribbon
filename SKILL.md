---
name: dimensional-rift-scan-ribbon
description: "Generate production-ready bilingual prompts for hand-controlled horizontal dimensional rifts using an immutable live-action base plate, a strict <=25% moving matte, and local alternate-world replacement. Use for 次元裂隙、横向时空切片、手势扫描、错切折叠、现实与艺术世界强反差，以及避免HUD屏幕、画中画、递归人物、内外同世界和全局场景替换。"
---

# Dimensional Rift Prompt Generator

Generate bilingual text-to-video prompts for a **single-subject, dual-world moving matte**. The target is not a screen displaying another shot. It is a shallow moving cut that locally replaces only the body and background fragments it currently covers.

## 1. Collect inputs

Require fields 1–6. Field 7 is optional.

1. Duration
2. Real scene
3. Real subject
4. Alternate scene
5. Alternate identity
6. Alternate art style
7. Ending action, default: close and restrained smile

If the user grants creative freedom, choose visually incompatible worlds, identities, materials, and palettes. Never prescribe an output ratio.

## 2. Load references

Read before generating:

- `references/prompt-template.md`
- `references/checklist.md`
- `references/target-effect-spec.md`
- `references/preset-dict.md` when ideas are needed

## 3. Build the shot as three compositing layers

Use these exact English phrases:

- `immutable live-action base plate outside the slit`
- `single-subject dual-world moving matte`
- `inside the matte only, restyle the exact currently covered body and background fragments`
- `the complete visual footprint of the rift, including edge light and every folded facet, never exceeds 25% of the full video frame`

Define the layers in this order, before describing alternate-world beauty:

1. **Layer 0 — immutable base plate:** the real subject and real environment occupy the full shot first. At least 75% of the frame remains visibly and recognizably this live-action reality on every frame. Outside the slit, 100% of pixels remain the original real subject and scene. The base plate never changes style, wardrobe, architecture, color world, or identity.
2. **Layer 1 — one moving matte:** one long, shallow, borderless horizontal slit, including all folds and edge effects, stays at or below 25% of the frame.
3. **Layer 2 — alternate treatment:** visible only through Layer 1. Apply alternate identity, costume, art style, light, and environment to the exact screen-space fragments currently covered by the slit. Zero alternate-world pixels may appear outside it.

The two worlds are mutually exclusive. The alternate world is forbidden globally and forbidden outside the matte. Never promote the alternate scene into the full-frame setting.

## 4. Enforce one body, not a second portrait

The rift must transform the **same continuous body**, not contain another person:

- Render one subject, one body, one head, one pose, and one performance in the entire frame.
- Do not compose a complete alternate character inside the slit.
- Do not show a self-contained alternate shot, portrait, miniature person, or full figure inside the slit.
- When the slit crosses the eyes, restyle only the covered eye-and-brow band; the forehead above and nose below remain real.
- When it crosses the mouth, restyle only the covered mouth-and-cheek band.
- When it crosses clothing, restyle only that covered clothing band.
- Covered background fragments become matching fragments of the alternate environment; they must not form a complete establishing shot.
- A fragment returns immediately to the real base plate when the slit uncovers it.
- Keep face scale, gaze, expression, head angle, pose, and gesture continuous across the boundary.

Never use `show a character inside the rift`, `alternate portrait`, `full alternate face`, `face-and-upper-torso crop`, or `mirrored person`. Those phrases invite picture-in-picture and duplicate people. Say **local identity/material replacement of the currently covered fragment**.

## 5. Define the rift silhouette and material

The rift is a nonphysical horizontal cut in the camera image:

- Alternate color and texture reach the cut itself. No transparent margin, glass, empty center, frame body, bezel, interface, or chassis.
- The boundary is only a single-pixel cyan–magenta chromatic seam where realities meet. It is not a luminous outline.
- Straight state: long shallow rectangle or slight trapezoid with two roughly parallel long edges.
- Fold state: one off-center diagonal crease forming two unequal connected planes. No centered vertical spine, symmetrical wings, or book shape.
- Every visible folded facet obeys the same local matte mapping. It does not display a duplicated shot.
- Zero HUD, dashboard, circuitry, corner brackets, reticle, book, butterfly, glass, fabric, ribbon, paper, card, photo, or filmstrip cues.

Do not call it a `window`, `screen`, `panel`, `HUD`, `monitor`, `membrane`, `ribbon`, or `portal`. Use `dimensional image slit`, `reality cut`, `spatial image slice`, or `moving matte`.

## 6. Enforce the 25% total visual-footprint cap

This is a hard per-frame rule:

> The complete envelope—including alternate treatment, seam, localized spill, distortion, corners, motion blur, and all folded facets—must remain at or below 25% of the full frame.

- Keep the envelope inside one horizontal bounding box no wider than 78% and no taller than 22% of the frame.
- A narrow scan state may be about 68–76% wide by 5–9% high.
- Add the projected areas of every folded face; folding creates no extra allowance.
- No seam, ray, glow, corner, or distortion escapes the bounding box.
- Repeat the cap in the mechanism, timeline, and negative constraints.

## 7. Hand interaction and motion

- Hands hover near the lateral ends with visible air gaps; they do not grip corners or support an object.
- One hand may pass in front while the other stays behind to establish occlusion depth.
- Pull apart → widen; opposite vertical movement → controlled shear; push/pull → depth shift; inward diagonal gesture → one off-center fold; pinch together → close.
- Keep gestures asymmetrical and causal. No visible strings.
- Avoid a persistent two-handed rectangular framing pose; change hand depth and finger configuration continuously.

For 11 seconds use six connected beats:

1. Establish the full real base plate, then activate a 1–2 pixel seam.
2. Open one legal slit; only covered fragments switch worlds.
3. Apply one depth shear with foreground/background hand occlusion.
4. Apply one off-center fold into unequal planes.
5. Flatten and scan across face and clothing; each fragment changes only while covered and restores immediately after.
6. Contract to the seam; reveal the unchanged real base plate.

No reset, second opening, edit, or idle hold longer than 0.25 seconds.

## 8. Preserve contrast without global takeover

Describe the real world first and repeat its lock in the timeline. Then express the alternate world as **local substitutions**, for example:

- covered silk robe fragment → etched ceramic mecha armor fragment
- covered palace column fragment → cropped hangar rib and cold vapor fragment
- covered warm skin/eye band → graphic ink-and-metal engineer treatment

Use incompatible palette pairs, but confine the alternate palette to the matte. The real-world lighting and palette must remain unchanged outside it.

## 9. Mandatory exclusions

Explicitly ban:

- full-frame alternate-world takeover, background replacement, global art-style transfer, or real subject becoming the alternate identity outside the slit
- picture-in-picture, inset video, framed copy, recursive image, Droste effect, nested slit, duplicate face, duplicate body, second person, miniature portrait, or complete alternate character composition
- HUD, dashboard, monitor, screen, interface, bezel, luminous frame, circuit border, corner brackets, reticle, glass panel, book, butterfly, center spine, equal wings
- fabric, ribbon, tape, paper, card, photo, filmstrip, black backface, transparent margin, empty center
- any total visual footprint above 25%, anything outside the 78% × 22% bounding box, or alternate pixels outside the matte
- text, logo, subtitle, cuts, zooms, pans, orbiting camera, random camera motion, sparks, lightning, explosive particles, rays, or broad bloom

## 10. Write and validate

- For 11 seconds, target 650–1200 English words.
- Use six timestamps and concrete screen-space examples.
- Write Chinese independently and naturally; do not mechanically translate English syntax.
- Replace every placeholder.
- Run `references/checklist.md`.
- If saved, run `python scripts/validate_prompt.py <prompt-file>` and fix every `FAIL`.
- Deliver English prompt, Chinese prompt, and a short measured self-check unless the user asks for one language only.
