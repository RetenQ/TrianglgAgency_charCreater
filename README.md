# 🎭 Triangle Agency Character Creator (三角机构角色卡生成器)

欢迎使用 **Triangle Agency Character Creator**！这是一个专为 TRPG 游戏《三角机构》(Triangle Agency) 设计的角色卡制作工具。轻松创建出精美、规范的角色卡片！✨

## ✨ 主要功能 (Features)

*   **📝 简易表单填写**: 通过直观的图形界面 (GUI) 填写角色的各项信息，告别繁琐的手动排版。
*   **🤖 自动化数据填充**: 选择“异常体”、“现实”或“职能”后，系统会自动从数据中加载相关描述、能力和问答题，省时省力！🚀
*   **🖼️ 头像支持**: 一键上传角色立绘，让你的特工形象更加生动。
*   **🖨️ 多格式输出**: 
    *   **HTML**: 生成交互式的网页版角色卡，支持勾选和填写。
    *   **PDF**: 自动调用 Microsoft Edge 生成高质量的打印版 PDF，方便跑团使用。📄
    *   **JSON**: 保存角色数据，随时重新加载修改。💾
*   **📦 便携运行**: 提供打包好的 `.exe` 可执行文件，无需安装 Python 环境，开箱即用！

## 🚀 快速开始 (Getting Started)

### 使用可执行文件 (推荐)

1.  进入 `release` 文件夹。
2.  双击运行 `RoleCardEditor.exe`。
3.  在弹出的窗口中填写角色信息。
    *   **Page 1 (档案)**: 填写基本资料、属性值、异能资质等。
    *   **Page 2 (调查)**: 填写触发器、指令、许可行为及问答。
4.  点击底部的 **"💾 保存并生成 (Save & Sync)"** 按钮。
5.  生成的角色卡文件将保存在 `output` 文件夹中。📂


## 📁 目录结构 (Directory Structure)

*   `release/`: 存放打包好的 `.exe` 程序。
*   `output/`: 默认的角色卡输出目录。
*   `ARC_setting/`: 包含异常体，现实，职能的数据的 JSON 文件，可以手动修改以达到自定义的目的！
*   `codeFile/`: 源代码目录。
    *   `json_form_gui.py`: 主程序 GUI 逻辑。
    *   `json_to_html.py`: HTML 生成核心逻辑。
    *   `template.html`: 角色卡 HTML 模板。
---

祝你的特工在三角机构的任务中好运！机构感谢您！🔺🕶️
