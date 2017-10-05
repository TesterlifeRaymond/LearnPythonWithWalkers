""" pass """
import unittest
from config import api
from lib import http


class BaseTestConfig(api.WeChatApi, http.HttpHandler, unittest.TestCase):
    """ pass """


class WeChatApi(BaseTestConfig):
    """ pass """
    @classmethod
    def setUpClass(cls):
        """ pass """
        cls.api_url = cls.enum.get('test_api')   # 获取被测url地址
        cls.data_tmp = cls.enum.get('data')
        cls.schema_path = cls.enum.get('schema_path')

    def test_wechat_api_is_ok_method_get(self):
        """ pass """
        resp = self.get(self.api_url, params=self.data_tmp).json()
        self.assertEqual(resp.get('reason'), '请求成功')
        self.assertEqual(resp.get('error_code'), 0)
        self.assertEqual(self.get_value(resp, 'ps'), 20)
        self.assertEqual(self.get_value(resp, 'pno'), 2)
        self.assertEqual(self.valid_json(resp, self.schema_path, 'wechat_success'), True)
