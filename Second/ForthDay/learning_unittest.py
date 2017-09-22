
import requests
from lxml import etree
import unittest
from unittest import TestCase


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


class TestCrawlInfo(TestCase):
	""" pass """

	@classmethod
	def setUpClass(cls):
		""" 每个测试类初始化一次 """
		# TestCrawlInfo.setUpClass()
		# 绑定关系 ==》 类本身
		cls.base = Base()

	def setUp(self):
		""" 每个测试方法初始化一次 """
		# test = TestCrawl()
		# 
		# test.setUp()

	def tearDown(self):
		""" 每个测试方法tearDown一次 """

	@classmethod
	def tearDownClass(cls):
		""" 每个测试类tearDown一次 """

	def test_001_base_class_ok(self):
		""" pass """
		self.assertEqual(bool(self), True)

	def test_002_base_request(self):
		""" pass """
		html = self.base.request('http://jandan.net/duan/page-500#comments')
		self.assertEqual('html' in html, True)

	def test_003_response_is_ok(self):
		resp = self.base.output(
			'http://jandan.net/duan/page-2731#comments',
			'//*[@id="comment-3569495"]/div/div/div[1]/strong/text()'
		)[0]
		self.assertEqual(resp, '光消失的地方')

if __name__ == '__main__':
	unittest.main()