#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from collectionsPractise import Iterable
#迭代
#循环遍历就是迭代 for...in
#可迭代类型：list tuple set str dict
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)

for ch in 'CXY':
    print(ch)

#通过collections模块的Iterable类型判断一个对象是可迭代对象  isinstance判断对象是否是后面的类型
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))

#enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)
#for可同时引用多个变量 但是一定要在每次迭代的时候保证当前迭代元素和引用变量数量相同
for x, y,z in [(1,1,1), (2,4,6), (3,9,7)]:
 print(x, y,z)

 #请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    # n=len(L)
    if len(L)<=0:
       return (None, None)
    else:
       min=L[0]
       max=L[0]
       for k in L:
           if k<min:
               min=k
           if k>max:
               max=k
       return (min,max)



# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


#列表生成式  内置可以创建list的语句规则

L=list(range(1,11))
print(L)
#列表生成式  将其最后生成列表语句提到前面来  结果：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
L=[x**2for x in range(1,11)]
print(L)
#所以还可以加判断  [4, 16, 36, 64, 100]
L=[x**2 for x in range(1,11) if x%2==0]
print(L)
#支持多重循环    for嵌套 结果先提到前面然后封装套list中
# 结果['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)
#支持多变量
# ['x=A', 'y=B', 'z=C']
d={'x':'A','y':'B','z':'C'}
L=[k+'='+v for k,v in d.items()]
print(L)

#可以在前方调用方法(x.lower全小写)   ['hello', 'world', 'ibm', 'apple']
L=['Hello','World','IBM','Apple']
L=[x.lower() for x in L]
print(L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L=[x.lower() for x in L1 if isinstance(x,str) ]
print(L)


