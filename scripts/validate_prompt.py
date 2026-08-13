#!/usr/bin/env python3
"""Mechanical quality gate for continuous coordinate-preserving ribbon prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_PHRASES = (
    "borderless body-registered transformation ribbon",
    "full-frame coordinate-preserving alternate crop",
    "one continuous connected ribbon, never separate portrait cards",
)
RANGE_SEP = r"[-–—]"


def english_part(text: str) -> str:
    match = re.search(
        r"(?is)(?:^|\n)#{1,4}\s*Part\s*A\b(.*?)(?=\n#{1,4}\s*Part\s*B\b|\Z)",
        text,
    )
    return match.group(1) if match else text


def has_range(text: str, low: str, high: str) -> bool:
    return bool(re.search(rf"{low}\s*{RANGE_SEP}\s*{high}\s*%", text))


def measure(text: str) -> dict[str, object]:
    en = english_part(text)
    low = en.lower()
    placeholders = re.findall(r"\{[A-Z][A-Z0-9_]*\}", text)
    timestamps = re.findall(
        rf"\[\s*\d+(?:\.\d+)?\s*{RANGE_SEP}\s*(?:\d+(?:\.\d+)?|DURATION)\s*(?:s|sec|seconds)?\s*\]",
        en,
        flags=re.I,
    )
    words = re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", en)
    negatives = len(re.findall(r"\b(?:NOT|NEVER|NO)\b", en))
    failures: list[str] = []
    warnings: list[str] = []

    if placeholders:
        failures.append("Unfilled placeholders remain.")
    if len(timestamps) != 8:
        failures.append(f"Expected 8 timestamped beats in Part A; found {len(timestamps)}.")

    phrase_counts = {phrase: low.count(phrase) for phrase in REQUIRED_PHRASES}
    for phrase, count in phrase_counts.items():
        if count < 1:
            failures.append(f'Missing exact phrase: "{phrase}".')

    if negatives < 18:
        failures.append(f"Negative constraints are too sparse; found {negatives}, require 18.")
    if not 750 <= len(words) <= 1300:
        warnings.append(f"English word count is {len(words)}; target is 750-1300 for 11 seconds.")

    slit_ok = has_range(en, "1", "2")
    adaptive_geometry_ok = (
        bool(re.search(r"both hands visible", en, flags=re.I))
        and bool(re.search(r"most of the available frame width", en, flags=re.I))
        and bool(re.search(r"one eye[- ]height", en, flags=re.I))
        and bool(re.search(r"(?:eye level|eye line).{0,40}upper chest", en, flags=re.I | re.S))
    )
    if not slit_ok or not adaptive_geometry_ok:
        failures.append("Missing 1-2% slit or ratio-independent adaptive framing rules.")

    if re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9)\b|aspect[- ]ratio", en, flags=re.I):
        failures.append("Prompt prescribes an output aspect ratio; leave ratio selection to the user.")

    coordinate_patterns = (
        r"exact (?:scale|screen-space rectangle)",
        r"screen coordinates?",
        r"corresponding background",
        r"continuous (?:UV|image) coordinates?.{0,40}(?:hinge|fold)",
        r"never recenter",
        r"never (?:move|place).{0,40}(?:face|facial crop).{0,40}(?:chest|sternum)",
    )
    missing_coordinates = [
        pattern for pattern in coordinate_patterns if not re.search(pattern, en, flags=re.I | re.S)
    ]
    if missing_coordinates:
        failures.append("Full-frame coordinate mapping is incomplete.")

    fold_ok = (
        bool(re.search(r"(?:three|four|3|4).{0,30}connected trapezoid panels", en, flags=re.I))
        and bool(re.search(r"two or three diagonal hinges", en, flags=re.I))
        and bool(re.search(r"continuous.{0,50}(?:across|through).{0,30}hinges", en, flags=re.I | re.S))
        and bool(re.search(r"NO independent stacked strips", en, flags=re.I))
    )
    if not fold_ok:
        failures.append("Connected trapezoid fold or anti-strip rule is incomplete.")

    active_ok = (
        bool(re.search(r"(?:active|visible).{0,50}0\.5\s*s?.{0,40}10\.2\s*s?", en, flags=re.I | re.S))
        or (
            bool(re.search(r"\[\s*0\.5\s*[-–—]", en))
            and bool(re.search(r"[-–—]\s*10\.2\s*s?\s*\]", en, flags=re.I))
        )
    )
    ending_ok = (
        bool(re.search(r"final\s+0\.8\s+seconds", en, flags=re.I))
        or bool(re.search(r"no longer than\s+0\.8\s+seconds", en, flags=re.I))
    )
    if not active_ok or not ending_ok:
        failures.append("Ribbon-active duration or maximum 0.8-second ending is missing.")

    hand_ok = (
        bool(re.search(r"18% of frame width", en, flags=re.I))
        and bool(re.search(r"10% of frame height", en, flags=re.I))
        and bool(re.search(r"1\.3\s*[-–—]\s*1\.6\s*[×x]", en, flags=re.I))
        and bool(re.search(r"(?:foreshorten|parallax)", en, flags=re.I))
        and bool(re.search(r"exchange.{0,35}(?:near/far|depth)", en, flags=re.I))
    )
    if not hand_ok:
        failures.append("Hand travel, perspective scale, foreshortening, or depth exchange is incomplete.")

    anti_card_patterns = (
        r"NO portrait card",
        r"NO (?:floating head|detached rectangle)",
        r"NO (?:recentered face|resized face)",
        r"NO (?:independent stacked strips|three separate rectangles)",
        r"NO (?:flower ending|long particle ending)",
        r"NO full-body transformation",
    )
    missing_guards = [
        pattern for pattern in anti_card_patterns if not re.search(pattern, en, flags=re.I)
    ]
    if missing_guards:
        failures.append("Portrait-card, stacked-strip, early-ending, or full-body guardrails are incomplete.")

    return {
        "status": "PASS" if not failures else "FAIL",
        "metrics": {
            "placeholder_count": len(placeholders),
            "timeline_beat_count": len(timestamps),
            "required_phrase_counts": phrase_counts,
            "negative_constraint_count": negatives,
            "english_word_count": len(words),
            "slit_geometry_present": slit_ok,
            "adaptive_geometry_present": adaptive_geometry_ok,
            "output_ratio_unspecified": not bool(
                re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9)\b|aspect[- ]ratio", en, flags=re.I)
            ),
            "coordinate_mapping_present": not missing_coordinates,
            "connected_fold_present": fold_ok,
            "active_duration_and_ending_present": active_ok and ending_ok,
            "hand_depth_choreography_present": hand_ok,
            "anti_card_guardrails_present": not missing_guards,
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    negatives = " ".join(["NO drift"] * 18)
    padding = " ".join(["controlled coordinate-preserving ribbon motion"] * 170)
    beats = "\n".join(f"[{i}.0-{i}.5s] connected motion" for i in range(8))
    sample = f"""# Part A
{'. '.join(REQUIRED_PHRASES)}. {beats}
Keep both hands visible. Start at 1-2%. Hero ribbon spans most of the available frame width. Compress the scan ribbon to one eye-height and keep it between eye level and upper chest.
Sample the exact screen-space rectangle with exact scale and screen coordinates and corresponding background.
Never recenter the face. Never move the facial crop to the chest. Keep continuous UV coordinates across every hinge and fold.
Use three connected trapezoid panels with two or three diagonal hinges; image remains continuous across all hinges. NO independent stacked strips.
Keep the ribbon active from 0.5s through 10.2s. The ending is no longer than 0.8 seconds.
Each wrist travels 18% of frame width or 10% of frame height. Foreground palm has 1.3-1.6x scale with foreshortening and parallax. Hands exchange near/far depth.
NO portrait card. NO floating head. NO detached rectangle. NO recentered face. NO resized face. NO three separate rectangles. NO flower ending. NO long particle ending. NO full-body transformation.
{negatives} {padding}
# Part B
Chinese reference.
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
