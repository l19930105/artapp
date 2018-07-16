#/user/bin/python
#encoding:utf-8

import os
import time
import csv

'''
本脚本实现的为：在某一测试场景下，监控CPU和内存
专项数据分析：
在一个时间段如20分钟cpu在40%稳定，是在可接受范围内的。
若一直在80%以上，就是有问题的。
'''

'''
adb shell top可选的参数如下:
    -m num  Maximum number of processes to display. 最多显示多少个进程
    -n num  Updates to show before exiting.  刷新次数 
    -d num  Seconds to wait between updates. 刷新间隔时间（默认5秒）
    -s col  Column to sort by (cpu,vss,rss,thr). 按哪列排序 
    -t      Show threads instead of processes. 显示线程信息而不是进程
    -h      Display this help screen.  显示帮助文档 

    adb命令如下：
    adb shell top -n 1|findstr com.xiaomi.shop
'''
# 控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "CPU", "内存", "电量", "流量")]
        self.cpuvalue = ""
        self.memvalue = ""
        self.power = ""
        self.receive = 1
        self.transmit = 1
        self.receive2 = 1
        self.transmit2 = 1

    # 单次测试过程
    def testprocess(self):
        # 获取CPU和内存
        result = os.popen("adb shell top -n 1|findstr com.xiaomi.shop")
        for line in result.readlines():
            if "fg" in line:
                # 将所有空行换成#
                line = "#".join(line.split())
                self.cpuvalue = line.split("#")[2]
                self.mem = line.split("#")[6]
                self.memvalue = str(round(int(self.mem[:-1]) / 1024)) + 'M'

        # 执行获取电量的命令
        powerData = os.popen("adb shell dumpsys battery")
        # 获取电量的level
        for line in powerData:
            if "level" in line:
                self.power = line.split(":")[1]

        # 小米商城 --
        result = os.popen('adb shell "ps | grep com.xiaomi.shop"')
        # 获取进程ID
        pid = result.readlines()[0].split(" ")[4]
        # print(">>>>>pid: " + str(pid))
        # 获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev")
        for line in traffic:
            if "eth0" in line:
                # 将所有空行换成#
                line = "#".join(line.split())
                # 按#号拆分，获取收到和发出的流量
                self.receive = line.split("#")[1]
                print("receive为：" + str(self.receive))
                self.transmit = line.split("#")[9]
                print("transmit为：" + str(self.transmit))
            elif "eth1" in line:
                # 将所有空行换成#
                line = "#".join(line.split())
                # 按#号拆分，获取收到和发出的流量
                self.receive2 = line.split("#")[1]
                print("222receive2为：" + str(self.receive2))
                self.transmit2 = line.split("#")[9]
                print("222transmit为：" + str(self.transmit2))

        # 计算所有流量之和
        alltraffic = int(self.receive) + int(self.transmit) + int(self.receive2) + int(self.transmit2)
        print("所有流量之和为： " + str(alltraffic))
        # 按KB计算流量值
        alltraffic = alltraffic / 1024
        # 保留小数点后两位
        alltraffic = round(alltraffic, 2)
        alltraffic = str(alltraffic) + "KB"

        # 获取当前时间
        currenttime = self.getCurrentTime()
        # 将获取到的数据存到数组中
        self.alldata.append((currenttime, self.cpuvalue, self.memvalue, self.power, alltraffic))

        print(">>>>>cpuvalue " + self.cpuvalue)
        print(">>>>>mem " + self.mem)
        print(">>>>>memvalue " + self.memvalue)
        print(">>>>>power " + self.power)
        print(">>>>>消耗流量为： " + str(alltraffic))

    # 多次执行测试过程
    def run(self):
        # 当执行次数大于0则执行单次测试过程，并次数-1
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(3)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def SaveDataToCSV(self):
        # 定义一个csv文件 --记录数据
        csvfile = open("APPstatus.csv", 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == '__main__':
    # 实例化controller类 并执行10次
    controller = Controller(3)
    # 跑起来
    controller.run()
    # 数据的存储
    controller.SaveDataToCSV()