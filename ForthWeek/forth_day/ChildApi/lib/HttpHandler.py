
""" pass """
from requests import Session
from .constuction import Construction
from jsonschema import validate
import json

class HttpHandler(Construction):
    """ pass """

    session = Session()

    @classmethod
    def get_value(cls, my_dict, key):
        """
            这是一个递归函数
        """

        if isinstance(my_dict, dict):

            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if cls.get_value(my_dict.get(my_dict_key), key) or \
                                cls.get_value(my_dict.get(my_dict_key), key) is False:
                    return cls.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if cls.get_value(my_dict_arr, key) \
                        or cls.get_value(my_dict_arr, key) is False:
                    return cls.get_value(my_dict_arr, key)


    @classmethod
    def list_for_key_to_dict(cls, *args, my_dict):
        """
            接收需要解析的dict和 需要包含需要解析my_dict的keys的list

        :param my_dict: 需要解析的字典
        :param args: 包含需要解析的key的多个字符串
            # list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=dict)
        :return: 一个解析后重新拼装的dict
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: cls.get_value(my_dict, key)})
        return result

    @classmethod
    def request(cls, method, url, data=None, **kwargs):
        if method in ['get', 'GET']:
            return cls.session.get(url, params=data)
        elif kwargs.get('json'):
            return cls.session.post(url, json=kwargs.get('json'))
        return cls.session.post(url, data=data)

    @classmethod
    def get(cls, url, params):
        return cls.request('get', url, params)

    @classmethod
    def post(cls, url, data=None, **kwargs):
        return cls.request('post', url, data=None, **kwargs)

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