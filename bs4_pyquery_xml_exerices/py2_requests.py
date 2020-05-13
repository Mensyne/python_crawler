#-*- coding:utf-8 -*-
import requests
print requests.get("http://www.baidu.com")

kw = {'wd':'中国'}
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get('http://www.baidu.com/s?',params=kw,headers=headers)
print response.content
print response.url
print response.encoding
print response.status_code


# 增加系数
url = 'http://fanyi.qq.com/api/translate'
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
keyword = {
    "source":"auto",
    "target" : "auto",
    "sourceText" : "你好Python", # 需要翻译的内容
    "sessionUuid ": "translate_uuid1517720945431" #translate_uuid + Unix时间戳（毫秒）
}

result = requests.post(url,headers=headers,data=keyword).json()
print result


# 代理
# proxies = {'http':'http://12.34.56.79:9527'}
# response = requests.get("http://www.baidu.com",proxies = proxies)
# print response.content

# 私密代理
# proxy = {'http':'mr_mao_hacker:sffqry9r@61.158.163.130:16816'}
# response = requests.get('http://www.baidu.com',proxies = proxy)
# print response.content

# Cookies
response = requests.get('http://www.baidu.com/')
# 返回cookiejar对象
cookiejar  = response.cookies

# 将CookierJar转成字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print cookiejar
print cookiedict

# session 对象的创建
import requests

ssion = requests.session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
data = {'email':'mr_mao_hacker@163.com','password':'alxxxxxxme'}

# 发送附带用户的和密码的请求，可以直接登录后Cookie值，保存到ssion里
ssion.post("http://www.renren.com/PLogin.do",data=data)

# sess 包含用户登录Cookie值，可以直接访问那些登录后才可以的访问的页面
response = ssion.get('http://www.renren.com/410043129/profile')

print response.content

# 处理HTTPS请求
response = requests.get("https://www.baidu.com/",verify=True)
print response.content

# 12306证书-----跳过证书验证设置verify=False
response1 = requests.get("https://www.12306.cn/mormhweb",verify=False)
print response1.content