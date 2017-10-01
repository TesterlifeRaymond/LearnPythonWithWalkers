
""" pass """
import json
from config import BaseConfig
import os


class BuDeJie(BaseConfig):
    """ pass """

    def __init__(self):
        """ pass """
        super(BuDeJie, self).__init__()
        self.crawl_info = self.get_value(self.enum, 'budejie')
        self.start_url = self.get_value(self.crawl_info, 'start_url')
        self.all_page_content_url, self.user_name, self.content, self.up, self.down = \
            self.get_value(self.crawl_info, 'xpaths')

    def get_all_page_url(self):
        """ pass """
        result = []
        for url in range(1, 1000):
            resp = self.request(self.start_url + '/{}'.format(url))
            # print(resp, self.start_url + '{}'.format(url))
            if resp.status_code == 404:
                return result
            parse = self.parse(resp.text, self.all_page_content_url)
            result.extend([self.start_url[0:-5] + uri[1::] for uri in parse])
        return result

    def get_user_info_and_content(self):
        """ pass """
        urls = self.get_all_page_url()
        for url in urls:
            user_name, content, up, down = self.output(
                url, [self.user_name, self.content, self.up, self.down]
            )
            result = dict(
                url=url,
                user_name=user_name[0],
                content=content[0],
                up=up[0],
                down=down[0]
            )
            file_name = url.split('-')[1].split('.')[0]
            file_content = json.dumps(result, ensure_ascii=False, indent=4)
            self.down_load_content(file_name, file_content)

    def down_load_content(self, file_name, file_content):
        """ pass """
        if not os.path.exists('file/budejie'):
            os.mkdir('file/budejie')
        with open('file/budejie/{}.json'.format(file_name), 'w', encoding='utf-8') as file:
            file.write(file_content)

    def main(self):
        """ pass """
        print(self.get_user_info_and_content())
