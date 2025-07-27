# -*- coding: utf-8 -*-
from manim import *
import numpy as np

class LayoutUtils:
    """
    提供Manim布局工具，帮助创建安全区域和自适应布局
    """
    
    @staticmethod
    def create_safe_zone(scene, margin=1.0, show_border=True, show_label=True):
        """
        创建并返回安全区域
        
        参数:
            scene: Manim场景对象
            margin: 边距大小
            show_border: 是否显示边界
            show_label: 是否显示标签
            
        返回:
            safe_zone: 安全区域矩形对象
            safe_width: 安全区域宽度
            safe_height: 安全区域高度
        """
        # 计算安全区域尺寸
        safe_width = config.frame_width - 2 * margin
        safe_height = config.frame_height - 2 * margin
        
        # 创建安全区域矩形
        safe_zone = Rectangle(
            width=safe_width,
            height=safe_height,
            stroke_color=RED,
            stroke_width=2,
            stroke_opacity=0.5 if show_border else 0,
        )
        
        # 添加标签
        if show_label:
            safe_zone_label = Text("安全区域", font_size=36, color=RED)
            safe_zone_label.to_edge(UP, buff=margin + 0.5)
            scene.add(safe_zone_label)
        
        # 添加到场景
        if show_border:
            scene.add(safe_zone)
            
        return safe_zone, safe_width, safe_height
    
    @staticmethod
    def auto_arrange(mobjects, direction=RIGHT, buff=0.5, safe_width=None, safe_height=None):
        """
        自动排列对象并确保在安全区域内
        
        参数:
            mobjects: 要排列的对象或对象组
            direction: 排列方向
            buff: 对象间距
            safe_width: 安全区域宽度
            safe_height: 安全区域高度
            
        返回:
            arranged_group: 排列后的对象组
        """
        # 创建组
        if not isinstance(mobjects, VGroup):
            group = VGroup(*mobjects) if isinstance(mobjects, list) else VGroup(mobjects)
        else:
            group = mobjects
            
        # 排列对象
        group.arrange(direction, buff=buff)
        
        # 检查是否需要缩放以适应安全区域
        if safe_width and group.width > safe_width:
            group.scale_to_fit_width(safe_width * 0.9)  # 留出10%余量
            
        if safe_height and group.height > safe_height:
            group.scale_to_fit_height(safe_height * 0.9)  # 留出10%余量
            
        return group
    
    @staticmethod
    def auto_margin(mobject, container_width, container_height, min_margin=0.5):
        """
        根据对象大小自动计算合适的边距
        
        参数:
            mobject: Manim对象
            container_width: 容器宽度
            container_height: 容器高度
            min_margin: 最小边距
            
        返回:
            margin: 计算出的边距
        """
        width_ratio = mobject.width / container_width
        height_ratio = mobject.height / container_height
        
        # 根据对象占比计算边距
        if width_ratio > 0.8 or height_ratio > 0.8:
            # 大对象使用小边距
            return min_margin
        elif width_ratio > 0.5 or height_ratio > 0.5:
            # 中等对象使用中等边距
            return min_margin * 2
        else:
            # 小对象使用大边距
            return min_margin * 3
    
    @staticmethod
    def fit_text_to_width(text_obj, max_width, min_font_size=24):
        """
        自动调整文本大小以适应指定宽度
        
        参数:
            text_obj: 文本对象
            max_width: 最大宽度
            min_font_size: 最小字体大小
            
        返回:
            text_obj: 调整后的文本对象
        """
        if text_obj.width > max_width:
            # 计算缩放比例
            scale_factor = max_width / text_obj.width
            new_font_size = text_obj.font_size * scale_factor
            
            # 确保字体大小不小于最小值
            if new_font_size < min_font_size:
                # 如果缩放后字体太小，尝试自动换行（分割文本）
                return LayoutUtils.auto_wrap_text(text_obj, max_width, min_font_size)
            else:
                # 直接缩放文本
                text_obj.scale(scale_factor)
                
        return text_obj
    
    @staticmethod
    def auto_wrap_text(text_obj, max_width, font_size=None):
        """
        自动将文本换行以适应指定宽度
        
        参数:
            text_obj: 文本对象
            max_width: 最大宽度
            font_size: 字体大小
            
        返回:
            wrapped_text: 换行后的文本对象组
        """
        # 获取原始文本
        original_text = text_obj.original_text if hasattr(text_obj, 'original_text') else text_obj.text
        
        # 设置字体大小
        if font_size is None:
            font_size = text_obj.font_size
        
        # 估算每行字符数
        char_width = font_size * 0.5  # 估算每个字符的平均宽度
        chars_per_line = int(max_width / char_width)
        
        # 分割文本
        lines = []
        current_line = ""
        
        for char in original_text:
            current_line += char
            if len(current_line) >= chars_per_line and char in "，。！？,.!? ":
                lines.append(current_line)
                current_line = ""
        
        if current_line:
            lines.append(current_line)
        
        # 创建文本对象
        text_objects = [Text(line, font_size=font_size, color=text_obj.color) for line in lines]
        wrapped_text = VGroup(*text_objects).arrange(DOWN, buff=0.2)
        
        return wrapped_text
    
    @staticmethod
    def prevent_overlap(mobjects, direction=DOWN, min_buff=0.5):
        """
        防止对象重叠
        
        参数:
            mobjects: 要排列的对象列表
            direction: 排列方向
            min_buff: 最小间距
            
        返回:
            VGroup: 排列后的对象组
        """
        result = VGroup()
        last_obj = None
        
        for obj in mobjects:
            if last_obj is None:
                result.add(obj)
            else:
                # 计算当前对象与上一个对象的边界框
                last_bbox = last_obj.get_bounding_box()
                curr_bbox = obj.get_bounding_box()
                
                # 根据方向计算需要的偏移量
                if direction == DOWN:
                    offset = last_bbox[1][1] - curr_bbox[0][1] + min_buff
                    obj.shift(DOWN * offset)
                elif direction == RIGHT:
                    offset = last_bbox[1][0] - curr_bbox[0][0] + min_buff
                    obj.shift(RIGHT * offset)
                elif direction == UP:
                    offset = curr_bbox[1][1] - last_bbox[0][1] + min_buff
                    obj.shift(UP * offset)
                elif direction == LEFT:
                    offset = curr_bbox[1][0] - last_bbox[0][0] + min_buff
                    obj.shift(LEFT * offset)
                
                result.add(obj)
            
            last_obj = obj
            
        return result
    
    @staticmethod
    def create_responsive_grid(mobjects, n_cols, safe_width, safe_height, h_buff=0.5, v_buff=0.5):
        """
        创建响应式网格布局
        
        参数:
            mobjects: 要排列的对象列表
            n_cols: 列数
            safe_width: 安全区域宽度
            safe_height: 安全区域高度
            h_buff: 水平间距
            v_buff: 垂直间距
            
        返回:
            grid: 网格布局对象组
        """
        # 计算每个单元格的最大宽度
        cell_width = (safe_width - (n_cols - 1) * h_buff) / n_cols
        
        # 创建行
        rows = []
        current_row = []
        
        for i, mob in enumerate(mobjects):
            # 确保对象不超过单元格宽度
            if mob.width > cell_width:
                mob.scale_to_fit_width(cell_width * 0.9)
                
            current_row.append(mob)
            
            # 当达到列数或处理完所有对象时，创建一行
            if (i + 1) % n_cols == 0 or i == len(mobjects) - 1:
                row_group = VGroup(*current_row).arrange(RIGHT, buff=h_buff)
                rows.append(row_group)
                current_row = []
        
        # 垂直排列所有行
        grid = VGroup(*rows).arrange(DOWN, buff=v_buff)
        
        # 确保整个网格不超过安全高度
        if grid.height > safe_height:
            grid.scale_to_fit_height(safe_height * 0.9)
            
        return grid

# 使用示例
"""
# 在场景中使用这些工具
class MyScene(Scene):
    def construct(self):
        # 创建安全区域
        safe_zone, safe_width, safe_height = LayoutUtils.create_safe_zone(self)
        
        # 创建一些对象
        title = Text("自适应布局示例", font_size=48)
        subtitle = Text("使用LayoutUtils工具类", font_size=36)
        
        # 自动排列并确保在安全区域内
        title_group = LayoutUtils.auto_arrange(
            [title, subtitle], 
            direction=DOWN, 
            buff=0.5, 
            safe_width=safe_width, 
            safe_height=safe_height
        )
        title_group.to_edge(UP, buff=1.5)
        
        self.play(Write(title_group))
        
        # 创建一些形状
        shapes = [Square(), Circle(), Triangle()]
        for shape in shapes:
            shape.set_color(BLUE)
            shape.set_fill(BLUE, opacity=0.5)
        
        # 创建响应式网格
        grid = LayoutUtils.create_responsive_grid(
            shapes, 
            n_cols=3, 
            safe_width=safe_width, 
            safe_height=safe_height
        )
        grid.next_to(title_group, DOWN, buff=1)
        
        self.play(FadeIn(grid))
"""