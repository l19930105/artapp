import requests
import json

# url = "https://ceshi.artapp.cn:443"
# print(">>>接口开始测试>>>")
# path = "/ArtAppWebTest/rest/user/login"
# full_url = url+path
# print("POST请求完整url=", full_url)
# data = {"mobile":"15827412957", "password":"e10adc3949ba59abbe56e057f20f883e"}
# print("POST请求参数=", data)
# headers = {"content-type":"application/x-www-form-urlencoded"}
# r = requests.post(full_url, data = data, headers = headers)
# print("POST响应状态码=", r.status_code)
# print("POST响应头=", r.headers)#r.headers["Content-Type"]
# print("POST响应结果=", r.text)
# print('POST接口的响应时间=', r.elapsed.total_seconds(),'秒')
# print(">>>接口结束>>>>>\n")

url = "http://bak.artapp.cn:80"
print(">>>接口开始测试>>>")
path = "/ArtAppWeb4_7_1/rest/user/login"
full_url = url+path
print("POST请求完整url=", full_url)
data = {"mobile":"15827412957", "password":"e10adc3949ba59abbe56e057f20f883e"}
print("POST请求参数=", data)
headers = {"content-type":"application/x-www-form-urlencoded"}
r = requests.post(full_url, data = data, headers = headers)
print("POST响应状态码=", r.status_code)
print("POST响应头=", r.headers)#r.headers["Content-Type"]
print("POST响应结果=", r.text)
print('POST接口的响应时间=', r.elapsed.total_seconds(),'秒')
print(">>>接口结束>>>>>\n")