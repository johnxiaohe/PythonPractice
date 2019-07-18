#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#单引号双引号三引号的区别
#单引号和双引号的作用差不多 单行显示 以及为了让另一种引号可以在字符串中显示出来的 当字符串中两种引号都有可以\转义他 当内部成对时无所谓 不成对时需要加\转义
s='He sayed : "I\'m fine" '
print(s)
s="He sayed: I'm fine"
#三引号 多行显示 单三引号 双三引号和上面的规避规则一样 换行避免引号相同的错误
s="""He sayed : "I am fine"
"""
print(s)

s="%d,%s,%.1f"%(1,'字符串',13.14)
print(s)
s="{0},字符串format格式书写,{1:.1f},{2:s}".format("好了",13.141,"完毕")
print(s)


