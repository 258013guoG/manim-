# -*- coding: utf-8 -*-
from manim import *
import numpy as np

# 设置抖音竖屏比例
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class AdvancedGeometry(Scene):
    def construct(self):
        # 创建封面
        title = Text("高级几何艺术", font_size=72, color=BLUE)
        subtitle = Text("探索数学与艺术的完美结合", font_size=36)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=DOWN), run_time=1)
        self.wait(1)
        self.play(title_group.animate.scale(0.7).to_edge(UP), run_time=1)
        
        # 第一部分：多边形变换序列
        section_title = Text("多边形变换", font_size=48, color=YELLOW)
        section_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(section_title), run_time=1)
        
        # 创建一系列正多边形，从三边形到十边形
        polygons = VGroup()
        num_sides_range = range(3, 11)  # 3到10边形
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, TEAL]
        
        # 创建初始三角形
        current_polygon = RegularPolygon(3, color=colors[0], fill_opacity=0.5)
        current_polygon.scale(2)
        self.play(Create(current_polygon), run_time=1)
        
        # 逐渐变换为更多边的多边形
        for i, num_sides in enumerate(num_sides_range[1:], 1):
            next_polygon = RegularPolygon(num_sides, color=colors[i], fill_opacity=0.5)
            next_polygon.scale(2)
            self.play(Transform(current_polygon, next_polygon), run_time=0.8)
            self.wait(0.3)
        
        # 添加文字说明
        explanation = Text("正多边形：当边数趋向无穷时\n将逐渐接近圆形", font_size=32)
        explanation.next_to(current_polygon, DOWN, buff=0.8)
        self.play(Write(explanation), run_time=1.5)
        self.wait(1)
        
        # 清除场景
        self.play(
            FadeOut(current_polygon),
            FadeOut(explanation),
            FadeOut(section_title),
            run_time=1
        )
        
        # 第二部分：分形几何 - 科赫雪花
        fractal_title = Text("分形几何：科赫雪花", font_size=48, color=GREEN)
        fractal_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(fractal_title), run_time=1)
        
        # 创建科赫雪花的基础三角形
        koch_scale = 3
        triangle = RegularPolygon(3, color=BLUE)
        triangle.scale(koch_scale)
        triangle.set_stroke(width=2)
        
        self.play(Create(triangle), run_time=1)
        self.wait(0.5)
        
        # 定义科赫曲线的递归函数
        def get_koch_points(points, order):
            if order == 0:
                return points
            new_points = []
            for i in range(len(points) - 1):
                p1, p2 = points[i], points[i + 1]
                p3 = p1 + (p2 - p1) / 3
                p5 = p1 + 2 * (p2 - p1) / 3
                
                # 计算等边三角形的第三个点
                vec = p5 - p3
                vec = np.array([-vec[1], vec[0], 0]) * np.sqrt(3) / 3
                p4 = p3 + vec
                
                new_points.extend([p1, p3, p4, p5])
            new_points.append(points[-1])
            return get_koch_points(new_points, order - 1)
        
        # 获取三角形的顶点
        vertices = [triangle.get_vertices()[i] for i in range(3)]
        vertices.append(vertices[0])  # 闭合路径
        
        # 逐步展示科赫雪花的生成过程
        max_order = 4
        current_curve = VMobject(stroke_width=2, color=BLUE)
        current_curve.set_points_as_corners(vertices)
        
        for order in range(1, max_order + 1):
            koch_points = get_koch_points(vertices, order)
            new_curve = VMobject(stroke_width=2, color=interpolate_color(BLUE, WHITE, order/max_order))
            new_curve.set_points_as_corners(koch_points)
            
            self.play(Transform(current_curve, new_curve), run_time=1.5)
            self.wait(0.5)
            
            # 更新顶点为当前迭代的结果
            vertices = koch_points
        
        # 添加文字说明
        koch_explanation = Text("科赫雪花：无限递归的分形结构\n具有无限周长但有限面积", font_size=32)
        koch_explanation.next_to(current_curve, DOWN, buff=0.8)
        self.play(Write(koch_explanation), run_time=1.5)
        self.wait(1.5)
        
        # 清除场景
        self.play(
            FadeOut(current_curve),
            FadeOut(koch_explanation),
            FadeOut(fractal_title),
            run_time=1
        )
        
        # 第三部分：黄金比例与斐波那契螺旋
        golden_title = Text("黄金比例与斐波那契螺旋", font_size=48, color=GOLD)
        golden_title.next_to(title_group, DOWN, buff=0.8)
        self.play(Write(golden_title), run_time=1)
        
        # 创建黄金矩形
        golden_ratio = (1 + np.sqrt(5)) / 2
        rect_width = 4
        rect_height = rect_width / golden_ratio
        golden_rect = Rectangle(
            width=rect_width,
            height=rect_height,
            color=GOLD,
            fill_opacity=0.3
        )
        
        self.play(Create(golden_rect), run_time=1)
        
        # 添加黄金比例标签
        ratio_label = MathTex(r"\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618", color=GOLD)
        ratio_label.next_to(golden_rect, UP, buff=0.5)
        self.play(Write(ratio_label), run_time=1.5)
        
        # 创建斐波那契矩形序列
        fib_rects = VGroup()
        fib_seq = [1, 1, 2, 3, 5, 8, 13, 21]
        current_x = 0
        current_y = 0
        direction = 0  # 0: 右, 1: 上, 2: 左, 3: 下
        scale_factor = rect_height / fib_seq[-1]  # 缩放因子，使最大矩形与黄金矩形高度相同
        
        for i, fib in enumerate(fib_seq):
            side_length = fib * scale_factor
            rect = Square(side_length=side_length, color=interpolate_color(BLUE, RED, i/len(fib_seq)))
            
            if direction == 0:  # 右
                rect.move_to([current_x + side_length/2, current_y + side_length/2, 0])
                current_x += side_length
            elif direction == 1:  # 上
                rect.move_to([current_x - side_length/2, current_y + side_length/2, 0])
                current_y += side_length
            elif direction == 2:  # 左
                rect.move_to([current_x - side_length/2, current_y - side_length/2, 0])
                current_x -= side_length
            elif direction == 3:  # 下
                rect.move_to([current_x + side_length/2, current_y - side_length/2, 0])
                current_y -= side_length
            
            direction = (direction + 1) % 4
            fib_rects.add(rect)
        
        # 将整个斐波那契矩形序列居中
        fib_rects.move_to(ORIGIN)
        
        # 逐个显示斐波那契矩形
        self.play(FadeOut(golden_rect), run_time=0.8)
        for rect in fib_rects:
            self.play(Create(rect), run_time=0.4)
        
        # 创建斐波那契螺旋
        spiral = VMobject(color=YELLOW, stroke_width=3)
        spiral_points = []
        
        # 为每个矩形创建四分之一圆弧
        arcs = VGroup()
        current_x = 0
        current_y = 0
        direction = 0
        start_angle = 0
        
        for i, fib in enumerate(fib_seq):
            side_length = fib * scale_factor
            if i < 2:  # 跳过前两个小矩形
                if direction == 0:  # 右
                    current_x += side_length
                elif direction == 1:  # 上
                    current_y += side_length
                elif direction == 2:  # 左
                    current_x -= side_length
                elif direction == 3:  # 下
                    current_y -= side_length
                direction = (direction + 1) % 4
                continue
            
            # 确定圆弧的中心点
            if direction == 0:  # 右
                arc_center = [current_x, current_y, 0]
                start_angle = PI
                current_x += side_length
            elif direction == 1:  # 上
                arc_center = [current_x, current_y, 0]
                start_angle = PI/2
                current_y += side_length
            elif direction == 2:  # 左
                arc_center = [current_x, current_y, 0]
                start_angle = 0
                current_x -= side_length
            elif direction == 3:  # 下
                arc_center = [current_x, current_y, 0]
                start_angle = -PI/2
                current_y -= side_length
            
            arc = Arc(
                radius=side_length,
                start_angle=start_angle,
                angle=PI/2,
                color=YELLOW,
                stroke_width=3
            )
            arc.move_arc_center_to(arc_center)
            arcs.add(arc)
            
            direction = (direction + 1) % 4
        
        # 显示螺旋
        self.play(Create(arcs, lag_ratio=0.5), run_time=2)
        self.wait(1)
        
        # 添加文字说明
        spiral_explanation = Text("斐波那契螺旋：大自然中的数学奇迹\n从花朵到星系，无处不在", font_size=32)
        spiral_explanation.next_to(fib_rects, DOWN, buff=0.8)
        self.play(Write(spiral_explanation), run_time=1.5)
        self.wait(1.5)
        
        # 结束动画
        self.play(
            FadeOut(fib_rects),
            FadeOut(arcs),
            FadeOut(spiral_explanation),
            FadeOut(golden_title),
            FadeOut(ratio_label),
            run_time=1.5
        )
        
        # 结束文字
        final_title = Text("几何之美无处不在", font_size=60, color=BLUE)
        final_subtitle = Text("数学是大自然的语言", font_size=36)
        final_group = VGroup(final_title, final_subtitle).arrange(DOWN, buff=0.5)
        
        self.play(
            FadeOut(title_group),
            Write(final_title),
            run_time=1.5
        )
        self.play(Write(final_subtitle), run_time=1)
        
        # 添加互动提示（抖音风格）
        interaction_tip = Text("点赞关注，发现更多数学之美", font_size=36, color=YELLOW)
        interaction_tip.to_edge(DOWN, buff=1)
        self.play(FadeIn(interaction_tip, shift=UP*0.5), run_time=1)
        self.wait(2)

# 运行命令：
# manim -pql advanced_geometry.py AdvancedGeometry