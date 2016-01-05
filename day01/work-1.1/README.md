# README

day001-work-1

		@南非波波!

功能实现：用户注册、登录接口
流程图：
![](http://i.imgur.com/C7Ilt5x.jpg)

程序实现：

	1.文件说明：
		main.py：主程序入口
		checkinput.py：检查用户输入是否符合规定，设置功能函数
		addusers.py:用户注册接口
		login.py:用户登录接口
	2.设置功能函数：
		main.main()：主体函数,程序的主入口,允许用户进行选择注册用户、用户登录、程序退出;
		checkinput.Countnum(filename)：获取文件行数,该函数在此暂未调用,在后续的练习中，比如购物网站等可能需要用到,暂且放在这里以作了解;
		checkinput.UserBlack(UserName)：判断用户名是否在黑名单中;
		checkinput.UserBlackAdd(Users)：将用户名添加到黑名单列表中;
		checkinput.AddUsersList(Users)：判断用户输入的用户名是否在列表中存在;
		addusers.AddUsers()：通过调用各种判断函数,将用户输入的用户和密码添加到用户列表中，如果用户已经存在,会返回main.main()函数;
		login.Login()：判断用户输入情况，用户在黑名单退出系统,不在用户列表返回主页提醒用户注册,用户和密码匹配成功后返回登录界面（欢迎信息和当前日期时间）;

代码地址：

	https://github.com/swht/projects/tree/master/day01/work-1.1

博客地址：

	http://www.cnblogs.com/songqingbo/p/5091808.html	#最下面	

使用方法：
	
	python3 main.py