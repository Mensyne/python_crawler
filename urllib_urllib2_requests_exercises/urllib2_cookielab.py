#-*- coding:utf-8 -*-
import urllib2
import cookielib
import urllib

def login():
    # 创建一个cookie的cookiejar的对象
    cookie_jar = cookielib.CookieJar()
    # 使用cookie_jar对象来构建handler处理器
    cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
    # 在通过handler处理器创建一个opener对象
    opener = urllib2.build_opener(cookie_handler)
    # 登录的url
    login_url  ='http://www.renren.com/PLogin.do'
    # 构建表单数据
    form_data = {'email':"mr+mao_hancker@163.com","password":"alarmchime"}
    # 转换为url编码字符
    url_data = urllib.urlencode(form_data)
    headers = {"User-Agent":'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0'}
    request = urllib2.Request(login_url,data=url_data,headers=headers)
    opener.open(request)
    # install_opener 将自定义的opener加载为全局权限，这样在代码的任何地方使用urlopen() 都具有opener的功能
    urllib2.install_opener(opener)

def main():
    login()
    url_list = [
        'http://www.renren.com/327550029/profile',
        'http://www.renren.com/410043129/profile'
    ]
    headers = {"User-Agent":'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;)'}
    for index,url in enumerate(url_list):
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        with open(str(index)+'_renren.html','w') as f:
            f.write(response.read())

if __name__ == '__main__':
    main()


