#!/usr/bin/env python
# coding=utf-8
import re

# re.match(pattern, string, flags=0)
# re.search(pattern, string, flags=0)
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
# 函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
reg0 = r"h"
str0 = "hello hello hello"
b = re.findall(r'h', str0)
print b
# findall(string[, pos[, endpos]])
# re.finditer 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，
# 并把它们作为一个迭代器返回。

# re.sub(pattern, repl, string, count=0, flags=0)
'''
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是: ", num
# ^ $ 开头 结尾 + 一次或多次 ？0次或有 . 一个任意字符
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下
# re.split(pattern, string[, maxsplit=0, flags=0])
a = re.split('\W+', 'one, two, three.')
print a  # 输出的结果后面有个'' 的原始是 分割之后必须后面补充一个空值，不能以分割符结尾
a = re.split('(\W+)', ' one, two, three.')  # (匹配非字母数字及下划线)
print a
a = re.split('\W+', ' one, two, three.', 1)  # 分隔一次
print a
a = re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print a
# 零宽断言的一个应用
