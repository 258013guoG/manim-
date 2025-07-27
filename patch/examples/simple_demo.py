#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的中文补丁使用示例
"""

from manim import *

# 导入中文补丁
# 注意：导入时会自动应用补丁，设置Text类的默认字体为中文字体
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from patch import ChineseText, ChineseMath

class SimpleChineseDemo(Scene):
    def construct(self):
        # 使用ChineseText显示纯中文
        title = ChineseText("中文补丁演示", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 使用普通Text类（已被补丁修改为使用中文字体）
        text1 = Text("这是普通的Text类，现在也支持中文了")
        text1.next_to(title, DOWN, buff=1)
        self.play(Write(text1))
        
        # 使用ChineseMath显示中文和数学公式混合内容
        formula1 = ChineseMath(r"数学公式示例：$E = mc^2$")
        formula1.next_to(text1, DOWN, buff=0.5)
        self.play(Write(formula1))
        
        formula2 = ChineseMath(r"复杂公式：$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$，这是牛顿-莱布尼茨公式")
        formula2.next_to(formula1, DOWN, buff=0.5)
        self.play(Write(formula2))
        
        # 创建一个提示
        tip = ChineseText("补丁已成功应用！", color=GREEN)
        tip.next_to(formula2, DOWN, buff=1)
        self.play(Write(tip))
        
        self.wait(2)

if __name__ == "__main__":
    import subprocess
    subprocess.run(["manim", "-pql", __file__, "SimpleChineseDemo"])