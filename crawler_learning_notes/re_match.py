#-*- coding:utf-8 -*-
import re
s = 'abcd1234bcda4321'
pattern = re.compile(r"\d+")
# 从起始位置开始查找，一次匹配
m = pattern.match(s)
print m
# 返回一个match 对象
m = pattern.match(s,4)
print m
print m.group()



