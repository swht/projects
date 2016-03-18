#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''

import time,sys
import module

if __name__ == "__main__":
    while True:
        count = 0
        if count < 3:
            print('''
            请输入一个计算公式，类似下面格式：
            =========================================================================================
            1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
            =========================================================================================
            系统默认匹配所有的数字、(、)、+、-、/、*、.
                                                                                计算器程序研发@南非波波
            ''')
            expression = input("请输入:").strip()  #或取用户输入的表达式字符串，并去除左右的空格
            # expression = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
            expression = expression.replace(' ','') #去除字符串中间的空格，使用replace进行空字符串替换空格
            if module.num_operator(expression): #成功匹配正确表达式
                # print(expression)
                result = module.recursion_bracket(expression) #将处理后没有括号的表达式赋值给expression
                print(result)
                break
            else:
                count += 1
                print("你输入的表达式格式不正确!")
                time.sleep(1)
                continue
        else:
            print("你的输入错误次数已达三次,计算器将自动退出!感谢你的使用!")
            time.sleep(1)
            sys.exit(3)
