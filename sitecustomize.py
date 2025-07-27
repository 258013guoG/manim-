#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动加载Manim中文补丁（零代码方案）

这个文件会在Python启动时自动加载，无需用户手动导入任何内容。
只需将此文件放在项目根目录或Python路径中的任何位置即可。

特点：
- 完全零代码：无需任何导入语句
- 智能检测：只在Manim项目中激活
- 自动加载：支持所有中文和符号
- 适合非程序员：不需要编程知识
"""

import sys
import os
import importlib.util
from pathlib import Path

# 检测是否为Manim环境的函数
def is_manim_environment():
    # 检查是否已导入manim模块
    if 'manim' in sys.modules:
        return True
    
    # 检查是否有manim相关命令行参数
    if any('manim' in arg.lower() for arg in sys.argv):
        return True
    
    # 检查当前目录或父目录是否有manim.cfg文件
    current_dir = Path.cwd()
    for _ in range(3):  # 检查当前目录及向上两级目录
        if (current_dir / 'manim.cfg').exists():
            return True
        if current_dir.parent == current_dir:  # 已到达根目录
            break
        current_dir = current_dir.parent
    
    return False

# 只在Manim环境中加载补丁
if is_manim_environment():
    try:
        # 尝试导入manim
        import manim
        
        # 检查是否已经应用了补丁
        if not hasattr(manim, "_chinese_patch_applied"):
            # 获取当前文件所在目录
            current_dir = Path(__file__).parent.absolute()
            
            # 将patch目录添加到Python路径
            patch_dir = current_dir / "patch"
            if patch_dir.exists():
                # 导入补丁
                try:
                    # 导入全自动补丁增强版
                    from patch import auto_chinese_patch
                    
                    # 标记补丁已应用
                    manim._chinese_patch_applied = True
                    
                    print("\n✅ Manim中文补丁已自动加载！现在可以直接使用中文，无需任何导入语句。\n")
                except ImportError as e:
                    print(f"\n⚠️ 无法导入中文补丁：{e}\n")
            else:
                print(f"\n⚠️ 未找到patch目录（{patch_dir}），无法自动加载中文补丁\n")
    except ImportError as e:
        # 检测到Manim环境但无法导入manim模块
        print(f"\n⚠️ 检测到Manim环境但无法导入manim模块：{e}\n")