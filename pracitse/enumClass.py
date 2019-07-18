#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'枚举类'
from enum import Enum , unique

#当需要定义常量时，使用大写变量进行整数定义 但是只能是整数int类型而且只是约定俗成的是常量 还可以更改
NUM=10

#为枚举类型定义一个class类型，每个常量都是class的唯一实例
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
#如上就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员 value默认从1开始赋值
print(Month.Jan.value)
for name,member in Month.__members__.items():
    print(name,'=>',member,';',member.value)

#@unique装饰器检查没有重复值
@unique
class WeekDay(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

print(WeekDay.Sun.value)
print(WeekDay['Tue'].value)
print(WeekDay(1).value)
for name,member in WeekDay.__members__.items():
    print(name,'=>',member,';',member.value)
#把Student的gender属性改造为枚举类型，可以避免使用字符串
class Gender(Enum):
    Male=0
    Female=1
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
