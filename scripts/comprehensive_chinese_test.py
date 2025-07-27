#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面测试Manim中文补丁的各项功能

这个脚本用于全面测试Manim中文补丁的各项功能，包括：
1. 纯中文文本
2. 中文与数学公式混合
3. 不同的文本类（Text, Tex, MathTex等）
4. 不同的字体设置
5. 动画效果
"""

from manim import *

class ComprehensiveChineseTest(Scene):
    def construct(self):
        # 标题
        title = Text("Manim中文补丁功能测试", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # 测试1：纯中文文本
        test1_title = Text("1. 纯中文文本", color=GREEN)
        test1_title.next_to(title, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test1 = Text("你好，这是一段中文文本。")
        test1.next_to(test1_title, DOWN, buff=0.3)
        self.play(Write(test1_title))
        self.play(Write(test1))
        
        # 测试2：纯数学公式
        test2_title = Text("2. 纯数学公式", color=GREEN)
        test2_title.next_to(test1, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test2 = MathTex(r"E = mc^2")
        test2.next_to(test2_title, DOWN, buff=0.3)
        self.play(Write(test2_title))
        self.play(Write(test2))
        
        # 测试3：中文和数学混合
        test3_title = Text("3. 中文和数学混合", color=GREEN)
        test3_title.next_to(test2, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test3 = MathTex(r"\text{爱因斯坦方程：}E = mc^2")
        test3.next_to(test3_title, DOWN, buff=0.3)
        self.play(Write(test3_title))
        self.play(Write(test3))
        
        # 测试4：复杂公式和中文混合
        test4_title = Text("4. 复杂公式和中文", color=GREEN)
        test4_title.next_to(test3, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test4 = MathTex(r"\text{勾股定理：}a^2 + b^2 = c^2\text{，其中}a\text{和}b\text{是直角边，}c\text{是斜边}")
        test4.next_to(test4_title, DOWN, buff=0.3)
        self.play(Write(test4_title))
        self.play(Write(test4))
        
        # 清除前面的内容
        self.play(FadeOut(test1_title, test1, test2_title, test2, test3_title, test3, test4_title, test4))
        
        # 测试5：不同字体
        test5_title = Text("5. 不同字体测试", color=GREEN)
        test5_title.next_to(title, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        self.play(Write(test5_title))
        
        # 默认字体（SimHei）
        test5_1 = Text("默认字体（SimHei）：你好，世界！", font_size=36)
        test5_1.next_to(test5_title, DOWN, buff=0.3)
        self.play(Write(test5_1))
        
        # 微软雅黑
        test5_2 = Text("微软雅黑：你好，世界！", font="Microsoft YaHei", font_size=36)
        test5_2.next_to(test5_1, DOWN, buff=0.3)
        self.play(Write(test5_2))
        
        # 宋体
        test5_3 = Text("宋体：你好，世界！", font="SimSun", font_size=36)
        test5_3.next_to(test5_2, DOWN, buff=0.3)
        self.play(Write(test5_3))
        
        # 清除前面的内容
        self.play(FadeOut(test5_title, test5_1, test5_2, test5_3))
        
        # 测试6：动画效果
        test6_title = Text("6. 动画效果测试", color=GREEN)
        test6_title.next_to(title, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        self.play(Write(test6_title))
        
        # 创建一个中文文本
        test6_text = Text("动画效果测试", font_size=48)
        test6_text.next_to(test6_title, DOWN, buff=0.5)
        self.play(Write(test6_text))
        
        # 各种动画效果
        self.play(test6_text.animate.scale(1.5))
        self.play(test6_text.animate.rotate(PI/4))
        self.play(test6_text.animate.set_color(RED))
        self.play(test6_text.animate.set_color_by_gradient(BLUE, GREEN, YELLOW))
        self.play(test6_text.animate.to_edge(RIGHT))
        self.play(test6_text.animate.to_edge(LEFT))
        self.play(test6_text.animate.to_edge(DOWN))
        
        # 清除所有内容
        self.play(FadeOut(title, test6_title, test6_text))
        
        # 总结
        summary = Text("Manim中文补丁测试完成！\n所有功能正常工作", color=YELLOW)
        self.play(Write(summary))
        self.wait(2)

if __name__ == '__main__':
    print("开始全面测试Manim中文补丁...")
    print("如果能看到这条中文消息，说明Python环境正常支持中文。")
    print("\n如果没有报错，并且能看到'Manim中文补丁已自动加载'的消息，说明补丁安装成功。")
    print("\n您可以通过运行：python -m manim comprehensive_chinese_test.py ComprehensiveChineseTest -p 来测试完整功能。")