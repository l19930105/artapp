import unittest
from model import function,myunit
from ArtAPP import ArtApp_Login
from time import  sleep
'''
测试课程管理的筛选类：
用户名密码正确，点击登录
用户名正确，密码错误，点击登录
用户名和密码为空，点击登录
'''
class FiltrateTest(myunit.StartEnd):
    def login(self):
        '''实现登录'''
        ArtApp_Login.user_login(self.driver,"13920376712","123456")
        self.driver.find_element_by_xpath(".//*[@id='men-10']/a/span[3]").click()
        self.driver.find_element_by_xpath(".//*[@id='menus_']/li[2]/a/span").click()
        sleep(2)
    # @unittest.skip('skip this case')
    def test_filtrate_normal(self):
        print("选择全部专业和全部状态  --  有三条记录...")

        # self.assertEqual(po.type_loginPass_hint(),'退出')
        # function.insert_img(self.driver,"test_ArtApp_normal.png")
        # print("test_zentao1_normal test Pass!")

if __name__ == '__main__':
    unittest.main()