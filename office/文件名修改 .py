import os
import tkinter as tk
from tkinter import filedialog, messagebox

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
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def select_directory():
    directory = filedialog.askdirectory(title="选择要处理的目录")
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def modify_file_names():
    directory = directory_entry.get()
    if not directory:
        messagebox.showerror("错误", "请输入或选择要处理的目录")
        return

    prefix = prefix_entry.get()
    suffix = suffix_entry.get()
    old_string = old_entry.get()
    new_string = new_entry.get()

    if not any([prefix, suffix, old_string, new_string]):
        messagebox.showerror("错误", "请至少输入一项修改内容")
        return

    if not os.path.exists(directory):
        messagebox.showerror("错误", "指定的目录不存在")
        return

    modified_count = 0
    for filename in os.listdir(directory):
        new_filename = filename

        if old_string and new_string:
            new_filename = new_filename.replace(old_string, new_string)

        if prefix:
            new_filename = prefix + new_filename

        if suffix:
            name, ext = os.path.splitext(new_filename)
            new_filename = name + suffix + ext

        if new_filename != filename:
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)

            if not os.path.exists(new_filepath):
                os.rename(old_filepath, new_filepath)
                modified_count += 1

    messagebox.showinfo("操作完成", f"修改操作已完成。共修改了 {modified_count} 个文件名。")

# 创建主窗口
root = tk.Tk()
root.title("文件名修改器")
root.geometry("450x250")  # 减小窗口大小

# 创建和放置控件
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="目录路径:").grid(row=0, column=0, sticky="e")
directory_entry = tk.Entry(frame, width=40)
directory_entry.grid(row=0, column=1, padx=5)
select_button = tk.Button(frame, text="浏览", command=select_directory)
select_button.grid(row=0, column=2)

tk.Label(frame, text="添加前缀:").grid(row=1, column=0, sticky="e")
prefix_entry = tk.Entry(frame, width=40)
prefix_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="添加后缀:").grid(row=2, column=0, sticky="e")
suffix_entry = tk.Entry(frame, width=40)
suffix_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="被替换的文字:").grid(row=3, column=0, sticky="e")
old_entry = tk.Entry(frame, width=40)
old_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="替换后的文字:").grid(row=4, column=0, sticky="e")
new_entry = tk.Entry(frame, width=40)
new_entry.grid(row=4, column=1, padx=5, pady=5)

modify_button = tk.Button(root, text="开始修改", command=modify_file_names)
modify_button.pack(pady=10)

# 添加版本信息
version_label = tk.Label(root, text="v1.3/9022564", fg="gray")
version_label.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=5)

# 绑定回车键到修改按钮
root.bind('<Return>', lambda event: modify_file_names())

# 运行主循环
root.mainloop()
