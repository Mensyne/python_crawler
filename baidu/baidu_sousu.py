#-*- coding:utf-8 -*-
import urllib
import urllib2

def sent_request():
    base_url = 'https://www.baidu.com/s?'
    keywords = raw_input("请输入你要查询的数据")
    # 进行url编码
    url_str = urllib.urlencode({'wd':keywords})
    print(url_str)
    print(urllib.quote(keywords))
    full_url = base_url + keywords
    print(full_url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    request = urllib2.Request(full_url,headers=headers)
    response = urllib2.urlopen(request)
    return response.read()

if __name__ == '__main__':
    html = sent_request()
    print(html)











