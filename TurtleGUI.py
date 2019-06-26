#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#海龟绘图  绘制图形

import turtle

# 设置笔刷宽度:
turtle.width(4)

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
#     turtle.pu()
#     turtle.goto(x,y)#画笔起始起始坐标
#     turtle.pd()
#     turtle.seth(0)
#     for i in range(5):
#         turtle.fd(200)#就是forward
#         turtle.rt(144)#右转角度
# # for x in range(0,250,50):
# drawStar(0,0)

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

turtle.penup()
turtle.bk(l)
turtle.pendown()
turtle.fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = turtle.width()

    # narrow the pen width
    turtle.width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    turtle.pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    turtle.lt(s)
    turtle.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    turtle.bk(l)
    turtle.rt(2 * s)
    turtle.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    turtle.bk(l)
    turtle.lt(s)

    # restore the previous pen width
    turtle.width(w)

turtle.speed("fastest")

draw_tree(l, 4)


# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
turtle.done()