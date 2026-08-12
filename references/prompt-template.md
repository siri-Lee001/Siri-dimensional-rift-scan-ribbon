# Body-Registered Scan-Ribbon Prompt Template

Use this template for the default SCAN-RIBBON MODE. Scale the timeline proportionally for durations other than 11 seconds.

## Input mapping

| Input | Derived prompt values |
|---|---|
| 时长 | exact beat boundaries from `preset-dict.md` |
| 现实场景 | real environment, stable background anchors, lighting |
| 现实主角 | gender, wardrobe, silhouette, identity anchors |
| 裂隙中的风格场景 | transformed texture motifs; keep it subordinate to the body transformation |
| 裂隙中的主角 | transformed identity and costume |
| 艺术风格 | style phrase and material descriptors |
| 收尾动作 | ending preset |

Auto-derive:

- `GESTURE_STYLE`
- `PALETTE`
- `REAL_IDENTITY_ANCHORS`
- `TRANSFORMED_IDENTITY_ANCHORS`
- `REGISTRATION_ANCHORS`: eyes, nose, mouth, jaw, hairline, shoulders, elbows, wrists, fingers, clothing seams
- `CONTRAST_AXIS`
- `ENDING_ACTION`

## English template

```text
SCENE SETUP

{REAL_CHARACTER}. {REAL_SCENE}. Fixed frontal medium shot, chest-level lens, waist-up framing, approximately 10% headroom, only breathing-like ±2px drift. {REAL_LIGHTING}. Photorealistic live action, cinematic detail, stable identity, coherent hands, unchanged background geometry.

CORE EFFECT — BORDERLESS BODY-REGISTERED TRANSFORMATION RIBBON

Create a borderless body-registered transformation ribbon controlled by {HIS_HER} {GESTURE_STYLE} hand movements. The ribbon is a narrow horizontal transformation frontier that INTERSECTS the subject's body plane. It is NOT a floating display in front of the person. It is NOT a portal, NOT a doorway, NOT a screen, NOT a picture frame.

Keep ribbon height between 8% and 18% of frame height, preferably 12–14%. Keep total ribbon area at or below 22% of frame area. Keep its width within the subject's arm span. Use razor-sharp compositing boundaries but NO visible neon rectangular border, NO glowing frame, NO bezel, and NO full alternate-world window.

The ribbon converts the exact real body regions it passes. Lock transformed eyes, nose, mouth, jaw, hairline, shoulders, clothing seams, elbows, wrists, hands, and fingers to the same screen coordinates as the live-action subject. Regions already passed by the scan may remain transformed. A reverse scan restores them. If a hand crosses the ribbon, transform only the intersected portion while preserving one continuous wrist, one continuous palm, and exactly five fingers.

The transformed identity is {TRANSFORMED_CHARACTER}, rendered as {ART_STYLE} with {STYLE_MATERIALS}. Preserve {REAL_IDENTITY_ANCHORS} as timing and registration anchors while changing {TRANSFORMED_IDENTITY_ANCHORS}. SAME PERSON means synchronized pose, gaze, expression, and coordinates; it does not require identical species, costume, status, or surface appearance.

Use {PALETTE}. Keep {TRANSFORMED_SCENE_MOTIFS} as compact motifs integrated behind or around the transformed body, never as a complete landscape inside a framed window. Keep the real {REAL_SCENE_SHORT} unchanged outside the transformed subject.

GESTURE CAUSALITY

Every ribbon motion must be caused by the hands on the same frames. Pulling outward opens it. Moving both hands upward scans it upward. Moving downward scans it downward. Opposing hand heights create a shallow S-wave. Pinching and crossing the ends creates a compact accordion fold. Rotating one hand creates a limited full-length axial twist. Bringing the hands together closes it. Allow no autonomous ribbon motion and no idle beat longer than 0.25 seconds.

{DURATION}-SECOND DENSE TIMELINE

[0.0–0.6s] PINCH-LINE ANTICIPATION: Begin with both hands near chest or chin level, fingertips pinching the ends of a hair-thin luminous line. Start the pull immediately. Keep the full real face and body visible.

[0.6–1.5s] PULL OPEN: Pull both hands rapidly outward. Expand only into a borderless ribbon 12–14% of frame height, within arm span and below 22% frame area. Reveal the first perfectly registered transformed slice across the chest or lower face. No frame, no portal, no separate character.

[1.5–3.0s] UPWARD SCAN + CONVERSION: Move both hands upward together. The ribbon scans from chest through neck, mouth, nose, and eyes. Every crossed region changes into {TRANSFORMED_CHARACTER} with exact coordinate lock. The already-scanned region remains transformed, producing a clean moving transformation frontier. Match expression and gaze continuously.

[3.0–4.3s] REVERSE DOWN-SCAN + SLICE SWITCH: Move the ribbon down through the face and shoulders. Reverse only selected regions so real and transformed identity alternate in stacked horizontal slices for a few frames. Keep all slices aligned to one body; no duplicated face, neck, or hands.

[4.3–5.7s] DIAGONAL S-WAVE: Raise one hand and lower the other. Tilt the narrow ribbon and form one shallow S-wave. Slide it diagonally across the face and torso while preserving registration. The subject performs a concise expression change; the transformed version mirrors it on the exact frames.

[5.7–7.2s] COMPACT ACCORDION FOLD: Pinch both ribbon ends and move them inward on opposing diagonals. Create two diagonal creases and flip one center panel, forming a low-height three-panel accordion. THIS IS THE MOST IMPORTANT FOLD. The ribbon stays 8–18% high, never becomes a diamond or giant butterfly, and never behaves like paper, film, card, or rigid glass. The registered face/body slice folds coherently with the band.

[7.2–8.6s] REOPEN + FAST DOUBLE SCAN: Snap the accordion open into one narrow ribbon. Perform one fast upward scan and one fast downward scan. Each pass toggles body regions between real and transformed states. Keep the background unchanged and anatomy continuous.

[8.6–9.9s] LIMITED AXIAL TWIST + RESTORE: Rotate one hand by approximately 90–140 degrees while stabilizing the other. Twist the ENTIRE narrow ribbon along its full length, never only one corner. Keep it low-height and within arm span. Immediately reverse the twist and scan downward to restore the live-action identity from forehead to chest.

[9.9–{DURATION}s] SNAP CLOSE + ENDING: Bring both hands together. Collapse the ribbon into a thin line and then a point. {ENDING_ACTION}. End with the real identity fully restored unless the user explicitly requests a transformed ending.

CONSISTENCY RULES

1. One person, one body, one face coordinate system throughout.
2. The ribbon intersects the body plane; it never floats as a screen in front.
3. Height stays 8–18% of frame height; area stays ≤22%; width stays within arm span.
4. Boundaries are visually borderless; no neon rectangle, frame, bezel, gate, or doorway.
5. Scan passage converts exact body regions; reverse passage restores them.
6. Face, hair, clothing, arms, wrists, palms, and fingers remain spatially registered.
7. SAME PERSON controls synchronization and coordinates, not literal appearance.
8. The fold is a compact three-panel accordion with two diagonal creases, never a diamond.
9. The entire ribbon performs the limited axial twist; no local curled corner.
10. The real background, camera, exposure, and composition remain stable.
11. Every beat contains motion; no idle pause exceeds 0.25 seconds.

NEGATIVE CONSTRAINTS

NOT a portal, NOT a doorway, NOT a screen, NOT a picture frame. NO neon rectangular border, NO glowing frame, NO full alternate-world window. NO detached floating panel, NO physical card, NO film strip, NO paper sheet, NO rigid glass pane. NO duplicate person, NO second full character, NO split screen, NO double exposure. NO facial-coordinate drift, NO misaligned eyes, NO duplicated mouth, NO broken neck seam. NO extra fingers, NO fused fingers, NO disconnected wrists, NO detached arms. NEVER exceed 18% of frame height or 22% of frame area. NEVER exceed arm span. NEVER obscure the entire face. NO idle pause, NO autonomous ribbon movement, NO full-screen transition, NO random camera movement, NO text, NO watermark, NO subtitle, NO UI, NO logo, NO flashing.
```

## 中文模板

```text
场景设定

{REAL_CHARACTER_CN}。{REAL_SCENE_CN}。固定正面中景，胸口高度取景，腰部以上构图，头顶约10%留白，镜头只允许±2px呼吸感漂移。{REAL_LIGHTING_CN}。真人电影质感，身份稳定，双手结构正确，背景几何不发生变化。

核心特效——无边框贴身变身扫描带

在人物身体平面上生成一条由双手控制的无边框横向变身扫描带。扫描带必须穿过人物身体，不是浮在人物前方的显示屏，不是传送门，不是门洞，不是画框。

扫描带高度保持画面高度8%–18%，通常使用12%–14%；总面积不超过画面22%；宽度不得超出角色臂展。边界使用锐利干净的蒙版切口，但不显示霓虹矩形边框、发光画框、屏幕边框或完整异世界窗口。

扫描带经过哪里，哪里的真人身体就按原坐标转化。眼睛、鼻子、嘴、下颌、发际线、肩膀、衣缝、手肘、手腕、手掌和手指必须与真人位置逐点对齐。已经扫过的区域可保持变身状态；反向扫描负责恢复真人。手掌穿过扫描带时，只改变相交部分，整只手必须连续，手腕不断裂，始终五根手指。

变身身份为{TRANSFORMED_CHARACTER_CN}，艺术风格为{ART_STYLE_CN}，具有{STYLE_MATERIALS_CN}。保留{REAL_IDENTITY_ANCHORS_CN}作为动作和坐标锚点，同时改变{TRANSFORMED_IDENTITY_ANCHORS_CN}。SAME PERSON 只表示姿势、视线、表情和屏幕坐标同步，不要求物种、服装、身份或表面材质相同。

使用{PALETTE_CN}。{TRANSFORMED_SCENE_MOTIFS_CN}只能作为贴合变身人物的局部纹理与小型环境意象，不能变成画框内的完整异世界全景。现实中的{REAL_SCENE_SHORT_CN}始终保持不变。

手势因果

所有扫描带动作必须由双手同帧触发：向外拉开形成窄带；双手上移带动向上扫描；双手下移带动向下扫描；一高一低形成浅S形；两端内收并交叉形成紧凑折叠；单手旋转带动全长有限轴向扭转；双手合拢让扫描带消失。禁止扫描带自行运动，禁止超过0.25秒的空白停顿。

{DURATION}秒密集时间线

[0.0–0.6s] 捏线预备：双手已在胸口或下巴附近，指尖捏住一条头发丝般细的光线两端，立即开始拉动。真人全脸和身体清楚可见。

[0.6–1.5s] 拉开窄带：双手快速向外拉开，只展开成画面高度12%–14%的无边框横带，位于臂展内、面积低于22%。在胸口或下半张脸首次出现完全对齐的变身切片。没有画框、没有传送门、没有第二个人。

[1.5–3.0s] 向上扫描变身：双手同步向上移动，扫描带从胸口依次经过颈部、嘴、鼻子和眼睛。每个被扫过的区域按原坐标转化为{TRANSFORMED_CHARACTER_CN}，已扫区域保持变身，形成清楚的移动变身分界线。表情与视线持续同步。

[3.0–4.3s] 反向下扫与切片切换：扫描带向下经过脸部和肩膀，选择性恢复部分区域，让真人与变身形态短暂形成上下错落的横向切片。所有切片仍属于同一个身体，禁止复制脸、颈部或双手。

[4.3–5.7s] 对角S形滑动：一只手抬高、另一只手压低，让窄带轻微倾斜并形成一个浅S形，斜向掠过脸和胸口。坐标保持锁定。真人做一次明确但短促的表情变化，变身形态同帧镜像。

[5.7–7.2s] 紧凑手风琴折叠：捏住扫描带两端，沿相反对角方向向内移动，形成两条斜折痕，并翻转中间一块，构成低矮的三段式手风琴。这是最重要的折叠。扫描带仍保持画面高度8%–18%，绝不能变成菱形、巨大蝴蝶、纸张、胶片、卡片或硬玻璃。带内的人脸/身体切片随三段结构连续折叠。

[7.2–8.6s] 展开与快速双扫：手风琴瞬间展开回一条窄带，立即完成一次快速上扫和一次快速下扫。每次经过都在真人与变身状态之间切换。背景完全不变，肢体保持连续。

[8.6–9.9s] 有限轴向扭转与恢复：一只手稳定，另一只手旋转约90–140度，让整条窄带沿全长轴向扭转，不能只卷一角。保持低矮、位于臂展内。随后立刻反向解扭并向下扫描，从额头到胸口恢复真人形态。

[9.9–{DURATION}s] 收线结尾：双手合拢，扫描带压缩成细线，再缩成一点。{ENDING_ACTION_CN}。除非用户明确要求，否则以真人完全恢复结束。

一致性规则

1. 全程只有一个人、一套身体、一套面部坐标。
2. 扫描带穿过身体平面，不能浮在前方变成屏幕。
3. 高度8%–18%，面积≤22%，宽度不超臂展。
4. 边界视觉上无框，不出现霓虹矩形、画框、门洞或屏幕边框。
5. 正向扫描转化对应身体区域，反向扫描恢复。
6. 脸、头发、服装、手臂、手腕、手掌和手指逐点配准。
7. SAME PERSON 约束同步与坐标，不约束物种或服装必须相同。
8. 折叠必须是低矮三段手风琴，带有两条斜折痕，不能变成菱形。
9. 有限扭转作用于整条扫描带，不能只卷曲局部。
10. 现实背景、镜头、曝光和构图全程稳定。
11. 每个时间段都有动作，空白停顿不得超过0.25秒。

负面约束

严禁传送门、门洞、屏幕、画框；严禁霓虹矩形边框、发光外框、完整异世界窗口；严禁漂浮面板、实体卡片、胶片、纸张、硬玻璃；严禁复制人物、第二个完整角色、分屏、双重曝光；严禁五官坐标漂移、眼睛错位、嘴巴重复、颈部断层；严禁多余手指、手指粘连、手腕断裂、手臂脱离；严禁扫描带高度超过画面18%、面积超过22%或宽度超出臂展；严禁完全遮住整张脸；严禁空白停顿、扫描带自行运动、全屏变身转场、随机运镜、文字、水印、字幕、UI、Logo和频闪。
```

## Self-check report

```text
=== 自检报告 ===
1. 占位符数量：PASS（0）/FAIL
2. 时间段数量：PASS（9）/FAIL
3. “borderless body-registered transformation ribbon”：PASS（≥1）/FAIL
4. 扫描动作：PASS（scan/扫描 ≥6）/FAIL
5. 负面约束：PASS（NOT/NEVER/NO ≥15）/FAIL
6. 英文长度：PASS（约900–1600词）/FAIL
7. 尺寸限制：PASS（8–18%高度、≤22%面积、臂展内）/FAIL
8. 身体配准：PASS（脸/服装/手部坐标锁定）/FAIL
9. 折叠形态：PASS（三段手风琴、无菱形）/FAIL
10. 无大画框/传送门：PASS/FAIL
11. 背景稳定、单一人物：PASS/FAIL
12. 无版权敏感词：PASS/FAIL
```
