# -*- coding: utf-8 -*-
from manim import *

class BasicCameraMovements(MovingCameraScene):
    def construct(self):
        # 创建标题
        title = Text("基本相机移动效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一些对象
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5).shift(LEFT*3)
        circle = Circle(radius=1, color=RED, fill_opacity=0.5).shift(RIGHT*3)
        triangle = Triangle(color=GREEN, fill_opacity=0.5).shift(UP*2)
        star = Star(color=YELLOW, fill_opacity=0.5).shift(DOWN*2)
        
        # 添加所有对象
        shapes = VGroup(square, circle, triangle, star)
        self.play(Create(shapes))
        self.wait(1)
        
        # 1. 移动相机焦点到方块
        self.play(self.camera.frame.animate.move_to(square))
        self.wait(1)
        
        # 2. 缩放相机以放大方块
        self.play(self.camera.frame.animate.scale(0.5))
        self.wait(1)
        
        # 3. 恢复相机
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait(1)
        
        # 4. 移动相机焦点到圆形
        self.play(self.camera.frame.animate.move_to(circle))
        self.wait(1)
        
        # 5. 缩放相机以放大圆形
        self.play(self.camera.frame.animate.scale(0.5))
        self.wait(1)
        
        # 6. 恢复相机
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait(1)
        
        # 7. 移动相机到三角形和星形之间
        midpoint = (triangle.get_center() + star.get_center()) / 2
        self.play(self.camera.frame.animate.move_to(midpoint))
        self.wait(1)
        
        # 8. 旋转相机视角
        self.play(self.camera.frame.animate.rotate(PI/4))
        self.wait(1)
        
        # 9. 恢复相机
        self.play(
            self.camera.frame.animate.rotate(-PI/4).move_to(ORIGIN).scale(1)
        )
        self.wait(1)
        
        # 结束信息
        conclusion = Text("基本相机移动效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


class CameraTrackingObjects(MovingCameraScene):
    def construct(self):
        # 创建标题
        title = Text("相机追踪物体", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一个将要移动的物体
        dot = Dot(color=RED)
        path = Circle(radius=3, color=WHITE)
        
        # 显示路径和起始点
        self.play(Create(path))
        self.play(Create(dot))
        self.wait(1)
        
        # 缩小相机视野，聚焦在点上
        self.play(self.camera.frame.animate.scale(0.5).move_to(dot))
        self.wait(1)
        
        # 创建点沿路径移动的动画
        dot_anim = MoveAlongPath(dot, path, run_time=8, rate_func=linear)
        
        # 创建相机追踪点的动画
        def update_camera(camera_frame):
            camera_frame.move_to(dot.get_center())
        
        # 添加相机更新函数
        self.camera.frame.add_updater(update_camera)
        
        # 播放点的移动动画
        self.play(dot_anim)
        
        # 移除相机更新函数
        self.camera.frame.remove_updater(update_camera)
        
        # 恢复相机
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait(1)
        
        # 结束信息
        conclusion = Text("相机追踪物体演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


class ZoomedSceneExample(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=3,
            zoomed_display_width=4,
            image_frame_stroke_width=4,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
            },
            **kwargs
        )

    def construct(self):
        # 创建标题
        title = Text("放大镜效果", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建一个复杂的图形
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"include_tip": False}
        )
        
        # 创建一个函数图像
        graph = axes.plot(lambda x: x**2, color=BLUE)
        graph_label = axes.get_graph_label(graph, "y=x^2", x_val=2, direction=UP)
        
        # 添加坐标轴和图像
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)
        
        # 激活放大镜
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        
        # 设置放大镜的位置和大小
        frame.move_to(axes.c2p(0, 0))  # 移动到原点
        frame.set_color(PURPLE)
        zoomed_display.move_to(RIGHT*3 + UP)
        
        # 显示放大镜
        self.play(Create(frame))
        self.activate_zooming(animate=True)
        
        # 移动放大镜查看不同部分
        self.play(frame.animate.move_to(axes.c2p(1, 1)))
        self.wait(1)
        self.play(frame.animate.move_to(axes.c2p(2, 4)))
        self.wait(1)
        self.play(frame.animate.move_to(axes.c2p(-1, 1)))
        self.wait(1)
        self.play(frame.animate.move_to(axes.c2p(-2, 4)))
        self.wait(1)
        
        # 移动放大显示区域
        self.play(zoomed_display.animate.shift(DOWN*3))
        self.wait(1)
        
        # 结束放大效果
        self.play(FadeOut(zoomed_display_frame), FadeOut(frame))
        self.wait(1)
        
        # 结束信息
        conclusion = Text("放大镜效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)


# 运行命令：
# manim -pql camera_effects_example.py BasicCameraMovements
# manim -pql camera_effects_example.py CameraTrackingObjects
# manim -pql camera_effects_example.py ZoomedSceneExample