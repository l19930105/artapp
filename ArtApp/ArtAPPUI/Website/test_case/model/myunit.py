import unittest
from driver import *

'''
用例运行前后的环境准备工作
'''
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        # 静态等待10秒
        self.driver.implicitly_wait(10)
        # 浏览器窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()