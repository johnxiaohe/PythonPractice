#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'元类'


class Hello(object):
    def hello(self):
        print("Hello,world")

print(type(Hello))#<class 'type'>  Hello是一个class，它的类型就是type
h=Hello()
print(type(h))#<class '__main__.Hello'>  h是一个实例，它的类型就是class Hello

#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
#type()函数既可以返回一个对象的类型，又可以创建出新的类型
"""要创建一个class对象，type()函数依次传入3个参数：
    class的名称；
    继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。"""
#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
def fn(self,name='world'):
    print("Hello,%s"%name)
Hello = type('Hello',(object,),dict(hello=fn))#创建class
h=Hello()
h.hello()


"""元类metaclass"""
#先定义metaclass，就可以创建类，最后创建实例  可以把类看成是metaclass创建出来的“实例”
#按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
## metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
"""__new__()方法接收到的参数依次是：
    当前准备创建的类的对象 list
    类的名字               MyList
    类继承的父类集合        List
    类的方法集合  attrs"""
L=MyList()
L.add(1)
print(L)

#Field类，它负责保存数据库表的字段名和字段类型
"""元类：动态为类添加方法 并且该动作可以顺延到子类身上，所以子类也会具备该动态的执行方法 又因为多态 这些执行方法获取到的属性都是子类的"""
class Field(object):

    def __init__(self, name, column_type):#列名，列类型
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系  添加了__mappings__方法 保存k-v 列-值对
        attrs['__table__'] = name # 假设表名和类名一致      添加了__table__方法 保存表名
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass): #为Model动态添加__mappings__方法和__table__方法

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
#metaclass可以隐式地继承到子类
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    # def haha(self):  如果不加if 这个haha也会被遍历打印出来
    #     pass

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
#Found model: User   多态 调用的是User 所以name是User 充当表名
# Found mapping: id ==> <IntegerField:id>           #遍历User里面定义的属性
# Found mapping: name ==> <StringField:username>    #遍历User里面定义的属性
# Found mapping: email ==> <StringField:email>      #遍历User里面定义的属性
# Found mapping: password ==> <StringField:password>#遍历User里面定义的属性
#Found mapping: haha ==> <function User.haha at 0x000002730D0439D8>如果不加if haha也会被打印出来
# SQL: insert into User (id,username,email,password) values (?,?,?,?)
# ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']

"""在ModelMetaclass中，一共做了几件事情：

    排除掉对Model类的修改；
    
    在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
    
    把表名保存到__table__中，这里简化为表名默认为类名。"""


