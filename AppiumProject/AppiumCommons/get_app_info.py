#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
在某一测试场景下，监控CPU和内存
'''

import platform
import os

#获取当前电脑系统
def get_system():
    system = platform.system()
    if system == 'Windows':
        manage = 'findstr'
    else:
        manage = 'grep'
    return manage

mange = get_system()

'''
adb shell top可选的参数如下
-m num  Maximum number of processes to display. 最多显示多少个进程
-n num  Updates to show before exiting.  刷新次数 
-d num  Seconds to wait between updates. 刷新间隔时间（默认5秒）
-s col  Column to sort by (cpu,vss,rss,thr). 按哪列排序 
-t      Show threads instead of processes. 显示线程信息而不是进程
-h      Display this help screen.  显示帮助文档 

adb命令如下：
adb shell top -n 1|findstr com.xiaomi.shop
'''

# 监控cpu
def get_cpu(appPackage):
	cpu_commond = 'adb shell top -n 1| %s %s' % (mange, appPackage)
    #popen专门执行命令的
	cpu = os.popen(cpu_commond).read().split()[2]
	return cpu

# 监控内存
def get_mem(appPackage):
	mem_commond = 'adb shell top -n 1| %s %s' % (mange, appPackage)
	mem = os.popen(mem_commond).read().split()[6]
	mem_m = str(round(int(mem[:-1])/1024))+'M'
	return mem_m


if __name__ == '__main__':
	cpu = get_cpu('com.xiaomi.shop')
	print(cpu)
	mem = get_mem('com.xiaomi.shop')
	print(mem)

