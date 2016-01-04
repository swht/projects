#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import sys,time,getpass
import checkinput,main

def Login():
	'''用户登录接口函数'''
	CountFlag1 = 0 #用户输入错误次数的统计
	CountFlag2 = 0 #用户输入为空的次数统计
	print('''
	==============================================
			欢迎光临南非波波小屋
	==============================================''')
	while True:
		if CountFlag1 < 3:
			if CountFlag2 < 3:
				Users = input("请输入登录用户名:").strip() #获取用户输入且去除首尾空格符
				if Users == '':
					print("你的输入为空,请重新输入!")
					CountFlag1 += 1
					CountFlag2 += 1
				else:
					checkinput.UserBlack(Users)	#黑名单不存在
					Passwd = getpass.getpass("请输入你的密码:").strip()
					if Passwd == '':
						print("密码不能为空,请重新入")
						CountFlag1 += 1
						CountFlag2 += 1
					else:
						if checkinput.LoginUsersList(Users,Passwd) == True:
							print("%s你好,欢迎光临南非波波小屋,今天是%s" % (Users,(time.strftime('%Y-%m-%d\t%H:%M:%S',time.localtime(time.time())))))
							time.sleep(1)
							sys.exit(0)
						elif checkinput.LoginUsersList(Users,Passwd) == False:
							print("你输入的用户名不存在!请先注册后再登录!")
							main.main()
						else: #其他情况就报用户名或密码错误
							print("你输入的用户名或密码错误!")
							CountFlag1 += 1
			else:
				print("你输入的错误次数已达3次,系统将返回主页!")
				main.main()
		else:
			print("你输入的错误次数已达3次,系统将退出")
			if Users == '':  #如果用户输入为空将直接退出
				sys.exit(1)
			else:  #如果用户输入不为空将用户最后输入错误的users加到黑名单列表
				checkinput.UserBlackAdd(Users)

# Login()