

# http://testerhome.com
# 他的规则 是把最后一个数字填写进去， 来请求对应的页面
# https://testerhome.com/topics/{}

# 实现一个class
# 可以通过手动输入， 请求对应id的网页 并获取标题及用户信息
# 实现一个方法， 获取0-300 id的页面数据
# 实现一个通用的 爬虫父类

import requests
from lxml import etree


class BaseCrawl:
	""" pass """
	session = requests.Session()
	base_url = 'https://testerhome.com/topics/{}'
	header_xpath = '//*[@id="main"]/div/div[1]/div[1]/div[1]/div/h1/text()'

	@classmethod
	def request(cls, url):
		""" pass """
		resp = cls.session.get(url)
		if resp.encoding != 'utf-8':
			resp.encoding = 'utf-8'
		if resp.status_code == 404:
			return 404
		return resp.text

	@classmethod
	def parse(cls, html, xpath):
		""" pass """
		return etree.HTML(html).xpath(xpath)

	@classmethod
	def get_all_urls(cls, num):
		""" pass """
		return [cls.base_url.format(url) for url in range(1, num +1)]


class TesterHomeCrawl(BaseCrawl):
	""" pass """

	@classmethod
	def get_one_page(cls, page_num=None):
		""" pass """
		obj = cls.request(cls.base_url.format(page_num))
		resp = obj if obj != 404 else 0
		if not resp:
			return "查询的页面走丢了"
		if page_num:
			return cls.parse(obj, cls.header_xpath)[1].strip()
		return '请输入一个正确的页面id ...'

if __name__ == '__main__':
	print(TesterHomeCrawl.get_one_page(3000))
	string = ' 123, 456, 789, 12345, 23456, 34567 '
	print(string.split(','))   # split 通过一个入参对string 进行分割
	print(string.strip())   # strip的作用是去掉一个字符串头和尾的空格 ， ！！！ strip不可以去掉一个字符串中间的空格

