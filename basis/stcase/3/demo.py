#!/usr/bin/env python
# coding=utf-8
import random
'''
Her0 bate 0.2

'''
welcome = "欢迎来到你的世界"
# 初始参数
list = {'name':'Depth','hp':100,'ack':50,'dun':10}
map = ['#','#','#','#','#','#','#','#','#','#']
msg = ''' a 向 左 d 向 右'''
User_msg = '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'],list['hp'],list['ack'],list['dun'])

def apple(hp):
    hp += 10
    return hp

def boom(hp):
    hp -=10
    return hp
event = [apple,boom]

# 正式程序
print welcome
print User_msg

# 核心动作
point = 0
while 1:
    map[point] = "*"
    print '你的位置',"".join(map)
    userinput = raw_input("你的下一步操作:")

    if userinput == 'd' and point < 9:
        map[point] = '#'
        point +=1
        print point
    elif userinput == 'a' and point >0:
        map[point] = '#'
        point -=1
    elif userinput == 'q' or point == 9:
        print "退出"
        break
    else:
        print msg

    if point ==3:
        list['hp'] = random.choice(event)(list['hp'])
        print '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'],list['hp'],list['ack'],list['dun'])
    elif point ==4:
        list['hp'] =boom(list['hp'])
        print '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'], list['hp'], list['ack'], list['dun'])