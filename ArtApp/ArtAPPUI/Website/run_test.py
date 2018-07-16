import unittest
from function import *
from BSTestRunner import BSTestRunner
import time

start = time.clock()

report_dir = './test_report'
test_dir = './test_case'

print("start run test case")
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")
#获取当前时间确保测试报告文件不重名
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+'result.html'

print("start write report..")
with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title="Test Report", description="localhost login test")
    runner.run(discover)
    f.close()

print("find latest report")
latest_report = latest_report(report_dir)

print("send email report..")
send_mail(latest_report)

print("Test end")

end = time.clock()
print("整个测试总共花费了 %f s" % (end - start))