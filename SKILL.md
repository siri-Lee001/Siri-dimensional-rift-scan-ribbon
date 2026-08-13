---
name: dimensional-rift-prompt
description: "Generate concise bilingual text-to-video prompts for a hand-controlled, sharp horizontal dimensional image slice containing a large clear alternate-world version of the real subject, with vivid edge-to-edge imagery and a strict 25% complete-footprint cap. Use for 次元裂隙、横向异世界影像切片、真人与动画角色反差、手势拉伸扭转和扫描效果，并避免透明眼罩、HUD、竖缝、椭圆透镜、孤立五官与技术说明可视化。"
---

# Visual-First Dimensional Rift Prompt

Generate a short, model-friendly prompt for one vivid horizontal dimensional image slice. Describe only visible things and actions. Do not explain post-production or compositing.

## Inputs

Collect:

1. Duration
2. Real scene
3. Real subject
4. Alternate scene
5. Alternate identity
6. Alternate art style
7. Optional ending action

Never prescribe an output ratio.

## Read before writing

- `references/prompt-template.md`
- `references/target-effect-spec.md`
- `references/checklist.md`

## Core visual

Use these exact English phrases:

- `one opaque horizontal dimensional image slice`
- `alternate-world imagery fills the slice edge to edge`
- `the alternate face stays large and clearly visible inside the slice`
- `the complete visual footprint, including glow and folded area, never exceeds 25% of the frame`

Describe the effect as follows:

- One long, wide, shallow rectangle floating in front of the subject.
- Approximate filled size: 72–76% of frame width and 24–28% of frame height. Keep the complete effect, including glow and deformation, at or below 25% of frame area.
- Two straight horizontal long edges, short straight end edges, sharp corners.
- A thin crisp cyan–magenta edge seam. No thick frame.
- The inside is opaque, saturated alternate-world footage. The real background is not visible through it.
- A large alternate face fills most of the slice height. It is recognizable at first glance, not a tiny person or isolated facial feature.
- The alternate person performs the same expression and hand rhythm as the real person.
- The real subject, wardrobe, and setting outside the slice remain unchanged.

The target is an image-filled spatial slice, not a literal glass object and not an empty cut in the face.

## Plain-language rule

Never put these production terms in the generated prompt:

- Plate A, Plate B, source plate
- matte, mask, compositing layer
- screen-space, coordinates, landmarks, registration tolerance
- bounding box, pixel mapping, UV mapping

Video generators may draw these terms literally as transparent panels, targeting lines, face guides, or seams. Describe the finished picture instead.

## Alternate character

- Show one large alternate head-and-shoulders image inside the slice.
- Keep the alternate face near the center of the slice and at roughly the same apparent scale as the real face.
- Include the eyes, nose, mouth, cheeks, hair or headdress together. Never crop down to one eye or floating lips.
- Use three bold identity cues that survive motion: one face cue, one silhouette cue, and one costume cue.
- Keep the alternate environment visible on both sides of the face.
- Do not demand perfect anatomical coordinate matching. Ask for visual alignment when the slice crosses the real face.

## Material and shape

- Use an opaque, taut, image-filled surface with no physical thickness.
- Art style describes the image inside, not the material of the slice.
- If the art style resembles glass, paper, collage, mosaic, metal, or fabric, say it is a painted/rendered look only.
- No transparency, refraction, reflection, clear glass, lens, oval, capsule, eye shape, vertical line, black crack, or empty wireframe.
- No HUD, interface, monitor frame, card, book, butterfly, paper sheet, or held prop.

## Hand control

- Hands remain near the left and right ends.
- Fingers pull, stretch, tilt, twist, and release with visible energy.
- Hands may approach the ends but do not hold the slice like a card or support it from below.
- The effect responds immediately to each gesture.

## 11-second motion grammar

Use six continuous beats:

1. A thin colored seam opens immediately into the full image-filled rectangle.
2. Hold the clear alternate face long enough to read it.
3. Pull one end slightly forward and the other slightly back for perspective.
4. Add one shallow off-center fold or elastic wave while preserving the wide silhouette and visible face.
5. Raise or tilt the slice across the real face; run one bright scan line **inside the alternate image** without shrinking the whole slice into a line.
6. Snap back to a flat rectangle, then close only in the final second.

Keep alternate imagery clearly visible from about 0.6s until about 10.0s. Do not let the effect vanish or become a bare light line in the middle.

## Mandatory exclusions

Explicitly ban:

- transparent eye shield, clear glass panel, oval lens, capsule, eye-shaped aperture
- vertical black crack, centered vertical seam, vertical slit
- isolated eye, floating lips, detached face, chest-level portrait
- empty light line before the final second, blank strip, outline-only shape
- full-frame alternate-world takeover or changes to the real subject outside the slice
- duplicate people, miniature full-body character, recursive picture, picture-in-picture
- hands cupping from below, card holding, edge gripping
- text, logo, subtitles, cuts, zooms, random camera movement, excessive rays or particles

## Output and validation

- Keep English around 450–750 words for 11 seconds.
- Write Chinese naturally, not as a literal translation.
- Use six timestamps.
- Run `python scripts/validate_prompt.py <prompt-file>` and fix every failure.
- Deliver English, Chinese, and a short self-check.
