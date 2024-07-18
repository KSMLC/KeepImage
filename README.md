# 图像压缩器

## 简介
这是一个使用 Python 编写的图像压缩工具，通过 `tkinter` 库构建图形用户界面（GUI），支持用户选择本地图像文件或者通过拖放的方式添加图像，并使用 `tinify` 库对图像进行压缩处理。

## 依赖库
- `tkinter`
- `filedialog`
- `messagebox`
- `ttk`
- `tkinterdnd2`
- `tinify`
- `PIL`
- `os`
- `sys`

## 环境设置
在运行代码前，请确保您已经安装了上述依赖库。

### 设置证书路径
为了避免打包运行时出现错误，需要设置证书路径：

```python
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')
```

### 设置 Tinify API 密钥
您需要获取 `Tinify` 的 API 密钥，并在代码中设置：

API获取：[TinyPNG – 开发者API (tinify.cn)](https://gitee.com/link?target=https%3A%2F%2Ftinify.cn%2Fdevelopers)

```python
tinify.key = "YOUR_API_KEY"
```

## 功能说明

### 选择文件
通过点击“浏览”按钮，可以选择要压缩的图像文件。支持的文件类型包括 `.jpg`、`.jpeg`、`.png` 和 `.webp`。

### 拖放文件
支持将图像文件直接拖放到应用窗口中进行添加。

### 加载图像预览
在选择或拖放图像文件后，会显示缩略图预览。

### 压缩图像
选择图像文件后，点击“压缩图像”按钮，选择输出文件夹，即可对图像进行压缩处理。压缩过程中会显示进度条和处理状态。

### 清空图像
点击“清空”按钮，可以清除已选择的图像文件。

## 代码结构
- `select_files` 函数：用于处理通过浏览选择文件的操作。
- `drop` 函数：处理拖放文件的操作。
- `compress_images` 函数：进行图像压缩的主要逻辑。
- `load_image` 函数：加载图像并生成缩略图。
- `clear_images` 函数：清空已选择的图像。

## 运行代码
直接运行主文件即可启动图像压缩器应用。

## 图片

![image-20240627225629008](https://alist.ksmlc.cn/d/Private/OnedriveE5/Image/202406272256919.png)

![1](https://alist.ksmlc.cn/d/Private/OnedriveE5/Image/202407181411390.png)
