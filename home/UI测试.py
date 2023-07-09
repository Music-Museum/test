# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import *

root_window = tk.Tk()
root_window.title('资料查看')
root_window.geometry('300x100')

# 设置完窗口后，添加组件
tk.Label(root_window, text='').pack()

cms = StringVar()
tk.Entry(root_window, width=12, textvariable=cms).pack()
'''
tk.Label(root_window, text="cm").pack()
tk.Label(root_window, text="你的身高是").pack()

result = StringVar()
tk.Label(root_window, textvariable=result).pack()

tk.Label(root_window, text="cm").pack()
'''

def calculate(*args):
    try:
        value = float(cms.get())
        result.set(value)
    except ValueError:
        pass


B = tk.Button(root_window, text="open", command=calculate)
B.pack()

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
