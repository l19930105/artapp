'''
利用unittest完成ArtAPP登录的业务操作，并在登录成功之后获取到用户名
两个case 一个登录成功 两个登录失败
setup和teardown里分别完成必要的初始化和quit
最后实现形成报告--发送邮件
'''

# coding=utf-8

from selenium import webdriver
from time import sleep
import unittest
import os
import easygui as g
import sys
# # 可以使用相对路径引用
# sys.path.append(os.getcwd() + '\\po')
# import search_page
from time import sleep


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

            # 我的手机
            # 'deviceName': '621QACQ932MCM',
            # # OS的版本
            # 'platformVersion': '7.0',

            # 虚拟机
            'deviceName': 'Android Emulator',
            # OS的版本
            'platformVersion': '4.4.2',

            # 被测试的App在电脑上的绝对路径，如果写了这个就可以不写下面的两个了
            # 缺点：每次执行都会重新安装！
            # 'app': 'os.path.abspath("d:\\python_workspace\\AppiumClassDemo\\小米商城.apk")',

            # 建议用下面这种写法
            # apk包名
            'appPackage': 'cn.art.app',
            # apk的launcherActivity
            # 注意，原生app的话要在activity前加个.
            'appActivity': 'cn.art.app.activities.common.WelcomeActivity',
            'noReset': 'true',
            # 隐藏手机中的软键盘,让手机中可以输入中文
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    # 这里写了一个登录的方法,账号和密码参数化
    def test_Login01(self):
        '''测试登录 --成功演示01'''
        user = "13100000020"
        # 输入手机号
        self.driver.find_element('id', "cn.art.app:id/et_login_tel").send_keys(user)
        # 点击密码
        self.driver.find_element('id', "cn.art.app:id/et_login_passwd").send_keys("123456")
        # 点击“登录”
        self.driver.find_element('id', "cn.art.app:id/btn_login").click()
        sleep(2)

    def type_loginPass_hint(self):
        # 登录成功后元素文本的获取
        return self.driver.find_element('id', "com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_userid").text

    def type_loginFail_hint(self):
        sleep(2)
        # 登录失败元素文本的获取
        return self.driver.find_element('id', "com.xiaomi.shop:id/error_password_tips").text

    # def test_Login01(self):
    #     '''测试登录 --成功演示01'''
    #     user = "553220293"
    #     # 调用登录方法
    #     self.login(user, "l2875985")
    #     loginPass = self.type_loginPass_hint()
    #     # 判断结果
    #     try:
    #         self.assertEqual(loginPass, '553220293')
    #     except Exception as e:
    #         print("账户：" + user + "  登录异常： ", str(e))
    #
    # def test_Login02(self):
    #     '''测试登录 -用户名错误--失败演示02'''
    #     user = "55322029"
    #     # 调用登录方法
    #     self.login(user, "l2875985")
    #     loginFail = self.type_loginFail_hint()
    #     # 判断结果
    #     try:
    #         self.assertEqual(loginFail, '用户名密码不匹配')
    #     except Exception as e:
    #         print("账户：" + user + "  登录异常： ", str(e))
    #
    # def test_Login03(self):
    #     '''测试登录 -密码错误--失败演示03'''
    #     user = "553220293"
    #     # 调用登录方法
    #     self.login(user,"l287598")
    #     loginFail = self.type_loginFail_hint()
    #     # 判断结果
    #     try:
    #         self.assertEqual(loginFail, '用户名密码不匹配')
    #     except Exception as e:
    #         print("账户：" + user + "  登录异常： ", str(e))

    def tearDown(self):
        # print("appium自动化运行完成>>>>>")
        print("运行完成" + ">>>>>")
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()