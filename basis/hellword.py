#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错

# 开始的python 复习项目
print 'Hello World'

# ' " ''' 三种引号之间的区别
'''
单引号 =  双引号 > 三引号（一段话）
字符串中有单引号用双引号 反之
'''

#一个运算测试
length = 5;  wight = 2
end = length * wight
print 'ens is', end
print 'yun is', 2 * (length + wight)

# 控制  depth = raw_input('depth cool or no cool?')
depth = 'cool'
if depth == "cool":
    print 'yes'
else:
    print 'no cool'

# for 迭代变量 in 序列： 序列一个一个的分组，字符串就是一个一个的字母 列表就是一个一个的词
# while 有一个可选的else从句
# elif 和 else  elif==if else则是从句
# pass 占位符 代码桩

old ='old'
while old:
    num = '22'
    age = '23'
    if age == num:
        print 'yes'
    elif age < num:
            print 'small'
    elif age > num:
           print 'big'
           break

count = 0
while count < 5:
   print count, "值 < 5"
   count = count + 1
else:
   print count, "值 >= 5"

for i in range(1, 5):
    print i
else:
    print '循环结束'

s = 1
#变量当中用引号赋值，相当于字符型

while True: # 起始一个真条件
    s+=1 # 加1
    if s < 5:
        print 's < 5'
        continue  # 截至剩下的代码块 重新循环
    if s > 5:
        break
    print 's > 5'
    # 从用户处取到输入。判断