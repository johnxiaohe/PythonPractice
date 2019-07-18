#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#图像处理标准库

from PIL import Image,ImageFilter,ImageDraw,ImageFont,ImageGrab
import random,time

#打开图像文件
im = Image.open("C:/Users/john/Pictures/timg.jpg")
#获得图片尺寸
w,h=im.size
print("Original image size:{0:.1f},{1:}".format(w,h))

#缩放
im.thumbnail((w/2,h/2))
print("Resize image to :%s,%s"%(w/2,h/2))
#保存缩放
im.save("C:/Users/john/Pictures/pillow/timg2k.jpg","jpeg")

im2=im.filter(ImageFilter.BLUR)
im2.save("C:/Users/john/Pictures/pillow/blur.jpg","jpeg")

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
image.save("C:/Users/john/Pictures/pillow/code.jpg","jpeg")

#屏幕抓取
print("等待两秒")
time.sleep(2)
#全屏抓取
ImageGrab.grab().save("C:/Users/john/Pictures/pillow/截屏.jpg")
print("抓屏完毕")

#指定范围抓取
img = ImageGrab.grab(bbox=(0,100,100,200))#前面两个是左上角坐标，后面两个是右下角坐标
img.save("C:/Users/john/Pictures/pillow/box.jpg")

#打开图片
im_rgb=Image.open("C:/Users/john/Pictures/pillow/截屏.jpg")

#半透明百分之五十（128/255）
im_rgba=im_rgb.copy()
im_rgba.putalpha(128)
im_rgba.save("C:/Users/john/Pictures/pillow/半透明.png")

#形状透明
im_a = Image.new("L",im_rgb.size,255)#白色区块
draw=ImageDraw.Draw(im_a)#实例化im_a的画笔
draw.rectangle((200,100,300,200),fill=0,outline=0)#fill=黑色（透明） outlin=无边框 画出该矩形
im_rgbb=im_rgb.copy()
im_rgbb.putalpha(im_a)
im_rgbb.save("C:/Users/john/Pictures/pillow/局部透明.png")
#打开外部查看器
im_rgbb.show()



