# Target Effect Specification

## Correct mental model

The target is a three-layer composite:

1. An immutable live-action base plate fills the full frame.
2. One shallow moving matte covers no more than 25% of the frame.
3. Alternate identity, style, and environment are visible only where that matte overlaps the existing subject and background.

It is a local replacement in one continuous image—not a screen showing another shot.

## Non-negotiable world separation

- At least 75% of every frame remains the recognizable real subject and real environment.
- Every pixel outside the matte remains real-world imagery.
- Alternate-world content has zero visibility outside the matte.
- The real and alternate scenes must be visually and semantically incompatible.
- The base plate never adopts the alternate costume, architecture, palette, or rendering style.

## Subject representation

- One subject, one head, one body, one pose.
- The same anatomical region changes locally at the matte boundary.
- A slit across the eyes contains only the alternate eye band, not a complete alternate face.
- A slit across the torso contains only the alternate torso band, not a miniature full person.
- Uncovered regions restore immediately to the real identity.
- Never place a second character, portrait, inset shot, or recursive copy inside the slit.

## Rift silhouette and material

- Long, shallow horizontal reality cut.
- Alternate treatment reaches the cut edge; no transparent glass margin.
- Boundary is a single-pixel cyan–magenta chromatic seam, not a luminous frame.
- One off-center diagonal fold may create two unequal connected facets.
- Every facet remains part of the same local moving matte.
- No HUD, screen, panel, chassis, book, butterfly, ribbon, fabric, or black backface.

## Footprint rule

On every frame:

1. Enclose alternate treatment, seam, spill, distortion, corners, motion blur, and folded facets in one screen-space box.
2. Keep the box no wider than 78% and no taller than 22% of frame.
3. Keep the total visible footprint at or below 25%.
4. Sum the projected areas of all folded facets.
5. Let no ray, line, corner, or glow escape the box.

## Failure corrections

### Inside and outside become the same alternate world

Cause: the alternate scene is described as a stronger full scene than the real base plate, so the model promotes it globally.

Correction: define and repeat the immutable real base plate first; require at least 75% real-world visibility; state zero alternate-world pixels outside the matte; express alternate details only as local substitutions.

### Recursive picture-in-picture

Cause: asking for an alternate person, portrait, mirrored character, or face-and-torso crop inside the slit.

Correction: render no second person and no self-contained alternate shot. Restyle only the exact eye, skin, hair, clothing, or background fragment currently covered by the moving matte.

### HUD or transparent display

Cause: window, hologram, membrane, neon perimeter, glass, diagnostic, interface, corner frame.

Correction: use a borderless reality cut with a single-pixel chromatic seam and no transparent margin or circuitry.

### Electronic book or butterfly

Cause: two hands gripping matching corners, a centered crease, two equal planes.

Correction: visible hand-edge gaps, asymmetrical hand depth, one off-center diagonal crease, two unequal planes.

### Oversized effect

Cause: counting the inner image but ignoring glow, fold faces, rays, and blur.

Correction: constrain the complete envelope to 78% × 22% and preserve the ≤25% hard cap in every state.
