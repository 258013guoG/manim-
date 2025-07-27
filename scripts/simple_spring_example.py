# -*- coding: utf-8 -*-
from manim import *

class SimpleSpringExample(Scene):
    def construct(self):
        # 创建标题
        title = Text("简化弹簧效果示例", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 创建两个点和连接线
        dot1 = Dot(color=RED).shift(LEFT*3)
        dot2 = Dot(color=BLUE).shift(RIGHT*3)
        spring = Line(dot1.get_center(), dot2.get_center(), color=GREEN)
        
        # 添加到场景
        self.play(Create(dot1), Create(dot2), Create(spring))
        
        # 创建弹簧效果的更新函数 - 简化版本
        def spring_force(mob, dt):
            # 获取两点之间的向量
            vector = dot1.get_center() - mob.get_center()
            # 计算弹簧力 (简化的胡克定律)
            distance = np.linalg.norm(vector)
            if distance > 0:  # 防止除以零
                direction = vector / distance
                # 弹簧自然长度为6
                spring_constant = 0.5  # 弹簧常数
                force = direction * spring_constant * (distance - 6)  
                # 应用力 - 确保velocity是浮点数数组
                mob.velocity = mob.velocity + force * dt
                # 添加阻尼
                mob.velocity = mob.velocity * 0.95
                # 更新位置
                mob.shift(mob.velocity * dt)
        
        # 更新弹簧线
        def update_spring(spring):
            spring.put_start_and_end_on(dot1.get_center(), dot2.get_center())
        
        # 初始化速度 - 明确使用浮点数数组
        dot2.velocity = np.array([0.0, 0.0, 0.0], dtype=float)
        
        # 添加更新器
        dot2.add_updater(spring_force)
        spring.add_updater(update_spring)
        
        # 移动第一个点，观察弹簧效果
        self.play(dot1.animate.shift(UP*2), run_time=1)
        self.wait(2)  # 等待弹簧效果
        
        self.play(dot1.animate.shift(DOWN*4), run_time=1)
        self.wait(2)  # 等待弹簧效果
        
        self.play(dot1.animate.shift(RIGHT*2 + UP*2), run_time=1)
        self.wait(2)  # 等待弹簧效果
        
        # 移除更新器
        dot2.remove_updater(spring_force)
        spring.remove_updater(update_spring)
        
        # 结束信息
        conclusion = Text("简化弹簧效果演示完成！", color=GREEN, font_size=36)
        conclusion.to_edge(DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)

# 运行命令：
# manim -pql simple_spring_example.py SimpleSpringExample