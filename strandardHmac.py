#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hmac,random
'Hmac算法'
#传入的key和message都是bytes类型，str类型需要首先编码为bytes
message=b'Hello,world!'
key=b'secret'
h=hmac.new(key,message,digestmod='MD5')
#如果消息很长可以多次调用h.update(s)
print(h.hexdigest())#21db988f124ebc9fade5492afb9df52d

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
