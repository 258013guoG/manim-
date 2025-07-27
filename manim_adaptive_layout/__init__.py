# -*- coding: utf-8 -*-
"""
Manim自适应布局系统

提供全面的布局管理功能，确保内容在不同屏幕比例下正确显示
特别优化了长文本处理和元素自动排列功能
"""

from .adaptive_layout_system import AdaptiveLayoutSystem

# 导入渲染工具
from . import render
from . import cli

__version__ = '0.1.0'
__all__ = ['AdaptiveLayoutSystem', 'render', 'cli']

# 尝试自动加载到全局命名空间
try:
    from .auto_load import register_to_global_namespace
    # 自动加载已在auto_load模块中执行
except ImportError:
    pass