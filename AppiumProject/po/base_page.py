# -*- coding: utf-8 -*-
_author_ = '刘斌宇  》》 指导老师：小强'

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

'''
该类主要是完成所有页面的一些公共方法的封装
其实说白了就是把原生态的多个方法组装或者改改用
这里的内容可以根据需要自行修改，不是标准，仅提供思路
'''
class BasePage(object):

    '''
    说明：
        初始化
    参数：
        se_driver
    '''
    def __init__(self,se_driver):
        self.driver = se_driver
        #self.driver=webdriver.Firefox()


    '''
    说明：
        定义open方法，访问URL
    参数：
        url：访问的地址链接
    '''
    def open(self,url):
        self.driver.get(url)

    '''
    说明：
        最大化浏览器，并访问URL
    参数：
        url：访问的地址链接
    '''
    def open_max(self,url):
        self.driver.maximize_window()
        self.driver.get(url)
       
    '''
    说明：
        退出
    '''
    def quit(self):
        self.driver.quit()

    '''
    说明：
        二次封装元素定位
    参数：
        element：元素属性--值
    返回：
        获取到的元素
    '''
    def get_element(self,element):

        if "--" not in element:
            raise NameError("语法错误！元素属性和指之间用--连接")

        by = element.split("--")[0].strip()
        value = element.split("--")[1].strip()

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class name":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link text":
            element = self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("元素属性不对，可以识别的有：'id','name','class_name','link_text','xpaht','css'")
        return element


    '''
    说明：
        二次封装输入数据
    参数：
        element：元素属性--值
        value：要输入的内容
    返回：
        无
    '''
    def input(self,element,value):
        try:
            ge = self.get_element(element)
            ge.send_keys(value)
        except Exception as e:
            print("出错了！", str(e))


    '''
    说明：
        先清空内容在输入
    参数：
        element：元素属性--值
        value：要输入的内容
    返回：
        无
    '''
    def clear_input(self,element,value):
        try:
            ge = self.get_element(element)
            ge.clear()
            ge.send_keys(value)
        except Exception as e:
            print("出错了！", str(e))



    '''
    说明：
        click和submit的封装
    参数：
        element：元素属性--值
        click：默认是点击操作，如果是submit则设置为false
    返回：
        无
    '''
    def click_submit(self,element,click=True):
        try:
            ge = self.get_element(element)
            if click:
                ge.click()
            else:
                ge.submit()
        except Exception as e:
            print("出错了！", str(e))


    '''
    说明：
        鼠标悬浮的封装
    参数：
        element：你懂的
    '''
    def mouse_move(self,element):
        try:
            ge = self.get_element(element)
            ActionChains(self.driver).move_to_element(ge).perform()
        except Exception as e:
            print("出错了！", str(e))

    '''
    说明：
        超级连接的封装。用的是部分匹配方法，选择方法的技巧也很重要
    参数：
        text：超级连接的名字
    '''
    def link_text(self,text):
        try:
            self.driver.find_element_by_partial_link_text(text).click()
        except Exception as e:
            print("出错了！", str(e))

    '''
    说明：
        获取tilte
    '''
    def get_title(self):
        title = self.driver.title
        return title

    '''
    说明：
        alert确认
    '''
    def alert_accept(self):
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            print("出错了！", str(e))


    '''
    说明：
        alert取消
    '''
    def alert_dismiss(self):
        try:
            self.driver.switch_to.alert.dismiss()
        except Exception as e:
            print("出错了！", str(e))


    '''
    说明：
        frame切换的封装
    参数：
        element：你懂的
    '''
    def switch_to_frame(self, element):
        try:
            iframe_el = self.get_element(element)
            self.driver.switch_to.frame(iframe_el)
        except Exception as e:
            print("出错了！", str(e))

    '''
    说明：
        回到主frame的封装
    '''
    def switch_to_frame_default(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print("出错了！", str(e))

    '''
    说明：
        鼠标双击的封装
    参数：
        element：你懂的
    '''
    def double_click(self,element):
        try:
            ge = self.get_element(element)
            ActionChains(self.driver).double_click(ge).perform()
        except Exception as e:
            print("出错了！", str(e))



    '''
    说明：
        二次封装js
    参数：
        script：要运行的js代码
    '''
    def js(self, script):
        try:
            self.driver.execute_script(script)
        except Exception as e:
            print("出错了！", str(e))
    


    '''
    说明：
        截图
    参数：
        file_path：保存图片的路径
    '''
    def take_screenshot(self, file_path):
        try:
            self.driver.get_screenshot_as_file(file_path)
        except Exception as e:
            print("出错了！", str(e))

    
    '''
    说明：
        输入数据之后按键盘上的回车
    参数：
        element：你懂的
        value：要输入的内容
        sec：等待时间，单位秒
    '''
    def input_enter(self,element,value,sec=1):
        try:
            ge=self.get_element(element)
            ge.send_keys(value)
            time.sleep(sec)
            ge.send_keys(Keys.ENTER)
        except Exception as e:
            print("出错了！", str(e))



'''
url = "http://www.xqtesting.com"
driver = webdriver.Firefox()
bp = BasePage(driver)
bp.open_max(url)
bp.input('id--words','小强测试品牌')
bp.click_submit('class name--btn-default')
time.sleep(5)
bp.quit()
'''
