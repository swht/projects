# README.md #

day001-work-2

		@南非波波

功能实现：多级菜单展示

流程图：
![](http://i.imgur.com/VTPPhZU.jpg)

程序实现：

	1.文件说明：
		main.py：主程序入口
		welcome.py：程序首页展示内容
		citylist.py：程序的字典内容
		checkinput.py：检查用户输入是否符合规定，设置二三级菜单展示函数
	2.设置功能函数：
		welcome.WelcomeInfo()：首页函数,调用checkinput.CheckInputOne(Choose)函数,根据用户输入返回相应值或者调用相应函数
		welcome.GoBack(Choose):返回函数,该函数最终设计目标实现多级返回,但目前只实现返回到首页
		checkinput.CheckInputOne(Choose)：函数判断用户在第一次输入的值是否异常,根据用户输入情况进行相应值返回或者调用相应函数
		checkinput.InputIfOne(Choose)：调用checkinput.ShowInfo(Area)函数展示地区下面的省份,并且多层循环、遍历字典、列表展示二三层菜单。期间调用checkinput.ChooseInputTwo(Choose)函数进行用户输入的判断,并返回True|Flase值.
	3.主函数入口：
		import welcome
		#main
		if __name__ =="__main__":
		    welcome.WelcomeInfo()

代码地址：

	https://github.com/swht/projects/tree/master/day01/work-2

使用方法：

	python3 main.py

博客地址：

	http://www.cnblogs.com/songqingbo/p/5091830.html