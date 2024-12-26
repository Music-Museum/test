# coding:UTF-8
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import font

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

# 添加Tooltip类
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tooltip = tk.Toplevel()
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, justify='left',
                      background="white", relief='solid', borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# 创建主窗口
root = tk.Tk()
root.title("资料打开")

# 设置主窗口背景色并强制更新
root.configure(bg="#F5F5DC")
root.update() # 强制更新

# 获取顶层窗口引用
toplevel_window = root.winfo_toplevel()
toplevel_window.config(bg="#F5F5DC")


# 创建框架
frame = tk.Frame(root, bg="#F5F5DC")
frame.pack(padx=7, pady=7)

# 创建输入框
entry = tk.Entry(frame, width=15, highlightbackground='#DDDDDD',
                 highlightcolor='#888888', highlightthickness=1, bd=0)
entry.pack(side=tk.LEFT, padx=(0, 5))
entry.bind('<Return>', open_file)

# 将focus_set延迟到窗口加载完成后执行
root.after(100, entry.focus_set)

# 设置字体
my_font = font.Font(family="Microsoft YaHei", size=13)

# 创建按钮
open_button = tk.Button(frame, text="打开", command=open_file, font=my_font,
                         bg="#FFB347", fg="#333333", # 浅橙色背景, 深灰色文字
                         activebackground="#E6A23C", activeforeground="#333333", # 深浅橙色激活背景, 深灰色文字
                         relief="flat",
                         bd=0)
open_button.pack(side=tk.LEFT)

# 版本信息标签
version_label = tk.Label(root, text="V1.3/9022564", foreground="#777777", cursor="hand2", font=my_font,
                         bg="#F5F5DC")
version_label.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=5)

# 分割线
separator = tk.Frame(root, bg="#D3D3D3", height=1)
separator.pack(side=tk.BOTTOM, fill=tk.X, pady=(2, 0))


# 添加 Tooltip
Tooltip(version_label, "支持KM类、GN、KG、DK\nDY(打样资料)")

# 禁用窗口调整大小
root.resizable(False, False)

# 运行主循环
root.mainloop()
