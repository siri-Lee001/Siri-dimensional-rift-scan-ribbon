# Dimensional Rift Scan Ribbon

面向 Codex、Claude Code 等本地 Skill Agent 的视频提示词技能。它生成一条由双手操控、穿过人物身体的连续异次元折叠带：横带不是肖像卡片，而是把当前摄像机画面的同一坐标区域实时转译成另一身份与艺术媒介。

## 这一版解决什么

对测试片与目标片逐段复盘后，本版集中修正五种高频失败：

- 裂隙出现前，整张脸提前变妆。
- 完整人脸被缩小并搬到胸前，形成手持肖像卡片。
- 眼睛、嘴和服装变成三张互不相连的照片条。
- 双手只在胸前捏住卡片，缺少前后景深和大幅扫动。
- 裂隙在约7–8秒提前消失，最后两秒被花朵或粒子占用。

## 核心机制

- 强制使用 `full-frame coordinate-preserving alternate crop`：裂隙覆盖哪里，就采样原画面同位置、同大小、同透视的脸、身体、手和背景。
- 一张脸只保留一套坐标；禁止重新居中、缩放或搬到胸前。
- 所有折叠面板属于同一条连续横带，图像坐标跨折痕连续，不产生独立肖像。
- 11秒采用8段动作：暗缝、宽幅脸部揭示、手掌纵深推进、连续梯形折叠、斜向锯齿扫动、窄带扫描、最终重开、0.8秒内闭合。
- 9:16和16:9采用不同横带尺寸，避免竖屏生成胸口短卡片。
- 前景手掌视觉尺寸达到后景手掌的1.3–1.6倍；每只手腕至少横移画面宽度18%或纵移高度10%。
- 裂隙从约0.5秒持续到10.2秒，禁止花朵和漫长粒子收尾。

## 仓库结构

```text
dimensional-rift-scan-ribbon/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   └── continuous-folding-ribbon-lessons.md
├── references/
│   ├── checklist.md
│   ├── preset-dict.md
│   ├── prompt-template.md
│   └── target-effect-spec.md
└── scripts/
    └── validate_prompt.py
```

## 安装

```powershell
git clone https://github.com/siri-Lee001/Siri-dimensional-rift-scan-ribbon.git "$env:USERPROFILE\.codex\skills\dimensional-rift-scan-ribbon"
```

安装后开启新任务或重启客户端，使技能重新载入。

## 调用示例

```text
调用 $dimensional-rift-scan-ribbon 做一个11秒、9:16的视频脚本：
现实中是冷峻的深夜列车长，裂隙中是金箔圣像般的星海祭司。
重点匹配连续折叠横带、手掌纵深、斜向扫动与同坐标画面采样。
```

## 质量验证

```powershell
python scripts\validate_prompt.py --self-test
python scripts\validate_prompt.py path\to\prompt.md
```

校验器检查8段时间轴、三条强制机制短语、画幅尺寸、全画面坐标连续性、连接式折叠、手部景深、10.2秒有效时长，以及肖像卡片、照片条和过长收尾等禁项。

## License

本仓库暂未附加开源许可证；在许可证明确前，默认保留全部权利。
