

class Student:
	""" student class """
	city = '北京'
	# 类属型

	def __init__(self, name, age, *args, **kwargs):
		""" 类的初始化行为 """
		# 实例属性
		self.name = name
		self.age = age
		self.abc = 'abc'

	def get_user_info(self):
		""" 获取完整的用户信息 """
		# self 代表类的实例对象
		# method  bound self
		# function 没有绑定关系的
		print(self)
		print('my name is {}, 我今年 {} 岁了， 我出生在 {}'.format(
			self.name, self.age, self.city
		))

	@classmethod
	def test_class_method(cls):
		""" 不用深度理解，有兴趣可以课后学习 """

	@staticmethod
	def test_static_method():
		""" 不用深度理解， 有兴趣可以课后学习 """


# print(Student.get_user_info)
# print(Student('name', 20).get_user_info)
# print(Student.test_static_method)
# print(Student.test_class_method)


class ClassName:
	def __init__(self, name, age, city):
		self.name = name
		self.age = age
		self.city = city

	def function(self):
		# self == instance
		print('my name is {}, 我今年 {}岁了，我出生在 {}'.format(self.name, self.age, self.city))


class AllStudent(Student):
	""" All Student class """
	def __init__(self, user_name, cls_num, school):
		self.cls_num = cls_num
		self.school = school
		self.name, self.age = 'Raymond', 30

	def get_user_info(self):
		""" 子类定义了一个父类中已存在的方法 """
		print('我是AllStudent Class 的method, 我什么都不想输出')
		return self.name, self.age, self.school, self.cls_num, self.city

	def get_user_info_self(self):
		print(self.get_user_info())


class Private:
	def __init__(self, name, age, inst):
		"""
		# __init__
		# __str__
		# __repr__
		# __len__
		# 在python中 被称之为双下函数
		# __name 定义的属性， 表示为私有属性, 在外部不可直接调用
		"""
		self.__name = name
		self.__age = age
		self.age = age
		inst.function()


class Student:
	""" pass """
	def __init__(self, user, age, city):
		""" pass """
		self.__user, self.__age, self.__city = user, age, city

	def get_user_name(self):
		pass

	def get_user_age(self):
		pass

	def get_user_city(self):
		pass

	def get_user_info(self):
		pass


class GetStudentInfo(Student):
	def __init__(self, user=None, age=None, city=None):
		self.__user = user
		self.__age = age
		self.__city = city

	def get_user_name(self):
		print(self.__user)

	def get_user_age(self):
		print(self.__age)

	def get_user_city(self):
		print(self.__city)

	def get_user_info(self):
		print('my name is {}, 我今年 {}岁了，我出生在 {}'.format(self.__user, self.__age, self.__city))


class GetPeopleInfo(Student):
	""" pass """
	def __init__(self, user, age, city):
		self.__user = user
		self.__age = age
		self.__city = city

	def get_user_name(self):
		print('my name is {}'.format(self.__user))

	def get_user_age(self):
		print('我今年 {} 岁'.format(self.__age))


if __name__ == '__main__':
	# 我们要制造不同的pizza 
	# 我们有一个基础的pizza 类
	# 然后通过继承和多态， 来实现不同pizza的制作， pizza信息， 和价格方法

	student = GetStudentInfo('Raymongd', '25', '上海')
	student.get_user_info()

	student = ClassName(name='王鹏', age=25, city='瑞金')
	private = Private('王鹏', 10000, student)
	print(private.age)
	ClassName.function(student)
	instance == self
	ClassName.function(self)
	self.get_user_info()
	instance = AllStudent(user_name='gang', cls_num='Python3', school='Raymond')
	print(instance.get_user_info_self())

	override
	oop 面向对象编程中
	有3大特性
	封装， 多态， 继承

	map_reduce = MapReduce()
	print(MapReduce)
	print(map_reduce)
	ray_student = Student(name='Raymond', age=30)
	print('ray_student object mem : {}'.format(ray_student))
	print(ray_student.get_user_info())
	dog_student = Student(name="狗子", age=18)
	gang_student = Student(name='gang', age=20)
	ray_student.city = '上海'
	ray_student.sex = 'male'
	dog_student.city = '成都'
	gang_student.city = '厦门'
	print(ray_student.name, ray_student.age, ray_student.city, ray_student.sex)
	print(dog_student.name, dog_student.age, dog_student.city)
	print(gang_student.name, gang_student.age, gang_student.city)

	print(instance_student.abc)
	print(instance_student)
	print(Student)
	print(instance_student.name, instance_student.age, instance_student.city)
	instance_student.get_user_info()
	print(Student.city)
	print(instance_student.city)


