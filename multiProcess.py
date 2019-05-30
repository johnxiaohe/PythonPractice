#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os,time,random
from multiprocessing import Process,Pool,Queue
import subprocess
'多进程'

#fork()复制当前进程并返回子进程ID 子进程调用getppid()获取父进程ID
#os.getpid获取当前进程ID   os.getppid获取父进程ID
print('Process (%s) start...'%os.getppid())
#下面的不能运行在windows
# pid=os.fork()
# if pid==0:
#     print('I am child process (%s) and my parent is %s'%(os.getpid(),os.getppid()))
# else :
#     print('I (%s) just created a child process (%s).'%(os.getpid(),pid))

'''multiprocessing模块'''
#multiprocessing模块是跨平台版本的多进程模块
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s(%s)...'%(name,os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s'%os.getpid())
#     p=Process(target=run_proc,args=('test',))#创建子进程 参数是子进程需要执行的函数以及参数列表
#     print('Child process will start.')
#     p.start()#运行子进程
#     p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#     print('Child process end.')

'''pool'''
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
def long_time_task(name):
    print('Run task %s(%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))

# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     p=Pool(4)
#     #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')

'''进程间通信'''
# 写数据进程执行的代码:
def write(q):
    print('Process to write : %s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

#d读数据进程执行的代码
def read(q):
    print('Process to read:%s'%os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue.'%value)

if __name__=='__main__':
    #父进程创建queue并传给各个进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()