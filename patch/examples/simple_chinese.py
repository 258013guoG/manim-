#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最简单的中文使用示例 - 无需显式导入补丁
"""

from manim import *

# 只需要设置默认字体为中文字体即可
Text.set_default(font="SimHei")

class SimpleChineseScene(Scene):
    def construct(self):
        # 直接使用Text类显示中文
        title = Text("简单中文演示", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 显示纯中文文本
        text1 = Text("这是直接使用Text类显示的中文文本")
        text1.next_to(title, DOWN, buff=1)
        self.play(Write(text1))
        
        # 显示数学公式
        formula = MathTex(r"E = mc^2")
        formula.next_to(text1, DOWN, buff=0.5)
        self.play(Write(formula))
        
        # 如果需要混合中文和数学公式，可以使用VGroup组合
        chinese_text = Text("爱因斯坦质能方程：")
        math_formula = MathTex(r"E = mc^2")
        mixed_group = VGroup(chinese_text, math_formula).arrange(RIGHT)
        mixed_group.next_to(formula, DOWN, buff=0.5)
        self.play(Write(mixed_group))
        
        # 添加提示
        tip = Text("无需导入补丁，只需设置默认字体！", color=GREEN)
        tip.next_to(mixed_group, DOWN, buff=1)
        self.play(Write(tip))
        
        self.wait(2)

if __name__ == "__main__":
    import subprocess
    subprocess.run(["manim", "-pql", __file__, "SimpleChineseScene"])