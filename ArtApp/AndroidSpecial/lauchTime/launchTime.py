#/user/bin/python
#encoding:utf-8

'''
冷启动：属于你第一次打开APP，系统在给你开一个进程。
热启动：就是你已经打开过APP但是实际上面你使用home键等。就是还存在后台的应用。再次打开的时候算是属于热启动了。

往往分析时剔除第一行数据
分析均值，其次看波动情况

1.与竞品进行分析，均值进行比较
2.与以往版本进行分析，看冷、热启动的波动情况
'''
import os
import time
import csv

# app类
class App(object):
    def __init__(self):
        self.content = ""
        self.startTime = 0

    # 启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.xiaomi.shop/com.xiaomi.shop.activity.MainTabActivity'
        self.content = os.popen(cmd)

    # 停止App
    def StopApp(self):
        # 冷启动
        # cmd = 'adb shell am force-stop com.xiaomi.shop'
        # 热启动
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    # 获取启动时间
    def GetLauchedTime(self):
        for line in self.content.readlines():
            # 如果找到ThisTime则停止寻找
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

# 控制类
class Controller(object):
    def __init__(self,count):
        self.app = App()
        self.counter = count
        # 收集测试数据的数组
        self.alldata = [("timestamp", "elapsedtime")]

    #   单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5)
        # 耗时
        elpasedtime = self.app.GetLauchedTime()
        self.app.StopApp()
        time.sleep(3)
        currenttime = self.getCurrentTime()
        # 存入数组
        self.alldata.append((currenttime,elpasedtime))

    # 多次执行测试过程
    def run(self):
        # 当执行次数大于0则执行单次测试过程，并次数-1
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return  currentTime

    # 数据的存储
    def SaveDataToCSV(self):
        # 定义一个csv文件 --热启动
        # csvfile = open("startTime.csv", 'w', newline='')
        # 定义一个csv文件 --冷启动
        csvfile = open("startTime2.csv", 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == '__main__':
    # 实例化controller类 并执行10次
    controller = Controller(10)
    # 跑起来
    controller.run()
    # 数据的存储
    controller.SaveDataToCSV()