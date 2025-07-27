# -*- coding: utf-8 -*-
from manim import *
import sys
import os

# 添加scripts目录到Python路径，以便导入manim_layout_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from manim_layout_utils import LayoutUtils

# 设置抖音竖屏比例
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class TikTokSafeLayout(Scene):
    def construct(self):
        # 创建安全区域（较大边距，确保在抖音上显示安全）
        safe_zone, safe_width, safe_height = LayoutUtils.create_safe_zone(self, margin=1.2)
        
        # 创建标题
        title = Text("抖音竖屏安全布局", font_size=60)
        subtitle = Text("确保内容不超出边界", font_size=40)
        
        # 自动调整标题大小，确保在安全区域内
        title = LayoutUtils.fit_text_to_width(title, safe_width * 0.9)
        subtitle = LayoutUtils.fit_text_to_width(subtitle, safe_width * 0.8)
        
        # 垂直排列标题和副标题
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        title_group.to_edge(UP, buff=1.5)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=DOWN), run_time=1)
        self.wait(1)
        
        # 创建一些演示对象
        # 1. 创建一个大矩形（故意超出安全区域）
        big_rect = Rectangle(width=10, height=4, color=RED, fill_opacity=0.5)
        big_rect.next_to(title_group, DOWN, buff=1)
        
        self.play(Create(big_rect), run_time=1)
        
        # 添加超出提示
        overflow_text = Text("超出安全区域！", font_size=36, color=RED)
        overflow_text.next_to(big_rect, DOWN, buff=0.5)
        self.play(Write(overflow_text), run_time=1)
        self.wait(1)
        
        # 自动调整大小以适应安全区域
        self.play(
            big_rect.animate.scale_to_fit_width(safe_width * 0.9),
            FadeOut(overflow_text),
            run_time=1.5
        )
        
        # 添加调整后提示
        adjusted_text = Text("自动调整大小后适应安全区域", font_size=32, color=GREEN)
        adjusted_text.next_to(big_rect, DOWN, buff=0.5)
        self.play(Write(adjusted_text), run_time=1)
        self.wait(1)
        
        # 2. 演示防止重叠
        self.play(
            FadeOut(big_rect),
            FadeOut(adjusted_text),
            run_time=1
        )
        
        # 创建多个形状（初始位置重叠）
        shapes = VGroup()
        colors = [BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        for i, color in enumerate(colors):
            shape = Circle(radius=1, color=color, fill_opacity=0.7)
            shape.move_to(ORIGIN)  # 所有形状都在同一位置（重叠）
            shapes.add(shape)
        
        shapes.next_to(title_group, DOWN, buff=1.5)
        
        self.play(FadeIn(shapes), run_time=1)
        
        # 添加重叠提示
        overlap_text = Text("元素重叠！", font_size=36, color=RED)
        overlap_text.next_to(shapes, DOWN, buff=0.5)
        self.play(Write(overlap_text), run_time=1)
        self.wait(1)
        
        # 使用auto_arrange自动排列，防止重叠
        arranged_shapes = LayoutUtils.auto_arrange(
            shapes, 
            direction=RIGHT, 
            buff=0.5, 
            safe_width=safe_width, 
            safe_height=None
        )
        
        self.play(
            ReplacementTransform(shapes, arranged_shapes),
            FadeOut(overlap_text),
            run_time=1.5
        )
        
        # 添加排列后提示
        arranged_text = Text("自动排列后不再重叠", font_size=32, color=GREEN)
        arranged_text.next_to(arranged_shapes, DOWN, buff=0.5)
        self.play(Write(arranged_text), run_time=1)
        self.wait(1)
        
        # 3. 演示文本自动换行
        self.play(
            FadeOut(arranged_shapes),
            FadeOut(arranged_text),
            run_time=1
        )
        
        # 创建一个长文本（故意超出安全区域）
        long_text = "这是一段很长的文本内容，在抖音竖屏视频中可能会超出屏幕边界。使用自动换行功能可以确保文本内容完全显示在安全区域内，不会被裁剪或超出可视范围。"
        original_text = Text(long_text, font_size=36)
        original_text.next_to(title_group, DOWN, buff=1.5)
        
        self.play(FadeIn(original_text), run_time=1)
        
        # 添加超出提示
        text_overflow = Text("文本超出安全区域！", font_size=32, color=RED)
        text_overflow.next_to(original_text, DOWN, buff=0.5)
        self.play(Write(text_overflow), run_time=1)
        self.wait(1)
        
        # 使用auto_wrap_text自动换行
        self.play(
            FadeOut(original_text),
            FadeOut(text_overflow),
            run_time=1
        )
        
        wrapped_text = Text(long_text, font_size=32)
        wrapped_text = LayoutUtils.auto_wrap_text(wrapped_text, safe_width * 0.9)
        wrapped_text.next_to(title_group, DOWN, buff=1.5)
        
        self.play(FadeIn(wrapped_text), run_time=1)
        
        # 添加换行后提示
        wrapped_text_label = Text("文本自动换行后适应安全区域", font_size=32, color=GREEN)
        wrapped_text_label.next_to(wrapped_text, DOWN, buff=0.5)
        self.play(Write(wrapped_text_label), run_time=1)
        self.wait(1)
        
        # 4. 演示响应式网格布局
        self.play(
            FadeOut(wrapped_text),
            FadeOut(wrapped_text_label),
            run_time=1
        )
        
        # 创建多个形状用于网格布局
        grid_shapes = []
        for i in range(8):  # 创建8个形状
            if i % 4 == 0:
                shape = Square(side_length=1.5, color=colors[i % len(colors)], fill_opacity=0.7)
            elif i % 4 == 1:
                shape = Circle(radius=0.8, color=colors[i % len(colors)], fill_opacity=0.7)
            elif i % 4 == 2:
                shape = Triangle(color=colors[i % len(colors)], fill_opacity=0.7)
            else:
                shape = RegularPolygon(5, color=colors[i % len(colors)], fill_opacity=0.7)
            grid_shapes.append(shape)
        
        # 使用create_responsive_grid创建网格布局
        grid_title = Text("响应式网格布局", font_size=42, color=BLUE)
        grid_title = LayoutUtils.fit_text_to_width(grid_title, safe_width * 0.8)
        grid_title.next_to(title_group, DOWN, buff=1.5)
        
        self.play(Write(grid_title), run_time=1)
        
        grid = LayoutUtils.create_responsive_grid(
            grid_shapes, 
            n_cols=4,  # 4列网格
            safe_width=safe_width, 
            safe_height=safe_height * 0.4,  # 限制高度
            h_buff=0.5, 
            v_buff=0.5
        )
        grid.next_to(grid_title, DOWN, buff=0.8)
        
        self.play(FadeIn(grid), run_time=1.5)
        
        # 添加网格布局提示
        grid_label = Text("自动计算网格布局，确保不超出安全区域", font_size=28, color=GREEN)
        grid_label = LayoutUtils.fit_text_to_width(grid_label, safe_width * 0.9)
        grid_label.next_to(grid, DOWN, buff=0.5)
        self.play(Write(grid_label), run_time=1)
        self.wait(1)
        
        # 结束部分
        self.play(
            FadeOut(grid),
            FadeOut(grid_label),
            FadeOut(grid_title),
            FadeOut(safe_zone),
            run_time=1
        )
        
        # 总结
        final_title = Text("抖音竖屏安全布局技巧", font_size=48, color=BLUE)
        final_title = LayoutUtils.fit_text_to_width(final_title, safe_width * 0.9)
        final_title.to_edge(UP, buff=1.5)
        
        self.play(ReplacementTransform(title_group, final_title), run_time=1.5)
        
        # 创建最佳实践列表
        practices = VGroup(
            Text("1. 定义安全区域，预留足够边距", font_size=36),
            Text("2. 使用fit_text_to_width控制文本大小", font_size=36),
            Text("3. 使用auto_wrap_text自动换行长文本", font_size=36),
            Text("4. 使用auto_arrange防止元素重叠", font_size=36),
            Text("5. 使用create_responsive_grid创建网格", font_size=36)
        )
        
        # 确保每个文本项不超出安全区域
        for practice in practices:
            practice = LayoutUtils.fit_text_to_width(practice, safe_width * 0.85)
        
        practices.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        practices.next_to(final_title, DOWN, buff=1.5)
        
        # 检查整个列表是否超出安全高度
        if practices.height > safe_height * 0.6:
            practices.scale_to_fit_height(safe_height * 0.6)
        
        for practice in practices:
            self.play(FadeIn(practice, shift=RIGHT*0.5), run_time=0.7)
        
        self.wait(1)
        
        # 添加互动提示
        tip = Text("点赞关注，了解更多Manim技巧！", font_size=36, color=YELLOW)
        tip = LayoutUtils.fit_text_to_width(tip, safe_width * 0.9)
        tip.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(tip, shift=UP*0.5), run_time=1)
        
        self.wait(2)

# 运行命令：
# manim -pql tiktok_safe_layout.py TikTokSafeLayout