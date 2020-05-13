#-*- coding:utf-8 -*-
# # 包含4个模块
# #1：reqeust  最基本的HTTP 的请求模块，模拟发送请求，只需要给库方法的传入URL 以及额外的参数，模拟这个过程
# #2： error 异步处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止
# #3： parse 一个工具模块，提供了许多url处理的方法，来拆分、解析、合并等
# #4： robotparser 主要是用来识别网站的robot.txt 文件，然后判断网站可以爬，哪些网站不可以爬，它其实用的比较少
# # 5：urlopen() urllib.request 模块提供了最基本的构造的HTTP 请求的方法，利用它可以模拟浏览器一个请求发起过程，同时它还带有的处理授权领证，重定向 浏览器cookie 以及其他内容
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# print('-------')
# # 查看响应的类型
# print(type(response))
# # 返回结果<class 'http.client.HTTPResponse'>，它是一个HTTPResponse类型的对象，它主要包含了read()、readinto(),getheader(name)、getheaders()、fileno()等方法，以及msg,version,status,reason,debuglevel,closed等属性
# # 得到这个对象之后，我们把它赋值为response变量，然后就可以调用这些方法和属性，得到返回结果的一系列信息了
# print(response.status)
# print('----')
# print(response.getheaders())
# print('----')
# print(response.getheader('Server'))
# # 前两个输出分别输出了响应的状态码和响应的头信息最后一个输出通过调用getheader()方法并传递一个参数Server获取了响应头中的Server值，结果是BWS/1.1，意思是服务器是用BWS/1.1搭建的。
# # 想给链接传递一些参数，该怎么实现呢？首先看一下urlopen()函数的API
# # urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# # 可以发现，除了第一个参数可以传递URL之外，我们还可以传递其他内容，比如data（附加数据）、timeout（超时时间）等。
# # data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型需要通过bytes()方法转化另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而是POST方式。
# import urllib.parse
# import urllib.request
# data=  bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response_data  = urllib.request.urlopen('http://www.baidu.com',data=data)
# print(response_data)
# # 传递了一个参数word，值是hello。它需要被转码成bytes（字节流）类型
# # 转字节流采用了bytes()方法，该方法的第一个参数需要是str（字符串）类型，需要用urllib.parse模块里的urlencode()方法来将参数字典转化为字符串,第二个参数指定编码格式为utf8
# # timeout 参数来设置超时时间如果请求超出了设置的这个时间，还没有得到响应，就会抛出异常如果不指定该参数，就会使用全局默认时间它支持HTTP、HTTPS、FTP请求
# response_data1 = urllib.request.urlopen('http://www.baidu.com',timeout=1)
# print(response_data1.read())
# # 于是抛出了URLError异常。该异常属于urllib.error模块，错误原因是超时,可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过它的抓取
# import socket
# import urllib.request
# import urllib.error
# try:
#     response_data_2 = urllib.request.urlopen('http://www.baidu.com',timeout=1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
#
# # timeout这个参数来实现超时处理
# # context参数，它必须是ssl.SSLContext类型，用来指定SSL设置
# #cafile和capath这两个参数分别指定CA证书和它的路径
# # request里面加入Headers的信息，这样才能利用更强大的Request,可以实现最基本请求的发起
# import urllib.request
# request = urllib.request.Request('http://www.baidu.com')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
#
# # Request可以通过怎样的参数来构造，它的构造方法如下：
# # class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# # headers是一个字典，它就是请求头，我们可以在构造请求时通过headers参数直接构造，也可以通过调用请求实例的add_header()方法添加。
# # 添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib，我们可以通过修改它来伪装浏览器。比如要伪装火狐浏览器，你可以把它设置为：也可以用的add_header()方法来添加
# # origin_req_host指的是请求方的host名称或者IP地址
# # unverifiable表示这个请求是否是无法验证的，默认是False
# # ---------------------------------------------
# # 高级用法：
# # 对于高级的操作，比如COOKies处理，代理的设置等，可以使用Handler工具
# # 可以理解为各种处理器，有专门的处理登录的验证，有处理Cookie的，有处理代理设置的，利用它们，我们可以几乎可以做到Http的请求所有的事情
# # 首先，介绍一下urllib.request模块里的BaseHandler类，它是所有其他Handler的父类，它提供了最基本的方法，例如default_open()、protocol_request()等。
# # 另一个比较重要的类就是OpenerDirector，我们可以称为Opener。我们之前用过urlopen()这个方法，实际上它就是urllib为我们提供的一个Opener
# #么要引入Opener呢？因为需要实现更高级的功能。之前使用的Request和urlopen()相当于类库为你封装好了极其常用的请求方法，利用它们可以完成基本的请求，但是现在不一样了，我们需要实现更高级的功能，所以需要深入一层进行配置，使用更底层的实例来完成操作，所以这里就用到了Opener
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)
#
# #这里首先实例化HTTPBasicAuthHandler对象，其参数是HTTPPasswordMgrWithDefaultRealm对象，它利用add_password()添加进去用户名和密码，这样就建立了一个处理验证的Handler。
# # 接下来用这个Handler并使用build_opener()方法构建一个Opener，这个Opener在发送请求时就相当于已经验证成功了，接下来，利用Opener的open()方法打开链接，就可以完成验证了
# # -------------------------
# # 代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy_handler = ProxyHandler({
#         'http':'http://127.0.0.1:9743',
#         'https':'https://127.0.0.1:9743'
#     })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
#
#
# # Cookie的处理
# # 处理Cookie就需要相关的Handler
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name +"="+item.value)
# # 首先，我们必须声明一个CookieJar对象。接下来，就需要利用HTTPCookieProcessor来构建一个Handler，最后利用build_opener()方法构建出Opener，执行open()函数即可
# # 输出为文本格式
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie1 = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# handler1 = urllib.request.HTTPCookieProcessor(cookie1)
# opener = urllib.request.build_opener(handler)
# opener1 = urllib.request.build_opener(handler1)
# response = opener.open('http://www.baidu.com')
# response1 = opener1.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)
# cookie.save(ignore_discard=True,ignore_expires=True)
# # CookieJar就需要换成MozillaCookieJar，它在生成文件时会用到，是CookieJar的子类，可以用来处理Cookies和文件相关的事件，比如读取和保存Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式
# # 另外，LWPCookieJar同样可以读取和保存Cookies，但是保存的格式和MozillaCookieJar不一样，它会保存成libwww-perl(LWP)格式的Cookies文件。
#
# # 从文件中读取的并利用
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# 调用load()方法来读取本地的Cookies文件，获取到了Cookies的内容

# 处理异常的处理
# 1：URLerror ----equest模块生的异常都可以通过捕获这个类来处理,一个属性reason，即返回错误的原因

# from urllib import request,error
# try:
#     response = request.urlopen('http://www.baidu.com')
# except error.URLError as e:
#     print(e.reason)


# 2:HTTPError ------ 专门用来处理HTTP请求错误，比如认证请求失败等，包含3个属性
# ------1:code 返回状态码HTTP 状态码  2：reason 同父类一样，用于返回错误的原因   3：headers 返回请求头
# from urllib import  request,error
# try:
#     response = request.urlopen('http://www.baidu.com')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.heades,sep='\n')

# URLError 是 HTTPError的父类，所以先选择捕获子类的错误，再去捕获父类的错误，所以上述代码更好的写法如下：
# from urllib import request,error
# try:
#     response = request.urlopen('http://www.baidu.com')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# 有时候，reason属性返回的不一定是字符串，也可能是一个对象
# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://www.baidu.com',timeout=0.01)
# except urllib.error.URLError  as e:
#     print(type(e.reason))
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
# reason属性的结果是socket.timeout类。所以，这里我们可以用isinstance()方法来判断它的类型，作出更详细的异常判断


# 解析链接
# 1：urlparse() ----实现url 的识别和分段
# from urllib.parse import urlparse
# result =  urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result)

# 2: urlparse 还包括了其他的参数：1 urlstring:带解析的URL   2：scheme  默认的协议（比如http或https
# from urllib.parse import urlparse
# result =  urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)

# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
# 3: urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# 参数urlstring: 这是待解析的url
# 参数scheme 默认的协议，在不包含scheme信息时，才生效
# allow_fragments fragment。如果它被设置为False，fragment部分就会被忽略，它会被解析为path、parameters或者query的一部分，而fragment部分为空
# from  urllib.parse import urlparse
# result= urlparse('http://www.baidu.com',allow_fragments=False)
# print(result)
#返回结果ParseResult实际上是一个元组，我们可以用索引顺序来获取，也可以用属性名获取。示例如下：
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com',allow_fragments=False)
# print(result)
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com',allow_fragments=False)
# print(result.scheme,result[0],result.netloc,result[1],sep='\n')

# 2 urlunparse() 相应的就有它的对立方法，接受的是一个可迭代对象，它的长度是6，否则会抛出参数数量不足
# 或者过多的问题
# from urllib.parse import urlunparse
# data = ['http','www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))
# 3:urlsplit() 与urlparse()方法类似，只不过它不再单独解析params这一部分
# from urllib.parse import urlsplit
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)

# SplitResult，它其实也是一个元组类型，既可以用属性获取值，也可以用索引来获取

# 4:urlunsplit() 与urlunparse 类似，唯一区别是长度必须为5
# from urllib.parse import urlunsplit
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))

# 5：urljoin() 提供一个base_url（基础链接）作为第一个参数，将新的链接作为第二个参数，该方法会分析base_url的scheme、netloc和path这3个内容并对新链接缺失的部分进行补充，最后返回结果
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com','FAQ.html'))

# 6: urlencode()-- 在构造GET 请求参数时候非常有用---常用
# from urllib.parse import urlencode
# params = {
#     'name':'json',
#     'age':18
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

# 7：parse_qs() 反序列化  如果我们有一串get请求参数，利用parse_qs()方法，就可以将它换回字典
# from urllib.parse import parse_qs
# query = 'name=json&age=18'
# print(parse_qs(query))

# 8:parse_qsl()------它用于将参数转化为元组组成的列表，如下：
# from urllib.parse import parse_qsl
# query='name=json&age=22'
# print(parse_qsl(query))

# 9:quote()---- 可以将内容转换为URL 的编码的格式，URL 中带有的中文参数时。
# 有时可能会导致乱码的问题，此时用这个方法可以将中文字符转化为URL 编码
# from urllib.parse import quote
# keyword='壁纸'
# url = 'http://www.baidu.com?wd='+quote(keyword)
# print(url)

# 10:unquote() 表示对URL 解码
# from urllib.parse import unquote
# url ='https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))