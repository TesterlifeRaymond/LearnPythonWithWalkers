

# def  ==》 定义一个函数 或 方法
# class ==》 定义一个类

# oop ==》 封装/继承/多态
import time
import requests
from lxml import etree
from functools import wraps

class People:
	""" 定义一个people的类 """
	# 类属型
	hello = 'hello'

	def __init__(self, city, sex, name):
		""" 这个类实例化时， 需要传入3个参数，city，sex， name """
		# self 是这个类的实例本身
		# self.xxx 代表类的实例属性
		self.city = city
		self.sex = sex
		self.name = name

	def people_say(self):
		""" 输出人说的话 """
		print('我是{}人, 我是一个{}生, 我的名字是{}'.format(self.city, self.sex, self.name))

	def people_sleep(self):
		""" 定义人的睡觉行为 """
		print('我是{}, 我现在要睡觉了。'.format(self.name))
		sleep_time = 10
		time.sleep(sleep_time)
		print('我睡了{}分钟, 我睡醒了'.format(sleep_time))

	def people_eat(self):
		""" 定义人吃饭的行为 """
		print('我要开始吃饭了....')


class Student(People):
	""" Student类 继承了People类 和他的类方法 """
	def __init__(self, city, sex, name):
		""" 初始化class  """
		super(Student, self).__init__(city, sex, name)

	def people_say(self):
		""" pass"""
		print('我是{}， 我的身份是{}'.format(self.name, Student.__name__))



def wrapper(func):
	""" pass """
	@wraps(func)
	def _wrapper(*args, **kwargs):
		""" pass """
		print('当前运行的函数是{}'.format(func.__name__))
		result = func(*args, **kwargs)
		print('当前这个函数的运行结果是【{}】'.format(result))
		return result
	return _wrapper




class TesterLifeCrawl:
	def __init__(self):
		self.url = 'http://testerlife.com'
		self.session = requests.Session()
		# tcp udp
		# requests.get() 与session.get()的区别？

	@wrapper
	def get_all_text(self, url, xpath):
		""" 获取全部段子 """
		elements = self.output(self.start_url, xpath)
		result = [''.join(element.xpath('p/text()')) for element in elements]
		return result
	
	@wrapper
	def parse(self, html, xpath):
		""" pass """
		# 接受一个html
		# 接受一个解析html 对应位置数据的xpath
		# etree ==》 html ==》 element
		# element.xpath(xpath) ==> '//title/text()' ==> 返回是html中title的返回值
		return etree.HTML(html).xpath(xpath)

	def get_page_html(self):
		""" pass """
		result = self.session.get(self.url)
		# session.get() ,  requests.get()
		if result.encoding != 'utf-8':
			result.encoding = 'utf-8'
		# response.text 返回一个字符串  str
		# response.content 返回的是一个bytes类型的数据流 b''  bytes
		# response.json() 返回一个json数据结构
		return result.text
	
	@wrapper
	def get_page_title(self):
		""" pass """
		return self.parse(self.get_page_html(), '//title/text()')[0]

	@wrapper
	def get_page_all_contents_titles(self):
		return ' , '.join(self.parse(self.get_page_html(), '//a[@class="article-title"]/text()'))


if __name__ == '__main__':
	crawl = TesterLifeCrawl()
	print(crawl.get_page_title())
	# print(crawl.get_page_all_contents_titles())
	# people = People('北京', 'male', '茶茶')
	# people.people_say()
	# people.people_eat()
	# people.people_sleep()
	# print('这是一个人的一天的行为')
	# student = Student('北京', 'male', '茶茶')
	# student.people_say()

