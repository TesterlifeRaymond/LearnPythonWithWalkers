
import json


def dict_to_json(dict):
	# 接受一个字典
	# 不进行ensure_asscii编码
	# 并返回一个排序后的 json结构体
	dict['@time'] = None
	return json.dumps(dict, ensure_ascii=False, sort_keys=True)
