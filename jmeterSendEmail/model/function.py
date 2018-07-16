from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from bs4 import BeautifulSoup

'''
公共方法类 实现截图和发送测试报告
'''

class SendMail:
    # 截图方法
    def insert_img(self,driver, filename):
        # 获取当前模块所在路径
        func_path = os.path.dirname(__file__)
        # print("func_path is %s" %func_path)

        # 获取test_case目录
        base_dir = os.path.dirname(func_path)
        # print("base_dir is %s" %base_dir)

        # 将路径转化为字符串
        base_dir = str(base_dir)

        # 对路径的字符串进行替换
        base_dir = base_dir.replace('\\', '/')

        # 避免路径转换失败，再次做字符串替换
        base_dir = base_dir.replace('\\', '/')
        # 获取项目文件的根目录路径
        base = base_dir.split('/Website')[0]
        # print(base)

        # 指定截图存放路径
        filepath = base + '/Website/test_report/screenshot/' + filename
        driver.get_screenshot_as_file(filepath)


    # 查找最新的测试报告
    def latest_report(self,report_dir):
        lists = os.listdir(report_dir)
        # 按时间顺序对该目录文件夹下面的文件进行排序
        lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
        print(("new report is :" + lists[-1]))
        file = os.path.join(report_dir, lists[-1])
        return file

    # 如果返回是Flase，那么就发邮件，else 通过
    # 整个方法放在报告生成之后，邮件发送之前
    def is_result_pass(self, report):
        try:
            with open(report, 'r', encoding='utf-8') as wb_data:
                soup = BeautifulSoup(wb_data, "html.parser")  # 将要解析的文件传入
                book_a = soup.findAll(attrs={"class": "details"})

                for book in book_a:
                    return book.string
                # # print(soup)
                # status = soup.find_all(id="total_row")
                # status = str(status)
                # print(status[59])  # 用例总计
                # result1 = int(status[59])  # 失败总计数
                # result2 = int(status[70])  # 错误总计数
                # print(result2)
                # if result1 > 0 or result2 > 0:
                #     # print("报告中存在错误或者失败的用例")
                #     return False
                # else:
                #     # print("报告用例均执行成功")
                #     return True
        except Exception as e:
            print("测试报告文件解析有误！", str(e))

    # 将测试报告发送到邮件
    def send_mail(self,latest_report):
        f = open(latest_report, 'rb')
        mail_content = f.read()
        f.close()

        # 发送邮件服务器
        smtpserver = 'smtp.163.com'
        # 发送邮箱用户名密码
        user = '13469975256@163.com'
        password = 'l2875985'
        # 发送和接收邮箱
        sender = '13469975256@163.com'
        # receives = ['zhangjunsen@artapp.cn', 'liubinyu5256@dingtalk.com','zhangxin@artapp.cn','xiongrui@artapp.cn']
        receives = ["957949761@qq.com"]
        # 获取当前时间 可确保测试报告文件不重名
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 发送邮件主题和内容
        subject = "现在时刻： " + now + "\n的新的线上接口监控测试报告来啦！！！"

        # HTML邮件正文
        msg = MIMEText(mail_content, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = ','.join(receives)

        # SSL协议端口号需要使用465
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        # HELO 向服务器标识用户身份
        smtp.helo(smtpserver)
        # 服务器返回结果确认
        smtp.ehlo(smtpserver)
        # 登录邮箱服务器用户名和密码
        smtp.login(user, password)

        print(">>>>>>>>>>>开始发送邮件")
        smtp.sendmail(sender, receives, msg.as_string())
        smtp.quit()
        print("<<<<<<<<<邮件发送结束!")


if __name__ == '__main__':

    # 生成邮件对象
    mail = SendMail()
    # 最近的jmeter报告文件
    latest_report = r'E:\PycharmProjects\SeleniumTest\PythonWork\jmeterSendEmail\test_report\线上接口监控--测试报告-201805140525.html'
    list = mail.is_result_pass(latest_report)
    print(list)
    # 调用邮件类中确认是否发送邮件方法
    # res = mail.is_result_pass(latest_report)
    # # 如果全部通过返回True无需发送邮件监控，如有不通过返回False需发送邮件
    # if res:
    #     print("用例全部通过无需发邮件，程序结束！")
    # else:
    #     mail.send_mail(latest_report)