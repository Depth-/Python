#!/usr/bin/env  python
# coding=utf-8
# Source = https://www.v2ex.com/t/463296
data = '''
        a, 1.324171
        b, 0.000126
        c, 1.970941
        a, 1.469649
        b, 0.000124
        c, 0.512929
        a, 1.290920
        b, 0.000118
        c, 0.259524
        a, 0.495958
        b, 0.000123
        c, 0.910949
        a, 1.268038
        b, 0.000118
        c, 1.016419
        a, 1.856081
        b, 0.000120
        c, 1.400075
        a, 1.314131
        b, 0.000140'''
result = {}

for line in data.splitlines():  # 按照行读取lines
    if not line:  # 判断是否为NONE
        continue  # 判断为空跳出循环
    key, value = line.split(",")  # 切割赋值
    result.setdefault(key, []).append(float(value))  # 分类 设定key为键值，后面逐行加如 数值为浮点数

for key, values in result.items():  # 遍历字典
    print key, sum(values), sum(values) / len(values), len(values)
