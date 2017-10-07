
""" pass """

import unittest
from lib import HttpHandler
from config import config


class RegisterApiTest(config.Register, unittest.TestCase, HttpHandler.HttpHandler):
    """ Child的项目的注册接口测试用例 """

    @classmethod
    def setUpClass(cls):
        """ 类初始化 """

    def test_register_api_is_ok(self):
        """ [注册][预期成功] 正常手机号用户注册成功 """
        self.data_tmp['username'] = self.mobile()
        self.data_tmp['password'] = self.password()
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('auth'), 'user')
        self.assertEqual(resp.get('code'), 200)
        self.assertEqual(resp.get('username'), self.data_tmp['username'])
        self.assertEqual(resp.get('message'), 'success')
        self.assertEqual(self.valid_json(resp, 'register', 'register_success'), True)

    def test_register_api_method_is_get(self):
        """ [注册][失败] 当请求方法是get时， 提示方法错误 """
        self.data_tmp['username'] = self.mobile()
        self.data_tmp['password'] = self.password()
        resp = self.get(self.api_url, params=self.data_tmp)
        self.assertEqual(resp.json().get('message'), 'The method is not allowed for the requested URL.')
        self.assertEqual(resp.status_code, 405)

    def test_register_api_not_username(self):
        """ [注册][失败] 当注册时， username参数为空"""
        self.data_tmp['username'] = ''
        self.data_tmp['password'] = self.password()
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('auth'), 'user')
        self.assertEqual(resp.get('code'), 200)
        self.assertEqual(resp.get('username'), self.data_tmp['username'])
        self.assertEqual(resp.get('message'), 'failed')
        self.assertEqual(self.valid_json(resp, 'register', 'register_no_mobile'), True)

    def test_repeat_register(self):
        """ [注册][失败] 如果手机号已经注册， 重复注册失败"""
        self.data_tmp['username'] = '13500001234'
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('auth'), 'user')
        self.assertEqual(resp.get('code'), 200)
        self.assertEqual(resp.get('username'), self.data_tmp['username'])
        self.assertEqual(resp.get('message'), 'failed')
        self.assertEqual(self.valid_json(resp, 'register', 'register_no_mobile'), True)