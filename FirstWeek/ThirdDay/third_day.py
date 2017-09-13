

# string 字符串类型  text = '' or "" or """ """ or ''' '''
# int 整形 12345， 1 ， -1 ， 100000000000000
# list 列表 (数组) [1, 2, 3, 4, 5, tuple(), "string"]
# tuple 元组 (与列表最大的不同， 在于元组不可被改变) ("string", 1000, [1, 2, 3], set())
# set 集合 {123, "string", [123, 456, 789], ()}
# dict 字典 {"key": "value", "name": "Ray", "age": 29}
# bool 布尔 True or False
# float 浮点型 123.456， 567.678， 3.0，4.0

# print("""这是docstring这是第二行\r\n\t 123456""")

# iterator
# 类型判断  type or isinstance
# type(param) ==> 这个参数的类型  param
# print(type(1234)) ==> int
# print(type([]))  ==> list

# isinstance
# print(isinstance(param, info))  
# isinstance('string', str)
# isinstance(123456, int)

# 使用type or isinstance 之后 都会返回Bool ==》 True or False

# print(type(123)) #==> int
# print(isinstance(123, int))

# 切片
# str, list, tuple
text = 'string'
# text_list = [1, 2, 3, 5, 6, 7]
# text_tuple = (1, 2, 3, 4, 5, 6)

# print(text[1])	# t
# print(text_list[2])	# 3
# print(text_tuple[3])   # 4
# index, start = 0, end = -1, step = 步长

# print(text[::2])   # 步长为2进行切片 返回s, r, n
# print(text[::-1])
# print(text[~1])

# 运算符
# + - * /
# Python 是强类型语言

# print(1 + 2)
# print([1, 2, 3] + [4, 5, 6])
# print("string" + "Hello" + "World!")
# print([1, 2, 3] * 2)
# print(len([1, 2, 3]) / 3)

# name = "Ray"
# age = "30"
# sex = "male"

# text = name + "," + age + "," + sex
# print(text)

# url = base_url + /hello
# public_key = sec_1 + sec_2 + json

# print(30 / 3)
# print("string" * 2)
# print([4, 5, 6, 7, 8, 9] * 2)

# pi = 3.1415926535897
# print(3 / 1.5)

# function 函数

# self.driver.find_element_by_id()
# module

# def get_file_path():
# 	return __file__

# def get_name():
# 	return __name__

# def print_message():
# 	print("Hello World !")


# def get_args_and_return(name, age, sex):
# 	""" 接受3个参数 三引号内 是函数的注释
# 	@param: name 
# 	@param: age 
# 	@param: sex 
# 	@return: "my name is {}, age = {}, sex = {}"
# 	# *, name=None
# 	# text = name + "," + age + "," + sex
# 	"""
# 	return "my name is {}, age = {}, sex = {}".format(name, age, sex)


# def get_args_and_return_(name, age, sex):
# 	""" pass """
# 	return "name %s, age %s, male %s" % (name, age, sex)


def test_return_and_print(apple):
	""" 1： 函数中， print 语句可以多次打印
	2： return语句 一旦被触发， 则代表return 之下的全部语句将不会被执行
	3: 返回值 是由return 这个关键字返回
	"""
	print("i will give you an {}".format(apple))
	print(1)
	print(apple * 2)
	print(2)

# format 是字符串格式化
# "name {}, age {}, male {}".format(1, 2, 3)
# "name %s, age %s, male %s" % (name, age, male)


def get_apples(*args):
	"""
	param : name, apple, age
	param : *args  代表非固定数量的入参
	"""
	age = args[0]
	apple = args[1]
	print("age", age)
	print("apple", apple)
	# *args  所有参数不做任何处理的情况下
	# args
	# print(len(args))   # len 内置函数， 获取一个参数的长度
	# # 参数类型可以为 ： str, list, dict, set, tuple
	# print(args)

def function_keywords(name=1, age=2, city='北京'):
	""" pass """
	print(name, age)

def function_keywords_kwargs(*gs):
	""" **kwargs 代表非固定数量的 keywords入参
	# name, age 这是固定长度必填参数， 如果不输入 则调用函数会报错
	# *args 非固定长度的入参， type(args) ==> tuple
	# **kwargs 非固定长度的键值对入参， type(kwargs) ==> dict
	"""
	print(kwargs)

# def function_keywords_list(user_list=None):
# 	user_list.append(1)   # user_list = [1]
# 	return user_list*kwar

if __name__ == '__main__':
	# get_apples(1, 'apple')
	function_keywords_kwargs(**dict(name='Ray', city='shanghai', sex='male', _class='2班', _time='22:50'))
	# function_keywords(age=30)
	# test_return_and_print('apple')
	# user_info = get_args_and_return('Ray', 30, 'male')   
	# print(type(user_info))
	# apple = test_return_and_print("apple")
	# print("----" * 20)
	# print("apple: ", apple)
	# print 不会返回对象给变量
	# 一个人有一个苹果
	# 这个人说， 我把这个苹果送给你   print
	# 这个人， 把苹果直接给你放在手里   return 
	# return 是不会打印对象， 但是会把对象返回给调用者
	# print(get_args_and_return_('Ray', 30, 'male'))