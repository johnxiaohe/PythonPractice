#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import base64
'Base64二进制编码方法'
s=base64.b64encode(b'binary\x00string')
print(s)#b'YmluYXJ5AHN0cmluZw=='
d=base64.b64decode(s)
print(d)#b'binary\x00string'

#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
s=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s)#b'abcd++//'
us=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(us)#b'abcd--__'
ud=base64.urlsafe_b64decode(us)
print(ud)#b'i\xb7\x1d\xfb\xef\xff'

#Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等 不能用于加密
#由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
#去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数 所以去掉等号后的编码不能被四整除 余数加n=4 n就是要补足的=号
def safe_base64_decode(s):
    while len(s) % 4 > 0:
        s += b'\x3d'
    return base64.b64decode(s)
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
