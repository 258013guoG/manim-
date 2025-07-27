# -*- coding: utf-8 -*-
from manim import *

class SynchronizedSubtitles(Scene):
    def construct(self):
        # 创建标题
        title = Text("同步字幕与动画", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建字幕容器 - 固定在底部
        subtitle_box = Rectangle(width=12, height=1, fill_opacity=0.1, stroke_opacity=0.3)
        subtitle_box.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(subtitle_box))
        
        # 初始字幕为空
        current_subtitle = Text("", font_size=30)
        current_subtitle.move_to(subtitle_box.get_center())
        self.add(current_subtitle)
        
        # 创建一个简单的几何演示
        # 1. 创建一个正方形
        self.update_subtitle(current_subtitle, "首先，我们创建一个正方形")
        square = Square(side_length=2, color=BLUE)
        self.play(Create(square))
        self.wait(1)
        
        # 2. 将正方形变成圆形
        self.update_subtitle(current_subtitle, "接下来，我们将正方形变成圆形")
        circle = Circle(radius=1, color=RED)
        self.play(ReplacementTransform(square, circle))
        self.wait(1)
        
        # 3. 添加一个三角形
        self.update_subtitle(current_subtitle, "现在，让我们添加一个三角形")
        triangle = Triangle(color=GREEN).scale(1.5)
        triangle.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(triangle))
        self.wait(1)
        
        # 4. 组合图形并移动
        self.update_subtitle(current_subtitle, "我们将这些图形组合在一起并移动它们")
        group = VGroup(circle, triangle)
        self.play(group.animate.arrange(DOWN, buff=0.5).move_to(ORIGIN))
        self.wait(1)
        
        # 5. 旋转组合图形
        self.update_subtitle(current_subtitle, "让我们旋转这个组合图形")
        self.play(Rotate(group, angle=PI, about_point=ORIGIN), run_time=2)
        self.wait(1)
        
        # 6. 添加数学公式
        self.update_subtitle(current_subtitle, "现在，我们添加一个数学公式")
        formula = MathTex(r"E = mc^2", font_size=48)
        formula.next_to(group, UP, buff=1)
        self.play(Write(formula))
        self.wait(1)
        
        # 7. 最终组合所有元素
        self.update_subtitle(current_subtitle, "最后，我们将所有元素组合在一起")
        final_group = VGroup(group, formula)
        self.play(final_group.animate.arrange(DOWN, buff=0.8).scale(0.8))
        self.wait(1)
        
        # 结束
        self.update_subtitle(current_subtitle, "演示完成！同步字幕可以帮助观众更好地理解动画内容")
        self.wait(2)
        
        # 清除字幕
        self.play(FadeOut(current_subtitle), FadeOut(subtitle_box))
        
        # 结束信息
        conclusion = Text("同步字幕演示完成！", color=GREEN, font_size=36)
        self.play(Write(conclusion))
        self.wait(2)
    
    def update_subtitle(self, current_subtitle, new_text):
        """更新字幕内容"""
        new_subtitle = Text(new_text, font_size=30)
        new_subtitle.move_to(current_subtitle.get_center())
        self.play(ReplacementTransform(current_subtitle, new_subtitle))
        return new_subtitle


class AdvancedSynchronizedSubtitles(Scene):
    def construct(self):
        # 创建标题
        title = Text("高级同步字幕技术", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一个更精美的字幕容器
        subtitle_box = RoundedRectangle(
            width=12, 
            height=1.2, 
            corner_radius=0.2,
            fill_opacity=0.2, 
            fill_color=BLUE_E,
            stroke_opacity=0.5,
            stroke_color=WHITE
        )
        subtitle_box.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(subtitle_box))
        
        # 创建字幕文本
        current_subtitle = Text("", font_size=30)
        current_subtitle.move_to(subtitle_box.get_center())
        self.add(current_subtitle)
        
        # 创建一个更复杂的数学演示 - 勾股定理
        # 1. 介绍勾股定理
        new_subtitle = self.update_subtitle_with_style(
            current_subtitle, 
            "勾股定理：直角三角形中，两直角边的平方和等于斜边的平方",
            gradient_colors=[BLUE, GREEN]
        )
        current_subtitle = new_subtitle
        
        # 显示公式
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=48)
        self.play(Write(formula))
        self.wait(1.5)
        
        # 2. 创建直角三角形
        new_subtitle = self.update_subtitle_with_style(
            current_subtitle, 
            "让我们创建一个直角三角形来验证这个定理",
            gradient_colors=[GREEN, YELLOW]
        )
        current_subtitle = new_subtitle
        
        # 移动公式到上方
        self.play(formula.animate.to_edge(UP, buff=1.5))
        
        # 创建直角三角形
        triangle = Polygon(
            ORIGIN, RIGHT*3, UP*4,
            color=WHITE,
            fill_opacity=0.2
        )
        self.play(Create(triangle))
        
        # 标记直角
        right_angle = RightAngle(
            Line(ORIGIN, RIGHT*3),
            Line(ORIGIN, UP*4),
            length=0.5,
            color=YELLOW
        )
        self.play(Create(right_angle))
        
        # 3. 标记边长
        new_subtitle = self.update_subtitle_with_style(
            current_subtitle, 
            "标记三角形的三条边：a=3, b=4, c=5",
            gradient_colors=[YELLOW, RED]
        )
        current_subtitle = new_subtitle
        
        # 添加边长标签
        a_label = MathTex("a = 3", font_size=36).next_to(triangle.get_edge_center(RIGHT)/2, DOWN, buff=0.3)
        b_label = MathTex("b = 4", font_size=36).next_to(triangle.get_edge_center(UP)/2, RIGHT, buff=0.3)
        c_label = MathTex("c = 5", font_size=36).next_to(triangle.get_vertices()[1]/2 + triangle.get_vertices()[2]/2, UP+LEFT, buff=0.3)
        
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)
        
        # 4. 验证勾股定理
        new_subtitle = self.update_subtitle_with_style(
            current_subtitle, 
            "验证：3² + 4² = 5²，即 9 + 16 = 25",
            gradient_colors=[RED, PURPLE]
        )
        current_subtitle = new_subtitle
        
        # 显示计算过程
        calculation = MathTex(r"3^2 + 4^2 = 9 + 16 = 25 = 5^2", font_size=42)
        calculation.next_to(formula, DOWN, buff=0.5)
        self.play(Write(calculation))
        self.wait(2)
        
        # 5. 结论
        new_subtitle = self.update_subtitle_with_style(
            current_subtitle, 
            "勾股定理得到验证！这是数学中最基本也最重要的定理之一",
            gradient_colors=[PURPLE, BLUE]
        )
        current_subtitle = new_subtitle
        self.wait(2)
        
        # 清除所有内容
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # 结束信息
        conclusion = Text("高级同步字幕演示完成！", color=GREEN, font_size=36)
        self.play(Write(conclusion))
        self.wait(2)
    
    def update_subtitle_with_style(self, current_subtitle, new_text, gradient_colors=None):
        """更新字幕内容，支持渐变色等样式"""
        new_subtitle = Text(new_text, font_size=30)
        
        # 应用渐变色
        if gradient_colors:
            new_subtitle.set_color_by_gradient(*gradient_colors)
        
        new_subtitle.move_to(current_subtitle.get_center())
        self.play(ReplacementTransform(current_subtitle, new_subtitle))
        return new_subtitle


# 运行命令：
# manim -pql synchronized_subtitles.py SynchronizedSubtitles
# manim -pql synchronized_subtitles.py AdvancedSynchronizedSubtitles