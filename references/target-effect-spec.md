# Target Effect Specification

## Correct mental model

The target is a horizontal cut where one reality replaces another inside a shallow strip. It is not a visible object with a chassis.

- Alternate imagery reaches the boundary itself.
- The boundary is a single-pixel cyan-magenta chromatic seam, not a luminous frame.
- There is no transparent glass margin, HUD ornament, corner bracket, central hinge housing, or empty panel area.
- The strip may shear or fold in depth while remaining a single connected image slice.

## Target silhouette

- Long and shallow; horizontal width dominates height.
- Straight state: rectangle or mild trapezoid.
- Depth state: one end approaches camera and the other recedes.
- Fold state: one off-center diagonal crease creates two unequal planes.
- Never form a symmetric V, butterfly, open book, double door, or two matching monitor wings.

## Footprint rule

On every frame:

1. Enclose alternate imagery, seams, color spill, distortion, corners, motion blur, and all folded faces in one screen-space bounding box.
2. Keep that complete box no wider than 78% and no taller than 22% of the frame.
3. Keep the total visible footprint ≤25% of full-frame area.
4. Sum all folded-face projected areas; a fold does not create extra allowance.
5. No ray, line, corner, or glow may escape the box.

## Subject representation

- Show one life-size crop of the same subject, never a miniature full-body figure.
- Match face scale, gaze, expression timing, head angle, pose, and gesture.
- Fill remaining pixels with the corresponding alternate environment.
- For a mecha-engineer identity, show the engineer's face and upper torso at the same scale as the real subject—not mecha robots standing in a hangar.

## Hand relationship

- Hands control from nearby space with visible air gaps.
- Avoid bilateral corner gripping; it creates a monitor or book.
- One hand may cross in front of the slice while the other remains behind it, creating clear occlusion depth.
- Use asymmetrical gestures and off-center folds.

## Failure corrections

### HUD or transparent display

Cause: holographic window, membrane, neon perimeter, glass, diagnostic, interface, sharp corner frame.

Correction: use borderless dimensional image slit, image-to-edge fill, single-pixel chromatic seam, no transparent margin, no circuitry, no brackets, no interface graphics.

### Electronic book or butterfly

Cause: two hands at matching corners, centered vertical crease, two equal panels, symmetrical fold.

Correction: visible hand-edge gaps, one off-center diagonal crease, two unequal planes, asymmetrical depth, no central spine.

### Oversized visual footprint

Cause: width × height calculation ignores glow, rays, sharp protrusions, and motion blur.

Correction: constrain the entire visible envelope to 78% × 22%, then retain the ≤25% hard cap.

### Miniature character inside the slit

Cause: describing a hangar, robot, or full alternate character instead of a matching crop.

Correction: require one life-size face-and-upper-torso crop of the same subject; ban distant figures and multiple mecha.
