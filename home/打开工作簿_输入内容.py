# coding:UTF-8

import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open(r'C:\Users\Administrator\Desktop\1.xlsx')
worksheet=workbook.sheets['sheet1']  # 选中sheet1
worksheet.range('A1').value='KM.6261'  # A1中输入
'''
worksheet = workbook.sheets.add('夹板')  新增工作表
'''
