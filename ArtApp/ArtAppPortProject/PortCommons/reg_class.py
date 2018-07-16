# encoding=utf-8
import requests
import json

'''
本class完成:
1.实现get，post_form，post_json请求的发送
2.返回请求状态码status_code，响应时间response_time，响应结果response
'''
class MyRequests:
    # get请求方式
    def get_requests(self, url, param, header={"content-type":"application/x-www-form-urlencoded"}):
        try:
            response = requests.get(url=url, params=param, headers=header)
            #  状态码
            status_code = response.status_code
            # 响应时间
            response_time = response.elapsed.total_seconds()
            # 响应内容,并将响应转换为 python 类型
            response = response.json()
            return status_code, response, response_time
        except Exception as e:
            print("get请求失败！", str(e))

    # post请求，请求头格式为form格式
    def post_form(self, url, data, header={"content-type":"application/x-www-form-urlencoded"}):
        try:
            response = requests.post(url=url, data=data, headers=header)
            #  状态码
            status_code = response.status_code
            # 响应时间
            response_time = response.elapsed.total_seconds()
            # 响应内容,并将响应转换为 python 类型
            response = response.json()
            return status_code, response, response_time
        except Exception as e:
            print("post_form请求失败！", str(e))

    def post_json(self,url,data,header={"content-type":"application/json"}):
        # 入参是json格式的，请求的时候需要把python类型转换为json类型才可以
        data = json.dumps(data)
        try:
            response = requests.post(url=url, data=data, headers=header)
            #  状态码
            status_code = response.status_code
            # 响应时间
            response_time = response.elapsed.total_seconds()
            # 响应内容,并将响应转换为 python 类型
            response = response.json()
            return status_code, response, response_time
        except Exception as e:
            print("post_json请求失败！", str(e))

    # 上传文件 -- 请求参数存在文件中
    def post_files(self, full_url, file_name, headers):
        print("文件上传请求URL=",full_url)
        print("上传文件名=",file_name)
        print("文件上传请求headers=",headers)

        files = {"file": open(file_name, "rb")}
        try:
            r = requests.post(full_url, files=files, headers=headers)
            #  状态码
            status_code = r.status_code
            #  响应头
            response_headers = r.headers
            # 响应内容,并将响应转换为 python 类型
            response = r.json()
            # 响应时间
            time = r.elapsed.total_seconds()
            return status_code, response, time
        except Exception as e:
            print("post_json请求失败！", str(e))

'''
测试接口：
1. 打开Mock文件
2. 测试get和Post接口
'''

# r = MyRequests()
# url = "http://localhost:12306"
# path1 = "/book_info"
# url1 = url+path1
# param1 = {"booke_name":"小强软件测试疯狂讲义","check_status":"on"}
# status_code1, response1, response_time1 = r.get_requests(url1, param1)
# print("get请求（带参数）的status_code=", status_code1)
# print("get请求（带参数）的response=", response1)
# print("get请求（带参数）的response_time=", response_time1)
#
# path2 = "/book_list"
# url2 = url+path2
# param2 = {}
# status_code2, response2, response_time2 = r.get_requests(url2,param2)
# print("get请求（不带参数）的status_code=",status_code2)
# print("get请求（不带参数）的response=",response2)
# print("get请求（不带参数）的response_time=",response_time2)
#
# path3 = "/login1"
# url3 = url+path3
# param3 = {"username":"xiaoqiang","pwd":"123123"}
# status_code3, response3, response_time3 = r.post_form(url3, param3)
# print("post_form请求的status_code=", status_code3)
# print("post_form请求的response=", response3)
# print("post_form请求的response_time=", response_time3)

# path4 = "/login2"
# url4 = url+path4
# param4 = {"username":"xiaoqiang", "pwd":"123123"}
# status_code4, response4, response_time4 = r.post_json(url4, param4)
# print("post_json请求的status_code=", status_code4)
# print("post_json请求的response=", response4)
# print("post_json请求的response_time=", response_time4)