# README.md #

day004-计算器

		@南非波波

功能实现：简单实现计算器功能，重点正则匹配

流程图：
![](http://i.imgur.com/rbTYvYP.jpg)

程序实现：

	1.文件说明：
		index.py：主程序入口
		module.py：程序模块函数定义

	2.设置功能函数：
		
		module.num_operator(expression):匹配一个表达式中的数字和运算符，如果匹配，返回expression，否则返回None。程序根据此函数判断用户输入的字符串表达式是否有异常字符
		module.charmap(expression):处理表达式字符串中的特殊字符（++ +- —+ ——）	
		module.compute_add_sub(expression):处理加减法，使用递归
		module.compute_mul_div(expression):处理乘除法，使用递归
		module.compute_pri(expression):处理优先级问题，只是对加减乘除和特殊字符处理函数的调用
		module.recursion_bracket(expression):递归处理括号函数，使用正则匹配第一次出现的括号对，然后调用module.compute_pri(expression)对匹配到的字符串进行处理，然后重新拼接expression表达式

	3.主函数入口：
		#main
		if __name__ =="__main__":  提示用户进行表达式的输入

代码地址：

	https://github.com/swht/projects/tree/master/day04/change_haproxy

使用方法：

	python3 index.py

博客地址：

	http://www.cnblogs.com/songqingbo/p/5149909.html