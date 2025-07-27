# -*- coding: utf-8 -*-
"""
Manim自适应布局系统

提供全面的布局管理功能，确保内容在不同屏幕比例下正确显示
特别优化了长文本处理和元素自动排列功能
"""

import textwrap
import math
import numpy as np

# 检查是否已导入manim，如果没有则导入
try:
    from manim import *
except ImportError:
    raise ImportError("请先安装manim库: pip install manim")

class AdaptiveLayoutSystem:
    """
    自适应布局系统 - 专为Manim动画设计
    提供全面的布局管理功能，确保内容在不同屏幕比例下正确显示
    特别优化了长文本处理和元素自动排列功能
    """
    
    @staticmethod
    def create_safe_zone(scene, margin=0.5, visible=False, color=RED, opacity=0.2):
        """
        创建安全区域，确保内容不会超出屏幕边界
        
        参数:
            scene: Manim场景对象
            margin: 边距大小
            visible: 是否显示安全区域边界
            color: 安全区域边界颜色
            opacity: 安全区域边界透明度
        
        返回:
            safe_zone: 安全区域矩形对象
            safe_width: 安全区域宽度
            safe_height: 安全区域高度
        """
        frame_width = config.frame_width
        frame_height = config.frame_height
        
        safe_width = frame_width - 2 * margin
        safe_height = frame_height - 2 * margin
        
        safe_zone = Rectangle(
            width=safe_width,
            height=safe_height,
            stroke_color=color,
            stroke_width=2,
            stroke_opacity=opacity if visible else 0
        )
        
        if visible:
            scene.add(safe_zone)
        
        return safe_zone, safe_width, safe_height
    
    @staticmethod
    def auto_fit_text(text_obj, max_width, min_font_size=24, max_font_size=None, step=1):
        """
        自动调整文本大小以适应指定宽度
        
        参数:
            text_obj: 文本对象 (Text, Tex, MathTex等)
            max_width: 最大宽度
            min_font_size: 最小字体大小
            max_font_size: 最大字体大小 (None表示不限制)
            step: 字体大小调整步长
        
        返回:
            调整后的文本对象
        """
        original_font_size = text_obj.font_size
        current_font_size = original_font_size
        
        # 如果文本已经足够小，直接返回
        if text_obj.width <= max_width:
            return text_obj
        
        # 如果文本太宽，逐步减小字体大小
        while text_obj.width > max_width and current_font_size > min_font_size:
            current_font_size -= step
            text_obj.font_size = current_font_size
        
        # 如果设置了最大字体大小且当前字体大小小于最大值，尝试增大
        if max_font_size and current_font_size < max_font_size and text_obj.width < max_width:
            while text_obj.width < max_width and current_font_size < max_font_size:
                current_font_size += step
                text_obj.font_size = current_font_size
                
                # 如果增大后超出最大宽度，回退一步
                if text_obj.width > max_width:
                    current_font_size -= step
                    text_obj.font_size = current_font_size
                    break
        
        return text_obj
    
    @staticmethod
    def auto_wrap_text(text_content, max_width, font_size=36, line_spacing=1.0, **text_kwargs):
        """
        自动换行文本，处理超长文本
        
        参数:
            text_content: 文本内容
            max_width: 最大宽度
            font_size: 字体大小
            line_spacing: 行间距
            **text_kwargs: 传递给Text的其他参数
        
        返回:
            自动换行后的文本对象
        """
        # 创建临时文本对象测量字符宽度
        temp_text = Text("A", font_size=font_size, **text_kwargs)
        approx_char_width = temp_text.width
        
        # 估算每行字符数
        chars_per_line = int(max_width / approx_char_width)
        
        # 使用textwrap进行换行
        if chars_per_line > 0:
            wrapped_text = textwrap.fill(text_content, width=chars_per_line)
        else:
            wrapped_text = text_content
        
        # 创建换行后的文本对象
        text_obj = Text(wrapped_text, font_size=font_size, line_spacing=line_spacing, **text_kwargs)
        
        # 如果仍然超出最大宽度，进行缩放
        if text_obj.width > max_width:
            text_obj.width = max_width
        
        return text_obj
    
    @staticmethod
    def create_adaptive_paragraph(text_content, max_width, max_height=None, font_size=36, 
                                 min_font_size=24, line_spacing=1.0, align="left", **text_kwargs):
        """
        创建自适应段落，处理超长文本，自动换行和缩放
        
        参数:
            text_content: 文本内容
            max_width: 最大宽度
            max_height: 最大高度 (None表示不限制)
            font_size: 初始字体大小
            min_font_size: 最小字体大小
            line_spacing: 行间距
            align: 对齐方式 ("left", "center", "right")
            **text_kwargs: 传递给Text的其他参数
        
        返回:
            自适应段落文本对象
        """
        # 首先尝试使用初始字体大小创建换行文本
        text_obj = AdaptiveLayoutSystem.auto_wrap_text(
            text_content, max_width, font_size, line_spacing, **text_kwargs
        )
        
        # 如果设置了最大高度且文本高度超出，减小字体大小
        current_font_size = font_size
        if max_height and text_obj.height > max_height:
            while text_obj.height > max_height and current_font_size > min_font_size:
                current_font_size -= 1
                text_obj = AdaptiveLayoutSystem.auto_wrap_text(
                    text_content, max_width, current_font_size, line_spacing, **text_kwargs
                )
        
        # 根据对齐方式调整文本
        if align == "center":
            text_obj.align_to(ORIGIN, LEFT)
        elif align == "right":
            text_obj.align_to(ORIGIN, RIGHT)
        
        return text_obj
    
    @staticmethod
    def split_long_text_into_pages(text_content, max_width, max_height, font_size=36, 
                                  min_font_size=24, line_spacing=1.0, **text_kwargs):
        """
        将超长文本分割成多个页面
        
        参数:
            text_content: 文本内容
            max_width: 最大宽度
            max_height: 最大高度
            font_size: 初始字体大小
            min_font_size: 最小字体大小
            line_spacing: 行间距
            **text_kwargs: 传递给Text的其他参数
        
        返回:
            页面列表，每个页面是一个文本对象
        """
        # 首先尝试使用最小字体大小创建换行文本，检查是否需要分页
        test_text = AdaptiveLayoutSystem.auto_wrap_text(
            text_content, max_width, min_font_size, line_spacing, **text_kwargs
        )
        
        # 如果即使使用最小字体也不超出高度，直接返回一个页面
        if test_text.height <= max_height:
            return [AdaptiveLayoutSystem.create_adaptive_paragraph(
                text_content, max_width, max_height, font_size, min_font_size, line_spacing, **text_kwargs
            )]
        
        # 需要分页处理
        paragraphs = text_content.split("\n\n")
        pages = []
        current_page_content = ""
        
        for paragraph in paragraphs:
            # 尝试添加当前段落到当前页面
            test_content = current_page_content + ("\n\n" if current_page_content else "") + paragraph
            test_text = AdaptiveLayoutSystem.auto_wrap_text(
                test_content, max_width, min_font_size, line_spacing, **text_kwargs
            )
            
            # 如果添加后超出高度，创建新页面
            if test_text.height > max_height and current_page_content:
                pages.append(AdaptiveLayoutSystem.create_adaptive_paragraph(
                    current_page_content, max_width, max_height, font_size, min_font_size, line_spacing, **text_kwargs
                ))
                current_page_content = paragraph
            else:
                current_page_content = test_content
        
        # 添加最后一页
        if current_page_content:
            pages.append(AdaptiveLayoutSystem.create_adaptive_paragraph(
                current_page_content, max_width, max_height, font_size, min_font_size, line_spacing, **text_kwargs
            ))
        
        return pages
    
    @staticmethod
    def prevent_overlap(mobjects, direction=DOWN, min_buff=0.2, fix_first=True):
        """
        防止对象重叠，自动调整位置
        
        参数:
            mobjects: 对象列表
            direction: 排列方向
            min_buff: 最小间距
            fix_first: 是否固定第一个对象位置
        
        返回:
            调整后的对象组
        """
        if len(mobjects) <= 1:
            return VGroup(*mobjects)
        
        result = VGroup(*mobjects)
        
        # 如果不固定第一个对象，所有对象都会移动
        if not fix_first:
            result.arrange(direction, buff=min_buff)
            return result
        
        # 固定第一个对象，只移动其他对象
        first_obj = mobjects[0]
        first_pos = first_obj.get_center()
        
        for i in range(1, len(mobjects)):
            current_obj = mobjects[i]
            prev_obj = mobjects[i-1]
            
            # 计算当前对象应该的位置
            if np.array_equal(direction, DOWN):
                target_y = prev_obj.get_bottom()[1] - min_buff - current_obj.height/2
                current_obj.move_to([current_obj.get_center()[0], target_y, 0])
            elif np.array_equal(direction, UP):
                target_y = prev_obj.get_top()[1] + min_buff + current_obj.height/2
                current_obj.move_to([current_obj.get_center()[0], target_y, 0])
            elif np.array_equal(direction, RIGHT):
                target_x = prev_obj.get_right()[0] + min_buff + current_obj.width/2
                current_obj.move_to([target_x, current_obj.get_center()[1], 0])
            elif np.array_equal(direction, LEFT):
                target_x = prev_obj.get_left()[0] - min_buff - current_obj.width/2
                current_obj.move_to([target_x, current_obj.get_center()[1], 0])
        
        # 确保第一个对象位置不变
        first_obj.move_to(first_pos)
        
        return result
    
    @staticmethod
    def create_responsive_grid(mobjects, n_cols=3, h_buff=0.5, v_buff=0.5, max_width=None, equal_heights=False):
        """
        创建响应式网格布局
        
        参数:
            mobjects: 对象列表
            n_cols: 列数
            h_buff: 水平间距
            v_buff: 垂直间距
            max_width: 最大宽度 (None表示不限制)
            equal_heights: 是否使所有行高度相等
        
        返回:
            网格布局对象组
        """
        if not mobjects:
            return VGroup()
        
        n_rows = math.ceil(len(mobjects) / n_cols)
        grid = VGroup()
        
        # 如果需要等高行，首先计算每行的最大高度
        row_heights = [0] * n_rows
        if equal_heights:
            for i, mob in enumerate(mobjects):
                row = i // n_cols
                row_heights[row] = max(row_heights[row], mob.height)
        
        # 创建行
        for r in range(n_rows):
            row_objects = []
            for c in range(n_cols):
                idx = r * n_cols + c
                if idx < len(mobjects):
                    obj = mobjects[idx].copy()
                    
                    # 如果需要等高行，调整对象高度
                    if equal_heights and obj.height < row_heights[r]:
                        # 创建背景以保持一致高度，但保持对象原始大小
                        padding = (row_heights[r] - obj.height) / 2
                        obj_group = VGroup(obj)
                        obj_group.arrange(DOWN, buff=padding*2)
                        row_objects.append(obj_group)
                    else:
                        row_objects.append(obj)
            
            # 创建行并添加到网格
            if row_objects:
                row = VGroup(*row_objects).arrange(RIGHT, buff=h_buff)
                grid.add(row)
        
        # 排列行
        grid.arrange(DOWN, buff=v_buff)
        
        # 如果设置了最大宽度且网格宽度超出，进行缩放
        if max_width and grid.width > max_width:
            grid.width = max_width
        
        return grid
    
    @staticmethod
    def auto_arrange_with_titles(title_content_pairs, direction=DOWN, title_scale=1.2, 
                               content_buff=0.3, section_buff=1.0, max_width=None):
        """
        自动排列带标题的内容部分
        
        参数:
            title_content_pairs: (标题,内容)对列表
            direction: 排列方向
            title_scale: 标题相对于内容的缩放比例
            content_buff: 标题与内容之间的间距
            section_buff: 各部分之间的间距
            max_width: 最大宽度 (None表示不限制)
        
        返回:
            排列好的对象组
        """
        sections = VGroup()
        
        for title, content in title_content_pairs:
            # 确保标题比内容大
            if isinstance(title, (Text, Tex, MathTex)) and isinstance(content, (Text, Tex, MathTex)):
                title.font_size = content.font_size * title_scale
            
            # 创建部分组
            section = VGroup(title, content)
            section.arrange(direction, buff=content_buff)
            
            # 如果设置了最大宽度，确保部分不超出
            if max_width and section.width > max_width:
                # 优先缩放内容而不是标题
                if content.width > title.width:
                    content.width = max_width
                    # 重新排列
                    section = VGroup(title, content)
                    section.arrange(direction, buff=content_buff)
                
                # 如果仍然超出，整体缩放
                if section.width > max_width:
                    section.width = max_width
            
            sections.add(section)
        
        # 排列所有部分
        if sections:
            sections.arrange(direction, buff=section_buff)
        
        return sections
    
    @staticmethod
    def create_scrolling_text(scene, text_obj, scroll_time=3, direction=UP, distance_factor=1.0):
        """
        创建文本滚动动画
        
        参数:
            scene: Manim场景对象
            text_obj: 文本对象
            scroll_time: 滚动时间
            direction: 滚动方向
            distance_factor: 滚动距离因子 (相对于文本高度)
        
        返回:
            None (直接在场景中播放动画)
        """
        # 计算滚动距离
        if direction in [UP, DOWN]:
            distance = text_obj.height * distance_factor
        else:  # LEFT, RIGHT
            distance = text_obj.width * distance_factor
        
        # 创建滚动动画
        scroll_anim = text_obj.animate.shift(direction * distance)
        scene.play(scroll_anim, run_time=scroll_time)
    
    @staticmethod
    def highlight_text_parts(scene, text_obj, parts_to_highlight, color=YELLOW, 
                           animation_per_part=True, run_time=0.5):
        """
        高亮显示文本的特定部分
        
        参数:
            scene: Manim场景对象
            text_obj: 文本对象 (Text类型)
            parts_to_highlight: 要高亮的文本部分列表
            color: 高亮颜色
            animation_per_part: 是否为每个部分创建单独的动画
            run_time: 每个高亮动画的运行时间
        
        返回:
            None (直接在场景中修改文本并可能播放动画)
        """
        if not isinstance(text_obj, Text):
            raise ValueError("text_obj必须是Text类型")
        
        animations = []
        
        for part in parts_to_highlight:
            if part in text_obj.original_text:
                # 找到部分在文本中的位置
                start_idx = text_obj.original_text.find(part)
                end_idx = start_idx + len(part)
                
                # 高亮显示
                if animation_per_part:
                    scene.play(text_obj[start_idx:end_idx].animate.set_color(color), run_time=run_time)
                else:
                    text_obj[start_idx:end_idx].set_color(color)
                    animations.append(Flash(text_obj[start_idx:end_idx], color=color, flash_radius=0.3))
        
        # 如果不为每个部分创建单独的动画，一次性播放所有动画
        if not animation_per_part and animations:
            scene.play(*animations, run_time=run_time)
    
    @staticmethod
    def create_platform_optimized_layout(scene, platform="tiktok", show_safe_zone=False):
        """
        创建针对特定平台优化的布局
        
        参数:
            scene: Manim场景对象
            platform: 平台名称 ("tiktok" 或 "xiaohongshu")
            show_safe_zone: 是否显示安全区域
        
        返回:
            safe_zone: 安全区域对象
            safe_width: 安全区域宽度
            safe_height: 安全区域高度
        """
        # 根据平台设置屏幕比例
        if platform.lower() == "tiktok":
            # 抖音竖屏 9:16
            config.frame_width = 9
            config.frame_height = 16
            config.pixel_width = 1080
            config.pixel_height = 1920
            margin = 1.0
        elif platform.lower() == "xiaohongshu":
            # 小红书 3:4
            config.frame_width = 9
            config.frame_height = 12
            config.pixel_width = 1080
            config.pixel_height = 1440
            margin = 0.8
        else:
            # 默认 16:9
            config.frame_width = 16
            config.frame_height = 9
            config.pixel_width = 1920
            config.pixel_height = 1080
            margin = 0.5
            
        # 确保场景相机更新为新的比例
        scene.camera.frame_width = config.frame_width
        scene.camera.frame_height = config.frame_height
        
        # 创建安全区域
        return AdaptiveLayoutSystem.create_safe_zone(scene, margin=margin, visible=show_safe_zone)
    
    @staticmethod
    def add_platform_elements(scene, platform="tiktok", username="@数学动画"):
        """
        添加平台特定元素（如水印、互动提示等）
        
        参数:
            scene: Manim场景对象
            platform: 平台名称 ("tiktok" 或 "xiaohongshu")
            username: 用户名
        
        返回:
            添加的元素组
        """
        elements = VGroup()
        
        # 添加用户名水印
        watermark = Text(username, font_size=24, color=WHITE, opacity=0.7)
        watermark.to_corner(DR, buff=0.3)
        elements.add(watermark)
        
        # 根据平台添加特定元素
        if platform.lower() == "tiktok":
            # 抖音互动提示
            interaction_tip = Text("点赞关注，了解更多数学动画！", font_size=28, color=YELLOW)
            interaction_tip.to_edge(DOWN, buff=0.5)
            elements.add(interaction_tip)
            
        elif platform.lower() == "xiaohongshu":
            # 小红书封面提示
            cover_tip = Text("↓ 向下滑动查看更多 ↓", font_size=28, color=YELLOW)
            cover_tip.to_edge(DOWN, buff=0.5)
            elements.add(cover_tip)
        
        # 添加到场景
        scene.add(elements)
        
        return elements