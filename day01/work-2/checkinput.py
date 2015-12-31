#!/usr/local/env python3
'''
Author:@swht
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import welcome,citylist
import sys,time

#一级菜单输入字段判断
def CheckInputOne(Choose):
    if Choose == '':
        print("指令不能为空,请输入正确指令!")
    else:
        if Choose.isdigit():
            Choose = int(Choose)
            if Choose >= 11 and Choose <= 19:
                InputIfOne(Choose)
            else:
                print("你输入的指令已超出范围,请按照系统指令进行输入!")
        else:
            print("请输入正确的指令,指令为整数型数字!")

def InputIfOne(Choose):
    if Choose == 11:
        ShowInfo("华北地区")
    if Choose == 12:
        ShowInfo("东北地区")
    if Choose == 13:
        ShowInfo("华东地区")
    if Choose == 14:
        ShowInfo("华中地区")
    if Choose == 15:
        ShowInfo("华南地区")
    if Choose == 16:
        ShowInfo("华南地区")
    if Choose == 17:
        ShowInfo("西北地区")
    if Choose == 18:
        ShowInfo("特别行政区")
    if Choose == 19:
        print("欢迎下次再来中国!")
        time.sleep(1)
        sys.exit(0)

#二级、三级菜单输入字段判断
def ChooseInputTwo(Choose):
    if Choose == '':
        print("指令不能为空,请输入正确指令!")
    else:
        if Choose.isdigit():
            return True
        elif Choose == 'back' or Choose == 'Back' or Choose == 'BACK':
            return False
        else:
            # print("你输入的指令已超出范围,请按照系统指令进行输入!")
            pass
#二级、三级菜单显示
def ShowInfo(Area):
    #显示省份
    for i in range(0,3): #允许用户最大错误次数3次
        print('''
            ===================================================
                                欢迎来到%s！
            ==================================================='''% Area)
        # citylist.CityList[Area].keys() 获取地区里面的省份键值
        Count = 0
        for index,key in enumerate(citylist.CityList[Area].keys()): #python3中citylist.CityList[Area].keys()输出的是dict_keys对象
            Count += 1
            print("\t\t\t序号:%s 省份:%s" % (index,key))
        Choose1 = input("\t\t请选择相应序号进入相应省份!返回上级菜单[Back]:").strip()
        ChooseInputTwo(Choose1)
        if ChooseInputTwo(Choose1) == True:
            Choose1 = int(Choose1)
            if Choose1 >= 0 and Choose1 < Count:
                #python3中将dict_keys转换成列表再做索引
                #python2中dict.keys()的输出对象就是一个列表，可以直接进行索引操作
                #KeyOne = citylist.CityList[Area].keys()[Choose1]
                KeyOne = list(citylist.CityList[Area].keys())[Choose1] #获取省份keys
                #显示城市
                for i in range(0,3): #允许用户最大错误次数3次
                    Count = 0
                    print('''
            ===================================================
                            欢迎来到%s！
            ===================================================''' % KeyOne)
                    for index,key in enumerate(citylist.CityList[Area][KeyOne]):
                        Count += 1
                        print("\t\t\t序号:%s 城市地区:%s" % (index,key))
                    Choose2 = input("\t\t请选择相应序号进入相应城市地区!返回上级菜单[Back]:").strip()
                    ChooseInputTwo(Choose2)
                    if ChooseInputTwo(Choose2) == True:
                        Choose2 = int(Choose2)
                        if Choose1 >= 0 and Choose2 < Count:
                            KeyTwo = citylist.CityList[Area][KeyOne][Choose2] #获取地区名称
                            print("\t\t哈哈，到头了!\t\t%s" % KeyTwo)
                            print("\t\t穿越到上一级菜单喽......")
                            time.sleep(1)
                            break
                        else:
                            print("你输入的指令不在范围内!")
                            time.sleep(1)
                            continue
                    elif ChooseInputTwo(Choose2) == False:
                        print("\t\t系统将返回上一级菜单!")
                        time.sleep(1)
                        break #跳出当前一级循环
                    else:
                        print("你是输入有误,请重新输入!")
                        time.sleep(1)
                        continue
                print("你的输入次数已达三次,系统返回上一级菜单!")
            else:
                print("你输入的指令不在范围内!")
                time.sleep(1)
                continue #跳出当前循环
        elif ChooseInputTwo(Choose1) == False:
            welcome.WelcomeInfo() #首页
        else:
            print("你的输入有误,请重新输入!")
    print("你的输入次数已达三次,系统将返回首页!")
    welcome.WelcomeInfo()
