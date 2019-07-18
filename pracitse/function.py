#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 导入math包
import math

#函数调用
#abs()求绝对值
s=abs(-50)
print(s)

#max()接收多个参数 返回最大值
s=max(2,3,4,5,6,1)
print(s)

#数据类型转换函数
s=int('123')
print(s)

#舍去小数部分
s=int(12.76)
print(s)
s=float('12.34')
print(s)
s=str(1.23)
print(s)
s=str(100)
print(s)
s=bool(1)
print(s)
s=bool("")
print(s)

#为函数起别名  不能带函数后面的括号
a=abs
print(a(-1))

#hex()将整数转换成十六进制字符串
n1=hex(255)
n2=hex(1000)
print(n1,n2)

#自定义函数 def 函数名(参数，参数) :
#若多个相同参数可以使用*参数来表示
def my_abs(x):
    #参数检查 isinstance函数用来检查对象是否是可用参数 第一个是要比对的参数 第二个是数据类型元组
    if not isinstance(x,(int,float)):
        raise TypeError('参数类型错误')
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-100))

def my_min(*args):
    s=list(args)
    num = len(s)-1
    if num<=0:
        return None
    else:
        for x in s:
            # 参数检查 isinstance函数用来检查对象是否是可用参数 第一个是要比对的参数 第二个是数据类型元组
            if not isinstance(x,(int,float)):
                raise TypeError('参数类型错误')
        k=s[0]
        while num>0:
            l=s[num]
            if k<l:
                k=l
            num = num - 1
    print(k)
my_min(9,2,7,4,11,6,0,2)

#定义空函数  pass占坑符  用于以后实现该函数
def nop():
    pass

#返回多个参数(其实返回的是一个元组tuple类型 所以还是返回的是一个单一值)   angle表示不传默认为0
def move(x,y,step,angle=0):
    print("angle:",angle)
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
print(move(1,2,3,math.pi/6))

#计算一元二次方程的解 正确的话返回的是一个元组或一个数
def quadratic(a,b,c):
    a2 = a*2
    b24ac=b**2-(4*a*c)
    if b24ac<0:
        return "该方程无解"
    else:
        bb = math.sqrt(b24ac)
        dt1 = (-b + bb) / a2
        if b24ac==0:
            return dt1
        dt2 = (-b - bb) / a2
        if b24ac>0:
            return dt1,dt2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
if quadratic(2,3,1)!=(-0.5, -1.0):
    print('测试失败')
elif quadratic(1,3,-4) !=(1.0, -4.0):
    print("测试失败")
else:
    print("测试成功")

#计算x2  在方法参数列表中提前赋值表示默认值，当调用时候没有传递该参数就使用默认值 参数可以指定调用时power(n=3)这样可以避免多默认值调用仅想改变其中一个的情况
# 定义默认参数要牢记一点：默认参数必须指向不变对象！ 如果要默认我为空则设置为None
# 函数定义时默认参数就已经确定并指向一个地址 每次调用均会去该地址找默认参数 如果该地址的值变了 默认参数的值也改变
def power(x,n=2):
    return x**n
print(power(2,3))


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数*ages、命名关键字参数和关键字参数**kw。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 1使用list或者tuple  内部循环调用
# 2.定义方法时参数名前面加* 这样函数内部参数numbers接收到的是一个元组  可以接收0-很多个参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    return sum
print(calc())
print(calc(1,2,3))
#已有list或者tuple调用可变参数  在变量名前加*当做参数即可 *nums表示把nums这个list的所有元素作为可变参数传进去
nums=[1,2,3,4,5]
print(calc(*nums))

#关键字参数
# 支持可变长度的关键字参数(可以传入任意个数的关键字参数) 即将键值对传入 内部会将该参数封装成一个dict(Map)
def person(name,age,**kw):
    print('name=',name,'age=',age,'other=',kw)
person('小和',18,city='焦作',sex='男')
person('小和',18,city='焦作',sex='男',height=170)
#也可以直接将dict传入 这时传入的是一个值复制，对传入的参数进行修改不会改变外面的参数值
dmap={'city':'焦作','sex':'男','height':170}
person('小和',18,**dmap)

#命名关键字参数 命名关键字参数必须传入参数名，这和位置参数不同 命名关键字参数可以有缺省值
#当参数中没有可变参数 例如*nums 或 **kw关键字参数的 需要在中间加一个*作为区分  后面的必须要以键值对形式
def person1(name,age,*,city,job):
    print(name,age,city,job)

person1('小和',18,job='CXY',city='BJ')

#参数中有可变参数 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person2(name,age,*ages,city='BJ',job='YY'):
    print(name,age,*ages,city,job)
person2('小和',18,*nums,city='HN',job='CXY')

#计算多数乘积
def product(*args):
    if len(args)<=0:
        raise TypeError('参数列表不能为空')
    else:
        sum=1
        for x in args:
            sum=sum*x
        return sum
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

"""递归函数
    需要注意栈溢出
    函数调用通过栈实现的
    每进入一个函数调用栈会增加一层栈帧，函数返回栈帧减少一层，调用次数过多会导致栈溢出
"""
#计算阶乘
def fact(n):
    if n<=0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(1))
print(fact(5))
print(fact(100))

#解决栈溢出方法是尾递归优化 尾递归和循环效果相似
#尾递归 在函数返回时调用自己本身并且return语句       不能包含表达式   没有任何编译器或者解释器实现尾递归了 这个只是概念 廖大大竟然开玩笑
                            #这样解释器会将尾递归优化使它只占用一层栈帧
                            # def fact(n):
                            #     return fact_iter(n, 1)
                            #
                            # def fact_iter(num, product):
                            #     if num == 1:
                            #         return product
                            #     return fact_iter(num - 1, num * product)
                            # print(fact_iter(5,1))
                            # print(fact_iter(4,5))
                            # print(fact_iter(3,20))
                            # print(fact_iter(2,60))
                            # print(fact_iter(1,120))

#汉诺塔问题 使用递归  当盘子是奇数向
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
move(4,'A','B','C')












