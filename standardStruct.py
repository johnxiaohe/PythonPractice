#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import struct , base64
'解决字节和二进制转换'

s=struct.pack('>I',10240099)
print(s)#b'\x00\x9c@c'
#pack的第一个参数是处理指令，'>I' >表示字节顺序是big-endian即网络序 I表示4字节无符号整数，参数个数要和指令一致

d=struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
print(d)#(4042322160, 32896)
#I为4字节无符号整数，H是2字节无符号整数

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
s=struct.unpack('<ccIIIIIIHH',s)
print(s)#(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    bmp_data=data[:30]
    s=struct.unpack('<ccIIIIIIHH',bmp_data)
    print(s)#(b'B', b'M', 616, 0, 54, 40, 28, 10, 1, 16)
    if s[1] == b'M':
        print('是位图')
        return {
            'width': s[6],
            'height': s[7],
            'color': s[9]
        }

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')