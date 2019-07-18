#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#循环practies

#for x in y 循环  x为y的子元素将循环完毕y
names=['xiaoe','tom','marry']
for name in names:
    print('hello,%s!'%name)

sum=0
enum=(1,2,3,4,5,6,7,8,9)
for x in enum:
    sum=sum+x
print(sum)
#range()函数可以生成一个整数序列 然后通过list()转换为list
index=range(10)
print(index)
print(list(index))
for x in list(index):
    sum=sum+x
print(sum)

#while 条件不满足退出
sum=0
n=99
while sum<n:
    sum=sum+10
    n=n-sum
print('n=%d , sum=%d'%(n,sum))

#break 结束循环 continue跳过当前循环
n=1
while n<100:
    n=n+1
    if(n%2==0):
        print('偶数不打印')
        continue
    print(n)
    if n==7:
        break
