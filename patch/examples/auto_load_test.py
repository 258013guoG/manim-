#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动加载中文补丁测试

这个示例不需要导入任何补丁，中文支持会自动加载。
只需确保sitecustomize.py文件位于项目根目录。
"""

# 只导入manim，不导入任何补丁
from manim import *

# 创建场景
class AutoLoadTest(Scene):
    def construct(self):
        # 标题
        title = Text("自动加载中文补丁测试", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 纯中文文本
        text1 = Text("1. 这是纯中文文本，无需导入任何补丁")
        text1.next_to(title, DOWN, buff=1)
        self.play(Write(text1))
        
        # 简单数学公式
        formula1 = MathTex(r"2. a^2 + b^2 = c^2")
        formula1.next_to(text1, DOWN, buff=0.5)
        self.play(Write(formula1))
        
        # 简单的中文和数学混合
        text2 = Text("3. 圆的面积公式是：")
        text2.next_to(formula1, DOWN, buff=0.5)
        self.play(Write(text2))
        
        formula2 = MathTex(r"S = \pi r^2")
        formula2.next_to(text2, RIGHT, buff=0.2)
        self.play(Write(formula2))
        
        # 尝试直接在MathTex中使用中文
        try:
            formula3 = MathTex(r"4. 勾股定理：a^2 + b^2 = c^2")
            formula3.next_to(text2, DOWN, buff=0.8)
            self.play(Write(formula3))
        except Exception as e:
            error_text = Text(f"4. MathTex中文测试失败", color=RED)
            error_text.next_to(text2, DOWN, buff=0.8)
            self.play(Write(error_text))
        
        # 尝试使用Tex类
        try:
            tex1 = Tex("5. 使用Tex类：爱因斯坦方程 $E = mc^2$")
            tex1.next_to(formula3 if 'formula3' in locals() else error_text, DOWN, buff=0.5)
            self.play(Write(tex1))
        except Exception as e:
            error_text2 = Text(f"5. Tex中文测试失败", color=RED)
            error_text2.next_to(formula3 if 'formula3' in locals() else error_text, DOWN, buff=0.5)
            self.play(Write(error_text2))
        
        # 总结
        summary = Text("中文补丁已自动加载！\n无需任何导入语句", color=GREEN)
        summary.next_to(tex1 if 'tex1' in locals() else error_text2, DOWN, buff=1)
        self.play(Write(summary))
        
        self.wait(2)