# -*- coding: utf-8 -*-
from manim import *
import sys
import os

# 导入自适应布局系统
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from adaptive_layout_system import AdaptiveLayoutSystem

# 注意：渲染此脚本时，请使用以下命令以确保正确的屏幕比例：
# manim -pql scripts/adaptive_layout_demo.py AdaptiveLayoutDemo
# 如果屏幕被挤压，可以尝试添加分辨率参数：
# manim -pql --resolution=1080,1920 scripts/adaptive_layout_demo.py AdaptiveLayoutDemo

class AdaptiveLayoutDemo(Scene):
    def construct(self):
        # 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 创建标题
        title = Text("自适应布局系统演示", font_size=48, color=BLUE)
        title.to_edge(UP, buff=1)
        self.play(Write(title))
        self.wait(0.5)
        
        # 第一部分：自适应文本演示
        section_title = Text("1. 自适应文本", font_size=36, color=GREEN)
        section_title.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(section_title))
        
        # 创建不同长度的文本示例
        short_text = "这是一段短文本。"
        medium_text = "这是一段中等长度的文本，展示自适应布局系统如何处理不同长度的内容。"
        long_text = "这是一段较长的文本内容，用于演示自适应布局系统的文本处理能力。系统会自动处理换行、缩放和对齐等问题，确保文本在不同屏幕比例下都能正确显示。当文本非常长时，系统会自动调整字体大小或进行换行处理，避免内容超出屏幕边界。"
        
        # 创建文本对象
        text_box_width = safe_width * 0.8
        
        short_text_obj = AdaptiveLayoutSystem.create_adaptive_paragraph(
            short_text, max_width=text_box_width, font_size=32
        )
        
        medium_text_obj = AdaptiveLayoutSystem.create_adaptive_paragraph(
            medium_text, max_width=text_box_width, font_size=32
        )
        
        long_text_obj = AdaptiveLayoutSystem.create_adaptive_paragraph(
            long_text, max_width=text_box_width, font_size=32, min_font_size=24
        )
        
        # 创建文本标签
        short_label = Text("短文本：", font_size=28, color=YELLOW)
        medium_label = Text("中等文本：", font_size=28, color=YELLOW)
        long_label = Text("长文本：", font_size=28, color=YELLOW)
        
        # 创建文本组
        short_group = VGroup(short_label, short_text_obj).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        medium_group = VGroup(medium_label, medium_text_obj).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        long_group = VGroup(long_label, long_text_obj).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # 排列文本组
        text_groups = VGroup(short_group, medium_group, long_group).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        text_groups.next_to(section_title, DOWN, buff=0.5)
        
        # 确保不超出安全区域
        if text_groups.height > safe_height * 0.6:
            text_groups.height = safe_height * 0.6
        
        # 显示文本组
        for group in text_groups:
            self.play(FadeIn(group), run_time=0.8)
        
        self.wait(1)
        
        # 清除文本部分
        self.play(FadeOut(text_groups), FadeOut(section_title))
        
        # 第二部分：超长文本处理
        section_title = Text("2. 超长文本处理", font_size=36, color=GREEN)
        section_title.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(section_title))
        
        # 创建超长文本
        very_long_text = """
几何学是数学的一个分支，研究空间中的形状、大小、位置以及它们之间的关系。欧几里得几何是最早系统化的几何学，以公理化方法建立，通过逻辑推理得出定理。

现代几何学包括多个分支，如解析几何、射影几何、微分几何、拓扑学等。几何学在物理学、工程学、计算机图形学等领域有广泛应用。

通过动画可视化，我们可以更直观地理解几何概念和定理，如勾股定理、圆的性质、多边形的特性等。这种方法特别适合教育和科普，能够帮助学习者建立直观的几何直觉。
"""
        
        # 创建分页文本
        pages = AdaptiveLayoutSystem.split_long_text_into_pages(
            very_long_text, 
            max_width=safe_width * 0.85,
            max_height=safe_height * 0.5,
            font_size=32,
            min_font_size=28,
            line_spacing=1.2
        )
        
        # 显示页码
        page_counter = Text("", font_size=24)
        page_counter.to_edge(DOWN, buff=1.5)
        
        # 逐页显示
        current_page = None
        for i, page in enumerate(pages):
            page_counter.become(Text(f"第 {i+1}/{len(pages)} 页", font_size=24))
            
            if current_page:
                self.play(FadeOut(current_page))
            
            page.next_to(section_title, DOWN, buff=0.8)
            self.play(FadeIn(page), Write(page_counter) if i == 0 else Transform(page_counter, Text(f"第 {i+1}/{len(pages)} 页", font_size=24).move_to(page_counter)))
            current_page = page
            self.wait(1.5 if i < len(pages)-1 else 1)
        
        # 清除页面
        self.play(FadeOut(current_page), FadeOut(page_counter), FadeOut(section_title))
        
        # 第三部分：自动排列与防止重叠
        section_title = Text("3. 自动排列与防止重叠", font_size=36, color=GREEN)
        section_title.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(section_title))
        
        # 创建几何图形
        circle = Circle(radius=1, color=RED, fill_opacity=0.5)
        square = Square(side_length=2, color=GREEN, fill_opacity=0.5)
        triangle = Triangle(color=BLUE, fill_opacity=0.5)
        star = Star(5, outer_radius=1, inner_radius=0.5, color=YELLOW, fill_opacity=0.5)
        pentagon = RegularPolygon(5, color=PURPLE, fill_opacity=0.5)
        
        # 创建图形标签
        circle_label = Text("圆形", font_size=24).next_to(circle, DOWN)
        square_label = Text("正方形", font_size=24).next_to(square, DOWN)
        triangle_label = Text("三角形", font_size=24).next_to(triangle, DOWN)
        star_label = Text("星形", font_size=24).next_to(star, DOWN)
        pentagon_label = Text("五边形", font_size=24).next_to(pentagon, DOWN)
        
        # 创建图形组
        circle_group = VGroup(circle, circle_label)
        square_group = VGroup(square, square_label)
        triangle_group = VGroup(triangle, triangle_label)
        star_group = VGroup(star, star_label)
        pentagon_group = VGroup(pentagon, pentagon_label)
        
        # 方法1：水平排列
        horizontal_title = Text("水平排列", font_size=28, color=BLUE)
        horizontal_title.next_to(section_title, DOWN, buff=0.8)
        
        # 使用自适应布局系统防止重叠
        horizontal_shapes = AdaptiveLayoutSystem.prevent_overlap(
            [circle_group.copy(), square_group.copy(), triangle_group.copy()], 
            direction=RIGHT, 
            min_buff=0.5
        )
        horizontal_shapes.next_to(horizontal_title, DOWN, buff=0.5)
        
        # 方法2：垂直排列
        vertical_title = Text("垂直排列", font_size=28, color=BLUE)
        vertical_title.next_to(horizontal_shapes, DOWN, buff=1)
        
        # 使用自适应布局系统防止重叠
        vertical_shapes = AdaptiveLayoutSystem.prevent_overlap(
            [star_group.copy(), pentagon_group.copy()], 
            direction=DOWN, 
            min_buff=0.5
        )
        vertical_shapes.next_to(vertical_title, DOWN, buff=0.5)
        
        # 显示排列
        self.play(FadeIn(horizontal_title))
        self.play(FadeIn(horizontal_shapes), run_time=1)
        self.play(FadeIn(vertical_title))
        self.play(FadeIn(vertical_shapes), run_time=1)
        
        self.wait(1)
        
        # 清除排列部分
        self.play(
            FadeOut(horizontal_title),
            FadeOut(horizontal_shapes),
            FadeOut(vertical_title),
            FadeOut(vertical_shapes),
            FadeOut(section_title)
        )
        
        # 第四部分：响应式网格布局
        section_title = Text("4. 响应式网格布局", font_size=36, color=GREEN)
        section_title.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(section_title))
        
        # 创建多个对象
        shapes = [
            Circle(radius=0.5, color=RED, fill_opacity=0.5),
            Square(side_length=1, color=GREEN, fill_opacity=0.5),
            Triangle(color=BLUE, fill_opacity=0.5),
            Star(5, outer_radius=0.5, inner_radius=0.25, color=YELLOW, fill_opacity=0.5),
            RegularPolygon(5, color=PURPLE, fill_opacity=0.5),
            RegularPolygon(6, color=ORANGE, fill_opacity=0.5),
            Circle(radius=0.5, color=PINK, fill_opacity=0.5),
            Square(side_length=1, color=TEAL, fill_opacity=0.5),
            Triangle(color=GOLD, fill_opacity=0.5)
        ]
        
        # 创建响应式网格
        grid = AdaptiveLayoutSystem.create_responsive_grid(
            shapes,
            n_cols=3,  # 列数
            h_buff=1.0,  # 水平间距
            v_buff=1.0,  # 垂直间距
            max_width=safe_width * 0.9,  # 最大宽度
            equal_heights=True  # 使所有行高度相等
        )
        grid.next_to(section_title, DOWN, buff=0.8)
        
        # 显示网格
        self.play(FadeIn(grid), run_time=1.5)
        self.wait(1)
        
        # 清除网格部分
        self.play(FadeOut(grid), FadeOut(section_title))
        
        # 第五部分：平台优化元素
        section_title = Text("5. 平台优化元素", font_size=36, color=GREEN)
        section_title.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(section_title))
        
        # 显示平台说明
        platform_text = Text("当前优化平台：抖音竖屏 (9:16)", font_size=28)
        platform_text.next_to(section_title, DOWN, buff=0.8)
        self.play(Write(platform_text))
        
        # 添加平台元素
        platform_elements = AdaptiveLayoutSystem.add_platform_elements(
            self, platform="tiktok", username="@数学动画"
        )
        
        # 高亮显示平台元素
        self.play(Indicate(platform_elements, color=YELLOW, scale_factor=1.2))
        self.wait(1)
        
        # 显示说明文本
        explanation = Text("自动添加水印和互动提示，\n优化竖屏显示效果", font_size=28, line_spacing=1.2)
        explanation.next_to(platform_text, DOWN, buff=0.8)
        self.play(FadeIn(explanation))
        
        self.wait(1.5)
        
        # 结束部分
        self.play(
            FadeOut(section_title),
            FadeOut(platform_text),
            FadeOut(explanation),
            FadeOut(title)
        )
        
        # 总结
        final_text = Text("自适应布局系统", font_size=48, color=BLUE)
        final_text.to_edge(UP, buff=1.5)
        
        features = VGroup(
            Text("✓ 自动文本换行与缩放", font_size=32),
            Text("✓ 超长文本分页处理", font_size=32),
            Text("✓ 防止元素重叠", font_size=32),
            Text("✓ 响应式网格布局", font_size=32),
            Text("✓ 平台优化元素", font_size=32)
        )
        
        features.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        features.next_to(final_text, DOWN, buff=1)
        
        self.play(Write(final_text))
        
        for feature in features:
            self.play(FadeIn(feature, shift=RIGHT*0.3), run_time=0.5)
        
        self.wait(2)

# 运行命令：
# manim -pql adaptive_layout_demo.py AdaptiveLayoutDemo