#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manim中文数学公式示例
展示如何在实际项目中使用中文LaTeX补丁
"""

from manim import *
import sys
import os

# 导入中文补丁
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from patch.manim_chinese_latex_patch import ChineseText, ChineseMath, ChineseTex, apply_chinese_patch

# 确保已应用中文补丁
apply_chinese_patch()

# 示例1：勾股定理演示
class PythagoreanTheoremDemo(Scene):
    def construct(self):
        # 标题
        title = ChineseText("勾股定理可视化", color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # 创建一个直角三角形
        triangle = Polygon(
            ORIGIN, RIGHT * 3, UP * 4,
            color=WHITE, fill_opacity=0.2
        )
        
        # 添加边的标签
        a_label = ChineseText("a = 3", font_size=24)
        a_label.next_to(triangle, DOWN, buff=0.2)
        
        b_label = ChineseText("b = 4", font_size=24)
        b_label.next_to(triangle, RIGHT, buff=0.2)
        
        c_label = ChineseText("c = 5", font_size=24)
        c_label.next_to(triangle, UP + LEFT, buff=0.2)
        
        # 显示三角形和标签
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        
        # 显示公式
        formula = ChineseMath("勾股定理：a^2 + b^2 = c^2")
        formula.next_to(triangle, DOWN * 3)
        self.play(Write(formula))
        
        # 计算验证
        calc1 = ChineseMath("a^2 + b^2 = 3^2 + 4^2 = 9 + 16 = 25")
        calc2 = ChineseMath("c^2 = 5^2 = 25")
        calc3 = ChineseText("∴ a² + b² = c²，勾股定理成立！")
        
        calcs = VGroup(calc1, calc2, calc3).arrange(DOWN, aligned_edge=LEFT)
        calcs.next_to(formula, DOWN, buff=0.5)
        
        self.play(Write(calc1))
        self.play(Write(calc2))
        self.play(Write(calc3))
        
        self.wait(2)

# 示例2：圆周率演示
class PiDemonstration(Scene):
    def construct(self):
        # 标题
        title = ChineseText("圆周率(π)可视化", color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # 创建一个圆
        circle = Circle(radius=2, color=WHITE)
        
        # 添加直径
        diameter = Line(circle.get_left(), circle.get_right(), color=YELLOW)
        
        # 添加标签
        d_label = ChineseText("直径(d)", font_size=24, color=YELLOW)
        d_label.next_to(diameter, DOWN, buff=0.2)
        
        c_label = ChineseText("周长(C)", font_size=24, color=WHITE)
        c_label.next_to(circle, UP, buff=0.2)
        
        # 显示圆和标签
        self.play(Create(circle))
        self.play(Create(diameter))
        self.play(Write(d_label), Write(c_label))
        
        # 显示公式
        formula = ChineseMath("π = \\frac{C}{d} = \\frac{周长}{直径}")
        formula.next_to(circle, DOWN * 3)
        self.play(Write(formula))
        
        # 计算示例
        calc1 = ChineseMath("例如：当半径r = 1时")
        calc2 = ChineseMath("周长C = 2πr = 2π")
        calc3 = ChineseMath("直径d = 2r = 2")
        calc4 = ChineseMath("π = \\frac{C}{d} = \\frac{2π}{2} = π ≈ 3.14159...")
        
        calcs = VGroup(calc1, calc2, calc3, calc4).arrange(DOWN, aligned_edge=LEFT)
        calcs.next_to(formula, DOWN, buff=0.5)
        
        self.play(Write(calc1))
        self.play(Write(calc2))
        self.play(Write(calc3))
        self.play(Write(calc4))
        
        self.wait(2)

# 示例3：欧拉公式演示
class EulerFormulaDemo(Scene):
    def construct(self):
        # 标题
        title = ChineseText("欧拉公式可视化", color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # 欧拉公式
        formula = MathTex(r"e^{i\pi} + 1 = 0")
        self.play(Write(formula))
        
        # 解释
        explanation = VGroup(
            ChineseText("欧拉公式被誉为\"数学中最美丽的公式\"，它将数学中五个基本常数联系在一起："),
            ChineseMath("• e：自然对数的底数，约等于2.71828..."),
            ChineseMath("• i：虚数单位，i^2 = -1"),
            ChineseMath("• π：圆周率，约等于3.14159..."),
            ChineseMath("• 1：乘法单位元"),
            ChineseMath("• 0：加法单位元")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        explanation.next_to(formula, DOWN, buff=0.5)
        self.play(Write(explanation, run_time=3))
        
        # 复平面可视化
        plane = ComplexPlane().scale(1.5)
        plane.next_to(explanation, DOWN, buff=0.5)
        self.play(Create(plane))
        
        # 单位圆
        unit_circle = Circle(radius=1.5, color=YELLOW)
        unit_circle.move_to(plane.get_center())
        self.play(Create(unit_circle))
        
        # 解释欧拉公式的几何意义
        geometric_meaning = ChineseText("几何意义：e^(iθ)表示单位圆上的点，当θ=π时，点位于(-1,0)")
        geometric_meaning.next_to(plane, DOWN, buff=0.5)
        self.play(Write(geometric_meaning))
        
        # 在复平面上标记点
        dot = Dot(plane.n2p(-1), color=RED)
        self.play(Create(dot))
        
        self.wait(2)

# 使用示例
if __name__ == "__main__":
    print("运行中文数学公式示例...")
    # 可以直接运行这个文件来测试
    import subprocess
    
    try:
        # 运行勾股定理演示
        print("\n运行勾股定理演示...")
        subprocess.run([sys.executable, "-m", "manim", __file__, "PythagoreanTheoremDemo", "-pql"], check=True)
        
        # 运行圆周率演示
        print("\n运行圆周率演示...")
        subprocess.run([sys.executable, "-m", "manim", __file__, "PiDemonstration", "-pql"], check=True)
        
        # 运行欧拉公式演示
        print("\n运行欧拉公式演示...")
        subprocess.run([sys.executable, "-m", "manim", __file__, "EulerFormulaDemo", "-pql"], check=True)
        
        print("\n所有示例运行完成！")
    except subprocess.CalledProcessError as e:
        print(f"示例运行失败：{e}")