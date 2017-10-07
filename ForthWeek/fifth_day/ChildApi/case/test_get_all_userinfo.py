""" pass """
import unittest
from lib import HttpHandler
from config import config


class QueryUserInfo(config.QueryUserInfo, unittest.TestCase, HttpHandler.HttpHandler):
    """ Child的项目的查询用户信息接口测试用例 """
    def setUp(self):
        """ pass """
        data = {'username': '13500001234', 'password': '12574655'}
        resp = self.post(config.Login.api_url, json=data).json()
        if not resp.get('message') == 'success':
            raise AssertionError('用户登陆失败， 请重新配置用户登录数据！！！')

    def test_query_userinfo_is_ok(self):
        """ [查询用户信息][成功] 正常的get请求可以获取到正确的返回结果 """
        resp = self.get(self.api_url, self.data_tmp).json()
        self.assertEqual(resp.get('code'), 200)
        self.assertEqual(resp.get('message'), 'success')
        self.assertIsNotNone(resp.get('attribute'))

    def test_query_userinfo_method_is_post(self):
        """ [查询用户信息][失败] 该接口只支持get方法请求， post方法返回405"""
        resp = self.post(self.api_url, json=self.data_tmp)
        self.assertEqual(resp.json().get('message'), 'The method is not allowed for the requested URL.')
        self.assertEqual(resp.status_code, 405)

    def test_query_userinfo_attribute(self):
        """ [查询用户信息][成功] 查询某个用户的用户信息并断言结果"""
        resp = self.get(self.api_url, self.data_tmp).json()
        attr = resp.get('attribute')[0]
        self.assertEqual(isinstance(attr, list), True)
        self.assertEqual(attr[0].get('id'), 1)
        self.assertEqual(attr[0].get('identity'), 'vip')
        self.assertEqual(attr[0].get('username'), 'yy')

    def test_query_userinfo_enum_type(self):
        """  [查询用户信息][成功] 查询所有用户的identity 枚举类型正确 """
        resp = self.get(self.api_url, self.data_tmp).json()
        attr = resp.get('attribute')[0]
        enum = sorted(list(set([item.get('identity') for item in attr])))
        self.assertEqual(self.assert_tmp.get('enum_type'), enum)
        # enum = [
        #     'admin',
        #     'vip',
        #     'user'
        # ]
        # result = []
        # for item in attr:
        #     result.append(item.get('identity'))
        # result = set(result)
        # result = list(result)
        # result = sorted(result)

