# Manim 布局工具使用指南

## 简介

`manim_layout_utils.py` 是一个专为 Manim 动画库设计的布局工具类，旨在解决以下常见问题：

1. 确保内容在安全区域内，不超出屏幕边界
2. 防止元素重叠
3. 自动调整文本大小和换行
4. 创建响应式网格布局
5. 根据内容自动计算合适的边距

## 安装和导入

将 `manim_layout_utils.py` 文件放在你的项目目录中，然后在你的 Manim 脚本中导入：

```python
# 导入布局工具类
from manim_layout_utils import LayoutUtils
```

## 主要功能

### 1. 创建安全区域

```python
safe_zone, safe_width, safe_height = LayoutUtils.create_safe_zone(self, margin=1.0, show_border=True, show_label=True)
```

**参数说明：**
- `scene`: Manim 场景对象
- `margin`: 边距大小（默认为 1.0）
- `show_border`: 是否显示边界（默认为 True）
- `show_label`: 是否显示标签（默认为 True）

**返回值：**
- `safe_zone`: 安全区域矩形对象
- `safe_width`: 安全区域宽度
- `safe_height`: 安全区域高度

### 2. 自动排列对象

```python
arranged_group = LayoutUtils.auto_arrange(mobjects, direction=RIGHT, buff=0.5, safe_width=None, safe_height=None)
```

**参数说明：**
- `mobjects`: 要排列的对象或对象组
- `direction`: 排列方向（默认为 RIGHT）
- `buff`: 对象间距（默认为 0.5）
- `safe_width`: 安全区域宽度（可选）
- `safe_height`: 安全区域高度（可选）

**返回值：**
- `arranged_group`: 排列后的对象组

### 3. 自动计算边距

```python
margin = LayoutUtils.auto_margin(mobject, container_width, container_height, min_margin=0.5)
```

**参数说明：**
- `mobject`: Manim 对象
- `container_width`: 容器宽度
- `container_height`: 容器高度
- `min_margin`: 最小边距（默认为 0.5）

**返回值：**
- `margin`: 计算出的边距

### 4. 自动调整文本大小

```python
adjusted_text = LayoutUtils.fit_text_to_width(text_obj, max_width, min_font_size=24)
```

**参数说明：**
- `text_obj`: 文本对象
- `max_width`: 最大宽度
- `min_font_size`: 最小字体大小（默认为 24）

**返回值：**
- `text_obj`: 调整后的文本对象

### 5. 自动换行文本

```python
wrapped_text = LayoutUtils.auto_wrap_text(text_obj, max_width, font_size=None)
```

**参数说明：**
- `text_obj`: 文本对象
- `max_width`: 最大宽度
- `font_size`: 字体大小（可选）

**返回值：**
- `wrapped_text`: 换行后的文本对象组

### 6. 防止对象重叠

```python
non_overlapping_group = LayoutUtils.prevent_overlap(mobjects, direction=DOWN, min_buff=0.5)
```

**参数说明：**
- `mobjects`: 要排列的对象列表
- `direction`: 排列方向（默认为 DOWN）
- `min_buff`: 最小间距（默认为 0.5）

**返回值：**
- `VGroup`: 排列后的对象组

### 7. 创建响应式网格布局

```python
grid = LayoutUtils.create_responsive_grid(mobjects, n_cols, safe_width, safe_height, h_buff=0.5, v_buff=0.5)
```

**参数说明：**
- `mobjects`: 要排列的对象列表
- `n_cols`: 列数
- `safe_width`: 安全区域宽度
- `safe_height`: 安全区域高度
- `h_buff`: 水平间距（默认为 0.5）
- `v_buff`: 垂直间距（默认为 0.5）

**返回值：**
- `grid`: 网格布局对象组

## 使用示例

```python
from manim import *
from manim_layout_utils import LayoutUtils

class MyScene(Scene):
    def construct(self):
        # 创建安全区域
        safe_zone, safe_width, safe_height = LayoutUtils.create_safe_zone(self)
        
        # 创建标题
        title = Text("自适应布局示例", font_size=48)
        subtitle = Text("使用LayoutUtils工具类", font_size=36)
        
        # 自动排列并确保在安全区域内
        title_group = LayoutUtils.auto_arrange(
            [title, subtitle], 
            direction=DOWN, 
            buff=0.5, 
            safe_width=safe_width, 
            safe_height=safe_height
        )
        title_group.to_edge(UP, buff=1.5)
        
        self.play(Write(title_group))
        
        # 创建一个长文本
        long_text = "这是一段很长的文本内容，在不同屏幕尺寸下可能会超出屏幕边界。"
        text_obj = Text(long_text, font_size=36)
        
        # 自动调整文本大小
        adjusted_text = LayoutUtils.fit_text_to_width(text_obj, safe_width * 0.9)
        adjusted_text.next_to(title_group, DOWN, buff=1)
        
        self.play(FadeIn(adjusted_text))
        
        # 创建一些形状
        shapes = [Square(), Circle(), Triangle()]
        for shape in shapes:
            shape.set_color(BLUE)
            shape.set_fill(BLUE, opacity=0.5)
        
        # 创建响应式网格
        grid = LayoutUtils.create_responsive_grid(
            shapes, 
            n_cols=3, 
            safe_width=safe_width, 
            safe_height=safe_height
        )
        grid.next_to(adjusted_text, DOWN, buff=1)
        
        self.play(FadeIn(grid))
```

## 最佳实践

1. 始终在场景开始时创建安全区域，并使用返回的 `safe_width` 和 `safe_height` 作为后续布局的参考
2. 对于文本内容，使用 `fit_text_to_width` 或 `auto_wrap_text` 确保不超出安全区域
3. 使用 `auto_arrange` 和 `prevent_overlap` 防止元素重叠
4. 对于多个元素的排列，考虑使用 `create_responsive_grid` 创建网格布局
5. 使用 `auto_margin` 根据内容大小自动计算合适的边距

## 注意事项

1. 安全区域的大小取决于 `margin` 参数，可以根据需要调整
2. 文本自动换行功能是基于估算的字符宽度实现的，可能需要根据具体字体进行调整
3. 在使用 `prevent_overlap` 时，确保对象已经有初始位置
4. 响应式网格布局会自动缩放对象以适应网格，如果不希望对象被缩放，可以预先调整对象大小

## 示例脚本

查看 `layout_utils_demo.py` 和 `safe_zone_demo.py` 获取更多使用示例。