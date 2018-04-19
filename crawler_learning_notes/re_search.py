#-*- coding:utf-8 -*-
import re
# 从任何位置开始查找，一次匹配
s = 'abcd1234bcda4321'
pattern = re.compile(r'\d+')
m = pattern.search(s)
print(m)
print m.group()
pattern = re.compile("([a-z]+)\s([a-z]+)",re.I)# 表示忽略字符串字母大小写
s1 = "Hello word, byebye World"
m1 = pattern.search(s1)
print m1.group(0)


