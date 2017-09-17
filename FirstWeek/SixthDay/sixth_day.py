# -*- encoding: utf-8 -*- 

# 一个不同类型的数据操作
# 函数的操作
# 包括函数的入参
# 函数的不确定类型的参数传递
# for while 循环的应用
# if elif else的操作


# 我们做一个猜数字游戏
# 用户先定义一个数字
# 然后 让使用者去猜这个数字是多少？
# 如果传递的参数大于我们定义的数字， 则打印太大了， 请重试
# 如果传递的参数小于我们定义的数字， 则打印大小了， 请重试
# 如果相等， 则打印猜对了的正确信息

# user_input = input('> 请输入你要猜的数字：')


num = 66

while 1:
	user = int(input('请输入一个数字： '))

	if num == user:
		print('恭喜你！！ 猜对了！')
		break

	if user > num:
		print('您输入的数字太大了， 请重试！')

	elif user < num:
		print('您输入的数字太小了， 请重试！')

	else:
		print('未知的错误信息， 请重新输入。')


# 港同学的课堂答题笔记

num = 9
# while 1 比 while True 性能上 略微好一丢丢
while 1:
    user = int(input('请输入一个数字: '))
	  # input 接受一个参数， 为str类型
    if user == num:
    	print("恭喜你， 猜对了。")
    	break
	  # 如果猜对了， 需要在while 循环中， 加上break 跳出循环
    if user < num:
        print('太小了，请重试')
    elif user > num:
        print('太大了，请重试')
	



# 我们做一个数字判断
# 我们定义一个函数， 这个函数接收2个必填参数
# 一个参数是随机数， 一个是用户定义的数字
# 随机获得一个数字， 判断这个数字的大小
# 如果这个数字大于50， 则打印随机数 - 用户定义的数字的值
# 如果这个数字小于50， 则返回随机数 + 用户定义数字的值
# 如果这个数字不在我们定义的区间中， 则返回错误信息

import random

# print(random.randint(1, 100))


def function(random_number, user_input_number):
	""" 这是要给判断两个数字大小的函数 """
	if random_number > 50:
		print(random_number - user_input_number)
	elif random_number < 50:
		print(random_number + user_input_number)
	else:   # random_number == 50
		print(random_number, user_input_number)
		print("未知的错误信息， 请重新输入。")


function(random.randint(0, 101), 66)


import random
# 编写一个随机生成手机号的函数
# 我们可以把不同的号段， 放入一个list中进行管理， 然后随机从list取出一个号段
# 然后生成一个11位的手机号

# prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147",
#       "150", "151", "152", "155", "156", "157", "158", "159", "186", "187",
#       "188"]
# ''.join(list)， 可以把一个list 变为字符串
# prelist[5] or random.choice(prelist) + random.randint(10000000, 99999999), "153"


def get_user_mobile():
    """ 这是一个生成随机手机号的函数 """
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + str(random.randint(9999999, 99999999))
 

def get_all_user_mobile():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147",
    	"150", "151", "152", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + ''.join([str(random.choice(list(range(10)))) for _ in range(8)])

print(get_all_user_mobile())


print([num for num in range(21, 99) if num % 2 == 0])

# 列表推导式
# 字典推导式
# 生成器

# 编写一个中文名字的生成函数
# 他可以是随机自动生成2个字的名字， 或者 3个字的名字
# 如果用户自己填写了一个姓氏， 则按照用户填写的姓氏生成一个名字


FIRST = """赵钱孙李周吴郑王冯陈楮卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闽席季麻强贾路娄危江童颜郭梅盛林刁锺徐丘骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麹家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘斜厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逑盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐锺离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木巫马公西漆雕乐正壤驷公良拓拔夹谷宰父谷梁晋楚阎法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生岳帅缑亢况后有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟"""
LAST = """刚强仁发民国忠艺文德志智辉华军生裕健炎宏毅坚石超鹏亮锦家春磊勇正东南斌武奎秋鑫伦朋隆宝靖俊杰友祖颂小宇兴波荣峰祥思振海凯远汉桥松柏利大宁晓军明泽培太博燕虹菁丽娟莘苹红玉妙丹芸香蕾兰慧玲静茹怡紫花华芳芬牛海奎知道是故古之王者建国君民教学为先"""


def get_user_name(first_name=None):
	if first_name:
		return first_name + random.choice(list(LAST))
	else:
		roll = random.randint(1, 101)
		if roll > 50:
			return random.choice(list(FIRST)) + random.choice(list(LAST))
		return random.choice(list(FIRST)) + random.choice(list(LAST)) + random.choice(list(LAST))


print(get_user_name('夏侯'))


# 如何快速的生成一个不重复的数字list
print(list(set(list(str(random.randint(1, 9)) for _ in range(11)))))


import string
pre = ['中文', 1234, 4567, 'abc', 'Raymong', 'uiasdfas', '北京', '上海', 'basdf', 12341, 56789, '成都', 'aabad']
# 编写一个函数， 把这个list中的三种类型的元素， 分成三个list显示出来。
# ENU
# MESSAGE
# re


def parse_list(prelist=pre):
	""" 编写一个函数， 把这个list中的三种类型的元素， 分成三个list显示出来。 """
	number_list, string_list, chinese_list = [], [], []
	for item in prelist:
		if type(item) == int:
			number_list.append(item)

		elif item[0] not in string.ascii_letters:
			chinese_list.append(item)
		else:
			string_list.append(item)

	print('number_list: ', number_list)
	print('chinese_list ', chinese_list)
	print('string_list ', string_list)

parse_list(pre)
