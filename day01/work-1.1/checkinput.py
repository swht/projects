#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''
import os,sys,time

UsersListPath = "./userslist.txt"
UserBlackPath = "./userblacklist.txt"
#获取文件内容的行数
def Countnum(filename):
	files = open(filename)
	data = files.read()
	files.flush()
	files.close()
	return data.count('\n')

#判断用户是否在黑名单中
def UserBlack(UserName):
	'''黑名单判断'''
	if os.path.exists(UserBlackPath):	#判断黑名单文件是否存在
		FileUsers = open(UserBlackPath)	#打开黑名单文件
		for UserBlack in FileUsers.readlines():	#读取黑名单文件内容
			if UserName == UserBlack:  #判断黑名单列表中用户名称是否与指定userName相同
				print("对不起,该用户已在系统黑名单列表中,请联系管理员!")
				time.sleep(1)
				sys.exit(1)  #若相同提醒用户‘该用户在黑名单列表中’并且退出程序
		FileUsers.close()	#关闭黑名单文件句柄


#将用户添加到黑名单中
def UserBlackAdd(Users):
	'''黑名单列表增加'''
	print("该用户将被家到系统黑名单中...")
	FileUsers = open(UserBlackPath,"a")
	FileUsers.write(Users)
	FileUsers.close()
	sys.exit(0)

#判断用户是否存在userlist列表中
def AddUsersList(Users):
	if os.path.exists(UsersListPath):  #判断文件存在
		if Countnum(UsersListPath) == 0: #判断文件内容为空
			return False
		else:
			UsersListFile = open(UsersListPath,'r')
			for lines in UsersListFile.readlines():
				db = lines.strip("\n").strip()  #去除换行符
				db = eval(db)  #将字符串类型转换成字典类型
				if Users == db['user']:
					return True  #返回True值说明用户名匹配成功
			UsersListFile.close()
	else:  #文件不存在
		return False  #返回False值说明用户列表文件不存在或为空

#判断用户是否存在userlist列表中
def LoginUsersList(Users,Passwd):
	if os.path.exists(UsersListPath):  #判断文件存在
		if Countnum(UsersListPath) == 0: #判断文件内容为空
			return False
		else:
			UsersListFile = open(UsersListPath,'r')
			for lines in UsersListFile.readlines():
				db = lines.strip("\n").strip()  #去除换行符
				db = eval(db)  #将字符串类型转换成字典类型
				if Users == db['user']:
					if Passwd == db['passwd']:
						return True  #返回True值说明用户名和密码匹配成功
			UsersListFile.close()
	else:  #文件不存在
		return False  #返回False值说明用户列表文件不存在

