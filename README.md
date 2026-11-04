# Connect6_Python

用 Python + pygame 实现的六子棋（Connect6）双人对战小游戏，19×19 棋盘，鼠标落子。

![LICENSE](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.13-blue)
![pygame](https://img.shields.io/badge/pygame-2.6.1-yellow)

<!-- 后续可在此插入游戏截图：![gameplay](docs/screenshot.png) -->

## 快速开始

### 方式一：下载即玩（Windows）

1. 打开 [Releases](https://github.com/TroutZun666/Connect6_Python/releases) 页面，下载最新的 `Connect6-*-win64.zip`；
2. 解压到任意目录（路径建议不含中文与空格）；
3. 双击目录中的 `Connect6.exe` 即可开始，无需安装 Python。

> - 不要单独移动 `Connect6.exe`：它依赖同目录下的 `fonts/` 才能显示中文，想放桌面请创建快捷方式。
> - exe 未做代码签名，首次运行可能被 Windows SmartScreen 拦截，点「更多信息 → 仍要运行」即可。

### 方式二：从源码运行

需要 Python 3.8+、pygame 2.0+（已在 Python 3.13 + pygame 2.6.1 上验证）。

```bash
git clone https://github.com/TroutZun666/Connect6_Python.git
cd Connect6_Python

python -m venv .venv
.\.venv\Scripts\activate        # Windows
source .venv/bin/activate       # macOS / Linux

pip install pygame

python main.py
```

> ⚠️ 必须在**项目根目录**执行 `python main.py`。字体使用相对路径 `fonts/...`，从其他目录启动会在渲染胜负提示时抛出 `FileNotFoundError`。

## 操作方式

| 操作 | 说明 |
| --- | --- |
| 鼠标左键 | 在交叉点落子；该点已有棋子或落在棋盘外则无效 |
| 空格 / R | 立即重新开局 |
| 关闭窗口 | 退出游戏 |

## 游戏规则

标准 Connect6 规则：

1. 棋盘 19×19，黑棋先行。
2. **第一手**：黑棋只落 1 子。
3. **此后双方每回合各落 2 子**，落完 2 子才交换行动权。
4. 任意一方在横、竖、正斜、反斜四个方向上连成 **6 子及以上**即获胜；每次落子后都会重新检测。
5. 棋盘被下满且无人连成 6 子时判为平局。

胜负与平局都会让游戏停止并显示「游戏结束」，此时按空格或 R 重开。

## 常见问题

**双击 exe 一闪而过？** 检查是否完整解压（`Connect6.exe` 与 `fonts\`、`_internal\` 同目录），以及是否点了 SmartScreen 的「更多信息 → 仍要运行」。

**提示找不到字体 / 中文显示成方块？** `fonts\SourceHanSerifSC-Bold.otf` 丢失，或 exe 被单独拷贝到了别处；重新解压整包即可。

**能出单文件 exe 吗？** 暂不支持。单文件版需要代码按 `sys._MEIPASS` 查找资源，目前字体路径是相对工作目录的。

**支持 macOS / Linux 吗？** 源码可以在这些平台运行，但需要自行安装 pygame 并打包；仓库只提供 Windows 构建。

## 项目结构

```
Connect6_Python/
├── main.py                          # 全部逻辑：窗口、棋盘绘制、落子、胜负与平局判定
├── fonts/
│   ├── SourceHanSerifSC-Bold.otf    # 思源宋体（SIL OFL 1.1）
│   └── LICENSE.txt                  # 字体许可证全文
├── LICENSE                          # MIT 许可证
├── README.md
└── .gitignore
```

## 开发与打包

逻辑集中在 `main.py` 一个文件，改完直接 `python main.py` 测试。打包 Windows 可执行文件（项目根目录、已激活虚拟环境）：

```powershell
pip install "pyinstaller>=6.11"

pyinstaller --noconfirm --clean --windowed --name Connect6 `
  --add-data "fonts;fonts" `
  --add-data "LICENSE;." `
  main.py
```

产物是完整的 `dist\Connect6\` 目录（`build/`、`dist/`、`*.spec` 已在 `.gitignore` 中忽略）。发布时压缩整个目录上传，并保留 `fonts/LICENSE.txt` —— 分发字体时附带许可证是 SIL OFL 的要求。

## 已知限制

- 无 AI 对手，仅支持本地双人对战。
- 结束画面只显示「游戏结束」，不提示获胜方。
- 无悔棋、计时、计分与对局回放。
- 字体路径为相对路径，从其他目录启动或单独移动 exe 会导致赢棋时闪退。
- 仅提供目录版 exe，暂无单文件版。

## 许可证

本项目包含两种不同许可证的成果：

- **代码**（`main.py` 等）采用 [MIT 许可证](LICENSE)，可自由使用、修改、分发与商用，保留版权声明即可。
- **字体**（`fonts/SourceHanSerifSC-Bold.otf`）采用 [SIL Open Font License 1.1](fonts/LICENSE.txt)，条款独立于 MIT：
  - 字体不可单独出售；
  - 修改后的衍生字体不得继续使用保留字体名 `Source`；
  - 再分发时需附带 `fonts/LICENSE.txt` 中的版权声明与许可全文。

> MIT 许可证不覆盖 `fonts/` 目录下的字体文件。

## 致谢

- [pygame](https://www.pygame.org/) —— 图形与事件处理
- [思源宋体 Source Han Serif](https://github.com/adobe-fonts/source-han-serif) —— 界面中文字体
