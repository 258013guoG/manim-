#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安装Manim中文补丁

这个脚本用于安装Manim中文补丁,使Manim支持中文和各种符号.
"""

import os
import shutil
import site
import sys
from pathlib import Path

def install_sitecustomize():
    """安装sitecustomize.py到用户的site-packages目录"""
    try:
        # 获取用户的site-packages目录
        user_site = site.getusersitepackages()
        
        # 如果目录不存在，创建它
        os.makedirs(user_site, exist_ok=True)
        
        # 复制sitecustomize.py文件
        shutil.copy('sitecustomize.py', os.path.join(user_site, 'sitecustomize.py'))
        
        # 复制patch目录
        patch_dir = Path(user_site) / 'patch'
        if patch_dir.exists():
            shutil.rmtree(patch_dir)
        shutil.copytree('patch', patch_dir)
        
        print(f'
✅ sitecustomize.py和patch目录已安装到{user_site}
')
        print('现在您可以在任何Manim项目中直接使用中文, 无需任何导入语句!')
        return True
    except Exception as e:
        print(f'
❌ 安装失败: {e}
')
        print('您仍然可以通过手动导入patch.auto_chinese_patch来使用中文补丁.')
        return False

def main():
    """主函数"""
    print('===== Manim中文补丁安装程序 =====')
    print('
这个程序将安装Manim中文补丁, 使Manim支持中文和各种符号.')
    print('
安装选项:')
    print('1. 安装到Python的site-packages目录(推荐, 全局生效)')
    print('2. 仅查看使用说明')
    print('3. 退出')
    
    choice = input('
请选择(1/2/3): ')
    
    if choice == '1':
        install_sitecustomize()
    elif choice == '2':
        print('
请查看README.md文件获取详细使用说明.')
    else:
        print('
已取消安装.')

if __name__ == '__main__':
    main()
