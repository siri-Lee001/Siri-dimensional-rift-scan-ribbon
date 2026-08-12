---
name: dimensional-rift-scan-ribbon
description: Generate production-ready text-to-video prompts for localized body-registered dimensional slices controlled by hand gestures. Use for 次元裂隙、横向局部扫描、人物局部艺术化替换、切片分层、三段折叠、手势拉开与收拢，以及要求真人脸部和身体坐标稳定的高反差短视频。
---

# Dimensional Rift Prompt Generator

Generate concise bilingual prompts for a localized transformation slice matching the supplied reference effect. Default to a **borderless body-registered transformation ribbon** whose alternate content exists only inside the currently visible slice.

## 1. Collect inputs

Require fields 1–6. Field 7 is optional.

1. 时长
2. 现实场景
3. 现实主角
4. 切片中的局部环境意象
5. 切片中的身份
6. 艺术风格
7. 收尾动作，默认“释放消散”

If the user grants creative freedom, choose a high-contrast pairing from `references/preset-dict.md`. Otherwise ask only for missing required fields.

## 2. Use localized-slice mode by default

Default to **LOCALIZED-SLICE MODE**:

- One live-action person and one stable background.
- Alternate identity appears only inside the visible ribbon or its child strips.
- Any region immediately returns to live action when the ribbon leaves it.
- Never accumulate transformation behind the scan.
- Never complete a full-body transformation.

Use an accumulating transformation frontier only when the user explicitly requests a full transformation. Use portal/window mode only when explicitly requested.

When a reference video is supplied, match its spatial relation, scale, hand choreography, fold behavior, and compositing logic before choosing character lore.

## 3. Load references

Read before generating:

- `references/prompt-template.md` — bilingual 8-beat localized-slice template
- `references/preset-dict.md` — gestures, palettes, art styles, and contrast presets
- `references/checklist.md` — mandatory quality gate

## 4. Enforce the effect

### Local-only compositing

- Use the exact English phrase `borderless body-registered transformation ribbon`.
- Also state exactly: `transformed content exists only inside the currently visible ribbon`.
- Intersect the subject's body plane; do not float the ribbon in front like a screen.
- Lock transformed eyes, nose, mouth, jaw, hair, clothing, wrists, palms, and fingers to the same screen coordinates.
- Outside the ribbon, preserve the original live-action person at all times.
- When the ribbon moves away, restore the crossed region immediately on the same frames.
- Do not describe armor, crowns, masks, lightning, or identity materials outside the ribbon.

### Geometry

- Start as a 1–2% high slit.
- Open to a 16–20% high ribbon; never exceed 22% of frame height.
- Keep width within arm span.
- A three-strip split uses three 4–7% high strips with live-action gaps between them.
- Use sharp borderless alpha edges: no neon outline, bezel, portal frame, or glowing rectangle.

### 11-second action grammar

Use 8 continuous beats:

1. Pinch a hairline slit
2. Pull open a localized ribbon
3. Move it up and down; leaving regions restore immediately
4. Form a compact three-panel accordion with two diagonal creases
5. Split into three thin horizontal slices and offset them laterally
6. Rejoin, perform one shallow S-sweep, and flatten
7. Compress ribbon to slit and point
8. Finish with a small expression or hand action

Do not add axial twist, energy sword motion, double scan, full-body conversion, or extra spectacle unless explicitly requested. Keep every hand motion readable; no idle pause longer than 0.25 seconds.

### Identity and style

- Keep one person, one skeleton, one face coordinate system, and one pair of hands.
- `SAME PERSON` means synchronized pose, expression, perspective, and coordinates.
- For first-pass testing, change artistic medium and costume details inside the slice rather than changing the whole species or body silhouette.
- Prefer beautiful, high-registration media: mineral-pigment mural, mother-of-pearl lacquer, stained glass, gold-leaf oil painting, porcelain enamel, mosaic, or woodblock print.
- Keep environment motifs small and inside the ribbon.

## 5. Prompt-writing rules

- Write executable commands, not lore-heavy narration.
- For 11 seconds, target 650–1200 English words; prioritize motion and compositing constraints.
- Write Chinese independently in natural storyboard language.
- Include scene setup, local-only mechanism, exact body registration, 8-beat timeline, and negative constraints.
- Replace every placeholder.
- Avoid copyrighted character and franchise names.

## 6. Mandatory negative constraints

Include these concepts in both languages:

- NO full-body transformation, NO cumulative transformation
- NO armor takeover, crown, helmet, mask, superhero pose
- NO laser, light sword, energy beam, lightning burst, glowing horizontal line
- NOT a portal, doorway, screen, picture frame, or complete alternate world
- NO detached panel, paper sheet, film strip, physical card, or rigid glass
- NO duplicate person, second character, split screen, or double exposure
- NO face-coordinate drift, extra fingers, fused fingers, or broken wrists
- NEVER exceed 22% of frame height or the subject's arm span
- NO camera cut, zoom, random movement, text, watermark, subtitle, UI, logo, or flashing

## 7. Validate and deliver

Run `references/checklist.md`. If the output is saved, run:

```bash
python scripts/validate_prompt.py <prompt-file>
```

Fix every `FAIL`. Deliver:

- Part A — English copy-ready prompt
- Part B — independently authored Chinese prompt
- Part C — measured self-check

If the user requests only one language, output only that language.
