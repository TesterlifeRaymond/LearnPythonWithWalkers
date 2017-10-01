
""" pass """

from core.recursion import GetDictParam
from core.http import HttpHandler


class BaseConfig(GetDictParam, HttpHandler):
	""" pass """
	enum = {
		"mzitu": {
			"all_page_num": 25,
			"start_url": "https://www.meitulu.com/t/nvshen/",
			"base_url": "https://www.meitulu.com/t/nvshen/{}.html",
			"xpaths": {
				"home_page_xpaths": [
					'//ul[@class ="img"]/li/a/@href',
					'//ul[@class ="img"]/li/a/img/@alt',
					'//ul[@class ="img"]/li/p[3]/a/text()'
				],
				# index 0: home_page_urls
				# index 1: home_page_numbers
				# index 2: home_page_names
				"download_img_xpaths": [
					'//div[@class ="content"]/center/img/@src',
					'//div[@class ="content"]/center/img/@alt',
				],
				# index 0: url
				# index 1: name
				"down_img_url": [
					"//img/@src"
				]
			}
		},
		"qiubai": {
			"start_url": "https://www.qiushibaike.com",
			"next_url_tmp": "https://www.qiushibaike.com/8hr/page/{}",
			"xpaths": [
				'13',   # all page number
				('//*[@class="col1"]/div[starts-with(@id,"qiushi")]'
					'/a[@class="contentHerf"]/@href'),   # all_page_content_url
				'//*[@id="single-next-link"]/div/text()',   # contents
			]
		},
		'budejie': {
			"start_url": "http://www.budejie.com/text/",
			"xpaths": [
				'//*[@class="j-r-list-c-desc"]/a/@href',   # all_page_content_url
				'//a[@class="u-user-name"]/text()',   # user name
				'//div[@class="j-r-list-c-desc"]/h1/text()',   # contents
				'//*[@class="j-r-list-tool-l-up"]/span/text()',   # up
				'//*[@class="j-r-list-tool-l-down "]/span/text()'
			]
		}
	}

	def __init__(self):
		""" pass """
		self.recursion = GetDictParam()
		self.get_value = self.recursion.get_value
		self.list_for_key_to_dict = self.recursion.list_for_key_to_dict
