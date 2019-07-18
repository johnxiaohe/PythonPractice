#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'模块创建规范' #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__='小和' #使用__author__变量把作者写进去

import sys #sys模块有一个argv变量，用list存储了  命令行      的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
            #运行python3 model.py获得的sys.argv就是['model.py']；
            #运行python3 model.py 小和获得的sys.argv就是['model.py', '小和]。
def test():
    args=sys.argv
    if len(args)==1:
        print("Hello world")
    elif len(args)==2:
        print("Hello %s!"%args[1])
    else:
        print("Too many arguments")

#在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__  执行该模块时
#在其他地方导入该model模块时，if判断将失败
#if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__=='__main__':
    test()

#类似__xxx__这样的变量是特殊变量 被直接引用 模块定义的文档注释也可以用特殊变量__doc__访问
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
#只能在模块内部使用这些函数或者变量

