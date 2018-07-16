from BasePage import *
from selenium.webdriver.common.by import By
# 导入显示等待类
from selenium.webdriver.support.ui import WebDriverWait
# 导入期望场景类
from selenium.webdriver.support import expected_conditions as EC
# 导入堆栈类
import traceback
# 导入异常类
from selenium.common.exceptions import NoAlertPresentException,TimeoutException

class LoginPage(Page):
    url='/ArtAppInst2/index'

    # 定位器
    username_loc = (By.ID,'login_user')
    password_loc = (By.ID,'login_password')
    submit_loc = (By.CLASS_NAME,'d_lofin_btn')

    #用户名输入框
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 密码输入框
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 登录模块封装
    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

        # 抓取是否获得弹窗,并捕获异常
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 等待alert框出现
            alert = wait.until(EC.alert_is_present())
            # 打印alert框体消息
            print(">>>>%s" % alert.text)
            sleep(1)
            # 确认警告消息
            alert.accept()
            sleep(1)
        except TimeoutException as e:
            # 捕获TimeoutException异常
            print(traceback.print_exc())

        except NoAlertPresentException as e:
            print(">>>>>捕获NoAlertPresentException异常")
            # 捕获其他异常
            print(traceback.print_exc())

    # 登录成功后元素文本的获取
    loginPass_loc = (By.CLASS_NAME, 'hidden-xs-down')
    # 登录失败元素文本的获取
    loginFail_loc = (By.ID, 'login_user')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return  self.find_element(*self.loginFail_loc).text