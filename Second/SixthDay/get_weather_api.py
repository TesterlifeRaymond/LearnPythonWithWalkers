

import requests
from lxml import etree
import json
import random
import xmltodict
import unittest
import HTMLTestRunner

class Base:
    """ pass """
    def __init__(self):
        """ pass """
        self.session = requests.Session()

    def request(self, url):
        """ pass """
        # base = Base()
        # base.request(url)
        resp = self.session.get(url)
        if resp.status_code != 'utf-8':
        	resp.encoding = 'utf-8'
        return resp.text

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

class Xml:
    """ 创建Xml 类"""
    @staticmethod
    def xml_to_json(xml_data):
        """
            接受一个xml，将其转换为json格式
        :param xml_data:
        :return:
        """
        return json.dumps(xmltodict.parse(xml_data), ensure_ascii=False, sort_keys=True)
    @staticmethod
    def json_to_xml(json_data):
        """
            接受一个json，将其转换为xml格式
        :param json_data:
        :return:
        """
        return xmltodict.unparse(json.loads(json_data))


class GetWeather(Base, Xml):
	""" pass """
	def __init__(self):
		""" pass """
		super(GetWeather, self).__init__()

	def get_city_code(self, url="http://flash.weather.com.cn/wmaps/xml/beijing.xml"):
		""" pass """
		xml = self.request(url) # ==> xml
		# xml_to_json = self.xml_to_json(xml)   # xml <tag a <>> == > json{'a':'b', 'c':'d'}
		# weather_dict = json.loads(xml_to_json)   # json ==＞dict 类型
		# beijing_info = weather_dict.get('beijing')   # 对字典进行了取值
		# beijing_city_info = beijing_info.get('city')   # 是对字典中北京所有城区的list 进行获取 list
		# random_beijing_city_param = random.choice(beijing_city_info)
		# print(random_beijing_city_param,  type(random_beijing_city_param))
		# return random_beijing_city_param.get('@url')
		# return random.choice(json.loads(self.xml_to_json(xml)).get('beijing').get('city')).get('@url')
		return 101010600

	def get_city_weather(self):
		""" pass """
		weather_url = 'http://www.weather.com.cn/data/cityinfo/{}.html'
		# weather_url  是接口地址
		return self.request(weather_url.format(self.get_city_code()))


class TestWeatherApi(unittest.TestCase):
	""" pass """
	@classmethod
	def setUpClass(cls):
		cls.dict_info = json.loads(GetWeather().get_city_weather())
		print(cls.dict_info)

	def test_weather_info_is_not_none(self):
		""" pass """
		self.assertEqual(self.dict_info is not None, True)

	def test_weather_info_keys(self):
		""" pass """
		# 获取的是完整返回的字典的第一个key == weatherinfo
		self.assertEqual(list(self.dict_info.keys())[0], 'weatherinfo')

	def test_city_info_is_ok(self):
		""" pass """
		# self.dict_info.get('weatherinfo').get('city') == 》 city的值 预期 == 平谷
		self.assertEqual(self.dict_info.get('weatherinfo').get('city'), '平谷')

	def test_city_code_is_ok(self):
		# self.dict_info.get('weatherinfo').get('cityid') ==》 cityid的值 预期 == '101011500'
		self.assertEqual(self.dict_info.get('weatherinfo').get('cityid'), '101011500')



if __name__ == '__main__':
	# unittest.main()
	import os
	testunit=unittest.TestSuite()
	testunit.addTest(unittest.makeSuite(TestWeatherApi))
	fp=open("./new.html","wb")
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description=u'Result:')
	runner.run(testunit)
	fp.close()