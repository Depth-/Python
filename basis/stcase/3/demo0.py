#!/usr/bin/env python
# coding=utf-8
import os

'''
Hero 登录验证
'''
key = 0
while True:
    if os.path.isfile('lock.log'):# 判断文件是否存在
        print "已被锁定"
        break

    username = raw_input('账号：')
    password = raw_input('密码：')

    key += 1
    if username =='admin' and password =='123456':
        print "登录成功"
        pass
        break
    else:
        if key == 3 :
            open('lock.log','w').write(username)
            print "你的账户 %s 已被锁定" % username
            break