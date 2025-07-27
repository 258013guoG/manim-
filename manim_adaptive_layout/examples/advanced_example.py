# -*- coding: utf-8 -*-
"""
Manim自适应布局系统高级示例

演示了自适应布局系统的高级功能，包括：
- 文本分页
- 文本滚动
- 文本高亮
- 带标题的内容排列

渲染命令：
    抖音竖屏: manim -pql --resolution=1080,1920 advanced_example.py AdvancedExample
    小红书: manim -pql --resolution=1080,1440 advanced_example.py AdvancedExample
    标准横屏: manim -pql --resolution=1920,1080 advanced_example.py AdvancedExample

注意：必须使用--resolution参数指定正确的分辨率，否则可能导致屏幕比例不正确
"""

from manim import *
from manim_adaptive_layout import AdaptiveLayoutSystem

class AdvancedExample(Scene):
    def construct(self):
        # 1. 设置抖音竖屏比例并创建安全区域
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 2. 创建标题
        title = Text("自适应布局系统高级功能", font_size=48)
        title.to_edge(UP, buff=1)
        self.add(title)
        
        # 3. 创建长文本用于分页示例
        long_text = """
自适应布局系统是一个专为Manim动画引擎设计的布局管理工具，解决了在不同屏幕比例下内容排版的问题。

主要特性包括：
- 安全区域管理：自动创建适合不同平台的安全区域
- 超长文本处理：自动换行、缩放、分页显示和滚动显示
- 自适应排列：防止元素重叠，自动调整位置
- 响应式网格：创建自适应的网格布局，支持等高行
- 平台优化：针对抖音、小红书等平台预设屏幕比例

本系统可以轻松适应不同平台的屏幕比例要求，让您的动画内容在任何设备上都能完美呈现。
"""
        
        # 4. 将长文本分页
        pages = AdaptiveLayoutSystem.split_long_text_into_pages(
            long_text,
            max_width=safe_width * 0.9,
            max_height=safe_height * 0.3,
            font_size=32,
            min_font_size=24
        )
        
        # 5. 显示分页效果
        self.next_section("分页示例")
        page_group = VGroup()
        page_counter = Text("", font_size=24)
        
        for i, page in enumerate(pages):
            page.next_to(title, DOWN, buff=0.8)
            if i == 0:
                self.add(page)
                current_page = page
            page_group.add(page)
        
        # 更新页码
        page_counter.text = f"第1页/共{len(pages)}页"
        page_counter.next_to(current_page, DOWN, buff=0.5)
        self.add(page_counter)
        
        # 翻页动画
        for i in range(1, len(pages)):
            new_page = pages[i]
            new_page.next_to(title, DOWN, buff=0.8)
            new_counter_text = f"第{i+1}页/共{len(pages)}页"
            
            self.play(
                FadeOut(current_page),
                FadeIn(new_page),
                Transform(page_counter, Text(new_counter_text, font_size=24).move_to(page_counter))
            )
            
            current_page = new_page
            self.wait(1)
        
        # 清除分页内容
        self.play(FadeOut(page_group), FadeOut(page_counter))
        
        # 6. 文本滚动示例
        self.next_section("滚动文本示例")
        scroll_title = Text("文本滚动示例", font_size=36)
        scroll_title.next_to(title, DOWN, buff=0.8)
        self.add(scroll_title)
        
        # 创建长文本用于滚动
        scroll_text = AdaptiveLayoutSystem.auto_wrap_text(
            "这是一段需要滚动显示的长文本。自适应布局系统提供了平滑的文本滚动功能，适合展示超出屏幕高度的内容。用户可以控制滚动方向、速度和距离。这对于展示大量文本信息非常有用。",
            max_width=safe_width * 0.8,
            font_size=32
        )
        
        # 创建裁剪区域
        clip_height = 3
        clip_rect = Rectangle(
            width=safe_width * 0.85,
            height=clip_height,
            stroke_opacity=0,
            fill_opacity=0
        )
        clip_rect.next_to(scroll_title, DOWN, buff=0.5)
        
        # 将文本放在裁剪区域顶部
        scroll_text.next_to(clip_rect.get_top(), DOWN, buff=0.1)
        scroll_text.align_to(clip_rect, LEFT).shift(RIGHT * 0.5)  # 左对齐并稍微缩进
        
        # 创建裁剪版本的文本
        clipped_text = scroll_text.copy()
        
        # 创建裁剪矩形
        clip_rect_stroke = clip_rect.copy()
        
        # 使用VGroup而不是Group，并添加到场景
        self.add(clip_rect_stroke)
        
        # 使用clip_by_rect方法代替clip_to_shape
        # 注意：我们需要确保文本在裁剪区域内可见，但超出部分不可见
        # 这可以通过添加遮罩或使用clip_by_rect方法实现
        
        # 创建一个遮罩组
        mask_group = VGroup()
        
        # 添加上下左右的遮罩矩形
        top_mask = Rectangle(
            width=config.frame_width,
            height=config.frame_height/2,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).move_to(clip_rect.get_top() + UP * config.frame_height/4)
        
        bottom_mask = Rectangle(
            width=config.frame_width,
            height=config.frame_height/2,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).move_to(clip_rect.get_bottom() + DOWN * config.frame_height/4)
        
        left_mask = Rectangle(
            width=(config.frame_width - clip_rect.width)/2,
            height=clip_rect.height,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).next_to(clip_rect, LEFT, buff=0)
        
        right_mask = Rectangle(
            width=(config.frame_width - clip_rect.width)/2,
            height=clip_rect.height,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        ).next_to(clip_rect, RIGHT, buff=0)
        
        mask_group.add(top_mask, bottom_mask, left_mask, right_mask)
        self.add(clipped_text, mask_group)
        
        # 创建滚动动画
        self.wait(1)
        AdaptiveLayoutSystem.create_scrolling_text(
            self, clipped_text, scroll_time=8, direction=UP, distance_factor=1.5
        )
        self.wait(1)
        
        # 清除滚动内容
        self.play(FadeOut(clipped_text), FadeOut(mask_group), FadeOut(clip_rect_stroke), FadeOut(scroll_title))
        
        # 7. 文本高亮示例
        self.next_section("文本高亮示例")
        highlight_title = Text("文本高亮示例", font_size=36)
        highlight_title.next_to(title, DOWN, buff=0.8)
        self.add(highlight_title)
        
        # 创建包含关键词的段落
        highlight_text = AdaptiveLayoutSystem.create_adaptive_paragraph(
            "自适应布局系统提供了文本高亮功能，可以突出显示文本中的关键词。这对于教育内容和演示非常有用。您可以高亮显示多个关键词，并控制高亮颜色和动画效果。",
            max_width=safe_width * 0.8,
            font_size=32
        )
        highlight_text.next_to(highlight_title, DOWN, buff=0.5)
        self.add(highlight_text)
        
        # 高亮关键词
        keywords = ["自适应布局系统", "文本高亮", "关键词", "教育内容", "动画效果"]
        self.wait(1)
        AdaptiveLayoutSystem.highlight_text_parts(
            self, highlight_text, keywords, color=YELLOW, animation_per_part=True, run_time=0.5
        )
        self.wait(1)
        
        # 8. 带标题的内容排列
        self.next_section("带标题的内容排列")
        self.play(FadeOut(highlight_text), FadeOut(highlight_title))
        
        # 创建标题和内容对
        title_content_pairs = [
            (Text("安全区域管理", font_size=32), Text("确保内容不会超出屏幕边界", font_size=24)),
            (Text("超长文本处理", font_size=32), Text("自动换行、缩放、分页和滚动", font_size=24)),
            (Text("自适应排列", font_size=32), Text("防止元素重叠，自动调整位置", font_size=24))
        ]
        
        # 使用自动排列功能
        sections = AdaptiveLayoutSystem.auto_arrange_with_titles(
            title_content_pairs,
            direction=DOWN,
            title_scale=1.2,
            content_buff=0.3,
            section_buff=0.8,
            max_width=safe_width * 0.9
        )
        sections.next_to(title, DOWN, buff=1)
        
        self.play(FadeIn(sections))
        self.wait(2)
        
        # 添加平台特定元素
        AdaptiveLayoutSystem.add_platform_elements(
            self, platform="xiaohongshu", username="@数学动画"
        )