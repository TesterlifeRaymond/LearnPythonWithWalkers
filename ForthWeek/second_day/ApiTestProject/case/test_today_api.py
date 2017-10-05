""" pass """

import unittest
from config import api
from lib import http


class TodayApi(api.JuHeApi, http.HttpHandler, unittest.TestCase):
    """ pass """
    @classmethod
    def setUpClass(cls):
        """ pass """
        cls.api_url = cls.enum.get('test_api')   # 获取被测url地址
        cls.data_tmp = cls.enum.get('data')

    def setUp(self):
        """ pass """

    def test_api_result_is_ok_method_get(self):
        """ pass """
        self.data_tmp['date'] = '10/4'
        resp = self.get(self.api_url, params=self.data_tmp).json()
        self.assertEqual(resp.get('result') is not None, True)
        self.assertEqual(resp.get('error_code'), 0)
        self.assertEqual(resp.get('reason'), 'success')

    def test_api_result_is_ok_method_post(self):
        """ pass """
        self.data_tmp['date'] = '10/4'
        resp = self.post(self.api_url, data=self.data_tmp).json()
        # type(resp) == > .get('result')
        self.assertIsNotNone(resp.get('result'))
        self.assertEqual(resp.get('error_code'), 0)
        self.assertEqual(resp.get('reason'), 'success')

    def test_not_have_date(self):
        """ pass """
        data = self.data_tmp
        data['date'] = ''
        resp = self.post(self.api_url, data=data).json()
        self.assertEqual(resp.get('error_code'), 206300)
        self.assertEqual(resp.get('reason'), "日期格式错误")

    def test_jsonschema_valid_success(self):
        """ pass """
        self.data_tmp['date'] = '10/4'
        resp = self.post(self.api_url, data=self.data_tmp).json()
        self.assertEqual(
            self.valid_json(resp, self.enum.get('schema_path'), 'today_success'), True)
        self.assertEqual(isinstance(resp.get('result'), list), True)

    def test_get_title(self):
        """ pass """
        self.data_tmp['date'] = '10/4'
        resp = self.post(self.api_url, data=self.data_tmp).json()
        self.assertEqual(self.get_value(resp, 'result')[0].get('title'), '中国唐朝僧人鉴真和尚圆寂')
        resp_list = self.get_value(resp, 'result')
        for item in resp_list:
            if item.get('e_id') == "11306":
                self.assertEqual(item.get('title'), '中国唐朝僧人鉴真和尚圆寂')
