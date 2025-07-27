# -*- coding: utf-8 -*-
"""
自动加载模块 - 使AdaptiveLayoutSystem可以在不导入的情况下直接使用

此模块会在Manim启动时自动将AdaptiveLayoutSystem注册到全局命名空间
"""

import sys
import importlib
from pathlib import Path

# 尝试导入manim
try:
    import manim
except ImportError:
    print("警告: 未找到manim库，自动加载功能将不可用")
    sys.exit(0)

# 导入AdaptiveLayoutSystem
try:
    from manim_adaptive_layout import AdaptiveLayoutSystem
except ImportError:
    print("警告: 未找到manim_adaptive_layout模块，自动加载功能将不可用")
    sys.exit(0)

def register_to_global_namespace():
    """
    将AdaptiveLayoutSystem注册到manim全局命名空间
    """
    # 获取manim模块的全局命名空间
    manim_globals = sys.modules['manim'].__dict__
    
    # 注册AdaptiveLayoutSystem
    manim_globals['AdaptiveLayoutSystem'] = AdaptiveLayoutSystem
    
    print("✅ AdaptiveLayoutSystem已自动加载到全局命名空间，可直接使用")

# 在导入时自动注册
register_to_global_namespace()