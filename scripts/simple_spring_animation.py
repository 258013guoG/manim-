# -*- coding: utf-8 -*-
from manim import *

class SimpleSpringAnimation(Scene):
    def construct(self):
        # 创建标题
        title = Text("简单弹簧动画", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # 创建两个点和连接线
        dot1 = Dot(color=RED).shift(LEFT*3)
        dot2 = Dot(color=BLUE).shift(RIGHT*3)
        line = Line(dot1.get_center(), dot2.get_center(), color=GREEN)
        
        # 添加到场景
        self.play(Create(dot1), Create(dot2), Create(line))
        self.wait(1)
        
        # 使用简单的动画来模拟弹簧效果
        # 移动第一个点
        self.play(dot1.animate.shift(UP*2))
        
        # 第二个点跟随移动，但有弹簧效果
        # 先过冲，然后回弹，最后稳定
        self.play(
            dot2.animate.shift(UP*2.5),  # 过冲
            rate_func=lambda t: smooth(t) * 1.25 if t < 0.8 else 1,
            run_time=0.8
        )
        self.play(
            dot2.animate.shift(DOWN*0.8),  # 回弹
            rate_func=smooth,
            run_time=0.6
        )
        self.play(
            dot2.animate.shift(UP*0.3),  # 小幅过冲
            rate_func=smooth,
            run_time=0.4
        )
        self.play(
            dot2.animate.shift(DOWN*0.1),  # 最终稳定
            rate_func=smooth,
            run_time=0.3
        )
        
        # 更新连接线
        self.play(
            line.animate.put_start_and_end_on(dot1.get_center(), dot2.get_center())
        )
        self.wait(1)
        
        # 再次移动第一个点
        self.play(dot1.animate.shift(DOWN*4))
        
        # 第二个点跟随移动，但有弹簧效果
        self.play(
            dot2.animate.shift(DOWN*5),  # 过冲
            rate_func=lambda t: smooth(t) * 1.25 if t < 0.8 else 1,
            run_time=0.8
        )
        self.play(
            dot2.animate.shift(UP*1.5),  # 回弹
            rate_func=smooth,
            run_time=0.6
        )
        self.play(
            dot2.animate.shift(DOWN*0.5),  # 小幅过冲
            rate_func=smooth,
            run_time=0.4
        )
        
        # 更新连接线
        self.play(
            line.animate.put_start_and_end_on(dot1.get_center(), dot2.get_center())
        )
        self.wait(1)
        
        # 结束信息
        conclusion = Text("简单弹簧动画演示完成！", color=GREEN, font_size=30)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)

# 运行命令：
# manim -pql simple_spring_animation.py SimpleSpringAnimation