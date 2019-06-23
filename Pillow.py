#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#图像处理标准库

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

#打开图像文件
im = Image.open("C:/Users/john/Pictures/timg.jpg")
#获得图片尺寸
w,h=im.size
print("Original image size:{0:.1f},{1:}".format(w,h))

#缩放
im.thumbnail((w/2,h/2))
print("Resize image to :%s,%s"%(w/2,h/2))
#保存缩放
im.save("C:/Users/john/Pictures/timg2k.jpg","jpeg")

im2=im.filter(ImageFilter.BLUR)
im2.save("C:/Users/john/Pictures/blur.jpg","jpeg")

#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#设置宽高
width=60*4
height=60

image=Image.new("RGB",(width,height),(255,255,255))#图片编码，宽高，背景色
#创建font对象
font=ImageFont.truetype("C:/Users/john/Anaconda3/Library/lib/fonts/DejaVuSans.ttf",36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素  将每个坐标点上都画上随机颜色小点点，如果不画就是白色北京了
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字  将文字输出到图片上 第一个参数定义起点位置的坐标 第二个是输出字符 第三个是字体 第四个是颜色
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊
# image=image.filter(ImageFilter.BLUR)
image.save("C:/Users/john/Pictures/code.jpg","jpeg")