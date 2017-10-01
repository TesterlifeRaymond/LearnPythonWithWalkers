import sys
from config import BaseConfig
import random
import time
import os


class QiuShiBaiKe(BaseConfig):
	def __init__(self):
		super(QiuShiBaiKe, self).__init__()
		self.crawl_info = self.recursion.get_value(self.enum, 'qiubai')
		self.start_url = self.recursion.get_value(self.crawl_info, 'start_url')
		self.next_url_tmp = self.recursion.get_value(self.crawl_info, 'next_url_tmp')
		self.all_page_number, self.all_content_href, self.contents = self.recursion.get_value(
			self.crawl_info, 'xpaths'
		)

	def get_all_page(self):
		return [self.next_url_tmp.format(url) for url in range(1, int(self.all_page_number) + 1)]

	def get_all_content_href(self):
		result = []
		for item in self.get_all_page():
			all_content_href = self.output(item, self.all_content_href)
			time.sleep(random.randint(0, 2))
			result.append([self.start_url + url for url in all_content_href if url])  # url /article/1922211.html
		return result

	def get_all_contents(self):
		for urls in self.get_all_content_href():
			# self.get_all_content_href() = list([], [], [] ....)
			for index, url in enumerate(urls):
				# index 0, url
				# index 1, url
				file_name = url.split('/')[-1] + '#{}'.format(index)
				# split('/') 对url进行分割， 分隔符为'/'
				content = self.output(url, self.contents)[0].strip()
				# content ==> list, content[0] ==> content , content.strip()
				self.write_file(file_name, content)
				time.sleep(random.randint(0, 2))

	def write_file(self, file_name, content):
		with open('file/{}.txt'.format(file_name), 'w', encoding='utf-8') as file:
			file.write(content)

	def main(self):
		self.get_all_contents()