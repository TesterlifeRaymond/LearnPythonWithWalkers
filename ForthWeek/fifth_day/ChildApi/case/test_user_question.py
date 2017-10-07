
""" pass """
import unittest
from lib import HttpHandler
from config import config
import json


class UserScoreApiTest(config.QueryUserScore, unittest.TestCase, HttpHandler.HttpHandler):
    """ Child的项目的历史纪录查询接口测试用例 """

    def setUp(self):
        """ pass """
        data = {'username': 'liujinjia', 'password': '123456'}
        resp = self.post(config.Login.api_url, json=data).json()
        if not resp.get('message') == 'success':
            raise AssertionError('用户登陆失败， 请重新配置用户登录数据！！！')
        self.username = resp.get('username')

    def test_query_user_score_is_ok(self):
        """ [历史纪录查询][成功] 正常登陆后， 查询用户历史数据正确 """
        self.data_tmp['username'] = self.username
        resp = self.post(self.api_url, json=self.data_tmp).json()
        resp = json.loads(resp)
        self.assertEqual(self.username, resp.get('username'))
        self.assertEqual(resp.get('message'), 'success')
        self.assertEqual(resp.get('code'), '200')

    def test_query_info_is_null(self):
        """ [历史纪录查询][失败] 新注册用户， 没有历史数据， 所以查询结果为null """
        self.data_tmp['username'] = self.mobile()
        resp = json.loads(self.post(self.api_url, json=self.data_tmp).json())
        self.assertEqual(resp.get('code'), '200')
        self.assertEqual(resp.get('username'), None)
        self.assertEqual(resp.get('message'), 'failed')
        self.assertEqual(self.valid_json(resp, 'score', 'not_user_score'), True)

    def test_query_user_score_api_method_is_get(self):
        """ [历史纪录查询][失败] 该接口不提供get方法请求数据， 所以执行结果失败 """
        self.data_tmp['username'] = self.username
        resp = self.get(self.api_url, params=self.data_tmp)
        status_code = resp.status_code
        self.assertEqual(status_code, 405)
        self.assertEqual('message' in list(resp.json().keys()), True)

    def test_query_user_score_ids(self):
        """ [历史纪录查询][成功] 获取全部的list答题记录的结果并于db中数据对比 """
        self.data_tmp['username'] = self.username
        resp = self.post(self.api_url, json=self.data_tmp).json()
        resp = json.loads(resp)
        score_list = eval(self.get_value(resp, 'response'))
        self.assertEqual(self.assert_tmp['score_ids'], [list(score_id.keys())[0] for score_id in score_list])