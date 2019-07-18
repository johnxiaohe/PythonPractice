#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'类定义'

#class关键字用来定义类 类名以大写字母开头 (object)表示继承关系说明该类是从哪个类继承的  类是模板，实例是根据类创建出来的对象
class Student(object):
    pass
bart = Student()
print(bart)

print(Student)

#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
bart.name='bali'
print(bart.name)

#类可以起到模板的作用 可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
#__init__方法的第一个参数永远是self，表示创建的实例本身  在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数
#object表示该Student是继承自object
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
bart = Student('小和',89)
bart.__init__("小张",779)
print("%s的分数是%d"%(bart.name,bart.score))

#要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__  实例的变量名以__开头就是私有属性
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print("%s,%s"%(self.__name,self.__score))
bart = Student("小和",89)
bart.print_score()
# print(bart.__name)#这里会报错 说没有该属性
#内部的__name变量已经被Python解释器自动改成了_Student__name
print(bart._Student__name)#不建议，因为本身就是不想让你访问

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

"""继承"""
class Animal(object):
    def run(self):
        print(self.__class__.__name__)
class Dog(Animal):
    pass
class Cat(Animal):
    pass
#子类获得了父类的全部功能
dog = Dog()
dog.run()
cat = Cat()
cat.run()
#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()， 继承的另一个好处：多态。
#于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
def Timer(object):
    def run(self):
        print("这样也可以调用run方法")

#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#判断对象类型，使用type()函数 可以传入 变量、基本类型、对象
print(type(dog))#<class '__main__.Dog'>  返回对应的Class类型
#子类可以是父类 但是父类不是子类

print(isinstance([1, 2, 3], (tuple)))#不是tuple
print(isinstance([1, 2, 3], (list, tuple)))#是list或tuple
#获得一个对象的所有属性和方法，可以使用dir()函数 返回一个包含字符串的list  是它的方法
print(dir('ABC'))#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#len()函数内部，它自动去调用该对象的__len__()方法 __len__方法返回长度 自定义的函数想要使用len()就要自定义__len__方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))
#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态  对象有无该属性，设置和得到该属性
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x**2
obj = MyObject()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404
print(hasattr(obj, 'power')) # 有方法'power'吗？
fn = getattr(obj, 'power') # 获取方法'power'
print(fn)
print(fn())

class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count = Student.count+1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
