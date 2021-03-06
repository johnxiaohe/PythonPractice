#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#海龟绘图  绘制图形

import turtle

# 设置笔刷宽度:
turtle.width(4)
turtle.shape("turtle")#设置光标样式  小乌龟  默认小箭头

#circle(100)  画圆方法 100是半径
#矩形
# # 前进:
# turtle.forward(200)
# # 右转90度:
# turtle.right(90)
#
# # 笔刷颜色:
# turtle.pencolor('red')
# turtle.forward(100)
# turtle.right(90)
#
# turtle.pencolor('green')
# turtle.forward(200)
# turtle.right(90)
#
# turtle.pencolor('blue')
# turtle.forward(100)
# turtle.right(90)

#五角星
# def drawStar(x,y):
#     turtle.pu()#画笔抬起 penup
#     turtle.goto(x,y)#画笔起始起始坐标
#     turtle.pd()#画笔落下  pendown
#     turtle.seth(0)
#
#     for i in range(5):
#         turtle.fd(200)#就是forward
#         turtle.rt(144)#右转角度
# for x in range(0,250,50):
#       turtle.begin_fill()#填充颜色
#       drawStar(0,0)
#       turtle.end_fill()#结束填充颜色

#树
# 设置色彩模式是RGB:
turtle.colormode(255)

turtle.lt(90)

lv = 14
l = 120
s = 45

turtle.width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
turtle.pencolor(r, g, b)

turtle.penup()#画笔抬起
turtle.bk(l) #backward
turtle.pendown()#画笔落下
turtle.fd(l) #forward

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = turtle.width()

    # narrow the pen width 每次递归都是之前的宽度四分之三
    turtle.width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    turtle.pencolor(r % 200, g % 200, b % 200)#设置画笔颜色

    l = 3.0 / 4.0 * l#前进长度

    turtle.lt(s)#左转45度 left
    turtle.fd(l)#前进l个长度 forward

    if level < lv:#左边树叉递归
        draw_tree(l, level + 1)
    turtle.bk(l)#回退l长度 backward
    turtle.rt(2 * s)#右转90度 right
    turtle.fd(l)#前进l个长度 forward

    if level < lv:#右边树叉递归
        draw_tree(l, level + 1)
    turtle.bk(l)#backward 后退l个
    turtle.lt(s)#左转45度 left

    # restore the previous pen width
    turtle.width(w)#完了之后将画笔宽度返回至原来的宽度

turtle.speed("fastest")

draw_tree(l, 4)


# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
turtle.done()