#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import itertools
#提供了用于操作迭代对象的函数

natuals=itertools.count(1)#指定步长以及起始位置的无线迭代器
#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
ns=itertools.takewhile(lambda x:x<10,natuals)
for n in ns:
    print(n)

cs=itertools.cycle('ABC')#字符串也是序列的一种相当于list了  cycle会无限重复该序列同样停不下来。
# for c in cs:
#     print(c)


#repeat()负责把一个元素无限重复下去，提供第二个参数就可以限定重复次数 不指定就无限循环
ns=itertools.repeat('A',3)
for n in ns:
    print(n)

#操作迭代器函数
# chain()把一组迭代对象串联起来，形成大迭代器
for c in itertools.chain('ABC','XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAABBBCCCAAA'):
    print(key,list(group))
    #A ['A', 'A', 'A']
    # B ['B', 'B', 'B']
    # C ['C', 'C', 'C']
    # A ['A', 'A', 'A']

#忽略大小写 groupby可以添加执行方法
for key , group in itertools.groupby('AaaBbbCccaAA',lambda c:c.upper()):
    print(key,list(group))
    '''A ['A', 'A', 'A']
    A ['A', 'a', 'a']
    B ['B', 'b', 'b']
    C ['C', 'c', 'c']
    A ['a', 'A', 'A']'''

#计算这个序列的前N项和
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    ns=itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    n=itertools.takewhile(lambda k:k<=2*N-1,ns)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    i=1
    last=list()
    for k in n:
        last.append(4/k*i)
        i=i*(-1)
    # step 4: 求和:
    i=0
    for k in last:
        i=i+k
    return i
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
