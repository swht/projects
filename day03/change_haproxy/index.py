#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import sys,time
import module

ha = './haproxy.conf'
#选择功能
def chooseView(choice):
    if choice == 1:  #获取配置文件所有内容
        print(module.getAllContent(ha))
        choice1 = input("请选择是否要继续(y/n):").strip()
        if choiceIf(choice1) == True:
            print("你选择的是继续,系统即将返回到系统主页!")
            time.sleep(1)
            chooseView(showView())
        if choiceIf(choice1) == False:
            print("你选择的是不继续操作,系统将退出!感谢你的使用!")
            time.sleep(1)
            sys.exit(0)

    if choice == 2:
        module.addLabelRecord(ha,getInputConnet())
    if choice == 3:
         module.delLabelRecord(ha,getInputConnet())
    if choice == 4:
        module.chgLabelRecord(ha)
    if choice == 'q':
        print("系统即将退出,感谢你的使用!")
        time.sleep(1)
        sys.exit(0)

#判断用户输入，是否继续或返回
def choiceIf(choice):
    if choice.isalpha():
        if choice == 'Y' or choice == 'y':
            return True
        elif choice == 'N' or choice == 'n':
            return False
        else:
            print("你的指令系统暂不支持!系统即将退出!")
            time.sleep(1)
            sys.exit(2)
    else:
        print("你输入的字符格式有误,系统将默认返回到主页!")
        time.sleep(1)
        chooseView(showView())

def showView():
    print('''
    ****欢迎使用haproxy配置文件修改系统****
    \t[1]获取配置文件信息\t\t[2]增加模块配置
    \t[3]删除模块配置    \t\t[4]修改模块配置
    \t[q]退出系统
    ************************************
    ''')
    while True:
        count = 0
        if count < 3:
            choice = input("\t请选择相应指令:").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice > 0 and choice < 5:
                    return choice
                else:
                    count += 1
                    print("你的输入已超出指令范围!")
            elif choice == 'q':
                return choice
            else:
                count += 1
                print("请输入正确的指令,指令为[1-4]的整型或q字符!")
        else:
            print("对不起,你的输入错误次数已达3次,系统即将退出,感谢你的使用!")
            time.sleep(1)
            sys.exit(1)

#获取用户输入字典
def getInputConnet():
    get_input_dict = {}
    count = 0
    while True:
        if count < 3:
            get_input_dict['label'] = input("请输入你需要增加记录内容的模块名称:").strip()
            get_input_dict['server'] = input("请输入server字段值:").strip()
            get_input_dict['weight'] = input("请输入weight字段值:").strip()
            get_input_dict['maxconn'] = input("请输入maxconn字段值:").strip()
            # if get_input_dict['label'].isalpha():
            if get_input_dict['label']:
                getall_dict = module.getAllContentDict(ha) #获取配置文件总的字典
                if get_input_dict['label'] in getall_dict.keys(): #用户输入的moudle在文件中存在，那就直接在原有的基础上增加记录值
                    return get_input_dict
                # else: #label模块不存在，根据用户选择是否要创建
                #     choice = input("你选择的模块不存在,是否要创建(y/n):").strip()
                #     if choiceIf(choice) == True:
                #         print("你选择的是继续,系统即将创建moudle %s!" % get_input_dict['label'])
                #         print('''即将创建的模块内容为:
                #         \t%s
                #         \t\t\tserver %s weight %s maxconn %s\n
                #         ''' % (get_input_dict['label'],get_input_dict['server'],get_input_dict['weight'],get_input_dict['maxconn']))
                #         return get_input_dict
                #     if choiceIf(choice) == False:
                #         print("你选择的是不继续操作,系统将退出!感谢你的使用!")
                #         time.sleep(1)
                #         sys.exit(0)

            else:
                count += 1
                print("模块名称Label需要全为字母的字符!")
        else:  #输错3次之后返回系统主页
            print("你的输入错误次数已达3次,系统即将返回主页!")
            time.sleep(1)
            chooseView(showView())

#main
if __name__ == "__main__":
    ha = './haproxy.conf'
    chooseView(showView())
