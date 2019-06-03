#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'分布式进程'
import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass

#只需从网络上接收对象，只需要注册对象名字即可
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，也就是运行task_master.py的机器
server_address='127.0.0.1'
print('Connect to server %s...'%server_address)
#端口和验证码要保证与主进程一致
m=QueueManager(address=(server_address,5000),authkey=b'abc')
#连接网络
m.connect()
#获取网络对象
task=m.get_task_queue()
result=m.get_result_queue()
#从task队列取任务并把结果写入result队列
for i in range(10):
    try:
        n=task.get(timeout=1)#取网络队列task里面的值
        print('run task %d * %d...'%(n,n))
        r = '%d * %d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)#处理完值之后将它放入result网络队列中
    except queue.Empty:
        print('task queue is empty.')#检测是否task队列是空的。
#处理结束
print('worker exit')
