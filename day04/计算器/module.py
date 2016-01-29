#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''

import re

#匹配一个表达式中的数字和运算符，如果匹配，返回expression，否则返回None
def num_operator(expression):
    match_list = re.findall("[0-9]|\(|\)|\+|\-|\*|\/|.",expression)
    if len(expression) == len(match_list):
        return True

#特殊字符处理
def charmap(expression):
    flag = True
    while flag:
        if expression.__contains__("++") or expression.__contains__("+-") or expression.__contains__("-+") or expression.__contains__("--"):
            # match_str = re.search("\d+\.*\d*(\+\-){1}\d+\.*\d*",expression).group()
            expression = expression.replace('+-','-')
            expression = expression.replace('++','+')
            expression = expression.replace('-+','-')
            expression = expression.replace('--','+')
        else:
            flag = False
    return expression
#操作加减
def compute_add_sub(expression):
    '''
    expression表达式传进来的形式是(5+1-4)，左右成一对括号。所以这里需要将括号去掉
    '''
    expression = expression.lstrip('(').rstrip(')') #去除表达式左右的括号
    match_test = re.search("\d+\.*\d*[\+\-]{1}\d+\.*\d*",expression)
    if not match_test:
        return expression
    else:
        match_str = match_test.group()
        if len(match_str.split('+')) > 1:
            num1,num2 = match_str.split("+")
            result = float(num1) + float(num2)
        else:
            num1,num2 = match_str.split("-")
            result = float(num1) - float(num2)
        exp_join = expression.split(match_str)
        expression = "%s%s%s" % (exp_join[0],result,exp_join[1])
    return compute_add_sub(expression)

#操作乘除
def compute_mul_div(expression):
    '''
    expression表达式传进来的形式是(9-2*5/3+7/3*99/4*2998+10*568/14)，左右成一对的括号。所以这里就需要将括号去掉然后递归处理乘除
    '''
    expression = expression.lstrip('(').rstrip(')') #去除表达式左右的括号
    match_test = re.search("\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*",expression)
    if not match_test: #判断是否能够匹配到* 或者 /。
        return expression
    else:
        match_str = match_test.group() #获取到匹配的运算式，比如5/3，2*5
        if len(match_str.split("/")) > 1: #计算除法
            num1,num2 = match_str.split("/")
            result = float(num1) / float(num2)
        else: #计算乘法 len(match_str.split("*")) > 1
            num1,num2 = match_str.split("*")
            result = float(num1) * float(num2)
        exp_join = expression.split(match_str)
        expression = "%s%s%s" % (exp_join[0],result,exp_join[1])
        compute_mul_div(expression)  #递归处理
    return compute_mul_div(expression)

#处理优先级的执行
def compute_pri(expression):
    expression = compute_mul_div(expression) #处理乘除
    expression = charmap(expression) #处理特殊字符
    expression = compute_add_sub(expression)  #处理加减
    return expression #返回一个值

#递归处理括号
def recursion_bracket(expression):
    match_list = re.findall("\(|\)",expression) #匹配括号,如果存在递归处理
    if not match_list:
        # print(expression)
        return compute_pri(expression)
    else:
        match_str = re.search("\([^()]*\)",expression) #匹配第一次出现的括号对
        if match_str:
            match_str = match_str.group()
            # print("match_str:",match_str)
            tmp = compute_pri(match_str)
            expression = "%s%s%s" % (expression.split(match_str)[0],tmp,expression.split(match_str)[1]) #字符串拼接
            # print("expression:",expression)
    return recursion_bracket(expression) #递归处理括号




# expression = "(9-2*5/3+7/3*99/4*2998+10*568/14)"
# res = compute_pri(expression)
# print(res)
#递归处理括号
# def recursion_bracket(expression):
#     match_list = re.findall("\(|\)",expression) #匹配括号,如果存在递归处理
#     if match_list:
#         tmp_list = [] #定义一个列表，存储左括号(
#         res = ''
#         for i in range(0, len(expression)):
#             if expression[i] == "(":
#                 tmp_list.append(i) #获取括号出现的索引值列表
#                 print("tmp_list:",tmp_list)
#                 continue
#             if expression[i] == ")" and tmp_list:
#                 ts = expression[tmp_list[-1]: i+1]
#                 if len(ts) > len(res):
#                     # ts = compute_mul_div(ts)
#                     # print(ts)
#                     # ts = charmap(ts)
#                     # ts = compute_add_sub(ts)
#                     res = ts
#                     print('i:%s,ts:%s' % (i,ts))
#                 tmp_list.pop()
#                 print(tmp_list)
#         print("res:",res)
#         # return recursion_bracket(res)
#
#     else: #匹配括号失败，返回表达式,做后续处理
#         expression = compute_mul_div(expression)
#         expression = charmap(expression)
#         expression = compute_add_sub(expression)