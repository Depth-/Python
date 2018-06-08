#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
#  基本分类  列表   元组    字典
#  常用的数据类型有7种  数字 字符串 列表 元组 字典 集合
#  下面讲 三种 括号代表的区别

print '[] 列表 的说明 可修改 可添加------------------------------------------'
shoplist = ['apple', 'mango', 'carrot', 'banana']
#定义一个列表
print '我有几个', len(shoplist),"内容"
for item in shoplist:
    print "循环输出 " + item

shoplist.append('rice')
print '现在具有的内容', shoplist
# 增加内容

shoplist.sort()
print '按照首字母排序', shoplist
print '单独取一个内容', shoplist[0]
# 排序

new_shop = shoplist[0]
del shoplist[0]     # 删除列表内第一个
print '删除一个内容', new_shop
print '剩下全部内容', shoplist


print '\n() 元组 的说明 不可修改 ------------------------------------------'
team = ('1', '2', '3')
print '组内有几个数据', len(team)

new_team = ('4', '5', team)  # 内容包括
print '新加入一个内容', len(new_team)

print '全部的内容', new_team
print '取一个内容', new_team[2]
print '取内容当中的内容 // 索引2当中的索引2的值', new_team[2][2] # 元组内的元组数据


print '\n{} 字典 的说明 不可修改 ------------------------------------------'
dict = { 'one' : '123',
         'two' : '456',
         'sun' : '789',
         'for' : '1011'}
print "输出的值%s" %dict['one']
print ("Tips：print语可以跟着%符号的字符。这些字符具备定制的功能。\n"
       "定制让输出满足某种特定的格式。定制可以是%s表示字符 或%d表示整数。\n"
       "组必须按照相同的顺序来对应这些定制。%s 定制后面%开头的输出")
print "My name is %s and weight is %d kg!" % ('Depth', 18)
# 用法是将一个值插入到一个有字符串格式符 %s 的字符串中

dict['thr'] = '1111'   # 增加
del dict['sun']        # 删除

print '\n其中包括%s个内容' %len(dict)

for name, key in dict.items(): # 循环名字和值两个字段来自dict的值
    print 'My Name %s key %s' % (name, key)
if 'two' in dict: # 单独判断一个
    print "\n two's %s" %dict["two"]


print ' \n序列的说明 ----------------------------------------------------'
list0 = ['one', 'two', 'thr', 'for']
print ''' Demo [1:2:3] 头：尾：间隔
        h    e   l  l  o     w  o  r  l  d   字符
        0    1   2  3  4  5  6  7  8  9  10  键位
        -11 -10 -9 -8 -7 -6 -5 -4 -3  -2 -1  负数键位
        索引切片对照表 -1代表从后置未开始  0代表从头开始
      '''
print 'is 0',list0[0]
print 'is 1',list0[1]
print 'is 2',list0[2]
print 'is 3',list0[3]
print 'is -1',list0[-1]
print 'is -2',list0[-2]
print 'is 1 和 3',list0[1:3]     # []切片中的数据 是从开始位开始，结束位结束,结束位会排斥在切片之外
print 'is 1 全部',list0[1:]       # 从1开始的全部
print 'is 1 到 -1',list0[1:-1]    # 平级的 -1 == 3 按照顺序
print '全部',list0[:]             # 全部


print '\n字符串的方法 ----------------------------------------------------'
strs =  "kukudedepth"

if strs.startswith('kukude'):
    print 'yes 判断开是是否匹配'
if 'kukude' in strs:
    print 'yes 是否存在'
if strs.find('depth')!=-1:
    print 'yes 查找指定字符串在另一个字符串的位置或返回-1代表找不到'

sybol = '__'
mylist = ['one','two','three']
print sybol.join(mylist),'join分割符，循环加入到列表当中的每个'


print '\n列表处理更详细的对比内容说明------------------------------------------'
list01 = ['one', 786, 2.23, 'for', 70.2]
list02 = [123, 'seven']
aTuple = (1,2,3,4)
list03 = list(aTuple)

print '列表重复',list01 * 2
print '列表组合',list01 + list02
print '列表长度',len(list01)
del list02[0]; print list02
print '元素是否存在于列表中','one' in list02
print "比较两个列表元素",cmp(list01, list02)
print '将元组转换为列表',list03
list03.extend(list01)
print '在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）',list03
print '统计某个元素在列表中出现的次数',list03.count(1)
print '从列表中找出某个值第一个匹配项的索引位置',list03.index('one')

for i in list01:
    print "循环输出列表01 " + str(i)

list03.insert(0, 'hello')
print '将对象插入列表',list03
print '移除列表中的一个元素（默认最后一个元素），并且返回该元素的值',list03.pop(0)
print list03
list03.remove(1)
print "移除列表中某个值的第一个匹配项",list03
list03.reverse()
print "反向列表中元素",list03
#下面两个是Python3
'''
print "输出所有的主键位",list01.keys()
print "输出所有的值",list01.values()
'''


print '\n元组------------------------------------------------------'
array = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
array[1][2]["k2"].append("seven")
# 在tu元祖当中第一位置的第二位置的K2字典增加一个
print "全部 ",array[0]
print "索引2 ",array[1]
print "索引2的索引3 ",array[1][2]
print "元组中包含的字典 ",array[1][2]["k2"]
# 元组的一级元素不可被修改增加删除但可以修改二级后的。如修改元祖中列表，字典等内容


print '\n其他 ------------------------------------------------------'
# 计算 1到100 内的总和 和 3 5倍数的总和
num = 0; bei = 0
for i in range(0,101):
    num += i
    if i % 3 == 0 or i % 5 ==0:
        bei +=i
print "35倍数",bei
print '总倍数 ',num

print (sum([i for i in range(10) if i % 3 ==0 or i % 5 == 0])),'10以内的3 5倍数之和'
# 列表表达式  [expr for iter_var in iterable] 核心语句是for循环  迭代iter对象的所有条目 讲 expr应用于序列的每个成员

# 生成器对象 用圆括号包含列表解析氏是一个生成器表达式，只有在使用的过程中 【调用】才会执行
g =( i for i in range(10) if i % 3 ==0 or i % 5 == 0)
for i in g:
    print i
# 列表解析 迭代到的内容用运算处理
[i * 10 for i in range(10)]


'''
# 往字典中添加数据脚本
print '\n字典 ----------------------------------------------------'
dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
# 往字典中添加数据
while flag == 'a' or 'c' :
    flag = raw_input("添加或查找单词 ?(a/c)")
    if flag == "a" :                             # 开启
        word = raw_input("输入单词(key):")
        defintion = raw_input("输入定义值(value):")
        dictionary[str(word)] = str(defintion)  # 添加字典 word = defintion
        print "添加成功!"
        pape = raw_input("您是否要查找字典?(a/0)")   #read
        if pape == 'a':
            print dictionary
        else :
            continue
    elif flag == 'c':
        check_word = raw_input("要查找的单词:")  # 检索
        for key in sorted(dictionary.keys()):            # yes
            if str(check_word) == key:
                print "该单词存在! " ,key, dictionary[key]
                break
            else:                                       # no
                off = 'b'
        if off == 'b':
            print "抱歉，该值不存在！"
    else:                               # 停止
        print "error type"
        break
'''