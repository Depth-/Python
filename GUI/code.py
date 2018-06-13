#!/usr/bin/env python
# coding=utf-8
import tkinter
import turtle

root = tkinter.Tk() # 生成主程序
label = tkinter.Label(root,text='hello') # 生成标签
label.pack() #添加标签进主窗口
button0 = tkinter.Button(root,text='按钮') # 生成按钮
button0.pack() #将按钮添加进主窗口
menu = tkinter.Menu(root) # 生成菜单
submenu = tkinter.Menu(menu,tearoff=0) #生成下拉菜单
submenu.add_command(label="open")
submenu.add_command(label="save")
menu.add_cascade(label="file",menu=submenu) #将下拉菜单添加到菜单
root.config(menu=menu) # 对主程序进行配置，使主程序启用下拉菜单
def wjx(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

button0.bind('<Button-1>',wjx)  # 点击按钮 执行函数

root.mainloop()
