from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''
公共方法类 实现截图和发送测试报告
'''

# 截图方法
def insert_img(driver, filename):
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
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))
    file = os.path.join(report_dir, lists[-1])
    return file

# 将测试报告发送到邮件
def send_mail(latest_report):
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
    receives = ['hbk5256@dingtalk.com', '957949761@qq.com']

    # 发送邮件主题和内容
    subject = 'Web Selenium 自动化测试报告'

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
    driver = webdriver.Firefox()
    driver.get("http://test.artapp.cn:9999/ArtAppInst2/index")
    insert_img(driver, "ArtApp.png")
    driver.quit()