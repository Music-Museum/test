# coding:UTF-8

import xlwings as xw  # 导入并简写

app = xw.App(visible=True, add_book=False)  # 启动程序，第一个参数设置程序窗口可见性，第二个参数设置是否新建工作簿
workbook = app.books.add()  # 新建工作簿
workbook.save(r'C:\Users\Administrator\Desktop\1.xlsx')
workbook.close()  # 关闭工作簿
app.quit()  # 退出excel程序
