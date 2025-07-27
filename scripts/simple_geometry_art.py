# -*- coding: utf-8 -*-
from manim import *
import numpy as np

# 设置抖音竖屏比例
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class SimpleGeometryArt(Scene):
    def construct(self):
        # 创建封面
        title = Text("几何艺术", font_size=72, color=BLUE)
        subtitle = Text("简约而不简单", font_size=36)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=DOWN), run_time=1)
        self.wait(1)
        self.play(title_group.animate.scale(0.7).to_edge(UP), run_time=1)
        
        # 第一部分：几何图形舞蹈
        section_title = Text("几何图形舞蹈", font_size=48, color=YELLOW)
        section_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(section_title), run_time=1)
        
        # 创建一组基本几何图形
        shapes = VGroup()
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        
        # 添加不同的几何图形
        square = Square(side_length=1, color=colors[0], fill_opacity=0.7)
        circle = Circle(radius=0.8, color=colors[1], fill_opacity=0.7)
        triangle = Triangle(color=colors[2], fill_opacity=0.7).scale(0.9)
        pentagon = RegularPolygon(5, color=colors[3], fill_opacity=0.7).scale(0.9)
        hexagon = RegularPolygon(6, color=colors[4], fill_opacity=0.7).scale(0.9)
        star = Star(5, outer_radius=1, inner_radius=0.5, color=colors[5], fill_opacity=0.7)
        
        shapes.add(square, circle, triangle, pentagon, hexagon, star)
        
        # 将图形排列成圆形
        shapes.arrange_in_grid(rows=2, cols=3, buff=1)
        shapes.move_to(ORIGIN)
        
        # 逐个显示图形
        for shape in shapes:
            self.play(FadeIn(shape, scale=0.5), run_time=0.7)
        
        # 让图形跳舞
        self.play(shapes.animate.arrange_in_grid(rows=3, cols=2, buff=1.2), run_time=1.5)
        self.play(Rotate(shapes, angle=PI/2), run_time=1.5)
        self.play(shapes.animate.arrange_in_grid(rows=1, cols=6, buff=0.5), run_time=1.5)
        self.play(shapes.animate.arrange_in_grid(rows=6, cols=1, buff=0.5), run_time=1.5)
        
        # 创建环形排列
        radius = 3
        self.play(
            *[shape.animate.move_to(radius * np.array([np.cos(i * TAU / len(shapes)), np.sin(i * TAU / len(shapes)), 0])) for i, shape in enumerate(shapes)],
            run_time=1.5
        )
        
        # 旋转整个图形组
        self.play(Rotate(shapes, angle=TAU, rate_func=smooth), run_time=3)
        
        # 清除场景
        self.play(FadeOut(shapes), FadeOut(section_title), run_time=1)
        
        # 第二部分：几何艺术图案
        section_title = Text("几何艺术图案", font_size=48, color=GREEN)
        section_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(section_title), run_time=1)
        
        # 创建同心圆图案
        circles = VGroup()
        num_circles = 12
        max_radius = 4
        
        for i in range(num_circles):
            radius = max_radius * (i + 1) / num_circles
            circle = Circle(
                radius=radius,
                stroke_width=2,
                stroke_color=interpolate_color(BLUE, RED, i / num_circles),
                stroke_opacity=0.7
            )
            circles.add(circle)
        
        self.play(Create(circles, lag_ratio=0.1), run_time=2)
        
        # 添加放射线
        lines = VGroup()
        num_lines = 24
        
        for i in range(num_lines):
            angle = i * TAU / num_lines
            start = ORIGIN
            end = max_radius * np.array([np.cos(angle), np.sin(angle), 0])
            line = Line(
                start, end,
                stroke_width=2,
                stroke_color=interpolate_color(YELLOW, PURPLE, i / num_lines),
                stroke_opacity=0.7
            )
            lines.add(line)
        
        self.play(Create(lines, lag_ratio=0.05), run_time=2)
        
        # 旋转图案
        self.play(
            Rotate(circles, angle=PI/2, rate_func=smooth),
            Rotate(lines, angle=-PI/2, rate_func=smooth),
            run_time=3
        )
        
        # 清除场景
        self.play(FadeOut(circles), FadeOut(lines), FadeOut(section_title), run_time=1)
        
        # 第三部分：动态几何艺术
        section_title = Text("动态几何艺术", font_size=48, color=PURPLE)
        section_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(section_title), run_time=1)
        
        # 创建波浪图案
        dots = VGroup()
        num_dots = 20
        dot_radius = 0.1
        
        for i in range(num_dots):
            for j in range(num_dots):
                x = (i - num_dots/2) * 0.4
                y = (j - num_dots/2) * 0.4
                dot = Dot(
                    point=[x, y, 0],
                    radius=dot_radius,
                    color=interpolate_color(BLUE, GREEN, (i+j)/(2*num_dots)),
                    fill_opacity=0.8
                )
                dots.add(dot)
        
        dots.move_to(ORIGIN)
        self.play(Create(dots, lag_ratio=0.01), run_time=2)
        
        # 创建波浪动画
        def wave_updater(mob, dt):
            for i, dot in enumerate(mob):
                x, y, z = dot.get_center()
                i_x = (i % num_dots) - num_dots/2
                i_y = (i // num_dots) - num_dots/2
                time = self.time
                
                # 创建波浪效果
                z = 0.5 * np.sin(i_x * 0.4 + time * 2) * np.cos(i_y * 0.4 + time * 2)
                dot.move_to([x, y, z])
                
                # 颜色变化
                color_factor = (np.sin(time + i_x * 0.2) + 1) / 2
                dot.set_color(interpolate_color(BLUE, RED, color_factor))
        
        # 应用更新器并播放动画
        dots.add_updater(wave_updater)
        self.wait(5)  # 让波浪动画运行5秒
        dots.remove_updater(wave_updater)
        
        # 清除场景
        self.play(FadeOut(dots), FadeOut(section_title), run_time=1)
        
        # 结束文字
        final_title = Text("几何之美", font_size=60, color=BLUE)
        final_subtitle = Text("简单形状，无限创意", font_size=36)
        final_group = VGroup(final_title, final_subtitle).arrange(DOWN, buff=0.5)
        
        self.play(
            FadeOut(title_group),
            Write(final_title),
            run_time=1.5
        )
        self.play(Write(final_subtitle), run_time=1)
        
        # 添加互动提示
        interaction_tip = Text("点赞关注，发现更多几何之美", font_size=36, color=YELLOW)
        interaction_tip.to_edge(DOWN, buff=1)
        self.play(FadeIn(interaction_tip, shift=UP*0.5), run_time=1)
        self.wait(2)

# 运行命令：
# manim -pql simple_geometry_art.py SimpleGeometryArt