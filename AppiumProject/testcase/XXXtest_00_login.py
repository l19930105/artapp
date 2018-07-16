'''
利用unittest完成官网的搜索
两个case 一个搜索 挨踢脱口秀 一个搜索小强测试品牌
setup和teardown里分别完成必要的初始化和quit
'''

#encoding=utf-8
from selenium import webdriver
from time import sleep
import unittest
import sys
import os
import easygui as g
# # 可以使用相对路径引用
# sys.path.append(os.getcwd() + '\\po')
# import search_page
'''
老方法 被弃用
'''
class TestLogin(unittest.TestCase):
    '''
       进行Appium测试的时候需要提前启动Appium服务，所以写个弹窗进行二次确认
       '''
    # 获取当前文件夹的父目录绝对路径
    BaseDir = os.path.dirname(os.path.dirname(__file__))

    # 存放的询问图片
    # img01 = r"E:\PycharmProjects\SeleniumTest\PythonWork\xiaoqiangSelenium\0425\File\ask.png"
    # 优化为获取File文件夹下的询问图片
    img01 = os.path.join(BaseDir,'File','ask.png')

    # 存放的询问图片
    # img02 = r"E:\PycharmProjects\SeleniumTest\PythonWork\xiaoqiangSelenium\0425\File\Wrong.gif"
    # 优化为获取File文件夹下的错误提示图片
    img02 = os.path.join(BaseDir,'File','Wrong.gif')


    # 用户选择是否开启Appium服务
    choices = g.buttonbox("是否启动Appium服务？" , title="移动自动化环境准备确认 ", image=img01, choices=('是', '不是'))
    # 玩家选择“不是”，直接退出程序
    if choices == '不是':
        g.msgbox("请启动Appium服务！", image=img02)
        sys.exit(0)

    def setUp(self):
        desired_caps = {
            # 使用哪种移动平台。IOS、Android
            'platformName': 'Android',
            # 启动哪种设备，是真机还是模拟器，可有可无
            'deviceName': 'Android Emulator',
            # OS的版本
            'platformVersion': '4.4.2',

            # 被测试的App在电脑上的绝对路径，如果写了这个就可以不写下面的两个了
            # 缺点：每次执行都会重新安装！
            # 'app': 'os.path.abspath("d:\\python_workspace\\AppiumClassDemo\\小米商城.apk")',

            # 建议用下面这种写法
            # apk包名
            'appPackage': 'com.xiaomi.shop',
            # apk的launcherActivity
            # 注意，原生app的话要在activity前加个.
            'appActivity': 'com.xiaomi.shop.activity.MainTabActivity',

            # 隐藏手机中的软键盘,让手机中可以输入中文
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

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

    # 这里写了一个登录的方法,账号和密码参数化
    def login(self, username, psw):
        # 输入用户名
        self.driver.find_element('id', "com.xiaomi.shop:id/et_account_name").send_keys(username)
        # 输入密码
        self.driver.find_element('id', "com.xiaomi.shop:id/et_account_password").send_keys(psw)
        # 点击“登录”
        self.driver.find_element('id', "com.xiaomi.shop:id/btn_login").click()
        sleep(3)

    def type_loginPass_hint(self):
        # 登录成功后元素文本的获取
        return self.driver.find_element('id', "com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_userid").text

    def type_loginFail_hint(self):
        sleep(2)
        # 登录失败元素文本的获取
        return self.driver.find_element('id', "com.xiaomi.shop:id/error_password_tips").text

    def test_Login01(self):
        '''测试登录 --成功演示01'''
        user = "553220293"
        # 调用登录方法
        self.login(user, "l2875985")
        loginPass = self.type_loginPass_hint()
        # 判断结果
        try:
            self.assertEqual(loginPass, '553220293')
        except Exception as e:
            print("账户：" + user + "  登录异常： ", str(e))

    def test_Login02(self):
        '''测试登录 -用户名错误--失败演示02'''
        user = "55322029"
        # 调用登录方法
        self.login(user, "l2875985")
        loginFail = self.type_loginFail_hint()
        # 判断结果
        try:
            self.assertEqual(loginFail, '用户名密码不匹配')
        except Exception as e:
            print("账户：" + user + "  登录异常： ", str(e))

    def test_Login03(self):
        '''测试登录 -密码错误--失败演示03'''
        user = "553220293"
        # 调用登录方法
        self.login(user,"l287598")
        loginFail = self.type_loginFail_hint()
        # 判断结果
        try:
            self.assertEqual(loginFail, '用户名密码不匹配')
        except Exception as e:
            print("账户：" + user + "  登录异常： ", str(e))

    def tearDown(self):
        # print("appium自动化运行完成>>>>>")
        print("运行完成" + ">>>>>")
        self.driver.quit()