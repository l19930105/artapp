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

    @ddt.data("postman", "postma", "")
    def testPost(self,mode):
        keyword = {"query": mode}
        headers = {"User-Agent":"hlj-android/3.3.0.1",
                   "Content-Type":"application/x-www-form-urlencoded",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.post("https://app.helijia.com/zmw/user/bind_dev",
                            #data=json.dumps(keyword),
                            data=keyword,
                            headers=headers,
                            cookies=cookies)
        print(res.text)
        if u"网页" in res.text:
            print("pass")
            result = True
        else:
            print("fail")
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()