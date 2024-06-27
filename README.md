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

## 打包运行

1. 使用`pyinstaller`进行打包例如：

   ```
   pyinstaller --onefile --console --name=KeepImage --upx-dir="E:\Program Files (x86)\upx-4.2.3-win64" --collect-all "tkinterdnd2" ./KeepImage.py
   ```

   其中`--upx-dir`为可选，打包必须加入`--collect-all "tkinterdnd2"`避免运行报错

2. 如果遇到证书问题需要将`cacert.pem`文件保存在打包后的exe目录下才能避免运行报错，如果不想保存在exe同级目录下请将`cacert.pem`保存到你想要的位置并修改下列代码：

3. ```
   # 设置证书路径，不然打包运行报错
   os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')
   ```

## 依赖

- `tkinter`：用于创建 GUI
- `tinify`：用于图像压缩
- `Pillow`：用于图像处理
- `tkinterdnd2`：用于拖放功能

可以通过以下命令安装依赖：
```bash
pip install tkinter Pillow tinify tkinterdnd2
```

## 图片

![image-20240627225629008](https://alist.ksmlc.cn/d/Private/Cloudreve/图片/202406272256919.png)
