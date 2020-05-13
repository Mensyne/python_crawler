#-*- coding:utf-8 -*-
import urllib2
import random
def send_request():
    USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"
    ]
    PROXY_LIST = [
        {"http": "maozhaojun:ntkn0npx@114.67.224.167:16819"},
        {"http": "maozhaojun:ntkn0npx@114.67.224.167:16819"},
        {"http": "maozhaojun:ntkn0npx@114.67.224.167:16819"},
        {"http": "maozhaojun:ntkn0npx@114.67.224.167:16819"},
        {"http": "maozhaojun:ntkn0npx@114.67.224.167:16819"}
    ]

    def send_request():
        url =  'http://www.baidu.com/'
        request = urllib2.Request(url)
        request.add_header('User-Agent',random.choice(USER_AGENT_LIST))
        proxy = random.choice(PROXY_LIST)
        proxy_handler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_handler)
        response = opener.open(request)
        print(response.read())
        print(request.get_header("User-agent"))

if __name__ == '__main__':
    send_request()

