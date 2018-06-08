#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
import time

result = []
while True:
    result.append(int(random.uniform(1,7))) #生成随机数 不包含最大值
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7))) #生成三个
    count = 0
    index = 2
    pointStr = ""
    while index >= 0: #键位沓于等于0
        currPoint = result[index] # index 是键位 ！！！！ 重点强调 从第三个开始输出
        count += currPoint #加法赋值运算 1 = 1+2
        index -= 1         #减法赋值运算 1 = 1-2 键位减一
        pointStr += " "
        pointStr += str(currPoint)  # 原有的往上加 是字符串的类型 不发生运算
    if count <= 11:
        print (pointStr + " -> " + "小" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    else:
        print (pointStr + " -> " + "大" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    result = []