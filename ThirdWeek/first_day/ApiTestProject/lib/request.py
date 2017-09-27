

from requests import Session
from lxml import etree


class Request:
	""" pass """
	session = Session()


	@classmethod
	def request(cls, url):
		cls.resp = cls.session.get(url)
		if cls.resp.encoding != 'utf-8':
			cls.resp.encoding = 'utf-8'
		return cls.resp

	@classmethod
	def parse(cls, html, xpath):
		return etree.HTML(html).xpath(xpath)

	@classmethod
	def get_status_code(cls):
		return cls.resp.status_code
