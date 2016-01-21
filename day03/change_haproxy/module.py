#!/usr/local/env python3
'''
Author:@南非波波
Blog:http://www.cnblogs.com/songqingbo/
E-mail:qingbo.song@gmail.com
'''

import json,os,shutil,time
import index

ha = "./haproxy.conf"

#备份配置文件
def haBak(ha):
    shutil.copyfile(ha,ha + '.bak')

#获取文件行数
def countnum(filename):
    files = open(filename)
    data = files.read()
    files.flush()
    files.close()
    return data.count('\n')

#获取文件所有内容
def getAllContent(ha):
    with open(ha,'r+') as f:
        all_content = f.read() #获取文件所有内容
    return all_content

#获取文件指定的label内容
def getAllContentDict(ha):
    with open(ha,'r+') as f:
        all_content = f.read() #获取文件所有内容，类型为str
        all_content_dict = {} #初始化一个总的字典。将文件的所有内容都存档到该字典中
        record = [] #初始化一个record列表，该列表用来存储每个label下面的记录值
        for line in all_content.split('\n'): #按照换行符进行每行内容遍历
            label_dict_temp = {} #初始化一个label的临时字典，该字典记录的是{label:record}
            if not line.startswith("        "): #判断每行内容是否为8个空格字符开头，这里取否，取的是label值
                record = [] #每次获取label值都要对record列表进行初始化，这里修改的是全局变量
                label_dict_temp[line] = record ##将record列表作为values值添加到label_dict_temp临时字典中
            else: #每行内容为8个空格字符开头，取得是label下面的record值
                record.append(line.strip())  #将该行的值append到record列表中，每行记录值以元素的身份存在在record中
            all_content_dict.update(label_dict_temp) #将获取的{label:record}字典更新到总的字典中
    return all_content_dict #最后返回值为配置文件的label内容


#增加模块记录值
def addLabelRecord(ha,dict_input):
    with open(ha,'r') as all_content,open(ha+'.new','w+') as all_content_new:
        all_content_dict = getAllContentDict(ha)
        add_str = "        server %s %s weight %s maxconn %s\n" % (dict_input['server'],dict_input['server'],dict_input['weight'],dict_input['maxconn'])
        if dict_input['label'] in all_content_dict.keys():
            flag = False
            for line in all_content.readlines():
                all_content_new.write(line)
                if line.strip('\n') == dict_input['label']:
                    flag = True
                    continue
                if flag:
                    all_content_new.write(add_str)
                    flag = False
        else:
            pass

    print("增加成功!")
    choice = input("请选择是否要更新到线上(y/n):").strip()
    if index.choiceIf(choice) == True:
        print("你选择的是更新到线上,系统即将把修改后的文件发布到线上并返回系统首页!")
        if os.path.exists(ha + '.bak'):
            os.remove(ha + '.bak')
        os.rename(ha,ha+'.bak')
        os.rename(ha+'.new',ha)
        time.sleep(1)
        index.chooseView(index.showView())
    if index.choiceIf(choice) == False:
        print("你选择的是放弃更新,系统即将返回系统首页!")
        if os.path.exist(ha + '.new'):
            os.remove(ha + '.new')
        index.chooseView(index.showView())

def delLabelRecord(ha,dict_input):
    with open(ha,'r') as all_content,open(ha+'.new','w+') as all_content_new:
        all_content_dict = getAllContentDict(ha)
        del_str = "        server %s %s weight %s maxconn %s\n" % (dict_input['server'],dict_input['server'],dict_input['weight'],dict_input['maxconn'])
        if dict_input['label'] in all_content_dict.keys():
            flag = False
            for line in all_content.readlines():
                if line.strip('\n') == dict_input['label']:
                    flag = True
                    all_content_new.write(line)
                    continue
                if flag == True and line == del_str:
                    flag = False
                    continue
                all_content_new.write(line)
        else:
            pass
    print("删除成功!")
    choice = input("请选择是否要更新到线上(y/n):").strip()
    if index.choiceIf(choice) == True:
        print("你选择的是更新到线上,系统即将把修改后的文件发布到线上并返回系统首页!")
        if os.path.exists(ha + '.bak'):
            os.remove(ha + '.bak')
        os.rename(ha,ha+'.bak')
        os.rename(ha+'.new',ha)
        time.sleep(1)
        index.chooseView(index.showView())
    if index.choiceIf(choice) == False:
        print("你选择的是放弃更新,系统即将返回系统首页!")
        if os.path.exists(ha + '.new'):
            os.remove(ha + '.new')
        index.chooseView(index.showView())

def chgLabelRecord(ha):
    #获取用户修改label记录值
    print("下面请按照提示输入你要修改的记录值！")
    dict_input1 = index.getInputConnet()
    print("下面请按照提示输入你要修改后的记录值!")
    dict_input2 = index.getInputConnet()
    with open(ha,'r') as all_content,open(ha+'.new','w+') as all_content_new:
        all_content_dict = getAllContentDict(ha)
        old_str = "        server %s %s weight %s maxconn %s\n" % (dict_input1['server'],dict_input1['server'],dict_input1['weight'],dict_input1['maxconn'])
        new_str = "        server %s %s weight %s maxconn %s\n" % (dict_input2['server'],dict_input2['server'],dict_input2['weight'],dict_input2['maxconn'])
        print(new_str)
        if dict_input1['label'] in all_content_dict.keys():
            flag = False
            for line in all_content.readlines():
                if line.strip('\n') == dict_input1['label']:
                    flag = True
                    all_content_new.write(line)
                    continue
                if flag == True and line == old_str:
                    all_content_new.write(new_str)
                    flag = False
                    continue
                all_content_new.write(line)
        else:
            pass
    print("修改成功!")
    choice = input("请选择是否要更新到线上(y/n):").strip()
    if index.choiceIf(choice) == True:
        print("你选择的是更新到线上,系统即将把修改后的文件发布到线上并返回系统首页!")
        if os.path.exists(ha + '.bak'):
            os.remove(ha + '.bak')
        os.rename(ha,ha+'.bak')
        os.rename(ha+'.new',ha)
        time.sleep(1)
        index.chooseView(index.showView())
    if index.choiceIf(choice) == False:
        print("你选择的是放弃更新,系统即将返回系统首页!")
        if os.path.exists(ha + '.new'):
            os.remove(ha + '.new')
        index.chooseView(index.showView())