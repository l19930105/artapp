# coding=utf-8

import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):
    def setUp(self):
        print("初始化")
    def tearDown(self):
        print("结束")

    @ddt.data("110100","110100","")
    def testGet(self,city_id):
        keyword = {"wd":"poptest"}
        headers = {"User-Agent":"test",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.get("https://customer-api.helijia.com/app-customer/transformers/getCityList?version=3.3.0.1&sign_type=md5&city="+ city_id + "&req_time=1472372990756&device_type=android&device_id=d3c1d53d0a8a378f",
                           params=keyword,
                           headers=headers,
                           cookies = cookies)
        print(res.text)
        if u"北京市" in res.text:
            print("pass")
            result = True
        else:
            print("fail")
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()