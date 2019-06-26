#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import configparser as cg

#定义配置文件路径
filename='.\config.ini'

#读入配置文件
infile=cg.ConfigParser()#获取实体类
infile.read(filename,'UTF-8')#以UTF-8的格式读入配置文件

#读取db部分
print('db.ip=',infile.get('db','ip'))
print('db.port=',infile.get('db','port'))
print('db.uid=',infile.get('db','uid'))
print('db.pwd',infile.get('db','pwd'))

#读取web部分
print('web.uid',infile.get('web','uid'))
print('web.pwd',infile.get('web','pwd'))

#换个读取方式
print('web.pwd',infile['web']['pwd'])

#写入新内容
infile['web']['ip']='192.168.0.1'

with open(filename,'w') as configfile:#打开文件流
    infile.write(configfile)#将值写入打开的文件流中


