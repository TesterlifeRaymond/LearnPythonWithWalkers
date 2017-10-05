""" pass """


from config import BaseTestClass
from config import api, load_time


class MenuApi(api.MenuApiConfig, BaseTestClass):
    """pass"""
    @classmethod
    def setUpClass(cls):
        """ pass """
        cls.menu_url = cls.enum.get('menu_api')
        cls.menu_name = cls.enum.get('menu_name')
        cls.key_name = cls.enum.get('key')

    @load_time
    def test_api_result_method_get_ok(self):
        """ pass """
        resp = self.get(self.menu_url.format(self.menu_name), params=self.key_name).json()
        # print(resp)
        self.assertIsNotNone(resp.get('result'), True)

    @load_time
    def test_api_resultcode_method_get_ok(self):
        """ pass """
        resp = self.get(self.menu_url.format(self.menu_name), params=self.key_name).json()
        # print(resp)
        self.assertEqual(resp.get('resultcode'), '200')

    @load_time
    def test_api_result_reason_method_post_ok(self):
        """ pass """
        resp = self.get(self.menu_url.format(self.menu_name), params=self.key_name).json()
        self.assertEqual(resp.get('reason'), 'Success')

    @load_time
    def test_api_result_title_is_ok_method_get(self):
        """ pass """
        resp = self.get(self.menu_url.format(self.menu_name), params=self.key_name).json()
        self.assertEqual(resp.get('result').get('data')[0].get('title'), '红烧排骨土豆')

    @load_time
    def test_api_result_method_post_is_ok(self):
        """ pass """
        url = self.menu_url.split('?')[0]
        # url = 'http://apis.juhe.cn/cook/query.php
        # post ==> data = {'key': '338ce1ecb756bf7ca4772fbb9f11cd75', 'menu': '红烧排骨'}
        data = {'key': '338ce1ecb756bf7ca4772fbb9f11cd75', 'menu': '红烧排骨'}
        resp = self.post(url, data=data).json()
        del resp
        # data ==> location 是从form表单提交上来的
        # json ==> location 是一个json结构体
