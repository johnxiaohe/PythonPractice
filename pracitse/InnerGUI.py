#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#Python支持第三方图形界面库：Tkinter、wxWidgets、Qt、GTK

#Python自带的库是Tkinter
from tkinter import *
import tkinter.messagebox as messagebox

#定义Application类 是所有Widge的父容器
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):#窗口组件
        self.helloLable=Label(self,text='hello,world!')#
        self.helloLable.pack()
        self.quitButton=Button(self,text="Quit",command=self.quit)#Button被点击时触发 quit方法(退出)
        self.quitButton.pack()#封装

#GUI中，每个Button、Label、输入框等都是窗口组件，Frame(框架)是可以容纳其他组件的大组件
#pack()方法把组件加到Frame中，实现布局，pack()是简单的布局，可以使用grid()实现复杂的布局

#实例化Application
# app=Application()
#设置窗口标题
# app.master.title("hello,world")
#主消息循环
# app.mainloop()
#GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理

#加入文本框
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):#窗口组件
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text="Hello",command=self.hello)#Button被点击时触发 quit方法(退出)
        self.alertButton.pack()#封装
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)

app = Application()
app.master.title("Hello,World")
app.mainloop()