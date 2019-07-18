#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#python中的正则表达式功能模块
import re

'正则表达式'
#正则表达式是用来匹配字符串的：用描述性语言给字符串定义一个规则(standard),符合规则的字符串就是合法的匹配的

'''正则表达式规则'''
#如果直接给出字符就是精准匹配，只能是该字符
#\d匹配一个数字  \w匹配一个字母或者数字（一个哦！！！）
#\s匹配一个空格(包括Tab等空白符)
#. 可以匹配任何字符
#特殊字符，在正则表达式中，要用'\'转义 例如 _ 需要 \_

'''匹配变长字符'''
# * 表示任意个字符(包括0个)
# + 表示至少一个字符
# ? 表示0或1个字符
# {n} 表示n个字符
# {n,m} 表示n至m个字符

'''正则进阶'''
#使用[]表示范围
#[0-9a-zA-Z\_]可以匹配一个数字、字母或下划线
#[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串 例如 'a100' '0_z' 'py300'
#[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或者下划线开头，后面接任意个由字母数字下划线开头组成的字符串
#[a-zA-Z\_][0-9a-zA-Z\_]{0,19}限制变量长度为1-20个字符
#A|B 可以匹配A或者B  例如(P|p)ython 可以匹配‘Python'或者'python'
# ^ 表示行的开头  ^\d表示必须以数字开头 ^[\d+] 以不少于一个数字开头  表示数量的在里面  表示强制定义的在外面
# $ 表示行的结束 \d$表示必须以数字结束  [\d+]$ 以不少于一个数字结尾





'''re模块的使用'''

print(re.match(r'^\d{3}\-\d{3,8}$','854-123456'))#<_sre.SRE_Match object; span=(0, 10), match='854-123456'>匹配成功返回Match对象 匹配错误返回None

#切割字符串
print(re.split(r'[\s,;]+','a ,;;  b  ,,,;    c'))#['a', 'b', 'c']

'''分组'''
#正则表达式还有提取子串的功能，()表示要提取的分组(Group)
#^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取区号和本地号码
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
#如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串  group(0)是原字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))

#识别时间
t='19:05:30'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
print(m.groups())#('19', '05', '30')

'''贪婪匹配'''
#正则表达式默认是贪婪匹配，意思是尽可能的匹配更多的字符
#举例如下， 本来应该分割开最后很多个0才对 但是贪婪匹配会将它全部匹配到第一个组里
m=re.match(r'^(\d+)(0*)$','102300').groups()
print(m)#('102300', '')
#使用?采用非贪婪匹配
m=re.match(r'^(\d+?)(0*)$','102300').groups()
print(m)#('1023', '00')

#预编译正则表达式
#如果一个正则表达式需要反复使用，那就不能每次都调用re进行编译正则表达式再匹配会影响效率占用资源所以需要对正则表达式进行预编译
#预编译
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
print(re_telephone.match('010-123456').groups())#('010', '123456')

re_telephone=re.compile(r'^[a-zA-Z._*#$]+@(gmail|microsoft|example|qq)(.com)$')
def is_valid_email(addr):
    if re_telephone.match(addr) ==None:
        return False
    return True
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


re_telephone=re.compile(r'^[<?]([\w\s]+)[>?]@(\w)+\.\w+$')
def name_of_email(addr):
    n = re.match(r'^[<]?([\w\s]*)[>]?[\w\s]*\@([\w\.]+)$', addr)
    return n[1]

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
















