# -*- coding: utf-8 -*-
from manim import *

class PathMotionExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("沿路径运动效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一个复杂的路径
        path = ParametricFunction(
            lambda t: np.array([
                3 * np.sin(t),
                2 * np.cos(t),
                0
            ]), t_range=[0, TAU], color=BLUE
        )
        
        # 创建一个将沿路径移动的对象
        dot = Dot(color=RED)
        
        # 显示路径和起始点
        self.play(Create(path))
        self.play(Create(dot))
        self.wait(1)
        
        # 使用MoveAlongPath动画让点沿路径移动
        self.play(MoveAlongPath(dot, path), run_time=5, rate_func=linear)
        self.wait(1)
        
        # 清除场景
        self.play(FadeOut(dot), FadeOut(path))
        
        # 创建更复杂的路径 - 心形曲线
        heart_path = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t) ** 3,
                13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                0
            ]), t_range=[0, TAU], color=RED
        ).scale(0.2)
        
        # 创建一个小球
        ball = Circle(radius=0.2, fill_opacity=1, color=YELLOW)
        
        # 显示心形路径和小球
        self.play(Create(heart_path))
        self.play(Create(ball))
        self.wait(1)
        
        # 让小球沿心形路径移动
        self.play(MoveAlongPath(ball, heart_path), run_time=5, rate_func=linear)
        self.wait(1)
        
        # 结束信息
        conclusion = Text("沿路径运动效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


class TracedPathExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("保留运动轨迹效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一个点
        dot = Dot(color=YELLOW)
        
        # 创建轨迹
        path = TracedPath(dot.get_center, stroke_width=3, stroke_color=ORANGE)
        
        # 添加点和轨迹到场景
        self.add(dot, path)
        
        # 创建复杂的运动
        self.play(
            dot.animate.move_to(RIGHT*3),
            run_time=1
        )
        self.play(
            dot.animate.move_to(RIGHT*3 + UP*2),
            run_time=1
        )
        self.play(
            dot.animate.move_to(LEFT*3 + UP*2),
            run_time=2
        )
        self.play(
            dot.animate.move_to(LEFT*3 + DOWN*2),
            run_time=1
        )
        self.play(
            dot.animate.move_to(RIGHT*3 + DOWN*2),
            run_time=2
        )
        self.play(
            dot.animate.move_to(ORIGIN),
            run_time=2
        )
        self.wait(1)
        
        # 清除场景
        self.play(FadeOut(dot), FadeOut(path))
        
        # 创建一个更复杂的例子 - 参数曲线
        dot2 = Dot(color=RED)
        path2 = TracedPath(dot2.get_center, stroke_width=3, stroke_color=BLUE)
        
        self.add(dot2, path2)
        
        # 创建参数运动
        def spiral_path(t):
            return np.array([
                np.cos(3*t) * t/5,
                np.sin(3*t) * t/5,
                0
            ])
        
        # 创建更新函数
        def update_dot(mob, dt):
            mob.time += dt
            mob.move_to(spiral_path(mob.time))
        
        # 初始化时间
        dot2.time = 0
        
        # 添加更新器
        dot2.add_updater(update_dot)
        
        # 运行动画
        self.wait(8)
        
        # 移除更新器
        dot2.remove_updater(update_dot)
        
        # 结束信息
        conclusion = Text("保留运动轨迹效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


class AnimationCombinationExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("动画组合效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 1. LaggedStart - 延迟启动动画
        subtitle1 = Text("LaggedStart - 延迟启动动画", font_size=32)
        subtitle1.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle1))
        
        # 创建多个对象
        squares = VGroup(*[Square(side_length=0.5, fill_opacity=0.5) for _ in range(10)])
        squares.arrange(RIGHT, buff=0.3)
        squares.set_color_by_gradient(BLUE, GREEN, RED)
        
        # 使用LaggedStart依次显示方块
        self.play(LaggedStart(
            *[Create(square) for square in squares],
            lag_ratio=0.2,
            run_time=5
        ))
        self.wait(1)
        
        # 使用LaggedStart依次移动方块
        self.play(LaggedStart(
            *[square.animate.shift(DOWN) for square in squares],
            lag_ratio=0.2,
            run_time=3
        ))
        self.wait(1)
        
        # 清除方块
        self.play(FadeOut(squares), FadeOut(subtitle1))
        
        # 2. Succession - 顺序启动动画
        subtitle2 = Text("Succession - 顺序启动动画", font_size=32)
        subtitle2.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle2))
        
        # 创建三个不同的对象
        circle = Circle(radius=1, color=RED)
        square = Square(side_length=2, color=BLUE)
        triangle = Triangle(color=GREEN)
        
        # 使用Succession依次播放不同的动画
        self.play(Succession(
            Create(circle),
            FadeOut(circle),
            Create(square),
            FadeOut(square),
            Create(triangle),
            FadeOut(triangle)
        ))
        self.wait(1)
        
        # 清除字幕
        self.play(FadeOut(subtitle2))
        
        # 3. AnimationGroup - 动画组
        subtitle3 = Text("AnimationGroup - 动画组", font_size=32)
        subtitle3.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle3))
        
        # 创建三个对象
        circle = Circle(radius=1, color=RED).shift(LEFT*3)
        square = Square(side_length=1.5, color=BLUE)
        triangle = Triangle(color=GREEN).shift(RIGHT*3)
        
        # 使用AnimationGroup同时播放不同的动画
        self.play(AnimationGroup(
            Create(circle),
            Create(square),
            Create(triangle),
            lag_ratio=0.5,  # 添加一些延迟
            run_time=3
        ))
        self.wait(1)
        
        # 使用AnimationGroup同时播放不同的动画
        self.play(AnimationGroup(
            circle.animate.scale(0.5),
            square.animate.rotate(PI/2),
            triangle.animate.shift(UP),
            lag_ratio=0.3,
            run_time=2
        ))
        self.wait(1)
        
        # 结束信息
        conclusion = Text("动画组合效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


class AnimationLinkageExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("动画联动效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一个控制点和被控制对象
        control_dot = Dot(color=RED).shift(LEFT*3)
        controlled_square = Square(side_length=1, color=BLUE).shift(RIGHT*3)
        
        # 添加到场景
        self.play(Create(control_dot), Create(controlled_square))
        self.wait(1)
        
        # 创建一条连接线
        line = Line(control_dot.get_center(), controlled_square.get_center(), color=YELLOW)
        self.play(Create(line))
        
        # 创建更新函数 - 方块跟随点移动
        def update_square(square):
            square.move_to(control_dot.get_center() + RIGHT*6)
        
        # 创建更新函数 - 线跟随点和方块
        def update_line(line):
            line.put_start_and_end_on(control_dot.get_center(), controlled_square.get_center())
        
        # 添加更新器
        controlled_square.add_updater(update_square)
        line.add_updater(update_line)
        
        # 移动控制点，观察联动效果
        self.play(control_dot.animate.shift(UP*2), run_time=2)
        self.wait(1)
        self.play(control_dot.animate.shift(RIGHT*2), run_time=2)
        self.wait(1)
        self.play(control_dot.animate.shift(DOWN*4), run_time=2)
        self.wait(1)
        self.play(control_dot.animate.shift(LEFT*2 + UP*2), run_time=2)
        self.wait(1)
        
        # 移除更新器
        controlled_square.remove_updater(update_square)
        line.remove_updater(update_line)
        
        # 清除场景
        self.play(FadeOut(control_dot), FadeOut(controlled_square), FadeOut(line))
        
        # 创建更复杂的联动示例 - 弹簧效果
        dot1 = Dot(color=RED).shift(LEFT*3)
        dot2 = Dot(color=BLUE).shift(RIGHT*3)
        spring = Line(dot1.get_center(), dot2.get_center(), color=GREEN)
        
        # 添加到场景
        self.play(Create(dot1), Create(dot2), Create(spring))
        
        # 创建弹簧效果的更新函数
        def spring_force(mob, dt):
            # 获取两点之间的向量
            vector = dot1.get_center() - mob.get_center()
            # 计算弹簧力 (简化的胡克定律)
            distance = np.linalg.norm(vector)
            direction = vector / distance
            force = direction * (distance - 6)  # 6是弹簧的自然长度
            # 应用力
            mob.velocity += force * dt
            # 添加阻尼
            mob.velocity *= 0.99
            # 更新位置
            mob.shift(mob.velocity * dt)
        
        # 更新弹簧线
        def update_spring(spring):
            spring.put_start_and_end_on(dot1.get_center(), dot2.get_center())
        
        # 初始化速度 - 使用浮点数数组
        dot2.velocity = np.array([0.0, 0.0, 0.0], dtype=float)
        
        # 添加更新器
        dot2.add_updater(spring_force)
        spring.add_updater(update_spring)
        
        # 移动第一个点，观察弹簧效果
        self.play(dot1.animate.shift(UP*2), run_time=2)
        self.wait(3)  # 等待弹簧效果
        
        self.play(dot1.animate.shift(DOWN*4), run_time=2)
        self.wait(3)  # 等待弹簧效果
        
        self.play(dot1.animate.shift(RIGHT*2 + UP*2), run_time=2)
        self.wait(3)  # 等待弹簧效果
        
        # 结束信息
        conclusion = Text("动画联动效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


# 运行命令：
# manim -pql advanced_animation_effects.py PathMotionExample
# manim -pql advanced_animation_effects.py TracedPathExample
# manim -pql advanced_animation_effects.py AnimationCombinationExample
# manim -pql advanced_animation_effects.py AnimationLinkageExample