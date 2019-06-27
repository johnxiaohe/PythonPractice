#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#Socket表示“打开了一个网络链接”
#打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可
import socket

#创建一个 socket  AF_INET指定使用IPv4协议 SOCK_STREAM指定使用面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接  web服务端口号是80  SMTP邮件端口号是25 FTP服务是21端口
# s.connect(('www.sina.com',80))
s.connect(('127.0.0.1',9999))

#发送请求
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# #接收数据
# buffer = []
# while True:
#     #每次最多接收1k字节
#     d=s.recv(1024)
#     if d :
#         buffer.append(d)
#     else :
#         break;
#
# data=b''.join(buffer)

#分离头和内容
# header,html=data.split(b'\r\n\r\n')
# print(header.decode('utf-8'))

#把数据写入文本
# with open('sina.html','wb') as f:
#     f.write(html)

'''客户端'''
#输出欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Marry',b'Jack',b'Tom']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')

s.close()

