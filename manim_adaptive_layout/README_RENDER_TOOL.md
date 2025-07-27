# Manim 自适应布局渲染工具

这个工具可以自动识别场景中的平台设置并生成正确的渲染命令，避免屏幕比例被挤压的问题。

## 问题背景

在使用 `AdaptiveLayoutSystem.create_platform_optimized_layout()` 方法设置不同平台的屏幕比例时，这些设置仅在代码运行时生效，不会影响最终的渲染命令。如果不在渲染命令中指定正确的分辨率，可能会导致屏幕比例被挤压，影响最终效果。

## 解决方案

`manim-render` 工具会自动：

1. 分析场景代码，检测使用的平台设置
2. 根据平台设置生成正确的渲染命令，包含适当的 `--resolution` 参数
3. 执行渲染命令，确保输出视频具有正确的屏幕比例

## 安装方法

```bash
pip install -e .
```

## 使用方法

### 命令行方式

```bash
manim-render <文件名> <场景名> [其他manim参数]
```

例如：

```bash
manim-render examples/advanced_example.py AdvancedExample -pql
```

### 直接调用脚本

```bash
python -m manim_adaptive_layout.render <文件名> <场景名> [其他manim参数]
```

或者：

```bash
python manim_adaptive_layout/render.py <文件名> <场景名> [其他manim参数]
```

## 支持的平台

- `tiktok`: 抖音竖屏 (9:16, 1080×1920)
- `xiaohongshu`: 小红书 (3:4, 1080×1440)
- `standard`: 标准横屏 (16:9, 1920×1080)

## 工作原理

1. 工具会动态加载场景类并分析其源代码
2. 检测是否使用了 `create_platform_optimized_layout` 方法以及指定的平台参数
3. 如果没有找到明确的平台设置，会检查是否直接设置了 `config.frame_width` 和 `config.frame_height`
4. 根据检测到的平台，自动添加正确的 `--resolution` 参数
5. 如果命令行中已经包含了 `--resolution` 参数，则优先使用命令行指定的分辨率

## 注意事项

- 如果无法检测到平台设置，将默认使用标准横屏 (16:9) 分辨率
- 工具会尝试获取场景类的源代码进行分析，如果无法获取源代码，可能无法正确检测平台设置
- 如果在命令行中已经指定了 `--resolution` 参数，工具将优先使用命令行指定的分辨率