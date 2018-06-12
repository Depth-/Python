#!/usr/bin/env python
# coding=utf-8
import sys
import re


"""
   Name: name.py read
   欢迎使用一个日志处理小脚本
"""


def split_log(line):  # 日志切分取出
    split_line = line.split()
    return {'IP':split_line[0],
            'IP2':split_line[3],
            'URL':split_line[5],
            'UA':split_line[7],
            'REQ':split_line[4],
            'bytes':split_line[-3]}

def data_report(logfile):
    report_dict = {}
    for line in logfile:
        line_dict = split_log(line) # 调用循环行 切分 取出
        print line_dict
        # print json.dumps(line_dict, encoding="UTF-8", ensure_ascii=False) 中文编码输出
        try:
            bytes_sent = str(line_dict['bytes']) # 如果不能设置成整数，证明没有数据
        except ValueError:
            continue   # 不是数字就跳过
        report_dict.setdefault(line_dict['IP'],[]).append(bytes_sent) # 设置默认值，更新字典
    return report_dict

def main():
    if not len(sys.argv) > 1:
        print __doc__,"没有参数"
        sys.exit(1)
    in_file_path = sys.argv[1]
    try:
        infile = open(in_file_path,'r')
    except IOError:
        print "文件打开失败"
        print __doc__
        sys.exit(1)
    log_report = data_report(infile)
    print log_report
    infile.close()

if __name__ == "__main__":
    main()