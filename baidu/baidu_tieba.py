# -*- coding:utf-8 -*-
import urllib
import urllib2


def send_request(url):
    print ('正在抓取网页中.......')
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        return response.read()
    except Exception as e:
        print(e)
        return ''


def write_html(html, filename):
    print('[INFO]' + '正在写入文件中.......' + filename)
    with open(filename, 'w',) as f:
        f.write(html)


def main(tieba_name, start_page, end_page):
    """
    http://tieba.baidu.com/f?kw=数据挖掘&ie=utf-8&pn=50
    http://tieba.baidu.com/f?kw=数据挖掘&ie=utf-8&pn=100
    :param tieba_name: 贴吧名
    :param start_page: 起始页
    :param end_page: 结束页
    :return: url
    """
    for page in range(start_page, end_page + 1):
        base_url = 'http://tieba.baidu.com/f?'
        p = (page - 1) * 50
        query_data = {'kw':tieba_name,'pn':p}
        url_str = urllib.urlencode(query_data)
        full_url = base_url + url_str
        print (full_url)
        filename = tieba_name + str(page) + '.html'
        html = send_request(full_url)
        write_html(html, filename)


if __name__ == '__main__':
    tieba_name = raw_input('请输入你要查找贴吧名')
    start_page = int(raw_input('请输入查找的起始页'))
    end_page = int(raw_input('请输入查找的结束页'))
    main(tieba_name, start_page, end_page)