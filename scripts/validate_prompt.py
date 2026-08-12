#!/usr/bin/env python3
"""Mechanical quality gate for localized dimensional-slice prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PHRASE = "borderless body-registered transformation ribbon"
LOCAL_ONLY = "transformed content exists only inside the currently visible ribbon"


def english_part(text: str) -> str:
    match = re.search(
        r"(?is)(?:^|\n)#{1,4}\s*Part\s*A\b(.*?)(?=\n#{1,4}\s*Part\s*B\b|\Z)",
        text,
    )
    return match.group(1) if match else text


def measure(text: str) -> dict[str, object]:
    en = english_part(text)
    placeholders = re.findall(r"\{[A-Z][A-Z0-9_]*\}", text)
    timestamps = re.findall(
        r"\[\s*\d+(?:\.\d+)?\s*[-–—]\s*\d+(?:\.\d+)?\s*(?:s|sec|seconds)?\s*\]",
        en,
        flags=re.I,
    )
    words = re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", en)
    negatives = len(re.findall(r"\b(?:NOT|NEVER|NO)\b", en))
    scans = len(re.findall(r"\bscan(?:s|ned|ning)?\b", en, flags=re.I))
    failures: list[str] = []
    warnings: list[str] = []

    if placeholders:
        failures.append("Unfilled placeholders remain.")
    if len(timestamps) != 8:
        failures.append(f"Expected 8 timestamped beats in Part A; found {len(timestamps)}.")
    if en.lower().count(PHRASE) < 1:
        failures.append(f'Missing exact phrase: "{PHRASE}".')
    if en.lower().count(LOCAL_ONLY) < 1:
        failures.append(f'Missing exact local-only rule: "{LOCAL_ONLY}".')
    if negatives < 12:
        failures.append(f"Negative constraints are too sparse; found {negatives}, require 12.")
    if not 650 <= len(words) <= 1200:
        warnings.append(f"English word count is {len(words)}; target is 650-1200 for 11 seconds.")

    size_ok = (
        bool(re.search(r"1\s*[-–—]\s*2\s*%", en))
        and bool(re.search(r"16\s*[-–—]\s*20\s*%", en))
        and "22%" in en
        and bool(re.search(r"arm\s+span", en, flags=re.I))
    )
    if not size_ok:
        failures.append("Missing slit, ribbon-height, maximum-height, or arm-span limits.")

    registration_terms = [
        r"body[- ]registered",
        r"screen coordinates?",
        r"face",
        r"wrists?",
        r"five fingers",
    ]
    missing_registration = [
        term for term in registration_terms if not re.search(term, en, flags=re.I)
    ]
    if missing_registration:
        failures.append("Body registration is incomplete: " + ", ".join(missing_registration))

    fold_ok = (
        bool(re.search(r"three[- ]panel accordion", en, flags=re.I))
        and bool(re.search(r"two diagonal creases", en, flags=re.I))
        and bool(re.search(r"three thin horizontal slices", en, flags=re.I))
    )
    if not fold_ok:
        failures.append("Three-panel fold or three-strip split is missing.")

    restore_ok = bool(
        re.search(r"restore.{0,60}immediately", en, flags=re.I | re.S)
        or re.search(r"immediately return.{0,30}live action", en, flags=re.I | re.S)
    )
    if not restore_ok:
        failures.append("Immediate live-action restoration is missing.")

    anti_full_body_ok = (
        bool(re.search(r"NO full-body transformation", en, flags=re.I))
        and bool(re.search(r"NO cumulative transformation", en, flags=re.I))
        and bool(re.search(r"NO (?:armor takeover|laser|light sword)", en, flags=re.I))
    )
    if not anti_full_body_ok:
        failures.append("Full-body, cumulative, armor, or energy-beam guardrails are incomplete.")

    if not re.search(r"idle\s+(?:beat|pause).{0,24}0\.25\s*seconds", en, flags=re.I):
        failures.append("Maximum 0.25-second idle interval is not stated.")

    return {
        "status": "PASS" if not failures else "FAIL",
        "metrics": {
            "placeholder_count": len(placeholders),
            "timeline_beat_count": len(timestamps),
            "exact_phrase_count": en.lower().count(PHRASE),
            "local_only_phrase_count": en.lower().count(LOCAL_ONLY),
            "scan_count": scans,
            "negative_constraint_count": negatives,
            "english_word_count": len(words),
            "size_constraints_present": size_ok,
            "body_registration_present": not missing_registration,
            "compact_fold_and_split_present": fold_ok,
            "immediate_restoration_present": restore_ok,
            "anti_full_body_guardrails_present": anti_full_body_ok,
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    negatives = " ".join(["NO drift"] * 12)
    padding = " ".join(["controlled local slice motion"] * 200)
    for separator in ("-", "–", "—"):
        beats = "\n".join(f"[{i}.0{separator}{i}.5s] local motion" for i in range(8))
        sample = f"""# Part A
{PHRASE}. {LOCAL_ONLY}. {beats}
Start at 1-2%, open to 16-20%, never exceed 22%, within arm span.
Exact screen coordinates, face, wrists, five fingers.
Three-panel accordion with two diagonal creases; three thin horizontal slices.
Restore every region immediately. No idle pause exceeds 0.25 seconds.
NO full-body transformation. NO cumulative transformation. NO armor takeover. NO laser. NO light sword.
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
