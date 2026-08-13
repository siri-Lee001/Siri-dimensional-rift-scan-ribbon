#!/usr/bin/env python3
"""V7 validator for concise visual-first dimensional image-slice prompts."""
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
REQ=("one opaque horizontal dimensional image slice","alternate-world imagery fills the slice edge to edge","the alternate face stays large and clearly visible inside the slice","the complete visual footprint, including glow and folded area, never exceeds 25% of the frame")
SEP=r"[-–—]"
FORBIDDEN_JARGON=(r"\bPlate A\b",r"\bPlate B\b",r"source plate",r"screen-space",r"landmark",r"registration tolerance",r"bounding box",r"UV mapping",r"pixel mapping")
def ep(t):
 m=re.search(r"(?is)(?:^|\n)#{1,4}\s*Part\s*A\b(.*?)(?=\n#{1,4}\s*Part\s*B\b|\Z)",t);return m.group(1) if m else t
def allp(t,ps):return all(re.search(p,t,re.I|re.S) for p in ps)
def measure(t):
 en=ep(t);low=en.lower();fails=[];warn=[];ph=re.findall(r"\{[A-Z][A-Z0-9_]*\}",t);beats=re.findall(rf"\[\s*\d+(?:\.\d+)?\s*{SEP}\s*\d+(?:\.\d+)?\s*(?:s|sec|seconds)?\s*\]",en,re.I);words=re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b",en);counts={p:low.count(p) for p in REQ};neg=len(re.findall(r"\b(?:NO|NEVER)\b",en,re.I))
 if ph:fails.append("Unfilled placeholders.")
 if len(beats)!=6:fails.append(f"Expected 6 beats; found {len(beats)}.")
 for p,c in counts.items():
  if not c:fails.append(f'Missing exact phrase: "{p}".')
 jargon=[p for p in FORBIDDEN_JARGON if re.search(p,en,re.I)]
 if jargon:fails.append("Forbidden production jargon present: "+", ".join(jargon))
 if not 450<=len(words)<=800:warn.append(f"English word count {len(words)}; target 450-800.")
 if neg<25:fails.append(f"Negative constraints too sparse: {neg}.")
 checks={
 "opaque_image_fill":allp(en,(r"opaque",r"edge to edge",r"real background.{0,30}(?:not|cannot).{0,20}(?:visible|seen)|cannot be seen through")),
 "wide_sharp_shape":allp(en,(r"74%.{0,20}26%",r"straight horizontal",r"sharp|crisp corners",r"cyan.{0,10}magenta")),
 "coherent_alternate_face":allp(en,(r"large head-and-shoulders|large alternate face",r"eyes.{0,50}nose.{0,50}mouth.{0,50}cheeks",r"hair|headdress",r"environment.{0,50}(?:left and right|both sides)")),
 "real_world_stable":allp(en,(r"outside.{0,40}(?:remains|stay).{0,60}(?:same|unchanged|real)",r"NO full-frame alternate")),
 "continuous_visibility":allp(en,(r"0\.6s.{0,80}10\.0s|from about 0\.6s until about 10\.0s",r"scan light.{0,60}inside",r"full image-filled slice remains open",r"NO empty light line before 10\.0s")),
 "hands":allp(en,(r"hands stay.{0,50}left and right|hands.{0,50}left and right ends",r"NO hands cupping",r"NO edge gripping")),
 "footprint":allp(en,(r"never exceeds 25%",r"NO transparent eye shield",r"NO oval lens",r"NO vertical black crack",r"NO isolated eye",r"NO floating lips",r"NO chest-level portrait")),
 }
 for n,ok in checks.items():
  if not ok:fails.append("Missing rule set: "+n)
 if re.search(r"\b(?:9\s*:\s*16|16\s*:\s*9)\b|aspect[- ]ratio",en,re.I):fails.append("Output ratio prescribed.")
 return {"status":"PASS" if not fails else "FAIL","metrics":{"placeholder_count":len(ph),"timeline_beat_count":len(beats),"required_phrase_counts":counts,"english_word_count":len(words),"negative_constraint_count":neg,"forbidden_jargon_count":len(jargon),**checks},"failures":fails,"warnings":warn}
def self_test():
 beats="\n".join(f"[{i}.0-{i}.5s] motion" for i in range(6));pad=" ".join(["vivid alternate world image"]*100)
 s=f"""# Part A
{'. '.join(REQ)}. {beats} A 74% wide and 26% high opaque slice with straight horizontal edges, sharp crisp corners, cyan-magenta seam. Real background cannot be seen through it. Large head-and-shoulders alternate face: eyes, nose, mouth, cheeks, hair and headdress together; environment visible left and right. Everything outside remains the same unchanged real scene. Keep imagery visible from about 0.6s until about 10.0s. A scan light moves inside while the full image-filled slice remains open.
Hands stay near left and right ends. NO hands cupping. NO edge gripping. NO transparent eye shield. NO clear glass panel. NO oval lens. NO capsule. NO eye-shaped aperture. NO vertical black crack. NO centered vertical seam. NO vertical slit. NO isolated eye. NO floating lips. NO detached face. NO chest-level portrait. NO blank strip. NO empty light line before 10.0s. NO HUD. NO screen. NO card. NO book. NO butterfly. NO duplicate person. NO miniature figure. NO picture-in-picture. NO recursive image. NO full-frame alternate takeover. NO text. NO logo. NO cut. NO zoom. {pad}""";r=measure(s);assert r["status"]=="PASS",r
def main():
 p=argparse.ArgumentParser();p.add_argument("prompt_file",nargs="?",type=Path);p.add_argument("--self-test",action="store_true");a=p.parse_args()
 if a.self_test:self_test();print("Self-test passed.");return 0
 if not a.prompt_file:p.error("prompt_file required")
 r=measure(a.prompt_file.read_text(encoding="utf-8"));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["status"]=="PASS" else 1
if __name__=="__main__":sys.exit(main())
