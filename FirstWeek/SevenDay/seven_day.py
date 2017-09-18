

# # 基础函数的使用
# # 内置函数
# # 对象的方法应用


# # list

# print(dir(list))

# number_list = list()
# # print(number_list)

# number_list.append('Raymond')
# number_list.append('摩羯')

# print(number_list)

# copy_number_list = number_list.copy()
# copy_number_list.append('狗子')
# print(number_list)
# print(copy_number_list)


# number_list.append('港')

# print(number_list)
# print(copy_number_list)

# print(copy_number_list.count('Raymond'))


# range_roll_number_list = list(list(range(1, 5)) for _ in range(5))
# print("range_roll_number_list 中包含 {} 个 [1, 2, 3, 4] list".format(range_roll_number_list.count([1, 2, 3, 4])))

# print('删除元素前的列表为 {}'.format(number_list))
# print('删除了最后一位元素， {}'.format(number_list.pop()))
# print('删除元素后的列表为 {}'.format(number_list))

# number_list.remove('Raymond')
# print(number_list)

# print('number_list', number_list)
# print('range_roll_number_list', range_roll_number_list)
# number_list.extend(range_roll_number_list)

# print(number_list)
# print(number_list.index([1, 2, 3, 4]))

# number_list.insert(5, '00000')
# print(number_list)



# print(dir(dict))

# my_dict = dict(name='Raymond', age=50, city='北京')

# print('my_dict 中全部的keys {}'.format(my_dict.keys()))   # 是获取这个dict中全部的key的list
# print('my_dict 中全部的values {}'.format(my_dict.values()))   # 是获取这个dict中全部的value的list
# print('my_dict 中的全部键值对 {}'.format(my_dict.items()))   # 是一个list中包含多个键值对的tuple
# print('my_dict 中获取 name 的值为 {}'.format(my_dict.get('name')))   # 获取字典中key=name的值

# my_list = ['北京', '上海', '重庆', '四川', '厦门', '三亚']
# my_dict = dict.fromkeys(my_list, '默认的城市信息')
# print(my_dict)

# my_dict['北京'] = '28度'
# print(my_dict)	
# my_dict.update(三亚="35度")
# print(my_dict)

# print(my_dict.pop('厦门'))
# print(my_dict)


# my_list = ['北京', '上海', '重庆', '四川', '厦门', '三亚']
# # 我想对这个列表进行 升序排序
# print(sorted(my_list))   # sorted是不会修改list本身的元素index位置的
# my_list.sort()   # 会修改list本身的元素index位置
# print(my_list)

# number_list = list(range(1, 25))
# print(sum(number_list))   # sum 获取列表中 全部的参数想加的结果
# # print(sum(my_list))

# # python3 官方文档中， 有明确的定义， 不建议使用map
# # map 被各种推导式所取代


# numbers = [num for num in range(1, 11, 2)]
# print(numbers)

# result = []
# for num in range(1, 11, 2):
# 	result.append(num)
# print(result)

# cities = ['三亚', '上海', '北京', '厦门', '四川', '重庆']
# times = ['123', '456', '789', '1234', '2345', '5678']

# my_dict = {k:v for k, v in zip(cities, times)}
# print(my_dict)

# ['三亚', '上海', '北京', '厦门', '四川', '重庆']
# 我们有一个地名的list
# 如果list中循环出的元素 字符长度为3个， 则打印这个地名信息
# 如果list中的循环出的元素， 字符长度为2， 则添加到一个新的list中 并打印这个list
# 如果list中的循环出的元素， 字符长度大于3， 则输出这个地名， 并打印出这是第几个长度大于3的字符


# my_list = ['黑龙江', '内蒙古', '三亚', '上海', '北京', '厦门', '四川', '重庆', '呼和浩特', '亚历山大', '百慕大三角']
# d_list = []
# count = 0
# for item in my_list:
#    if len(item) == 3:
#       print(item)

#    elif len(item) == 2:
#       d_list.append(item)

#    elif len(item) > 3:
#       print(item)
#       count += 1
#       # count = count + 1
#       print(count)

# print(d_list)


# [1, 100, 22, 55, 223, 55, 44, 12345, 1000, 555]
# 我们有一个列表， 这个列表全是数字
# 我们用循环取值的形式遍历这个列表
# 如果这个数字大于1， 小于等于100， 则把这些数字的和打印出来
# 如果这个数字， 大于100 小于10000 则打印出这些数字的list
# 否则 打印这些数字

# num_list = []
# sum_num = 0
# num = [1, 100, 22, 55, 223, 55, 44, 12345, 1000, 555]

# for item in num:
#    if 1 < item <= 100:
#       sum_num += item
#       print("sum_num", sum_num)

#    elif 100 < item < 10000:
#       num_list.append(item)
#       print('num_list', num_list)

#    else:
#       print('未命中：', item)



my_dict = dict(user_name='港', age=20, city='北京', sex="male")

# 取出 这个字典的key， value  并打印出来 对应key的value
for key, value in my_dict.items():
	print(key, value)



num_list = [1, 2, 3, 4, 5]
name_list = ['Ray', '摩羯', '茶茶', '煎饼', '打老虎']

# 我们想把打印这样的结果 1: Ray, 2: 摩羯, 3:茶茶， 4： 煎饼， 5：打老虎

for num, name in zip(num_list, name_list):
	print(num, name)

"""
1 Ray
2 摩羯
3 茶茶
4 煎饼
5 打老虎
"""


# 打印 100以内， 可以被4 整除的数字
# for num in range(0, 100):
# 	if num % 4 == 0:
# 		print(num)


# for num in range(0, 101, 4):
# 	print(num)

# print(list(range(0, 101, 4)))


string = [1, 'string', 123, 'string2', 456, 'abc']

# 遍历列表， 打印所有的数字
# 遍历列表， 打印所有的字符串

# type or isinstance

for item in string:
	if type(item) == str:
		print('str：', item)
	elif isinstance(item, int):
		print('int: ', item)
	else:
		pass

# print([item for item in string if isinstance(item, str)])
# print([item for item in string if isinstance(item, int)])


