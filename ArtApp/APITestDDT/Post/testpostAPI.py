#encoding: utf-8
import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):

    @ddt.data(
        ("15977778888", "999999"),
        ("15977778889", "999998")
    )
    @ddt.unpack
    def testPost(self, username_data, password_data):
        formdata = {
            "username": username_data,
            "password": password_data,
            "verify": '',
            "referer":'https://m.imooc.com'}

        headers_data = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36',
            'Host': 'm.imooc.com'
        }

        #cookies部分的配置
        cookies_data = dict(imooc_uuid='ffbd103a-b800-4170-a267-4ea3b301ff06',
                            imooc_isnew_ct='1511175583',
                            imooc_isnew='2',
                            page = 'https://m.imooc.com/')

        res = requests.post("https://m.imooc.com/passport/user/login",
            data = formdata,
            headers = headers_data,
            cookies = cookies_data
        )

        print(res.json())

        self.assertTrue(90003 == res.json()['status'] or 10005 == res.json()['status'])

if __name__ == "__main__":
    unittest.main()