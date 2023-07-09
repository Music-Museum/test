# coding:UTF-8

import pandas as pd

data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
a = data['c1']  # 一维数据，不包含列索引
b = data[['c1']]  # 二维数据，包含列索引，可以继续添加参数，增加列
c = data[1:3]  # 选取第一行到第二行的数据，但是容易混淆报错，官方推荐用iloc方法选取数据
d = data.iloc[1:3]
e = data.iloc[-1:]  # 选取单行必须使用iloc，倒数第一行[书中没有冒号，有错误]
f = data.loc[['r2', 'r3']]  # 根据行名称选择,注意两层方括号
g = data.head(2)  # 选取前两行数据
h = data.iloc[0:2][['c1', 'c3']]  # 整合，先选取行，再选取列，字符串有点乱，loc使用字符串作为索引，iloc使用数字作为索引
i = data.iloc[0:2, [0, 2]]  # 注意方括号的使用，逗号和分号的使用
j = data[(data['c1'] > 1) & (data['c2'] == 5)]  # 两个条件的时候条件要用括号包起来。
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
