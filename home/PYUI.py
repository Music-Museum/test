# tkinter简单示例源码
import tkinter as tk
# 调用Tk()创建主窗口
root_window =tk.Tk()
# 设置窗口大小和位置：窗口的宽与高，窗口距离屏幕的左边距和上边距
root_window.geometry('300x300+300+200')
# 给窗口起一个名字，也就是窗口的名字
root_window.title("胡高高，加油！")
# 开启主循环，让窗口处于显示状态
root_window.mainloop()
