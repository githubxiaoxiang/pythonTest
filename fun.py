import string;
import re;
from functools import partial
import itertools
# 3.2 函数
# 返回多个值
# def fun():
#     a=1
#     b=2
#     c=3
#     return a,b,c

# print(fun());#1,2,3

# 去除空白符、删除各种标点符号、正确的大写格式等。做法之一是使用内建的字符串方法和正则表达式re模块
# states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda','south   carolina##', 'West virginia?'];
# def clean_str(strs):
#     result=[];
#     for value in strs:
#         value = value.strip();
#         value = re.sub('[!#?]','',value);
#         value = value.title();
#         result.append(value);
#     return result;

# print(clean_str(states));


# 匿名（lambda）函数
# def short_function(x):
#     return x * 2

# equiv_anon = lambda x: x * 2
# print(equiv_anon(2));

# def apply_for_list(some_list,f):
#     return [f(x) for x in some_list]
# ints = [1,2,0,8,9];
# print(apply_for_list(ints,lambda x: x*2));

# 各字符串不同字母的数量对其进行排序
# strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
# print(list(strings[0]));#['f', 'o', 'o']
# print(set(list(strings[0])));#{'o', 'f'}
# print(len(set(list(strings[0]))));#2
# strings.sort(key=lambda x: len(set(list(x))));
# print(strings);#['aaaa', 'foo', 'abab', 'bar', 'card']

# def squares(n=10):
#     print('Generating squares from 1 to {0}'.format(n ** 2))
#     for i in range(1,n+1):
#         yield i**2

# gen = squares()
# print(gen)

# for x in gen:
#     print(x,end=' ');

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# sum = 0
# a =[1,2,3,4]
# for i in itertools.permutations(a,3):
#     print(i)
#     sum+=1
# print(sum)