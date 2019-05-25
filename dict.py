#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#内置字典  也叫map使用键值对存储K-V 查找速度快
# dict内部存放的顺序和key放入的顺序是没有关系的。 无序的  通过key计算位置的算法称为哈希算法（Hash）。
#dict的key必须是不可变对象。
#list实现 list使用[]括起来  不可变list(元组) 使用()小括号括起来
names=['xh','xl','xw']
scores=[95,75,85]
#dict(map)使用{}括起来
d={'xh':95,'xl':75,'xw':85}
for name in names:
    print('%s的成绩是%d'%(name,d[name]))
d['xm']=60
print(d['xm'])
#多次赋值同一个key 会替换原值
d['xm']=50
print(d['xm'])

print('xh是否在dict中:','xh'in d)
print('xy是否在dict中','xy'in d)
#get() 获取指定的值 不存在返回None 或者自己指定的值
print(d.get('xm'))
print(d.get('xy'))
print(d.get('xy',0))
#弹出该值 删除掉
print(d)
d.pop('xm')
print(d)