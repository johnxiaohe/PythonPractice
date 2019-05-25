#!/usr/bin/env python
# # -*- coding:utf-8 -*-
#从现在开始记的 把之前的记录一下
# chr()表示将ascll码转换为字符  ord()将字符转换为ascll码
#s.encode('编码')按照规则进行编码 s.decode(‘编码’)进行解码
#%d输出整数 %s输出字符串 %f浮点数 %.1f小数点后保留一位 %x十六进制数
#int(s)将字符串转换为整数
#print('%s,%d'%('该数字是：',100))    print('{0}{1}'.formart('该数字是:',100))
#同一个块儿域中，缩进在同一个位置表示是同一个执行体  意味着是在同一个大括号中
age=12
if age>=28:
    print('your age is',age)
    print('if域结束')
elif age>=18:
    print('your age <28 but >=18')
    print('else if 域1结束')
#当符合条件则不会向下执行直接跳出判断 elif可以有很多
elif age >= 18:
    print('your age <28 but >=18')
    print('else if 域2结束')
elif age >= 10:
    print('your age <18 but >=10')
    print('else if 域2结束')
else:
    print('your age < 18')
    print('else域结束')
#if 后面判断只要不是False或者非空字符串、非零值、非空List就为True
x=True
if x:
    print('True')

#input()输入均为字符串，如需要整数类型需要int()转换
s=input('请输入一个整数:')
check = int(s)
if check>50:
    print('数字太大了')
elif check==50:
    print('数字刚好')
else:
    print('太小了再大点')