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

class LayoutUtilsDemo(Scene):
    def construct(self):
        # 创建安全区域
        safe_zone, safe_width, safe_height = LayoutUtils.create_safe_zone(self)
        
        # 第一部分：标题和介绍
        title = Text("Manim自适应布局工具", font_size=48)
        subtitle = Text("防止内容超出屏幕和重叠", font_size=36)
        
        # 使用工具类自动排列并确保在安全区域内
        title_group = LayoutUtils.auto_arrange(
            [title, subtitle], 
            direction=DOWN, 
            buff=0.5, 
            safe_width=safe_width, 
            safe_height=safe_height
        )
        title_group.to_edge(UP, buff=1.5)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=DOWN), run_time=1)
        self.wait(1)
        
        # 第二部分：自动文本适应
        section_title = Text("自动文本适应", font_size=42, color=BLUE)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=1)
        
        # 创建一个长文本
        long_text = "这是一段很长的文本内容，在不同屏幕尺寸下可能会超出屏幕边界。使用自适应技术可以确保内容始终在安全区域内显示，不会被裁剪或超出可视范围。"
        
        # 创建原始文本对象（故意设置较大字体）
        original_text = Text(long_text, font_size=36)
        original_text.next_to(section_title, DOWN, buff=0.8)
        
        # 显示原始文本（会超出安全区域）
        self.play(FadeIn(original_text), run_time=1)
        self.wait(1)
        
        # 添加超出提示
        overflow_text = Text("文本超出安全区域！", font_size=32, color=RED)
        overflow_text.next_to(original_text, DOWN, buff=0.5)
        self.play(Write(overflow_text), run_time=1)
        self.wait(1)
        
        # 使用工具类自动调整文本大小
        self.play(FadeOut(original_text), FadeOut(overflow_text), run_time=1)
        
        # 方法1：自动缩放文本
        method1_title = Text("方法1：自动缩放文本", font_size=32, color=GREEN)
        method1_title.next_to(section_title, DOWN, buff=0.8)
        
        adjusted_text = Text(long_text, font_size=36)
        adjusted_text = LayoutUtils.fit_text_to_width(adjusted_text, safe_width * 0.9)
        adjusted_text.next_to(method1_title, DOWN, buff=0.5)
        
        self.play(Write(method1_title), run_time=1)
        self.play(FadeIn(adjusted_text), run_time=1)
        self.wait(1)
        
        # 方法2：自动换行文本
        self.play(FadeOut(adjusted_text), run_time=1)
        
        method2_title = Text("方法2：自动换行文本", font_size=32, color=GREEN)
        method2_title.next_to(method1_title, DOWN, buff=1.5)
        
        wrapped_text = Text(long_text, font_size=32)
        wrapped_text = LayoutUtils.auto_wrap_text(wrapped_text, safe_width * 0.9)
        wrapped_text.next_to(method2_title, DOWN, buff=0.5)
        
        self.play(Write(method2_title), run_time=1)
        self.play(FadeIn(wrapped_text), run_time=1)
        self.wait(1)
        
        # 第三部分：防止元素重叠
        self.play(
            FadeOut(section_title),
            FadeOut(method1_title),
            FadeOut(method2_title),
            FadeOut(wrapped_text),
            run_time=1
        )
        
        section_title = Text("防止元素重叠", font_size=42, color=BLUE)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=1)
        
        # 创建一些形状（故意重叠）
        shapes = VGroup()
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        shape_classes = [Square, Circle, Triangle, RegularPolygon, Star]
        
        for i, (shape_class, color) in enumerate(zip(shape_classes, colors)):
            if shape_class == RegularPolygon:
                shape = shape_class(5, color=color, fill_opacity=0.7)
            elif shape_class == Star:
                shape = shape_class(5, outer_radius=1, inner_radius=0.5, color=color, fill_opacity=0.7)
            else:
                shape = shape_class(color=color, fill_opacity=0.7)
            shape.scale(0.8)
            # 故意让所有形状都在中心位置（重叠）
            shape.move_to(ORIGIN)
            shapes.add(shape)
        
        # 显示重叠的形状
        shapes_group = VGroup(shapes).arrange(DOWN, buff=1)
        shapes_group.next_to(section_title, DOWN, buff=0.8)
        
        self.play(FadeIn(shapes), run_time=1)
        
        # 添加重叠提示
        overlap_text = Text("元素重叠问题", font_size=32, color=RED)
        overlap_text.next_to(shapes, DOWN, buff=0.5)
        self.play(Write(overlap_text), run_time=1)
        self.wait(1)
        
        # 使用工具类防止重叠
        self.play(FadeOut(overlap_text), run_time=1)
        
        # 水平排列（使用auto_arrange）
        method1_title = Text("方法1：水平自动排列", font_size=32, color=GREEN)
        method1_title.next_to(shapes, DOWN, buff=0.5)
        
        self.play(Write(method1_title), run_time=1)
        self.play(
            shapes.animate.arrange(RIGHT, buff=0.4),
            run_time=1.5
        )
        
        # 检查是否超出安全区域并自动调整
        if shapes.width > safe_width:
            self.play(
                shapes.animate.scale_to_fit_width(safe_width * 0.9),
                run_time=1
            )
        
        self.wait(1)
        
        # 第四部分：响应式网格布局
        self.play(
            FadeOut(shapes),
            FadeOut(method1_title),
            FadeOut(section_title),
            run_time=1
        )
        
        section_title = Text("响应式网格布局", font_size=42, color=BLUE)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=1)
        
        # 创建多个形状用于网格布局
        grid_shapes = []
        for i in range(9):  # 创建9个形状
            shape_class = shape_classes[i % len(shape_classes)]
            color = colors[i % len(colors)]
            
            if shape_class == RegularPolygon:
                shape = shape_class(5, color=color, fill_opacity=0.7)
            elif shape_class == Star:
                shape = shape_class(5, outer_radius=1, inner_radius=0.5, color=color, fill_opacity=0.7)
            else:
                shape = shape_class(color=color, fill_opacity=0.7)
            shape.scale(0.8)
            grid_shapes.append(shape)
        
        # 使用工具类创建响应式网格
        grid = LayoutUtils.create_responsive_grid(
            grid_shapes, 
            n_cols=3, 
            safe_width=safe_width, 
            safe_height=safe_height * 0.4  # 限制高度以便在屏幕上显示
        )
        grid.next_to(section_title, DOWN, buff=0.8)
        
        self.play(FadeIn(grid), run_time=1.5)
        
        # 添加说明
        grid_text = Text("自动计算网格布局，确保不超出安全区域", font_size=28, color=GREEN)
        grid_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(grid_text), run_time=1)
        self.wait(1)
        
        # 第五部分：自动边距计算
        self.play(
            FadeOut(grid),
            FadeOut(grid_text),
            FadeOut(section_title),
            run_time=1
        )
        
        section_title = Text("自动边距计算", font_size=42, color=BLUE)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=1)
        
        # 创建不同大小的对象
        small_obj = Circle(radius=0.5, color=BLUE, fill_opacity=0.7)
        medium_obj = Square(side_length=2, color=GREEN, fill_opacity=0.7)
        large_obj = Rectangle(width=4, height=3, color=RED, fill_opacity=0.7)
        
        # 计算并应用自动边距
        small_margin = LayoutUtils.auto_margin(small_obj, safe_width, safe_height)
        medium_margin = LayoutUtils.auto_margin(medium_obj, safe_width, safe_height)
        large_margin = LayoutUtils.auto_margin(large_obj, safe_width, safe_height)
        
        # 添加边距标签
        small_label = Text(f"小对象边距: {small_margin}", font_size=24)
        medium_label = Text(f"中对象边距: {medium_margin}", font_size=24)
        large_label = Text(f"大对象边距: {large_margin}", font_size=24)
        
        # 排列对象和标签
        small_group = VGroup(small_obj, small_label).arrange(DOWN, buff=0.3)
        medium_group = VGroup(medium_obj, medium_label).arrange(DOWN, buff=0.3)
        large_group = VGroup(large_obj, large_label).arrange(DOWN, buff=0.3)
        
        all_groups = VGroup(small_group, medium_group, large_group).arrange(RIGHT, buff=1)
        all_groups.next_to(section_title, DOWN, buff=1)
        
        # 检查是否超出安全区域并自动调整
        if all_groups.width > safe_width:
            all_groups.scale_to_fit_width(safe_width * 0.9)
        
        self.play(FadeIn(all_groups), run_time=1.5)
        
        # 添加说明
        explanation = Text("对象越大，自动使用越小的边距", font_size=32, color=YELLOW)
        explanation.next_to(all_groups, DOWN, buff=0.8)
        self.play(Write(explanation), run_time=1)
        self.wait(1)
        
        # 结束部分
        self.play(
            FadeOut(all_groups),
            FadeOut(explanation),
            FadeOut(section_title),
            FadeOut(safe_zone),
            run_time=1
        )
        
        # 总结
        final_title = Text("Manim布局工具类", font_size=48, color=BLUE)
        final_title.scale_to_fit_width(safe_width * 0.8)
        final_title.to_edge(UP, buff=1.5)
        
        self.play(ReplacementTransform(title_group, final_title), run_time=1.5)
        
        # 创建最佳实践列表
        practices = VGroup(
            Text("1. LayoutUtils.create_safe_zone()", font_size=32),
            Text("2. LayoutUtils.fit_text_to_width()", font_size=32),
            Text("3. LayoutUtils.auto_wrap_text()", font_size=32),
            Text("4. LayoutUtils.auto_arrange()", font_size=32),
            Text("5. LayoutUtils.create_responsive_grid()", font_size=32),
            Text("6. LayoutUtils.auto_margin()", font_size=32),
            Text("7. LayoutUtils.prevent_overlap()", font_size=32)
        )
        
        practices.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        practices.scale_to_fit_width(safe_width * 0.9)
        practices.next_to(final_title, DOWN, buff=1)
        
        for practice in practices:
            self.play(FadeIn(practice, shift=RIGHT*0.5), run_time=0.5)
        
        self.wait(1)
        
        # 添加互动提示
        tip = Text("点赞关注，了解更多Manim技巧！", font_size=36, color=YELLOW)
        tip.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(tip, shift=UP*0.5), run_time=1)
        
        self.wait(2)

# 运行命令：
# manim -pql layout_utils_demo.py LayoutUtilsDemo