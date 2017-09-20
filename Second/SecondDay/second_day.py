

class Pizza:
	""" pass """
	def __init__(self, name, price, num):
		self.name = name
		self.price = price
		self.num = num

	def get_pizza_name(self):
		""" pass """

	def get_pizza_price(self):
		""" pass """

	def get_pizza_num(self):
		""" pass """

	def get_pizza_info(self):
		""" pass """


class CheesePizza(Pizza):
	""" pass """
	def __init__(self, name, price, num):
		""" pass """
		super(CheesePizza, self).__init__(name, price, num)
	
	def get_pizza_name(self):
		""" pass """
		return self.name

	def get_pizza_num(self):
		return self.num
	
	def get_pizza_price(self):
		return self.price

	def get_pizza_info(self):
		return "这是一个{}pizza, 他的价格是{}, 还剩下几份{}".format(
			self.name, self.price, self.num
		)


class PureMeatPizza(Pizza):
	def __init__(self, name, price, num):
		super(PureMeatPizza, self).__init__(name, price, num)

	def get_pizza_name(self):
		""" pass """
		return '这是一个肉pizza ， 他的名字是{}'.format(self.name)

	def get_pizza_num(self):
		return '这是一个肉pizza ， 他还剩余{}'.format(self.num)
	
	def get_pizza_price(self):
		return '这是一个肉pizza ， 他的价格是{}'.format(self.price)

	def get_pizza_info(self):
		return "这是一个{}pizza, 他的价格是{}, 还剩下几份{}".format(
			self.name, self.price, self.num
		)


class BuildPizza:
	def __init__(self, name, price, num, pizza_type):
		# if pizza_type == 'chease':
		# 	self._build = CheesePizza(name, price, num)
		# elif pizza_type == 'meat':
		# 	self._build = PureMeatPizza(name, price, num)
		self.__build_obj = {
			"chease": CheesePizza,
			"meat": PureMeatPizza
		}.get(pizza_type)

		self.__build = self.__build_obj(name, price, num)

	def build(self):
		return self.__build.get_pizza_info()


class Peoples:
	""" pass """
	def __init__(self, name, user_type, age):
		""" pass """
		self.__name = name
		self.__user_type = user_type
		self.__age = age

	def get_user_info(self):
		""" pass """

	def get_user_works(self):
		""" pass """

	def get_user_type(self):
		""" pass """

	def modify_user_name(self, new_name):
		self.__name = new_name


class Student(Peoples):
	def __init__(self, name, user_type, age):
		# super(Student, self).__init__(name, user_type, age)
		Peoples.__init__(self, name, user_type, age)
		self.__name = name
		self.__user_type = user_type
		self.__age = age

	def __setter__(self):
		""" pass """

	def __getter__(self):
		""" pass """

	def get_user_info(self):
		""" pass """
		return "我的名字是{}, 我是一名{}, 我今年{}岁".format(self.__name, self.__user_type, self.__age)

	def get_user_works(self):
		""" pass """
		return "我是一名{}, 我正在读书".format(self.get_user_type())

	def get_user_type(self):
		""" pass """
		return self.__user_type

	def modify_user_name(self, new_name):
		self.__name = new_name


class Teacher(Peoples):
	def __init__(self, name, user_type, age):
		""" pass """
		super(Teacher, self).__init__(name, user_type, age)
		self.__name = name
		self.__user_type = user_type
		self.__age = age

	def get_user_info(self):
		""" pass """
		return "我的名字是{}, 我是一名{}, 我今年{}岁".format(self.__name, self.__user_type, self.__age)

	def get_user_works(self):
		""" pass """
		return "我是一名{}, 我正在一所学校教书".format(self.get_user_type())

	def get_user_type(self):
		""" pass """
		return self.__user_type

	def modify_user_name(self, new_name):
		self.__name = new_name


class Works(Peoples):
	def __init__(self, name, user_type, age):
		""" pass """
		super(Works, self).__init__(name, user_type, age)
		self.__name = name
		self.__user_type = user_type
		self.__age = age

	def get_user_info(self):
		""" pass """
		return "我的名字是{}, 我是一名{}, 我今年{}岁".format(self.__name, self.__user_type, self.__age)

	def get_user_works(self):
		""" pass """
		return "我是一名{}, 我在学校是一个电工".format(self.get_user_type())

	def get_user_type(self):
		""" pass """
		return self.__user_type

	def modify_user_name(self, new_name):
		self.__name = new_name


class GetUsers:
	def __init__(self, name, user_type, age):
		enu = {
			'Student': Student,
			'Teacher': Teacher,
			'Works': Works
		}
		self.user_type = user_type

		self.user = enu.get(user_type)(name, user_type, age)

	def get_user_info(self):
		if self.user_type == 'Teacher':
			self.user.modify_user_name('Ray')
		if self.user_type == 'Works':
			self.user.modify_user_name('狗子')
		return self.user.get_user_info()

if __name__ == '__main__':
	teacher = GetUsers('Raymond', 'Teacher', 30)
	print(teacher.get_user_info())

	student = GetUsers('港', 'Student', 20)
	print(student.get_user_info())

	worker = GetUsers('茶茶', 'Works', 30)
	print(worker.get_user_info())
	# 课后练习
	# 实现一个构造数据的类
	# 这个类包含 创建手机号方法， 可以自定义手机号已什么号段开头
	# 这个类包含 创建随机中文名的方法， 可以指定姓氏
	# 这个类包含 创建随机平台的email， 可以指定平台 aabbcc@163.com
	# 这个类包含 创建随机的密码， 可以指定长度， 随机或生成符合规则的随机密码 （只要中文的， 只要英文的， 只要数字的， 长度可以指定）

	# 我们有一个学校
	# 学校有3种类型的人群
	# 1： 学生， 2： 老师， 3：内勤人员
	# class 多态 继承 和封装， 实现不同人员的工作内容
	# class Peoples:
	#    def __init__(self, name, user_type, age)
	#    def get_user_info, name , 他的职责是什么, 这个人的age是多少
	#    def get_user_works()  这个人打工内容是什么。 打印一句描述工作的话
	#    def get_user_type()   可以动态的修改一个人的信息

	# cheese = CheesePizza('芝士Pizz', 100, 3)
	# print(cheese.get_pizza_info())

	# meat = PureMeatPizza('牛肉大葱', 200, 5)
	# print(meat.get_pizza_info())
	# build_pizza = BuildPizza('芝士Pizz', 200, 5, 'chease')
	# print(build_pizza.build())