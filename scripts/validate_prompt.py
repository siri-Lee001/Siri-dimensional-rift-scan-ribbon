#!/usr/bin/env python3
"""Validate concise borderless registered scan-ribbon prompts."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TIME_RE = re.compile(r"\[\s*(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*(?:s|sec|seconds)?\s*\]", re.I)
FORBIDDEN_JARGON = (
    r"\bPlate [AB]\b", r"source plate", r"matte", r"mask layer",
    r"screen-space", r"coordinates?", r"landmarks?", r"bounding box",
    r"pixel mapping", r"UV mapping",
)
CORE = (
    ("borderless ribbon", r"one opaque borderless horizontal dimensional scan ribbon"),
    ("footprint cap", r"(?:never|does not) exceed(?:s)? 25%|never over 25%"),
    ("registered counterpart", r"same apparent body position.{0,100}(?:scale|size)|same apparent scale.{0,100}body position"),
    ("local body zone", r"only the (?:body )?(?:zone|region|part).{0,40}(?:crosses|intersects)|replaces only the body zone"),
    ("unchanged exterior", r"outside (?:the|this) (?:ribbon|effect).{0,80}(?:unchanged|photoreal|real)"),
    ("hands outside", r"hands? remain(?:s)? (?:wholly )?outside.{0,50}(?:ends|ribbon)"),
    ("no frame", r"no visible (?:outline|border|frame)|NO visible border"),
)


def measure(text: str) -> dict:
    failures: list[str] = []
    warnings: list[str] = []
    beats = [(float(a), float(b)) for a, b in TIME_RE.findall(text)]
    duration_match = re.search(r"Create a (\d+(?:\.\d+)?)-second", text, re.I)
    duration = float(duration_match.group(1)) if duration_match else None
    words = re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", text)
    placeholders = re.findall(r"\{[A-Z][A-Z0-9_]*\}", text)
    negative_block = re.search(r"(?is)\bNEGATIVE\s*:(.*)$", text)
    negative_count = len(re.findall(r"\b(?:NO|NEVER)\b", negative_block.group(1), re.I)) if negative_block else 0

    if placeholders:
        failures.append("Unfilled placeholders remain.")
    if duration is None:
        failures.append("Missing duration declaration.")
    if duration is not None and duration <= 6 and len(beats) != 5:
        failures.append(f"A 4-6 second prompt requires exactly 5 beats; found {len(beats)}.")
    if beats:
        if abs(beats[0][0]) > 0.01:
            failures.append("First beat must start at 0.00 seconds.")
        if duration is not None and abs(beats[-1][1] - duration) > 0.05:
            failures.append("Final beat must end at the declared duration.")
        for index, ((start, end), following) in enumerate(zip(beats, beats[1:]), 1):
            if end <= start or abs(end - following[0]) > 0.05:
                failures.append(f"Invalid continuity around beat {index}.")

    for label, pattern in (("Real action", r"Real action:"), ("Ribbon response", r"Ribbon response:"), ("Alternate response", r"Alternate response:")):
        if beats and len(re.findall(pattern, text, re.I)) < len(beats):
            failures.append(f"Every beat needs {label}.")

    for name, pattern in CORE:
        if not re.search(pattern, text, re.I | re.S):
            failures.append(f"Missing core rule: {name}.")

    fold_requested = bool(re.search(r"\b(?:fold|bow-tie|diagonal creases?)\b", text, re.I))
    if fold_requested:
        required_fold = (
            ("inward wrist cause", r"wrists? rotate inward|inward wrist"),
            ("joined surface", r"(?:one|remain) (?:joined|continuous).{0,30}(?:surface|image)|remain joined"),
            ("readable hold", r"hold.{0,30}(?:0\.2|0\.3|brief|readable)"),
            ("full flatten", r"flatten(?:s|ed|ing)? (?:fully|completely)|fully flat"),
            ("no fold travel", r"no (?:vertical|lateral|ribbon )?(?:travel|scan)|does not (?:travel|scan)"),
        )
        for name, pattern in required_fold:
            if not re.search(pattern, text, re.I | re.S):
                failures.append(f"Missing fold rule: {name}.")
        if re.search(r"\bNO fold\b", text, re.I):
            failures.append("Prompt requests and forbids folding.")

    if duration is not None and duration <= 6:
        if not 260 <= len(words) <= 430:
            warnings.append(f"English word count is {len(words)}; target 260-430 for 5 seconds.")
        if not 10 <= negative_count <= 18:
            failures.append(f"Use 10-18 high-value negatives for 5 seconds; found {negative_count}.")
        if len(re.findall(r"\b(?:tilt|pulse|diagonal sweep|scan light|glow burst)\b", text, re.I)) > 1:
            failures.append("Five-second prompt exceeds the interaction budget.")

    jargon = [p for p in FORBIDDEN_JARGON if re.search(p, text, re.I)]
    if jargon:
        failures.append("Forbidden production jargon present: " + ", ".join(jargon))
    if re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9|1\s*:\s*1)\b|aspect[- ]ratio", text, re.I):
        failures.append("Output ratio must not be prescribed.")

    return {
        "status": "PASS" if not failures else "FAIL",
        "metrics": {
            "duration_seconds": duration,
            "timeline_beats": len(beats),
            "english_word_count": len(words),
            "negative_constraint_count": negative_count,
            "placeholder_count": len(placeholders),
            "forbidden_jargon_count": len(jargon),
        },
        "failures": failures,
        "warnings": warnings,
    }


def self_test() -> None:
    beats = []
    edges = ((0, .6), (.6, 1.5), (1.5, 2.7), (2.7, 4.3), (4.3, 5))
    for start, end in edges:
        beats.append(
            f"[{start:.2f}-{end:.2f}s]\nReal action: hands remain outside both ends; wrists rotate inward then change trajectory.\n"
            "Ribbon response: one continuous motion; during the fold there is no travel or scan, the one joined surface forms diagonal creases, holds briefly for 0.25 seconds, then flattens completely.\n"
            "Alternate response: it mirrors the visible corresponding body zone."
        )
    sample = f"""Create a 5-second fixed frontal-camera photorealistic one-take video.
Create one opaque borderless horizontal dimensional scan ribbon. It never exceeds 25% of the frame and has no visible outline. One counterpart occupies the same apparent body position and scale. The ribbon replaces only the body zone it crosses. Everything outside the ribbon remains photoreal and unchanged. Both hands remain wholly outside both ends. Both wrists rotate inward; the image remains one joined surface, holds briefly for 0.25 seconds, then flattens completely; there is no travel or scan during the fold.
{chr(10).join(beats)}
NEGATIVE: NO frame. NO monitor. NO glass. NO oversized face. NO traveling portrait. NO hand contact. NO gripping. NO duplicate subject. NO detached pieces. NO center crack. NO text. NO cut. NO zoom. NO pan.
""" + " natural motion" * 20
    result = measure(sample)
    assert result["status"] == "PASS", result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt_file", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("Self-test passed.")
        return 0
    if not args.prompt_file:
        parser.error("prompt_file required")
    result = measure(args.prompt_file.read_text(encoding="utf-8"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
