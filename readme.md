# Manim自适应布局系统与中文补丁

[![PyPI version](https://img.shields.io/badge/pip-v0.1.0-blue.svg)](https://pypi.org/project/manim-adaptive-layout/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 简介

Manim自适应布局系统是一个专为[Manim](https://github.com/ManimCommunity/manim)动画引擎设计的布局管理工具，解决了在不同屏幕比例下（如抖音竖屏、小红书方屏等）内容排版的问题。

本系统提供了一套全面的布局管理功能，确保您的动画内容在任何屏幕比例下都能正确显示，特别优化了长文本处理和元素自动排列功能。

此外，本项目还包含一个独立的Manim中文补丁工具包，可以让Manim完美支持中文和数学公式混合显示，无需额外配置。

## 主要特性

### 自适应布局系统

- **安全区域管理**：自动创建适合不同平台的安全区域，防止内容超出屏幕
- **超长文本处理**：自动换行、缩放、分页显示和滚动显示
- **自适应排列**：防止元素重叠，自动调整位置
- **响应式网格**：创建自适应的网格布局，支持等高行
- **平台优化**：针对抖音、小红书等平台预设屏幕比例
- **文本高亮**：突出显示文本中的关键词
- **文本滚动**：创建平滑的文本滚动动画

### 中文补丁工具包

- **全自动中文支持**：无需额外配置，直接在Manim中使用中文
- **中文与数学公式混合**：在同一个对象中混合使用中文和LaTeX公式
- **零代码自动加载**：可配置为自动加载，无需在代码中导入
- **兼容所有Manim类**：对Text、Tex、MathTex等所有类提供中文支持

## 安装

### 自适应布局系统

```bash
pip install manim-adaptive-layout
```

### 中文补丁工具包

中文补丁工具包作为独立组件提供，您可以通过以下步骤安装：

#### 方法1: 零代码自动加载（推荐）

1. 将 `sitecustomize.py` 文件复制到以下位置之一:
   - Python的site-packages目录（全局生效）
   - 您的Manim项目根目录（仅对该项目生效）

2. 将 `patch` 目录复制到与 `sitecustomize.py` 相同的目录中

3. 无需任何导入语句，直接使用Manim，中文补丁将自动加载

#### 方法2: 手动导入

1. 将 `patch` 目录复制到您的Manim项目中

2. 在您的Manim脚本开头添加:
   ```python
   from patch.auto_chinese_patch import *
   ```

## 快速开始

### 自适应布局系统

#### 方法1：直接导入使用（推荐）

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

#### 方法2：无需导入，直接使用（全局可用）

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

### 中文补丁工具包

#### 零代码自动加载（推荐）

安装后，无需任何导入语句，直接使用Manim，所有类都将自动支持中文：

```python
from manim import *

class ChineseExample(Scene):
    def construct(self):
        # 直接使用Text显示中文
        text = Text("你好，世界！")
        self.play(Write(text))
        
        # 直接使用MathTex显示中文和数学公式混合内容
        formula = MathTex("勾股定理：$a^2 + b^2 = c^2$")
        formula.next_to(text, DOWN)
        self.play(Write(formula))
        
        # 直接使用Tex显示中文和LaTeX混合内容
        tex = Tex("爱因斯坦：$E = mc^2$")
        tex.next_to(formula, DOWN)
        self.play(Write(tex))
```

#### 手动导入

```python
from manim import *
# 导入中文补丁
from patch.auto_chinese_patch import *

class ChineseExample(Scene):
    def construct(self):
        # 所有Manim类现在都支持中文
        text = Text("你好，世界！")
        formula = MathTex("勾股定理：$a^2 + b^2 = c^2$")
        
        self.play(Write(text))
        self.play(Write(formula))
```

## 详细文档

更多详细功能和使用示例，请查看 [完整文档](manim_adaptive_layout/README.md)。

## 示例

### 自适应布局系统示例

项目包含多个示例脚本，展示了不同功能的使用方法：

- 基础示例：`manim_adaptive_layout/examples/basic_example.py`
- 高级示例：`manim_adaptive_layout/examples/advanced_example.py`
- 屏幕比例示例：`manim_adaptive_layout/examples/screen_ratio_example.py`
- 直接使用示例：`manim_adaptive_layout/examples/direct_use_example.py`

### 中文补丁示例

中文补丁工具包包含以下示例：

- 快速入门：`patch/examples/quickstart.py`
- 简单中文：`patch/examples/simple_chinese.py`
- 自动加载测试：`patch/examples/auto_load_test.py`
- 中文数学示例：`patch/examples/chinese_math_examples.py`
- 自动补丁演示：`patch/examples/auto_patch_demo.py`

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

## 贡献

欢迎提交问题和改进建议！

## 许可

[MIT](manim_adaptive_layout/LICENSE)