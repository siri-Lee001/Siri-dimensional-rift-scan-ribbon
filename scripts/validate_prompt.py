#!/usr/bin/env python3
"""Quality gate for geometric holographic dimensional-rift prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = (
    "sharp-edged geometric dimensional window",
    "flat smooth taut semi-transparent holographic membrane",
    "the total visible projected area of all rift surfaces never exceeds 25% of the full video frame",
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
    if not 650 <= len(words) <= 1050:
        warnings.append(f"English word count is {len(words)}; target is 650-1050.")
    if negatives < 18:
        failures.append(f"Negative constraints are too sparse; found {negatives}, require 18.")

    material_terms = (
        r"thin.{0,25}crisp.{0,25}linear.{0,40}cyan.{0,15}magenta.{0,15}violet",
        r"straight (?:top and bottom )?edges?",
        r"sharp corners?",
        r"hard.{0,20}crease",
        r"planar.{0,25}(?:triangular|trapezoid)",
        r"no opaque black backface",
        r"subtle.{0,35}(?:light|rim).{0,40}(?:finger|cheek|skin|hair|clothing)",
    )
    material_ok = all(re.search(p, en, re.I | re.S) for p in material_terms)
    if not material_ok:
        failures.append("Rift material stack or light interaction is incomplete.")

    area_ok = (
        len(re.findall(r"(?:≤|at or below|never exceed|remains?).{0,20}25%|25%.{0,35}(?:area|frame)", en, re.I)) >= 3
        and bool(re.search(r"screen[- ]space area", en, re.I))
        and bool(re.search(r"(?:sum|add).{0,60}(?:facet|surface|face).{0,60}25%", en, re.I | re.S))
        and bool(re.search(r"NO half-frame portal", en, re.I))
        and bool(re.search(r"NO full-frame takeover", en, re.I))
    )
    if not area_ok:
        failures.append("The repeated 25% projected-area cap or folded-facet sum rule is incomplete.")

    hand_ok = (
        bool(re.search(r"hands remain beside.{0,60}(?:left/right|left and right).{0,40}(?:upper corners|edges)", en, re.I | re.S))
        and bool(re.search(r"never underneath.{0,30}support", en, re.I))
        and bool(re.search(r"invisible tension", en, re.I))
        and bool(re.search(r"no strings are visible", en, re.I))
    )
    if not hand_ok:
        failures.append("Hand position or invisible-tension control is incomplete.")

    sync_ok = all(re.search(p, en, re.I | re.S) for p in (
        r"same person",
        r"gaze",
        r"expression timing",
        r"head angle",
        r"hand gestures",
        r"mirrors?.{0,35}(?:real|subject|person)",
    ))
    if not sync_ok:
        failures.append("Alternate-identity synchronization is incomplete.")

    anti_material = (
        r"NO black fabric",
        r"NO black ribbon",
        r"NO silk",
        r"NO opaque black backface",
        r"NO cloth wrinkles",
        r"NO hands supporting",
        r"NO chest-level portrait card",
        r"NO disconnected stacked strips",
    )
    if not all(re.search(p, en, re.I) for p in anti_material):
        failures.append("Forbidden-material or portrait-card guardrails are incomplete.")

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
            "rift_material_stack_present": material_ok,
            "projected_area_cap_present": area_ok,
            "hand_control_present": hand_ok,
            "alternate_identity_synchronized": sync_ok,
            "forbidden_material_guardrails_present": all(re.search(p, en, re.I) for p in anti_material),
            "output_ratio_unspecified": ratio_unspecified,
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    beats = "\n".join(f"[{i}.0-{i}.5s] motion" for i in range(6))
    padding = " ".join(["controlled holographic geometry"] * 150)
    sample = f"""# Part A
{'. '.join(REQUIRED)}. {beats}
A thin crisp linear cyan-magenta-violet contour. Straight top and bottom edges, sharp corners, hard diagonal crease, planar acute triangular facets. Every face carries imagery; no opaque black backface. Subtle colored rim light reaches nearby fingers and cheeks.
This is a screen-space area limit. Keep at or below 25% in opening, remains at or below 25% while folding, and never exceed 25% in scanning. Add the projected area of every visible facet; the sum of all facets remains at or below 25%. NO half-frame portal. NO full-frame takeover.
Hands remain beside the left/right edges or upper corners, never underneath in a supporting pose. Invisible tension controls it; no strings are visible.
The same person matches gaze, expression timing, head angle, pose, and hand gestures; the alternate person mirrors the real subject.
NO black fabric. NO black ribbon. NO silk. NO scarf. NO rubber. NO tape. NO paper. NO card. NO photo. NO filmstrip. NO sprocket holes. NO rigid glass. NO opaque black backface. NO cloth wrinkles. NO soft folds. NO drooping. NO fluttering. NO sagging. NO rounded corners. NO hands supporting the rift from below. NO chest-level portrait card. NO disconnected stacked strips. {padding}
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
