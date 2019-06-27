#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#服务器需要绑定某个端口并监听连接，如果有客户端连接了就要与之建立连接，随后这个socket就负责与该客户端的连接直至中断
import socket,threading,time

#一个socket依赖：服务器地址、服务器端口、客户端地址、客户端端口唯一来确定一个Socket
#一个连接一个进程或者线程
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9999))

#监听端口，等待连接最大数量是五个
s.listen(5)
print("Waiting for connection...")

def tcplink(sock,addr):
    print("Accept new connection from %s:%s"%addr)
    sock.send(b'Welcome')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(("Hello,%s!"%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.'%addr)

#服务器开始循环接收客户端连接，accept()会等待并返回一个客户端连接给服务器
while True:
    #接受一个新连接
    socket,addr=s.accept()
    print(addr)
    #创建线程处理TCP连接
    t=threading.Thread(target=tcplink,args=(socket,addr))
    t.start()

