import requests
response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
# 各种请求的方式
requests.post('www.baidu.com')
requests.get('www.baidu.com')
# 带有参数的get请求
import requests
data ={
    'name':'germey',
    'age':22
}
response = requests.get('www.baidu.com',data)
print(response.text)
# 解析json
import requests
import json
response = requests.get('www.baidu.com')
print(type(response.text))
print(response.json())
print(json.load(response.text))
print(type(response.json()))
# 获取二进制数据
import requests
response = requests.get('www.baidu.com')
with open('load.txt','wb') as f:
    f.write(response.content)
    f.close()
# 添加headders
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response  =requests.get('www.baidu.com',headers=headers)
print(response.text)
# 基本的post 请求
import requests
data= {'name':'germy','age':12}
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response=requests.post('www.baidu.com',data=data,headers =headers)
print(response.json())
# 响应 response 属性
import requests
response=requests.get('www.baidu.com')
print(type(response.status_code),response.status_code)
print(type(response.history),response.history)
# 转态码
import requests
response = requests.get('www.baidu.com')  
if not response.sattus_code== 200:
    print("404 Not Found")

# 文件上传
import requests
files ={'file':open('favion.ico','rb')}
resposne = requests.post('www.baidu.com',files=files)

# 获取cookies
import requests
response = requests.get('www.baidu.com')
print(response.cookies)
for key,value in response.cookies.items():
    print(key+'='+value)

# 模拟登录
import requests
s =requests.Session()
s.get('www.baidu.com')
response=s.get('www.baidu.com')
print(response.text)

# 证书验证
import requests
from  requests.packages import urllib3
urllib3.disable_warnings()
response= requests.get('www.baidu.com',verify=False)
reponse =requests.get('www.baidu.com',cert=('/path/server.crt','/path/key'))
print(response.status_code)

# 代理设置
import requests
proxies = {
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
}
response=requests.get('www.baidu.com',proxies=proxies)
print(response.get(text))
# 超时设置
import requests
from requests.exceptions import Timeout
try:
    response = requests.get('www.baidu.com',Timeout=5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')

# 认证设置

import requests
from requests.auth import  HTTPBasicAuth
r = requests.get('www.baidu.com',auth=HTTPBasicAuth)
print(r.status_code)

# 异常处理

import requests
from requests.exceptions import ReadTimeout,ConnectionError
try:
    resposne = requests.get('www.baidu.com',Timeout=5)
    print(response.status_code)
except  ReadTimeout:
    print("Timeout")
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')

