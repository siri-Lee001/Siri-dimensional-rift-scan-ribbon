---
name: dimensional-rift-scan-ribbon
description: Generate production-ready text-to-video prompts for body-registered transformation ribbons, scanning reality tears, gesture-controlled folds, and optional dimensional windows. Use for 次元裂隙、横向扫描变身、人物局部风格替换、手势拉开/折叠/扭转特效、平行身份切换，以及需要贴合真人脸部和身体的高反差 AI 视频脚本。
---

# Dimensional Rift Scan-Ribbon Generator

Generate compact, executable bilingual prompts for AI video models. Default to a **borderless body-registered transformation ribbon**, modeled on a narrow horizontal scan band that intersects the subject and converts the corresponding body regions into an alternate identity or art style.

## 1. Collect inputs

Require fields 1–6. Field 7 is optional.

1. `[时长]`
2. `[现实场景]`
3. `[现实主角]`
4. `[裂隙中的风格场景]`
5. `[裂隙中的主角]`
6. `[艺术风格]`
7. `[收尾动作]`，默认“释放消散”

If the user says “你自己发挥 / 随便设定”, choose the parameters from `references/preset-dict.md` and state the choices briefly. If required fields are missing and no creative freedom is granted, ask only for the missing fields.

## 2. Select the effect mode

Use **SCAN-RIBBON MODE by default**.

- **SCAN-RIBBON MODE**: narrow borderless horizontal band, exact body registration, repeated up/down scans, local style replacement, compact fold, S-wave, controlled axial twist, reverse restoration. Use unless the user explicitly asks for a portal/window showing another complete world.
- **PORTAL-WINDOW MODE**: framed or bounded window containing a complete alternate scene. Use only when explicitly requested. Do not silently fall back to it.

When a reference video is provided, analyze its observable effect mechanics first. Match spatial relation, motion grammar, scale, and compositing behavior rather than reusing a generic portal template.

## 3. Load references

Read all three before generating:

- `references/prompt-template.md` — complete bilingual scan-ribbon template and timing grammar
- `references/preset-dict.md` — gesture, palette, art-style, contrast, and ending presets
- `references/checklist.md` — mandatory validation

## 4. Enforce the scan-ribbon mechanism

### Spatial compositing

- Use the exact phrase **“borderless body-registered transformation ribbon”** in English.
- Make the ribbon intersect the subject's body plane; do not float it in front like a screen.
- Keep the background outside the subject unchanged.
- Inside and behind the moving ribbon, align transformed eyes, nose, mouth, hair, shoulders, clothing, arms, and hands to the same real coordinates.
- Treat the ribbon as a moving transformation frontier: regions already passed by the scan may remain transformed; a reverse scan restores them.
- If a hand crosses the ribbon, transform only the portion inside or behind the scan boundary while preserving one continuous hand and correct finger count.

### Geometry and scale

- Keep ribbon height at **8–18% of frame height**; use 12–14% for most shots.
- Keep total ribbon area at **≤22% of frame area**.
- Keep width within the subject's arm span.
- Use razor-sharp alpha boundaries but **no visible frame, no neon rectangle, no glowing picture border**.
- Permit only mild tilt, shallow S-wave, compact accordion fold, and limited full-length axial twist.
- Never expand into a large rectangle, diamond, portal, doorway, or full-screen alternate world.

### Action density

For an 11-second video, use 9 continuous beats:

1. Pinch a thin line
2. Pull open the narrow ribbon
3. Scan upward through torso and face
4. Reverse scan downward with partial identity switching
5. S-wave / diagonal slide
6. Compact accordion fold with two diagonal creases
7. Reopen and perform a fast double scan
8. Limited full-length axial twist and reverse restoration
9. Snap closed and ending action

Allow no idle beat longer than 0.25 seconds. Every beat must include hand movement, ribbon movement, scan conversion, facial response, or a combination.

### Fold behavior

- Fold the **narrow ribbon**, not a large window.
- Create two diagonal creases and one flipping center panel, like a compact three-panel accordion.
- Keep the folded effect low-height and within the arm span.
- Do not form a diamond, giant butterfly, physical card, sheet, film strip, or origami object.

### Identity and style

- Use `SAME PERSON` only as synchronization and coordinate-registration guidance.
- The transformed identity may differ radically in species, costume, status, age styling, or medium.
- Preserve pose, gaze, expression timing, face orientation, and body coordinates.
- Use the user's art style or derive one from the preset dictionary. Never default to ordinary anime or cel shading unless requested.
- Prefer high-registration art styles with strong facial structure: stained glass, gold-leaf icon, ink-and-mineral pigment, lacquer engraving, cyanotype collage, mosaic, woodblock, or oil-and-metal-leaf hybrid.

## 5. Prompt writing rules

- Write commands, not literary narration.
- Prioritize executable motion and spatial constraints over lore.
- Keep the English prompt approximately **900–1600 words** for an 11-second video. Longer is not better; remove redundant adjectives before removing motion constraints.
- Author Chinese independently in natural storyboard language; do not translate sentence by sentence.
- Include: scene setup, core mechanism, body-registration rules, 9-beat timeline, consistency rules, negative constraints.
- Replace every placeholder. No `{...}` may remain.
- Do not use copyrighted character or franchise names. Convert them into generic visual traits.

## 6. Mandatory negative constraints

Include the following concepts in both languages:

- NOT a portal, NOT a doorway, NOT a screen, NOT a picture frame
- NO neon rectangular border, NO glowing frame, NO full alternate-world window
- NO detached floating panel, NO physical card, NO film strip, NO paper sheet
- NO duplicate person, NO second full character, NO split screen, NO double exposure
- NO coordinate drift between real and transformed facial features
- NO extra fingers, NO broken hands, NO disconnected arms
- NEVER exceed 18% of frame height or 22% of frame area
- NEVER obscure the entire face; keep identity readable during scans
- NO idle pauses, NO random independent ribbon motion
- NO text, watermark, UI, subtitle, logo, or flashing

## 7. Validate and deliver

Run `references/checklist.md`. Fix every failure before delivery.

When the finished prompt is saved as a text or Markdown file, also run:

```bash
python scripts/validate_prompt.py <prompt-file>
```

Treat every `FAIL` as a required rewrite. `WARN` items require a deliberate review, not automatic acceptance. For chat-only output, apply the same measurements manually and include them in Part C.

Deliver:

- **Part A** — English copy-ready prompt
- **Part B** — independently authored Chinese reference prompt
- **Part C** — self-check report with measured counts

If the user requests only English or a copy-ready version, output only Part A.
