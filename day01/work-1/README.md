# README.md #

day001-work-1

		@南非波波

功能实现：登录接口

流程图：

![](http://i.imgur.com/61eFd0u.jpg)

程序实现：

	1.设置功能函数：
		Welcome(LoginFlag)：根据LoginFlage返回不同的信息
		UserBlack()：黑名单列表判断UsersName是否被锁定
		UserBlackAdd(Users)：添加UsersName到黑名单
		Login(Passwd):用户登录函数
	2.函数调用
		Login(Passwd)函数调用UserBlack()函数，先判断UsersName是否在黑名单中；
		Login(Passwd)函数根据用户输入的判断情况，调用Welcome(LoginFlag)函数返回不同的提示信息；
		Login(Passwd)函数在执行满三次正常结束之后调用UserBlackAdd(Users)函数，将用户所输入Users添加到黑名单列表；
	3.主函数入口：
		if __name__ == '__main__':
代码地址：

	https://github.com/swht/projects/tree/master/day01/work-1

博客地址：

	http://www.cnblogs.com/songqingbo/p/5091808.html

测试账号：

	users：qingbo
	passwd：test