#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-24 09:39
# @Author  : zhdya@zhdya.cn
# @File    : Python_Monday.py

##    id username age classs phone_number gender
##    6 zhdya 28 python666 18862223222 Man

menu = ['id', 'username', 'age', 'class', 'phone_number', 'gender']

def select():
    while 1:
        input_str = input("Pls input the select command like: [select * from asd], [quit] for exit!: ")
        if input_str == 'quit':
            break
        if input_str.startswith('select') and input_str.split()[1] == '*' and input_str.split()[2] == 'from' and input_str.split()[3] == 'asd':
            with open('asd.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    print(line)
            break
        if input_str.startswith('select') and input_str.split()[1] in menu:
            chx = input_str.split()[1]
            if chx == 'username':
                with open('asd.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        newline = line.split()[1]
                        print(newline)
                break
        if input_str.startswith('select') and input_str.split()[1] in menu:
            chx = input_str.split()[1]
            if chx == 'id':
                with open('asd.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        newline = line.split()[0]
                        print(newline)
                break
        if input_str.startswith('select') and input_str.split()[1] in menu:
            chx = input_str.split()[1]
            if chx == 'age':
                with open('asd.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        newline = line.split()[2]
                        print(newline)
                break
        else:
            print("you input was wrong, pls checking it and input it again!!")


def insert():
    while 1:
        input_str = input("Pls input the insert command like: [insert into asd values ( id username age class phone_number gender )], [quit] for exit!: ")
        if input_str == 'quit':
            break
        if input_str.startswith('insert') and input_str.split()[1] == 'into' and input_str.split()[2] == 'asd' and input_str.split()[3] == 'values':
            newinput = input_str.split('(')[1].split(')')[0]
            with open('asd.txt', 'a', encoding='utf-8') as f:
                f.writelines('\n' + newinput)
                print("successfully import data: <{0}>".format(newinput))
            break
        else:
            print("you input was wrong, pls checking it and input it again!!")

def delete():
    while 1:
        input_str = input("Pls input the delete command like: [delete from asd where id= 1], [quit] for exit!: ")
        if input_str == 'quit':
            break
        if input_str.split('delete') and input_str.split()[1] == 'from' and input_str.split()[2] == 'asd' and input_str.split()[3] == 'where' and input_str.split()[4] == 'id=':
            newinput = input_str.split()[5]
            with open('asd.txt', 'r', encoding='utf-8') as f:
                datas = f.readlines()
                with open('asd.txt','w',encoding='utf-8') as fw:
                    for line in datas:
                        if newinput == line.split()[0]:
                            continue
                        fw.write(line)
                    break
        else:
            print("you input was wrong, pls checking it and input it again!!")


if __name__ == '__main__':
    print('1:select\n2:add\n3:delete\n4:update')
    input_num = input('Pls choice the number: ')
    if input_num.isdigit():
        input_num = int(input_num)
        if(input_num==1):
            select()
        elif(input_num==2):
            insert()
        elif(input_num==3):
            delete()
        elif(input_num==4):
            update()
        else:
            print("pls just input 1, 2, 3, 4")
    else:
        print("you input was wrong!!")