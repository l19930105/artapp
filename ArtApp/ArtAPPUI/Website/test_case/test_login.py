import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import  sleep

'''
测试登录实现类：
用户名密码正确，点击登录
用户名正确，密码错误，点击登录
用户名和密码为空，点击登录
'''
class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''用户名和密码正确'''
        print("test_ArtApp_normal is start test...")
        po = LoginPage(self.driver)
        po.Login_action('15110136827',"123456")
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(),'退出')
        function.insert_img(self.driver,"test_ArtApp_normal.png")
        print("test_zentao1_normal test Pass!")

    # @unittest.skip('skip this case')
    def test_login2_PasswdError(self):
        '''用户名正确，密码错误'''
        print("test_ArtApp2_passwdError is start test...")
        po=LoginPage(self.driver)
        po.Login_action('15110136827',111111)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"test_ArtApp2_PasswdError.png")
        print("test_ArtApp2_empty test end")

    def test_login3_empty(self):
        '''用户名和密码为空'''
        print("test_ArtApp3_empty is start test...")
        po=LoginPage(self.driver)
        po.Login_action('','')

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"test_ArtApp3_empty.png")
        print("test_ArtApp3_empty test end")

if __name__ == '__main__':
    unittest.main()