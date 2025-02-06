# coding:UTF-8
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import pandas as pd


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
    elif text.startswith('出木'):
        path = r'\\192.168.251.9\pe\制造本部工艺资料管理\五金、出木通用标准\老出木标准及出木通用标准\出木通用代码标准'
        filename = r'\\192.168.251.9\pe\制造本部工艺资料管理\五金、出木通用标准\老出木标准及出木通用标准\出木通用代码标准'
    elif text.startswith('材料'):
        path = r'\\192.168.251.9\研发材料信息库\材料评审资料\软体材料'
        filename = r'\\192.168.251.9\研发材料信息库\材料评审资料\软体材料'
    elif text.startswith('平台'):
        path = r'\\192.168.251.9\外贸价值链功能产品开发部\预研与平台架构模块\平台标准部分\平台模型'
        filename = r'\\192.168.251.9\外贸价值链功能产品开发部\预研与平台架构模块\平台标准部分\平台模型'
    elif text.startswith('资料'):
        path = r'\\192.168.251.9\外贸价值链功能产品开发部\功能开发模块\工艺组资料汇总（原档）新'
        filename = r'\\192.168.251.9\外贸价值链功能产品开发部\功能开发模块\工艺组资料汇总（原档）新'
    else:
        messagebox.showerror("错误", "暂无法识别")
        return

    full_path = os.path.join(path, filename)

    if os.path.exists(full_path):
        os.startfile(full_path)
    else:
        messagebox.showerror("错误", f"未找到文件")


# 新增功能函数（需要移到界面创建代码之前）
def search_csv():
    query = search_entry.get().strip()
    if not query:
        return
    
    try:
        csv_path = r"\\192.168.251.9\外贸价值链功能产品开发部\功能开发模块\结构工序\胡高高\11.csv"
        # 尝试不同编码方式（按优先级尝试）
        encodings = ['utf-8', 'gb18030', 'utf-16', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                df = pd.read_csv(csv_path, encoding=encoding)
                break
            except UnicodeDecodeError:
                continue
        else:
            raise ValueError("无法自动检测文件编码")
            
        # 在B列和C列中搜索
        mask = (df.iloc[:, 1].astype(str).str.contains(query)) | \
               (df.iloc[:, 2].astype(str).str.contains(query))
        results = df[mask].values.tolist()
        
        result_list.delete(0, tk.END)
        for row in results:
            result_list.insert(tk.END, f"{row[1]} {row[2]}")
            
    except Exception as e:
        messagebox.showerror("错误", f"查询失败：{str(e)}")

def copy_to_clipboard():
    selected = result_list.get(tk.ACTIVE)
    if selected:
        root.clipboard_clear()
        # 直接复制选中的完整内容，不再进行分割处理
        root.clipboard_append(selected.strip())
        root.update()


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
root.title("资料查询")

# 设置字体
my_font = font.Font(family="Microsoft YaHei", size=8)

# 设置主窗口背景色并强制更新
root.configure(bg="#F0EAD6")  # 更柔和的米色
root.update()  # 强制更新

# 获取顶层窗口引用
toplevel_window = root.winfo_toplevel()
toplevel_window.config(bg="#F0EAD6")

# 创建主框架
main_frame = tk.Frame(root, bg="#F0EAD6")
main_frame.pack(fill=tk.BOTH, expand=True)

# 第一行：输入框和打开按钮
frame = tk.Frame(main_frame, bg="#F0EAD6")
frame.grid(row=0, column=0, sticky="w", padx=7, pady=7)

def focus_next_entry(event):
    search_entry.focus_set()

# 第一行：输入框和打开按钮
entry = tk.Entry(frame, width=25, highlightbackground='#DCD0C0',
                 highlightcolor='#A9A9A9', highlightthickness=1, bd=0)
entry.pack(side=tk.LEFT, padx=(0, 5), pady=2)
entry.bind('<Return>', open_file)
entry.bind('<Down>', focus_next_entry)  # 绑定向下键

open_button = tk.Button(frame, text="打开", command=open_file, font=my_font,
                        bg="#f2c6b4", fg="#696969",
                        activebackground="#C0B090", activeforeground="#333333",
                        relief="flat", bd=0)
open_button.pack(side=tk.LEFT, pady=1)

# 第二行：搜索框和复制按钮
search_frame = tk.Frame(main_frame, bg="#F0EAD6")
search_frame.grid(row=1, column=0, sticky="w", padx=7, pady=(0,5))

def copy_first_result():
    if result_list.size() > 0:  # 检查是否有搜索结果
        result_list.selection_clear(0, tk.END)  # 清除当前选择
        result_list.selection_set(0)  # 选择第一个结果
        result_list.activate(0)  # 激活第一个结果
        copy_to_clipboard()  # 调用复制函数

search_entry = tk.Entry(search_frame, width=25, highlightbackground='#DCD0C0',
                       highlightcolor='#A9A9A9', highlightthickness=1, bd=0)
search_entry.pack(side=tk.LEFT, padx=(0, 5), pady=2)
search_entry.bind("<KeyRelease>", lambda e: root.after(500, search_csv))
search_entry.bind('<Up>', lambda e: entry.focus_set())  # 绑定向上键
search_entry.bind('<Return>', lambda e: copy_first_result())  # 绑定回车键

copy_btn = tk.Button(search_frame, text="复制", command=copy_to_clipboard, font=my_font,
                    bg="#f2c6b4", fg="#696969",
                    activebackground="#C0B090", activeforeground="#333333",
                    relief="flat", bd=0)
copy_btn.pack(side=tk.LEFT, pady=1)

# 结果显示列表框
result_list = tk.Listbox(main_frame, height=3, bg="white", relief="flat",
                        selectbackground="#f2c6b4", width=20)
result_list.grid(row=2, column=0, sticky="ew", padx=7, pady=(0,5))
# 添加双击事件绑定
result_list.bind("<Double-Button-1>", lambda e: copy_to_clipboard())

# 设置列表框宽度
result_list.config(width=20)
# 版本信息标签
version_label = tk.Label(main_frame, text="V2.0/9022564", foreground="#777777", cursor="hand2", font=my_font,
                         bg="#F0EAD6")
version_label.grid(row=3, column=0, sticky="sw", padx=10, pady=5)

# 分割线
separator = tk.Frame(main_frame, bg="#D3D3D3", height=1)
separator.grid(row=4, column=0, sticky="ew", pady=(2, 0))

# 配置网格布局权重
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# 将focus_set延迟到窗口加载完成后执行
root.after(100, entry.focus_set)

# 添加 Tooltip
Tooltip(version_label, "1-1.货号路径：KM类、GN、KG、DK\nDY(打样资料)\n1-2.常用路径：出木、材料、平台、资料\n2-1.两个输入框可以通过上下键切换，搜\n索框可以模糊搜索，搜索后按回车复制\n第一个结果，双击任意搜索结果也可以\n复制")

# 禁用窗口调整大小
root.resizable(False, False)

# 运行主循环
root.mainloop()
