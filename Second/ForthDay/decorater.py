

# AOP 面向切面编程
from functools import wraps


def log(func, *args):
	result =  func(*args)
	return result


def _log(func):   # 1
	# @wraps(func)
	def wrap(*args, **kwargs):
		print(3)
		print('当前即将运行的函数名是{}'.format(func.__name__))
		result = func(*args, **kwargs)
		print(5)
		print('这个函数已经完成， 输出结果 :{}'.format(result))
		print(6)
		return result   # 6
	return wrap   # 2


@_log # ==》 wrap ==》 result
# _log(who_am_i, *args, **kwargs)
# _log print当前即将运行的函数名是
# 执行 result = func(*(name, ), **kwargs)
# _log '这个函数已经完成， 输出结果
# return _log == result
def who_am_i(name):
	""" pass """
	print(4)
	return "my name is {}".format(name)


def get_city():
	""" pass """
	return 'beijing'

@_log
def get_aaa():
	return 'aaa'


class TestClassMethod:
	""" pass """

	@staticmethod
	def test_static():
		""" pass """

	@classmethod
	def test_classmethod(cls):
		""" pass """

	def test_instance_method(self):
		""" pass """


if __name__ == '__main__':
	# 一道重点面试题
	# python 中和java 有明确不同的地方
	# java 中method 和function是语义上的区别
	# 而在python中， 对象的绑定关系是有明确区分的
	print(TestClassMethod.test_static)   # function , 其实是一个函数， 因为他没有和类有绑定行为
	print(TestClassMethod.test_classmethod)   # 他绑定了class.__main__
	print(TestClassMethod().test_instance_method)   # 他绑定是这个类的实例对象
	# print(log(who_am_i, 'Ray'))
	# print(who_am_i.__name__)
	# print(who_am_i.__doc__)
	# print(''.center(20, "="))
	# print(get_city())
	# print(''.center(20, "="))
	# print(get_aaa())