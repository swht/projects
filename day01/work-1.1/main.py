#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''

import checkinput,login,addusers
import time,sys

def main():
    Choose = input('''
	==============================================
                    欢迎光临南非波波小屋!
	==============================================
			[1]注册   [2]登录   [3]退出
	请选择相应指令:''').strip()
    if Choose == '':
        print("指令不能为空,请输入正确指令!")
    else:
        if Choose.isdigit():
            Choose = int(Choose)
            if Choose >= 1 and Choose <= 3:
                if Choose == 1:
                    addusers.AddUsers()
                if Choose == 2:
                    login.Login()
                if Choose == 3:
                    print("欢迎下次光临南非波波小屋!")
                    time.sleep(1)
                    sys.exit(0)
            else:
                print("你输入的指令已超出范围,请按照系统指令进行输入!")
        else:
            print("请输入正确的指令,指令为整数型数字!")

#main
if __name__ =="__main__":
    main()

