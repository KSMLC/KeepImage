import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tinify
from PIL import Image, ImageTk
import os

# 设置 Tinify API 密钥
tinify.key = ""

def select_files():
    file_paths = filedialog.askopenfilenames(
        filetypes=[("图像文件", "*.jpg *.jpeg *.png *.webp")])
    if file_paths:
        input_path_var.set(", ".join(file_paths))
        for file_path in file_paths:
            load_image(file_path)

def drop(event):
    file_paths = event.data.split()
    if file_paths:
        cleaned_paths = [path.strip('{}') for path in file_paths]
        input_path_var.set(", ".join(cleaned_paths))
        for file_path in cleaned_paths:
            load_image(file_path)


def compress_images():
    input_paths = input_path_var.get().split(", ")
    if not input_paths:
        messagebox.showwarning("警告", "请先选择要压缩的图像文件.")
        return

    output_folder = filedialog.askdirectory()
    if not output_folder:
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    progress_bar["value"] = 0
    total_images = len(input_paths)
    for index, input_path in enumerate(input_paths, start=1):
        processing_label.config(text=f"正在处理第 {index}/{total_images} 张图片...")
        root.update()  # 更新 GUI

        try:
            filename = os.path.basename(input_path)
            output_path = os.path.join(output_folder, filename)
            source = tinify.from_file(input_path)
            source.to_file(output_path)
            progress_bar["value"] = (index / total_images) * 100
        except tinify.Error as e:
            messagebox.showerror("错误", f"{filename} 图像压缩失败: {str(e)}")
            return

    messagebox.showinfo("成功", "所有图像压缩完成")
    processing_label.config(text="所有图像压缩完成")

def load_image(file_path):
    img = Image.open(file_path)
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

def clear_images():
    input_path_var.set("")
    img_label.config(image="")

# 创建主窗口
root = TkinterDnD.Tk()
root.title("图像压缩器")

# 创建并放置控件
input_path_var = tk.StringVar()

frame = tk.Frame(root)
frame.pack(pady=20)

input_label = tk.Label(frame, text="选择要压缩的图像:")
input_label.grid(row=0, column=0, padx=10, pady=5)

input_entry = tk.Entry(frame, textvariable=input_path_var, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)

browse_button = tk.Button(frame, text="浏览", command=select_files)
browse_button.grid(row=0, column=2, padx=10, pady=5)

clear_button = tk.Button(frame, text="清空", command=clear_images)
clear_button.grid(row=0, column=3, padx=10, pady=5)

compress_button = tk.Button(root, text="压缩图像", command=compress_images)
compress_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, mode="determinate")
progress_bar.pack(pady=10)

processing_label = tk.Label(root, text="", fg="red")
processing_label.pack(pady=5)

img_label = tk.Label(root)
img_label.pack(pady=10)

# 添加拖放功能
root.drop_target_register(DND_FILES)
root.dnd_bind("<<Drop>>", drop)

# 运行主循环
root.mainloop()
