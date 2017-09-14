
# string , list , tuple
# start = 0, end = 4, step = 1

# string = '和Raymond一起学Python'
# print(string[0:4])
# print(string[0])   # 和
# print(string[5])   # o


# function 函数
# 强类型语言


# def function_name():
# 	print("Hello, First Function")


# def get_user_info(name, age, sex):
# 	""" 获取一个用户信息 """
# 	print("my name is {}, age = {}, sex = {}".format(name, age, sex))


# def get_user_age(name):
# 	age = 20
# 	print('%s age is %s' % (name, age))
# 	return age


# def give_me_apple(apple):
# 	print('i will give you {}'.format(apple))
# 	# 他说 他准备给我一个苹果， 但是他没有给 (print)
# 	return apple
# 	# 他没有说话， 但是他给了我一个苹果


# def print_and_return():
# 	print(1)   # 打印结果为1
# 	return 2   # 返回结果为2
# 	print(3)


# hive = ('张三', '30', '北京')   # h_user, h_age, h_city = hive
# oracle = ('张三', '31', '上海')   # o_user, o_age, o_city = oracle

# h_user, h_age, h_city = hive
# o_user, o_age, o_city = oracle

# print(h_user == o_user)
# print(h_age == o_age)
# print(h_city == o_city)

# def all_user_info(*args):
# 	""" args, 不确定数量的入参， 他传递进函数的， 是一个tuple类型
# 	"""
# 	a, b, c = args
# 	# list, tuple  常用的赋值方法， 如果args长度大于3， 则会报错
# 	print('a : {}\nb: {}\nc: {}\n'.format(a, b, c))


def all_user_info_kw(**kwargs):
	# python3.6 以前， dict 是无序的
	# 如果你需要一个有序的字典， 可以使用orderdict这个类库
	print(kwargs)
	dog = kwargs['last']
	# dog = kwargs['dog']   # 当字典中，不能存在[key], 则会报错
	ray = kwargs.get('Ray')   # 如果key=Ray 不存在， 则get方法返回None
	ray = kwargs.get('Ray', 'Raymond')
	# get(获取字典中的该key的值， default 默认值)
	print('dog : {}'.format(dog))
	print('ray : {}'.format(ray))


# def get_all(func, **kw):
# 	""" python中的函数， 可以接受一个function作为参数 """
# 	print(func)   # func.__name__ = all_user_info_kw
# 	func(**kw)


# def get_all_user_info(city):
# 	all_city = {
# 	    "北京": ['Ray', '阿智', '港', '平淡'],
# 	    "上海": ['摩羯', '狗子', '老黄', '打老虎']
# 	}
# 	return all_city.get(city, '您查询的信息不在我们的dict中')

# **, dict(first="Ray",second="平淡",third="阿智",last="狗子")) 
# **, kwargs


# 匿名函数 lambda

# 定义一个函数， 他接受2个参数， a, b
# 让这个函数 返回 a + b

# def add(a, b):
# 	return a + b


# _add = lambda a, b: a + b


# print(sorted(list(range(1, 20)), key=lambda x : str(x)))

# lambda _add 是函数名
# lambda 和 def
# a, b 都是入参
# a + b 都是返回


if __name__ == '__main__':
	# print(add(3, 5))
	# print(_add(2, 4))
	# print(get_all_user_info("北京"))
	# user_a, user_b, user_c, user_d = get_all_user_info("北京")
	# print(user_a, user_b, user_c, user_d)
	# get_user_info('Ray', 30, 'male')
	# print(get_user_age('狗子'))
	# print(give_me_apple('apple'))
	# print(print_and_return())
	# all_user_info('Ray', '港', '阿智')
	# all_user_info_kw(first="Ray", second="平淡", third="阿智", last="狗子")
	# get_all(
	# 	all_user_info_kw,   # 传入的是函数的对象
	# 	**dict(first="Ray", second="平淡", third="阿智", last="狗子")
	# )

	user = dict(a='ray', b='狗子')

	# **, user ==> dict(a='ray', b='狗子')
	# **, kw, dict(a='ray', b='狗子')
	def func(dt, **user):
		print('dt', dt)
		print('kw', kw)

	func(user)   # dt = user, func(user, {})
	func('', **user) # dt = '', **user = func('' ==> dt, a='ray', b='狗子')