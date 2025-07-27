# Manim 自适应布局渲染工具安装指南

## 安装步骤

1. 确保已安装 Python 3.7 或更高版本

2. 克隆或下载本仓库

3. 进入项目根目录

   ```bash
   cd manim_adaptive_layout
   ```

4. 安装包（开发模式）

   ```bash
   pip install -e .
   ```

5. 验证安装

   ```bash
   manim-render --help
   ```

## 快速开始

### 使用命令行工具

```bash
manim-render examples/render_tool_example.py TiktokExample -pql
```

这个命令会：

1. 自动检测 `TiktokExample` 场景中的平台设置（抖音竖屏 9:16）
2. 生成正确的渲染命令，包含 `--resolution=1080,1920` 参数
3. 执行渲染命令，确保输出视频具有正确的屏幕比例

### 在自己的项目中使用

1. 在场景中使用 `AdaptiveLayoutSystem.create_platform_optimized_layout` 方法设置平台

   ```python
   from manim import *
   from manim_adaptive_layout import AdaptiveLayoutSystem
   
   class MyScene(Scene):
       def construct(self):
           # 设置抖音竖屏比例
           safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
               self, platform="tiktok", show_safe_zone=True
           )
           
           # 添加内容...
   ```

2. 使用渲染工具渲染场景

   ```bash
   manim-render my_file.py MyScene -pql
   ```

## 更多信息

详细使用说明请参考 [README_RENDER_TOOL.md](README_RENDER_TOOL.md)。