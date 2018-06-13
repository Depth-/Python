#!/usr/bin/env python
# coding=utf-8

import wx
import turtle



class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None ,
                         title = "my tools",
                         size =(400,600))
        panel = wx.Panel(frame,-1)
        self.buttonWJX = wx.Button(panel,
                                   -1,
                                   "五角星",
                                   pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.OnButtonWJX,self.buttonWJX) # 绑定不上！！
        frame.Show()
        return True

    def OnButtonWJX(self,event): # 需要额外参数
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()