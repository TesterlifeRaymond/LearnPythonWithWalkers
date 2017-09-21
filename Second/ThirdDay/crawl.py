
# api test http
# 数据结构，json, dict, str, int,   在爬虫中， 是最常用到的， 而且他是基于http交互场景


import requests
from bs4 import BeautifulSoup
from lxml import etree
# pip install lxml


class TesterLifeCrawl:
    """ http://testerlife.com crawl """
    def __init__(self):
        """ pass """
        self.session = requests.Session()
        # session.get, session.post
        # requests.post() == > 200 success
        # requests.post() == > 403  你要先去登陆 
        # session.post() == > 200 success
        # session.post() == > 200 success
        self.start_url = 'http://testerlife.com'

    def get_blog_title(self):
        """ 获取blog 的名字 """
        html = self.session.get(self.start_url).text   # 去取页面信息
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.get_text()
        # html 找到title这个标签， 取出他的text
        # soup.title.get_text()
        return title

    def get_blog_content_title(self):
        """ 我们去获取testerife的文章标题 """
        html = self.session.get(self.start_url).text   # 去把html 拿回来
        soup = BeautifulSoup(html, 'html.parser')   # 实例化BeautifulSoup(html, 'html.parser')
        # <a class="article-title" href="/2017/07/03/python-logbook/">
        #    python-logbook-function
        # </a>
        article_title_list = soup.find_all('a', {'class': 'article-title'})
        # print('article_title_list : ', article_title_list)
        article_titles = [string.get_text() for string in article_title_list]
        return 'article_titles : {}'.format(article_titles)


class TesterHome:
    def __init__(self):
        """ pass """
        self.session = requests.Session()
        self.start_url = 'http://testerhome.com'

    def get_testerhome_page_titles(self):
        """ //div[@class="title media-heading"]/a/@title
        # xpath 定位
        # selenium
        # lxml
        """
        html = self.session.get(self.start_url).text
        el = etree.HTML(html)
        return el.xpath('//div[@class="title media-heading"]/a/@title')

    def get_testerhome_user_info(self):
        """ pass """
        html = self.session.get(self.start_url).text
        el = etree.HTML(html)
        return el.xpath('//div[@class="title media-heading"]/a/@title')


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


class TestBaseClass(Base):
    def __init__(self):
        super(TestBaseClass, self).__init__()

    def get_testerhome_page_titles(self):
        """ pass """
        return self.output(
            'http://testerhome.com',
            # '//*[@id="main"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/a/@title'
            '//div[@class="title media-heading"]/a/@title'
        )

    def get_testerhome_user_info(self):
        return self.output(
            'http://testerhome.com',
            '//div/a[@class="user-name"]/@data-name'
        )

if __name__ == '__main__':
    base_class_instance = TestBaseClass()
    titles = base_class_instance.get_testerhome_page_titles()
    user_name = base_class_instance.get_testerhome_user_info()

    for name, title in zip(user_name, titles):
        print('文章作者: {} ======== 文章标题: {}'.format(name, title))
    # tester_life = TesterLifeCrawl()
    # # print(tester_life.get_blog_title())
    # print(tester_life.get_blog_content_title())
    
    # tester_home = TesterHome()
    # for title in tester_home.get_testerhome_page_titles():
    #     print(title)

