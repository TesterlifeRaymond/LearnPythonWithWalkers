""" python 第二期 第二天课程 """
# python 基础数据类型

# string =  ''' '''or """ """ or " " or ''   # type(string) ==> str
# int = 123 or 456 or 789   # 整形
# list = [1, 2, "a", tuple(), list(), set()]   # list 类型 java 数组。 list是可变的
# tuple = (1, 2, "a", tuple(), list(), set()
# # tuple 类型 元组， 它与list最大的区别，tuple是不可变的
# dict = {"name": "Raymond", "age": 28, "city": "BeiJing"} or \
# 	dict(name='Ray', age=30, city='ShangHai')
# float = 1234.5678   # 浮点型

# type()
# 接受一个对象，接受参数， 并返回这个参数的类型

# print(type(111), 'int')
# print(type('111'), 'str')
# print(type([1, 2, 3, 4, 5, 6]), 'list')

# # list() = []
# print(type(list()))

# # tuple = ()
# # [1, 2, 3, 4, {'set', 'set1'}, (1,2,3)]  type() == > list
# print(type((1, 2, [3, 4]), 'tuple')
# print(type(dict(a=1, b=2, c=3)), 'dict')
# print(type({'abc', 'cde', 'cde'}), 'set')
# print(type(True or False), 'bool')
# print(type(123.456), 'float')


# # type, isinstance

# print(isinstance('string', str))
# print(isinstance(12345, int))
# print(isinstance(1234.5678, float))
# print(isinstance(True, bool))
# print(isinstance(dict(), dict))
# print(isinstance({123, "456", "789"}, set))
# print(isinstance((), tuple))
# print(isinstance([], list))


# 解析 / 切片/ 取值
# 迭代器 。

# 可迭代的数据类型， str, dict, list, tuple, set

string = "Raymond"
_list = ['R', 'a', 'y', 'm', 'o', 'n', 'd']
_tuple = ('R', 'a', 'y', 'm', 'o', 'n', 'd')
# index

number_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print(string[5])
print(string, string[0], string[-1])
print(_list, _list[0], string[-1])
print(_tuple, _tuple[0], _tuple[-1])

# # index, end

print(string[3:5])   # 切片 从第3个位置开始,包含3， 到第5个位置结束， 不包含5
print(string[2:4])   # 切片 2：4

# 切片中的第三个位置的参数， 为step 步长

print(_list[::2])
print(number_list[::4])   # [1, 5, 9]
print(number_list[::])

# number_list.reverse()	# reverse 反转一个迭代器
number_list[::-1]


print(number_list)

deal_tuple = ("user_id", "deal_info", "create_time")

number_list = list(range(11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 1 - 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] index : -1其实等于9
print(number_list[-1:])

print(number_list)
print(number_list[::5])
print(number_list[::-1])
print(number_list[-11:2])

# python 切片 list[start, end, step]
# python 切片 start, end, step=1
# index代表迭代器的索引， 它从0开始计算， 最后一位为-1, step 步长
# 运算符



#（1,2,3,4,5）  [2:-3:step = 1]和[-3:2: step=-1]具体的区别是？
# 2
# []