#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全自动中文补丁增强版示例

这个示例展示了如何使用全自动中文补丁增强版，无需导入特殊类或继承。
只需导入auto_chinese_patch一次，之后所有Manim类都将自动支持中文。
"""

# 导入Manim
from manim import *

# 导入全自动中文补丁增强版（只需导入一次）
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import patch.auto_chinese_patch

# 现在可以直接使用所有Manim类，它们都将自动支持中文
class AutoPatchDemo(Scene):
    def construct(self):
        # 标题 - 直接使用Text
        title = Text("全自动中文补丁演示", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 示例1：直接使用Text显示中文
        text1 = Text("1. 直接使用Text显示中文，无需设置字体")
        text1.next_to(title, DOWN, buff=1)
        self.play(Write(text1))
        
        # 示例2：直接使用MathTex显示数学公式
        text2 = Text("2. 直接使用MathTex显示数学公式")
        text2.next_to(text1, DOWN, buff=0.5)
        formula1 = MathTex(r"\int_{a}^{b} f(x) \, dx = F(b) - F(a)")
        formula1.next_to(text2, DOWN, buff=0.3)
        self.play(Write(text2))
        self.play(Write(formula1))
        
        # 示例3：直接使用MathTex显示中文和数学公式混合内容
        text3 = Text("3. 直接使用MathTex显示中文和数学公式混合内容")
        text3.next_to(formula1, DOWN, buff=0.5)
        formula2 = MathTex("牛顿第二定律：$F = ma$，其中$F$是力，$m$是质量，$a$是加速度")
        formula2.next_to(text3, DOWN, buff=0.3)
        self.play(Write(text3))
        self.play(Write(formula2))
        
        # 示例4：使用特殊符号和中文混合
        text4 = Text("4. 使用特殊符号和中文混合")
        text4.next_to(formula2, DOWN, buff=0.5)
        formula3 = MathTex("复数：$z = a + bi$，其中$i^2 = -1$，欧拉公式：$e^{i\pi} + 1 = 0$")
        formula3.next_to(text4, DOWN, buff=0.3)
        self.play(Write(text4))
        self.play(Write(formula3))
        
        # 示例5：使用Tex类显示中文和LaTeX混合内容
        text5 = Text("5. 使用Tex类显示中文和LaTeX混合内容")
        text5.next_to(formula3, DOWN, buff=0.5)
        formula4 = Tex("爱因斯坦质能方程：$E = mc^2$，\\其中$E$是能量，$m$是质量，$c$是光速")
        formula4.next_to(text5, DOWN, buff=0.3)
        self.play(Write(text5))
        self.play(Write(formula4))
        
        # 总结
        summary = Text("全自动补丁增强版\n支持任意中文和符号混合使用\n无需导入特殊类或继承", color=GREEN)
        summary.next_to(formula4, DOWN, buff=1)
        self.play(Write(summary))
        
        self.wait(2)

if __name__ == "__main__":
    import subprocess
    subprocess.run(["manim", "-pql", __file__, "AutoPatchDemo"])