#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
# 备份文件的工具
import os
import time

source = ['/Users/depth/web/404/index.html',
          '/Users/depth/web/502/index.html']  # 需要备份的路径
back_dir = '/Users/depth/back'  # 备份到的地址

today = back_dir + time.strftime('%Y%m%d')  # 获得当前日期与时间 新建备份路径
now = time.strftime('%H%M%S')  # 时间

comment = raw_input('输入你的备注名： ')

if len(comment) == 0:  # 文件名字及路径
    target = today + os.sep + now + '.zip'  # os.sep 根据相应的平台自动生成分割符
    print target
else:
    target = today + os.sep + now + '_' + comment.replace('', '_') + '.zip'
    print target

if not os.path.exists(today):
    os.mkdir(today)
    print '创建目录成功', today  # 判断路径是否存在

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# 循环赋值备份 注意空格 第一个 s 引用  第二个使用了自定义s  join循环路径

if os.system(zip_command) == 0:  # 如果命令运行成功 返回0  失败返回错误号
    print '备份成功', target
else:
    print '备份失败'
