#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全自动中文补丁增强版快速入门示例

这个示例展示了使用全自动中文补丁增强版的最简单方法。
只需两行代码，即可让Manim支持中文和各种符号的混合使用。
"""

# 导入Manim
from manim import *

# 导入全自动中文补丁增强版（只需这一行）
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import patch.auto_chinese_patch

# 创建场景
class QuickStartDemo(Scene):
    def construct(self):
        # 直接使用Text显示中文
        text = Text("你好，世界！")
        self.play(Write(text))
        
        # 直接使用MathTex显示中文和数学公式混合内容
        formula = MathTex("勾股定理：$a^2 + b^2 = c^2$")
        formula.next_to(text, DOWN)
        self.play(Write(formula))
        
        # 直接使用Tex显示中文和LaTeX混合内容
        tex = Tex("爱因斯坦：$E = mc^2$")
        tex.next_to(formula, DOWN)
        self.play(Write(tex))
        
        # 显示说明
        note = Text("全自动补丁增强版\n随意编码都不会出错", color=GREEN)
        note.next_to(tex, DOWN, buff=1)
        self.play(Write(note))
        
        self.wait(2)

if __name__ == "__main__":
    import subprocess
    subprocess.run(["manim", "-pql", __file__, "QuickStartDemo"])