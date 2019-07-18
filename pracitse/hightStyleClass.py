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
#通过继承，子类可以扩展父类的功能  多重继承中各类的属性或方法重复，遵循取左原则
class Animal(object):#动物
    pass
class Mammal(Animal):#哺乳动物
    pass
class Bird(Animal):#鸟类
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print("Running")
class Flyable(object):
    def fly(self):
        print("Flying")
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。  多重继承中各类的属性或方法重复，遵循取左原则
class Dog(Animal,Runnable):
    pass
class Bat(Animal,Flyable):
    pass
#MixIn 重用其功能的类  如果需要“混入”额外的功能，通过多重继承就可以 实现这种设计通常称之为MixIn。
#MixIn的目的就是给一个类增加多个功能
class RunnableMixIn(object):  #只是为了使用该类的某个方法或者某些方法 而且这些方法可以通过该类被多个类继承进行使用(重用其功能)
    def run(self):
        print("Running")
class FlyableMixIn(object):
    def fly(self):
        print("Flying")

"""定制类"""
#__str__
class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('jem'))#<__main__.Student object at 0x000002209D1605C0>
#__str__类中定义该方法 打印调用类时会返回该方法返回值
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
print(Student("jem"))#jem

#直接敲变量不用print，打印出来的实例还是<__main__.Student object at 0x000002209D1605C0>
# 因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串
s = Student("jem")
print(s.__repr__())#<__main__.Student object at 0x000002618B471748>
#所以在控制台的话 要打印该实例不用print就要将__repr__也改写了，可以直接将__repr__=__str__

#__iter__ 一个类想被用于for...in循环或者类似于list、tuple一样就需要实现 它返回一个迭代对象 然后python会不断调用该迭代对象的__next__方法拿到下一个值
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self   # 实例本身就是迭代对象，故返回自己  因为它具有迭代对象的特征  __next__
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a  # 返回下一个值
for n in Fib():
    print(n)

#__getitem__  可以获取对象的某个元素  根据实现该对象可以是list dict 等
# 可以让对象有list的功能 进行定位取值
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行(不能进行定位取值)
#如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str
#__setitem__()方法，把对象视作list或dict来对集合赋值
#__delitem__()方法，用于删除某个元素
class Fib(object):
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a
f=Fib()
print(f[11])

#实现list的切片方法  __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for n in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start = item.start
            stop = item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
f=Fib()
print(f[0:5])
print(f[:10])

#__getattr__ 动态返回一个属性
#当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性 返回函数也是完全可以的
#要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
class Student(object):
    def __init__(self,name):
        self.name=name
    def __getattr__(self, item):
        if item == "score":
            return 89
        if item == 'age':
            return lambda :25
        raise AttributeError("参数不存在")
s = Student("jem")
print(s.name)
print(s.score)
print(s.age)#<function Student.__getattr__.<locals>.<lambda> at 0x0000020E9E82DD08>
print(s.age())#25

#动态生成API的SDK
class Chain(object):
    def __init__(self,path=""):
        self._path=path
    def __getattr__(self, item):
        return Chain("%s/%s"%(self._path,item))
    def __str__(self):
        return self._path
    __repr__=__str__
print(Chain().status.user.timeline.list)

#__call__ 调用实例本身
class Chain(object):
    #REST风格 API
    def __init__(self,path=""):
        self._path=path
    def __getattr__(self, item):

        # if isinstance(item,str):
            return Chain("%s/%s"%(self._path,item))
    def __call__(self, *args, **kwargs):
        return Chain("%s/%s"%(self._path,args[0]))
    def __str__(self):
        return self._path
    __repr__=__str__
c = Chain()
print(c(15))#/15
print(Chain().users('Min').repos.age(15))#/users/Min/repos/age/15    ()后面就相当于调用实例本身 只不过不能再users和('Min')中间加.了