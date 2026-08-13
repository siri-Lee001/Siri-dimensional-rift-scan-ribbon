---
name: dimensional-rift-prompt
description: "Generate concise duration-adaptive bilingual video prompts for a photoreal performer remotely puppeteering one borderless horizontal dimensional scan ribbon. The ribbon replaces only the body region it crosses with a registered alternate-world counterpart, supports readable folding and multi-axis gestures, and keeps its full footprint under 25%. Use for 次元裂隙、二次元X光扫描、局部异世界替换、手势折叠、横扫、对位角色以及5/10/15/30秒脚本。"
---

# Borderless Registered Scan Ribbon

Build prompts around one visible causal chain:

`real hand motion -> ribbon motion or fold -> matching alternate body region -> synchronized response`

The effect is a borderless moving strip of alternate rendering attached to the real composition, not a framed screen carrying a portrait.

## Inputs

Collect or infer duration, real scene, real subject and wardrobe, alternate identity, alternate-world counterpart of the immediate scene, art style, and optional ending. Accept any gender, species, or body plan. Never prescribe output ratio.

## Required reading

- `references/target-effect-spec.md`: visual model and learned failures
- `references/action-library.md`: reliable complete action units
- `references/duration-composer.md`: complexity budget by duration
- `references/prompt-template.md`: concise output grammar
- `references/checklist.md`: delivery gate

Read `references/preset-dict.md` only when creative inputs are delegated.

## Core visual model

- Use exactly one opaque, borderless, wide horizontal ribbon with straight cut boundaries and sharp corners.
- Show no drawn frame, neon outline, white border, glass panel, card, or UI.
- Keep the complete footprint, including deformation, at or below 25% of the frame.
- Imagine one alternate counterpart occupying the same apparent body position, scale, pose, and facing direction as the real subject.
- The ribbon reveals only the alternate body zone it crosses. Chest shows alternate chest/costume; eye level shows alternate eyes/upper face. Never carry a complete portrait between body heights.
- Continue the subject silhouette through both horizontal boundaries. The alternate head and shoulders must not grow to fill the ribbon.
- Restyle the corresponding local background within the ribbon instead of inserting a separate framed vista.
- Keep everything outside the ribbon photoreal and unchanged.

## Remote hand control

- Keep both hands outside the left and right ends with clear air gaps. Any hand entering, crossing, covering, gripping, or supporting the ribbon is a failure.
- Make elbows, forearms, wrists, and fingers visibly initiate each response.
- Change hand trajectory or finger shape every beat; do not hold a static open-palm framing pose.
- Keep the ribbon centered between the hands and responsive without showing wires.

## Duration and priority

Apply the complexity budget in `duration-composer.md`. In 5 seconds use five beats and at most four effect verbs. When folding is requested, use exactly:

`open -> registered rise -> hero fold and flatten -> one return/sweep -> close`

Do not add another tilt, pulse, diagonal path, scan light, expression sequence, or decorative effect to that 5-second version. The fold is the hero action, not an optional clause.

For each beat write `Real action`, `Ribbon response`, and `Alternate response`.

## Folding rule

Use one joined bow-tie fold only when requested: the left and right sections hinge in depth along two clean diagonal creases; their inner acute tips meet at the center while all image content remains one continuous surface. Hold the readable folded shape briefly, then reverse the exact wrist motion and flatten fully.

Do not describe paper, grabbing corners, detached triangles, split pieces, a center crack, or duplicate characters. During the fold, suspend scanning; resume only after the ribbon is flat.

## Prompt economy

- For 5 seconds, target 260–430 English words and 5 timestamped beats.
- Use 10–18 high-value negative constraints, not a wall of repeated prohibitions.
- State each invariant once, then devote most words to visible hand choreography.
- Do not include post-production jargon, coordinates, percentages for anatomy, or implementation explanations.

## Output and validation

Return separate natural Chinese and English prompts plus a compact diagnosis/self-check. Tell the user to submit only one language version.

Run `python scripts/validate_prompt.py <english-prompt-file>` and fix every failure before delivery.
