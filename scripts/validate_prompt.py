#!/usr/bin/env python3
"""V6 quality gate for face-anchored registered-cut prompts."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

REQUIRED = (
 "immutable live-action base plate outside the slit",
 "two co-registered source plates under one moving horizontal matte",
 "the alternate source plate remains fully invisible outside the matte",
 "the matte moves over stationary screen-space registered plates; alternate facial features never travel with the matte",
 "the alternate face center is locked to the real face center, never to the slit center",
 "the slit overlaps the real face throughout every open frame",
 "single-subject dual-world moving matte",
 "inside the matte only, restyle the exact currently covered body and background fragments",
 "the complete visual footprint of the rift, including edge light and every folded facet, never exceeds 25% of the full video frame",
)
SEP=r"[-–—]"
def enpart(t):
 m=re.search(r"(?is)(?:^|\n)#{1,4}\s*Part\s*A\b(.*?)(?=\n#{1,4}\s*Part\s*B\b|\Z)",t); return m.group(1) if m else t
def allp(t,ps): return all(re.search(p,t,re.I|re.S) for p in ps)
def measure(t):
 en=enpart(t); low=en.lower(); fails=[]; warns=[]
 ph=re.findall(r"\{[A-Z][A-Z0-9_]*\}",t); beats=re.findall(rf"\[\s*\d+(?:\.\d+)?\s*{SEP}\s*\d+(?:\.\d+)?\s*(?:s|sec|seconds)?\s*\]",en,re.I); words=re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b",en); neg=len(re.findall(r"\b(?:NO|NEVER|ZERO|FORBIDDEN)\b",en,re.I)); counts={p:low.count(p) for p in REQUIRED}
 if ph:fails.append("Unfilled placeholders remain.")
 if len(beats)!=6:fails.append(f"Expected 6 beats; found {len(beats)}.")
 for p,c in counts.items():
  if not c:fails.append(f'Missing exact phrase: "{p}".')
 if not 500<=len(words)<=900:warns.append(f"English word count {len(words)}; target 500-900.")
 if neg<25:fails.append(f"Negative constraints too sparse: {neg}.")
 checks={
 "world_lock":allp(en,(r"at least 75%",r"outside the slit.{0,80}100%",r"zero alternate-world pixels.{0,30}outside")),
 "landmark_registration":allp(en,(r"pupils?.{0,30}(?:real pupils|over real pupils)",r"nose.{0,30}real nose",r"mouth.{0,30}real mouth",r"jaw.{0,30}real jaw",r"±?3%|3% size.position tolerance")),
 "stationary_features":allp(en,(r"stationary screen-space",r"features? never travel",r"face center.{0,50}real face center",r"No feature rides|NO facial feature traveling")),
 "face_corridor":allp(en,(r"overlaps the real face.{0,40}every open frame",r"eyebrow.{0,40}chin",r"(?:±?4%|4% of frame height)",r"NO face centered on chest",r"NO isolated eye",r"NO floating lips")),
 "rectangular_geometry":allp(en,(r"72%.{0,20}29%",r"straight.{0,40}horizontal",r"end caps?.{0,20}vertical",r"NO oval lens",r"NO ellipse",r"NO capsule",r"NO eye-shaped aperture",r"NO curved long edges")),
 "nonphysical":allp(en,(r"Art style.{0,50}Plate B",r"zero material thickness",r"not.{0,30}made from glass")),
 "footprint":allp(en,(r"76%.{0,20}31%",r"72%.{0,10}29%.{0,30}20\.88%",r"NEVER exceed 25%")),
 "continuity":allp(en,(r"0\.6s.{0,60}10\.2s",r"face-filled slit visible through 10\.2s|filled with registered alternate footage from 0\.6s until 10\.2s",r"NO early disappearance",r"NO empty light line before 10\.2s")),
 "hands":allp(en,(r"hands hover.{0,50}(?:left and right|air gaps)",r"never.{0,30}below",r"palms never face upward",r"NO hands cupping",r"NO edge gripping")),
 "anti_pip":allp(en,(r"NO portrait inside the slit",r"NO second person",r"NO picture-in-picture",r"NO recursive image",r"NO global alternate-world takeover")),
 }
 for n,ok in checks.items():
  if not ok:fails.append(f"Missing or incomplete rule set: {n}.")
 if re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9)\b|aspect[- ]ratio",en,re.I):fails.append("Output ratio prescribed.")
 return {"status":"PASS" if not fails else "FAIL","metrics":{"placeholder_count":len(ph),"timeline_beat_count":len(beats),"required_phrase_counts":counts,"english_word_count":len(words),"negative_constraint_count":neg,**checks},"failures":fails,"warnings":warns}
def self_test():
 beats="\n".join(f"[{i}.0-{i}.5s] motion" for i in range(6)); pad=" ".join(["face anchored registered reality cut"]*120)
 s=f"""# Part A
{'. '.join(REQUIRED)}. {beats}
At least 75% is real. Outside the slit, 100% is real. Zero alternate-world pixels outside. Alternate pupils over real pupils, alternate nose over real nose, alternate mouth over real mouth, alternate jaw over real jaw, ±3% tolerance. Stationary screen-space plates; features never travel. Face center locked to real face center. No feature rides downward. The slit overlaps the real face in every open frame, eyebrow-to-chin corridor, ±4% of frame height.
Sharp 72% x 29% rectangle, 20.88%. Straight horizontal top and bottom edges; end caps vertical. Complete box 76% x 31%. Art style affects Plate B only; zero material thickness; not made from glass. Filled with registered alternate footage from 0.6s until 10.2s. Keep face-filled slit visible through 10.2s.
Both hands hover left and right with air gaps, never below. Palms never face upward.
NO face centered on chest. NO isolated eye. NO floating lips. NO oval lens. NO ellipse. NO capsule. NO eye-shaped aperture. NO curved long edges. NO facial feature traveling with the slit. NO early disappearance. NO empty light line before 10.2s. NO hands cupping. NO edge gripping. NO portrait inside the slit. NO second person. NO picture-in-picture. NO recursive image. NO global alternate-world takeover. NO HUD. NO screen. NO book. NO card. NO ribbon. NO text. NEVER exceed 25%. {pad}
# Part B
中文。"""; r=measure(s); assert r["status"]=="PASS",r
def main():
 p=argparse.ArgumentParser();p.add_argument("prompt_file",nargs="?",type=Path);p.add_argument("--self-test",action="store_true");a=p.parse_args()
 if a.self_test:self_test();print("Self-test passed.");return 0
 if not a.prompt_file:p.error("prompt_file required")
 r=measure(a.prompt_file.read_text(encoding="utf-8"));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["status"]=="PASS" else 1
if __name__=="__main__":sys.exit(main())
