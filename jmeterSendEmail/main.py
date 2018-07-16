
import time
import sys
import os
# 获取相对路径
sys.path.append(os.getcwd() + '\\model')
import function

start = time.clock()

report_dir = './test_report'

# 生成邮件对象
mail = function.SendMail()
# 根据路径获取到最近的jmeter报告文件
latest_report = mail.latest_report(report_dir)

'''
发送邮件前确认是否进行发送
'''
# 调用邮件类中确认是否发送邮件方法
res = mail.is_result_pass(latest_report)
# 如果全部通过返回True无需发送邮件监控，如有不通过返回False需发送邮件
if res:
    print("用例全部通过无需发邮件，程序结束！")
else:
    mail.send_mail(latest_report)

# #调用发送邮件的方法
# mail.send_mail(latest_report)

end = time.clock()
print("发送邮件总共花费了 %f s" % (end - start))