#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from web.webtest.hello import application
from wsgiref.simple_server import make_server

httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')

if __name__=='__main__':
    #监听HTTP请求
    httpd.serve_forever()
