# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

# 读取README.md文件作为长描述
readme_path = os.path.join(os.path.dirname(__file__), "manim_adaptive_layout", "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Manim自适应布局系统 - 专为不同屏幕比例优化的动画布局工具"

setup(
    name="manim-adaptive-layout",
    version="0.1.0",
    author="Manim中文补丁团队",
    author_email="example@example.com",
    description="Manim自适应布局系统 - 专为不同屏幕比例优化的动画布局工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/manim-adaptive-layout",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "manim>=0.17.0",
    ],
    # 添加入口点配置，使模块可以在安装后自动加载
    entry_points={
        "manim.plugins": [
            "manim_adaptive_layout = manim_adaptive_layout.entry_points:manim_load_plugin",
        ],
        "console_scripts": [
            "manim-render = manim_adaptive_layout.cli:main",
        ],
    },
    # 包含示例文件
    include_package_data=True,
    package_data={
        "manim_adaptive_layout": ["examples/*.py"],
    },
)