#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#获取系统信息的第三方模块
import psutil

#在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
# 要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码


"""所以要使用第三方模块psutil"""
print(psutil.cpu_count())#cpu逻辑数量
print(psutil.cpu_count(logical=False))#物理核心

#统计CPU用户/系统/空闲时间
print(psutil.cpu_times())#scputimes(user=73658.890625, system=39189.734375, idle=651311.9375, interrupt=2673.984375, dpc=1193.6875)

#实现类似于top命令的cpu使用率 每秒刷新一次，累计10次  显示当前cpu使用率
# for x in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))

#获取内存信息
#使用psutil获取物理内存以及交换内存信息(交换区内存)
wl=psutil.virtual_memory()
print(wl)
#svmem(total=8480653312, available=2819543040, percent=66.8, used=5661110272, free=2819543040)
jh=psutil.swap_memory()
print(jh)
#sswap(total=9017524224, used=6994763776, free=2022760448, percent=77.6, sin=0, sout=0)

#获取磁盘信息
#获取磁盘分区、磁盘使用、磁盘IO等信息
fq=psutil.disk_partitions()#磁盘分区信息
print(fq)
#[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')]
us=psutil.disk_usage("/")#磁盘使用情况
print(us)
#sdiskusage(total=254142160896, used=122931654656, free=131210506240, percent=48.4)
io=psutil.disk_io_counters()#磁盘IO
print(io)
#sdiskio(read_count=2678883, write_count=1795879, read_bytes=88661115904, write_bytes=55890906624, read_time=2516, write_time=1141)

#获取网络信息
#psutil可以获取网络接口和网络连接信息

#获取网络读写字节/包的个数
net = psutil.net_io_counters()
print(net)
#snetio(bytes_sent=924662864, bytes_recv=38886315130, packets_sent=7562604, packets_recv=29889726, errin=0, errout=0, dropin=0, dropout=0)

#获取网络接口信息
address=psutil.net_if_addrs()
print(address)
#{'以太网 4': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-E0-4C-36-5B-A7', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.130.156', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::cd0b:d21d:da63:829c', netmask=None, broadcast=None, ptp=None)], '本地连接* 11': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='A0-C5-89-3F-A9-72', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.166.190', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::c5b6:db1f:3d59:a6be', netmask=None, broadcast=None, ptp=None)], '以太网 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-50-56-C0-00-01', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.49.1', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::5941:ca15:eabc:f005', netmask=None, broadcast=None, ptp=None)], '以太网 3': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-50-56-C0-00-08', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.32.1', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::e55e:e822:7806:73c5', netmask=None, broadcast=None, ptp=None)], 'SSTAP 1': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-FF-1E-5B-48-30', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='10.198.75.60', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.225.246', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::a0ed:f12c:55f:e1f6', netmask=None, broadcast=None, ptp=None)], 'WLAN': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='A0-C5-89-3F-A9-71', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.1.106', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::149f:2321:aca5:7a53', netmask=None, broadcast=None, ptp=None)], 'Loopback Pseudo-Interface 1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]}

#获取网络接口状态
status = psutil.net_if_stats()
print(status)
#{'以太网 2': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500), '以太网 3': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500), '以太网 4': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500), 'SSTAP 1': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500), 'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500), 'WLAN': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=300, mtu=1500), '本地连接* 11': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500)}

#获取当前网络连接信息
print(psutil.net_connections())
#[sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63433), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49665), raddr=(), status='LISTEN', pid=1316), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::1', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=1008), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63431), raddr=addr(ip='127.0.0.1', port=1080), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=63470), raddr=addr(ip='47.240.5.159', port=13775), status='ESTABLISHED', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=2368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=63480), raddr=addr(ip='203.119.213.249', port=80), status='ESTABLISHED', pid=16112), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=60309), raddr=(), status='NONE', pid=6652), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=52312), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=6942), raddr=(), status='LISTEN', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59323), raddr=addr(ip='222.138.2.184', port=443), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49665), raddr=(), status='LISTEN', pid=1316), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=63474), raddr=addr(ip='203.208.50.38', port=443), status='ESTABLISHED', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.49.1', port=52309), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=62455), raddr=(), status='NONE', pid=3452), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49667), raddr=(), status='LISTEN', pid=2840), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=5040), raddr=(), status='LISTEN', pid=9612), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63436), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63451), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.32.1', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63465), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63482), status='ESTABLISHED', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63463), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=445), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59332), raddr=addr(ip='223.119.243.112', port=80), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=62675), raddr=(), status='NONE', pid=7788), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=3306), raddr=(), status='LISTEN', pid=3380), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::5941:ca15:eabc:f005', port=52305), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49670), raddr=(), status='LISTEN', pid=756), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=912), raddr=(), status='LISTEN', pid=3752), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=59511), raddr=addr(ip='127.0.0.1', port=59510), status='ESTABLISHED', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63457), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63459), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.32.1', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59328), raddr=addr(ip='223.119.243.112', port=80), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=15292), raddr=(), status='LISTEN', pid=13488), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59329), raddr=addr(ip='223.119.243.112', port=80), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63435), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=1008), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::5941:ca15:eabc:f005', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59765), raddr=addr(ip='52.139.250.253', port=443), status='ESTABLISHED', pid=3792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=4013), raddr=(), status='LISTEN', pid=3828), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=49101), raddr=(), status='NONE', pid=6652), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58214), raddr=(), status='LISTEN', pid=6652), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63471), raddr=addr(ip='127.0.0.1', port=1080), status='ESTABLISHED', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49670), raddr=(), status='LISTEN', pid=756), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=445), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=59512), raddr=addr(ip='127.0.0.1', port=59513), status='ESTABLISHED', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=63483), raddr=addr(ip='47.240.5.159', port=13775), status='ESTABLISHED', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.106', port=2177), raddr=(), status='NONE', pid=13660), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=59510), raddr=addr(ip='127.0.0.1', port=59511), status='ESTABLISHED', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59368), raddr=addr(ip='121.51.24.106', port=80), status='ESTABLISHED', pid=4960), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=62040), raddr=(), status='NONE', pid=6652), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5355), raddr=(), status='NONE', pid=2368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63469), status='ESTABLISHED', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63471), status='ESTABLISHED', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63453), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49667), raddr=(), status='LISTEN', pid=2840), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::5941:ca15:eabc:f005', port=2177), raddr=(), status='NONE', pid=13660), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=65000), raddr=(), status='LISTEN', pid=3452), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.49.1', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63455), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.106', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=59659), raddr=(), status='LISTEN', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=62454), raddr=(), status='NONE', pid=3260), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63342), raddr=(), status='LISTEN', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=4012), raddr=(), status='LISTEN', pid=3828), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63449), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63469), raddr=addr(ip='127.0.0.1', port=1080), status='ESTABLISHED', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59330), raddr=addr(ip='223.119.243.112', port=80), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49664), raddr=(), status='LISTEN', pid=684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63447), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=7680), raddr=(), status='LISTEN', pid=5796), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59327), raddr=addr(ip='223.119.243.112', port=80), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::e55e:e822:7806:73c5', port=2177), raddr=(), status='NONE', pid=13660), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.106', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=7680), raddr=(), status='LISTEN', pid=5796), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49664), raddr=(), status='LISTEN', pid=684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=65090), raddr=(), status='NONE', pid=12704), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59331), raddr=addr(ip='223.119.243.112', port=80), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::e55e:e822:7806:73c5', port=52306), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=2368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.49.1', port=2177), raddr=(), status='NONE', pid=13660), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::1', port=52308), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::149f:2321:aca5:7a53', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=57918), raddr=addr(ip='108.177.97.188', port=5228), status='ESTABLISHED', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=59513), raddr=addr(ip='127.0.0.1', port=59512), status='ESTABLISHED', pid=8732), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.32.1', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49671), raddr=(), status='LISTEN', pid=776), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49671), raddr=(), status='LISTEN', pid=776), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=58045), raddr=addr(ip='223.119.202.32', port=443), status='CLOSE_WAIT', pid=10832), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.106', port=52311), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=59264), raddr=(), status='NONE', pid=7788), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63467), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59338), raddr=addr(ip='223.119.153.70', port=443), status='CLOSE_WAIT', pid=9760), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49666), raddr=(), status='LISTEN', pid=1724), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=63432), raddr=addr(ip='54.169.169.186', port=13775), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=135), raddr=(), status='LISTEN', pid=1000), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.32.1', port=52310), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63482), raddr=addr(ip='127.0.0.1', port=1080), status='ESTABLISHED', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::149f:2321:aca5:7a53', port=52307), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5050), raddr=(), status='NONE', pid=9612), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=65000), raddr=(), status='NONE', pid=3452), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=62652), raddr=(), status='LISTEN', pid=9576), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63472), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.49.1', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.32.1', port=2177), raddr=(), status='NONE', pid=13660), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=49215), raddr=(), status='NONE', pid=12704), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=57911), raddr=addr(ip='118.178.135.232', port=443), status='ESTABLISHED', pid=7792), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63473), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.32.1', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.1.106', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=60310), raddr=(), status='NONE', pid=6652), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.49.1', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::e55e:e822:7806:73c5', port=1900), raddr=(), status='NONE', pid=4672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='127.0.0.1', port=62453), raddr=(), status='NONE', pid=3452), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49666), raddr=(), status='LISTEN', pid=1724), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=902), raddr=(), status='LISTEN', pid=3752), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1080), raddr=addr(ip='127.0.0.1', port=63437), status='TIME_WAIT', pid=0), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=1080), raddr=(), status='LISTEN', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=1080), raddr=(), status='LISTEN', pid=5684), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5355), raddr=(), status='NONE', pid=2368), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=135), raddr=(), status='LISTEN', pid=1000), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::149f:2321:aca5:7a53', port=2177), raddr=(), status='NONE', pid=13660), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.49.1', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.1.106', port=59451), raddr=addr(ip='223.252.199.69', port=6003), status='ESTABLISHED', pid=4744)]

#获取进程信息
pids=psutil.pids()
print(pids)#[0, 4, 96, 272, 404,
#获取进程信息
pids=psutil.pids()
print(pids)#[0, 4, 96, 272, 404,


#获取进程信息
pids=psutil.pids()
print(pids)#[0, 4, 96, 272, 404,
#获取进程信息
pids=psutil.pids()
print(pids)#[0, 4, 96, 272, 404, 

#获取进程信息
pids=psutil.pids()
print(pids)#[0, 4, 96, 272, 404, 584, 608, 684, 696, 756, 776, 832, 884, 904, 928, 1000, 1008, 1052, 1100, 1136, 1148, 1256, 1268, 1280, 1316, 1372, 1376, 1404, 1432, 1460, 1516, 1548, 1576, 1584, 1592, 1608, 1724, 1780, 1808, 1892, 1960, 2044, 2052, 2104, 2112, 2140, 2276, 2308, 2360, 2368, 2468, 2532, 2548, 2580, 2680, 2748, 2796, 2840, 2880, 2888, 3060, 3260, 3268, 3276, 3292, 3308, 3316, 3328, 3336, 3344, 3356, 3368, 3380, 3452, 3472, 3500, 3584, 3608, 3612, 3636, 3652, 3708, 3740, 3752, 3772, 3784, 3792, 3804, 3828, 3888, 4052, 4100, 4176, 4400, 4480, 4548, 4672, 4744, 4788, 4960, 5052, 5184, 5220, 5232, 5260, 5484, 5644, 5648, 5676, 5684, 5796, 5824, 5888, 5972, 5984, 6080, 6460, 6504, 6560, 6568, 6612, 6652, 6868, 6904, 7048, 7108, 7468, 7528, 7688, 7788, 7792, 7804, 7820, 8208, 8240, 8324, 8468, 8484, 8560, 8652, 8732, 8840, 8880, 9032, 9068, 9076, 9196, 9320, 9384, 9488, 9576, 9612, 9760, 9788, 9808, 9820, 9996, 10288, 10612, 10740, 10752, 10832, 10880, 10892, 10960, 10996, 11008, 11164, 11396, 11620, 11648, 11904, 12036, 12100, 12152, 12300, 12372, 12504, 12536, 12540, 12620, 12704, 12780, 12784, 12824, 12932, 13024, 13048, 13120, 13124, 13488, 13564, 13660, 13780, 14056, 14100, 14108, 14492, 14612, 14740, 14768, 14836, 14892, 15044, 15244, 15312, 15344, 15372, 15684, 15772, 15796, 16112, 16140, 16148, 16172, 16288, 16344]

#拿到指定进程
p=psutil.Process(12100)
print(p.name())#进程名称：RuntimeBroker.exe
print(p.exe())#进程exe路径：C:\Windows\System32\RuntimeBroker.exe
print(p.cwd())#进程工作目录：C:\WINDOWS\system32
print(p.cmdline())#进程启动的命令行：['C:\\Windows\\System32\\RuntimeBroker.exe', '-Embedding']
print(p.ppid())#父进程Id
parent=p.parent()#获取父进程
print(parent.children())#子进程列表[psutil.Process(pid=5888, name='unsecapp.exe', started='2019-06-15 14:23:54'), psutil.Process(pid=5972, name='WmiPrvSE.exe', started='2019-06-15 14:23:54'), psutil.Process(pid=11008, name='ShellExperienceHost.exe', started='19:32:33'), psutil.Process(pid=15772, name='SearchUI.exe', started='19:32:33'), psutil.Process(pid=14056, name='RuntimeBroker.exe', started='19:32:34'), psutil.Process(pid=12932, name='RuntimeBroker.exe', started='19:32:34'), psutil.Process(pid=10892, name='SettingSyncHost.exe', started='19:32:35'), psutil.Process(pid=15684, name='LockApp.exe', started='19:32:36'), psutil.Process(pid=14836, name='ChsIME.exe', started='19:32:36'), psutil.Process(pid=11620, name='RuntimeBroker.exe', started='19:32:36'), psutil.Process(pid=9488, name='RemindersServer.exe', started='19:32:37'), psutil.Process(pid=10832, name='Video.UI.exe', started='19:32:37'), psutil.Process(pid=10740, name='RuntimeBroker.exe', started='19:32:37'), psutil.Process(pid=14612, name='unsecapp.exe', started='19:32:46'), psutil.Process(pid=15312, name='RuntimeBroker.exe', started='19:32:49'), psutil.Process(pid=3608, name='WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe', started='19:32:55'), psutil.Process(pid=16344, name='ApplicationFrameHost.exe', started='20:15:13'), psutil.Process(pid=9760, name='WinStore.App.exe', started='20:15:13'), psutil.Process(pid=9032, name='RuntimeBroker.exe', started='20:15:14'), psutil.Process(pid=5676, name='SystemSettings.exe', started='20:17:29'), psutil.Process(pid=10960, name='MicrosoftEdge.exe', started='20:17:39'), psutil.Process(pid=16288, name='browser_broker.exe', started='20:17:39'), psutil.Process(pid=12100, name='RuntimeBroker.exe', started='20:17:40'), psutil.Process(pid=7048, name='MicrosoftEdgeCP.exe', started='20:17:40'), psutil.Process(pid=12300, name='MicrosoftEdgeCP.exe', started='20:17:40'), psutil.Process(pid=1404, name='Calculator.exe', started='20:17:50'), psutil.Process(pid=7468, name='Microsoft.Photos.exe', started='21:43:39'), psutil.Process(pid=11648, name='RuntimeBroker.exe', started='21:43:40'), psutil.Process(pid=12620, name='SogouImeBroker.exe', started='21:44:21'), psutil.Process(pid=15796, name='SystemSettingsBroker.exe', started='22:16:57'), psutil.Process(pid=14492, name='WmiPrvSE.exe', started='23:10:46')]
print(parent.status())#进程状态  running
# print(parent.username())#进程用户名   要获取权限先
print(parent.create_time())#进程创建时间 时间戳 1560579826.0
# print(parent.terminal())#进程终端  linux上有终端概念
print(parent.cpu_times())#进程使用的cpu时间 pcputimes(user=77.1875, system=99.296875, children_user=0.0, children_system=0.0)

print(parent.memory_info())#进程使用的内存  pmem(rss=25341952, vms=18825216, num_page_faults=1520122, peak_wset=36626432, wset=25341952, peak_paged_pool=929264, paged_pool=902800, peak_nonpaged_pool=36664, nonpaged_pool=27720, pagefile=18825216, peak_pagefile=22953984, private=18825216)

p.connections() # 进程相关网络连接
p.num_threads()  # 进程的线程数量
p.threads() # 所有线程信息
p.environ() # 进程环境变量
# p.terminate()  # 结束进程


"""psutil还提供了一个test()函数，可以模拟出ps命令的效果"""
# psutil.test()
