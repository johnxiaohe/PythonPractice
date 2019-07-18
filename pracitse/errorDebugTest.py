#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging

'错误调试测试'
import logging #记录错误信息模块
#logging允许指定记录级别 debug info warning error 级别最高的是debug
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
logging.basicConfig(level=logging.INFO)
from functools import reduce
import pdb
import unittest
import doctest
'''错误处理'''
#try...except...finally   所有的错误类型都继承自BaseException 错误有向下兼容的特性，捕获父类可以将子类捕获

try:
    print("try...")
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
except RuntimeError as e: #可以捕获多个错误
    print('RuntimeError')
else:               #如果没有发生错误就会执行else  在finally之前执行
    print('no error')
finally:
    print('finally...')
print('END')

#try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用 未被捕获的错误会向上层抛出由上层处理
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
        # logging.exception(e)#打印错误栈
    finally:
        print('finally...')

main()
print('end')#捕获后后面程序会继续执行
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获,打印一个错误信息，然后程序退出
#定义错误class
class FooError(ValueError):
    pass
def foor(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s'%s)
    return
try:
    foor('0')
except FooError as e:
    print(e)
print('zuihou')
#raise语句如果不带参数，就会把当前错误原样抛出
def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        ss = s.strip()
        try:
            return int(ss)
        except ValueError as e:
            return float(ss)

def calc(exp):
    ss=exp.split('+')
    ns=map(str2num,ss)
    return reduce(lambda acc,x:acc+x,ns)
def main():
    r=calc('100+200+345')
    print('100+200+345=',r)
    r=calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6=',r)
main()

'''调试，debug'''
#断言 assert  意思是后面表达式应该为真 为假则根据逻辑后面的将会出错 断言失败程序将会抛出AssertionError
# 启动Python解释器时可以用-O(字母)参数来关闭assert 关闭后，你可以把所有的assert语句当成pass来看
# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zeror'#如果断言失败将会抛出错误并打印这句话  AssertionError: n is zeror
#     return n/0
# foo('0')

#使用logging
#logging允许指定记录级别 debug info warning error 级别最高的是debug
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
s='0'
n=int(s)
logging.info('n=%d',n)
# print(10/n)

#pdb.set_trace()  import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停  命令p 变量名 查看变量，或者用命令c继续运行
# print(10 / n)

'''单元测试'''
#单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
#编写单元测试，我们需要引入Python自带的unittest模块
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
# 编写一个测试类，从unittest.TestCase继承。
# class TestDict(unittest.TestCase):
#     # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法,测试的时候不会被执行
#     #只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()
#     #可以在单元测试中编写两个特殊的setUp()和tearDown()方法  两个方法会分别在每调用一个测试方法的前后分别被执行
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     # 期待抛出指定类型的Error   assertRaises(Error)
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
# #一种运行单元测试是下面两行，另一种方法是在命令行通过参数-m unittest直接运行单元测试
# if __name__ == '__main__':
#     unittest.main()

'''文档测试'''
#Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
#doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确  不必担心doctest会在非测试环境下执行  只有在命令行直接运行时，才执行doctest
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

