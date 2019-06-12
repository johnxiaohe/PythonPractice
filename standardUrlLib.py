#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from urllib import request,parse
#urllib提供一系列操作URL的功能

#GET urllib的request模块可以非常方便的抓取URL内容，发送一个GET请求到指定页面，返回HTTP响应
with request.urlopen('https://www.douban.com/') as f:
    data=f.read(10)
    print("Status:",f.status,f.reason)
    # for k,v in f.getheaders():
    #     print("%s,%s"%(k,v))
    print("Data:",data.decode('utf-8'))

#模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
req = request.Request('http://www.douban.com/')
#模拟iphone6
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print("Status",f.status,f.reason)
    # for k,v in f.getheaders():
    #     print("%s,%s"%(k,v))
    print("Data",f.read(10).decode("utf-8"))

#POST
#模拟发送post请求需要把参数data以bytes形式传入
#模拟微博登录
# print("Login to weibo.cn...")
# email=input("Email:")
# password=input("Password:")
# login_data=parse.urlencode([
#     ('username', email),
#     ('password', password),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req=request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

#Handler 代理
#通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
# proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass

#User-Agent头就是用来标识浏览器的
import json
#利用urllib读取JSON，然后将JSON解析为Python对象：
def fetch_data(url):
    with request.urlopen(url) as f:
        data=f.read()
        data_str=data.decode('utf-8')
    return json.loads(data_str)

# 测试
URL = 'https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

'''XML'''

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)