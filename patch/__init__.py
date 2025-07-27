#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manim中文支持工具集

提供三种使用方式：
1. 全自动补丁增强版：import patch.auto_chinese_patch
2. 专用类：from patch import ChineseText, ChineseMath, ChineseTex
3. 手动应用补丁：from patch.manim_chinese_utils import apply_chinese_patch
"""

# 导出所有工具
from .manim_chinese_utils import (
    ChineseText,
    ChineseMath,
    ChineseTex,
    apply_chinese_patch,
    CHINESE_PATTERN,
    DEFAULT_CHINESE_FONT,
    CTEX_TEMPLATE,
    create_ctex_template
)

# 导出全自动补丁增强版模块（使用相对导入避免循环导入）
from . import auto_chinese_patch

# 自动应用中文补丁（专用类模式）
apply_chinese_patch()