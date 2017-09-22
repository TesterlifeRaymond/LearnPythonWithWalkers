

# 爬取http://jandan.net/duan 当前页面的段子 和用户信息
import requests
from lxml import etree
import json


class Base:
    """ pass """
    def __init__(self):
        """ pass """
        self.session = requests.Session()

    def request(self, url):
        """ pass """
        # base = Base()
        # base.request(url)
        return self.session.get(url).text

    def parse(self, html, xpath):
        """ pass """
        # base = Base()
        # base.parse(html, xpath)
        return etree.HTML(html).xpath(xpath)

    def output(self, url, xpath):
        """ pass """
        # base = Base()
        # html = base.request(url)
        # return base.parse(html, xpath)
        html = self.request(url)
        return self.parse(html, xpath)



class JdCrawl(Base):
	""" 获取煎蛋段子当前页面的 全部段子和对应的用户信息 """
	def __init__(self, url):
		super(JdCrawl, self).__init__()
		self.start_url = url

	def get_all_text(self):
		""" 获取全部段子 """
		texts_xpath = '//div[@class="text"]'
		elements = self.output(self.start_url, texts_xpath)
		result = []
		for item in elements:
			result.append(''.join(item.xpath('p/text()')))
		return result

	def get_all_user_info(self):
		""" 获取全部用户名 """
		user_xpath = '//div[@class="author"]/strong/text()'
		elements = self.output(self.start_url, user_xpath)
		return elements

	def get_all_text_and_userinfo(self):
		""" pass """
		for user, text in zip(self.get_all_user_info(), self.get_all_text()):
			print(user, '分隔符'.center(20, '='), text)

class GetAllJoker(JdCrawl):
	""" pass """
	def __init__(self, url):
		""" pass """
		super(GetAllJoker, self).__init__(url)
		self.url = url
		self.base_url = 'http://jandan.net/duan/page-{}#comments'
		# '[123]' ==> json.loads ==> [123]
		self.all_pages = json.loads(self.output(self.url, '//*[@id="comments"]/div[3]/div/span/text()')[0])[0]
		# page_num = self.output(self.url, '//*[@id="comments"]/div[3]/div/span/text()') == > ['[2731]']
		# page_num[0] ==> '[2731]' type == > str
		# json.loads(page_num[0]) == > '[2731]' == > [2731] list
		# json.loads(page_num[0])[0]
		# page = 2731
		print(self.all_pages)
		self.url_list = [self.base_url.format(url) for url in range(self.all_pages)]
		# base_url = 'http://jandan.net/duan/page-{}#comments'
		# result = []
		# for url in range(2731):
		#    result.append(base_url.format(url))

	def get_all_page_content(self):
		""" pass """
		user_xpath = '//div[@class="author"]/strong/text()'
		texts_xpath = '//div[@class="text"]/p/text()'

		for url in self.url_list:
			html = self.request(url)
			users = self.parse(html, user_xpath)
			contents = self.parse(html, texts_xpath)

			for user, content in zip(users, contents):
				print(user, '分隔符'.center(20, '='), content)


if __name__ == '__main__':
	joker = GetAllJoker('http://jandan.net/duan')
	joker.get_all_page_content()
	# crawl = JdCrawl('http://jandan.net/duan')
	# crawl = JdCrawl('http://jandan.net/duan/page-2730#comments')
	# crawl.get_all_text()
	# crawl.get_all_user_info()
	# crawl.get_all_text_and_userinfo()