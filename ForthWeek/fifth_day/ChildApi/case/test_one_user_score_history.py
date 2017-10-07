""" pass """

import unittest
from lib import HttpHandler
from config import config
import random


class UserHistoryApiTest(config.QueryOneUserScore, unittest.TestCase, HttpHandler.HttpHandler):
    """ Child的项目的查询用户某次历史答题记录接口测试用例 """

    def setUp(self):
        self.data_tmp = {'username': 'liujinjia', 'score_id': random.choice(self.assert_tmp.get('score_ids'))}

    def test_query_user_score(self):
        """ [查询用户某次历史答题记录][成功] 正常请求该接口， 并获得正确的返回结果 """
        resp = self.post(self.api_url, json=self.data_tmp).json()
        history = eval(self.get_value(resp, 'question'))
        self.assertEqual(len(history), int(self.get_value(resp, 'titleNum')))

    def test_query_user_score_is_null(self):
        """ [查询用户某次历史答题记录][失败] 当输入的id在db中不存在时， 返回结果 """
        self.data_tmp['score_id'] = 1000
        resp = self.post(self.api_url, json=self.data_tmp)
        # resp.status_code = 502
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('message'), 'failed')

    def test_query_user_method_is_get(self):
        """ [查询用户某次历史答题记录][失败] 当输入的id在db中不存在时， 返回结果 """
        resp = self.get(self.api_url, params=self.data_tmp)
        self.assertEqual(resp.status_code, 405)
        self.assertIsNotNone(resp.json().get('message'))
        # pymysql 
        # 不要去用mysqldb
