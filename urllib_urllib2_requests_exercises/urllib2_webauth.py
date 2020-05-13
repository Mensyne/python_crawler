#-*- coding:utf-8 -*-
import urllib2

def send_request():
    url = 'http://192.168.72.82/'
    username = "bigcat"
    password = '123456'
    # 限购一个处理器对象，基于HTTP账户
    passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # 添加信息web 和账户密码
    passmgr.add_password(None,url,username,password)
    # 构建处理器对象
    httpauth_handler = urllib2.HTTPBasicAuthHandler(passmgr)
    # 构建自定义的opener对象
    opener = urllib2.build_opener(httpauth_handler)
    response = opener.open(url)
    print response.read()

if __name__ == '__main__':
    send_request()

