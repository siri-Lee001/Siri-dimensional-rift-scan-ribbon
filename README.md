# Dimensional Rift Scan Ribbon

为 Codex、Claude Code 等支持本地 Skill 的 AI Agent 准备的影视级视频提示词技能。它专门生成“人物身体坐标贴合式次元扫描”脚本：一条无边框窄幅扫描带穿过真人身体，将对应区域转换成高反差角色或艺术材质，并通过手势完成扫描、切片、折叠、扭转与恢复。

它不是传统的“大传送门”模板。默认效果更接近后期合成中的局部扫描变身：背景保持现实，人物五官与肢体坐标不漂移，特效动作在短时间内连续发生。

## 核心能力

- 11 秒默认采用 9 个紧凑动作段：捏线、拉开、上扫、反扫切片、S 形滑动、三段手风琴折叠、快速双扫、全长轴向扭转、收拢结尾。
- 使用 `borderless body-registered transformation ribbon` 机制，让扫描带真正穿过人物身体平面，而不是悬浮屏幕。
- 锁定眼睛、鼻子、嘴、下颌、发际线、衣缝、手腕和五根手指的真实坐标。
- 扫描带高度限制为画面 8%–18%，面积不超过 22%，宽度不超过人物臂展。
- 支持彩色玻璃、金箔圣像、矿物岩彩、漆艺金缮、蓝晒拼贴、马赛克、木版画等高识别度艺术风格。
- 同时输出可直接复制的英文 Prompt、自然中文分镜参考和机械质检报告。
- 内置提示词质检器，检测时间段、扫描密度、身体注册、折叠结构、尺寸限制和旧版大窗口回退。

## 仓库结构

```text
dimensional-rift-scan-ribbon/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   └── gold-thunder-priest.md
├── references/
│   ├── checklist.md
│   ├── preset-dict.md
│   └── prompt-template.md
└── scripts/
    └── validate_prompt.py
```

## 安装

将整个仓库克隆或复制到 Codex 的技能目录：

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL> "$env:USERPROFILE\.codex\skills\dimensional-rift-scan-ribbon"
```

也可以安装到其他支持 `SKILL.md` 的 Agent 技能目录。安装后重新打开任务，或重启对应客户端，使技能重新被发现。

## 调用示例

```text
调用 $dimensional-rift-scan-ribbon 生成一个 11 秒视频脚本：
现实中是一名深夜地铁清洁工，裂隙中是金箔雷暴祭司，
采用拜占庭珐琅马赛克与漆艺金缮风格，动作密集，结尾竖起大拇指。
```

如果没有给出角色或风格，可以直接要求技能自由发挥：

```text
调用 $dimensional-rift-scan-ribbon 做一个 11 秒高反差脚本。
角色和艺术风格由你决定，重点强化扫描、折叠和全长扭转。
```

## 输入字段

1. 时长
2. 现实场景
3. 现实主角
4. 裂隙中的风格场景或局部意象
5. 裂隙中的主角
6. 艺术风格
7. 收尾动作（可选）

## 质量验证

技能生成的 Prompt 保存为 Markdown 或文本文件后，可运行：

```powershell
python scripts\validate_prompt.py path\to\prompt.md
```

合格结果会显示：

```json
{
  "status": "PASS",
  "failures": [],
  "warnings": []
}
```

验证器会检查：

- 是否存在未替换的 `{PLACEHOLDER}`
- 英文部分是否包含 9 个时间段
- 是否使用精确的身体注册扫描带机制
- 扫描动作和负面约束是否足够
- 尺寸、臂展和人物坐标要求是否完整
- 折叠是否为三段手风琴结构
- 是否回退到旧版巨型窗口或霓虹边框

运行验证器自测：

```powershell
python scripts\validate_prompt.py --self-test
```

## 设计原则

- 动作优先于形容词堆砌。
- 手势与特效必须同帧因果对应。
- 人物只有一个，身体坐标只有一套。
- 现实背景不随扫描变成完整异世界。
- 折叠的是窄幅扫描场，而不是实体纸片或巨型菱形窗口。
- 默认避免普通动画风格，优先使用更具材质感和艺术性的媒介。

## License

本仓库暂未附加开源许可证。正式公开前，请由仓库所有者选择并添加合适的 `LICENSE`；在许可证明确前，默认保留全部权利。
