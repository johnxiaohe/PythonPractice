#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from collections import Iterable
#列表生成器  列表数量大 使用即时演算推出，不保存实际内容
#一边循环一边计算的机制，称为生成器：generator

#第一种方法很简单，只要把一个列表生成式的[]改成()
L=[x**2 for x in range(1,11)]
print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
g=(x**2 for x in range(1,11))
print(g) #<generator object <genexpr> at 0x000002D8348524C0>
#next(g) 会计算下一个g的内部元素并返回  内部会自己记录计算到那个了
next(g)
next(g)
#for 循环进行输出
print(isinstance(g,Iterable)) #True   它是一个可迭代对象
for x in g:
    print(x)

"""定义generator的另一种方法"""
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):  #波非那切数列 除第一个和第二个数外，任意一个数都可由前两个数相加得到：
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return '结束'

print(fib(6))

def fib(max):  #波非那切数列 除第一个和第二个数外，任意一个数都可由前两个数相加得到：
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return '结束'
#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print(fib(6))  #<generator object fib at 0x000001EE702BCFC0>

#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g=fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print("Generator return value ",e.value)
        break

def triangles():
    L = [1]
    while True:
        yield L
        L = [L[i]+L[i+1] for i in range(len(L)-1)]
        L.insert(0, 1)
        L.append(1)

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


"""迭代器"""
#可以直接作用于for循环的数据类型  直接作用于for循环的对象统称为可迭代对象：Iterable。
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#使用iter()方法将可迭代但不是Iterator类型的对象转化成Iterator 例如list tuple str dict set
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# Python的for循环本质上就是通过不断调用next()函数实现的