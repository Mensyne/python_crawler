#-*- coding:utf-8 -*-
from pyquery import PyQuery as pq
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# 字符串初始化
html= '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
# 获取所有li标签
print doc("li")
# URL初始化
doc1 = pq(url="http://cuiqingcai.com")
print doc1('title')

# 基本CSS 选择器
html2 = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc2 = pq(html2)
print "-"*50
print doc2("#container .list li")
print type(doc2("#container .list li"))


print "-"*100
items = doc2(".list")
print type(items)
print items
lis = items.find('li')
print type(lis)
print lis

print "-"*100
lis = items.children()
print lis

print "-"*100

html3 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc3 = pq(html3)
li  = doc3('.item-0 active')
print li
print str(li)


print "-"*100
# 多个节点 使用items
doc = pq(html3)
lis = doc("li").items()
for li in lis:
    print li , type(li)

# 获取属性-attr()属性
html4 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc  = pq(html4)
a = doc('.item-0.active a')
print "-"*100
print a,type(a)
print "-"*100
#attr()方法，只会得到第一个节点的属性。
print a.attr('href')

print "-"*100
print a.attr.href

print "-"*100
doc = pq(html4)
a = doc('a')
for item in a.items():
    print(item.attr('href'))

# 获取文本---text()


html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print "-"*100
print(a.text())

#获取文本
html5 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html5)
a = doc('.item-0.active a')
print a
print "-"*100
print a.text()

# 要获取这个节点内部的HTML文本，就要用html()方法
li = doc('li')
print(li)
print "-"*100
print li.html()
#html()方法返回的是第一个li节点的内部HTML文本，而text()则返回了所有的li节点内部的纯文本
print "-"*100
print li.text()

# CSS选择器
html6 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html6)
li = doc('li:first-child')
print li
li2 = doc('li:last-child')
print "-"*100
print li2
li3 = doc('li:nth-child(2)')
print "-"*100
print li3
li4 = doc('li:gt(2)')
print "-"*100
print "**"
print li4
li5 = doc('li:nth-child(2n)')
print "-"*100
print li5


