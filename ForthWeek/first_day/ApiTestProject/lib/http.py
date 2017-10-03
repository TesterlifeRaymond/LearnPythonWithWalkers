""" pass """

import json
from jsonschema import validate
import requests
from . import recursion


class HttpHandler(recursion.GetDictParam):
    """ pass """
    session = requests.Session()

    @classmethod
    def get(cls, url, params=None):
        """ pass """
        return cls.request('get', url, params=params)

    @classmethod
    def post(cls, url, **kw):
        """ pass """
        if kw.get('json'):
            return cls.request('post', url, json=kw.get('json'))
        return cls.request('post', url, data=kw.get('data'))

    @classmethod
    def request(cls, method, url, **kwargs):
        """ kwarg
        # method : get, post, put, delete, head, option
        ： headers
        ： cookies
        ： json={1: 2, 3, 4}
        ： data = {}
        """
        if method in ['get', 'GET', 'Get']:
            return cls.session.get(url, **kwargs)
        if kwargs.get('json'):
            return cls.session.post(url, json=kwargs.get('json'), **kwargs)
        return cls.post(url, data=kwargs.get('data'), **kwargs)

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
