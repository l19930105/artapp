from locust import HttpLocust, TaskSet, task

# 定义用户行为
class UserBehavior(TaskSet):

    '''
    baidu_page()方法表示一个用户行为，访问百度首页。使用@task装饰该方法为一个事务
    client()用于指定请求的路径“/”，因为是百度首页，所以指定为根路径
    '''
    @task
    def baidu_page(self):
        self.client.get("/")

'''
WebsiteUser()类用于设置性能测试。
 task_set ：指向一个定义了的用户行为类。
 min_wait ：用户执行任务之间等待时间的下界，单位：毫秒。
 max_wait ：用户执行任务之间等待时间的上界，单位：毫秒。
'''
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

'''
首先，在cmd命令启动性能测试：

root@TEST:~# locust -f locustfile.py --host=https://www.baidu.com

其中：
-f：指定性能测试脚本文件；
–host：指定被测试应用的URL地址，注意访问百度使用的HTTPS协议；

通过浏览器访问：http://127.0.0.1:8089（Locust启动网络监控器，默认端口号为8089），
'''
'''
单击“Start swarming”按钮，开始运行性能测试，各个参数如下：

Type：请求的类型，例如GET/POST；
Name：请求的路径，这里为百度首页，即https://www.baidu.com/；
request：当前请求的数量；
fails：当前请求失败的数量；
Median：中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值；
Average：平均值，单位毫秒，所有请求的平均响应时间；
Min：请求的最小服务器响应时间，单位毫秒；
Max：请求的最大服务器响应时间，单位毫秒；
Content Size：单个请求的大小，单位字节；
reqs/sec：每秒钟请求的个数。

'''