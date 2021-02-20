import pandas as pd
import numpy as np
# ---------------test1-----------------#
# obj = pd.Series([1,2,3,4])
# # 0    1
# # 1    2
# # 2    3
# # 3    4
# print(obj)
# print(obj.values)#[1 2 3 4]
# print(obj.index)  #RangeIndex(start=0, stop=4, step=1)

# # a    1
# # b    2
# # c    3
# # d    4
# obj = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(obj)
# print(obj['a'])
# obj['a'] = 5
# print(obj)
# # 索引列表
# print(obj[['a','c']])
# # 根据布尔型数组进行过滤、标量乘法、应用数学函数等）都会保留索引值的链接
# print(obj[obj > 3])
# print(obj*2)
# print(np.exp(obj))

# # Series看成是一个定长的有序字典，因为它是索引值到数据值的一个映射
# print('b' in obj)

# 如果数据被存放在一个Python字典中，也可以直接通过这个字典来创建Series：
# sdata = {'class_id':3500,'name':'测试','star':1,'level':1}
# obj3 = pd.Series(sdata)
# print(obj3)

# 传入排好序的字典的键以改变顺序  不在key列表的将被移除 sdata中不存在的key将插入 置为NaN
# class_id    3500
# star           1
# tf           NaN
# name          测试
# keys =['class_id','star','tf','name']
# obj4=pd.Series(sdata,index=keys)
# print(obj4)

# 缺失（missing）或NA表示缺失数据。pandas的isnull和notnull函数可用于检测缺失数据
# class_id    False
# star        False
# tf           True
# name        False
# print(pd.isnull(obj4))
# class_id     True
# star         True
# tf          False
# name         True
# print(pd.notnull(obj4))

# Series也有类似的实例方法
# class_id    False
# star        False
# tf           True
# name        False
# print(obj4.isnull())

# Series最重要的一个功能是，它会根据运算的索引标签自动对齐数据 如果你使用过数据库，你可以认为是类似join的操作。
# a     6.0
# b     NaN
# c    11.0
# d    11.0
# f     NaN
# s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
# s2=pd.Series([5,6,7,8],index=['a','f','d','c'])
# print(s1+s2)
# Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切
# indexn
# a    1
# b    2
# c    3
# d    4
# Name: sname, dtype: int64
# s1.name='sname'
# s1.index.name='indexn'
# print(s1)


# ---------------test2-----------------#
# DataFrame是一个表格型的数据结构，它含有一组有序的列
data = {'class_id':[11001,11002,11003,11004,11005,11006],
        'star':[1,2,3,1,2,3],
        'name':['英雄1','英雄2','英雄3','英雄4','英雄5','英雄6']}
#    class_id  star name
# 0     11001     1  英雄1
# 1     11002     2  英雄2
# 2     11003     3  英雄3
# 3     11004     1  英雄4
# 4     11005     2  英雄5
# 5     11006     3  英雄6
# frame = pd.DataFrame(data)
# print(frame)
# head方法会选取前五行
# print(frame.head())

# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
#    star name  class_id
# 0     1  英雄1     11001
# 1     2  英雄2     11002
# 2     3  英雄3     11003
# 3     1  英雄4     11004
# 4     2  英雄5     11005
# 5     3  英雄6     11006
# print(pd.DataFrame(data,columns=['star','name','class_id']))

# 如果传入的列在数据中找不到，就会在结果中产生缺失值
#   star name  class_id quality
# a     1  英雄1     11001     NaN
# b     2  英雄2     11002     NaN
# c     3  英雄3     11003     NaN
# d     1  英雄4     11004     NaN
# e     2  英雄5     11005     NaN
# f     3  英雄6     11006     NaN
# print(pd.DataFrame(data,columns=['star','name','class_id','quality'],index=['a','b','c','d','e','f']))

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
# 0    英雄1
# 1    英雄2
# 2    英雄3
# 3    英雄4
# 4    英雄5
# 5    英雄6
# Name: name, dtype: object
# print(frame['name'])

# 行也可以通过位置或名称的方式进行获取，比如用loc属性（稍后将对此进行详细讲解）
# class_id    11002
# star            2
# name          英雄2
# Name: 1, dtype: object
# print(frame.loc[1])


# 为不存在的列赋值会创建出一个新列
# 不能用frame.quality创建新的列。
# 列可以通过赋值的方式进行修改。例如，我们可以给那个空的"quality"列赋上一个标量值或一组值
#    class_id  star name  quality
# 0     11001     1  英雄1        1
# 1     11002     2  英雄2        1
# 2     11003     3  英雄3        1
# 3     11004     1  英雄4        1
# 4     11005     2  英雄5        1
# 5     11006     3  英雄6        1
# frame['quality'] = 1
# print(frame)

# 如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值
#    class_id  star name  quality
# 0     11001     1  英雄1      NaN
# 1     11002     2  英雄2      1.0
# 2     11003     3  英雄3      2.0
# 3     11004     1  英雄4      3.0
# 4     11005     2  英雄5      NaN
# 5     11006     3  英雄6      NaN
# quality_data = pd.Series([1,2,3],index=[1,2,3])
# frame['quality'] = quality_data
# print(frame)

# del方法可以用来删除这列
# del frame['quality']
# print(frame)


# 常见的数据形式是嵌套字典
# 嵌套字典传给DataFrame，pandas就会被解释为：外层字典的键作为列，内层键则作为行索引
# pop = {'out_a':{2000:1,2002:3},'out_b':{2000:1.2,2002:3.5,2004:5}}
# pop_frame= pd.DataFrame(pop)
#       out_a  out_b
# 2000    1.0    1.2
# 2002    3.0    3.5
# 2004    NaN    5.0
# print(pop_frame)
# 使用类似NumPy数组的方法，对DataFrame进行转置（交换行和列）
#        2000  2002  2004
# out_a   1.0   3.0   NaN
# out_b   1.2   3.5   5.0
# print(pop_frame.T)


# 重新索引
# 用该Series的reindex将会根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值：
# obj = pd.Series([1,2,3,4],index=['d','b','c','a'])
# print(obj)
# obj2= obj.reindex(['a','b','c','d','e'])
# print(obj2)
# 重新索引时可能需要做一些插值处理。method选项即可达到此目的，例如，使用ffill可以实现前向值填充
# obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj3)
# print(obj3.reindex(range(6), method='ffill'))

# 借助DataFrame，reindex可以修改（行）索引和列。只传递一个序列时，会重新索引结果的行
# frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','d'],columns=['city','form','color'])
#    city  form  color
# a     0     1      2
# b     3     4      5
# d     6     7      8
# print(frame)
# frame2 = frame.reindex(['a','b','c','d'])
#    city  form  color
# a   0.0   1.0    2.0
# b   3.0   4.0    5.0
# c   NaN   NaN    NaN
# d   6.0   7.0    8.0
# print(frame2)
# column_data=['city','fo','color']
# frame3 = frame.reindex(columns=column_data)
#    city  fo  color
# a     0 NaN      2
# b     3 NaN      5
# d     6 NaN      8
# print(frame3)


# 丢弃指定轴上的项
# drop方法返回的是一个在指定轴上删除了指定值的新对象
# obj = pd.Series(np.arange(5),index=['a','b','c','d','e'])
# print(obj.drop('a'))
# print(obj) #不改变还是5个数据

# inplace=True可以就地修改对象，不会返回新的对象  小心使用inplace，它会销毁所有被删除的数据。
# obj.drop('a',inplace=True) 
# print(obj)

# print(obj.drop(['b','d']))

# DataFrame，可以删除任意轴上的索引值
data = pd.DataFrame(np.arange(16).reshape(4,4),index=['ohio','colorado','utah','new york'],columns=['one','two','three','four'])

# 用标签序列调用drop会从行标签（axis 0）删除值
# print(data.drop(['colorado','utah']))

# 通过传递axis=1或axis='columns'可以删除列的值
# print(data.drop('two',axis=1))
# print(data.drop(['two','three'],axis='columns'))


# data.drop(['two'],axis='columns',inplace=True)
# print(data)


# 用loc和iloc进行选取
# 使用轴标签（loc）或整数索引（iloc），从DataFrame选择行和列的子集
# frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','d'],columns=['city','form','color'])
# print(frame.loc[['a'],['city','form']])
# print(frame.loc['a','city'])

# 用iloc和整数进行选取
# print(frame.iloc[[1],[2,1]])

# 两个索引函数也适用于一个标签或多个标签的切片
# print(frame.loc[:'b','form'])
# print(frame.iloc[:,:2][frame.city>3])


# 在算术方法中填充值
# df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
# df2 = pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
# print(df1)
# print(df2)
# df2.loc[1,'b'] = np.nan
# print(df2)

# 没有重叠的位置就会产生NA值
# print('df1+df2=\n',df1+df2)
# 使用df1的add方法，传入df2以及一个fill_value参数
# print(df1.add(df2,fill_value=0))

# 以字母r开头，它会翻转参数
# print(1/df1) #等价于  df1.rdiv(1)
# print(df1.rdiv(1))

# DataFrame和Series之间的运算
# 默认情况下，DataFrame和Series之间的算术运算会将Series的索引匹配到DataFrame的列，然后沿着行一直向下广播


