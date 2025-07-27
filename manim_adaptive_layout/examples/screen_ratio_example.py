#!/usr/bin/env python

"""
Mainim自适应布局系统屏幕比例示例

演示了如何正确设置不同平台的屏幕比例，避免内容被挤压变形

渲染命令：
    抖音竖屏: manim -pql --resolution=1080,1920 screen_ratio_example.py TiktokExample
    小红书: manim -pql --resolution=1080,1440 screen_ratio_example.py XiaohongshuExample
    标准横屏: manim -pql --resolution=1920,1080 screen_ratio_example.py StandardExample

注意：必须使用--resolution参数指定正确的分辨率，否则可能导致屏幕比例不正确
"""

from manim import *

class TiktokExample(Scene):
    """抖音竖屏示例 (9:16)"""
    def construct(self):
        # 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 添加标题
        title = Text("抖音竖屏 (9:16)", font_size=48).to_edge(UP)
        self.add(title)
        
        # 添加屏幕比例信息
        info = Text(f"分辨率: 1080x1920\n比例: 9:16", font_size=36).next_to(title, DOWN, buff=0.5)
        self.add(info)
        
        # 添加网格背景以便观察比例
        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-10, 10, 1))
        self.add(grid)
        
        # 添加中心点标记
        center_dot = Dot(color=RED)
        center_label = Text("中心点", font_size=36, color=RED).next_to(center_dot, DOWN)
        self.add(center_dot, center_label)
        
        # 添加水平和垂直参考线
        h_line = Line(LEFT*10, RIGHT*10, color=YELLOW)
        v_line = Line(UP*10, DOWN*10, color=YELLOW)
        self.add(h_line, v_line)
        
        # 添加提示文本
        note = Text(
            "注意：必须使用正确的分辨率参数\nmanim -pql --resolution=1080,1920", 
            font_size=32,
            color=GREEN
        ).to_edge(DOWN, buff=1)
        self.add(note)


class XiaohongshuExample(Scene):
    """小红书方屏示例 (3:4)"""
    def construct(self):
        # 设置小红书方屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="xiaohongshu", show_safe_zone=True
        )
        
        # 添加标题
        title = Text("小红书方屏 (3:4)", font_size=48).to_edge(UP)
        self.add(title)
        
        # 添加屏幕比例信息
        info = Text(f"分辨率: 1080x1440\n比例: 3:4", font_size=36).next_to(title, DOWN, buff=0.5)
        self.add(info)
        
        # 添加网格背景以便观察比例
        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-10, 10, 1))
        self.add(grid)
        
        # 添加中心点标记
        center_dot = Dot(color=RED)
        center_label = Text("中心点", font_size=36, color=RED).next_to(center_dot, DOWN)
        self.add(center_dot, center_label)
        
        # 添加水平和垂直参考线
        h_line = Line(LEFT*10, RIGHT*10, color=YELLOW)
        v_line = Line(UP*10, DOWN*10, color=YELLOW)
        self.add(h_line, v_line)
        
        # 添加提示文本
        note = Text(
            "注意：必须使用正确的分辨率参数\nmanim -pql --resolution=1080,1440", 
            font_size=32,
            color=GREEN
        ).to_edge(DOWN, buff=1)
        self.add(note)


class StandardExample(Scene):
    """标准横屏示例 (16:9)"""
    def construct(self):
        # 设置标准横屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="standard", show_safe_zone=True
        )
        
        # 添加标题
        title = Text("标准横屏 (16:9)", font_size=48).to_edge(UP)
        self.add(title)
        
        # 添加屏幕比例信息
        info = Text(f"分辨率: 1920x1080\n比例: 16:9", font_size=36).next_to(title, DOWN, buff=0.5)
        self.add(info)
        
        # 添加网格背景以便观察比例
        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-10, 10, 1))
        self.add(grid)
        
        # 添加中心点标记
        center_dot = Dot(color=RED)
        center_label = Text("中心点", font_size=36, color=RED).next_to(center_dot, DOWN)
        self.add(center_dot, center_label)
        
        # 添加水平和垂直参考线
        h_line = Line(LEFT*10, RIGHT*10, color=YELLOW)
        v_line = Line(UP*10, DOWN*10, color=YELLOW)
        self.add(h_line, v_line)
        
        # 添加提示文本
        note = Text(
            "注意：必须使用正确的分辨率参数\nmanim -pql --resolution=1920,1080", 
            font_size=32,
            color=GREEN
        ).to_edge(DOWN, buff=1)
        self.add(note)