
import json
import xmltodict

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