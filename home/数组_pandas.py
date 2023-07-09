# coding:UTF-8

'''  创建数组,数组可以直接计算，列表不可以，列表乘以2等于复制一遍，列表嵌套后打印还是一行，数组嵌套数组后打印是一列
import numpy as np

b = np.array([1, 2, 3, 4])
print(b*2)

import pandas as pd

a = pd.Series(['A', 'B', 'C'])
b = pd.DataFrame([[1, 2], [3, 4], [5, 6]])  # 还可以指定行index和列columns索引名称
print(a)
print(b)

C = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['x', 'y', 'z'])  # 默认键名为列名，也可以指定为行名
print(C)
'''
import numpy as np
import pandas as pd

a=np.arange(12).reshape(3, 4) # 创建二维数组，横3竖4
b=pd.DataFrame(a,index=[1, 2, 3], columns=['x', 'y', 'z', 'x'])  # 指定数组索引
print(b)
