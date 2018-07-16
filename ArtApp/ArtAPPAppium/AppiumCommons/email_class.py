import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication


class SendMail:
    def send_mail(self, from1, to, title, content=None, type="plain", attach=None, pic=None):
        msg = email.mime.multipart.MIMEMultipart()
        # 生成包含多个邮件体的对象
        msg["from"] = from1
        msg["to"] = to
        msg["subject"] = title

        # 邮件正文
        if (content != None):
            txt = email.mime.text.MIMEText(content, type)
            msg.attach(txt)

        # 文件附件
        if (attach != None):
            part = MIMEApplication(open(attach, "rb").read())
            part.add_header("Content-Disposition", "attachment", filename=attach)
            msg.attach(part)

        # jpg图片附件
        if (pic != None):
            jpgpart = MIMEApplication(open(pic, "rb").read())
            jpgpart.add_header("Conten-Dispositon", "attachment", filename=pic)  # 收到的图片后缀名变成了.bin格式，上网查了一下资料，没看懂，先不纠结了。
            msg.attach(jpgpart)

        # 发送邮件
        smtp = smtplib
        # 链接服务器，smtp地址+端口
        smtp = smtplib.SMTP("smtp.163.com", "25")

        # 设置为调试模式，console中显示
        # smtp.set_debuglevel(1)

        # 登录，用户名+密码
        smtp.login("13469975256@163.com", "l2875985")

        # 发送，from+to+内容
        smtp.sendmail(from1, to, str(msg))

        # 退出
        smtp.quit()
        print("发送邮件结束>>>>>")

if __name__ == '__main__':
    #设置变量并调用发送邮件
    from1 = "13469975256@163.com"
    to = "957949761@qq.com"
    # 标题
    titile = "接口测试报告"
    # 内容
    content = "发送邮件测试"
    # 附件
    attach = r"E:\PycharmProjects\SeleniumTest\PythonWork\xiaoqiangSelenium\PortProject\reports\testcase_report.xlsx"

    #pic="E:\\Python_study\\work\\excel\\test.jpg"

    #生成对象并调用方法
    mail = SendMail()
    mail.send_mail(from1,to,titile,content,"html",attach)
    print("发送邮件结束>>>>>")