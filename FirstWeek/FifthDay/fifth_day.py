

def function(name, *args, key=None, **kwargs):
	"""
	@param: name 必填参数
	@param: *args 不确定数量的非kw参数， args的类型为Tuple
	@param: key=value, 指定的kw入参
	@param: **kwargs 不确定个数的kw参数， kwargs的类型为dict
	"""


_lambda = lambda x, y: x + y
# lambda 是定义匿名函数的关键字
# x, y 代表定义的这个函数 需要两个入参a, b
# x + y 代表该函数运行后返回的结果


def add(a, b):
    """ return a + b """
    return a + b


def all_add(*args):
	""" pass """
	# list or tuple  并把他们所有位置相加的结果返回
	return sum(args)


# 循环
# for  or  while
# for 是遍历取值
# while 是进入一个死循环， 直到符合条件后退出， 否则持续循环

number_list = list(range(1, 21))


# for num in number_list:
# 	print(num)

# num = 0
# while num < len(number_list):
# 	print(number_list[num])
# 	num += 1

# if elif else
# 判断

# string = '' or ""
# int = 0
# list = []
# dict or set = {}
# None
# tuple = ()

# text = "string"
# number = 1

# # type(text) == str: ==> 类型判断
# # if isinstance(text, str): ==> 返回True or False 然后判断是否进入if
# # if text == 'string'
# # if text:

# if text == 1:
# 	print('text is a number , error !!!!!')
# elif number == 1:
# 	print(True)
# else:
# 	print('.....')


# def get_enu_value(user_type):
# 	""" dict[key]"""
# 	enu = {
# 		1: 666,
# 		2: 'error',
# 		3: 'pass',
# 		4: 'success'
# 	}.get(user_type, 'element is not define...')
# 	return enu

# my_dict = {
# 	1: 666,
# 	2: 'error',
# 	3: 'pass',
# 	4: 'success'
# }
# my_dict[1]
# my_dict.get(1)
# my_dict[1] = 777   如果key存在， 则改变key的value
# my_dict["1"] = 888888
# # 如果my_dict中不存在key为"1"的value时， 则添加这对key=value

# my_list = list(range(1, 21))
# # my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # tuple可以通过下标进行取值， 但是不可以修改内部的item

# my_string = 'abcd123456789'
# my_string = list(my_string)
# my_string[0] = "Raymond"
# # ''.join()
# print(''.join(my_string))

# # generator
# (num for num in (range(1, 21)))


# number_list = [1, 2, 5, 10, 1, 5, 11, 100, 119, 11, 12, 15, 22, 25, 99, 22, 100]
# 修改number_list 第5个位置的值
# 删除number_list 中的一个元素
# 删除指定位置的元素
# 增加一个元素
# 合并两个list
# 通过for 或者 while 循环 配合if 实现list去重


number_list = [1, 2, 5, 10, 1, 5, 11, 100, 119, 11, 12, 15, 22, 25, 99, 22, 100]
# [1, 2, 5, 10, 11, 100, 119, 12, 15, 22, 25, 99]

# list.append(param)
# [].append(param)
def duplicate_removal(my_list):
    """ pass """
    result = []
    for num in my_list:
    	if num not in result:
    		result.append(num)
    return result

def remove(my_list):
	result = []
	num = 0
	while num < len(number_list):
		if number_list[num] not in result:
			result.append(number_list[num])
		num += 1
	return result


if __name__ == '__main__':
	# dir
	# print(dir(list))
	# print(dir(tuple))
	# print(dir(dict))
	# print(dir(remove))
	# 我们不清楚一个方法或者类如何使用的时候， 可以用dir(param)
	# print(dir(list))
	# print(number_list)
	# print(number_list.pop())
	# print(number_list.index(5))
	# copy_number_list = number_list.copy()
	# # deepcopy
	# print(copy_number_list)
	# my_dict = {
	# 	1: 666,
	# 	2: 'error',
	# 	3: 'pass',
	# 	4: 'success'
	# }

	# print(my_dict.items())
	# for key, value in my_dict.items():
	# 	print(key, value)

	# map  这个python3的官方文档中已经明确不建议使用。
	# reduce 这个是配合匿名函数用比较多
	# math
	# re
	# for key, value in zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']):
	# 	print(key, value)


	# string
	# python2 unicode str utf-8

	# 有一个函数
	# 这个函数接收2个参数
	# 如果第一个参数类型为string ， 则修改第二参数类型为str ， 并返回两个参数相加的结果
	# if type(param_a) == str or if isinstance(param_a, str):
	# 如果第一个参数为int， 则判断第二个参数是否为list， 如果为list 则将第一个参数添加到list中
	# 如果第一个参数为int， 第二参数不为list， 则判断第二参数是否为int ， 如果为int， 则返回相减的结果
	# 如果 第一个参数为dict，则把第二个参数当作第一个参数的value


	# def function(param_a, param_b):
	# 	""" pass """
	# 	if isinstance(param_a, str):
	# 		return param_a + str(param_b)

	# 	if isinstance(param_a, int):
	# 		if isinstance(param_b, list):
	# 			param_b.append(param_a)
	# 			return param_b
	# 		if isinstance(param_b, int):
	# 			return param_a - param_b
	# 		else:
	# 			return False

	# 	if isinstance(param_a, dict):
	# 		if param_a.get('city') is None:
	# 			param_a['city'] = param_b
	# 			# param_a[key] = value
	# 			return param_a
	# 		return param_a.get('city')

	# info = dict()
	# info['abc'] = 123
	# info['bcd'] = 456
	# print(info)

	# # print(function("Raymond", {"北京": "Raymond", "上海": "狗子"}))
	# # print(function(123456, [67890, 12345, 'abcde']))
	# # print(function(1234567, 12345))
	# print(function(1234567, "string"))


	# 有一个函数
	# 这个函数接收三个参数， a, b, c=运算符
	# 先判断 c 的类型是什么
	# a 或 b  不是int 类型， 则返回错误信息（print)
	# 如果 c = + , 则 a + b >= 100 , 则返回， 这两个数字相加超过100
	# 如果c = * ，则 a * b > 1000 ， 并且a + b < 100 则打印， 这两个数字的信息的字符串 "a {}, b {}".format()
	# 如果c = - , 则 a - b < 0, 则返回 a - b
	# 如果上述条件均不符合， 则返回 一句自定义的话
	

	def function(param_a, param_b, parse):
		""" pass """

		if not isinstance(param_a, int) or not isinstance(param_b, int):
			return "a or b参数类型错误"

		if parse not in ["+", "-", "*"]:
			return "你输入的运算符是错误的"

		if parse == '+' and param_a + param_b >= 100:
			return 	"这两个数字相加超过100, a + b = {}".format(param_a + param_b)

		if parse == '*' and param_a * param_b > 1000 and param_a + param_b < 100:
			return "param_a : {},\nparam_b : {},\nparam_a * param_b {},\nparam_a + param_b {}".format(param_a, param_b, param_a * param_b, param_a + param_b)

		if parse == '-' and param_a - param_b < 0:
			return "a - b = {}".format(param_a - param_b)

		return "这真是一个神奇的错误"
