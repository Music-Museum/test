# coding:UTF-8

import os
import shutil
from win32com.client import Dispatch
import xlwings as xw

product_name = input()
folder_path = r'C:\Users\Administrator\Desktop\hu'
full_path = folder_path+'\\'+product_name
modle_path = full_path+'\\'+product_name
if os.path.exists(full_path):  # 检查是否已存在
    print('重复')
elif product_name[0].islower():  # 检查首字母大小写
    print('大写')
else:
    os.mkdir(full_path)
    os.mkdir(modle_path)

product_doc_path = r'C:\Users\Administrator\Desktop\打样单'+'\\'+product_name
product_doc_list = os.listdir(product_doc_path)
for i in product_doc_list:
    detail_path = product_doc_path+'\\'+i
    shutil.copytree(detail_path, full_path, dirs_exist_ok=True)  # 第三个参数是不删除目标文件夹的内容

template_path = r'C:\Users\Administrator\Desktop\KM. BOM.xlsm'
shutil.copy(template_path, full_path)

old_bom_name = full_path+'\\'+'KM. BOM.xlsm'
new_bom_name = full_path+'\\'+product_name+' BOM.xlsm'
os.renames(old_bom_name, new_bom_name)

shortcut_path = r'C:\Users\Administrator\Desktop'+'\\'+product_name+'.lnk'  # 路径
shortcut_folder = full_path  # 目标文件夹

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = shortcut_folder
shortcut.save()

app = xw.App(visible=True, add_book=False)
workbook = app.books.open(new_bom_name)
worksheet = workbook.sheets['总表']
worksheet.range('H2').value = product_name
workbook.save()
workbook.close()
app.quit()
