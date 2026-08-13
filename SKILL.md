---
name: dimensional-rift-scan-ribbon
description: Generate production-ready text-to-video prompts for body-embedded dimensional ribbons that reveal an alternate rendering of the same camera view, with coordinate-locked faces and hands, continuous perspective folds, scan sweeps, and gesture-controlled closure. Use for 次元裂隙、横向折叠带、真人与艺术身份局部切换、手势展开/折叠/扫描，以及需要避免肖像卡片、全身变身和坐标漂移的高反差短视频。
---

# Dimensional Rift Prompt Generator

Generate bilingual prompts for a **body-embedded continuous folding ribbon**. Match the reference effect before maximizing character lore.

## 1. Collect inputs

Require fields 1–6. Field 7 is optional.

1. Duration
2. Real scene
3. Real subject
4. Alternate-scene motifs
5. Alternate identity
6. Art style
7. Ending action, default: close and restrained smile

If the user grants creative freedom, choose a high-contrast pairing from `references/preset-dict.md`. Otherwise ask only for missing required fields.

## 2. Choose the effect mode

Default to **CONTINUOUS FOLDING-RIBBON MODE**:

- One live-action camera view and one person.
- The ribbon contains an alternate rendering of the exact corresponding horizontal crop from that same camera view.
- The ribbon remains body-embedded and intersects the face, neck, shoulders, torso, or hands while active.
- The ribbon may widen, fold into connected panels, narrow into a scan strip, and reopen.
- Content outside the ribbon stays live action unless the user explicitly requests an accumulating full transformation.

Never default to a portrait card, handheld photo, detached screen, three independent rectangles, portal, or full-body transformation.

Read `references/target-effect-spec.md` after a failed test or whenever the user supplies a target video.

## 3. Load references

Read before generating:

- `references/prompt-template.md` — bilingual 8-beat continuous-ribbon template
- `references/preset-dict.md` — gestures, palettes, styles, contrast, timing
- `references/checklist.md` — mandatory quality gate
- `references/target-effect-spec.md` — geometry, framing rules, and failure corrections

## 4. Enforce full-frame coordinate sampling

Use these exact English phrases:

- `borderless body-registered transformation ribbon`
- `full-frame coordinate-preserving alternate crop`
- `one continuous connected ribbon, never separate portrait cards`

The ribbon samples the same screen-space rectangle that it covers. Its alternate face, hair, body, background, and hands keep the exact scale, crop, perspective, and coordinates of the live-action image beneath it.

- Never recenter a face inside the ribbon.
- Never resize the face to fit a panel.
- Never move a facial crop down onto the chest.
- Never show a complete floating head inside a rectangle.
- If the ribbon crosses background beside the face, show the alternate rendering of that corresponding background area—not blank filler and not a portrait backdrop.
- Folding changes only panel orientation and perspective. UV/content coordinates remain continuous across every hinge.
- The active ribbon must overlap the subject. It may not float entirely in empty space or sit wholly below the chin as a held card.

## 5. Adaptive geometry

- Frame from waist or mid-torso upward and keep both hands visible throughout the active sequence.
- Begin with a 1–2% high hairline slit.
- Open the hero ribbon across both eyes, nose, cheeks, and upper mouth; extend it toward opposite lateral hand positions so it occupies most of the available frame width.
- Compress the scan ribbon to roughly one eye-height while keeping it wide enough to intersect the face and both hand trajectories.
- Keep the ribbon between eye level and upper chest. Never turn it into a short card at the sternum.
- Use two or three connected diagonal hinges. No panel may become large enough to contain a complete independently composed head.

Use borderless alpha edges with no glow, bezel, outline, or rigid thickness.

## 6. 11-second motion grammar

Use 8 continuous beats:

1. Pinch a dark slit
2. Pull into a wide hero ribbon crossing the face
3. Push one palm toward camera and create strong depth/parallax
4. Fold the same ribbon into three or four connected trapezoid panels
5. Sweep the connected zigzag ribbon diagonally while hands exchange depth
6. Flatten into a thin scan strip and perform one up/down local scan
7. Reopen once for a final wide alternate-identity reveal
8. Compress and close in the final 0.8 seconds

Keep the ribbon visibly active from approximately 0.5s until 10.2s. Do not begin the ending early. Each wrist must travel visibly: at least 18% of frame width or 10% of frame height across the active sequence. Include one foreground palm with perspective foreshortening, approximately 1.3–1.6× the apparent size of the rear hand.

Do not add independent strip stacking, axial twist, light-sword motion, armor takeover, lightning burst, or long decorative ending particles unless explicitly requested.

## 7. Identity, hands, and style

- Keep one person, one skeleton, one face coordinate system, and one pair of hands.
- Preserve gaze, expression timing, face angle, hair silhouette, shoulder line, wrists, palms, and exactly five fingers.
- A hand crossing the ribbon may be artistic inside the ribbon and live action outside it, but it remains one continuous hand.
- For first-pass testing, preserve the subject's silhouette and change art medium, makeup, garment surface, and local motifs inside the ribbon.
- Prefer mineral-pigment mural, mother-of-pearl lacquer, stained glass, gold-leaf oil painting, porcelain enamel, mosaic, or woodblock print.
- Keep the ending under 0.8 seconds. Prefer a small smile, blink, snap, or hand release over a flower, prop, or particle sequence.

## 8. Prompt writing and validation

- For 11 seconds, target 750–1300 English words.
- Use executable spatial and motion commands, not lore-heavy narration.
- Author Chinese independently.
- Include full-frame coordinate sampling, adaptive framing, 8 timestamps, hand trajectories, connected fold, scan, and negative constraints.
- Replace every placeholder and avoid copyrighted character names.

Run `references/checklist.md`. If saved, run:

```bash
python scripts/validate_prompt.py <prompt-file>
```

Fix every `FAIL`. Deliver English prompt, independently authored Chinese prompt, and measured self-check unless the user asks for one language only.
