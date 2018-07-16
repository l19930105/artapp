#usr/bin/python
#encoding:utf-8

from appium import webdriver
import unittest
from time import sleep
from ddt import ddt, data, unpack

# 小米商城登录用例
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.xiaomi.shop'
        desired_caps['appActivity'] = 'com.xiaomi.shop.activity.MainTabActivity'
        # 隐藏手机中的软键盘,让手机中可以输入中文
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(10)

        # 广告页的跳过
        self.driver.find_element('id', 'com.xiaomi.shop:id/skip').click()

        # 进入我的
        self.driver.find_element('id', "com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_mine_text").click()
        # 点击登录注册
        self.driver.find_element('id', "com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_username").click()
        # 点击“用户帐号密码登录”
        self.driver.find_element('id', "com.xiaomi.shop:id/entry_to_password_login").click()
        sleep(2)
    '''
    三组测试数据
    1、 用户名、密码正确，登录成功
    2、 用户名正确、密码错误，登录失败
    3、 用户名错误、密码正确，登录失败
    '''
    @data(("553220293", "l2875985", False),
          ("553220293", "l287598", True),
          ("55322029", "l2875985", True))
    @unpack #使用复杂的数据结构时，需要用到@unpack
    def testLogIn(self, username, password, expectedresult):
        # 输入用户名
        self.driver.find_element('id', "com.xiaomi.shop:id/et_account_name").send_keys(username)
        # 输入密码
        self.driver.find_element('id', "com.xiaomi.shop:id/et_account_password").send_keys(password)
        # 点击“登录”
        self.driver.find_element('id', "com.xiaomi.shop:id/btn_login").click()

        try:
            # 如果登录按钮仍然存在
            if self.driver.find_element('id', "com.xiaomi.shop:id/btn_login").is_displayed():
                exist = True
                print(username + " 登录失败！")
        except Exception as e:
            print(">>>" + str(e))
            exist = False
            print(username +" 登录成功！")
        self.assertEqual(exist,expectedresult)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
