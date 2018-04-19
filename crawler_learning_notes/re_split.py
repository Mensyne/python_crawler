#-*- coding:utf-8 -*-
import re
# 分割字符串，返回列表
s = "a.. ,, .. ;;ab ..a"
pattern =  re.compile(r'[\s\.;,]')
result_list = pattern.split(s)
print result_list
pattern =  re.compile(r'[\s\.;,]+')
result_list = pattern.split(s)
print result_list


