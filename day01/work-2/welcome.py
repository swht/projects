#!/usr/local/env python3
'''
Author:@swht
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import citylist
import checkinput
import sys,time
#登录欢迎界面
def WelcomeInfo():
    for i in range(0,3):
        Choose = input('''
            ===================================================
                                欢迎来到中国！
            ===================================================
            [11]华北地区   [12]东北地区   [13]华东地区   [14]华中地区
            [15]华南地区   [16]西南地区   [17]西北地区   [18]特别行政区
            [19]退出
            请选择相应指令:''').strip()
        checkinput.CheckInputOne(Choose)
    GoBack("地区")

#错误次数已达3，程序退出
def GoBack(Choose):
    if Choose == "地区":
        print("你的输入错误次数已达3次,系统将退出!")
        time.sleep(1)
        sys.exit(1)