# -*- coding: utf-8 -*-
"""
入口点配置 - 使模块可以在安装后自动加载
"""

def manim_load_plugin():
    """
    Manim插件加载入口点
    
    当Manim启动时，会自动调用此函数
    """
    try:
        from .auto_load import register_to_global_namespace
        # 注册到全局命名空间
        register_to_global_namespace()
    except ImportError as e:
        print(f"警告: 自动加载失败 - {e}")