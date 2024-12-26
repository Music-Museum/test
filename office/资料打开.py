# coding:UTF-8
import os
import tkinter as tk
from tkinter import messagebox

def sanitize_input(text):
    """清理输入内容"""
    return text.replace("80.", "").replace(" ", "").replace("\n", "")

def open_file(event=None):
    text = sanitize_input(entry.get().upper())  # 清理输入并转换为大写
    
    if text.startswith('H'):
        path = r'G:\hu'
        filename = text[1:]
    elif text.startswith('DY'):
        path = r'\\192.168.251.9\外贸价值链功能产品开发部\项目管理模块\功能研发项目资料\2022~2024年立项及开发资料'
        filename = text[2:]
    elif text.startswith('KM'):
        path = r'\\192.168.251.9\pe\制造本部工艺资料管理\外贸工艺资料\KM类'
        filename = text
    elif text.startswith('GN'):
        path = r'\\192.168.251.9\pe\制造本部工艺资料管理\内销工艺资料\GN--（功能）'
        filename = text
    elif text.startswith('KG'):
        path = r'\\192.168.251.9\pe\制造本部工艺资料管理\内销工艺资料\KG--（内销功能）'
        filename = text
    elif text.startswith('DK'):
        path = r'\\192.168.251.9\pe\制造本部工艺资料管理\内销工艺资料\DK--类（电商）'
        filename = text
    else:
        messagebox.showerror("错误", "暂无法识别")
        return

    full_path = os.path.join(path, filename)
    
    if os.path.exists(full_path):
        os.startfile(full_path)
    else:
        messagebox.showerror("错误", f"未找到文件")

# 创建主窗口
root = tk.Tk()
root.title("资料打开")

'''# 设置窗口大小（保持原来的尺寸）
window_width = max(300, root.winfo_reqwidth())
window_height = root.winfo_reqheight() + 20
root.geometry(f"{window_width}x{window_height}")'''

# 创建框架来容纳输入框和按钮
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# 创建框架来容纳输入框和按钮，并稍微向下移动
frame = tk.Frame(root)
frame.pack(padx=7, pady=5)  # 调整 `pady` 增加顶部和底部间距

# 创建和放置控件
entry = tk.Entry(frame, width=23)  # 增加输入框宽度
entry.pack(side=tk.LEFT, padx=(0, 5))
entry.bind('<Return>', open_file)

open_button = tk.Button(frame, text="打开", command=open_file)
open_button.pack(side=tk.LEFT)

# 添加版本信息
version_label = tk.Label(root, text="V1.2/9022564", foreground="gray")
version_label.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=5)

# 禁止调整窗口大小
root.resizable(False, False)

# 运行主循环
root.mainloop()
