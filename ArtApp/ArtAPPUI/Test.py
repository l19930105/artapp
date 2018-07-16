from selenium import  webdriver
from time import  sleep
import easygui as g
from selenium.webdriver.support.select import Select

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
        sleep(1)
        # 进入设置
        driver.find_element_by_xpath(".//*[@id='men-10']/a/span[3]").click()
        # 进入课程管理
        driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[1]/nav/ul/li[11]/ul/li[2]/a/span").click()

    #实现退出
    def user_logout(self,driver):
        #退出登录
        driver.find_element_by_css_selector(".hidden-xs-down").click()
        sleep(1)
        driver.find_element_by_css_selector(".confirm").click()
        # 刷新页面
        driver.refresh()
        g.msgbox("都退出系统啦 洗洗睡吧！")

    def Filtrate(self, driver):
        driver.switch_to_frame("iframepage")
        # 选择范围 下拉框
        s1 = driver.find_element_by_css_selector("#majorCode")
        Select(s1).select_by_visible_text("小提琴")
        # 全部状态 下拉框
        s2 = driver.find_element_by_css_selector("#status")
        Select(s2).select_by_visible_text("激活")
        sleep(1)
        SearchReB1 = driver.find_element_by_xpath(".//*[@id='marjors']/tbody/tr/td[1]")
        SearchReB2 = driver.find_element_by_xpath(".//*[@id='marjors']/tbody/tr/td[2]")
        SearchReB3 = driver.find_element_by_xpath(".//*[@id='marjors']/tbody/tr/td[3]")
        SearchReB4 = driver.find_element_by_xpath(".//*[@id='marjors']/tbody/tr/td[4]")
        SearchReB5 = driver.find_element_by_xpath(".//*[@id='marjors']/tbody/tr/td[5]")
        print(str(SearchReB1.text),"   ", end='')
        print(str(SearchReB2.text), "   ", end='')
        print(str(SearchReB3.text), "   ", end='')
        print(str(SearchReB4.text), "   ", end='')
        print(str(SearchReB5.text), "   ", end='')

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
    Login().Filtrate(driver)
    g.msgbox("程序运行结束！")
    #调用退出
    # Login().user_logout(driver)
