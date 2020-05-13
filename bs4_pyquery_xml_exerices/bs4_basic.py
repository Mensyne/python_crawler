#-*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

# 创建soup对象
soup = BeautifulSoup(html,'lxml')

# 格式化输出soup的对象的内容
print  soup.prettify()
print soup.title
print soup.head
print soup.a
print soup.p
print soup.name
print soup.p.attrs
print soup.p['class']

# 以对这些属性和内容等等进行修改
soup.p['class'] = "newClass"
print soup.p

# 删除class 属性
del soup.p['class']
print soup.p

# 获取标签内的文字
print soup.p.string
print type(soup.p.string)

# BeautifulSoup 对象表示的是一个文档的内容。大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
print type(soup.name)
print soup.name
print soup.attrs


print soup.head.contents
print soup.head.contents[0]

print soup.head.children
for child in  soup.body.children:
    print child

print soup.head.string
print soup.title.strng

print soup.find_all("a")
print soup.find_all(["a","b"])

print soup.find_all(id='link2')
# class_ 因为python的关键字里面有class关键字
print soup.find_all(class_ = "sister")

print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
print soup.find_all(text=re.compile("Dormouse"))

print soup.select('b')
print soup.select('.sister')
print soup.select('#link1')
print soup.select('p #link1')


print("----------")
print soup.select('a[class="sister"]')
print soup.select('p a[href="http://example.com/elsie"]')


# 获取内容
print "-"*50
print soup.select('title')[0].get_text()
print "-"*50
for title in  soup.select('title'):
    print title.get_text()