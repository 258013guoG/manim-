# -*- coding: utf-8 -*-
from manim import *
import sys
import os

# 设置抖音竖屏比例
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class GeometryTextFormulaMix(Scene):
    def construct(self):
        # 创建安全区域（预留边距）
        safe_margin = 1  # 边距单位
        safe_width = config.frame_width - 2 * safe_margin
        safe_height = config.frame_height - 2 * safe_margin
        
        # 可视化安全区域边界（调试用，最终可以注释掉）
        safe_zone = Rectangle(
            width=safe_width,
            height=safe_height,
            stroke_color=RED,
            stroke_width=2,
            stroke_opacity=0.3,
        )
        
        # 第一部分：标题
        title = Text("几何·文字·公式", font_size=60)
        subtitle = Text("混合动画测试", font_size=40)
        
        # 确保标题在安全区域内
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        title_group.scale_to_fit_width(safe_width * 0.9)  # 留出10%的余量
        title_group.to_edge(UP, buff=safe_margin + 0.5)
        
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=DOWN), run_time=0.8)
        self.wait(0.5)
        
        # 第二部分：几何图形展示
        section_title = Text("几何变换", font_size=48, color=BLUE)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=0.8)
        
        # 创建几何图形
        triangle = Triangle(color=GREEN, fill_opacity=0.8).scale(1.2)
        square = Square(color=RED, fill_opacity=0.8).scale(1.2)
        circle = Circle(color=BLUE, fill_opacity=0.8).scale(1.2)
        star = Star(5, outer_radius=1.2, inner_radius=0.6, color=YELLOW, fill_opacity=0.8)
        
        # 初始位置
        shapes = VGroup(triangle, square, circle, star).arrange(RIGHT, buff=0.8)
        shapes.scale_to_fit_width(safe_width * 0.9)  # 确保在安全区域内
        shapes.next_to(section_title, DOWN, buff=0.8)
        
        # 逐个显示几何图形
        for shape in shapes:
            self.play(FadeIn(shape, scale=1.2), run_time=0.5)
        self.wait(0.5)
        
        # 几何变换：旋转
        self.play(
            Rotate(triangle, angle=PI, about_point=triangle.get_center()),
            Rotate(square, angle=PI/2, about_point=square.get_center()),
            Rotate(circle, angle=2*PI, about_point=circle.get_center()),
            Rotate(star, angle=PI, about_point=star.get_center()),
            run_time=2
        )
        self.wait(0.5)
        
        # 几何变换：缩放
        self.play(
            triangle.animate.scale(0.7),
            square.animate.scale(1.3),
            circle.animate.scale(0.8),
            star.animate.scale(1.2),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 清除几何部分
        self.play(
            FadeOut(shapes),
            FadeOut(section_title),
            run_time=0.8
        )
        
        # 第三部分：长文本展示
        section_title = Text("长文本段落", font_size=48, color=GREEN)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=0.8)
        
        # 创建长文本
        long_text = """几何学是数学的一个分支，研究空间中的形状、大小、位置以及它们之间的关系。欧几里得几何是最早系统化的几何学，以公理化方法建立，通过逻辑推理得出定理。

现代几何学包括多个分支，如解析几何、射影几何、微分几何、拓扑学等。几何学在物理学、工程学、计算机图形学等领域有广泛应用。

通过动画可视化，我们可以更直观地理解几何概念和定理，如勾股定理、圆的性质、多边形的特性等。"""
        
        # 分段显示长文本
        paragraphs = long_text.split("\n\n")
        text_group = VGroup()
        
        for i, paragraph in enumerate(paragraphs):
            text = Text(paragraph, font_size=32, line_spacing=1.2)
            text.scale_to_fit_width(safe_width * 0.85)  # 确保在安全区域内
            
            if i == 0:
                text.next_to(section_title, DOWN, buff=0.8)
            else:
                text.next_to(text_group[-1], DOWN, buff=0.5)
                
            text_group.add(text)
            self.play(FadeIn(text, shift=UP*0.5), run_time=1)
            
        self.wait(0.5)
        
        # 高亮关键词
        keywords = ["欧几里得几何", "解析几何", "微分几何", "勾股定理"]
        for text in text_group:
            for keyword in keywords:
                if keyword in text.original_text:
                    # 找到关键词在文本中的位置
                    start_idx = text.original_text.find(keyword)
                    end_idx = start_idx + len(keyword)
                    
                    # 高亮显示关键词
                    text[start_idx:end_idx].set_color(YELLOW)
                    self.play(Flash(text[start_idx:end_idx], color=YELLOW, flash_radius=0.3), run_time=0.5)
        
        self.wait(0.5)
        
        # 清除文本部分
        self.play(
            FadeOut(text_group),
            FadeOut(section_title),
            run_time=0.8
        )
        
        # 第四部分：数学公式展示
        section_title = Text("数学公式", font_size=48, color=YELLOW)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=0.8)
        
        # 创建数学公式
        formulas = VGroup()
        
        # 勾股定理
        pythagoras = MathTex("a^2 + b^2 = c^2", font_size=48)
        pythagoras_title = Text("勾股定理", font_size=36, color=BLUE)
        pythagoras_group = VGroup(pythagoras_title, pythagoras).arrange(DOWN, buff=0.3)
        formulas.add(pythagoras_group)
        
        # 二次方程求根公式
        quadratic = MathTex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", font_size=48)
        quadratic_title = Text("二次方程求根公式", font_size=36, color=BLUE)
        quadratic_group = VGroup(quadratic_title, quadratic).arrange(DOWN, buff=0.3)
        formulas.add(quadratic_group)
        
        # 微积分基本定理
        calculus = MathTex("\\int_{a}^{b} f'(x) dx = f(b) - f(a)", font_size=48)
        calculus_title = Text("微积分基本定理", font_size=36, color=BLUE)
        calculus_group = VGroup(calculus_title, calculus).arrange(DOWN, buff=0.3)
        formulas.add(calculus_group)
        
        # 欧拉公式
        euler = MathTex("e^{i\\pi} + 1 = 0", font_size=48)
        euler_title = Text("欧拉恒等式", font_size=36, color=BLUE)
        euler_group = VGroup(euler_title, euler).arrange(DOWN, buff=0.3)
        formulas.add(euler_group)
        
        # 排列公式组
        formulas.arrange(DOWN, buff=1)
        formulas.scale_to_fit_height(safe_height * 0.6)  # 确保在安全区域内
        formulas.next_to(section_title, DOWN, buff=0.8)
        
        # 逐个显示公式
        for formula_group in formulas:
            self.play(FadeIn(formula_group, shift=UP*0.5), run_time=0.8)
            self.wait(0.3)
        
        self.wait(0.5)
        
        # 公式变换动画
        # 勾股定理变换为三维形式
        pythagoras_3d = MathTex("a^2 + b^2 + c^2 = d^2", font_size=48)
        pythagoras_3d.move_to(pythagoras.get_center())
        
        self.play(Transform(pythagoras, pythagoras_3d), run_time=1.5)
        self.wait(0.3)
        
        # 欧拉公式展开
        euler_expanded = MathTex("e^{i\\theta} = \\cos\\theta + i\\sin\\theta", font_size=48)
        euler_expanded.move_to(euler.get_center())
        
        self.play(Transform(euler, euler_expanded), run_time=1.5)
        self.wait(0.5)
        
        # 清除公式部分
        self.play(
            FadeOut(formulas),
            FadeOut(section_title),
            run_time=0.8
        )
        
        # 第五部分：混合展示（几何+文字+公式）
        section_title = Text("混合展示", font_size=48, color=PURPLE)
        section_title.next_to(title_group, DOWN, buff=1)
        
        self.play(Write(section_title), run_time=0.8)
        
        # 创建混合内容
        # 1. 几何图形
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.5)
        circle.to_edge(LEFT, buff=safe_margin + 0.5)
        circle.shift(DOWN * 2)
        
        # 2. 文字说明
        explanation = Text("圆的面积公式", font_size=36)
        explanation.next_to(circle, UP, buff=0.5)
        
        # 3. 数学公式
        area_formula = MathTex("A = \\pi r^2", font_size=48)
        area_formula.next_to(circle, RIGHT, buff=1)
        
        # 显示混合内容
        self.play(
            Create(circle),
            Write(explanation),
            Write(area_formula),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 动态展示：半径变化，面积公式更新
        r_value = ValueTracker(1.5)  # 初始半径
        
        # 更新圆的大小
        circle.add_updater(
            lambda c: c.become(Circle(
                radius=r_value.get_value(),
                color=BLUE,
                fill_opacity=0.5
            ).move_to(c.get_center()))
        )
        
        # 更新面积公式
        area_decimal = DecimalNumber(
            3.14 * 1.5**2,
            num_decimal_places=2,
            font_size=36
        )
        area_decimal.next_to(area_formula, DOWN, buff=0.5)
        area_label = Text("面积 = ", font_size=36).next_to(area_decimal, LEFT, buff=0.2)
        area_unit = Text(" 平方单位", font_size=36).next_to(area_decimal, RIGHT, buff=0.2)
        
        area_group = VGroup(area_label, area_decimal, area_unit)
        
        # 更新面积值
        area_decimal.add_updater(
            lambda d: d.set_value(3.14 * r_value.get_value()**2)
        )
        
        self.play(FadeIn(area_group))
        
        # 动态改变半径
        self.play(r_value.animate.set_value(2.5), run_time=2)
        self.wait(0.5)
        self.play(r_value.animate.set_value(1.0), run_time=2)
        self.wait(0.5)
        self.play(r_value.animate.set_value(1.8), run_time=1)
        self.wait(1)
        
        # 结束部分
        self.play(
            FadeOut(circle),
            FadeOut(explanation),
            FadeOut(area_formula),
            FadeOut(area_group),
            FadeOut(section_title),
            FadeOut(safe_zone),
            run_time=1
        )
        
        # 总结
        final_title = Text("几何·文字·公式混合测试", font_size=48, color=BLUE)
        final_title.scale_to_fit_width(safe_width * 0.9)
        final_title.to_edge(UP, buff=safe_margin + 1)
        
        self.play(ReplacementTransform(title_group, final_title), run_time=1.5)
        
        # 创建总结列表
        summary = VGroup(
            Text("1. 几何图形的创建与变换", font_size=36),
            Text("2. 长文本的分段显示与高亮", font_size=36),
            Text("3. 数学公式的展示与变换", font_size=36),
            Text("4. 混合内容的动态交互", font_size=36)
        )
        
        summary.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        summary.scale_to_fit_width(safe_width * 0.85)
        summary.next_to(final_title, DOWN, buff=1)
        
        for item in summary:
            self.play(FadeIn(item, shift=RIGHT*0.5), run_time=0.7)
        
        self.wait(1)
        
        # 添加互动提示
        tip = Text("点赞关注，了解更多数学动画！", font_size=36, color=YELLOW)
        tip.to_edge(DOWN, buff=safe_margin + 0.5)
        self.play(FadeIn(tip, shift=UP*0.5), run_time=1)
        
        self.wait(2)

# 运行命令：
# manim -pql geometry_text_formula_mix.py GeometryTextFormulaMix