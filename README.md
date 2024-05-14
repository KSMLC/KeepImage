# KeepImage

KeepImage 是一个使用 Tkinter 和 Tinify API 的简单图像压缩工具，支持拖放和批量压缩图像。

## 功能

- 选择单个或多个图像文件进行压缩
- 支持拖放文件进行选择
- 实时显示正在处理的图像
- 进度条显示压缩进度
- 压缩完成后提示
- 自动创建输出文件夹（如果不存在）
- 清空选择的图像列表

## 支持的文件格式

- JPEG (.jpg, .jpeg)
- PNG (.png)
- WebP (.webp)

## 使用

1. 在 `KeepImage.py` 文件中设置你的 Tinify API 密钥

    API获取：[TinyPNG – 开发者API (tinify.cn)](https://tinify.cn/developers)

    ```python
    tinify.key = "YOUR_API_KEY"
    ```

2. 运行脚本
    ```bash
    python KeepImage.py
    ```

3. 使用界面选择或拖放图像文件，点击“压缩图像”按钮进行压缩。

## 依赖

- `tkinter`：用于创建 GUI
- `tinify`：用于图像压缩
- `Pillow`：用于图像处理
- `tkinterdnd2`：用于拖放功能

可以通过以下命令安装依赖：
```bash
pip install tkinter Pillow tinify tkinterdnd2
