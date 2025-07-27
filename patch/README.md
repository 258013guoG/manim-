# Manim 中文支持工具集

这个工具集提供了在 Manim 动画库中显示中文文本和数学公式的完整解决方案。

## 最新版本：零代码自动加载补丁

我们现在提供了零代码自动加载补丁，它可以：

- **完全零代码**：无需任何导入语句，自动加载
- **适合非程序员**：完全不需要编程知识
- **全自动识别**：只在Manim项目中激活
- **支持所有中文和符号**：自动处理各种混合情况
- **智能处理**：自动识别内容类型，选择最佳渲染方式

## 全自动补丁增强版

我们还提供了全自动补丁增强版，它可以：

- **无需导入特殊类**：直接使用原生Manim类（Text、MathTex、Tex等）
- **无需继承**：不需要继承特殊类，直接编码即可
- **支持所有中文和符号**：自动处理各种混合情况，包括中文、数学公式、特殊符号等
- **零配置**：导入一次，永久生效，随意编码都不会出错
- **智能处理**：自动识别内容类型，选择最佳渲染方式

## 问题背景

Manim 使用 LaTeX 渲染数学公式，但默认情况下 LaTeX 不支持中文，导致含有中文的数学公式无法正确显示。

## 解决方案

本工具集提供了三个主要类来解决这个问题：

1. `ChineseText`: 默认使用中文字体的文本类
2. `ChineseMath`: 能够同时处理中文和数学公式的混合类
3. `ChineseTex`: 尝试使用 CTEX 模板渲染中文，失败则回退到 `ChineseMath`

## 使用方法

### 方法零：零代码自动加载（最推荐）

只需将 `sitecustomize.py` 文件复制到项目根目录，无需任何导入语句：

```python
# 完全不需要导入任何补丁！
from manim import *

class MyScene(Scene):
    def construct(self):
        # 直接使用Text显示中文
        text = Text("你好，世界！")
        self.play(Write(text))
        
        # 直接使用MathTex显示中文和数学公式混合内容
        formula = MathTex("勾股定理：$a^2 + b^2 = c^2$")
        formula.next_to(text, DOWN)
        self.play(Write(formula))
```

这种方法适合：
- 不懂编程的用户
- 希望完全零配置的用户
- 不想每次都添加导入语句的用户

### 方法一：全自动补丁增强版（推荐）

只需在脚本开头导入一次：

```python
import patch.auto_chinese_patch
```

之后就可以直接使用所有原生Manim类，它们都将自动支持中文：

```python
from manim import *
import patch.auto_chinese_patch

class MyScene(Scene):
    def construct(self):
        # 直接使用Text显示中文
        text = Text("你好，世界！")
        self.play(Write(text))
        
        # 直接使用MathTex显示中文和数学公式混合内容
        formula = MathTex("勾股定理：$a^2 + b^2 = c^2$")
        formula.next_to(text, DOWN)
        self.play(Write(formula))
```

### 方法二：使用专用类

如果你希望更明确地控制中文渲染，可以使用专用类：

```python
from patch import ChineseText, ChineseMath, ChineseTex
```

导入时会自动应用补丁，设置 `Text` 类的默认字体为中文字体。

### 方法三：手动应用补丁

如果不希望自动应用补丁，可以这样导入：

```python
from patch.manim_chinese_utils import ChineseText, ChineseMath, ChineseTex, apply_chinese_patch

# 手动应用补丁
apply_chinese_patch()
```

### 使用示例

```python
from manim import *
from patch import ChineseText, ChineseMath

class PythagoreanTheoremDemo(Scene):
    def construct(self):
        # 使用 ChineseText 显示纯中文
        title = ChineseText("勾股定理演示", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 使用 ChineseMath 显示中文和数学公式混合内容
        formula = ChineseMath(r"在直角三角形中，直角边 $a$、$b$ 和斜边 $c$ 满足：$a^2 + b^2 = c^2$")
        self.play(Write(formula))
        
        self.wait(2)
```

## 示例文件

### 零代码自动加载示例

查看 `examples/auto_load_test.py` 文件，这是一个零代码自动加载的示例：

```bash
python -m manim patch/examples/auto_load_test.py AutoLoadTest -pql
```

### 全自动补丁增强版示例

#### 快速入门示例

查看 `examples/quickstart.py` 文件，这是一个最简单的入门示例：

```bash
python -m manim patch/examples/quickstart.py QuickStartDemo -pql
```

#### 完整功能示例

查看 `examples/auto_patch_demo.py` 文件，展示了全自动补丁增强版的所有功能：

```bash
python -m manim patch/examples/auto_patch_demo.py AutoPatchDemo -pql
```

### 专用类示例

查看 `examples/chinese_math_examples.py` 文件，其中包含了三个使用专用类的完整示例：

1. 勾股定理演示 (`PythagoreanTheoremDemo`)
2. 圆周率演示 (`PiDemonstration`)
3. 欧拉公式演示 (`EulerFormulaDemo`)

运行示例：

```bash
python -m manim patch/examples/chinese_math_examples.py PythagoreanTheoremDemo -pql
```

### 简单示例

查看 `examples/simple_chinese.py` 文件，展示了最简单的中文支持方法：

```bash
python -m manim patch/examples/simple_chinese.py SimpleChineseScene -pql
```

## 推荐字体

以下是一些推荐的中文字体：

- SimHei (黑体)
- SimSun (宋体)
- KaiTi (楷体)
- FangSong (仿宋)
- Microsoft YaHei (微软雅黑)
- DyMeansHappy (抖音美好体)

## 技术原理

### 专用类的工作原理

专用类（`ChineseText`、`ChineseMath`、`ChineseTex`）的核心原理是：

1. 使用正则表达式分离中文和数学公式部分
2. 中文部分使用 `Text` 类渲染
3. 数学公式部分使用 `MathTex` 类渲染
4. 将两部分组合成一个 `VGroup`

这样既保证了中文的正确显示，又不影响数学公式的渲染效果。

### 零代码自动加载补丁的工作原理

零代码自动加载补丁（`sitecustomize.py`）采用了Python的站点自定义机制：

1. **Python启动机制**：Python在启动时会自动导入`sitecustomize`模块
2. **自动检测**：补丁会检测当前环境是否为Manim项目
3. **条件激活**：只在Manim环境中自动加载中文补丁
4. **透明集成**：用户完全无感知，不需要任何代码修改

这种方法使得用户可以完全零代码使用中文支持，特别适合不懂编程的用户。

### 全自动补丁增强版的工作原理

全自动补丁增强版（`auto_chinese_patch`）采用了更先进的方法：

1. **猴子补丁技术**：通过替换原生Manim类的初始化方法，使其自动支持中文
2. **智能内容识别**：自动检测内容中是否包含中文
3. **多级回退机制**：
   - 对于 `Tex` 类，首先尝试使用CTEX模板渲染
   - 如果失败，则回退到分离中文和LaTeX的方法
   - 如果再次失败，则使用 `Text` 类渲染
4. **无缝集成**：修改后的类保持与原始类相同的接口，用户无需改变使用习惯

这种方法使得用户可以直接使用原生Manim类（`Text`、`MathTex`、`Tex`等），而无需关心中文渲染的细节。

## 注意事项

### 零代码自动加载补丁注意事项

1. `sitecustomize.py` 文件必须放在项目根目录或Python能够找到的路径中
2. 如果系统中已有其他 `sitecustomize.py` 文件，可能会产生冲突
3. 在某些特殊环境下（如虚拟环境），可能需要额外配置
4. 这种方法会全局影响所有Python程序，但我们已经添加了检测机制，只在Manim项目中激活

### 全自动补丁增强版注意事项

1. 导入 `patch.auto_chinese_patch` 应该在导入其他Manim类之后进行，以确保补丁能正确应用
2. 全自动补丁会修改原生Manim类的行为，如果项目中有其他修改这些类的代码，可能会产生冲突
3. 对于极其复杂的混合内容，可能需要手动调整排版

### 专用类注意事项

1. 如果使用 `ChineseTex` 类，需要确保系统中安装了支持中文的 LaTeX 环境
2. 在 Windows 系统中，推荐使用 SimHei (黑体) 或 Microsoft YaHei (微软雅黑) 字体
3. 在 Linux 系统中，可能需要安装额外的中文字体包

### 通用注意事项

1. 如果遇到字体问题，可以尝试安装更多中文字体或修改默认字体
2. 对于特别复杂的数学公式，建议将中文和数学部分分开编写
3. 本工具集主要解决中文显示问题，对于其他非拉丁文字（如日文、韩文等）也有一定支持