#-*- coding:utf-8 -*-
from lxml import etree

html = etree.parse('./hello.html')
print(type(html))
# 获取所有的li标签
result = html.xpath("//li")
print(result)
print(type(result))
print(len(result))
print(type(result[0]))
# 获取所有的li标签下classshuxiang
result1 = html.xpath('//li/@class')
print(result)

# 获取li标签下href 为link1.html的a标签
result2 = html.xpath('//li/a[@href="link1.html"]')
print(result2)

# 获取<li> 标签下的所有 <span> 标签
# 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
result3 = html.xpath('//li//span')
print(result3)

# 获取 <li> 标签下的<a>标签里的所有 class
result4 = html.xpath('//li/a//@class')
print(result4)

# 获取最后一个 <li> 的 <a> 的 href
result5 = html.xpath('//li[last()]/a/@href')
print(result5)

# 获取倒数第二个元素的内容
result6 = html.xpath('//li[last()-1]/a')
# 使用text 可以获取元素的内容
print(result6[0].text)

# 获取 class 值为 bold 的标签名

result7 = html.xpath('//*[@class="bold"]')
# tag 方法可以获取标签名
print(result7[0].tag)





