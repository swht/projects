#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import getpass,sys,time
import checkinput,main

UsersListPath = "./userslist.txt"

#判断用户输入的是否符合要求
def AddUsers():
	print('''
	==============================================
			欢迎加入南非波波小屋
	==============================================''')
	CountFlag1 = 0
	CountFlag2 = 0
	while True:
		if CountFlag1 < 3:
			User = input("请输入你的用户名:").strip()
			if User == '':
				print("你的输入为空,请重新输入!")
				CountFlag1 += 1
				CountFlag2 += 1
			else:
				if len(User) >= 4 and len(User) <= 10:
					if checkinput.AddUsersList(User) == True:
						print("该用户已被注册!")
					else:
						while True:
							if CountFlag2 < 3:
								Passwd1 = getpass.getpass("请输入你的密码:").strip() #getpass.getpass()可以将用户输入的密码以暗文形式实现
								if Passwd1 == '':
									print("你的输入为空,请重新输入!")
									CountFlag2 += 1
								elif len(Passwd1) < 6:
									print("你的密码太简单,请重新输入!")
									CountFlag2 += 1
								else:
									Passwd2 = getpass.getpass("请再次输入你的密码:").strip()
									if Passwd1 == Passwd2:
										db = {"user":User,"passwd":Passwd1}
										UsersListFile = open(UsersListPath,"a")
										UsersListFile.write(str(db))
										UsersListFile.write('\n')
										UsersListFile.close() #直接调用增加用户接口
										main.main()
									else:
										print("你两次输入的密码不一致,请重新输入!")
										CountFlag1 += 1
							else:
								print("你输入的错误次数已达3次!系统将返回主页!")
								main.main()
				else:
					print("请输入4-10位字符或数字组合作为用户名!")
					CountFlag1 += 1
		else:
			print("你输入的错误次数已达3次!系统将退出!感谢你对南非波波小屋的支持!")
			time.sleep(1)
			sys.exit(1)

# AddUsers()

