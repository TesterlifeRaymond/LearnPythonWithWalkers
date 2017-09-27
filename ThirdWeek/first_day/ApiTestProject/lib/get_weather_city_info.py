
import json
from config import config
from lib import request, xml


class GetCityCode(config.ProjectConfig, request.Request, xml.Xml):
	def __init__(self, city_name):
		""" pass """
		self.city_name = city_name

	def get_city_codes(self):
		""" pass """
		city_info = self.xml_to_json(self.request(self.get_city_code.format(self.city_name)).text)
		# json.loads(city_info).get('beijing').get('city')  返回的是city_info 字典类型取值 key = beijing的值
		# 再从key = beijing ==> dict类型， 去获取key = city 的值
		# 最后获取到的 key = city 的值是一个列表
		# pythonic
		return json.loads(city_info).get('beijing').get('city')

	def get_city_weather_info(self, city_code):
		weather_info = self.request(self._get_city_weather_info.format(city_code))
		# weather_info == > Response对象
		if self.get_status_code() == 200:
			return weather_info.json().get('weatherinfo')
		return 'Error'
