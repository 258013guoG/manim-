# -*- coding: utf-8 -*-
from manim import *

class text_displayer:
    """
    字幕替换封装
    """

    def __init__(
        self, sc: Scene, arr, start_position=UP * 3, display_length=1, buff=0.5
    ) -> None:
        """
        初始化

        Parameters
        ---------
        sc
            绘制字幕的场景
        arr
            字幕列表，是 list 类型
        start_position
            字幕开始位置，默认位置偏上 UP*3
        display_length
            最多显示字幕行数，超出时则隐藏最早的那一行，其他行相应移动位置
        buff
            每行字幕间隔的位置
        """
        self.sc = sc  # 当前场景
        self.text_arr = arr  # 所有文本
        self.start_position = start_position  # 开始显示的位置
        self.display_length = display_length  # 最多显示的行数
        self.buff = buff  # 每行文本之间的间隔
        self.cur_index = 0  # 当前的index

    def next(self) -> bool:
        if self.cur_index >= len(self.text_arr):
            return False

        # 是否需要上移
        if self.cur_index >= self.display_length:  # 已达到显示的最大值
            # 清除第一层的文字
            self.sc.play(FadeOut(self.text_arr[self.cur_index - self.display_length]))

            # 上移已有的文字
            for i in range(self.display_length - 1, 0, -1):
                self.sc.play(
                    self.text_arr[self.cur_index - i].animate.move_to(
                        self.start_position
                        + DOWN * (self.display_length - 1 - i) * self.buff
                    )
                )

        # 显示当前行
        d = self.cur_index // self.display_length
        if d == 0:
            self.sc.play(
                Write(
                    self.text_arr[self.cur_index].shift(
                        self.start_position - UP * self.buff * self.cur_index
                    )
                )
            )
        else:
            self.sc.play(
                Write(
                    self.text_arr[self.cur_index].shift(
                        self.start_position - UP * self.buff * (self.display_length - 1)
                    )
                )
            )

        self.cur_index += 1
        return True


class ScrollingTextExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("滚动字幕示例", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建字幕列表
        subtitles = [
            Text("第一行：Manim是一个强大的数学动画库", color=RED, font_size=24),
            Text("第二行：它由3Blue1Brown（Grant Sanderson）开发", color=YELLOW, font_size=24),
            Text("第三行：可以创建高质量的数学解释视频", color=BLUE, font_size=24),
            Text("第四行：支持各种几何图形和动画效果", color=GREEN, font_size=24),
            Text("第五行：可以轻松处理文本和数学公式", color=ORANGE, font_size=24),
            Text("第六行：提供了丰富的坐标系统", color=PURPLE, font_size=24),
            Text("第七行：支持2D和3D场景", color=TEAL, font_size=24),
            Text("第八行：可以自定义各种动画效果", color=PINK, font_size=24),
        ]
        
        # 创建字幕显示器 - 一次显示一行
        self.next_section("单行显示")
        td1 = text_displayer(self, subtitles, start_position=UP, display_length=1)
        while td1.next():
            self.wait(0.5)
        self.wait(1)
        self.clear()
        
        # 重新显示标题
        self.play(Write(title))
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建字幕显示器 - 一次显示三行
        self.next_section("三行显示")
        td2 = text_displayer(self, subtitles, start_position=UP, display_length=3)
        while td2.next():
            self.wait(0.5)
        self.wait(1)
        
        # 结束信息
        conclusion = Text("滚动字幕演示完成！", color=GREEN, font_size=36)
        self.play(Write(conclusion))
        self.wait(2)


# 运行命令：manim -pql scrolling_text_example.py ScrollingTextExample