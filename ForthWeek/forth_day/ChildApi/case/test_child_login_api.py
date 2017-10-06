
""" pass """
import unittest
from lib import HttpHandler
from config import config


class LoginApiTest(config.Login, unittest.TestCase, HttpHandler.HttpHandler):
    """ Child的项目的登陆接口测试用例 """

    def test_login_success_is_ok(self):
        """ [登陆][成功] 正常登陆行为可以成功登陆 """
        self.data_tmp['username'] = '13500001234'
        self.data_tmp['password'] = '12574655'
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('auth'), 'user')
        self.assertEqual(resp.get('code'), '200')
        self.assertEqual(resp.get('username'), self.data_tmp['username'])
        self.assertEqual(resp.get('message'), 'success')
        self.assertEqual(self.valid_json(resp, 'login', 'login_success'), True)

    def test_repeat_login(self):
        """ [登陆][成功] 某个用户重复调用登陆接口 """
        self.data_tmp['username'] = '13500001234'
        self.data_tmp['password'] = '12574655'
        resp = self.post(self.api_url, json=self.data_tmp)
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('auth'), 'user')
        self.assertEqual(resp.get('code'), '200')
        self.assertEqual(resp.get('username'), self.data_tmp['username'])
        self.assertEqual(resp.get('message'), 'success')
        self.assertEqual(self.valid_json(resp, 'login', 'login_success'), True)

    def test_error_password(self):
        """ [登陆][失败] 错误的用户密码 """
        self.data_tmp['password'] = ''
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('auth'), 'user')
        self.assertEqual(resp.get('code'), '200')
        self.assertEqual(resp.get('username'), '')
        self.assertEqual(resp.get('message'), 'success')

    def test_not_register_user_login(self):
        """ [登陆][失败] 未注册的用户不可以直接登陆 """
        self.data_tmp['username'] = self.mobile()
        self.data_tmp['password'] = self.password()
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('code'), '200')
        self.assertEqual(resp.get('username'), None)
        self.assertEqual(resp.get('message'), 'failed')

    def test_not_mobile(self):
        """ [登陆][失败] 登陆时没有提交手机号 , 不可成功登陆 """
        self.data_tmp['username'] = ''
        resp = self.post(self.api_url, json=self.data_tmp).json()
        self.assertEqual(resp.get('code'), '200')
        self.assertEqual(resp.get('username'), '')
        self.assertEqual(resp.get('message'), 'failed')
