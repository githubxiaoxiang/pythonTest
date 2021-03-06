#!/usr/bin/python3
from enum import Enum
import urllib.request
import urllib.parse
import string
import sys
import os
import numpy
import datetime
import bisect
from collections import defaultdict
import collections.abc
from functools import reduce
import functools
# print(sys.argv)
# str='this is test str'
# print(str)
# print(str[0:3])
# print(str[0:-1])
# print("Hello, World!")
# print( "this is a line with \n" );
# print("Hello")
# s = r'this\has\no\special\characters'
# print(s);
# dt  =  datetime.datetime(2020,12,4,8,50);
# print(dt.strftime('%m/%d/%y %H:%M'));
# print(dt.date());
# print(dt.day);
# print(dt.month);
# print( range(10));
# a,b = 1,2;
# b,a = a,b;
# print(a,b);
# tup = 1,2,(4,5);
# tup2=(9,8,8)+(111,2);
# print(tup);
# print(tup2);
# lista =[1,2,3];
# listb = [4,5,6];
# # lista.append(listb);
# lista.extend(listb);
# print(lista);

# arr = [1,2,5,8,10]
# print(bisect.bisect(arr,6));
# bisect.insort(arr,9);
# print(arr);

# arr2 = [7, 2, 3, 6, 3, 5, 6, 0, 1];
# print(arr2[::2]);
# print(arr2[::-1]);

# some_list = ["aaa","bbb","ccc"];
# mapping = {};
# for i,v in enumerate(some_list):
#     mapping[v] =i;

# print(mapping);

# zip可以处理任意多的序列，元素的个数取决于最短的序列
# seq1 = ['foo', 'bar', 'baz'];
# seq2= ['one', 'two', 'three'];
# seq3=["true","false"]
# ziped = zip(seq1,seq2,seq3);
# # print(list(ziped));
# for i,(a,b,c) in enumerate(ziped):
#  print('{0}:{1},{2},{3}'.format(i,a,b,c));

# # reversed可以从后向前迭代一个序列： 只有实体化（即列表或for循环）之后才能创建翻转的序列。
# print(list(reversed(range(10))))

# 用序列创建字典
# {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
# mapping = dict(zip(range(5),reversed(range(5))));
# print(mapping);

# # [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
# mapping2 = list(zip(range(5),reversed(range(5))));
# print(mapping2);


words = ['apple', 'bat', 'bar', 'atom', 'book']
# by_letter={}
# for word in words:
#     letter = word[0];
#     if letter not in by_letter:
#         by_letter[letter] = [word];
#     else:
#         by_letter[letter].append(word);

# for word in words:
#     letter = word[0];
#    by_letter.setdefault(letter, []).append(word)
# by_letter = defaultdict(list);
# for word in words:
#     by_letter[word[0]].append(word);

# print(by_letter);

# 集合是无序的不可重复的元素的集合。你可以把它当做字典，但是只有键没有值
# a={1,2,3,4,5};
# b={1,3,5};
# print(a.union(b));#{1, 2, 3, 4, 5}
# print(a|b);#{1, 2, 3, 4, 5}
# print(a.intersection(b));#{1, 3, 5}
# print(a&b);#{1, 3, 5}
# print({1,2,3}.issubset(a));#True
# print(a.issuperset({1,2,3}));#True
# print({1, 2, 3} == {3, 2, 1})#True
# 与字典类似，集合元素通常都是不可变的。要获得类似列表的元素，必须转换成元组
# a_data=[1,2,3,4];
# a_dic = {tuple(a_data)};
# b_dic = {(1,2,4)};
# print(a_dic);#{(1, 2, 3, 4)}
# print(a_dic.union(b_dic));#{(1, 2, 3, 4), (1, 2, 4)}

# c1 = {1,2,3};
# c2 ={1,4,5};
# c =  c1.copy();
# c|=c2;
# print(c);#{1, 2, 3, 4, 5}
# d=c1.copy();
# d&=c2;
# print(d);#{1}
#--------------------------------------列表、集合和字典推导式start--------------------------------#
# 列表、集合和字典推导式
# 列表推导式是Python最受喜爱的特性之一。它允许用户方便的从一个集合过滤元素，形成列表，在传递参数的过程中还可以修改元素。形式如下
#[expr for val in collection if condition]
# 等同于下面的for循环
# result = []
# for val in collection:
#     if condition:
#         result.append(expr)

# str = ['a', 'as', 'bat', 'car', 'dove', 'python']
# data = [x.upper() for x in str if len(x)>2]
# print(data);

# 字典的推导式
# dict_comp = {key-expr : value-expr for value in collection if condition}
# 集合的推导式与列表很像，只不过用的是尖括号
# set_comp = {expr for value in collection if condition}

# unique_lengths = {len(x) for x in str};
# print(unique_lengths);#{1, 2, 3, 4, 6}
# # map函数可以进一步简化
# print(set(map(len,str)));#{1, 2, 3, 4, 6}
# print(list(map(len,str)));#[1, 2, 3, 3, 4, 6]

# dic_data = {value:index for index,value in enumerate(str)};
# print(dic_data);#{'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}

# 嵌套列表推导式
# some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# flattened  =[x for tup in some_tuples for x in tup];
# result = [[x for x in tup]for tup in some_tuples];
# print(flattened);#[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(result);#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#--------------------------------------列表、集合和字典推导式end--------------------------------#

# 切片
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略 L[:3]
#L[1:3] 从索引1开始，取出2个元素
# L[-1]取倒数第一个元素  倒数第一个元素的索引是-1
# L[-2:] 取倒数两个数
# L[:10:2]  前10个数，每两个取一个
# L[::5]  所有数，每5个取一个
# L[:]   复制一个list
# L[start: stop: step],分别为起始下标，终止下标，步长(默认为1)
# step正负只决定切片方向，正为从左往右，负为从右往左
# start/stop值为负代表从左往右倒数几个元素  L[3:-3] 从左3到右3区间
# 切片始终以start为开始，stop结束，确保切片[start: stop]区间有值，否则为空表



# 给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 迭代是通过for ... in来完成
# dict = {'a': 1, 'b': 2, 'c': 3}
# for key in dict:
#     print(key)
# for value in dict.values():
#     print(value)
# for k,v in dict.items():
#     print(k,v)

# 字符串也是可迭代对象
# for char in 'ABC':
#     print(char)
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
# bol =isinstance('abcsss', collections.abc.Iterable)
# print(bol)
# print(isinstance(['a','b','c'],collections.abc.Iterable))
# print(isinstance(123,collections.abc.Iterable))

# 对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
# for k,v in enumerate(['a','b','c']):
#     print(k,v)

# for x,y in [(1,1),(2,4),(3,9)]:
#     print(x,y)

# def findMinAndMax(L):
#     min=0
#     max=0
#     for k,v in enumerate(L):
#         if min>v or min==0:
#             min =v
#         if max<v or max==0:
#             max=v
#     return (min,max)

# print(findMinAndMax([1,2,3,4]))


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
# print(list(range(1,11)))

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
# L=[]
# for v in range(1,11):
#     L.append(v*v)
# print(L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# print([x*x for x in range(1,11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
# print([x*x for x in range(1,11) if x%2==0])

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
# print([x if x%2==0 else -x for x in range(1,11)])

# 还可以使用两层循环，可以生成全排列：
# print([m+n for m in 'ABC' for n in 'xyz'])

# 列出当前目录下的所有文件和目录名
# print([d for d in os.listdir('.')])

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 只要把一个列表生成式的[]改成()，就创建了一个generator
# g = (x * x for x in range(10))
# 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
# print(next(g))
# 这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
# for key in g:
#     print(key)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加
# def fab(max):
#     n,a,b =0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# print(fab(3))

# fib函数变成generator，只需要把print(b)改为yield b就可以
# def fab(max):
#     n,a,b =0,0,1
#     while n<max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# f = fab(3)
# print(next(f))

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128#0
# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 方法1：
# def triangles():
#     a=[1]
#     n=0
#     while n<5:
#         yield a
#         # 补0
#         b = a[:]+[0]
#         a=[b[i]+b[i-1] for i in range(len(b))]
#         n=n+1
# g = triangles()
# for key in g:
#     print(key)
# 方法2：
# [0]+result:0 1 4 6 4 1
# result+[0]:1 4 6 4 1 0  两列对应相加 移位相加
# def triangles2():
#     result = [1]
#     temp = [1]
#     n=0
#     while n<5:
#         yield result
#         result = [sum(i) for i in zip([0]+result, result+[0])]
#         n =n+1
# g2 = triangles2()
# for key in g2:
#     print(key)

# 方法3：
# def triangles3():
#     n=1
#     while n<5:
#         b=[]
#         [b.append(1) if index==0 or index ==(n-1) else b.append(a[index-1]+a[index]) for index in range(n)]
#         yield b
#         n+=1
#         a=b
# g3 = triangles3()
# for key in g3:
#     print(key)

# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，
# 但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# print(isinstance((x for x in range(10)),collections.abc.Iterable))
# print(isinstance((x for x in range(10)),collections.abc.Iterator))
# print(isinstance(iter([]),collections.abc.Iterator))

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 通过list()函数让它把整个序列都计算出来并返回一个list
# def f(x):
#     return x*x
# r= map(f,[1,2,3,4,5])
# print(list(r))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2Int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2Num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2Num,s))
# print(str2Int('12345')+2)

# lambda函数进一步简化
# def char2Num(s):
#     return DIGITS[s]
# def str2Int(s):
#     return reduce(lambda x,y:x*10+y,map(char2Num,s))
# print(str2Int('12345'))

# def prod(l):
#     return reduce(lambda x,y:x*y,l)
# print(prod([1,2,3,4,5]))

# def str2float(s):
#     a,b = s.split('.')
#     x1=reduce(lambda x,y:x*10+y,map(int,a))
#     y1=reduce(lambda x,y:x*0.1+y,map(int,b[::-1]))
#     y1=y1/10
#     return x1+y1
# print(str2float('123.456'))

# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
# 在一个list中，删掉偶数，只保留奇数
# def fn(n):
#     return n%2==1
# print(list(filter(fn,[1,2,3,4,5])))

# 一个序列中的空字符串删掉
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty,['A','',None,'abc','ad'])))

#-----------------------------------------------------------filter求素数start-----------------------------------------------------------#
# 用filter求素数
# 计算素数的一个方法是埃氏筛法
# 首先，列出从2开始的所有自然数，构造一个序列2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉

# 先构造一个从3开始的奇数序列(已排除2的倍数)  注意这是一个生成器，并且是一个无限序列。
# def _odd_iter():
#     n =1
#     while True:
#         n=n+2
#         yield n
# 定义一个筛选函数
# def _not_divisible(n):
#     return lambda x:x%n>0

# 定义一个生成器，不断返回下一个素数  这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it) #返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n),it)  #构造新序列

#  primes()也是一个无限序列 调用时需要设置一个退出循环的条件
# for n in primes():
#     if(n<1000):
#         print(n)
#     else:
#         break
#-----------------------------------------------------------filter求素数end-----------------------------------------------------------#

#-----------------------------------------------------------filter获取回数start-----------------------------------------------------------#
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 方法1：
# def is_palindrome(n):
#     return str(n)[::]==str(n)[::-1]

# 方法2
# def is_palindrome(n):
#     return n== int(str(n)[::-1])

# 方法3 整数倒序
# def is_palindrome(n):
#     s=n
#     y=0
#     while s!=0:
#         y=y*10+s%10
#         s =s//10
#     return y==n

# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:',list(output))
#-----------------------------------------------------------filter获取回数end-----------------------------------------------------------#

# sorted 排序
# print(sorted([1,-12,3,6,31])) #默认升序
# print(sorted([1,-12,3,6,31],key=None,reverse=True)) #降序
# print(sorted([1,-12,3,6,31],key=abs)) #绝对值排序
# print(sorted(['aba','Zgb','eab'],key=str.lower))

# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=takeSecond) # 指定第二个元素排序
# print(random)

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def takeOne(elem):
#     return str(elem[0]).lower()
# L.sort(key=takeOne)
# print(L)


# 返回函数 函数作为返回值
# 正常求和
# def cal_num(*args):
#     a =0
#     for n in args:
#         a=a+n
#     return a
# print(cal_num(1,2,3))

# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）
# def lazy_num(*args):
#     def sum():
#         a =0;
#         for n in args:
#             a+=n
#         return a
#     return sum

# f = lazy_num(1,2,3)
# print(f())
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
# f1 =lazy_num(1,2,3)
# f2=lazy_num(1,2,3)
# print(f1==f2)

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
# 方法1：利用nonlocal关键字声明变量x，既不是局部变量，也不是全局变量，需要向上一层变量空间找这个变量 只在闭包里面生效，只能用在嵌套函数中，是python3中新添的关键字，python2中无
# def createCounter():
#     x =0
#     def counter():
#         nonlocal x
#         x+=1
#         return x
#     return counter

# 方法二：利用可变数据类型list
# def createCounter():
#     L =[0]
#     def counter():
#         L[0]+=1
#         return L[0]
#     return counter

# 方法三：利用生成器
# def createCounter():
#     def g():
#         n =0;    #生成器生成有序数列1，2，3......
#         while True:
#             n+=1
#             yield n

#     a = g()
#     def counter():
#         return next(a) #每次调用next()函数获得生成器的下一个返回值
#     return counter

# 方法四：利用len()
# def createCounter():
#     L = []
#     def counter():
#         L.append(1)
#         return len(L)
#     return counter

# counterA = createCounter()
# for n in range(4):
#     print(counterA())


# 匿名函数
# print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 装饰器
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
# 而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
# def log(text="call"):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# # @log()
# @log('execute')
# def now():
#     print('2015-3-25')
# now()

# 偏函数
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# int2 = functools.partial(int, base=2)
# print(int2('100', base=2))

# int2('10010') 相当于：
# kw = { 'base': 2 }
# int('10010', **kw)

# max2 = functools.partial(max, 10)
# max2(5, 6, 7)  相当于：
# args = (10, 5, 6, 7)
# max(*args)


# 类可以起到模板的作用，因此，可以在创建实例的时候，
# 把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去

#  注意：特殊方法“__init__”前后分别有两个下划线！！！
# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量(不建议)
# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#     # 外部代码要获取name和score
#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     # 外部代码修改score
#     def set_score(self,score):
#         if(0<=score<=100):
#             self.__score = score
#         else:
#             raise ValueError('bad score')

# 继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# class Dog(Animal):
#     def run(self):
#         # 父类原本封装的方法实现是，子类方法的一部分
#         # super()
#         print('Dog is running...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')

# def run_twice(animal):
#     animal.run()

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
# 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
# class Timer(object):
#     def run(self):
#         print('Start...')


# 获取对象信息
# 1.使用type()
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
# import types
# def fn():
#     pass
# type(123)==int
# type('abc')==str
# type(fn) == types.FunctionType
# type(abs)==types.BuiltinFunctionType
# type(lambda x:x*x)==types.LambdaType
# type((x for x in range(10))) == types.GeneratorType

# 2.使用isinstance()
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
# 继承关系object -> Animal -> Dog -> Husky
# class Animal(object):
#      pass
# class Dog(Animal):
#     pass
# class Husky(Dog):
#     pass

# a = Animal()
# d = Dog()
# h = Husky()

# print(isinstance(h,Husky))
# print(isinstance(h,Dog))
# isinstance(h,Husky)
# isinstance(h,Dog)
# isinstance('a', str)
# isinstance(b'a', bytes)
# isinstance([1, 2, 3], (list, tuple))

# 使用dir()  getattr()、setattr()以及hasattr()
# 获得一个对象的所有属性和方法
# print(dir('ABC'))
# len('ABC') 等价于 'ABC'.__len__
# class MyObject(object):
#     def __init__(self):
#         self.x = 9

#     def power(self):
#         return self.x*self.x

# obj = MyObject()
# # 对象的属性
# hasattr(obj,'x')
# getattr(obj,'x')
# setattr(obj,'y',10)
# # 可以传入一个default参数，如果属性不存在，就返回默认值
# getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# # 获得对象的方法
# hasattr(obj,'power')
# fn = getattr(obj,'power')
# fn()
# 只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
# sum = obj.x + obj.y
# 就不要写：
# sum = getattr(obj, 'x') + getattr(obj, 'y')


# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量
# class Student(object):
#     def __init__(self,name):
#         self.name = name

# s = Student('aa')
# s.score = 99

# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
# class Student(object):
#     name = "student"
#     count = 0
#     def __init__(self):
#         Student.count+=1


# obj = Student()
# print(obj.name)
# # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# obj.name = 'aaaa'
# print(obj.name)
# del obj.name  #如果删除实例的name属性
# print(obj.name)  #再次调用obj.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
# 实例属性属于各个实例所有，互不干扰；

# 类属性属于类所有，所有实例共享一个属性；

# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念
# 多重继承、定制类、元类

# 绑定属性和方法
# 1.类中直接绑定
# class Student(object):
#     def __init__(self,name):
#         self.name = name

#     def set_age(self,age):
#         self.age = age
# # 2.实例绑定
# from  types import MethodType
# id =0
# def set_id(self,id):
#     self.id = id
# obj = Student("aa")
# obj.grade = 12
# obj.set_id = MethodType(set_id,obj) #给实例绑定一个方法  对另一个实例是不起作用的
# obj.set_id(22)
# print(obj.id)

# # obj2 = Student('bb')  #对另一个实例是不起作用的  报错
# # obj2.set_id(33)
# # 3.为了给所有实例都绑定方法，可以给class绑定方法
# def set_score(self,score):
#     self.score = score
# Student.set_score =set_score

# obj3 = Student('cc')
# obj3.set_score(100)
# print(obj3.score)


# 使用__slots__:限制实例能添加的属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的/
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
# class Student(object):
#     __slots__ =('name','age')  # 用tuple定义允许绑定的属性名称

# # obj = Student()
# # obj.score =12  #报错

# class ExeStudent(Student):
#     pass
# stu = ExeStudent()
# stu.score = 30  #不会报错
# print(stu.score)


# 使用@property
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
# 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
# class Student(object):
#     def __init__(self):
#         pass

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('must interger')
#         if value<0 or value>100:
#             raise ValueError('score必须大于0小于100')
#         self._score = value

#     # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
#     @property
#     def age(self):
#         return 10

# obj = Student()
# obj.score = 60
# print(obj.score,obj.age)


# class Screen(object):
#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self,value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self,value):
#         self._height =value

#     @property
#     def resolution(self):
#         return self.width*self.height

# 多重继承
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017502939956896
class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('run')


class Flyable(object):
    def fly(self):
        print('fly')


class Ostrich(Bird):
    pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


class Dog(Mammal, Runnable):
    pass


class Parrot(Bird, Flyable):
    pass

# MixIn
# 设计类的继承关系时，通常，主线都是单一继承下来的 如 Ostrich继承Bird 如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn 还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。  自己补充：其他的有接口的概念 如js ts
# class RunnableMixIn(object):
#     def run(self):
#         print('run')

# class FlyableMixIn(object):
#     def fly(self):
#         print('fly')

# class CarnivorousMixIn(object):
#     pass

# class Dog2(Mammal,RunnableMixIn,CarnivorousMixIn):
#     pass
# # Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供
# from socketserver import (TCPServer,UDPServer,ThreadingMixIn)
# # 编写一个多进程模式的TCP服务  ForkingMixIn 在if hasattr(os, "fork"):才执行 所以ForkingMixIn导入会失败 class MyTCPServer(TCPServer,ForkingMixIn):
# class MyTCPServer(TCPServer):
#     pass

# #编写一个多线程模式的UDP服务
# class MyUDPServer(UDPServer,ThreadingMixIn):
#     pass


# 定制类
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904
# __slots__:定义允许绑定的属性名称
# __len__：能让class作用于len()函数
# __str__:返回用户看到的字符串
# __repr__:返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
# __iter__:如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# __getitem__:Fib要表现得像list那样按照下标取出元素,需要实现该方法  list有个神奇的切片方法所以需加isInstance判断是int还是切片
# __setitem__:对象视作list或dict来对集合赋值
# __delitem__():用于删除某个元素
# 通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
# __getattr__:  当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找

# class Student(object):
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return 'Student Object (name:%s)' % self.name

#     # 细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看
#     __repr__ = __str__

# s = Student('aaa')
# print(s)
# s

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1

#     def __iter__(self):
#         return self   # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#         if self.a > 1000:  # 退出循环的条件
#             raise StopIteration()
#         else:
#             return self.a  # 返回下一个值

#     # 但是没有对step参数  也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
#     def __getitem__(self, n):
#         if isinstance(n, int):# n是索引
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a+b
#         return a  # 返回值
#         if isinstance(n,slice): # n是切片

# for n in Fib():
#     print(n)

# print(Fib()[2])

# __getattr__
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
# class Student(object):
#     def __init__(self,name):
#         self.name = name

#     def __getattr__(self,attr):
#         if(attr=='score'):
#             return 3
#         if(attr=='age'):
#             return lambda:25 #返回函数也是可以的  只是调用时得用age()
#         raise AttributeError('\'Student\' Object not has attr:%s' % attr)

# s = Student('aaa')
# print(s.score)
# print(s.age())
# # print(s.abc)  #没抛出AttributeError的错误 则默认返回NONE


# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

# 利用完全动态的__getattr__，我们可以写出一个链式调用
# class Chain(object):
#     def __init__(self,path):
#         self._path =path

#     def __getattr__(self,path):
#         return Chain('%s/%s' % (self._path,path))

#     def __str__(self):
#         return self._path
#     __repr__ = __str__

# print(Chain('http://api.server').user.timeline.list)  #输出http://api.server/user/timeline/list

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
# class Student(object):
#     def __init__(self,name):
#         self.name = name

#     def __call__(self):
#         print('My name %s' % self.name)

# s = Student('sname')
# s()  #直接调用__call__打印了
# print(callable(Student('aa')))


# /users/:user/repos 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用  Chain().users('michael').repos
# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path

#     def __getattr__(self,path):
#         return Chain('%s/%s' % (self._path,path))

#     def __call__(self,path):
#         return Chain('%s/%s' % (self._path,path))

#     def __str__(self):
#         return self._path
#     __repr__ = __str__

# print(Chain().users("michael").repos) #输出/users/michael/repos


# 使用枚举类
# 每个常量都是class的一个唯一实例。Python提供了Enum类来实现
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
# Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# # value属性则是自动赋给成员的int常量，默认从1开始计数。
# print(Month.Jan) #Month.Jan
# print(Month.Jan.vlaue) #1
# for name,member in Month.__members__.items():
#     print(name,member.value)  #Jan 1


# 需要更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以帮助我们检查保证没有重复值。
# @unique
# class WeekDay(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

# print(WeekDay.Sun)  #WeekDay.Sun
# print(WeekDay['Sun']) #WeekDay.Sun
# print(WeekDay(1))  #WeekDay.Mon
# print(WeekDay(0))  #WeekDay.Sun
# print(WeekDay.Sun.value) #0

# 使用元类
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
# type：动态创建类
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# def fn(self, name='world'): # 先定义函数
#     print('Hello, %s.' % name)

# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# h = Hello()
# h.hello()

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# metaclass: 直译为元类,控制类的创建行为
# 先定义metaclass，就可以创建类，最后创建实例。
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# 错误处理 try expect finally


# IO编程
# 文件读写
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017607179232640
# try:
#     f = open('./io/io_1.txt','r',encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#         print('bb')
    
# Python引入了with语句来自动帮我们调用close()方法
# with open('./io/io_1.txt','r',encoding='utf-8') as f2:
#     print(f2.read())

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# with open('./io/io_1.txt','r',encoding='utf-8') as f3:
#     print(f3.readline()) #读取单行
 
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
# f3 = open('./io/io_1.txt','r',encoding='utf-8',errors='ignore')

# 写文件
# 调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# f4 = open('./io/io_2.txt','w')
# f4.write('hello world')
# f4.close()

# with open ('./io/io_2.txt','w') as f5:
#     f5.write('hello world2')

# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
# with open('./io/io_2.txt','a')  as f6:
#     f6.write('\nhello append')


# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# with open('./io/p_t.png','rb') as f7:
#     print(f7.read())


# StringIO和BytesIO是在内存中操作str和bytes的方法
# StringIO操作的只能是str
# BytesIO操作二进制数据
from io import StringIO
from io import BytesIO
# sio = StringIO()
# sio.write('测试io')
# print(sio.getvalue())

# 以用一个str初始化StringIO 然后，像读文件一样读取
# sio2 = StringIO('hello\nworld\npython')
# while True:
#     s = sio2.readline()
#     if s=='':
#         break
#     print(s.strip())


# bio = BytesIO()
# bio.write('中文'.encode('utf-8'))
# print(bio.getvalue())

# \xe4\xb8\xad\xe6\x96\x87
# 用一个bytes初始化BytesIO 然后，像读文件一样读取
# bio2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(bio2.read())


# 操作文件和目录 https://www.liaoxuefeng.com/wiki/1016959663602400/1017623135437088
# Python内置的os模块也可以直接调用操作系统提供的接口函数

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.name)

# 要获取详细的系统信息，可以调用uname()函数  uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的 

# 环境变量
# print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
# print(os.environ.get('PATH'))   

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径
# print('当前目录绝对路径-----',os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 然后创建一个目录:
# 删掉一个目录:
from pathlib import Path
# pt = os.path.join('.\\io','testDir')
# print(pt)
# if not os.path.exists(pt): #检测文件是否存在
#     os.mkdir(pt)
#     print('创建目录')
# else:
#     os.rmdir(pt)
#     print('删除目录')
# my_file = Path(pt)  
# if my_file.is_dir(): #检测是否为一个目录 指定的目录存在
#     print('是一个目录')  #指定的文件存在
# if my_file.is_file():
#     print('是一个文件')
# if my_file.exists(): #检测路径是一个文件或目录可以使用 exists() 
#     print('文件或目录存在')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
# indows下会返回这样的字符串part-1\part-2
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# print(os.path.split(pt))  #('./io', 'testDir')

# os.path.splitext()可以直接让你得到文件扩展名
# print(os.path.splitext(pt))  #('.\\io\\testDir', '')
# print(os.path.splitext('.\\io\io_1.txt'))  #('.\\io\\io_1', '.txt')


# 文件操作
#  对文件重命名:  os.rename
# url = '.\\io\\io_4.txt'
# if os.path.exists(url):
#     os.rename('.\\io\\io_4.txt','.\\io\\io_4.py')
#     print('rename success')
# else:
#     print('rename file not exits')

# 删掉文件:   os.remove
# rurl = '.\\io\\io_5.txt'
# if os.path.exists(rurl):
#     os.remove(rurl)
#     print('删除文件成功')
# else:
#     print('删除文件不存在')

# shutil模块
# 在os模块中不存在复制文件的函数 原因是复制文件并非由操作系统提供的系统调用 但shutil模块提供了copyfile()的函数
# import shutil
# cpNameStr = '.\\io\\io_5.txt'
# shutil.copyfile(cpNameStr,'.\\io\\io_5copy.txt')

# 利用Python的特性来过滤文件
# 列出当前目录下的所有目录
# print([x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


# os.getcwd(): 查看当前所在路径
# os.listdir(path): 列举目录下的所有文件（包含目录）,返回一个列表
# os.path.abspsth(path): 返回目录的绝对路径
# os.path.split(path): 将路径分为文件夹、文件名
# os.path.join(path1,path2): 将路径进行组合
# os.mkdir() 创建一个空目录
# os.rmdir() 删除一个空目录
# os.makedirs() 生成多层递归目录。
# os.removedirs(dirname) 删除多层递归空目录
# os.rename() 修改目录名或者文件名
# os.path.exists(path): 判断文件或者目录是否存在
# os.path.isfile(path): 判断是否为文件 os.path.isdir(path): 判断是否为目录 这两个方法返回的都是True或者False 所以记住一个和 os.path.exists则可以判断目录或者文件夹了
# os.path.getsize(name):获得绝对路径

# 在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相/绝对路径
# 使用r就防止了\t的转义 r 表示不转义
# Path  = r"F:\pythonSpace\pythonTest"
# searchPath = r"F:\pythonSpace\pythonTest"

# str = 'io_1'
# Aggregate_list = []
# def search_file(path,str,other):  #other传-1时为相对路径，否则为绝对路径
#     for file in os.listdir(path):
#         this_path = os.path.join(path,file)
#         if os.path.isfile(this_path):
#             if this_path.find(str)!=-1:
#                 if other == - 1:
#                     this_path = this_path.replace(searchPath,'')[1:]
#                     Aggregate_list.append(this_path)
#                 else:
#                     Aggregate_list.append(this_path)
#         else:
#             search_file(this_path,str,other)
#     return Aggregate_list
# print(search_file(searchPath,str,-1))


# 序列化 https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# import pickle
# pd = dict(name='测试name',age=22,score=100)
# # print(pickle.dumps(pd))

# with open('./pick/dump.txt','wb') as f:
#     pickle.dump(pd,f)

# with open('./pick/dump.txt','rb') as f:
#     print(pickle.load(f))

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
import json
# jd = dict(name='测试name',age=22,score=100)
# # dumps()方法返回一个str
# print(json.dumps(jd))  #{"name": "\u6d4b\u8bd5name", "age": 22, "score": 100}

# 把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
# json_str = '{"name": "\u6d4b\u8bd5name", "age": 22, "score": 100}'
# print(json.loads(json_str)) #{'name': '测试name', 'age': 22, 'score': 100}

# -------------------------------JSON进阶说明start-------------------------------------
# JSON进阶 print(json.dumps(s, default=lambda obj: obj.__dict__))
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
# print(json.dumps(s, default=student2dict))
# -------------------------------JSON进阶说明end-------------------------------------

# Python既支持多进程，又支持多线程 https://www.liaoxuefeng.com/wiki/1016959663602400/1017627212385376
# 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
# 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。

# 正则表达式
# *:任意个字符（包括0个）  
# +:至少一个字符  如:\s+表示至少有一个空格
# ?:0个或1个字符
# {n}:n个字符
# {n,m}:n-m个字符
# []表示范围
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。
# 正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group） group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串

import re
# 由于Python的字符串本身也用\转义  建议使用Python的r前缀，就不用考虑转义的问题
# re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# print(re.match(r'^(\d+?)0$','102300'))

# 切分字符串
# print('a b   c'.split(' '))  #['a', 'b', '', '', 'c']  没法多个空格
# print(re.split(r'\s+','a b   c'))  #['a', 'b', 'c']
# print(re.split(r'[\s\,]+','a, b   c'))  #['a', 'b', 'c']
# print(re.split(r'[\s\,\;]+','a, b   c'))  #['a', 'b', 'c']

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0)) #010-12345
# print(m.group(1)) #010
# print(m.group(2)) #12345

# 贪婪匹配
# re.match(r'^(\d+)(0*)$', '102300').groups() #\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# re.match(r'^(\d+?)(0*)$', '102300').groups() #加个?就可以让\d+采用非贪婪匹配



# 常用内建模块
# datetime是Python处理日期和时间的标准库
# datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime
# %a %A  %b %B   https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
from datetime import datetime,timedelta,timezone
# 获取当前日期和时间
# print(datetime.now())

# 获取指定日期和时间
# dt = datetime(2020,2,23,9,00)
# print(dt.now())

# datetime转换为timestamp 时间戳
# 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# times = datetime.timestamp(dt)
# print(times)

# timestamp转换为datetime
# print(datetime.fromtimestamp(times)) #2020-02-23 09:00:00

# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换 本地时间是指当前操作系统设定的时区。
# UTC标准时区的时间  (标准时间与北京时间差了8小时)
# print(datetime.utcfromtimestamp(times)) #2020-02-23 01:00:00  

# str转换为datetime
# 必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
# 转换后的datetime是没有时区信息的。
# curt = datetime.strptime('2021-1-20 20:30:50','%Y-%m-%d %H:%M:%S')
# print(curt) 

# # datetime转换为str
# cpt = datetime.now()
# print(cpt.strftime('%a, %b %d %H:%M'))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
# ddt = datetime.now()
# print(ddt)
# print(ddt-timedelta(hours=3))
# print(ddt+timedelta(days=1,hours=3))

# 本地时间转换为UTC时间
# datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
# tz_utc_8 = timezone(timedelta(hours=8))
# ddt2 = datetime.now()
# print(ddt2)
# ddt2.replace(tzinfo=tz_utc_8)
# print(ddt2)
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区

# 时区转换
# print(datetime.now()) #021-02-23 10:47:39.689560
# print(datetime.utcnow()) ##2021-02-23 02:47:39.689560
# # 拿到UTC时间，并强制设置时区为UTC+0:00:
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)  #2021-02-23 02:47:39.689560+00:00
# # astimezone()将转换时区为北京时间:
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) 
# print(bj_dt) #2021-02-23 10:50:54.708714+08:00
# # 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
# dj_dt1 = utc_dt.astimezone(timezone(timedelta(hours=9)))
# dj_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(dj_dt1,dj_dt2)  #dj_dt1 和 dj_dt2等价

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

# 如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
# def to_timestamp(dt_str, tz_str):
#     h = int(tz_str[3:-3])
#     tz = timezone(timedelta(hours=h))
#     dt= datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#     dt = dt.replace(tzinfo=tz)
#     return dt.timestamp()
# print(to_timestamp('2021-1-21 9:01:30','UTC+08:00')) #1611190890
# print(datetime(2021,1,21,9,1,30).timestamp())   #1611190890
# print(datetime.now().timestamp())  #1614050937.889305


# collections
# collections是Python内建的一个集合模块，提供了许多有用的集合类
# namedtuple：是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# namedtuple('名称', [属性list]):

# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p = Point(2,3)
# print(p.x,p.y)

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素

# from collections import deque
# q =  deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q) #deque(['y', 'a', 'b', 'c', 'x'])

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入
# from collections import defaultdict
# df = defaultdict(lambda :'N/A')
# df['key1'] = 'aaaa'
# print(df['key1']) #aaaa
# print(df['key2']) #N/A

   
#OrderedDict
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

# from collections import OrderedDict
# od = dict([('a',1),('c',2),('b',3)])
# print(od) #{'a': 1, 'c': 2, 'b': 3}
# od2 = OrderedDict([('a',1),('c',2),('b',3)])
# print(od2)  #OrderedDict([('a', 1), ('c', 2), ('b', 3)])
# od3 = OrderedDict()
# od3['z'] = 2
# od3['y'] = 3
# od3['x'] =1
# print(od3.keys()) #odict_keys(['z', 'y', 'x'])

# ChainMap
# 把一组dict串起来并组成一个逻辑上的dict ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# 读写这个对象就像是读字典一样 不会真的把字典合并在一起，而是在内部储存一个Key到每个字典的映射 
# 先去查询这个key在哪个字典里面，然后再去对应的字典里面查询对应的值
# 1.两个字典里面有一个Key的名字相同，那么使用ChainMap以后会读取哪一个？答：第一个拥有这个Key的字典里面的值
from collections import ChainMap
# ca = {'a':1,'c':3}
# cb = {'b':2,'a':5}
# e = ChainMap(ca,cb)
# print(e['a']) #1

# 2.为ChainMap对象添加一个Key-Value对，那么这个值会添加到哪里？ 答：新的Key-Value会被添加进第一个字典里面
# ca = {'a':1,'c':3}
# cb = {'b':2,'a':5}
# e = ChainMap(ca,cb)
# e['d'] = 45
# print(ca,cb) #{'a': 1, 'c': 3, 'd': 45} {'b': 2, 'a': 5}

#3.从原字典里面删除一个Key，ChainMap对象里面的Key也会消失吗? 答：如果修改了原来的字典，那么 ChainMap对象也会相应更新
# ca = {'a':1,'c':3}
# cb = {'b':2,'a':5}
# e = ChainMap(ca,cb)
# ca['e'] = 6
# print(e) #ChainMap({'a': 1, 'c': 3, 'e': 6}, {'b': 2, 'a': 5})
# del ca['e']
# print(e)

# 4.从ChainMap对象里面删除一个Key，那么原字典里面的Key会消失吗?
# 答：如果这个Key只在一个源字典中存在，那么这个Key会被从源字典中删除。
# 如果这个Key在多个字典中都存在，那么Key会被从第一个字典中删除。当被从第一个字典中删除以后，第二个源字典的Key可以继续被 ChainMap读取。
# ca = {'a':1,'c':3}
# cb = {'b':2,'a':5}
# e = ChainMap(ca,cb)
# e.pop('c') 
# print(ca,cb) #{'a': 1} {'b': 2, 'a': 5}
# e.pop('a')
# print(ca,cb) #{} {'b': 2, 'a': 5}
# print(e['a']) # 5

#Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数 
# Counter实际上也是dict的一个子类
# from collections import Counter
# c = Counter()
# for char in 'progress':
#     c[char] = c[char]+1

# print(c) #Counter({'r': 2, 's': 2, 'p': 1, 'o': 1, 'g': 1, 'e': 1})
# #  也可以一次性update
# c.update('hello') #会计算progress 和hello的 
# print(c) #Counter({'r': 2, 'o': 2, 'e': 2, 's': 2, 'l': 2, 'p': 1, 'g': 1, 'h': 1})

# c2 = Counter()
# c2.update('wo shi ni') #Counter({' ': 2, 'i': 2, 'w': 1, 'o': 1, 's': 1, 'h': 1, 'n': 1}) 空格也会计算
# print(c2)


# base64
# Base64是一种用64个字符来表示任意二进制数据的方法。0~63   0~111111 6位
# 最常见的二进制编码方法
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行
# Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示
#Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
# Base64的原理:
# 1.准备一个包含64个字符的数组：['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 2.对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit
# 3.得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

import base64 
# bd = base64.b64encode(b'binary\x00string')
# print(bd) #b'YmluYXJ5AHN0cmluZw=='
# st = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
# print(st) #b'binary\x00string'

# tip = '世界你好'
# tb = bytes(tip,'utf-8')
# print(tb) #b'\xe4\xb8\x96\xe7\x95\x8c\xe4\xbd\xa0\xe5\xa5\xbd'
# bd2 = base64.b64encode(tb)  #b'5LiW55WM5L2g5aW9'
# print(bd2)

# b = b''         # 创建一个空的bytes
# b = bytes()      # 创建一个空的bytes
# b = b'hello'    #  直接指定这个hello是bytes类型
# b = bytes('string',encoding='编码类型')  #利用内置bytes方法，将字符串转换为指定编码的bytes
# b = str.encode('编码类型')   # 利用字符串的encode方法编码成bytes，默认为utf-8类型
# bytes.decode('编码类型')：将bytes对象解码成字符串，默认使用utf-8进行解码。

# 标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
# bt = b'i\xb7\x1d\xfb\xef\xff'
# print(base64.b64encode(bt))  #b'abcd++//'
# print(base64.urlsafe_b64encode(bt)) #b'abcd--__'

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
# 'abcd' -> 'YWJjZA=='
# 自动去掉=:
# 'abcd' -> 'YWJjZA'

# Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码

# 写一个能处理去掉=的base64解码函数：
# def safe_base64_decode(s):  #s是64编码
#     length = len(s)
#     mod = length % 4  #长度必须4的倍数 差几位则末位自动补= 进行解码
#     s += b'='*(4-mod) if (mod != 0 and mod !=4) else b''
#     return base64.urlsafe_b64decode(s)

# assert b'abcd' == safe_base64_decode(b'YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA')
# print('ok')

# 去掉=号
# def safe_base64_decode(s):  #s未常规字符串
# 	b = base64.b64encode(s.encode('utf-8'))#因为python3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码
# 	bstr_tmp = str(b,'utf-8') #把byte类型的数据转换为utf-8的数据
# 	b_str= bstr_tmp.strip(r'=+') #用正则把 = 去掉
# 	return b_str
 
# s = "binarybstr\x00string"
# safe_b = safe_base64_decode(s)
# print(safe_b)

# struct https://www.liaoxuefeng.com/wiki/1016959663602400/1017685387246080
# struct模块来解决bytes和其他二进制数据类型的转换。
import struct
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# print(struct.pack('>I',10240099))   #b'\x00\x9c@c'

# unpack把bytes变成相应的数据类型
# >IH:  后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')) #(4042322160, 32896)


# Big Endian 和 Little Endian 模式的区别
# big endian是指低地址存放最高有效字节（MSB），而little endian则是低地址存放最低有效字节（LSB）
# 所有网络协议也都是采用big endian的方式来传输数据的。所以有时我们也会把big endian方式称之为网络字节序
# 数字0x12345678在两种不同字节序CPU中的存储顺序
# Big Endian

#    低地址                                            高地址

#  ----------------------------------------------------------------------------->

#    |     12     |      34    |     56      |     78    |

# Little Endian 

#    低地址                                            高地址

#    ----------------------------------------------------------------------------->

#    |     78     |      56    |     34      |     12    |


# hashlib
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
# 摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难
# 要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
import hashlib 
# myMd = hashlib.md5()
# myMd.update('hello world'.encode('utf-8'))
# print(myMd.hexdigest()) #5eb63bbbe01eeed093cb22bb8f5acdc3

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
# myMd2 = hashlib.md5()
# myMd2.update('hello '.encode('utf-8'))
# myMd2.update('world'.encode('utf-8'))
# print(myMd2.hexdigest()) #5eb63bbbe01eeed093cb22bb8f5acdc3

# sha1 = hashlib.sha1('hello world'.encode('utf-8'))
# print(sha1.hexdigest())   #2aae6c35c94fcfb415dbe95f408b9ce91ee846ed

# sha2 = hashlib.sha1()
# sha2.update('hello world'.encode('utf-8'))
# print(sha2.hexdigest()) #2aae6c35c94fcfb415dbe95f408b9ce91ee846ed

# 摘要算法应用
# name	password
# michael	123456

# username	password
# michael	e10adc3949ba59abbe56e057f20f883e
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }

# def login(user,password):
#     dbp = db[user]
#     if dbp:
#         mymd = hashlib.md5()
#         mymd.update(password.encode('utf-8'))
#         if mymd.hexdigest()==dbp:
#             return True
#     return False
# 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# 由于常用口令的MD5值很容易被计算出来，
# 所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
# def calc_md5(password):
#     return get_md5(password + 'the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？
# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。


# hmac
# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
# Python自带的hmac模块实现了标准的Hmac算法
# hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
import hmac
# message = b'hello world'
# key = b'secret'
# hm = hmac.new(key,message,digestmod='md5')
# print(hm.hexdigest())

# itertools
# itertools提供了非常有用的用于操作迭代对象的函数。
#count()会创建一个无限的迭代器
# cycle()会把传入的一个序列无限重复下去
# repeat()负责把一个元素无限重复下去

# natuals = itertools.count(1)  #count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
# for n in natuals:
#     print(n) 

# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
import itertools
# ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
# natures = itertools.count(1)
# ns = itertools.takewhile(lambda x:x<=10,natures)
# print(list(ns)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# urllib
# Get：urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

# Post：要以POST发送一个请求，只需要把参数data以bytes形式传入
# Handler：还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
from urllib import request,parse
# 例1：对豆瓣的一个URLhttps://www.baidu.com/进行抓取，并返回响应
# rUrl ='https://www.baidu.com/'
# with request.urlopen(rUrl) as f:
#     data = f.read()
#     print('status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data:\n',data.decode('utf-8'))

#模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
# 例2：模拟iPhone 6去请求豆瓣首页
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data:\n',data.decode('utf-8'))

# 例3：模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
# 以POST发送一个请求，只需要把参数data以bytes形式传入
# print('login to weibo.cn....')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin','https://passport.weibo.cn')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req,data=login_data.encode('utf-8')) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print("Data:\n",f.read().decode('utf-8'))
# 登录成功        Data: {"retcode":20000000,"msg":"","data":{...,"uid":"1658384301"}}
# 登录失败 Data:{"retcode":50050011,"msg":"\u8bf7\u5b8c\u6210\u9a8c\u8bc1","data":{"errurl":"https:\/\/passport.weibo.cn\/signin\/secondverify\/index?id=2MDJgNe9lAAQfmwSPo-Eoa2caibijGrssBWxvZ2lu&first_enter=1","errline":526}}


# XML
# DOM vs SAX
# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 正常情况下，优先考虑SAX，因为DOM实在太占内存。
# SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数
# 如：<a href="/">python</a>  
# 产生3个事件
# 1、start_element事件，在读取<a href="/">时；
# 2、char_data事件，在读取python时；
# 3、end_element事件，在读取</a>时。
# from xml.parsers.expat import ParserCreate
# from xml.parsers.expat import ParserCreate
# class DefaultSaxHandler(object):
#     def start_element(self,name,attrs):
#         print('sax:start_element:%s，attrs:%s' % (name,str(attrs)))
    
#     def end_element(self,name):
#         print('sax:end_element:%s' % name)

#     def char_data(self,text):
#         print('sax:char_data:%s' % text)

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# p = ParserCreate()
# handler = DefaultSaxHandler()
# p.StartElementHandler = handler.start_element
# p.EndElementHandler = handler.end_element
# p.CharacterDataHandler = handler.char_data
# p.Parse(xml)

# 读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

# HTMLParser https://www.cnblogs.com/liuhaidon/archive/2019/12/18/12060184.html
# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。
# 常用方法
# HTMLParser.feed(data)：接收一个字符串类型的HTML内容，并进行解析。
# HTMLParser.close()：当遇到文件结束标签后进行的处理方法。如果子类要复写该方法，需要首先调用HTMLParser累的close()。
# HTMLParser.reset()：重置HTMLParser实例，该方法会丢掉未处理的html内容。
# HTMLParser.getpos()：返回当前行和相应的偏移量。
# HTMLParser.handle_starttag(tag, attrs)：对开始标签的处理方法。例如<div id="main">，参数tag指的是div，attrs指的是一个（name,Value)的列表，即列表里面装的数据是元组。
# HTMLParser.handle_endtag(tag)：对结束标签的处理方法。例如</div>，参数tag指的是div。
# HTMLParser.handle_startendtag(tag, attrs)：识别没有结束标签的HTML标签，例如<img />等。
# HTMLParser.handle_data(data)：对标签之间的数据的处理方法。<tag>test</tag>，data指的是“test”。
# HTMLParser.handle_comment(data)：对HTML中注释的处理方法。
# HTMLParser.handle_entityref(name)：&nbsp 
# HTMLParser.handle_charref(name)：&#1234

# tag表示的是html标签，attrs是一个列表，列表元素为一个个“(属性，值)”形式的元组。 
# HTMLParser会自动将tag和attrs都转为小写。
from html.parser import HTMLParser
from html.entities import name2codepoint
import html
# class MyHtmlParse(HTMLParser):
#     def handle_starttag(self,tag,attrs):
#         print('starttag:<%s> %s' % (tag,str(attrs)))
    
#     def handle_endtag(self,tag):
#         print('endtag:<%s>' % tag)
    
#     def handle_startendtag(self,tag,attrs):
#         print('startendtag:<%s/>' %tag)
    
#     def handle_comment(self,data):
#         print('<!--%s-->' % data)
    
#     def handle_entityref(self,name):
#         print('$%s' % name)
    
#     def handle_charref(self,name):
#         print('$#%s' % name)
    
# hXml = '''<html>
#             <head>这是头标签</head>
#             <body>
#                 <!-- test html parser -->
#                 <p>Some <a href=\"#\">html</a> HTML&nbsp;&#1234; Ӓtutorial...<br>END</p>
#                 <img />
#             </body></html>'''
# mp = MyHtmlParse()
# mp.feed(hXml)
# mp.close()


# 处理HTML转义字符
# 转义字符（Escape Sequence）由三部分组成：第一部分是一个 & 符号，第二部分是实体（Entity）名字，第三部分是一个分号。 比如，要显示小于号（<），就可以写 &lt;。
# myHtmlStr = '&lt;abc&gt;'
# # 反转义：方式1
# html_parse = HTMLParser()
# text = html_parse.unescape(myHtmlStr)
# print(text)  #<abc>

# # # 反转义：方式2
# text = html.unescape(myHtmlStr) #<abc>
# print(text)

# # 转义
# ctx = html.escape(text) #&lt;abc&gt;
# print(ctx)


# 例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
# Python官网发布的会议时间、名称和地点的网页源码样式：
#  <li>
#       <h3 class="event-title"><a href="/events/python-events/776/">PyCon AU 2019</a></h3>
#     <p>                 
#         <time datetime="2019-08-02T00:00:00+00:00">02 Aug. &ndash; 06 Aug. <span class="say-no-more"> 2019</span></time>
#         <span class="event-location">Sydney, Australia</span>              
#     </p>
#  </li>
# 上段未html  非代码

fUrl = 'https://www.python.org/events/python-events/'
def get_data(path):
    myHeader = {
        'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
    }
    req = request.Request(path,headers=myHeader)
    with request.urlopen(req,timeout=25) as f:
        data = f.read()
        print(f'Status: {f.status} {f.reason}')
        return data.decode('utf-8')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata ='' # 设置一个空的标志位
        self.info  = []

    def handle_starttag(self,tag,attrs):
        if ('class','event-title') in attrs:
            self.__parsedata = 'name'
        if tag =="time":
            self.__parsedata = 'time'
        if ('class','say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class','event-location') in attrs:
            self.__parsedata = 'location'
    
    def handle_endtag(self,tag):
        self.__parsedata = '' # 在HTML 标签结束时，把标志位清空
    
    def handle_data(self,data):
        if self.__parsedata=='name':
            self.info.append(f'会议名称：{data}')
        if self.__parsedata=='time':
            self.info.append(f'会议时间：{data}')
        if self.__parsedata=='year':
            if re.match(r'\s\d{4}',data):
                self.info.append(f'会议年份：{data.strip()}')   # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
        if self.__parsedata=='location':
            self.info.append(f'会议地点：{data}')

myP = MyHTMLParser()
data = get_data(fUrl)
myP.feed(data)
myP.close()
for s in myP.info:
    print(s)
    
