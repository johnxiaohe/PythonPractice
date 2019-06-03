#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'集合的内建模块'
from collections import namedtuple,deque,defaultdict,OrderedDict,ChainMap,Counter
import os,argparse
#命名元组 成为一个nametuple类型
Point = namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)#1
print(p.y)#2
print(isinstance(p,Point))#True
print(isinstance(p,tuple))#True

'''deque'''
#list是线性存储，按索引访问很快，插入删除很慢
#deque是双向列表 适用于队列和栈 插入删除快
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)#deque(['y', 'a', 'b', 'c', 'x'])
q.pop()#删除队尾
print(q)#deque(['y', 'a', 'b', 'c'])
q.popleft()#删除队头
print(q)#deque(['a', 'b', 'c'])

'''defaultdict'''
#dict如果key不存在会抛出KeyError  使用defaultdict如果key不存在可以返回一个默认值
#默认值是一个函数返回的，该函数在创建defaultdict的时候传入
dd=defaultdict(lambda :'N/A')
dd['Key1']='abc'
print(dd['Key1'])#abc
print(dd['Key2'])#N/A

'''有序dict ： OrderedDict'''
#dict的key是无序的 ，OrderedDict是有序的（按照插入顺序排序）
d=dict([('a',1),('b',2),('c',3)])
print(d)#{'a': 1, 'b': 2, 'c': 3}
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)#OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#使用orderedDict实现一个先进先出的dict，当容量超出限制时删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity=capacity
    def __setitem__(self, key, value):
        #该key是否在dict中存在 存在就1 不存在就0
        containsKey =1 if key in self else 0
        #当前的长度再加上要设置的key是否大于创建的dict长度，大于就删除最前一个 如果last=True就是删除最后一个(可以利用这个创建排行榜)
        if len(self)-containsKey >=self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:#如果key存在在dict中就更新该key的value值
            del self[key]#删除该key对其value的引用(将该value的地址删掉，此时该key无引用但是在dict中还存在该key)
            print('set:',[key,value])
        else:#否则就添加该key
            print('add',(key,value))
        OrderedDict.__setitem__(self,key,value)#进行添加或者更新操作key
od=LastUpdatedOrderedDict(3)
od['1']=1
od['2']=2
od['3']=3
print(od)
od['4']=4
print(od)
od['4']=5
print(od)

'''ChainMap'''
#把一组dict串起来组成逻辑上的dict，查找的时候会按照顺序在内部的dict依次查找
#构造缺省参数
defaults={
    'color':'red',
    'user':'guest'
}
#构造命令行参数
parser=argparse.ArgumentParser()#创建命令行参数
parser.add_argument('-u','--user')#如果-u就是user的值
parser.add_argument('-c','--color')#-c就是color的值
namespace=parser.parse_args()
command_line_args={k:v for k,v in vars(namespace).items() if v}#命名空间参数构造

#组合成ChainMap     先命令行为主 然后找环境变量 最后才是默认值(将多个dict组合成一个逻辑上的dict，优先从第一个dict中找值)
combined=ChainMap(command_line_args,os.environ,defaults)

#打印参数
print('color=%s'%combined['color'])
print('user=%s'%combined['user'])

#Counter是一个简单的计数器
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)#Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
