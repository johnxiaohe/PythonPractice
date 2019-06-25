#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#检测字符串编码属性
import chardet

result=chardet.detect(b'Hello,world!')#检测编码
print(result)#{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
data="离离原上草，一岁一枯荣".encode("gbk")
print(chardet.detect(data))#{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data="最新の主要ニュース".encode("euc-jp")
print(chardet.detect(data))#{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}



