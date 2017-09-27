
import os
from requests import Session
import random
from lxml import etree


class BaseCrawl:
	""" pass """
	def __init__(self):
		self.session = Session()

	def request(self, url, encoding='gbk'):
		resp = self.session.get(url)
		# text  返回请求的字符串
		# json 它只能对返回json的接口进行取值， 如果是html 则会报错
		# content 他返回的 是一个bytes 自己额了字节流
		if encoding:
			resp.encoding = encoding
		return resp

	def parse(self, html, xpath):
		return etree.HTML(html).xpath(xpath)

	def output(self, url, xpath=None):
		html = self.request(url).content
		if not xpath:
			return html
		return self.parse(html ,xpath)


	def download_img(self, img_url_list, img_name_list):
		num = 0
		for img_url , img_name in zip(img_url_list, img_name_list):
			if not os.path.exists(os.path.abspath(img_name)):
				os.mkdir(os.path.abspath(img_name))
			img_urls = '//ul[@class="clearfix"]/li/a/@href'
			img = self.parse(self.request(img_url).content, img_urls)

			for img_id in img:
				num += 1 + random.randint(1000, 10000)
				# /bizhi/5983_74134_2.html
				img_id_pa = img_id.split('_')[1]
				# img_id.split('_') 代表着把/bizhi/5983_74134_2.html 字符串用_分割， 返回一个被分割的列表
				# ['/bizhi/5983', '74134, '2.html']
				# 74134
				base_url = 'http://desk.zol.com.cn/showpic/1920x1080_{}_{}.html'
				_img = self.output(base_url.format(img_id_pa, num), '//img/@src')[0]   # bytes类型的数据
				print(img_name, _img)
				print(os.path.abspath(img_name) + '/{}.png'.format(img_name + str(num)))
				with open(os.path.abspath(img_name) + '/{}.png'.format(img_name + str(num)), 'wb') as file:
					file.write(self.request(_img).content)


class DesktopImg(BaseCrawl):
	""" pass """
	# 爬虫和接口自动化的交互模式是一致的
	# http 交互
	# 爬虫中， 有大量的数据解析， 而接口测试，也有同样的工作量
	# 
	def __init__(self, start_url):
		super(DesktopImg, self).__init__()
		self.base_url = 'http://desk.zol.com.cn{}'
		self.start_url = start_url
		self.page_num = 50

	def get_all_img_pages_catory(self):
		all_type = '//dl[@class="filter-item first clearfix"]/dd[@class="brand-sel-box clearfix"]/a/@href'
		all_pages = self.output(self.start_url, all_type)
		all_list = [self.base_url.format(url) for url in all_pages]
		return all_list

	def get_all_types_img_list(self):
		result = []
		for page_num in range(1, self.page_num + 1):
			for url in self.get_all_img_pages_catory():
				result.append(url + str(page_num) + '.html')
		return result

	def start_download(self):
		all_img_url_types_xpath = '//ul[@class="pic-list2  clearfix"]/li/a/@href'
		all_img_title_xpath = '//ul[@class="pic-list2  clearfix"]/li/a/img/@title'
		for url in self.get_all_types_img_list():
			html = self.output(url)
			titles = self.parse(html, all_img_title_xpath)
			urls = self.parse(html, all_img_url_types_xpath)
			self.download_img([self.base_url[0:-2] + url for url in urls], titles)
			# return 


if __name__ == '__main__':
	desk = DesktopImg('http://desk.zol.com.cn/pc/')
	desk.start_download()