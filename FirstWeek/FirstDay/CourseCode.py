
"""
# -*- coding: utf-8 -*-
# @Author: SH-liujinjia
# @Date:   2017-09-11 21:45:22
# @Last Modified by:   SH-liujinjia
# @Last Modified time: 2017-09-12 10:24:30
# @github project: https://github.com/TesterlifeRaymond/Let-s-go-python-
"""

import keyword
# print('Hello World !', end=' ')
# print('Raymond_行者, 讲师')
# print(1234567890)
# print((12345, 56789, 67890))
# print("!@#$%^&*()_")

# print("狗子, 你好!")
# print('我要权限你!')


# type and instance
# type 用于获取, 当前输入的数据类型, 并返回
# instance ... instance(入参, 对比数据类型)

# text = '狗子, 我要权限你!'
# TEXT = '我从来都不变, 当然, 只是很少数的时候发生改变'
# integer = 1234567890    # int 整数类型
# floats = 91.32  # float
# tuples = ("狗子", 29, "male")
# kwlist = keyword.kwlist
# 我是谁 = "Raymond_行者"

# print(type(text), text)
# print(type(integer), integer)
# print(type(floats), floats)
# print(type(tuples), tuples)   # ('狗子', 29, 'male')  元组
# print(type(kwlist), kwlist)   # ['False', 'None', 'True', 'and'] 列表

# 打印 = print

# 打印(text)
# 打印(我是谁)
# text = 我是谁
# 打印(text)
# text 和 TEXT 并不是同一个对象
# 打印(TEXT)

# print('''我是Raymond''')

# decimal

# print(__file__)
# print(__name__)
# from test_import import *

if __name__ == '__main__':
    import keyword   # 引入keyword包
    """ 这是一行注释 """
    print   # 函数的应用
    print(end="")   # 修改print默认的分割符
    # 基础数据类型
    string = '' or "" or """ """ or ''' '''   # string
    integer = 100000123456   # int
    tuples = (1, 2, 'string', [], dict())   # tuple
    array = [1, "string", dict(), tuple()]
    print(string)
    print(integer)
    print(tuples)
    print(array)
    _dict = {"key": "value", "key1": "value1", "key2": "value2"}
    __dict = dict(key=123, key1=456, key2=789)
    print(type(_dict), _dict)
    print(_dict)
    print(__dict)

    import json
    # dict
    # json
    print(type(json.dumps(_dict)), json.dumps(_dict))    # 这是一个json 字符串
    string_dict = json.dumps(_dict)     # json.dumps 将字典类型 type(dict) -- > type(string) 转变为string类型
    # string_dict --> dict
    print(type(string_dict))
    _dict = json.loads(string_dict)
    print(type(_dict))
    # json包中, 常用的两个方法
    # 1: json.dumps     是将字典类型(dict) --> (string)
    # 2: json.loads     是将字符串类型(string) -- > (dict)
