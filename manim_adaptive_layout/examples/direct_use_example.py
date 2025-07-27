# -*- coding: utf-8 -*-
"""
无需导入直接使用AdaptiveLayoutSystem示例

演示了如何在不导入的情况下直接使用AdaptiveLayoutSystem
这得益于自动加载功能，AdaptiveLayoutSystem会自动注册到全局命名空间

渲染命令：
    抖音竖屏: manim -pql --resolution=1080,1920 direct_use_example.py DirectUseExample
    小红书: manim -pql --resolution=1080,1440 direct_use_example.py DirectUseExample
    标准横屏: manim -pql --resolution=1920,1080 direct_use_example.py DirectUseExample

注意：必须使用--resolution参数指定正确的分辨率，否则可能导致屏幕比例不正确
"""

# 只导入manim，不导入AdaptiveLayoutSystem
from manim import *

# AdaptiveLayoutSystem会自动可用，无需导入

class DirectUseExample(Scene):
    def construct(self):
        # 1. 设置抖音竖屏比例并创建安全区域
        # 直接使用AdaptiveLayoutSystem，无需导入
        safe_zone, safe_width, safe_height = AdaptiveLayoutSystem.create_platform_optimized_layout(
            self, platform="tiktok", show_safe_zone=True
        )
        
        # 2. 创建标题
        title = Text("无需导入直接使用示例", font_size=48)
        title.to_edge(UP, buff=1)
        self.add(title)
        
        # 3. 创建说明文本
        explanation = AdaptiveLayoutSystem.create_adaptive_paragraph(
            "这个示例演示了如何在不导入的情况下直接使用AdaptiveLayoutSystem。\n\n" +
            "这得益于自动加载功能，AdaptiveLayoutSystem会自动注册到全局命名空间，使您可以在任何Manim场景中直接使用它。", 
            max_width=safe_width * 0.9, 
            max_height=safe_height * 0.3,
            font_size=36
        )
        explanation.next_to(title, DOWN, buff=0.8)
        self.add(explanation)
        
        # 4. 创建功能列表
        features = [
            "✅ 无需导入，直接使用",
            "✅ 自动适应不同屏幕比例",
            "✅ 全局可用，随处调用",
            "✅ 与原生Manim无缝集成"
        ]
        
        feature_texts = []
        for feature in features:
            text = Text(feature, font_size=32, color=GREEN)
            feature_texts.append(text)
        
        # 使用自动排列功能防止重叠
        arranged_features = AdaptiveLayoutSystem.prevent_overlap(
            feature_texts, direction=DOWN, min_buff=0.5
        )
        arranged_features.next_to(explanation, DOWN, buff=1)
        self.add(arranged_features)
        
        # 5. 添加平台特定元素
        AdaptiveLayoutSystem.add_platform_elements(
            self, platform="tiktok", username="@数学动画"
        )
        
        # 6. 添加使用说明
        usage_title = Text("使用方法", font_size=36, color=YELLOW)
        usage_title.next_to(arranged_features, DOWN, buff=1)
        self.add(usage_title)
        
        usage_code = Code(
            code_string="""from manim import *

class MyScene(Scene):
    def construct(self):
        # 直接使用AdaptiveLayoutSystem
        safe_zone, safe_width, safe_height = \
            AdaptiveLayoutSystem.create_platform_optimized_layout(
                self, platform="tiktok"
            )
        
        # 创建自适应文本
        text = AdaptiveLayoutSystem.create_adaptive_paragraph(
            "自动换行和缩放的文本", 
            max_width=safe_width
        )
        
        self.add(text)""",
            language="python",
            background="window",
            background_config={
                "stroke_width": 1,
                "stroke_color": WHITE
            },
            paragraph_config={"font_size": 24}
        )
        usage_code.next_to(usage_title, DOWN, buff=0.5)
        
        # 确保代码不超出安全区域
        if usage_code.width > safe_width * 0.9:
            usage_code.width = safe_width * 0.9
        
        self.add(usage_code)