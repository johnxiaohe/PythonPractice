#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from types import MethodType
#面向对象高级特性

#定义一个class之后 可以给该class绑定任何属性 动态语言的灵活特性
class Student(object):
    pass

s=Student()
s.name = "jem"
print(s.name)
del s.name  #这会删除该类的name属性
#print(s.name)#会报错  没有该属性'Student' object has no attribute 'name'

#方法其实也是变量可以赋值给变量 所以可以将方法绑定到对象上面  但是只是给该实例绑定方法和属性 对其他实例的对象是没有作用的
def set_age(self , age):
    self.age = age  #会给对象绑定age属性
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

#想要让所有的该类对象都有绑定的方法 可以给该类绑定 这样所有该类的实例都可以调用被绑定的方法
d = Student()

def set_score(self,score):
    self.score = score
Student.set_score = set_score

d.set_score(89)#当然要在给该class绑定方法之后再调用在之前调用会出错的
print(d.score)

"""使用__slots__"""
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ("name","age")#使用tuple元组定义允许绑定的属性名称
s = Student()
s.name="jem"
s.age=18
# s.score=89#'Student' object has no attribute 'score' 使用__slots__限制属性之后 就不能对实例自由绑定属性了
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student):
    pass
g= GraduateStudent()
g.score = 89#不会报错
print(g.score)

#对类属性进行限制
#Python内置的@property装饰器就是负责把一个方法变成属性调用的 将该方法声明为一个属性
class Derector(object):
    @property  #把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):
        return self._score  #这个前面的下划线一定要加的 表示该属性为私有的

    @score.setter #此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer")
        if value<0 or value >100:
            raise ValueError("score must between 0~100")
        self._score = value

s = Derector()
s.score = 89# OK，实际转化为s.set_score(60)
print(s.score)

#定义只读属性，只定义getter方法不定义setter方法就是一个只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2019-self._birth
s = Student()
s.birth=1996
print(s.birth)
print(s.age)

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

"""多重继承"""
