import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

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

def replace_file_names():
    directory = directory_entry.get()
    if not directory:
        messagebox.showerror("错误", "请输入或选择要处理的目录")
        return

    old_string = old_entry.get()
    new_string = new_entry.get()

    if not old_string or not new_string:
        messagebox.showerror("错误", "请输入被替换的文字和替换后的文字")
        return

    if not os.path.exists(directory):
        messagebox.showerror("错误", "指定的目录不存在")
        return

    result_text.delete(1.0, tk.END)  # 清空结果文本框
    found_match = False

    for filename in os.listdir(directory):
        old_filepath = os.path.join(directory, filename)
        new_filename = filename.replace(old_string, new_string)
        new_filepath = os.path.join(directory, new_filename)

        if old_filepath != new_filepath:
            found_match = True
            if not os.path.exists(new_filepath):
                os.rename(old_filepath, new_filepath)
                result_text.insert(tk.END, f"文件名 '{filename}' 已更改为 '{new_filename}'\n")
            else:
                result_text.insert(tk.END, f"无法重命名 '{filename}'，因为 '{new_filename}' 已存在\n")

    if not found_match:
        result_text.insert(tk.END, "未找到被替换文字，没有文件被重命名。\n")
    else:
        result_text.insert(tk.END, "\n替换操作已完成。\n")

# 创建主窗口
root = tk.Tk()
root.title("文件名替换")
root.geometry("500x450")  # 增加窗口大小

# 创建主框架
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 创建和放置控件
ttk.Label(main_frame, text="目录路径:").grid(row=0, column=0, sticky=tk.E, pady=5)
directory_entry = ttk.Entry(main_frame, width=50)
directory_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
select_button = ttk.Button(main_frame, text="浏览", command=select_directory)
select_button.grid(row=0, column=2, pady=5)

ttk.Label(main_frame, text="被替换的文字:").grid(row=1, column=0, sticky=tk.E, pady=5)
old_entry = ttk.Entry(main_frame, width=50)
old_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

ttk.Label(main_frame, text="替换后的文字:").grid(row=2, column=0, sticky=tk.E, pady=5)
new_entry = ttk.Entry(main_frame, width=50)
new_entry.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

replace_button = ttk.Button(main_frame, text="开始替换", command=replace_file_names)
replace_button.grid(row=3, column=1, pady=10)

result_text = tk.Text(main_frame, height=10, width=60)
result_text.grid(row=4, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

# 设置列的权重，使其能够自适应调整
main_frame.columnconfigure(1, weight=1)

# 添加版本信息
version_label = ttk.Label(root, text="v1.1/9022564", foreground="gray")
version_label.grid(row=1, column=0, sticky=(tk.S, tk.W), padx=10, pady=5)

# 运行主循环
root.mainloop()
