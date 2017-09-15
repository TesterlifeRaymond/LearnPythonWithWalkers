
import time


def function():
	""" 在python中， def关键字代表定义一个函数 """
	print('my name is function')


def get_param(name, age, city):
	""" 获取这个函数中传递的参数， 并打印出来
	@name: 必填参数
	@age: 必填参数
	@city: 必填参数
	# 如果， 必填参数在调用函数时没有被传递， 则该函数会报错
	"""
	print("my name is {}, age = {}, city = {}".format(name, age, city))


def kw_param(name=None, age=None, city=None):
	"""
	name = None
	age = None
	city = None
	# 该函数接收的参数， 均有默认值， 所以调用该函数时， 可以缺省参数传递
	"""
	print("my name is %s, age = %s, city = %s" % (name, age, city))


def args_and_kwargs(*args, **kwargs):
	""" docstring
	# pylint
	# flake8
	# pylint 和 flake8 都是用于python代码的静态检查

	# type(args) == > tuple
	# type(kwargs) == > dict
	# args和kwargs 都是不确定参数(不确定数量， 不确定key值)
	"""
	print(type(args), args)
	print(type(kwargs), kwargs)


# 匿名函数

add = lambda x, y: x + y

# 对一个list 进行字典序排序
# print(sorted(list(range(1, 21)), key=lambda x: str(x)))


def add(x, y):
	""" 这是一个加法函数 """
	return x + y

args = ('Ray', 30, '北京')
kwargs = dict(name='狗子', age=20, city='上海')

# args_and_kwargs(*args, **kwargs)
# args_and_kwargs(args, kwargs)
# args_and_kwargs(args=args, kwargs=kwargs)



# 判断
# 循环

string = 'Raymond'
# python中的False 都有哪些呢？
# string = "" or '' or """"""
# int = 0
# list = []
# dict = {}
# set = {}
# False
# None

# text = list()   # False
# print(type(text))   # list

# # if True: 才会执行if下面的缩进代码
# # if False: 是不会打印if下面的缩进代码的
# # if后面的判断 ，是为真的， 并且以：结尾
# # if True

if text == 1:
	print(True)
elif text == "1":
	print("string")
elif type(text) == list:
	print("list")
else:
	print("element not in enu")

if not True:
	# if True 代表 True 为真
	# if not True 代表 not True 为假
	print('Raymond')
else:
	print('狗子')


# USER_TYPE = "False"
# # type(USER_TYPE) == > str 而不是bool
# # False  != False
# # == 代表判断两个值 相等
# # != 代表判断两个值 不相等

# if USER_TYPE:
# 	print("Hello World !")
# else:
# 	print("USER_TYPE is False")


# and 左边为True 和 右边也为True， 才会被认为是True
# or 左边或右边 有一个为True 时， 则会返回True
# pythonic

user_info = dict(name='Raymond', city='北京', age=30)

if user_info.get('name') == 'Ray':
	print('Hi {}'.format(user_info.get('name')))

elif user_info.get('age') == 31 and user_info.get('city') == "北京":
	print('o, he is Raymond')

elif user_info.get('age') == 30 or user_info.get('city') == '北京':
	print('6666666666666666')

else:
	print(".......")


def enu(user_type):
	# dict.get()， 如果没有被命中， 则返回None
	_enu = {
	    "北京": ['Ray', '港'],
	    "上海": ['dog', '摩羯'],
	    "重庆": ['小智', 'Nancy']
	}.get(user_type, "您查询的城市用户信息不存在！！！")
	# 判断的是 _enu.get() 是否为True
	return _enu

print(enu("四川"))



text = "北京"

if text == "北京":
	print(['Ray', '港'])
elif text == "上海":
	print(['dog', '摩羯'])
elif text == "重庆":
	pass
else:
	print('xxxx')


# 循环
# for while
# 是可迭代的对象
# str, list, tuple, dict, set, iterator 迭代器
# generator 生成器

for num in "12345":
	# 类型转换
	# num = "1" 我们需要把它转换成int类型， 则可以使用int("1")
	# num = "1" 而我们需要用它与一个type(int) == > 1 对比的时候， str(1)
	# break ==》 退出循环， 循环结束
	# pass ==》 占位， 不输出， 跳过（什么都不做）
	# continue ==》 跳出当前次循环
	if num == str(2):
		continue
	else:
		print(num)


for num in list(range(1, 21)):
	if num == 2:
		print(2)
		# 会
	elif num == 6:
		pass
		# 不会
	elif num == 12:
		continue
		# 不会
	elif num == 15:
		break
		# 不会
	else:
		# 不会
		# 12
		print('............')

num = 0
# num = 0
while True:
	# num = 2
	if num == 2:
		num += 1
		continue   # 跳出本次循环， 进入下一次循环
	num += 1   # num = num +1
	# num = 2
	print('这是一个死循环的第{}次'.format(num))
	time.sleep(1)   # 告诉线程， 休息1秒
	print("num", num)
	if num == 5:
		break

# while 1:
# 	for num in list(range(1, 21)):
# 		if num == 5:
# 			break   # break 只退出最近的一层循环
# 		time.sleep(1)
# 		print(num)


# number_list = [1, 2, 5, 10, 1, 5, 11, 100, 119, 11, 12, 15, 22, 25, 99, 22, 100]
# 修改number_list 第5个位置的值
# 删除number_list 中的一个元素
# 删除指定位置的元素
# 增加一个元素
# 合并两个list
# 通过for 或者 while 循环 配合if 实现list去重