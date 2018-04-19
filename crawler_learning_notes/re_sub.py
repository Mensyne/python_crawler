#-*- coding:utf-8 -*-
import re
# 替换

# 处理 Unicode字符串替换
s = u"Hello世界, 你好World.1234"
# 表示Unicode中文字符范围
pattern = re.compile(u"[\u4e00-\u9fa5]")
# 将符合匹配的结果替换为 ""
print pattern.sub("",s)


# 表示非Unicode中文字符集范围
pattern = re.compile(u"[^\u4e00-\u9fa5]")
# 将所有非中文部分替换为 ""
print pattern.sub("", s)


# 处理非Unicode字符串替换
s = "Hello世界, 你好World.1234"
# 匹配Unicode中文字 再 编码为 utf-8 后的字符集范围
pattern = re.compile(u"[^\u4e00-\u9fa5]".encode("utf-8"))
print pattern.sub("",s)



s = "hello 123, hello 456, byebye789"
# 匹配文本，并对匹配的每组数据分组
pattern = re.compile("(\w+)\s(\w+)")
# 替换时使用源字符串的分组数据
result = pattern.sub(r'[\1][\2][\1]',s)
print result