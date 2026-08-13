#!/usr/bin/env python3
"""Quality gate for horizontal borderless dimensional image-slit prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = (
    "horizontal borderless dimensional image slit",
    "alternate-world imagery reaches every edge with no transparent glass margin",
    "the complete visual footprint of the rift, including edge light and every folded facet, never exceeds 25% of the full video frame",
)
SEP = r"[-–—]"


def english_part(text: str) -> str:
    m = re.search(r"(?is)(?:^|\n)#{1,4}\s*Part\s*A\b(.*?)(?=\n#{1,4}\s*Part\s*B\b|\Z)", text)
    return m.group(1) if m else text


def measure(text: str) -> dict[str, object]:
    en = english_part(text)
    low = en.lower()
    placeholders = re.findall(r"\{[A-Z][A-Z0-9_]*\}", text)
    beats = re.findall(rf"\[\s*\d+(?:\.\d+)?\s*{SEP}\s*(?:\d+(?:\.\d+)?|DURATION)\s*(?:s|sec|seconds)?\s*\]", en, re.I)
    words = re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", en)
    negatives = len(re.findall(r"\b(?:NO|NEVER|NOT)\b", en))
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
    if not 600 <= len(words) <= 950:
        warnings.append(f"English word count is {len(words)}; target is 600-950.")
    if negatives < 24:
        failures.append(f"Negative constraints are too sparse; found {negatives}, require 24.")

    appearance_patterns = (
        r"single[- ]pixel.{0,35}cyan.{0,15}magenta.{0,35}(?:chromatic seam|color split)",
        r"long.{0,20}shallow.{0,40}(?:rectangle|trapezoid|slit)",
        r"no (?:frame body|bezel)",
        r"no transparent (?:glass )?margin",
        r"off-center diagonal crease",
        r"two unequal connected planes",
        r"no (?:black|opaque black) backface",
    )
    appearance_ok = all(re.search(p, en, re.I | re.S) for p in appearance_patterns)
    if not appearance_ok:
        failures.append("Borderless slit appearance or asymmetric fold definition is incomplete.")

    footprint_ok = (
        bool(re.search(r"bounding box.{0,50}(?:no wider than|width).{0,20}78%.{0,50}(?:no taller than|height).{0,20}22%", en, re.I | re.S))
        and bool(re.search(r"(?:imagery|seams).{0,80}(?:motion blur).{0,80}(?:folded|faces)", en, re.I | re.S))
        and bool(re.search(r"(?:sum|add).{0,60}(?:face|facet).{0,60}25%", en, re.I | re.S))
        and bool(re.search(r"no (?:ray|glow).{0,40}(?:escape|outside)", en, re.I))
        and bool(re.search(r"NEVER exceed.{0,30}78%.{0,10}22%", en, re.I))
        and bool(re.search(r"NEVER exceed 25%", en, re.I))
    )
    if not footprint_ok:
        failures.append("Complete-envelope bounding box or 25% footprint rule is incomplete.")

    identity_ok = all(re.search(p, en, re.I | re.S) for p in (
        r"one life-size alternate",
        r"same scale as the real subject",
        r"face scale",
        r"gaze",
        r"expression timing",
        r"head angle",
        r"mirrors?.{0,30}real subject",
        r"NO miniature full-body figure",
        r"NO multiple mecha figures",
    ))
    if not identity_ok:
        failures.append("Life-size single alternate identity or synchronization is incomplete.")

    hand_ok = (
        bool(re.search(r"hands hover.{0,50}air gaps", en, re.I | re.S))
        and bool(re.search(r"do not grip matching corners", en, re.I))
        and bool(re.search(r"one hand.{0,40}in front.{0,50}other.{0,30}behind", en, re.I | re.S))
    )
    if not hand_ok:
        failures.append("Air-gap hand control or foreground/background occlusion is incomplete.")

    anti_hud = (
        r"NO HUD",
        r"NO holographic dashboard",
        r"NO transparent monitor",
        r"NO digital interface",
        r"NO screen",
        r"NO circuit border",
        r"NO corner brackets",
        r"NO open book",
        r"NO electronic book",
        r"NO butterfly wings",
        r"NO centered spine",
        r"NO symmetrical V-fold",
        r"NO bilateral corner gripping",
    )
    anti_hud_ok = all(re.search(p, en, re.I) for p in anti_hud)
    if not anti_hud_ok:
        failures.append("HUD, screen, book, butterfly, or symmetric-fold guardrails are incomplete.")

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
            "borderless_slit_appearance_present": appearance_ok,
            "complete_footprint_cap_present": footprint_ok,
            "life_size_alternate_identity_present": identity_ok,
            "air_gap_occlusion_choreography_present": hand_ok,
            "anti_hud_book_guardrails_present": anti_hud_ok,
            "output_ratio_unspecified": ratio_unspecified,
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    beats = "\n".join(f"[{i}.0-{i}.5s] motion" for i in range(6))
    padding = " ".join(["controlled borderless dimensional image"] * 130)
    sample = f"""# Part A
{'. '.join(REQUIRED)}. {beats}
A single-pixel cyan-magenta chromatic seam. A long shallow horizontal rectangle. Alternate imagery fills to every edge with no frame body or bezel and no transparent glass margin. One off-center diagonal crease forms two unequal connected planes with no black backface.
Enclose imagery, seams, color spill, corners, motion blur, and folded faces in one bounding box no wider than 78% and no taller than 22%. Sum every folded face; combined area remains at or below 25%. No ray or glow may escape outside the box. NEVER exceed the 78% x 22% bounding box. NEVER exceed 25% total visual footprint.
Show one life-size alternate at the same scale as the real subject. Match face scale, gaze, expression timing, head angle, pose, and gestures. The alternate mirrors the real subject. NO miniature full-body figure. NO multiple mecha figures.
Both hands hover with visible air gaps and do not grip matching corners. One hand passes in front while the other remains behind.
NO HUD. NO holographic dashboard. NO transparent monitor. NO digital interface. NO screen. NO frame. NO bezel. NO circuit border. NO corner brackets. NO targeting reticle. NO glass. NO open book. NO electronic book. NO butterfly wings. NO centered spine. NO symmetrical V-fold. NO two equal panels. NO matching wings. NO bilateral corner gripping. NO neon rays. NO broad glow. NO black fabric. NO ribbon. NO paper. NO card. NO photo. NO filmstrip. {padding}
# Part B
中文。
"""
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
