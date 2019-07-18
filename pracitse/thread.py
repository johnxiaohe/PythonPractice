#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import threading,time
'多线程'

#线程模块_thread、threading,threading对_thread进行封装是高级模块
#新线程执行的代码
def loop():
    print('thread %s is running...'%threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s>>>%s'%(threading.current_thread().name,n))
        # time.sleep(1)
    print('thread %s ended.'%threading.current_thread().name)

print('thread %s is running...'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.'%threading.current_thread().name)
#任何进程会默认启动一个主线程MainThread,主进程可以启动新的线程
#threading.current_thread返回当前线程实例
#多进程中，每个变量有独自的拷贝，线程不共享 多线程中变量线程共享。所以多线程需要注意安全问题
# balance=0
# #多线程会涉及变量安全问题所以要给操作加锁
# lock = threading.Lock()
# def change_it(n):
#     global balance
#
#     balance = balance+n
#     balance = balance-n
# def run_thread(n):
#     for i in range(100):
#         #获取锁
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             #释放锁
#             lock.release()
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

'''多线程安全问题'''
class Student(object):
    def __init__(self,name):
        self.name=name
#使用局部变量 将局部变量放入dict中
global_dict={}
def do_task_1():
    #不传入std,而是根据当前线程查找
    std=global_dict[threading.current_thread()]
    std.name=std.name+'1'
def do_task_2():
    std=global_dict[threading.current_thread()]
    std.name=std.name+'2'
def std_thread(name):
    std=Student(name)
    #把std放到全局变量global_dict中
    global_dict[threading.current_thread()]=std
    do_task_1()
    do_task_2()
    print(global_dict[threading.current_thread()].name)
t1=threading.Thread(target=std_thread,args=('小和',))
t2=threading.Thread(target=std_thread,args=('小范',))
t1.start()
t2.start()
t1.join()
t2.join()
print('thread %s is ended.'%threading.current_thread().name)

#ThreadLocal实现线程安全 类似于dict
#创建全局TreadLocal对象
local_school=threading.local()
def process_student():
    #获取当前线程关联的student
    std=local_school.student
    print('Hello,%s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')#Hello,Alice (in Thread-A)
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')#Hello,Bob (in Thread-B)
t1.start()
t2.start()
t1.join()
t2.join()
#全局变量local_school就是一个ThreadLocal对象,但是它帮每个线程保存了各自的局部变量类似于dict根据自己的线程去取各自的局部变量互不干扰
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息
