

# headers
# cookies
# body
# args
# session

# http 中包含方法如下
# get
# post
# put
# delete
# head


import requests
from bs4 import BeautifulSoup
from urllib import parse
	
# request 请求
# response 响应
# status_code http 状态码
# http code 
# 200 成功
# 302 重定向
# 400 参数错误
# 403 无权限
# 405 错误的请求方法
# 500 服务器错误， 无法返回

response = requests.get('http://testerlife.com')
print(response.ok)
print(response.url)
print(response.cookies)
print(response.headers)
print(dir(response))
print(response.status_code)   # 获取响应码
print(response.text)   # 字符串类型
proint(reponse.content)   # 字节流 bytes

response = requests.get('http://www.runoob.com/http/http-tutorial.html')
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, "html.parser")
print(soup.a.get_text().rstrip())
print(soup.find('a', {'target': '_top'}).get_text().strip())


with open('http-tutorial.html', 'wb') as file:
	file.write(response.content)

