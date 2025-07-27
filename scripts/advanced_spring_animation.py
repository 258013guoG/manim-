# -*- coding: utf-8 -*-
from manim import *

class AdvancedSpringAnimation(Scene):
    def construct(self):
        # 创建标题
        title = Text("高级弹簧动画", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # 创建一个弹簧系统
        # 固定点
        fixed_dot = Dot(color=RED).shift(UP*2)
        fixed_label = Text("固定点", font_size=20).next_to(fixed_dot, UP, buff=0.2)
        
        # 弹簧末端的物体
        mass = Square(side_length=0.5, color=BLUE).shift(UP*2 + DOWN*3)
        mass_label = Text("质量块", font_size=20).next_to(mass, DOWN, buff=0.2)
        
        # 弹簧 - 使用多段线来模拟弹簧
        def create_spring(start, end, segments=10, amplitude=0.2):
            # 创建一个弹簧形状的折线
            points = []
            direction = end - start
            length = np.linalg.norm(direction)
            unit_direction = direction / length
            # 创建垂直于主方向的向量
            if abs(unit_direction[0]) < abs(unit_direction[1]):
                perpendicular = np.array([1, 0, 0])
            else:
                perpendicular = np.array([0, 1, 0])
            perpendicular = perpendicular - np.dot(perpendicular, unit_direction) * unit_direction
            perpendicular = perpendicular / np.linalg.norm(perpendicular)
            
            # 创建弹簧的点
            for i in range(segments + 1):
                t = i / segments
                point = start + t * direction
                if 0 < i < segments:
                    # 添加锯齿形状
                    zigzag = amplitude * perpendicular * (1 if i % 2 else -1)
                    point = point + zigzag
                points.append(point)
            
            # 创建折线
            spring_line = VMobject(color=GREEN)
            spring_line.set_points_as_corners(points)
            return spring_line
        
        spring = create_spring(
            start=fixed_dot.get_center(),
            end=mass.get_center(),
            segments=10,
            amplitude=0.2
        )
        
        # 添加到场景
        self.play(
            Create(fixed_dot), Write(fixed_label),
            Create(mass), Write(mass_label),
            Create(spring)
        )
        self.wait(1)
        
        # 模拟弹簧振动
        # 1. 初始位置
        self.play(mass.animate.shift(DOWN), run_time=0.5)
        
        # 更新弹簧
        new_spring = create_spring(
            start=fixed_dot.get_center(),
            end=mass.get_center(),
            segments=10,
            amplitude=0.3  # 拉长时振幅增大
        )
        self.play(Transform(spring, new_spring), run_time=0.5)
        self.wait(0.5)
        
        # 2. 释放弹簧 - 向上振动
        # 使用rate_func来模拟弹簧振动
        # 定义一个弹簧振动函数
        def spring_oscillation(t):
            # 指数衰减的正弦函数
            decay = np.exp(-2 * t)  # 衰减因子
            oscillation = np.sin(10 * t * PI)  # 振动因子
            return 0.5 + 0.5 * decay * oscillation
        
        # 创建振动动画
        oscillation_animations = [
            mass.animate.shift(UP*3),  # 总位移
            mass_label.animate.shift(UP*3)  # 标签跟随移动
        ]
        
        self.play(
            *oscillation_animations,
            rate_func=spring_oscillation,
            run_time=3
        )
        
        # 更新弹簧到最终位置
        final_spring = create_spring(
            start=fixed_dot.get_center(),
            end=mass.get_center(),
            segments=10,
            amplitude=0.2
        )
        self.play(Transform(spring, final_spring))
        self.wait(1)
        
        # 创建第二个弹簧系统 - 水平方向
        self.play(
            FadeOut(fixed_dot), FadeOut(fixed_label),
            FadeOut(mass), FadeOut(mass_label),
            FadeOut(spring)
        )
        
        # 水平弹簧系统
        wall = Line(DOWN*2, UP*2, color=GREY).shift(LEFT*4)
        wall_label = Text("墙", font_size=20).next_to(wall, UP, buff=0.2)
        
        box = Square(side_length=1, color=BLUE).shift(RIGHT*2)
        box_label = Text("物体", font_size=20).next_to(box, UP, buff=0.2)
        
        h_spring = create_spring(
            start=wall.get_center() + RIGHT*0.1,
            end=box.get_left(),
            segments=8,
            amplitude=0.2
        )
        
        # 添加到场景
        self.play(
            Create(wall), Write(wall_label),
            Create(box), Write(box_label),
            Create(h_spring)
        )
        self.wait(1)
        
        # 压缩弹簧
        self.play(box.animate.shift(LEFT*1.5), run_time=0.8)
        
        # 更新弹簧
        compressed_spring = create_spring(
            start=wall.get_center() + RIGHT*0.1,
            end=box.get_left(),
            segments=8,
            amplitude=0.3
        )
        self.play(Transform(h_spring, compressed_spring), run_time=0.5)
        self.wait(0.5)
        
        # 释放弹簧 - 水平振动
        box_label_copy = box_label.copy()
        
        self.play(
            box.animate.shift(RIGHT*4),
            box_label.animate.shift(RIGHT*4),
            rate_func=spring_oscillation,
            run_time=3
        )
        
        # 更新弹簧到最终位置
        final_h_spring = create_spring(
            start=wall.get_center() + RIGHT*0.1,
            end=box.get_left(),
            segments=8,
            amplitude=0.2
        )
        self.play(Transform(h_spring, final_h_spring))
        self.wait(1)
        
        # 结束信息
        conclusion = Text("高级弹簧动画演示完成！", color=GREEN, font_size=30)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)

# 运行命令：
# manim -pql advanced_spring_animation.py AdvancedSpringAnimation