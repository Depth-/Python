#!/usr/bin/env python
# coding=utf-8

# 套接字的意义两台主机之间建立一个通讯链接
# 文件名：client.py


# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 22222  # 设置端口好  注意端口是否被占用

s.connect((host, port))
print s.recv(1024)
s.close()
