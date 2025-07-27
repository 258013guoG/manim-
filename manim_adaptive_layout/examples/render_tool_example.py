# -*- coding: utf-8 -*-
"""
渲染工具示例

这个脚本展示了如何使用自适应布局系统和渲染工具。

渲染命令：
    # 使用渲染工具（自动检测平台设置）
    manim-render render_tool_example.py TiktokExample -pql
    manim-render render_tool_example.py XiaohongshuExample -pql
    manim-render render_tool_example.py StandardExample -pql
    
    # 传统方式（需要手动指定分辨率）
    manim -pql --resolution=1080,1920 render_tool_example.py TiktokExample
    manim -pql --resolution=1080,1440 render_tool_example.py XiaohongshuExample
    manim -pql --resolution=1920,1080 render_tool_example.py StandardExample
"""

from manim import *
from manim_adaptive_layout import AdaptiveLayoutSystem

class TiktokExample(Scene):
    def construct(self):
        # 设置抖音竖屏比例
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 添加标题
        title = Text("抖音竖屏示例 (9:16)", font_size=48)
        title.to_edge(UP, buff=1)
        self.add(title)
        
        # 添加屏幕比例信息
        info = Text(f"屏幕比例: {config.frame_width}:{config.frame_height}\n分辨率: {config.pixel_width}x{config.pixel_height}", 
                   font_size=36)
        info.next_to(title, DOWN, buff=1)
        self.add(info)
        
        # 添加说明文字
        note = Text("使用渲染工具自动检测平台设置", font_size=36, color=YELLOW)
        note.next_to(info, DOWN, buff=1)
        self.add(note)
        
        # 添加网格背景以便观察屏幕比例
        grid = NumberPlane()
        self.add(grid)
        
        # 添加中心点标记
        center_dot = Dot(color=RED)
        self.add(center_dot)
        
        # 添加平台元素
        AdaptiveLayoutSystem.add_platform_elements(self, platform="tiktok")
        
        self.wait(2)

class XiaohongshuExample(Scene):
    def construct(self):
        # 设置小红书方屏比例
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="xiaohongshu", show_safe_zone=True
        )
        
        # 添加标题
        title = Text("小红书方屏示例 (3:4)", font_size=48)
        title.to_edge(UP, buff=1)
        self.add(title)
        
        # 添加屏幕比例信息
        info = Text(f"屏幕比例: {config.frame_width}:{config.frame_height}\n分辨率: {config.pixel_width}x{config.pixel_height}", 
                   font_size=36)
        info.next_to(title, DOWN, buff=1)
        self.add(info)
        
        # 添加说明文字
        note = Text("使用渲染工具自动检测平台设置", font_size=36, color=YELLOW)
        note.next_to(info, DOWN, buff=1)
        self.add(note)
        
        # 添加网格背景以便观察屏幕比例
        grid = NumberPlane()
        self.add(grid)
        
        # 添加中心点标记
        center_dot = Dot(color=RED)
        self.add(center_dot)
        
        # 添加平台元素
        AdaptiveLayoutSystem.add_platform_elements(self, platform="xiaohongshu")
        
        self.wait(2)

class StandardExample(Scene):
    def construct(self):
        # 设置标准横屏比例
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="standard", show_safe_zone=True
        )
        
        # 添加标题
        title = Text("标准横屏示例 (16:9)", font_size=48)
        title.to_edge(UP, buff=1)
        self.add(title)
        
        # 添加屏幕比例信息
        info = Text(f"屏幕比例: {config.frame_width}:{config.frame_height}\n分辨率: {config.pixel_width}x{config.pixel_height}", 
                   font_size=36)
        info.next_to(title, DOWN, buff=1)
        self.add(info)
        
        # 添加说明文字
        note = Text("使用渲染工具自动检测平台设置", font_size=36, color=YELLOW)
        note.next_to(info, DOWN, buff=1)
        self.add(note)
        
        # 添加网格背景以便观察屏幕比例
        grid = NumberPlane()
        self.add(grid)
        
        # 添加中心点标记
        center_dot = Dot(color=RED)
        self.add(center_dot)
        
        self.wait(2)