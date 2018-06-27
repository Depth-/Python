# coding=utf-8
# 磁盘监控
from optparse import OptionParser
import sys,os
try:
    if sys.argv[1] == '':
        print '没有数据'
    elif sys.argv[1] == 'cpu':
        data = os.popen('sysctl -n machdep.cpu.brand_string').read()
    #类似于1个对象，需要属性取值
        print data
    elif sys.argv[1] == 'data':
        data = os.popen('diskutil list | df -h').read()
        print data

except:
    print '没有参数'

# 参数举例
parser = OptionParser()
parser.add_option("-a","--address",dest='address',default='localhost',help="ADDRESS")
# dest是存储的变量，default是缺省值，help是帮助提示
# 增加一个选项
(options,args) = parser.parse_args()
print options
print args


