#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错

### 1.开始的python 复习项目
print 'Hello World'

### 2.' " ''' 三种引号之间的区别
'''
单引号 =  双引号 > 三引号（一段话）
'''

### 3.一个运算测试
length = 5
wight = 2
end = length * wight
print 'ens is', end
print 'dobule is', 2 * (length + wight)

### 4.控制
depth = 'cool'
depth = raw_input('depth cool or no cool?')

if depth == "cool":
    print 'yes'
else:
    print 'no cool'

### while有一个可选的else从句
number ='20'
old ='nianling'
while old:
    age = raw_input('age?')
    if age == number:
        print 'yes'
    elif age < number:
            print 'small'
    elif age > number:
           print 'big'
           break

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

for i in range(1, 5):
    print i
else:
    print 'The for loop is over'

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) > 3:
        continue
    print 'length > 3'
    ##从用户处取到输入。判断
## 5.14 end 