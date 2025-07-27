# -*- coding: utf-8 -*-
"""
Manim自适应布局系统基础示例

演示了如何使用自适应布局系统的基本功能

渲染命令：
    抖音竖屏: manim -pql --resolution=1080,1920 basic_example.py BasicExample
    小红书: manim -pql --resolution=1080,1440 basic_example.py BasicExample
    标准横屏: manim -pql basic_example.py BasicExample
"""

from manim import *

# 导入自适应布局系统
# 方法1: 直接导入
from manim_adaptive_layout import AdaptiveLayoutSystem

# 方法2: 如果已全局注册，可以不导入直接使用
# AdaptiveLayoutSystem 会自动可用

class BasicExample(Scene):
    def construct(self):
        # 1. 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 2. 创建标题
        title = Text("自适应布局系统示例", font_size=48)
        title.to_edge(UP, buff=1)
        self.add(title)
        
        # 3. 创建自适应段落
        paragraph = AdaptiveLayoutSystem.create_adaptive_paragraph(
            "这是一段自动换行和缩放的文本，可以适应不同屏幕比例。无论是抖音竖屏还是小红书方屏，都能正确显示。", 
            max_width=safe_width * 0.9, 
            max_height=safe_height * 0.2,
            font_size=36
        )
        paragraph.next_to(title, DOWN, buff=0.5)
        self.add(paragraph)
        
        # 4. 创建几何图形并防止重叠
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=GREEN)
        triangle = Triangle(color=RED)
        
        shapes = [circle, square, triangle]
        arranged_shapes = AdaptiveLayoutSystem.prevent_overlap(
            shapes, direction=RIGHT, min_buff=0.5
        )
        arranged_shapes.next_to(paragraph, DOWN, buff=1)
        self.add(arranged_shapes)
        
        # 5. 创建响应式网格
        elements = []
        for i in range(6):
            text = Text(f"元素 {i+1}", font_size=24)
            box = SurroundingRectangle(text, color=YELLOW, buff=0.3)
            group = VGroup(box, text)
            elements.append(group)
        
        grid = AdaptiveLayoutSystem.create_responsive_grid(
            elements, n_cols=2, h_buff=0.5, v_buff=0.5,
            max_width=safe_width * 0.8, equal_heights=True
        )
        grid.next_to(arranged_shapes, DOWN, buff=1)
        self.add(grid)
        
        # 6. 添加平台特定元素（水印和互动提示）
        AdaptiveLayoutSystem.add_platform_elements(
            self, platform="tiktok", username="@数学动画"
        )