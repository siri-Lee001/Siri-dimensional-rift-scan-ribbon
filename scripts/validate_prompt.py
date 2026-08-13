#!/usr/bin/env python3
"""Quality gate for single-subject dual-world moving-matte prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = (
    "immutable live-action base plate outside the slit",
    "single-subject dual-world moving matte",
    "inside the matte only, restyle the exact currently covered body and background fragments",
    "the complete visual footprint of the rift, including edge light and every folded facet, never exceeds 25% of the full video frame",
)
SEP = r"[-–—]"


def english_part(text: str) -> str:
    m = re.search(r"(?is)(?:^|\n)#{1,4}\s*Part\s*A\b(.*?)(?=\n#{1,4}\s*Part\s*B\b|\Z)", text)
    return m.group(1) if m else text


def has_all(text: str, patterns: tuple[str, ...]) -> bool:
    return all(re.search(p, text, re.I | re.S) for p in patterns)


def measure(text: str) -> dict[str, object]:
    en = english_part(text)
    low = en.lower()
    placeholders = re.findall(r"\{[A-Z][A-Z0-9_]*\}", text)
    beats = re.findall(rf"\[\s*\d+(?:\.\d+)?\s*{SEP}\s*(?:\d+(?:\.\d+)?|DURATION)\s*(?:s|sec|seconds)?\s*\]", en, re.I)
    words = re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", en)
    negatives = len(re.findall(r"\b(?:NO|NEVER|ZERO|FORBIDDEN)\b", en, re.I))
    failures: list[str] = []
    warnings: list[str] = []

    if placeholders:
        failures.append("Unfilled placeholders remain.")
    if len(beats) != 6:
        failures.append(f"Expected 6 timestamped beats; found {len(beats)}.")

    phrase_counts = {p: low.count(p) for p in REQUIRED}
    for phrase, count in phrase_counts.items():
        if count < 1:
            failures.append(f'Missing exact phrase: "{phrase}".')

    if not 650 <= len(words) <= 1200:
        warnings.append(f"English word count is {len(words)}; target is 650-1200.")
    if negatives < 30:
        failures.append(f"Negative constraints are too sparse; found {negatives}, require 30.")

    base_plate_ok = has_all(en, (
        r"at least 75%.{0,80}(?:real|live-action)",
        r"outside the slit.{0,80}100%.{0,80}(?:original|real|live-action)",
        r"zero alternate-world pixels.{0,40}outside",
        r"(?:forbidden|never).{0,80}(?:global|full-frame)|(?:global|full-frame).{0,80}(?:forbidden|never)",
    ))
    if not base_plate_ok:
        failures.append("Immutable real-world base-plate lock or zero-alternate-pixels rule is incomplete.")

    local_matte_ok = has_all(en, (
        r"one subject.{0,30}one head.{0,30}one.{0,20}body",
        r"(?:eye-and-brow|eye.{0,15}band)",
        r"(?:clothing|robe|torso).{0,25}(?:band|fragment)",
        r"returns? immediately.{0,60}(?:uncover|passes|leaves)",
        r"NO (?:second person|duplicate body)",
        r"NO (?:picture-in-picture|inset video)",
        r"NO (?:recursive image|Droste effect)",
    ))
    if not local_matte_ok:
        failures.append("Local body-fragment replacement or anti-duplicate/anti-recursion rules are incomplete.")

    appearance_ok = has_all(en, (
        r"single[-– ]pixel.{0,30}cyan.{0,12}magenta.{0,35}(?:chromatic seam|color split)",
        r"long.{0,20}shallow.{0,40}(?:rectangle|trapezoid|slit)",
        r"no (?:frame body|bezel|transparent glass margin)",
        r"off-center diagonal crease",
        r"two unequal connected planes",
    ))
    if not appearance_ok:
        failures.append("Borderless slit appearance or asymmetric fold definition is incomplete.")

    footprint_ok = has_all(en, (
        r"bounding box.{0,60}(?:no wider than|width).{0,20}78%.{0,60}(?:no taller than|height).{0,20}22%",
        r"(?:sum|add).{0,60}(?:facet|face).{0,80}25%",
        r"no (?:ray|glow).{0,50}(?:escape|outside)",
        r"NEVER exceed.{0,30}78%.{0,10}22%",
        r"NEVER exceed 25%",
    ))
    if not footprint_ok:
        failures.append("Complete-envelope bounding box or 25% footprint rule is incomplete.")

    hand_ok = has_all(en, (
        r"hands hover.{0,60}air gaps",
        r"never grip matching corners|do not grip matching corners",
        r"one hand.{0,45}in front.{0,60}other.{0,35}behind",
    ))
    if not hand_ok:
        failures.append("Air-gap hand control or front/back occlusion is incomplete.")

    anti_global_ok = has_all(en, (
        r"NO full-frame alternate world",
        r"NO global alternate art style",
        r"NO background replacement",
        r"NO alternate (?:costume|architecture).{0,25}outside the slit",
        r"NO duplicate face",
        r"NO nested slit",
    ))
    if not anti_global_ok:
        failures.append("Global takeover, nested-slit, or duplicate-person guardrails are incomplete.")

    anti_object_ok = has_all(en, (
        r"NO HUD",
        r"NO transparent monitor",
        r"NO screen",
        r"NO panel",
        r"NO digital interface",
        r"NO open book",
        r"NO butterfly wings",
        r"NO centered spine",
        r"NO bilateral corner gripping",
    ))
    if not anti_object_ok:
        failures.append("HUD, screen, book, butterfly, or symmetric-object guardrails are incomplete.")

    ratio_unspecified = not bool(re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9)\b|aspect[- ]ratio", en, re.I))
    if not ratio_unspecified:
        failures.append("Prompt prescribes an output ratio; leave it to the user.")

    return {
        "status": "PASS" if not failures else "FAIL",
        "metrics": {
            "placeholder_count": len(placeholders),
            "timeline_beat_count": len(beats),
            "required_phrase_counts": phrase_counts,
            "english_word_count": len(words),
            "negative_constraint_count": negatives,
            "immutable_base_plate_present": base_plate_ok,
            "local_fragment_matte_present": local_matte_ok,
            "borderless_slit_appearance_present": appearance_ok,
            "complete_footprint_cap_present": footprint_ok,
            "air_gap_occlusion_choreography_present": hand_ok,
            "anti_global_takeover_present": anti_global_ok,
            "anti_hud_object_guardrails_present": anti_object_ok,
            "output_ratio_unspecified": ratio_unspecified,
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    beats = "\n".join(f"[{i}.0-{i}.5s] motion" for i in range(6))
    padding = " ".join(["controlled local reality replacement"] * 160)
    sample = f"""# Part A
{'. '.join(REQUIRED)}. {beats}
At least 75% remains real live-action. Outside the slit, 100% remains the original real scene. Zero alternate-world pixels appear outside. The alternate world is forbidden as a global full-frame scene.
Render one subject, one head, one continuous body. An eye-and-brow band and a clothing band change locally. Each fragment returns immediately when the slit uncovers it.
A single-pixel cyan-magenta chromatic seam. A long shallow horizontal slit and rectangle, then a trapezoid. No frame body or bezel and no transparent glass margin. One off-center diagonal crease forms two unequal connected planes.
One bounding box no wider than 78% and no taller than 22%. Sum every folded facet and remain below 25%. No ray or glow may escape outside. NEVER exceed 78% x 22%. NEVER exceed 25%.
Both hands hover with visible air gaps and never grip matching corners. One hand passes in front while the other stays behind.
NO full-frame alternate world. NO global alternate art style. NO background replacement. NO alternate costume outside the slit. NO alternate architecture outside the slit. NO picture-in-picture. NO inset video. NO framed copy. NO recursive image. NO Droste effect. NO nested slit. NO duplicate face. NO duplicate body. NO second person. NO complete alternate character. NO miniature portrait. NO full figure. NO HUD. NO holographic dashboard. NO transparent monitor. NO screen. NO panel. NO digital interface. NO frame body. NO bezel. NO circuit border. NO corner brackets. NO reticle. NO glass. NO open book. NO butterfly wings. NO centered spine. NO equal wings. NO bilateral corner gripping. NO ribbon. NO paper. NO card. NO text. {padding}
# Part B
中文。"""
    report = measure(sample)
    assert report["status"] == "PASS", report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt_file", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("Self-test passed.")
        return 0
    if not args.prompt_file:
        parser.error("prompt_file is required unless --self-test is used")
    report = measure(args.prompt_file.read_text(encoding="utf-8"))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
