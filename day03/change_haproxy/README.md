# README.md #

day003-change_haproxy

		@南非波波

功能实现：修改haproxy配置文件

流程图：
![](http://i.imgur.com/JIm5ndl.jpg)

程序实现：

	1.文件说明：
		index.py：主程序入口
		module.py：程序模块函数定义

	2.设置功能函数：
		index.chooseView(choice)：根据用户的的选择调用相应的功能函数模块
		index.choiceIf(choice):判断用户输入Y/N是否规范，返回值为True或False，根据返回值进行相应的函数调用和函数结束
		index.def showView():函数展示整个菜单，并获取用户的输入信息，返回值为用户输入的字符串，该值会传递到index.chooseView()函数中
		index.getInputConnet()：获取用户对label记录值操作的字段，返回值为字段的字典，该字典会传递到函数module.addLabelRecord(ha,dict_input)、module.delLabelRecord(ha,dict_input)中进行相应操作。
		module.getAllContentDict(ha):该函数模块获取整个配置文件的内容
		module.addLabelRecord(ha,dict_input):操作增加字段值
		module.delLabelRecord(ha,dict_input):操作删除字段值
		module.chgLabelRecord(ha):操作修改字段值		


	3.主函数入口：
		#main
		if __name__ =="__main__":
		    chooseView(showView())

代码地址：

	https://github.com/swht/projects/tree/master/day01/work-2

使用方法：

	python3 main.py

博客地址：

	http://www.cnblogs.com/songqingbo/p/5091830.html