#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manim中文自动补丁增强版

这个补丁会自动修改Manim的核心类，使其支持中文和各种符号，无需用户手动导入或继承。
只需将此文件放在项目目录中，并在启动脚本中导入一次即可永久生效。

使用方法：
在项目的任何位置添加：
import patch.auto_chinese_patch

之后就可以直接使用所有Manim类，它们都将自动支持中文。
"""

from manim import *
import re
import types
import inspect

# 定义中文字符和标点的正则表达式
CHINESE_PATTERN = re.compile(r'[\u4e00-\u9fff\uff00-\uffef]+')

# 默认中文字体
DEFAULT_CHINESE_FONT = "SimHei"

# 创建支持中文的TeX模板
def create_ctex_template():
    """创建支持中文的TeX模板"""
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{CJKutf8}")
    template.add_to_preamble(r"\usepackage{xeCJK}")
    template.add_to_preamble(r"\setCJKmainfont{SimSun}")
    template.add_to_document(r"\begin{CJK}{UTF8}{gbsn}")
    template.add_to_document(r"\end{CJK}")
    return template

# 创建CTEX模板实例
CTEX_TEMPLATE = create_ctex_template()

def _split_chinese_and_math(tex_string):
    """将字符串分割为中文和数学部分"""
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

# 保存原始的MathTex.__init__方法
original_mathtex_init = MathTex.__init__

# 增强的MathTex.__init__方法
def enhanced_mathtex_init(self, tex_string, **kwargs):
    """增强的MathTex初始化方法，支持中文"""
    # 检查是否包含中文
    if CHINESE_PATTERN.search(tex_string):
        # 先调用原始初始化方法创建一个空的MathTex对象
        original_mathtex_init(self, "", **kwargs)
        
        # 分离中文和LaTeX部分
        parts = _split_chinese_and_math(tex_string)
        
        # 创建组合对象
        combined = VGroup()
        
        # 处理每个部分
        for part_type, content in parts:
            if part_type == "chinese":
                # 中文部分使用Text
                obj = Text(content, font=DEFAULT_CHINESE_FONT)
            else:  # part_type == "math"
                # 数学部分使用原始的MathTex
                if content.strip():
                    try:
                        obj = MathTex(content, **kwargs)
                    except Exception as e:
                        print(f"MathTex错误: {e}，使用Text替代")
                        obj = Text(content, font=DEFAULT_CHINESE_FONT)
                else:
                    obj = Text("", font=DEFAULT_CHINESE_FONT)
            
            # 添加到组合中
            combined.add(obj)
        
        # 水平排列所有部分
        if len(combined) > 0:
            combined.arrange(RIGHT, buff=0.05)
            
            # 清除现有的子对象并添加combined
            self.submobjects = []
            self.add(combined)
    else:
        # 不包含中文，使用原始的MathTex.__init__
        original_mathtex_init(self, tex_string, **kwargs)

# 保存原始的Tex.__init__方法
original_tex_init = Tex.__init__

# 增强的Tex.__init__方法
def enhanced_tex_init(self, tex_string, **kwargs):
    """增强的Tex初始化方法，支持中文"""
    # 检查是否包含中文
    if CHINESE_PATTERN.search(tex_string):
        # 先调用原始初始化方法创建一个空的Tex对象
        original_tex_init(self, "", **kwargs)
        
        # 尝试使用CTEX模板
        try:
            # 创建一个临时Tex对象
            if 'tex_template' not in kwargs:
                kwargs['tex_template'] = CTEX_TEMPLATE
            temp_tex = Tex.__new__(Tex)
            original_tex_init(temp_tex, tex_string, **kwargs)
            
            # 复制临时对象的属性到self
            self.submobjects = []
            self.add(*temp_tex.submobjects)
        except Exception as e:
            print(f"Tex错误: {e}，使用Text和MathTex组合替代")
            # 回退到分离中文和数学部分的方法
            self.submobjects = []
            
            # 分离中文和LaTeX部分
            parts = _split_chinese_and_math(tex_string)
            
            # 创建组合对象
            combined = VGroup()
            
            # 处理每个部分
            for part_type, content in parts:
                if part_type == "chinese":
                    # 中文部分使用Text
                    obj = Text(content, font=DEFAULT_CHINESE_FONT)
                else:  # part_type == "math"
                    # 数学部分使用Tex
                    if content.strip():
                        try:
                            obj = Tex(content, **kwargs)
                        except Exception:
                            obj = Text(content, font=DEFAULT_CHINESE_FONT)
                    else:
                        obj = Text("", font=DEFAULT_CHINESE_FONT)
                
                # 添加到组合中
                combined.add(obj)
            
            # 水平排列所有部分
            if len(combined) > 0:
                combined.arrange(RIGHT, buff=0.05)
                self.add(combined)
    else:
        # 不包含中文，使用原始的Tex.__init__
        original_tex_init(self, tex_string, **kwargs)

# 应用补丁
def apply_auto_chinese_patch():
    """应用自动中文补丁到Manim"""
    # 设置Text类默认字体
    Text.set_default(font=DEFAULT_CHINESE_FONT)
    
    # 替换MathTex.__init__方法
    MathTex.__init__ = enhanced_mathtex_init
    
    # 替换Tex.__init__方法
    Tex.__init__ = enhanced_tex_init
    
    print("已应用全自动中文补丁增强版，所有Manim类现在都支持中文和符号混合使用")
    return True

# 自动应用补丁
apply_auto_chinese_patch()

# 测试场景
class AutoChinesePatchTest(Scene):
    def construct(self):
        # 测试标题
        title = Text("全自动中文补丁增强版测试", color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # 测试1：纯中文文本 - 直接使用Text
        test1_title = Text("1. 纯中文文本 - Text", color=GREEN)
        test1_title.next_to(title, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test1 = Text("这是一段中文文本，直接使用Text类")
        test1.next_to(test1_title, DOWN, buff=0.3)
        self.play(Write(test1_title))
        self.play(Write(test1))
        
        # 测试2：纯数学公式 - 直接使用MathTex
        test2_title = Text("2. 纯数学公式 - MathTex", color=GREEN)
        test2_title.next_to(test1, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test2 = MathTex(r"E = mc^2")
        test2.next_to(test2_title, DOWN, buff=0.3)
        self.play(Write(test2_title))
        self.play(Write(test2))
        
        # 测试3：中文和数学混合 - 直接使用MathTex
        test3_title = Text("3. 中文和数学混合 - MathTex", color=GREEN)
        test3_title.next_to(test2, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test3 = MathTex("爱因斯坦方程：E = mc^2")
        test3.next_to(test3_title, DOWN, buff=0.3)
        self.play(Write(test3_title))
        self.play(Write(test3))
        
        # 测试4：复杂公式和中文混合 - 直接使用MathTex
        test4_title = Text("4. 复杂公式和中文 - MathTex", color=GREEN)
        test4_title.next_to(test3, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test4 = MathTex(r"勾股定理：$a^2 + b^2 = c^2$，其中$a$和$b$是直角边，$c$是斜边")
        test4.next_to(test4_title, DOWN, buff=0.3)
        self.play(Write(test4_title))
        self.play(Write(test4))
        
        # 测试5：使用Tex
        test5_title = Text("5. 使用Tex类", color=GREEN)
        test5_title.next_to(test4, DOWN, buff=0.5).align_to(LEFT + 2*UP)
        test5 = Tex(r"这是使用Tex类的中文和公式：$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$")
        test5.next_to(test5_title, DOWN, buff=0.3)
        self.play(Write(test5_title))
        self.play(Write(test5))
        
        # 总结
        self.play(FadeOut(test1_title, test1, test2_title, test2, test3_title, test3, test4_title, test4, test5_title, test5))
        
        summary = Text("全自动补丁增强版已成功应用！\n现在可以直接使用所有Manim类\n无需导入或继承特殊类", color=YELLOW)
        self.play(Write(summary))
        
        self.wait(2)

# 使用示例
if __name__ == "__main__":
    print("运行全自动中文补丁增强版测试...")
    # 可以直接运行这个文件来测试
    import subprocess
    import sys
    
    try:
        subprocess.run([sys.executable, "-m", "manim", __file__, "AutoChinesePatchTest", "-pql"], check=True)
        print("测试完成！")
    except subprocess.CalledProcessError as e:
        print(f"测试失败：{e}")