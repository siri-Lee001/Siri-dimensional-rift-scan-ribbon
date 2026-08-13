# Target Effect Specification and Failure Corrections

Use after every generated-video review.

## Observable target mechanics

- A wide horizontal band crosses the face and extends toward both hands.
- The band contains the alternate rendering of the exact covered camera crop, including subject and corresponding background.
- One hand often advances toward camera, producing strong palm foreshortening and asymmetrical depth.
- The wide band bends into connected trapezoid panels with diagonal hinges.
- The alternate image stays continuous across folds; hinges do not create new crops.
- The band narrows and scans across eyes, mouth, neck, and chest, then may reopen.
- Real and alternate rendering can coexist in one frame without introducing a second person.

## Failure: full-face style spills outside the ribbon

Cause: describing a transformed identity more strongly than spatial masking.

Correction:

- Repeat that outside-ribbon pixels remain original live action.
- Preserve hair ornaments, makeup, and costume outside the band.
- Keep radical identity details subordinate to ribbon geometry.

## Failure: held portrait card

Symptoms: a complete alternate head appears inside a small rectangle at chest height; face is resized or recentered.

Cause: phrases such as “show the alternate character inside the ribbon” without full-frame coordinate mapping.

Correction:

- State `full-frame coordinate-preserving alternate crop`.
- Require the band to sample the exact covered screen-space area.
- Require background continuation beside the face.
- Ban complete heads, portrait composition, recentering, and resizing.
- Keep the wide band crossing the face or neck, not floating at the sternum.

## Failure: stacked photo strips

Symptoms: two or three independent horizontal rectangles show eyes, mouth, and costume like a collage.

Cause: requesting a three-strip split as a primary action.

Correction:

- Use one continuous zigzag ribbon with connected trapezoid panels.
- Allow narrowing, but do not detach the panels.
- Specify continuous UV/image coordinates across hinges.

## Failure: static hands

Symptoms: hands only hold edges near the torso; no depth, scale change, or sweeping gesture.

Correction:

- Require one foreground palm 1.3–1.6× the rear hand.
- Require each wrist to travel at least 18% of frame width or 10% of frame height.
- Exchange hand depth during the zigzag sweep.

## Failure: effect ends too early

Symptoms: ribbon disappears around 7–8 seconds and decorative particles occupy the ending.

Correction:

- Keep ribbon visible from about 0.5s through 10.2s.
- Limit closure and reaction to final 0.8 seconds.
- Ban flower props and long particle endings by default.

## Framing correction

- Use a waist-up or mid-torso-up composition with both hands visible.
- Let the hero ribbon cross the life-size face and reach toward opposite lateral hand positions.
- Adapt the hand arcs and ribbon width to the available frame without naming or prescribing an output ratio.
- Use camera depth and palm foreshortening when lateral room is limited.
