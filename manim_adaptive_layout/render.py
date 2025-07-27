#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manim自适应布局渲染工具

这个脚本可以自动识别场景中的平台设置并生成正确的渲染命令，
避免屏幕比例被挤压的问题。

使用方法：
    python render.py <文件名> <场景名> [其他manim参数]
    python render.py --batch <文件名> [其他manim参数]  # 批量渲染文件中的所有场景
    python render.py --list-platforms  # 列出支持的平台
    python render.py --help  # 显示帮助信息

例如：
    python render.py examples/advanced_example.py AdvancedExample -pql
    python render.py --batch examples/render_tool_example.py -pql
"""

import sys
import os
import re
import inspect
import importlib.util
import subprocess
from pathlib import Path

# 平台分辨率映射
PLATFORM_RESOLUTIONS = {
    "tiktok": "1080,1920",      # 抖音 9:16
    "douyin": "1080,1920",     # 抖音别名
    "xiaohongshu": "1080,1440", # 小红书 3:4
    "xhs": "1080,1440",        # 小红书别名
    "standard": "1920,1080",    # 标准 16:9
    "horizontal": "1920,1080",  # 标准横屏别名
    "vertical": "1080,1920",    # 通用竖屏
    "square": "1080,1080",      # 方形 1:1
    "bilibili": "1920,1080",    # B站
    "youtube": "1920,1080",     # YouTube
    "instagram": "1080,1080",   # Instagram
    "weibo": "1080,1920",       # 微博
}

# 平台别名映射
PLATFORM_ALIASES = {
    "douyin": "tiktok",
    "xhs": "xiaohongshu",
    "horizontal": "standard",
    "bilibili": "standard",
    "youtube": "standard",
    "instagram": "square",
    "weibo": "vertical",
}

def show_help():
    """
    显示帮助信息
    """
    print("Manim自适应布局渲染工具")
    print("\n使用方法:")
    print("  python render.py <文件名> <场景名> [其他manim参数]")
    print("  python render.py --batch <文件名> [其他manim参数]  # 批量渲染文件中的所有场景")
    print("  python render.py --list-platforms  # 列出支持的平台")
    print("  python render.py --help  # 显示帮助信息")
    print("\n例如:")
    print("  python render.py examples/advanced_example.py AdvancedExample -pql")
    print("  python render.py --batch examples/render_tool_example.py -pql")

def list_platforms():
    """
    列出支持的平台
    """
    print("支持的平台:")
    print("\n主要平台:")
    for platform, resolution in sorted(PLATFORM_RESOLUTIONS.items()):
        if platform not in PLATFORM_ALIASES:
            width, height = resolution.split(",")
            ratio = float(width) / float(height)
            ratio_str = f"{int(ratio * 100) / 100:.2f}" if ratio < 1 else f"{int(ratio * 100) / 100:.2f}"
            print(f"  {platform}: {width}×{height} (比例 {ratio_str})")
    
    print("\n平台别名:")
    for alias, platform in sorted(PLATFORM_ALIASES.items()):
        print(f"  {alias} → {platform}")

def load_scene_class(file_path, scene_name):
    """
    动态加载场景类
    """
    try:
        # 获取绝对路径
        abs_path = Path(file_path).resolve()
        
        # 加载模块
        spec = importlib.util.spec_from_file_location("module.name", abs_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 获取场景类
        if hasattr(module, scene_name):
            return getattr(module, scene_name)
        else:
            print(f"错误: 在文件 {file_path} 中未找到场景 {scene_name}")
            return None
    except Exception as e:
        print(f"错误: 加载场景类失败 - {e}")
        return None

def get_all_scenes_from_file(file_path):
    """
    从文件中获取所有场景类
    """
    try:
        # 获取绝对路径
        abs_path = Path(file_path).resolve()
        
        # 加载模块
        spec = importlib.util.spec_from_file_location("module.name", abs_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 获取所有场景类
        from manim import Scene
        scenes = []
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Scene) and obj != Scene:
                scenes.append(name)
        
        return scenes
    except Exception as e:
        print(f"错误: 加载文件失败 - {e}")
        return []

def detect_platform_from_code(scene_class):
    """
    从场景类代码中检测平台设置
    """
    # 获取场景类的源代码
    source_code = inspect_source_code(scene_class)
    if not source_code:
        return None
    
    # 检查是否使用了create_platform_optimized_layout方法
    platform_match = re.search(r'create_platform_optimized_layout\s*\(\s*self\s*,\s*platform\s*=\s*["\']([^"\']*)["\'](?:\s*,|\s*\))', source_code)
    if platform_match:
        platform = platform_match.group(1).lower()
        # 处理平台别名
        if platform in PLATFORM_ALIASES:
            platform = PLATFORM_ALIASES[platform]
        return platform
    
    # 检查是否直接设置了config.frame_width和config.frame_height
    if re.search(r'config\.frame_width\s*=\s*9', source_code) and re.search(r'config\.frame_height\s*=\s*16', source_code):
        return "tiktok"
    elif re.search(r'config\.frame_width\s*=\s*9', source_code) and re.search(r'config\.frame_height\s*=\s*12', source_code):
        return "xiaohongshu"
    elif re.search(r'config\.frame_width\s*=\s*16', source_code) and re.search(r'config\.frame_height\s*=\s*9', source_code):
        return "standard"
    elif re.search(r'config\.frame_width\s*=\s*1', source_code) and re.search(r'config\.frame_height\s*=\s*1', source_code):
        return "square"
    
    return None

def inspect_source_code(scene_class):
    """
    获取场景类的源代码
    """
    try:
        return inspect.getsource(scene_class)
    except Exception as e:
        print(f"警告: 无法获取场景类源代码 - {e}")
        return None

def build_render_command(file_path, scene_name, platform, extra_args):
    """
    构建渲染命令
    """
    resolution = PLATFORM_RESOLUTIONS.get(platform)
    if not resolution:
        print(f"警告: 未知平台 '{platform}'，将使用默认分辨率")
        return ["manim"] + extra_args + [file_path, scene_name]
    
    # 检查是否已经包含了--resolution参数
    has_resolution = any(arg.startswith("--resolution=") for arg in extra_args)
    if has_resolution:
        print(f"注意: 命令行中已包含--resolution参数，将使用命令行指定的分辨率")
        return ["manim"] + extra_args + [file_path, scene_name]
    
    # 添加--resolution参数
    return ["manim", f"--resolution={resolution}"] + extra_args + [file_path, scene_name]

def render_scene(file_path, scene_name, extra_args):
    """
    渲染单个场景
    """
    # 加载场景类
    scene_class = load_scene_class(file_path, scene_name)
    if not scene_class:
        return False
    
    # 检测平台
    platform = detect_platform_from_code(scene_class)
    if platform:
        print(f"检测到平台: {platform}")
    else:
        print("未检测到平台设置，将使用默认分辨率")
        platform = "standard"
    
    # 构建渲染命令
    cmd = build_render_command(file_path, scene_name, platform, extra_args)
    cmd_str = " ".join(cmd)
    print(f"\n执行渲染命令: {cmd_str}\n")
    
    # 执行渲染命令
    try:
        subprocess.run(cmd)
        return True
    except Exception as e:
        print(f"错误: 执行渲染命令失败 - {e}")
        return False

def batch_render(file_path, extra_args):
    """
    批量渲染文件中的所有场景
    """
    # 获取所有场景
    scenes = get_all_scenes_from_file(file_path)
    if not scenes:
        print(f"错误: 在文件 {file_path} 中未找到任何场景")
        return False
    
    print(f"在文件 {file_path} 中找到 {len(scenes)} 个场景:")
    for i, scene in enumerate(scenes):
        print(f"  {i+1}. {scene}")
    
    # 渲染所有场景
    success_count = 0
    for i, scene in enumerate(scenes):
        print(f"\n[{i+1}/{len(scenes)}] 渲染场景: {scene}")
        if render_scene(file_path, scene, extra_args):
            success_count += 1
    
    print(f"\n批量渲染完成: {success_count}/{len(scenes)} 个场景成功")
    return success_count > 0

def main():
    # 检查参数
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    # 处理特殊命令
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        show_help()
        sys.exit(0)
    
    if sys.argv[1] == "--list-platforms":
        list_platforms()
        sys.exit(0)
    
    # 批量渲染模式
    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("错误: 批量渲染模式需要指定文件名")
            show_help()
            sys.exit(1)
        
        file_path = sys.argv[2]
        extra_args = sys.argv[3:]
        
        if not batch_render(file_path, extra_args):
            sys.exit(1)
    else:
        # 单场景渲染模式
        if len(sys.argv) < 3:
            print("错误: 需要指定文件名和场景名")
            show_help()
            sys.exit(1)
        
        file_path = sys.argv[1]
        scene_name = sys.argv[2]
        extra_args = sys.argv[3:]
        
        if not render_scene(file_path, scene_name, extra_args):
            sys.exit(1)

if __name__ == "__main__":
    main()