#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from functools import reduce
import time
import functools
#高阶函数
#函数可以赋值给变量，函数名本身就是变量指向函数的位置  可以将函数名指向其他地方 所以不要将函数名作为变量名使用
f=abs
print(f(-10))

#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add (x,y,f):
    return f(x)+f(y)
print(add(-5, 6, abs))


#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x**2
r=map(f,[1,2,3,4,5,6])
print(list(r))
print(list(map(str,[1,2,3,4,5,6])))

#reduce() 把函数作用在[x1, x2, x3, ...]序列上 函数必须接受两个参数 reduce会拿函数结果和序列的下一个元素继续调用该函数直至结束
#reduce(f,[x1,x2,x3])相当于f(f(f(x1,x2),x3),x4)
def add(x,y):
    return x*10+y
print(reduce(add,[1,2,3,4,5]))

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
#将字符串转化为数字
L=reduce(add,map(char2num,'13579'))
print(L)
#upper转换大写  lower转换小写  str也可以这样使用 后面切片 最后再拼接到一起
def sw(s):
    return s[0].upper()+s[1:-1].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(sw, L1))
print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def mm(s,x):
        return s*x
    return reduce(mm,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):

    # n=s.index('.')
    a,b=s.split('.')
    it=reduce(lambda x,y:x*10+y,map(int,a))
    ft=reduce(lambda x,y:x*10+y,map(int,b))/pow(10,len(b)) #pow 返回x的y次方
    return it+ft

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


#filter 接收一个函数和一个序列 函数依次作用每个元素，根据返回值是True还是False决定保留还是舍弃该元素
# filter()函数返回的是一个Iterator
def is_odd(n):
    return n%2==1
L=list(filter(is_odd,[1,2,3,4,5,6,7,8,9,0]))
print(L)

def not_empty(n):
    return n and n.strip()
L=list(filter(not_empty,['A','B',None,'C','']))
print(L)

#用filter求素数
def _odd_iter():  #一个从3开始的奇数序列生成器
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0 #返回的是 lambda x:x%n>0 这个匿名函数
def primes():
    yield 2
    it = _odd_iter()#初始序列
    while True:
        n=next(it)  # 返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it) # 构造新序列  相当于filter(lambda x: x%n>0 ,it)   这时的n是确定值，由上面传下来的

for n in primes():
    if n < 100:
        print(n)
    else:
        break

print('筛选回数')
#筛选回数
def is_palindrome(n):
    s=str(n)
    return s==s[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


#排序算法 sorted()
print(sorted([36, 5, -12, 9, -21]))
#sorted() 可以接收一个函数进行自定义排序
print(sorted([36, 5, -12, 9, -21],key=abs))  #按照绝对值大小排序
#sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#对字符串排序是按照ASCLL大小比较的， 如果想要忽略大小写就将他们先统一大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#设置反向排序参数
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#用sorted()对上述列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score,reverse=True)
print(L3)

#函数可以返回值 函数也可以返回回去 因为函数也相当于变量
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,3,4,5,6)
#当调用该方法时 执行的是返回回来的sum方法 返回的函数并没有立刻执行，而是直到调用了f()才执行
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数称为“闭包（Closure)
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数： 即两次调用的方法都是新建出来的不是之前的方法循环利用
print(f())

#闭包   返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs=[]
    #range(x,y) 前闭后开
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
        #fs里面存放的是三个f函数返回回去的
    return fs
#，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
f1,f2,f3=count() #将返回的列表赋值给这三个
print("还未调用")
print(f1())#9
print(f2())#9
print(f3())#9  因为这三个调用的时候i都是循环到3了

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：  保持当前返回函数的参数值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))#这时返回的时候 I值记录到函数中是固定的
    return fs
f1,f2,f3=count()
print(f1())#1
print(f2())#4
print(f3())#9  要想变量固定需要再借助一个函数 将变量固定住

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    i = [0]
    def counter():
        i[0]=i[0]+1
        return i[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#匿名函数 lambda x : 表达式  键字lambda表示匿名函数，冒号前面的x表示函数参数  匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f=lambda x:x%2
print(f(5))
#返回匿名函数
def build():
    return lambda x:x**2
f=build()
print(f(5))


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L)


"""装饰器  decorator就是一个返回函数的高阶函数   执行完自己的函数就执行返回的装饰函数"""
#函数的方法_name_返回函数名称
# def now():
#     print("now被调用了")
# print(now.__name__)

#我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(function):
    def wapper(*args,**kwargs):
        print("即将调用 %s()方法"% function.__name__)
        return function(*args,**kwargs)
    return wapper

@log
def now():
    print("now()被调用了")
#执行   相当于在执行前加了一层动态代理了 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：、
#原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
now()

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(function):
        def wrapper(*args,**kwargs):
            print("%s %s():"%(text,function.__name__))
            return function(*args,**kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print("now又被执行了")

now()

print(now.__name__) #返回的是wrapper now被赋值成为wapper了  然后wapper又调用了now之前的函数

def metric(fn):
    def wapper(*args,**kwargs):
        start = time.time()
        print("123")
        res = fn(*args,**kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return res
    return wapper

# 测试
@metric
def fast(x, y):  #想要传参数 只需要在调用方法里面传参数就好了
    time.sleep(0.0012)
    print("fast")
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    print("slow")
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else :
    print("测试成功")

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args,**kwargs):
            print("begin call")
            kfc = func(*args,**kwargs)
            print("end call")
            print(text)
            return kfc
        return wapper
    return decorator

@log("执行该方法完毕")
def pt(x,y):
    print(x+y)
pt(1,2)
print(pt.__name__) #@functools.wraps(func) 将该方法的名字属性继续赋值给wapper 不然返回的名字将会是wapper 因为装饰器操作其实是将函数指向wapper 然后wapper内部执行了该方法

"""偏函数"""
#function模块的偏函数Partial function
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是重新设置默认值），返回一个新的函数，调用这个新函数会更简单。
#将函数的默认值修改生成新函数并赋值给一个变量
int("123",base=10)#int类型默认base是十 将字符串转换成十进制数
int("123",base=8)#输入八进制数 将字符串按八进制数转化成十进制
int2=functools.partial(int,base=2)#使用functools的片函数partial 将函数int的base默认值重新设置为2生成的新函数 赋值给int2
i=int2("10")
print(i)#输入2进制数 输出十进制2
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数


