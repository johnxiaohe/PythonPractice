#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#list[] 不可变元组tuple使用()
s=['a','b','c']
t=('a','b','c')
#list()方法用于将元组转换为列表。   range() 函数可创建一个整数列表 range()函数，可以生成一个整数序列，再通过list()函数可以转换为list 这个为0-9 十个整数
L=list(range(10))
#len()计算长度 列表就是列表长度 字符串就字符串长度 字节就是所占字节数
print(len(L))
print(L)
#list是一个可变的有序表 appen()向末尾增加元素
s.append('d')
print(s)
#插入指定位置 insert(index,元素)
s.insert(1,'a')
print(s)
#删除末尾元素并返回 pop() pop(index)删除指定元素
print(s.pop())
print(s.pop(1))
print(s)
#替换元素 类似于Java的数组赋值
s[0]='c'
s[2]='a'
print(s)
#list里面的元素的数据类型可以不同可以是其他list  反正就是可以是各种数据类型啦 类似于多维数组

#tuple定义一个元素要加, 不加,则该变量不是元组而是一个单纯的元素 元组要想内容可变 可以将其内部元素设置成为list
t=(1,)
#空的元组和list
L=[]
T=()
print(len(L),len(T))
print(L,T)

#切片  Python中符合序列的有序序列都支持切片(slice) 列表,字符,元组(截取)
# 格式:[start : end : step] Start:起始索引,从0开始,-1表示结束 End:结束索引 Step:步长
# L[n1:n2:n3]
#n1代表开始元素下标，不写就是从第一个开始  看n3符号定，n3是负的就是最右边是开始  n3是正的就是从最左边开始
#n2代表结束元素下标,不写就是最后一个元素结束 看n3符号定，n3是负的就是最右边是开始  n3是正的就是从最左边开始
#n3代表切片间隔和方向 不写默认1 如-2表示切片从后往前间隔为2

#L中每个元素都有正负两种下标，正数从L[0]开始，表示第一个元素。倒数L[-1]表示倒数第一个元素。L[0]和L[-10]指的同一个元素都是0
#无论L[0]还是L[-10] ，我觉得可以这么理解：你先把负数转换成正数。
L=list(range(0,10))
#常用的几种切片方式:
#  [:] 如:list2=list1[:] 全部截取 类似复制
#  [0:1:n] 如:list1[0:3;1] 从0开始到3每次增加1截取,不包含索引结束位置 前闭后开
#  [0:-1:1]:从0开始到结束,每次增加1,截取不包含索引结束位置 前闭后开
#  [:3]:默认从起始位置索引,每次增加1截取,结束位置索引为3
#  [3:0:-1]反向取值,每次增加1截取,不包含索引结束位置

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('         ') != '':
    print('测试失败!')
else:
    print('测试成功!')