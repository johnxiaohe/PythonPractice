#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import socket
#UDP传输协议
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))

#不用监听直接获取请求
print("Lisenting On 9999")
while True:
    #接收数据 recvfrom()方法返回数据和客户端的地址与端口
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s'%addr)
    #sendto()就可以把数据用UDP发给客户端
    s.sendto(b'Hello,%s!'%data,addr)
