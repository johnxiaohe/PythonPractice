#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hashlib,random
'摘要算法简介'
#hashlib提供了常见的摘要算法， MD5、SHA1等
#摘要算法又称为哈希算法、散列算法 通过一个函数将任意长度的数据转换为一个长度固定的数据(通常为16进制的字符串表示)
# 生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
#摘要算法就是通过函数将数据计算出固定长度的摘要digest，防止数据被别人篡改(不可逆)
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())#d26a53750bc40b38b65a520292f69306

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的 一个括号都不能变
md51=hashlib.md5()
md51.update('how to use md5 '.encode('utf-8'))
md51.update('in python hashlib?'.encode('utf-8'))
print(md51.hexdigest())#d26a53750bc40b38b65a520292f69306

#另一种SHA1    SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
sha1=hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())#2c76b57293ce30acef38d98f6046927161b46a44


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def calc_md5(password):
    md52 = hashlib.md5()
    md52.update(password.encode('utf-8'))
    return md52.hexdigest()

def login(user, password):
    if db[user]==calc_md5(password) :
        return True
    else:
        return False
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')