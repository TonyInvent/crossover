# Crossover Design — LR4 Low-Pass + Zobel · 分频器设计 — LR4 低通 + Zobel

A conventional passive crossover for a 6.5″ 8‑ohm mid-woofer, plus the full physics story behind it.
一只 6.5″ 8Ω 中低音单元的常规被动分频器设计，以及它背后的完整物理故事。

[English](#english) · [中文](#中文)

---

## English

### What this is

A 4th-order **Linkwitz–Riley low-pass** (2 kHz) with a **Zobel** impedance-compensation network, designed for a 6.5″ 8-ohm mid-woofer. Everything is derived from closed-form textbook formulas — **no optimizer**.

### The design

| Parameter | Value |
|---|---|
| Crossover | 4th-order Linkwitz–Riley low-pass, fc = 2 kHz |
| Nominal load | R = Re = 6.2 Ω |
| LR4 components | L1 = 0.930 mH · C2 = 20.4 µF · L3 = 0.465 mH · C4 = 4.54 µF |
| Zobel | Rz = 6.2 Ω · Cz = 18.2 µF (= Le/Re²) |
| Driver (Thiele–Small) | Re = 6.2 Ω · Le = 0.7 mH · Bl = 9.0 · Mms = 22 g · Fs ≈ 52 Hz |

### Results

- Electrical |H(fc)| ≈ −6.3 dB, |H(4fc)| ≈ −48 dB.
- In-band (200 Hz – 1 kHz) deviation ≈ ±1.0 dB — flat for a real driver + passive network.
- Electromagnetic damping η = D/(Bl²/Re) ≈ **0.41 at 1 kHz**: the Zobel shunts the crossover's source-impedance spike and repairs the mid-band damping hole.

### Why conventional, not an optimizer

A passive 4th-order L-C ladder has a source-impedance spike near fc that is **intrinsic to the topology** — no optimizer can remove it, and it barely matters because the cone is already mass-controlled (low velocity) there. The conventional LR4 + Zobel is the sound engineering answer.

### Repository layout

| File | What it is |
|---|---|
| `crossover_final.py` | Self-contained design script (NumPy + Matplotlib only) |
| `index.html` | Bilingual web page rendering the two essays (MathJax) |
| `why-an-impedance-curve-is-not-a-sound-pressure-curve.md` | English explainer (Feynman-style) |
| `一条阻抗曲线，为什么没有变成一条声压曲线？.md` | 中文解释 |
| `crossover_response.png` / `crossover_zsource.png` / `crossover_damping.png` | Plots |

### Run it

```bash
python crossover_final.py
```

Prints the component values and the response/impedance/damping numbers, and writes the three plots.

### Live page

**https://tonyinvent.github.io/crossover/**

---

## 中文

### 这是什么

一只 6.5″ 8Ω 中低音单元的 **4 阶 Linkwitz–Riley 低通**（2 kHz）+ **Zobel** 阻抗补偿网络。全部由教科书闭式公式直接算出——**不用任何优化器**。

### 设计

| 参数 | 值 |
|---|---|
| 分频 | 4 阶 Linkwitz–Riley 低通，fc = 2 kHz |
| 标称负载 | R = Re = 6.2 Ω |
| LR4 元件 | L1 = 0.930 mH · C2 = 20.4 µF · L3 = 0.465 mH · C4 = 4.54 µF |
| Zobel | Rz = 6.2 Ω · Cz = 18.2 µF（= Le/Re²） |
| 单元（Thiele–Small） | Re = 6.2 Ω · Le = 0.7 mH · Bl = 9.0 · Mms = 22 g · Fs ≈ 52 Hz |

### 结果

- 电气 |H(fc)| ≈ −6.3 dB，|H(4fc)| ≈ −48 dB。
- 带内（200 Hz – 1 kHz）偏差 ≈ ±1.0 dB——对真实单元 + 被动网络来说已经足够平坦。
- 电磁阻尼 η = D/(Bl²/Re) 在 1 kHz 处 ≈ **0.41**：Zobel 并联压低了分频器的源阻抗尖峰，补上了中频段的阻尼洞。

### 为什么用常规设计、而不是优化器

被动 4 阶 L-C 阶梯在分频点附近的源阻抗尖峰是**拓扑固有属性**，优化器消不掉；而且该频率振膜已进入质量控制区（速度很低），尖峰对阻尼几乎无影响。常规 LR4 + Zobel 才是工程上靠谱的答案。

### 目录结构

| 文件 | 说明 |
|---|---|
| `crossover_final.py` | 自包含设计脚本（仅 NumPy + Matplotlib） |
| `index.html` | 渲染两篇解释文章的双语网页（MathJax） |
| `why-an-impedance-curve-is-not-a-sound-pressure-curve.md` | 英文解释（费曼风格） |
| `一条阻抗曲线，为什么没有变成一条声压曲线？.md` | 中文解释 |
| `crossover_response.png` / `crossover_zsource.png` / `crossover_damping.png` | 图表 |

### 运行

```bash
python crossover_final.py
```

打印元件数值与响应/阻抗/阻尼结果，并生成三张图。

### 在线页面

**https://tonyinvent.github.io/crossover/**
