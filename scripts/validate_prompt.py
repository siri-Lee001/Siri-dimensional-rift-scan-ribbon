#!/usr/bin/env python3
"""Mechanical quality gate for dimensional-rift prompt outputs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PHRASE = "borderless body-registered transformation ribbon"
OLD_FAILURE_PATTERNS = {
    "old_large_window_ratio": r"(?:45|55)\s*%\s+of\s+the\s+frame",
    "old_framed_window": r"holographic dimensional window|neon-glowing (?:rectangular )?frame",
}


def english_part(text: str) -> str:
    """Return Part A when present, otherwise validate the complete text."""
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
    negative_count = len(re.findall(r"\b(?:NOT|NEVER|NO)\b", en))
    scan_count = len(re.findall(r"\bscan(?:s|ned|ning)?\b", en, flags=re.I))
    failures: list[str] = []
    warnings: list[str] = []

    if placeholders:
        failures.append("Unfilled placeholders remain.")
    if len(timestamps) != 9:
        failures.append(f"Expected 9 timestamped beats in Part A; found {len(timestamps)}.")
    if en.lower().count(PHRASE) < 1:
        failures.append(f'Missing exact phrase: "{PHRASE}".')
    if scan_count < 6:
        failures.append(f"Scan language is too sparse; found {scan_count}, require at least 6.")
    if negative_count < 12:
        failures.append(f"Negative constraints are too sparse; found {negative_count}, require at least 12.")
    if not 900 <= len(words) <= 1600:
        warnings.append(f"English word count is {len(words)}; target is 900-1600 for 11 seconds.")

    size_ok = (
        bool(re.search(r"(?:8\s*[-–—]\s*18|12\s*[-–—]\s*14)\s*%", en))
        and "22%" in en
        and bool(re.search(r"arm\s+span", en, flags=re.I))
    )
    if not size_ok:
        failures.append("Missing ribbon height, area, or arm-span limits.")

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
        failures.append("Body-registration details are incomplete: " + ", ".join(missing_registration))

    fold_ok = (
        bool(re.search(r"three[- ]panel accordion", en, flags=re.I))
        and bool(re.search(r"two diagonal creases", en, flags=re.I))
    )
    if not fold_ok:
        failures.append("Compact three-panel accordion fold with two diagonal creases is missing.")

    if not re.search(r"idle\s+(?:beat|pause).{0,24}0\.25\s*seconds", en, flags=re.I):
        failures.append("The maximum 0.25-second idle interval is not stated.")

    forbidden_hits = [
        name for name, pattern in OLD_FAILURE_PATTERNS.items() if re.search(pattern, en, flags=re.I)
    ]
    if forbidden_hits:
        failures.append("Legacy failure patterns detected: " + ", ".join(forbidden_hits))

    return {
        "status": "PASS" if not failures else "FAIL",
        "metrics": {
            "placeholder_count": len(placeholders),
            "timeline_beat_count": len(timestamps),
            "exact_phrase_count": en.lower().count(PHRASE),
            "scan_count": scan_count,
            "negative_constraint_count": negative_count,
            "english_word_count": len(words),
            "size_constraints_present": size_ok,
            "body_registration_present": not missing_registration,
            "compact_fold_present": fold_ok,
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    negatives = " ".join(["NO drift"] * 12)
    padding = " ".join(["controlled cinematic motion"] * 300)
    for separator in ("-", "–", "—"):
        beats = "\n".join(f"[{i}.0{separator}{i}.5s] scan motion" for i in range(9))
        sample = f"""# Part A
{PHRASE}. {beats}
Height 8-18%, nominal 12-14%; area 22%; within arm span.
Exact screen coordinates, face, wrists, five fingers.
Compact three-panel accordion with two diagonal creases.
No idle beat exceeds 0.25 seconds. {negatives} {padding}
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

    text = args.prompt_file.read_text(encoding="utf-8")
    report = measure(text)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
