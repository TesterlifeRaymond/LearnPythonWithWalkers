
import sys
from config import BaseConfig


class MeiZiTu(BaseConfig):
	def __init__(self):
		super(MeiZiTu, self).__init__()
		self.spider_info = self.recursion.get_value(self.enum, 'mzitu')
		self.start_url = self.recursion.get_value(self.spider_info, 'start_url')
		self.home_page_xpaths = self.recursion.get_value(self.spider_info, 'home_page_xpaths')
		self.base_url = self.recursion.get_value(self.spider_info, 'base_url')
	
	def get_tags_page_num(self, all_page_info):
		""" pass """
		page_urls, page_numbers, page_names = all_page_info[0], all_page_info[1], all_page_info[2]
		number = 0

		for page_url, page_num, page_name in zip(page_urls, page_numbers, page_names):
			all_page_num = int(int(page_num.split(' ')[-1].split('[')[1].split(']')[0]) / 4)
			print(all_page_num, page_name)   # 取出每个妹子有多少页图片

			for _page_num in range(1, all_page_num + 1):
				number += 1
				if number == 1:
					new_url = page_url
				else:
					new_url = page_url[:-5] + '_{}.html'.format(_page_num)
				# 取出所有妹子的 所有图片页面的url
				print(new_url, page_name)

	def get_home_page(self):
		all_page = self.get_all_page()
		all_page.append(self.start_url)
		for item in all_page:
			param = self.output(self.start_url, self.home_page_xpaths)
			print(self.get_tags_page_num(param))

	def get_all_page(self):
		""" pass """
		all_page_num = self.recursion.get_value(self.spider_info, 'all_page_num')
		# all_page_num = 25
		# result = []
		# for page_num in range(2, 25 + 1):   # for page_num in range(2,all_page_num + 1)
		# 	result.append(self.base_url.format(page_num))
		# return result
		return [self.base_url.format(page_num) for page_num in range(2,all_page_num + 1)]

	def main(self):
		self.get_all_page()