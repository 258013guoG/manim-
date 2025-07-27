# -*- coding: utf-8 -*-
from manim import *

class AutoScrollingText(Scene):
    def construct(self):
        # 创建标题
        title = Text("自动滚动字幕效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建长文本
        long_text = """Manim是一个强大的数学动画库，由3Blue1Brown（Grant Sanderson）开发。
它可以创建高质量的数学解释视频，支持各种几何图形和动画效果。
Manim可以轻松处理文本和数学公式，提供了丰富的坐标系统。
它支持2D和3D场景，可以自定义各种动画效果。
通过编程方式创建动画，让数学概念更加直观易懂。
可以实现复杂的数学变换和推导过程的可视化。
适合教育工作者、学生和数学爱好者使用。
本示例展示了如何实现自动滚动字幕效果。"""
        
        # 将长文本分割成行
        lines = long_text.strip().split('\n')
        
        # 创建文本对象
        text_group = VGroup()
        for i, line in enumerate(lines):
            text = Text(line, font_size=24)
            text.move_to(DOWN * 3 + UP * i * 0.8)  # 初始位置在屏幕底部以下
            text_group.add(text)
        
        # 添加所有文本到场景
        self.add(text_group)
        
        # 创建自动滚动动画
        self.next_section("自动滚动")
        # 计算需要滚动的总距离
        total_height = len(lines) * 0.8
        scroll_time = 10  # 滚动总时间
        
        # 创建滚动动画
        self.play(
            text_group.animate.shift(UP * (total_height + 6)),  # +6确保所有文本都能完全滚过屏幕
            run_time=scroll_time,
            rate_func=linear  # 使用线性速率函数使滚动速度恒定
        )
        
        self.wait(1)
        self.clear()
        
        # 第二部分：逐行淡入淡出效果
        title = Text("逐行淡入淡出效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建新的文本对象，带有不同颜色
        colored_texts = []
        colors = [RED, YELLOW, GREEN, BLUE, PURPLE, ORANGE, TEAL, PINK]
        
        for i, line in enumerate(lines):
            text = Text(line, font_size=24, color=colors[i % len(colors)])
            text.move_to(ORIGIN)  # 所有文本都在中心位置
            colored_texts.append(text)
        
        # 逐行淡入淡出
        self.next_section("淡入淡出")
        for i, text in enumerate(colored_texts):
            if i > 0:
                # 淡出前一个文本
                self.play(FadeOut(colored_texts[i-1]))
            # 淡入当前文本
            self.play(FadeIn(text))
            self.wait(0.5)
        
        # 淡出最后一个文本
        self.play(FadeOut(colored_texts[-1]))
        
        # 结束信息
        conclusion = Text("高级滚动字幕演示完成！", color=GREEN, font_size=36)
        self.play(Write(conclusion))
        self.wait(2)


class ContinuousTextScroller(VGroup):
    """连续文本滚动器，可以实现类似电影片尾字幕的效果"""
    
    def __init__(self, text_content, width=6, font_size=24, line_spacing=0.3, **kwargs):
        super().__init__(**kwargs)
        
        self.container = Rectangle(
            width=width + 0.5,
            height=5,
            stroke_opacity=0,
            fill_opacity=0
        )
        
        # 分割文本内容
        lines = text_content.strip().split('\n')
        
        # 创建文本组
        self.text_group = VGroup()
        for i, line in enumerate(lines):
            text = Text(line, font_size=font_size)
            # 确保文本宽度不超过容器
            if text.width > width:
                text.scale_to_fit_width(width)
            text.move_to(DOWN * i * (font_size/30 + line_spacing))
            self.text_group.add(text)
        
        # 计算文本总高度
        self.total_height = len(lines) * (font_size/30 + line_spacing)
        
        # 初始位置设置在容器底部以下
        self.text_group.move_to(self.container.get_bottom() + DOWN * 2)
        
        # 添加到VGroup
        self.add(self.container, self.text_group)
    
    def scroll_animation(self, run_time=15):
        """创建滚动动画"""
        # 计算需要移动的距离，使所有文本都能滚过容器
        distance = self.total_height + self.container.height
        return self.text_group.animate.shift(UP * distance), run_time


class MovieCreditsExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("电影片尾字幕效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建片尾字幕内容
        credits_text = """导演
张三

编剧
李四
王五

主演
赵六 饰 数学家
钱七 饰 学生
孙八 饰 教授

摄影
周九

剪辑
吴十

音乐
郑十一

特效
王十二

制片人
刘十三

出品方
Manim工作室

鸣谢
3Blue1Brown
Grant Sanderson

©2023 Manim示例 版权所有"""
        
        # 创建滚动器
        scroller = ContinuousTextScroller(credits_text, width=6, font_size=24, line_spacing=0.3)
        scroller.move_to(ORIGIN)
        
        # 添加到场景
        self.add(scroller.container)  # 只添加容器，文本将从下方滚入
        
        # 创建滚动动画
        self.next_section("片尾字幕")
        animation, run_time = scroller.scroll_animation(run_time=20)
        self.play(animation, run_time=run_time, rate_func=linear)
        
        # 结束信息
        self.clear()
        conclusion = Text("电影片尾字幕效果演示完成！", color=GREEN, font_size=36)
        self.play(Write(conclusion))
        self.wait(2)


# 运行命令：
# manim -pql advanced_scrolling_text.py AutoScrollingText
# manim -pql advanced_scrolling_text.py MovieCreditsExample