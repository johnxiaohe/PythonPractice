#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'分布式进程'

import random,time,queue
from multiprocessing.managers import BaseManager

#线程和进程中应该先选择进程，进程还可以分布到多台机器上，但是线程只能分布到同一台机器的多个CPU上
#multiprocessing的managers子模块支持把多进程分布到多台机器上。通过网络通信，一个服务进程可以作为调度者，将任务分布到其他多个进程中

#发送任务的队列
task_queue=queue.Queue()
#接收结果的队列
result_queue=queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue
def getresult():
    return result_queue
def test():
    #把两个Queue都注册到网络上，callable参数关联了Queue对象
    ##windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    QueueManager.register('get_task_queue',callable=gettask)
    QueueManager.register('get_result_queue',callable=getresult)

    #绑定端口5000，设置验证码‘abc’
    ##绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地  authkey是两台机器通信的秘钥
    manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    #启动Queue
    manager.start()
    #获得通过网络访问的Queue对象  必须这样先获取再操作 不可以用上面定义好的  因为这是封装好的网络对象
    task=manager.get_task_queue()
    result=manager.get_result_queue()

    # 注册任务
    for i in range(10):
        n=random.randint(0,10000)
        print('Put task %d...'%n)
        task.put(n)#循环十次将结果放入task网络队列中
    #从result队列读取结果
    print('Try get results...')
    for i in range(10):
        # 延迟十秒等worker那边处理完塞入结果再取 如果没有启动worker这边结果队列将是空的
        r=result.get(timeout=10)
        print('Result:%s'%r)
    #关闭
    manager.shutdown()
    print('master exit')
#另一个是task_worker.py

if __name__ == '__main__':
    #windows下多进程可能会炸，添加这句可以缓解
    # freeze_support()
    test()#将关于网络分布的放入main下面不然会报错
