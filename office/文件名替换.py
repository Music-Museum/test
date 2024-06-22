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

    for filename in os.listdir(directory):
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, filename.replace(old_string, new_string))

        if old_filepath != new_filepath and not os.path.exists(new_filepath):
            os.rename(old_filepath, new_filepath)
            result_text.insert(tk.END, f"文件名 '{filename}' 已更改为 '{os.path.basename(new_filepath)}'\n")

    result_text.insert(tk.END, "\n替换操作已完成.\n")

# 创建主窗口
root = tk.Tk()
root.title("文件名替换")
root.geometry("450x400")  # 增加窗口大小

# 创建和放置控件
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="目录路径:").grid(row=0, column=0, sticky="e")
directory_entry = tk.Entry(frame, width=40)
directory_entry.grid(row=0, column=1, padx=5)
select_button = tk.Button(frame, text="浏览", command=select_directory)
select_button.grid(row=0, column=2)

tk.Label(frame, text="被替换的文字:").grid(row=1, column=0, sticky="e")
old_entry = tk.Entry(frame, width=40)
old_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="替换后的文字:").grid(row=2, column=0, sticky="e")
new_entry = tk.Entry(frame, width=40)
new_entry.grid(row=2, column=1, padx=5, pady=5)

replace_button = tk.Button(root, text="开始替换", command=replace_file_names)
replace_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=55)  # 增加文本框大小
result_text.pack(pady=10)

# 添加版本信息
version_label = tk.Label(root, text="v1.1/9022564", fg="gray")
version_label.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=5)



# 绑定回车键到替换按钮
root.bind('<Return>', lambda event: replace_file_names())

# 运行主循环
root.mainloop()
