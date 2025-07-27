# Manim 自适应布局系统使用指南

## 简介

`AdaptiveLayoutSystem` 是一个专为 Manim 动画库设计的自适应布局系统，提供全面的布局管理功能，确保内容在不同屏幕比例下正确显示。该系统特别优化了长文本处理和元素自动排列功能，适用于抖音、小红书等竖屏平台的动画制作。

## 主要特性

- **安全区域管理**：自动创建安全区域，确保内容不会超出屏幕边界
- **超长文本处理**：自动换行、缩放和分页显示超长文本
- **自适应排列**：防止元素重叠，自动调整位置
- **响应式网格**：创建自适应的网格布局
- **平台优化**：针对抖音、小红书等平台的特定比例和元素优化
- **文本高亮**：支持关键词高亮和动画效果
- **文本滚动**：支持长文本滚动动画

## 安装和导入

将 `adaptive_layout_system.py` 文件放在你的 Manim 项目目录中，然后在你的脚本中导入：

```python
from adaptive_layout_system import AdaptiveLayoutSystem
```

## 使用方法

### 1. 创建平台优化布局

```python
class MyScene(Scene):
    def construct(self):
        # 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 添加平台特定元素（水印、互动提示等）
        AdaptiveLayoutSystem.add_platform_elements(self, platform="tiktok", username="@你的用户名")
```

### 2. 处理超长文本

#### 2.1 自动换行和缩放

```python
# 创建自适应段落
text = AdaptiveLayoutSystem.create_adaptive_paragraph(
    "这是一段很长的文本内容...",
    max_width=safe_width * 0.9,  # 使用安全区域宽度的90%
    max_height=safe_height * 0.7,  # 可选：限制最大高度
    font_size=32,  # 初始字体大小
    min_font_size=24,  # 最小字体大小
    line_spacing=1.2,  # 行间距
    align="left"  # 对齐方式：left, center, right
)
```

#### 2.2 分页显示超长文本

```python
# 创建分页文本
pages = AdaptiveLayoutSystem.split_long_text_into_pages(
    long_text_content, 
    max_width=safe_width * 0.9,
    max_height=safe_height * 0.7,
    font_size=32,
    min_font_size=24,
    line_spacing=1.2
)

# 逐页显示
current_page = None
for i, page in enumerate(pages):
    if current_page:
        self.play(FadeOut(current_page))
    
    page.next_to(title, DOWN, buff=0.8)
    self.play(FadeIn(page))
    current_page = page
    self.wait(1.5)
```

#### 2.3 滚动显示超长文本

```python
# 创建一个大文本对象
scrolling_text = AdaptiveLayoutSystem.auto_wrap_text(
    long_text_content,
    max_width=safe_width * 0.9,
    font_size=28,
    line_spacing=1.2
)

# 设置初始位置
scrolling_text.next_to(title, DOWN, buff=0.8)

# 显示文本
self.play(FadeIn(scrolling_text))

# 滚动动画
AdaptiveLayoutSystem.create_scrolling_text(
    self, scrolling_text, scroll_time=5, direction=UP, distance_factor=0.8
)
```

#### 2.4 高亮关键词

```python
# 创建文本
text = AdaptiveLayoutSystem.create_adaptive_paragraph(
    "这是一段包含关键词的文本内容...",
    max_width=safe_width * 0.9,
    font_size=32
)

# 高亮关键词
keywords = ["关键词1", "关键词2", "关键词3"]
AdaptiveLayoutSystem.highlight_text_parts(
    self, text, keywords, color=YELLOW, animation_per_part=True, run_time=0.7
)
```

### 3. 防止元素重叠

```python
# 创建多个对象
objects = [Circle(), Square(), Triangle()]

# 防止重叠，自动排列
arranged_objects = AdaptiveLayoutSystem.prevent_overlap(
    objects, direction=DOWN, min_buff=0.3, fix_first=True
)
```

### 4. 创建响应式网格

```python
# 创建多个对象
objects = [Circle(), Square(), Triangle(), Star(), RegularPolygon(5)]

# 创建响应式网格
grid = AdaptiveLayoutSystem.create_responsive_grid(
    objects,
    n_cols=3,  # 列数
    h_buff=0.5,  # 水平间距
    v_buff=0.5,  # 垂直间距
    max_width=safe_width * 0.9,  # 最大宽度
    equal_heights=True  # 是否使所有行高度相等
)
```

### 5. 带标题的内容排列

```python
# 创建标题和内容对
title_content_pairs = [
    (Text("第一部分", color=BLUE), Text("这是第一部分的内容...")),
    (Text("第二部分", color=GREEN), Text("这是第二部分的内容...")),
    (Text("第三部分", color=RED), Text("这是第三部分的内容..."))
]

# 自动排列带标题的内容
sections = AdaptiveLayoutSystem.auto_arrange_with_titles(
    title_content_pairs,
    direction=DOWN,  # 排列方向
    title_scale=1.2,  # 标题相对于内容的缩放比例
    content_buff=0.3,  # 标题与内容之间的间距
    section_buff=1.0,  # 各部分之间的间距
    max_width=safe_width * 0.9  # 最大宽度
)
```

## 完整示例

```python
from manim import *
from adaptive_layout_system import AdaptiveLayoutSystem

class AdaptiveLayoutDemo(Scene):
    def construct(self):
        # 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 创建标题
        title = Text("自适应布局演示", font_size=48, color=BLUE)
        title.to_edge(UP, buff=1)
        self.play(Write(title))
        
        # 创建长文本
        text_content = "这是一段较长的文本内容，用于演示自适应布局系统的文本处理能力。系统会自动处理换行、缩放和对齐等问题，确保文本在不同屏幕比例下都能正确显示。"
        
        text = AdaptiveLayoutSystem.create_adaptive_paragraph(
            text_content,
            max_width=safe_width * 0.9,
            font_size=32,
            min_font_size=24,
            line_spacing=1.2
        )
        text.next_to(title, DOWN, buff=0.8)
        
        self.play(FadeIn(text))
        self.wait(1)
        
        # 创建几何图形
        circle = Circle(radius=1, color=RED)
        square = Square(side_length=2, color=GREEN)
        triangle = Triangle(color=BLUE)
        
        # 防止重叠，自动排列
        shapes = AdaptiveLayoutSystem.prevent_overlap(
            [circle, square, triangle], direction=RIGHT, min_buff=0.5
        )
        shapes.next_to(text, DOWN, buff=1)
        
        self.play(Create(shapes))
        self.wait(1)
        
        # 添加平台元素
        AdaptiveLayoutSystem.add_platform_elements(self, platform="tiktok", username="@数学动画")
        
        self.wait(2)
```

## 适配不同平台

### 抖音（竖屏 9:16）

```python
safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
    self, platform="tiktok", show_safe_zone=True
)
```

### 小红书（竖屏 3:4）

```python
safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
    self, platform="xiaohongshu", show_safe_zone=True
)
```

### 自定义比例

如果需要自定义屏幕比例，可以直接设置 config 参数后创建安全区域：

```python
# 自定义屏幕比例
config.frame_width = 12
config.frame_height = 9
config.pixel_width = 1440
config.pixel_height = 1080

# 创建安全区域
safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_safe_zone(
    self, margin=0.8, visible=True
)
```

## 最佳实践

1. **始终使用安全区域**：确保所有重要内容都在安全区域内，避免内容被裁剪
2. **自适应文本处理**：对于长文本，使用自动换行和缩放功能，或考虑分页/滚动显示
3. **防止元素重叠**：使用 `prevent_overlap` 方法确保元素之间有足够的间距
4. **响应式设计**：使用相对尺寸（如 `safe_width * 0.9`）而不是固定尺寸
5. **平台优化**：根据目标平台（抖音/小红书）选择适当的屏幕比例和元素

## 注意事项

- 对于非常复杂的布局，可能需要手动调整一些参数
- 文本分页功能适用于静态展示，如果需要动态效果，考虑使用滚动文本
- 在高分辨率渲染时，确保字体大小足够大以保证可读性

## 渲染命令

```bash
manim -pql your_script.py YourScene
```

如果需要高质量渲染：

```bash
manim -pqh your_script.py YourScene
```