#encoding: utf-8

import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):

    @ddt.data("App专项测试", "自动化", "Python")
    def testGet(self, queryword):
        #header部分的配置
        headers_data = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36',
            'Host':'m.imooc.com',
            'Referer': 'https://m.imooc.com/',
            'Connection':'keep-alive',
            'Accept-Encoding':'gzip, deflate, br'
        }

        #cookies部分的配置
        cookies_data = dict(imooc_uuid='ffbd103a-b800-4170-a267-4ea3b301ff06',
                            imooc_isnew_ct='1511175583',
                            imooc_isnew='2',
                            page = 'https://m.imooc.com/')

        #get请求的构造
        res = requests.get(
            "https://m.imooc.com/search/?words="+queryword,
            headers=headers_data,
            cookies=cookies_data)

        # print(res.status_code)
        # print(res.text)

        self.assertTrue(u"共找到" in res.text)

if __name__ == "__main__":
    unittest.main()