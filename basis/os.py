#!/usr/bin/env  python
# coding=utf-8
import os
'''
● os.name字符 指示你正在使 的平台。 如对于Windows，它是'nt'， 对于Linux/Unix  户，它是'posix'。
● os.getcwd()函数得到当前 作 录，即当前Python脚本 作的 录 径。
● os.getenv()和os.putenv()函数分别 来读取和设置环境变 。
● os.listdir()返回指定 录下的所有 件和 录名。
● os.remove()函数 来删除 个 件。
● os.system()函数 来运 shell命令。
● os.linesep字符 给出当前平台使 的 终 符。 如，Windows使 '\r\n'，Linux使
 '\n' Mac使 '\r'。
● os.path.split()函数返回 个 径的 录名和 件名。
>>> os.path.split('/home/swaroop/byte/code/poem.txt')
('/home/swaroop/byte/code', 'poem.txt')
● os.path.isfile()和os.path.isdir()函数分别检验给出的 径是 个 件还是 录。类似地，os.
path.exists()函数 来检验给出的 径是否真地存在。'''