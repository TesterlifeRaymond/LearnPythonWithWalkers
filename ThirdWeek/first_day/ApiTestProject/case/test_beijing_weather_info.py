
import json
import unittest
from lib import get_weather_city_info
from lib import dict_to_json


class BeiJingYanQingTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		""" pass """
		cls.assert_file = open('assert\\yanqing.json', encoding='utf-8')
		# 打开 assert\\yanqing.json 这个文件， 他的文件编码是'utf-8'
		# cls.assert_file 是一个file的句柄
		# cls.assert_file = <_io.TextIOWrapper name='assert\\yanqing.json' mode='r' encoding='utf-8'>
		cls.obj = get_weather_city_info.GetCityCode('beijing')
		cls.city_code = cls.obj.get_city_codes()[0].get('@url')
		cls.city_info = cls.obj.get_city_weather_info(cls.city_code)
		cls.assert_info = dict_to_json(json.loads(cls.assert_file.read()))

	@classmethod
	def tearDownClass(cls):
		cls.assert_file.close()

	def test_city_code_is_ok(self):
		self.assertEqual(self.city_code, '101010800')

	def test_city_name_is_ok(self):
		self.assertEqual(self.city_info.get('city'), '延庆')

	def test_city_resp_type(self):
		self.assertEqual(type(self.city_info), dict)

	def test_city_weather(self):
		self.assertEqual(self.city_info.get('weather'), '晴')

	def test_city_all_info(self):
		resp = self.obj.get_city_codes()[0]
		resp_string = dict_to_json(resp)
		self.assertEqual(self.assert_info == resp_string, True)

