

from requests import Session
from lxml import etree


class HttpHandler:
	session = Session()
	header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2737.18 Safari/537.36',}

	@classmethod
	def request(cls, url, encoding='utf-8'):
		""" pass """
		resp = cls.session.get(url, headers=cls.header)
		if encoding:
			resp.encoding = encoding
		return resp

	@classmethod
	def parse(cls, html, xpath):
		""" pass """
		return etree.HTML(html).xpath(xpath)

	@classmethod
	def output(cls, url, xpaths=None):
		# self or cls
		html = cls.request(url).text.replace('<br>', '').replace('</br>', '')
		# xpaths = ['//title/text()', '//img/src']
		# [self.parse(html, xpath) for xpath in xpaths]
		# result = []
		# for xpath in xpaths:
		#    result.append(self.parse(xpath))
		# return result
		if isinstance(xpaths, list):
			return [cls.parse(html, xpath) for xpath in xpaths]
		return cls.parse(html, xpaths)