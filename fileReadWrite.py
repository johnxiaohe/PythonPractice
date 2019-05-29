#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from io import StringIO,BytesIO
import os#进行操作系统文件操作
import pickle
import json
'文件读写'
#file-like Object
'''读文件'''
#open()函数，传入文件名和标识符 r表示读
try:
    f=open('c:\\mywin32pc_log.txt','r')#打开该文件 默认读取文本文件并且是UTF-8格式编码的
    print(f.read())  # 一次读取文件全部内容，读到内存中并用一个str对象表示
except IOError as e:#如果文件不存在，open()函数就会抛出一个IOError的错误
    print(e)
finally:
    if f!=None:
        f.close()#使用完关闭文件
#Python引入了with语句来自动帮我们调用close()方法
# 调用read(size)方法，每次最多读取size个字节的内容
with open('c:\\mywin32pc_log.txt','r') as f:
    print(f.read(36))
#readline()可以每次读取一行内容
with open('c:\\mywin32pc_log.txt','r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
#readlines()一次读取所有内容并按行返回list
with open('c:\\mywin32pc_log.txt','r') as f:
    print(f.readlines().__len__())

#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
f=open('c:\\mywin32pc_log.txt','rb')
print(f.read())
f.close()

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f=open('c:\\mywin32pc_log.txt','r',encoding='gbk')
print(f.read(36))
f.close()
#如果编码不规范，可能会报UnicodeDecodeError open还有errors参数直接忽略errors='ignore'

'''写文件'''
#open()函数传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）
#传入'a'以追加（append）模式写入
f=open(r'C:\Users\john\python.txt','w')
f.write('第一行')
f.close()

with open(r'c:\Users\john\python.txt','a') as f:
    f.write('追加\n')#换行
    f.write('第二行\n')
    f.writelines('''第三行
第四行
第五行''')#writelines将字符原样输出

#StringIO 在内存中读写str
f=StringIO()
f.write('Hello')
print(f.getvalue())#getvalue()方法用于获得写入后的str
f.close()

#BytesIO操作二进制数据 实现了在内存中读写bytes
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.read())
print(f.getvalue())
f.close()
# f.seek(0) #解决方法：用seek将指针归零
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))
f.close()

f=StringIO('')
f.write('abc')
print(f.read()) #返回'' 因为write已经使指针发生了移动让指针移到c的后面
print(f.getvalue()) #返回'abc' 因为getvalue不受指针影响
f.seek(2) #解决方法：用seek(index)将指针归到index的位置
print(f.read()) #返回'abc'
f.close()

#打印操作系统类型
print(os.name)#posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统  要获取详细的系统信息，可以调用uname()函数  uname()函数在Windows上不提供

#在操作系统中定义的环境变量，全部保存在os.environ这个变量中
print(os.environ)
print(os.environ.get('JAVA_HOME'))#C:\Program Files\Java\jdk1.8.0_121  读取某一个环境变量
print(os.environ.get('x', 'default'))#没有就调用默认

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
#查看当前目录的路径
print(os.path.abspath('.'))#C:\workspace\python\pracitse
#在某个目录下创建一个新的目录,下面是拼接目录  把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
path = os.path.join('C:\workspace\python','python')
print(path)
# os.mkdir(path)#创建目录
# os.remove(path)#删除目录
#拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split(r'c:\Users\john\python.txt'))#('c:\\Users\\john', 'python.txt')
#os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext(r'c:\Users\john\python.txt'))#('c:\\Users\\john\\python', '.txt')
#对文件重命名
# os.rename(r'c:\Users\john\python.txt','python.py')

#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(r'C:\workspace')])

'''序列化'''
#把变量从内存中变成可存储或传输的过程称之为序列化 Python中叫pickling  其他语言中也被称之为serialization，marshalling，flattening等等
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
#把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
#Python提供了pickle模块来实现序列化

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))#b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
# 用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f=open(r'c:\Users\john\python.txt','wb')
pickle.dump(d,f)
f.close()

#要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
#也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f=open(r'c:\Users\john\python.txt','rb')
print(pickle.loads(f.read()))
f.seek(0)
print(pickle.load(f))
f.close()

#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
d = dict(name='Bob', age=20, score=88)
#dumps()方法返回一个str，内容就是标准的JSON
print(json.dumps(d))
#dump()方法可以直接把JSON写入一个file-like Object
#JSON反序列化为Python对象，用loads()JSON的字符串反序列化，load()方法从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print()
print(type(json.loads(json_str)))#<class 'dict'>

#序列化class
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
#Student实例首先被student2dict()函数转换成dict再被顺利序列化为JSON：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
#下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
#class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
print(json.dumps(s, default=lambda obj: obj.__dict__))
#果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))#__main__.Student object at 0x0000022E02647080>

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)#{"name": "\u5c0f\u660e", "age": 20} 对中文进行了编码
s = json.dumps(obj, ensure_ascii=False)
print(s)#{"name": "小明", "age": 20} 不对中文进行编码
