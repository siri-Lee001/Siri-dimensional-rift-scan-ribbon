#!/usr/bin/env python3
"""V5 quality gate for co-registered dual-plate dimensional-rift prompts."""

from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

REQUIRED = (
    "immutable live-action base plate outside the slit",
    "two co-registered source plates under one moving horizontal matte",
    "the alternate source plate remains fully invisible outside the matte",
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
    en, failures, warnings = english_part(text), [], []
    low = en.lower()
    placeholders = re.findall(r"\{[A-Z][A-Z0-9_]*\}", text)
    beats = re.findall(rf"\[\s*\d+(?:\.\d+)?\s*{SEP}\s*\d+(?:\.\d+)?\s*(?:s|sec|seconds)?\s*\]", en, re.I)
    words = re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", en)
    negatives = len(re.findall(r"\b(?:NO|NEVER|ZERO|FORBIDDEN)\b", en, re.I))
    if placeholders: failures.append("Unfilled placeholders remain.")
    if len(beats) != 6: failures.append(f"Expected 6 timestamped beats; found {len(beats)}.")
    counts = {p: low.count(p) for p in REQUIRED}
    for p, count in counts.items():
        if not count: failures.append(f'Missing exact phrase: "{p}".')
    if not 650 <= len(words) <= 1300: warnings.append(f"English word count is {len(words)}; target is 650-1300.")
    if negatives < 30: failures.append(f"Negative constraints too sparse: {negatives}; require 30.")

    base_ok = has_all(en, (
        r"at least 75%.{0,80}(?:real|live-action)",
        r"outside the slit.{0,80}100%.{0,80}(?:Plate A|original|real)",
        r"zero alternate(?:-world)? pixels.{0,40}outside",
    ))
    registration_ok = has_all(en, (
        r"Plate B.{0,100}(?:complete|full-size|synchronized)",
        r"(?:identical|same).{0,60}(?:scale|face size).{0,100}(?:coordinates|screen coordinates)",
        r"gaze.{0,80}expression.{0,80}(?:pose|head angle).{0,80}(?:timing|camera)",
        r"(?:never|do not).{0,30}scale Plate B down",
        r"three large.{0,40}(?:identity )?anchors",
        r"eye treatment",
        r"hair.{0,20}headdress silhouette|hair or headdress silhouette",
        r"costume.{0,20}background cue|costume or background cue",
    ))
    local_ok = has_all(en, (
        r"(?:eye-and-brow|eye.{0,15}band)",
        r"(?:clothing|robe|torso).{0,30}band",
        r"returns? immediately|immediately returns?",
        r"NO (?:picture-in-picture|inset portrait)",
        r"NO recursive image",
        r"NO (?:duplicate person|second person)",
    ))
    geometry_ok = has_all(en, (
        r"long axis.{0,50}12 degrees.{0,20}horizontal",
        r"width.{0,50}(?:3\.5 times height|3\.5:1)",
        r"(?:Hero state|hero reveal).{0,60}(?:18.{0,10}22% high|20% high|74%.{0,20}20%)",
        r"scan state.{0,40}10.{0,10}14% high|FLATTEN.{0,80}10.{0,10}14%",
        r"shallow off-center Z-depth kink|shallow Z-kink",
        r"ends?.{0,60}(?:55%|frame width apart)",
    ))
    continuity_ok = has_all(en, (
        r"continuously open.{0,60}(?:0\.6s|0\.6 seconds).{0,50}(?:10\.2s|10\.2 seconds)",
        r"NO early disappearance",
        r"NO vertical slit",
        r"NO diamond",
        r"NO isolated triangle",
        r"NO detached shard",
        r"NO empty wireframe",
        r"NO decorative",
    ))
    material_ok = has_all(en, (
        r"art style.{0,80}(?:image rendering|Plate B)",
        r"not physically made from.{0,100}glass.{0,100}paper",
        r"zero material thickness|no object affordance",
    ))
    hand_ok = has_all(en, (
        r"hands hover.{0,60}air gaps",
        r"hand centers?.{0,80}(?:left and right|left/right).{0,60}never below",
        r"palms? never face upward|NO palms presenting",
        r"one hand.{0,45}in front.{0,60}other.{0,35}behind",
        r"NO hands cupping from below",
    ))
    footprint_ok = has_all(en, (
        r"(?:box|bounding box).{0,60}(?:no wider than|width).{0,20}78%.{0,60}(?:no taller than|height).{0,20}22%",
        r"sum.{0,60}(?:facet|face).{0,80}25%",
        r"NEVER exceed.{0,30}78%.{0,10}22%",
        r"NEVER exceed 25%",
    ))
    guards_ok = has_all(en, (
        r"NO full-frame alternate world", r"NO global alternate art style", r"NO background replacement",
        r"NO nested slit", r"NO HUD", r"NO screen", r"NO panel", r"NO book", r"NO butterfly",
    ))
    checks = {
        "immutable_base_plate": base_ok, "co_registered_plate_b": registration_ok,
        "local_registered_crop": local_ok, "horizontal_shape_lock": geometry_ok,
        "continuous_visibility": continuity_ok, "style_not_physical_material": material_ok,
        "lateral_hands_no_cupping": hand_ok, "complete_footprint_cap": footprint_ok,
        "global_and_object_guardrails": guards_ok,
    }
    for name, ok in checks.items():
        if not ok: failures.append(f"Missing or incomplete rule set: {name}.")
    if re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9)\b|aspect[- ]ratio", en, re.I):
        failures.append("Output ratio is prescribed.")
    return {"status":"PASS" if not failures else "FAIL", "metrics":{
        "placeholder_count":len(placeholders), "timeline_beat_count":len(beats),
        "required_phrase_counts":counts, "english_word_count":len(words),
        "negative_constraint_count":negatives, **checks,
    }, "failures":failures, "warnings":warnings}

def self_test() -> None:
    beats = "\n".join(f"[{i}.0-{i}.5s] motion" for i in range(6))
    padding = " ".join(["registered horizontal alternate footage"] * 190)
    sample = f"""# Part A
{'. '.join(REQUIRED)}. {beats}
At least 75% remains real live-action. Outside the slit, 100% remains Plate A. Zero alternate-world pixels outside.
Plate B is a complete full-size synchronized take at identical scale, face size, and screen coordinates; same gaze, expression, head angle, pose, timing, and camera. Never scale Plate B down. Three large identity anchors: eye treatment, hair or headdress silhouette, costume or background cue. An eye-and-brow band and clothing band immediately return when uncovered.
The long axis stays within 12 degrees of horizontal; width remains 3.5 times height. Hero state is 20% high. Scan state is 10-14% high. One shallow off-center Z-depth kink; ends remain 55% of frame width apart. Continuously open from 0.6s until 10.2s.
Art style affects Plate B image rendering only. Not physically made from glass, paper, fabric, metal, ceramic; zero material thickness and no object affordance.
Both hands hover with visible air gaps. Both hand centers stay left and right, never below. Palms never face upward. One hand passes in front while the other stays behind.
One bounding box no wider than 78% and no taller than 22%. Sum every folded facet below 25%. NEVER exceed 78% x 22%. NEVER exceed 25%.
NO early disappearance. NO vertical slit. NO square. NO diamond. NO isolated triangle. NO detached shard. NO empty wireframe. NO decorative strip. NO hands cupping from below. NO palms presenting. NO full-frame alternate world. NO global alternate art style. NO background replacement. NO picture-in-picture. NO inset portrait. NO recursive image. NO nested slit. NO duplicate person. NO second person. NO HUD. NO screen. NO panel. NO book. NO butterfly. NO interface. NO card. NO glass object. NO ribbon. NO paper. NO text. {padding}
# Part B
中文。"""
    report = measure(sample)
    assert report["status"] == "PASS", report

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("prompt_file",nargs="?",type=Path); p.add_argument("--self-test",action="store_true"); a=p.parse_args()
    if a.self_test: self_test(); print("Self-test passed."); return 0
    if not a.prompt_file: p.error("prompt_file is required unless --self-test is used")
    report=measure(a.prompt_file.read_text(encoding="utf-8")); print(json.dumps(report,ensure_ascii=False,indent=2)); return 0 if report["status"]=="PASS" else 1

if __name__ == "__main__": sys.exit(main())
