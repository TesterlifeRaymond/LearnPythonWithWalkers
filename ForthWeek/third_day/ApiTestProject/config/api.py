""" pass """


class DouBanApi:
    """ pass """
    enum = {
        "book_api_test": {
            "name": "book_api_test",
            "book_api": "https://api.douban.com/v2/book/{}",
            "book_id": "6548683",
        },
        "search_book_api": {
            "name": "search_book_api",
            "search_api_url": "https://api.douban.com/v2/book/search?q={}",
            "keywords": "三国演义"
        }
    }


class JuHeApi:
    """ pass """
    enum = {
        "test_api": "http://v.juhe.cn/todayOnhistory/queryEvent.php",
        "data": {'key': "1d39d53a70ebed87d5cabbc8b73b96e2", "date": ''},
        "schema_path": "today"
    }


class WeChatApi:
    """docstring for ClassName"""
    enum = {
        "test_api": "http://v.juhe.cn/weixin/query",
        "data": {
            'ps': '20', 'pno': '2', 'dtype': 'json', 'key': '4beb9d77d2b95ce9bec6d8363ee5a620'
        },
        "schema_path": "wechat"
    }


class MenuApiConfig:
    """ pass """
    enum = {
        "menu_api": "http://apis.juhe.cn/cook/query.php?menu={}&",
        "key": 'key=338ce1ecb756bf7ca4772fbb9f11cd75',
        "menu_name": "红烧排骨"
    }
