#usr/bin/python
#encoding:utf-8

from appium import webdriver
import unittest
from time import sleep
from ddt import ddt, data

import sys
import os

# print(os.getcwd())
# 可以使用相对路径引用
sys.path.append(os.getcwd() + '\\po')
import get_app_info

print(os.getcwd())

# 小米商城-->搜索测试用例
@ddt
class TestSearch(unittest.TestCase):
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
        sleep(1)
        # 点击“用户帐号密码登录”
        self.driver.find_element('id', "com.xiaomi.shop:id/entry_to_password_login").click()
        # 输入用户名
        self.driver.find_element('id', "com.xiaomi.shop:id/et_account_name").send_keys("553220293")
        # 输入密码
        self.driver.find_element('id', "com.xiaomi.shop:id/et_account_password").send_keys("l2875985")
        sleep(1)
        # 点击“登录”
        self.driver.find_element('id', "com.xiaomi.shop:id/btn_login").click()
        sleep(2)

    '''
    三组测试数据
    1、 手机
    2、 平板电脑
    3、 电视
    '''
    @data("手机", "游戏本", "电视")
    def testSearch(self, searchFor):
        # 回到首页
        self.driver.find_element('id', "com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_home_txt").click()
        # 点击搜索框
        self.driver.find_element('id', "com.xiaomi.shop.plugin.homepage:id/fragment_search_swither").click()
        sleep(2)
        # 输入搜索内容
        self.driver.find_element('id', "com.xiaomi.shop2.plugin.search:id/input").send_keys(searchFor)
        # 点击“搜索”
        self.driver.find_element('id', "com.xiaomi.shop2.plugin.search:id/search_fragment_search_btn").click()
        sleep(2)
        print("当前搜索的内容为： " + str(searchFor))
        cpu = get_app_info.get_cpu('com.xiaomi.shop')
        print("当前手机CPU为： " + cpu)
        mem = get_app_info.get_mem('com.xiaomi.shop')
        print("当前手机内存为： " + mem)
        # 获取搜索内容的文本
        searchResult = self.driver.find_element('id', "com.xiaomi.shop2.plugin.search:id/product_title")
        text = searchResult.text
        # 断言判断搜索结果是否正确
        self.assertIn(searchFor, text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
