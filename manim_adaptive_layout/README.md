# Manim自适应布局系统

[![PyPI version](https://img.shields.io/badge/pip-v0.1.0-blue.svg)](https://pypi.org/project/manim-adaptive-layout/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 简介

Manim自适应布局系统是一个专为[Manim](https://github.com/ManimCommunity/manim)动画引擎设计的布局管理工具，解决了在不同屏幕比例下（如抖音竖屏、小红书方屏等）内容排版的问题。

本系统提供了一套全面的布局管理功能，确保您的动画内容在任何屏幕比例下都能正确显示，特别优化了长文本处理和元素自动排列功能。

## 主要特性

- **安全区域管理**：自动创建适合不同平台的安全区域，防止内容超出屏幕
- **超长文本处理**：自动换行、缩放、分页显示和滚动显示
- **自适应排列**：防止元素重叠，自动调整位置
- **响应式网格**：创建自适应的网格布局，支持等高行
- **平台优化**：针对抖音、小红书等平台预设屏幕比例
- **文本高亮**：突出显示文本中的关键词
- **文本滚动**：创建平滑的文本滚动动画

## 安装

```bash
pip install manim-adaptive-layout
```

## 快速开始

### 方法1：直接导入使用（推荐）

```python
from manim import *
from manim_adaptive_layout import AdaptiveLayoutSystem

class MyScene(Scene):
    def construct(self):
        # 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 创建自适应文本
        text = AdaptiveLayoutSystem.create_adaptive_paragraph(
            "这是一段自动换行和缩放的文本，可以适应不同屏幕比例。", 
            max_width=safe_width, 
            max_height=safe_height/2
        )
        
        self.add(text)
```

### 方法2：无需导入，直接使用（全局可用）

安装后，系统会自动将`AdaptiveLayoutSystem`类注册到Manim全局命名空间，您可以直接使用：

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # 直接使用AdaptiveLayoutSystem，无需导入
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 创建自适应文本
        text = AdaptiveLayoutSystem.create_adaptive_paragraph(
            "这是一段自动换行和缩放的文本，可以适应不同屏幕比例。", 
            max_width=safe_width, 
            max_height=safe_height/2
        )
        
        self.add(text)
```

## 详细功能

### 1. 创建平台优化布局

```python
safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
    self, platform="tiktok", show_safe_zone=True
)
```

支持的平台：
- `"tiktok"`: 抖音竖屏 (9:16)
- `"xiaohongshu"`: 小红书 (3:4)
- 默认: 标准横屏 (16:9)

### 2. 处理超长文本

#### 自动换行和缩放

```python
text = AdaptiveLayoutSystem.create_adaptive_paragraph(
    "这是一段长文本...", 
    max_width=safe_width, 
    max_height=safe_height/2,
    font_size=36,
    min_font_size=24
)
```

#### 分页显示

```python
pages = AdaptiveLayoutSystem.split_long_text_into_pages(
    "这是一段非常长的文本，需要分页显示...",
    max_width=safe_width,
    max_height=safe_height*0.8
)

# 显示第一页
self.add(pages[0])
```

#### 滚动显示

```python
long_text = AdaptiveLayoutSystem.auto_wrap_text(
    "这是一段需要滚动显示的长文本...",
    max_width=safe_width
)

self.add(long_text)

# 创建滚动动画
AdaptiveLayoutSystem.create_scrolling_text(
    self, long_text, scroll_time=5, direction=UP
)
```

### 3. 防止元素重叠

```python
# 创建多个几何图形
shapes = [Circle(), Square(), Triangle()]

# 水平排列，防止重叠
arranged_shapes = AdaptiveLayoutSystem.prevent_overlap(
    shapes, direction=RIGHT, min_buff=0.5
)

self.add(arranged_shapes)
```

### 4. 创建响应式网格

```python
# 创建多个元素
elements = [Text(f"元素{i}") for i in range(9)]

# 创建3列网格
grid = AdaptiveLayoutSystem.create_responsive_grid(
    elements, n_cols=3, h_buff=0.5, v_buff=0.5,
    max_width=safe_width, equal_heights=True
)

self.add(grid)
```

### 5. 添加平台特定元素

```python
# 添加水印和互动提示
elements = AdaptiveLayoutSystem.add_platform_elements(
    self, platform="tiktok", username="@数学动画"
)
```

## 渲染命令

为了确保正确的屏幕比例，请使用以下命令渲染，**必须**指定正确的分辨率参数：

### 抖音竖屏 (9:16)

```bash
manim -pql --resolution=1080,1920 your_script.py YourScene
```

### 小红书 (3:4)

```bash
manim -pql --resolution=1080,1440 your_script.py YourScene
```

### 标准横屏 (16:9)

```bash
manim -pql --resolution=1920,1080 your_script.py YourScene
```

> **重要提示**：必须使用`--resolution`参数指定正确的分辨率，否则可能导致屏幕比例不正确，内容被挤压变形。即使使用了`create_platform_optimized_layout`方法设置了平台，也需要在渲染命令中指定对应的分辨率。

## 贡献

欢迎提交问题和改进建议！

## 许可

[MIT](LICENSE)