#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-16 09:50
# @Author  : zhdya
# @File    : home_work.py

# 1: 写一个python交互的登陆系统

# user_info = {'zhangsan':'zhangsan111','lisi':'lisi111','wangwu':'wangwu111','niuliu':'niuliu111'}
#
# name = input("Pls input your name: ")
# pwd = input("Pls input your password: ")
#
# if name in user_info.keys() and user_info[name] == pwd:
#     print("Success!!")
# else:
#     print("Sorry, you type the wrong username or password!!")

# # 2: 模拟mysql查询语句
# # id  name  age  class  phone_number  gender

# 1 zhangsan 18 python111 1212121211 Man


def select():
    pass


def add():
    input_str = input("Pls add the data like：[id, name, age, class, phone_number, gender]: ")
    f = open('asd.txt','a',encoding='utf-8')
    f.writelines('\n'+input_str)


def delete():
    pass


if __name__ == '__main__':
    print('1:select\n2:add\n3:delete')
    input_num = input('Pls choice the number: ')
    if input_num.isdigit():
        input_num = int(input_num)
        if(input_num==1):
            select()
        elif(input_num==2):
            add()
        elif(input_num==3):
            delete()
        else:
            print("pls just input 1, 2, 3")
    else:
        print("you input was wrong!!")