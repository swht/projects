#!/usr/local/env python3
'''
Author:@swht
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import os,sys,time

UserName = "qingbo"
UserPasswd = "test"
UserBlackPath = "./user_black.txt"

def Welcome(LoginFlag):
	'''欢迎信息页面'''
	if LoginFlag == "True":
		print ("Welcome login the System!")
	if LoginFlag == "Error":
		print ("Sorry,your passwd is Error!")
	if LoginFlag == "False":
		print ("Sorry,your userName is not have!")
	if LoginFlag == "Space":
		print("Sorry,your input is null!")
def UserBlack():
	'''黑名单判断'''
	if os.path.exists(UserBlackPath):	#判断黑名单文件是否存在
		FileUsers = open(UserBlackPath)	#打开黑名单文件
		UserBlack = FileUsers.read()	#读取黑名单文件内容
		FileUsers.close()	#关闭黑名单文件句柄
		if UserName == UserBlack:  #判断黑名单列表中用户名称是否与指定userName相同
			print ("Sorry,your name is in the blacklist,Please to connet the admin!")
			sys.exit(1)  #若相同提醒用户‘该用户在黑名单列表中’并且退出程序
def UserBlackAdd(Users):
	'''黑名单列表增加'''
	print ("Your name is now to add the blacklist!")
	FileUsers = open(UserBlackPath,"w")
	FileUsers.write(Users)
	FileUsers.close()
	sys.exit(0)

def Login(Passwd):
	'''用户登录接口函数'''
	global Users
	UserBlack();	#黑名单不存在或者用户名没在列表中执行while循环
	while True:
		Users = input("users:").strip() #获取用户输入且去除首尾空格符
		if Users == '':
			Welcome("Space")
			break
		else:
			if Users == UserName:	#判定用户名是否正确
				Passwd = input("passwd:").strip()
				if Passwd == '':
					Welcome("Space")
					break
				else:
					if Passwd == UserPasswd: #判断用户密码是否正确
						Welcome("True"); #用户名和密码都正确，调用登录成功接口
						time.sleep(1)
						sys.exit(0)
					else:
						Welcome("Error");	#密码错误调用密码错误提示接口
						break
			else:
				Welcome("False"); #用户名和密码错误调用相应提示接口
				break
#main
if __name__ == '__main__':
	for i in range(3): #允许用户输错3次
		Login("Passwd");
	if Users == '':
		print("Sorry,users is null,the system is quit a later！")
		time.sleep(1)
		sys.exit(1)
	else:
		UserBlackAdd(Users);