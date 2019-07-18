#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
from datetime import datetime,timedelta,timezone
#获取当前的日期和时间
now = datetime.now()
print(now)
#获取指定的日期和时间  可以构建超前时间
dt = datetime(2019,11,11,11,11,11)
print(dt)

'''datetime转换为timestamp'''
#timestamp是相对于1970年1月1日0时0分0秒的秒数  如果有小数位，小数位表示毫秒数
dt=dt.timestamp()
print(dt)#1573441871.0

'''timestamp转换为datetime'''
dt=datetime.fromtimestamp(dt)
print(dt)#2019-11-11 11:11:11

#转换为标准时区的时间不是东八区
dt=dt.timestamp()
dt=datetime.utcfromtimestamp(dt)
print(dt)#2019-11-11 03:11:11

'''str转换为datetime'''
#转换后的datetime时区信息
sday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(sday)

'''datetime转换为str'''
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))#Sun,Jun 02 14:54 2019年六月2号 周日

'''datetime加减'''
#日期加减就是获取向前或者向后的日期，可以直接用+-运算符 导入timedelta类
now=datetime.now()
print(now)#2019-06-02 15:00:24.711637
now=now+timedelta(hours=10)
print(now)#2019-06-03 01:00:24.711637
now=now-timedelta(days=1)
print(now)#2019-06-02 01:00:24.711637
now=now+timedelta(days=1,hours=10,minutes=10,seconds=2)
print(now)#2019-06-03 11:10:26.711637

'''本地时间转换为UTC时间'''
#datetime类型有一个时区属性tzinfo默认为None，所以无法获知该datetime是哪个时区，除非给tzinfo强行设置一个时区
tz_utc_8=timezone(timedelta(hours=8))#创建时区UTF+8:00
print(tz_utc_8)
print(type(tz_utc_8))
now=datetime.now()
dt=now.replace(tzinfo=tz_utc_8)
print(dt)#2019-06-02 15:12:56.001033+08:00

'''时区转换'''
#使用utcnow()拿到当前utc时间，再转换其他时区时间
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)#2019-06-02 07:12:56.001033+00:00
#转换为北京时间
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)#2019-06-02 15:12:56.001033+08:00
#转换为东京时间
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)#2019-06-02 16:12:56.001033+09:00
#北京时间转换为东京时间
tokyo_dt=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)#2019-06-02 16:12:56.001033+09:00
#时区转换在于拿到当前时区的datetime然后设置其正确时区作为基准再通过astimezone转换至其他时区

def to_timestamp(dt_str, tz_str):
    now=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    print(now)
    t=re.match(r'^UTC((\+|\-)(\d+)):(\d+)$', tz_str)
    print(t)
    now=now.replace(tzinfo=timezone(timedelta(hours=int(t.group(1)))))
    return datetime.timestamp(now)


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')


