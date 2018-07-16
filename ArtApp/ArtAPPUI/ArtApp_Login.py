from selenium import  webdriver
from time import  sleep
import easygui as g

class Login():
    #实现登录
    def user_login(self,driver,user,password):
        # 定位到输入用户名,密码并实现登录
        driver.find_element_by_css_selector("#login_user").clear()
        driver.find_element_by_css_selector("#login_user").send_keys(user)
        driver.find_element_by_css_selector("#login_password").clear()
        driver.find_element_by_css_selector("#login_password").send_keys(password)
        driver.find_element_by_css_selector('.d_lofin_btn').click()
        sleep(1)
        # driver.find_element_by_css_selector(".confirm").click()

    # 测试是否点击到左边的菜单
    def caidan(self):
        # 进入设置
        driver.find_element_by_xpath(".//*[@id='men-10']/a/span[3]").click()
        sleep(1)
        # 定位课程管理并进行点击
        driver.find_element_by_xpath("//a[contains(@href,'courseProduct')]").click()
        driver.switch_to_frame("iframepage")
        # 点击【添加课程】
        driver.find_element_by_xpath("//button[@onclick='addCourse()']").click()
        sleep(1)
        # 点击返回
        driver.find_element_by_xpath(".//*[@id='myModalAdd']/div/div/div[3]/button[1]").click()

    # 实现退出
    def user_logout(self,driver):
        #退出登录
        driver.find_element_by_css_selector(".hidden-xs-down").click()
        sleep(1)
        driver.find_element_by_css_selector(".confirm").click()
        # 刷新页面
        driver.refresh()
        g.msgbox("都退出系统啦 洗洗睡吧！")

if  __name__  == '__main__':
    # 加载浏览器驱动
    driver = webdriver.Chrome()
    # 浏览器最大化
    driver.maximize_window()
    driver.refresh()
    sleep(1)
    # 打开玖首页
    driver.get("http://test.artapp.cn:9999/ArtAppInst2/index")
    # 隐式等待--全局等待5秒
    driver.implicitly_wait(5)
    #调用登录
    Login().user_login(driver,"13920376712","123456")
    #调用退出
    # Login().user_logout(driver)
    Login().caidan()
