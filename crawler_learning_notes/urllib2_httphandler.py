#-*- coding:utf-8 -*-
import  urllib2
def send_request():
    url = 'http://www.baidu.com'
    headers = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"}
    request = urllib2.Request(url,headers=headers)
    http_handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(http_handler)
    response = opener.open(request)
    return response.read()

if __name__ == '__main__':
    send_request()

