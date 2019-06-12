#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#读写文件资源需要使用try...finally
# try:
#     f=open('/path/to/file','r')
# finally:
#     if f:
#         f.close()

#with可以让我们不用担心资源关闭操作
# with open('/path/to/file','r') as f:
#     f.read()

#实现上下文管理的对象均可以使用with
#通过__enter__和__exit__方法实现上下文管理(即自动帮你开始执行enter方法结束执行exit方法)
class Query(object):
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print("上下文管理执行进入方法")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error")
        else :
            print("End")
    def query(self):
        print("执行主体内容对于:%s"%self.name)

with Query('Bob') as q:
    q.query()

#使用@contentmanager简化__enter__和__exit__
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print("Begin")
    q=Query(name)
    yield q#这个q是__enter__的返回值
    print("End")
#@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
with create_query("Bob") as q:
    q.query()

#希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    t=name
    yield t#返回可调用的参数
    print("</%s>" % name)
#with语句首先执行yield之前的语句，因此打印出<h1>；
#yield调用会执行with语句内部的所有语句，因此打印出hello和world；
#最后执行yield之后的语句，打印出</h1>。
with tag("h1") as t :
    print("hello",t)
    print("world",t)

#@closing 修饰对象必须要有close方法
#closing对象，这个对象就是一个上下文管理器，它的__exit__函数仅仅调用传入参数的close函数
#如果一个对象没有实现上下文就不能用于with语句 可以使用closing()把对象变为上下文对象 例如urlopen()
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

#closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()