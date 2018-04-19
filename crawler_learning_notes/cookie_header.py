#-*- coding:utf-8 -*-
import urllib2

def send_request():
    ulr_list = [
       'http://www.renren.com/327550029/profile',
        'http://www.renren.com/410043129/profile'
    ]
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding" : "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        # 重点：附带了登录状态的Cookie
        "Cookie": "anonymid=j7wsz80ibwp8x3; _r01_=1; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; depovince=GUZ; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; jebecookies=ec00c648-8bdd-45ee-aa7c-75e082f30a05|||||; ick_login=54a22963-3812-4e6e-9f9a-6fab76e186dc; p=a13841ca187d177502cc3fb0987080ca9; first_login_flag=1; t=0194d3026c400887dd00fd1559bb3ed09; societyguester=0194d3026c400887dd00fd1559bb3ed09; id=327550029; xnsid=3914f6f4; loginfrom=syshome; ch_id=10016; wp_fold=0",
        "Host": "www.renren.com",
        "Referer": "http://zhibo.renren.com/top",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    for index,url in enumerate(ulr_list):
        # 构建并发送附带登录状态的cookie请求
        request =  urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        with open(str(index)+".html",'w') as f:
            f.write(response.read())

if __name__ == '__main__':
    send_request()



