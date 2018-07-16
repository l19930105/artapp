import string
import sys
import os
# 获取相对路径
sys.path.append(os.getcwd() + '\\PortCommons')
import email_class
import log_class
sys.path.append(os.getcwd() + '\\src')
import run_testcase
import time
import WeiXinSendMsg  # 导入微信发送消息模块
import itchat

# 存入程序开始时间
start = time.clock()

# test_path = r"E:\PycharmProjects\SeleniumTest\PythonWork\xiaoqiangSelenium\ArtAppPortProject\testcase\testcase_student.xlsx"
#存放测试用例的文件夹 优化为相对路径
test_path = './testcase/testcase_APP.xlsx' # app接口
# test_path = './testcase/testcase_Institution.xlsx' # 后台机构接口
# report_path = r"E:\PycharmProjects\SeleniumTest\PythonWork\xiaoqiangSelenium\ArtAppPortProject\reports"
#存放报告的文件夹
report_path = './reports'
#获取当前时间 可确保测试报告文件不重名
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_path + '/' + now + ' report.xlsx'

log_file = "log.txt"
log = log_class.Logger(log_file)
# RunTestCase类里如果有其它方法，如果有其它方法需要写日志，就不需要在那些方法里再生成日志对象调用了，
# 所以可以把生成日志对象，写到__init__方法里
rt = run_testcase.RunTestCase(log_file)
rt.run(test_path, report_name)

# 调用发送邮件的方法
mail = email_class.SendMail()
'''
发送邮件前确认是否进行发送
'''
# 调用邮件类中确认是否发送邮件方法
mail.is_result_pass(report_name)
# 调用邮件类中确认是否发送邮件方法
res = mail.is_result_pass(report_name)

# # 通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码。
# itchat.auto_login(hotReload=True)

# 如果全部通过返回True无需发送邮件监控，如有不通过返回False需发送邮件
if res:
    print("用例全部通过无需发邮件，程序结束！")
    log.info("线上接口用例全部通过，不用担心啦！")
    # # 发送微信的好友备注名
    # name = "刘斌宇的"
    # # 发送微信的内容
    # content = "线上接口用例全部通过，不用担心啦！"
    # # 调用发送微信消息的方法
    # mail = WeiXinSendMsg.send_move(name, content)
else:
    print("接口调用有问题！！！！")
    log.info("新的接口自动化报告来啦！！！邮件的附件有excel的测试报告")
    # name = "刘斌宇的"
    # # 发送微信的内容
    # content = "接口调用有问题！，快去查看你的QQ邮箱"
    # # 调用发送微信消息的方法
    # mail = WeiXinSendMsg.send_move(name, content)

    # 设置变量并调用发送邮件
    from1 = "13469975256@163.com"
    to = ["957949761@qq.com"]
    # 接收邮件列表,是list,不是字符串
    # to = ["liubinyu5256@dingtalk.com","zhangjunsen@artapp.cn","letian@artapp.cn","zhangxin@artapp.cn"]

    titile = "现在时刻： " + now + " 的新的接口测试报告来啦！！！"


    content = "新的接口自动化报告来啦！！！邮件的附件有excel的测试报告"
    # 添加上面获取的附件
    attach = report_name
    mail.send_mail(from1, to, titile, content, "html", attach)

# #设置变量并调用发送邮件
# from1 = "13469975256@163.com"
# to = "957949761@qq.com"
# titile = now + "的接口测试报告"
# content = "现在时刻： " + now + "\n 的新的接口测试报告来啦！！！"
# attach = report_name
# mail.send_mail(from1,to,titile,content,"html",attach)

# 存入结束时间
end = time.clock()
# 获取脚本执行时间，并保留两位小数
usetime = round((end - start),2)
log.info("整个接口测试总共花费了 " + str(usetime) + " s")
# print("整个接口测试总共花费了 %.2f s" % (end - start))