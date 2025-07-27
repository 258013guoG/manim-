#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manim中文支持工具集
提供全面的Manim中文LaTeX支持解决方案
"""

from manim import *
import re
import os
import sys

# 定义中文字符和标点的正则表达式
CHINESE_PATTERN = re.compile(r'[\u4e00-\u9fff\uff00-\uffef]+')

# 创建支持中文的TeX模板
def create_ctex_template():
    """创建支持中文的TeX模板"""
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{CJKutf8}")
    template.add_to_preamble(r"\usepackage{xeCJK}")
    template.add_to_preamble(r"\setCJKmainfont{SimSun}")
    template.add_to_document(r"\begin{CJK}{UTF8}{gbsn}")
    # 在文档末尾添加结束标记
    template.add_to_document(r"\end{CJK}")
    return template

# 创建CTEX模板实例
CTEX_TEMPLATE = create_ctex_template()

# 设置默认中文字体
DEFAULT_CHINESE_FONT = "SimHei"

class ChineseMath(VMobject):
    """
    ChineseMath类 - 用于替代MathTex，支持中文和数学公式混合使用
    自动检测中文字符，并使用Text类处理中文，使用MathTex处理数学公式
    """
    def __init__(self, tex_string, font=DEFAULT_CHINESE_FONT, **kwargs):
        super().__init__(**kwargs)
        
        # 分离中文和LaTeX部分
        parts = self._split_chinese_and_math(tex_string)
        
        # 创建组合对象
        combined = VGroup()
        
        # 处理每个部分
        for part_type, content in parts:
            if part_type == "chinese":
                # 中文部分使用Text
                obj = Text(content, font=font)
            else:  # part_type == "math"
                # 数学部分使用MathTex
                # 确保内容不为空且不仅包含空白字符
                if content.strip():
                    try:
                        obj = MathTex(content)
                    except Exception as e:
                        print(f"MathTex错误: {e}，使用Text替代")
                        obj = Text(content, font=font)
                else:
                    # 如果内容为空，创建一个空的Text对象
                    obj = Text("", font=font)
            
            # 添加到组合中
            combined.add(obj)
        
        # 水平排列所有部分
        if len(combined) > 0:
            combined.arrange(RIGHT, buff=0.05)
            
            # 复制组合对象的属性到self
            self.add(combined)
    
    def _split_chinese_and_math(self, tex_string):
        """
        将字符串分割为中文和数学部分
        返回一个列表，每个元素是一个元组(类型, 内容)
        类型可以是"chinese"或"math"
        """
        # 查找所有中文匹配
        matches = list(CHINESE_PATTERN.finditer(tex_string))
        
        if not matches:
            # 如果没有中文，直接返回整个字符串作为数学部分
            return [("math", tex_string)]
        
        # 分割字符串
        parts = []
        last_end = 0
        
        for match in matches:
            start, end = match.span()
            
            # 添加数学部分（如果有）
            if start > last_end:
                math_part = tex_string[last_end:start]
                if math_part.strip():
                    parts.append(("math", math_part))
            
            # 添加中文部分
            chinese_part = tex_string[start:end]
            parts.append(("chinese", chinese_part))
            
            last_end = end
        
        # 添加最后一个数学部分（如果有）
        if last_end < len(tex_string):
            math_part = tex_string[last_end:]
            if math_part.strip():
                parts.append(("math", math_part))
        
        return parts

class ChineseText(Text):
    """增强的Text类，默认使用中文字体"""
    def __init__(self, text, font=DEFAULT_CHINESE_FONT, **kwargs):
        super().__init__(text, font=font, **kwargs)

class ChineseTex(MathTex):
    """
    增强的MathTex类，尝试使用CTEX模板渲染中文
    如果失败，自动回退到ChineseMath
    """
    def __init__(self, tex_string, **kwargs):
        # 检查是否包含中文
        if CHINESE_PATTERN.search(tex_string):
            try:
                # 尝试使用CTEX模板
                super().__init__(tex_string, tex_template=CTEX_TEMPLATE, **kwargs)
            except Exception as e:
                print(f"ChineseTex错误: {e}，回退到ChineseMath")
                # 回退到ChineseMath
                chinese_math = ChineseMath(tex_string, **kwargs)
                self.add(chinese_math)
        else:
            # 不包含中文，直接使用MathTex
            super().__init__(tex_string, **kwargs)

# 应用补丁到Manim
def apply_chinese_patch():
    """应用中文补丁到Manim"""
    # 设置Text类默认字体
    Text.set_default(font=DEFAULT_CHINESE_FONT)
    print("已应用中文补丁，Text类默认字体设置为", DEFAULT_CHINESE_FONT)
    return True

# 自动应用补丁
apply_chinese_patch()

# 创建一个测试场景
class ChinesePatchTest(Scene):
    def construct(self):
        # 测试标题
        title = ChineseText("Manim中文补丁测试", color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # 测试1：纯中文文本
        test1_title = ChineseText("1. 纯中文文本", color=GREEN)
        test1_title.next_to(title, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test1 = ChineseText("这是一段中文文本，使用ChineseText类")
        test1.next_to(test1_title, DOWN, buff=0.3)
        self.play(Write(test1_title))
        self.play(Write(test1))
        
        # 测试2：纯数学公式
        test2_title = ChineseText("2. 纯数学公式", color=GREEN)
        test2_title.next_to(test1, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test2 = MathTex(r"E = mc^2")
        test2.next_to(test2_title, DOWN, buff=0.3)
        self.play(Write(test2_title))
        self.play(Write(test2))
        
        # 测试3：中文和数学混合
        test3_title = ChineseText("3. 中文和数学混合", color=GREEN)
        test3_title.next_to(test2, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test3 = ChineseMath("爱因斯坦方程：E = mc^2")
        test3.next_to(test3_title, DOWN, buff=0.3)
        self.play(Write(test3_title))
        self.play(Write(test3))
        
        # 测试4：尝试使用ChineseTex
        test4_title = ChineseText("4. ChineseTex尝试", color=GREEN)
        test4_title.next_to(test3, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        
        # 这里可能会失败并回退到ChineseMath
        try:
            test4 = ChineseTex(r"\text{勾股定理：}a^2 + b^2 = c^2")
            success_text = "(成功使用CTEX模板)"
        except Exception:
            test4 = ChineseMath("勾股定理：a^2 + b^2 = c^2")
            success_text = "(回退到ChineseMath)"
        
        test4.next_to(test4_title, DOWN, buff=0.3)
        test4_note = ChineseText(success_text, color=YELLOW, font_size=24)
        test4_note.next_to(test4, RIGHT, buff=0.3)
        
        self.play(Write(test4_title))
        self.play(Write(test4))
        self.play(Write(test4_note))
        
        self.wait(2)

# 使用示例
if __name__ == "__main__":
    print("运行Manim中文补丁测试...")
    # 可以直接运行这个文件来测试
    import subprocess
    
    try:
        subprocess.run([sys.executable, "-m", "manim", __file__, "ChinesePatchTest", "-pql"], check=True)
        print("测试完成！")
    except subprocess.CalledProcessError as e:
        print(f"测试失败：{e}")