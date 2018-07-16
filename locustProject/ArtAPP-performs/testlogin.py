from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    @task()
    def login(self):
        # phone = 15827412957
        self.client.post("/ArtAppWeb4_7_1/rest/user/login", data={"mobile":"15827412957", "password":"e10adc3949ba59abbe56e057f20f883e"})

#This is another HttpLocust class.
class MobileUserLocust(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

'''
首先，在cmd命令启动性能测试：
脚本地址：E:/PycharmProjects/SeleniumTest/PythonWork/locustProject/simpleDemo/testlogin.py
locust -f locustfile.py --host=http://bak.artapp.cn:80

其中：
-f：指定性能测试脚本文件；
–host：指定被测试应用的URL地址，注意访问百度使用的HTTPS协议；

通过浏览器访问：http://127.0.0.1:8089（Locust启动网络监控器，默认端口号为8089），
'''