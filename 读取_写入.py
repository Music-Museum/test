# coding:UTF-8
''''
import pandas as pd
data = pd.read_excel('1.xlsx', sheet_name='夹板')  # 可以将括号内文件相对路径（脚本所在路径）设置成绝对路径

import pandas as pd
data = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
data.to_excel(r'C:\Users\Administrator\Desktop\1.xlsx',index=False)  # 将DataFrame中的数据写入工作簿,忽略行标题
'''