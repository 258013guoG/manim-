#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manim自适应布局渲染工具的命令行入口点

这个脚本提供了一个命令行工具，使用户能够直接调用渲染工具。

使用方法：
    manim-render <文件名> <场景名> [其他manim参数]
    manim-render --batch <文件名> [其他manim参数]  # 批量渲染文件中的所有场景
    manim-render --list-platforms  # 列出支持的平台
    manim-render --help  # 显示帮助信息
"""

import sys
from manim_adaptive_layout.render import main as render_main

def main():
    """
    命令行入口点
    """
    # 将命令名称从manim-render替换为render.py
    if len(sys.argv) > 0:
        sys.argv[0] = "render.py"
    
    # 调用渲染工具的主函数
    render_main()

if __name__ == "__main__":
    main()