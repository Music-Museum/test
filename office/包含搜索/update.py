import win32com.client as win32
import pythoncom
import time

# 初始化 COM
pythoncom.CoInitialize()

try:
    # 创建 Excel 应用程序对象
    xlApp = win32.Dispatch("Excel.Application")

    # 设为后台运行（不弹出 Excel 界面）
    xlApp.Visible = False
    xlApp.DisplayAlerts = False  # 关闭所有弹窗
    xlApp.AskToUpdateLinks = False  # 自动跳过“是否更新链接”提示
    xlApp.AlertBeforeOverwriting = False  # 禁用覆盖文件时的提示

    # 打开 Excel 文件（路径前加 r 以防止转义字符问题）
    file_path = r"E:\物料\BOM物料参考\BOM模板\KM. EBOM-结构.xlsm"
    xlWorkbook = xlApp.Workbooks.Open(file_path, UpdateLinks=0)  # 0 = 不更新链接

    # 运行 VBA 宏
    xlApp.Run("gengxingwaimao")  # 替换为你的宏名

    # 等待 Excel 处理宏（可选）
    time.sleep(8)  # 可根据宏的运行时间调整

    # 保存工作簿并关闭
    xlWorkbook.Save()  # 确保更改被保存
    xlWorkbook.Close(SaveChanges=True)

    # 退出 Excel
    xlApp.Quit()

    print("更新完成")

except Exception as e:
    print(f"发生错误: {e}")

finally:
    # 释放 Excel 进程
    xlApp = None
    pythoncom.CoUninitialize()
