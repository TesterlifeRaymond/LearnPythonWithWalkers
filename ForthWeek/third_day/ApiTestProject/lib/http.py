""" pass """

import json
from jsonschema import validate
import requests
from . import recursion
from functools import wraps
from time import time


def request_info_wrap(func):
    """ pass """
    @wraps(func)
    def wrap(*args, **kwargs):
        """ pass """
        print('当前调用函数 {},'.format(func.__name__))
        print('当前函数入参包含', args)
        print('当前函数keywords入参包含', kwargs)
        return func(*args, **kwargs)
    return wrap

# request_info_wrap(func, *args, **kwargs):
#    print('当前调用函数 {},'.format(func.__name__))
#    print('当前函数入参包含', args)
#    print('当前函数keywords入参包含', kwargs)
#    return func(*args, **kwargs)

# request_info_wrap(get, *args, **kwargs)


def load_time(func):
    """ pass """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time() - start
        print(func.__doc__)
        print('当前测试方法{}， 执行完成，耗时 {}'.format(func.__name__, end))
        return result
    return wrapper


class HttpHandler(recursion.GetDictParam):
    """ pass """
    session = requests.Session()

    @classmethod
    @load_time
    @request_info_wrap
    def get(cls, url, params=None):
        """ 这是get方法的docstring """
        # 1
        return cls.request('get', url, params=params)   # 2

    @classmethod
    @load_time
    @request_info_wrap
    def post(cls, url, **kw):
        """ 这是post方法的docstring """
        if kw.get('json'):
            return cls.request('post', url, json=kw.get('json'))
        return cls.request('post', url, data=kw.get('data'))

    @classmethod
    @load_time
    @request_info_wrap
    def request(cls, method, url, **kwargs):
        """ kwarg
        # method : get, post, put, delete, head, option
        ： headers
        ： cookies
        ： json={1: 2, 3, 4}
        ： data = {}
        """
        if method in ['get', 'GET', 'Get']:
            # 3
            return cls.session.get(url, **kwargs)
        if kwargs.get('json'):
            return cls.session.post(url, json=kwargs.get('json'))
        return cls.session.post(url, data=kwargs.get('data'))

    @classmethod
    def valid_json(cls, myjson, class_name, schname):
        """ 按照jsonSchema格式校验jsonkey、jsonkeyType、jsonCount """
        schfile = 'schema/%s/%s.json' % (class_name, schname)
        with open(schfile, 'r') as f:
            mysch = json.load(f)
        try:
            validate(myjson, mysch)
        except Exception as e:
            return e
        else:
            return True
        finally:
            pass
