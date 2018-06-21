#!/usr/bin/env python
# coding=utf-8
# 生成20个激活码 连接数据库 保存

import random, string, re, MySQLdb


def rand_str(num, length=8):  # 定义次数与长度
    for i in range(num):
        chars = string.ascii_letters + string.digits  # 生成小写字母+大写字母+数字
        s = [random.choice(chars) for i in range(length)]  # 取随机返回一个字符当中的1个，取长度
        s = str(s)
        # s = s.strip('[]')
        # s = s.replace('\'','')
        # s = s.replace(',', '')
        # s = s.replace(' ', '')
        s = re.sub(r"\W+", "", s)
        print s  # 两种方法
        # 数据库部分
        conn = MySQLdb.connect("localhost", "root", "你的密码", "yaoqingma")
        cur = conn.cursor()  # 方法获取操作
        sql = 'INSERT INTO list(字段名) VALUES("%s")' % s  # 需要提前建立好数据库与表
        cur.execute(sql)  # 执行sql语句
        conn.commit()  # 提交到数据库


a = random.randint(48, 57)
b = random.randint(65, 90)
c = random.randint(97, 122)
d = random.randint(100, 200)
print chr(a) + chr(b) + chr(c) + chr(d)

if __name__ == '__main__':
    pass
# 自己生效
rand_str(5)
