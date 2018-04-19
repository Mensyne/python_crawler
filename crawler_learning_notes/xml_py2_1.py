#-*- coding:utf-8 -*-
from lxml import etree

# 文件读取
# 读取外部文件----etree.parse()方法来读取文件
html = etree.parse("./hello.html")
result = etree.tostring(html,pretty_print=True)
print(result)


