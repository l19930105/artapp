
'''
利用unittest完成小米商城APP登录的业务操作，并在登录成功之后获取到用户名
两个case 一个登录成功 两个登录失败
setup和teardown里分别完成必要的初始化和quit
最后实现形成报告--发送邮件
'''
#encoding=utf-8

import unittest
import HTMLTestRunner_CN_Chart_Screen
import time
import os
import sys

# 可以使用相对路径引用
sys.path.append(os.getcwd() + '\\AppiumCommons')
import email_class

#　单个执行
# sys.path.append(os.getcwd() + '\\testcase')
# from test_00_search import TestSearch

# 存入程序开始时间
start = time.clock()

# 能够遍历多个以test开头的测试类
def create_suite(case_path):
    uts = unittest.TestSuite()
    """
     使用discover 可以一次调用多个脚本
     case_path 被测试脚本的路径
     pattern 脚本名称匹配规则
    """
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    for test_suite in discover:
        for test_case in test_suite:
            # 测试嘞
            uts.addTest(test_case)
    return uts

# 存放测试用例路径
test_path = "./testcase"

# 通过添加类名来运行
# all_suite = unittest.makeSuite(TestSearch)

suite = create_suite(test_path)

# # 存放报告的文件夹
# report_path = r"E:\PycharmProjects\SeleniumTest\PythonWork\AppiumPortProject\reports"
# 优化为相对路径
report_path = "./reports"
#获取当前时间 可确保测试报告文件不重名
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_path + '/'+ now + 'result.html'
fp = open(report_name, 'wb')
runner = HTMLTestRunner_CN_Chart_Screen.HTMLTestRunner(verbosity=2, stream=fp, title='Appium-小米商城APP-自动化测试', description='测试小米商城登录功能')
runner.run(suite)
fp.close()
#调用发送邮件的方法
mail = email_class.SendMail()
# 设置变量并调用发送邮件
from1 = "13469975256@163.com"
to = "957949761@qq.com"
titile = "现在时刻： " + now + "\n的新的移动端测试报告来啦！！！"
content = "新的移动端自动化测试报告来啦，记得去看专项数据哦！！！"
# 添加上面获取的附件
attach = report_name
mail.send_mail(from1, to, titile, content, "html", attach)
print("发送邮件结束>>>>>")
# 存入结束时间
end = time.clock()
print("整个测试总共花费了 %.1f 秒" % (end - start))
