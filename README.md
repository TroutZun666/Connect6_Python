# Connect6_Python

使用 Python + pygame 实现的六子棋（Connect6）双人对战小游戏。19×19 棋盘，鼠标落子，先横、竖或斜向连成 6 子的一方获胜。

![LICENSE](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.13-blue)
![pygame](https://img.shields.io/badge/pygame-2.6.1-yellow)

<!-- 后续可在此插入游戏截图：![gameplay](docs/screenshot.png) -->

## 功能特性

- 19×19 标准棋盘，格子与棋子按 50 px 步长绘制
- 鼠标左键落子，黑白双方自动轮流
- 落子后实时判定横向、竖向、两条斜向的六子连线
- 分出胜负后弹出「游戏结束」提示
- 按空格键立即开局重来
- 中文字体内置（思源宋体），无需额外安装字体

## 规则说明

- 棋盘 19×19，黑棋先行，黑白交替。
- **本版本每回合落 1 子** —— 这是简化实现，并非标准 Connect6 规则。
- 任意一方在横、竖、正斜、反斜四个方向上连成连续的 6 子（或更多）即获胜。
- 标准 Connect6 规则为：黑棋第 1 手只落 1 子，此后双方每回合各落 2 子。该规则尚未实现，后续版本计划补上。

## 环境要求

| 项目 | 要求 |
| --- | --- |
| Python | 3.8 及以上（已在 3.13 上验证） |
| pygame | 2.0 及以上（已验证 2.6.1） |
| 操作系统 | Windows / macOS / Linux |

## 安装与运行

```bash
git clone https://github.com/TroutZun666/Connect6_Python.git
cd Connect6_Python

# 可选：创建虚拟环境
python -m venv .venv
.\.venv\Scripts\activate        # Windows
source .venv/bin/activate       # macOS / Linux

pip install pygame

python main.py
```

> ⚠️ 请在**项目根目录**下运行 `python main.py`。当前字体路径为相对路径 `fonts/...`，从其他目录启动时，胜负提示处的文字渲染会报 `FileNotFoundError`。

## 操作说明

| 操作 | 说明 |
| --- | --- |
| 鼠标左键 | 在棋盘交叉点落子（该位置为空时生效） |
| 空格键 | 重新开始一局 |
| 关闭窗口 | 退出游戏 |

## 项目结构

```
Connect6_Python/
├── main.py                          # 全部游戏逻辑：窗口、棋盘绘制、落子、胜负判定
├── fonts/
│   ├── SourceHanSerifSC-Bold.otf    # 思源宋体（SIL OFL 1.1）
│   └── LICENSE.txt                  # 字体许可证全文
├── LICENSE                          # MIT 许可证
├── README.md
└── .gitignore
```

## 已知限制

- 每回合仅落 1 子，未实现标准 Connect6 的「首手 1 子、之后每回合 2 子」规则。
- 没有 AI 对手，仅支持本地双人对战。
- 无悔棋、计时、计分与平局判定；棋盘下满时不会自动结束。
- 胜负判定用全局状态实现，暂不支持多局对局记录或回放。

## 许可证

本项目包含两种不同许可证的成果：

- **代码**（`main.py` 等）采用 [MIT 许可证](LICENSE)，可自由使用、修改、分发与商用，保留版权声明即可。
- **字体**（`fonts/SourceHanSerifSC-Bold.otf`）采用 [SIL Open Font License 1.1](fonts/LICENSE.txt)，其许可条款独立于 MIT：
  - 字体不可单独出售；
  - 修改后的衍生字体不得继续使用保留字体名 `Source`；
  - 再分发时需附带 `fonts/LICENSE.txt` 中的版权声明与许可全文。

> MIT 许可证不覆盖 `fonts/` 目录下的字体文件。

## 致谢

- [思源宋体 Source Han Serif](https://github.com/adobe-fonts/source-han-serif) —— 界面中文字体
