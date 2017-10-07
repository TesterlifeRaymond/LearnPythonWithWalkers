
""" pass """
import random


class Register:
    """ pass """
    api_url = 'http://182.92.178.14/api/v1/register'
    method = 'post'
    data_tmp = {"username": "", "password": ""}
    assert_tmp = {}


class Login:
    """ pass """
    api_url = 'http://182.92.178.14/api/v1/login'
    method = 'post'
    data_tmp = {'username': '', 'password': ''}
    assert_tmp = {}


class QueryUserInfo:
    """ pass """
    api_url = 'http://182.92.178.14/api/v1/userInfo'
    method = 'get'
    data_tmp = {}
    assert_tmp = {
        "enum_type": ['admin', 'user', 'vip']
    }


class QueryUserScore:
    """ pass """
    api_url = 'http://182.92.178.14/api/v1/userQuestion'
    method = 'post'
    data_tmp = {'username': ''}
    assert_tmp = {
        'score_ids': [3, 4, 5, 6, 7, 8, 9, 81, 82, 83, 84, 114, 115, 116]
    }


class QueryOneUserScore:
    """ pass """
    api_url = 'http://182.92.178.14/api/v1/userScore'
    method = 'post'
    assert_tmp = {
        'score_ids': [3, 4, 5, 6, 7, 8, 9, 81, 82, 83, 84, 114, 115, 116]
    }
    data_tmp = {'username': 'liujinjia', 'score_id': random.choice(assert_tmp.get('score_ids'))}
