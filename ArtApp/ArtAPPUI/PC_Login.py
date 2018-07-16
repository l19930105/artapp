'''
设计网站的登录校验
'''
# coding:utf-8
from selenium import webdriver
import unittest
from time import sleep

class WegLogin(unittest.TestCase):
    '''登录ArtApp的登录'用例'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://test.artapp.cn:9999/ArtAppInst2/index"
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def login(self, user, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''
        # 定位到输入用户名,密码并实现登录
        self.driver.find_element_by_css_selector("#login_user").clear()
        self.driver.find_element_by_css_selector("#login_user").send_keys(user)
        self.driver.find_element_by_css_selector("#login_password").clear()
        self.driver.find_element_by_css_selector("#login_password").send_keys(psw)
        self.driver.find_element_by_css_selector('.d_lofin_btn').click()
        sleep(1)


    def is_login_sucess(self):
        '''判断是否获取到登录失败的弹窗'''
        try:
            self.driver.find_element_by_css_selector(".confirm").is_displayed()
            return True
        except:
            return False

    def test_01(self):
        '''账户、密码正确'''
        # 调用登录方法
        self.login("15110136827", "123456")
        # 判断结果 登录成功返回False
        result = self.is_login_sucess()
        self.assertFalse(result)

    def test_02(self):
        '''密码错误'''
        # 调用登录方法
        self.login("15110136827", "111111")
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()