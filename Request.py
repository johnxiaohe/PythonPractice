#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#处理URL操作的第三方库
import requests

# r=requests.get("https://www.douban.com/")#豆瓣首页
# print(r.status_code)
# print(r.text[0:30])#列表切片

#如果url有参数，传入一个dict作为参数
r=requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)#https://www.douban.com/search?q=python&cat=1001
print(r.encoding)#utf-8
#使用content属性获取byte对象
b=r.content
print(b)

#对特定类型响应
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# json=r.json()
# print(r)

#传入Header参数
r=requests.get('https://www.douban.com/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text[0:200])

#发送post请求就改用post方法
# p=requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
"""requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数"""
# params={'key':'value'}
# r=requests.post("url",json=params)# 内部自动序列化为JSON

#上传更复杂的编码格式需要使用files参数 读取文件一定要使用rb格式读取，这样读取出来的是二进制的bytes长度才是文件的正确长度
# upload_file={'file':open("C:/Users/john/Pictures/pillow/局部透明.png","rb")}
# r=requests.post("url",files=upload_file)

"""除下post和get还有put和delete方法"""

#获取响应头
# r.headers['Content-Type']#获取响应头的某个属性

#获取Cookie
# r.cookies["name"]


#请求加入cookie
# cs={'token':'12345','status':'working'}
# r=requests.get("url",cookies=cs)

"所以一共请求有 cookies、files、json、headers、params参数可以设置请求的各种属性"
