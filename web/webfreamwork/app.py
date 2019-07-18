#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""GET /：首页，返回Home；

GET /signin：登录页，显示登录表单；

POST /signin：处理登录表单，显示登录结果。"""

from flask import Flask
from flask import request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_from():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    #从request对象中获取表单内容
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='admin':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password ',username=username)

if __name__=="__main__":
    app.run()
