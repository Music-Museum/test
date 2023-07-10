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
k = data.sort_values(by='c2',ascending=False)  # 按C2列排序，ascending，上升，默认True
l = data.sort_index(ascending=True)  # 行索引排序
m = data.drop(columns=['c1', 'c3'])  # 删除c1 c3列，默认不改变原数据，要改变需要增加参数inplace
n = data.drop(index=['r1', 'r3'])
o = pd.merge(m, n, how='outer')  # 数据表拼接，默认交集，设置how，可以并集，mn分左右，可以设计how参数为left，注意加单引号
#  也可以按行索引合并，还可以使用concat，和append
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
print(k)
print(l)
print(m)
print(n)
print(o)