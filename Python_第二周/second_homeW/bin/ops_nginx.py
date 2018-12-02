#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-1 13:27
# @Author  : zhdya@zhdya.cn
# @File    : ops_nginx.py


groupA = ['10.0.0.1:8080', '10.0.0.2:8080']
groupB = ['192.168.0.1:8080', '192.168.0.2:8080']

def startA():
    with open('../conf/nginx.conf', 'r', encoding='utf-8') as f:
        datas = f.readlines()
    with open('../conf/nginx.conf', 'w', encoding='utf-8') as fw:
        for line in datas:
            if line.strip().startswith('server') and line.strip().split()[1] in groupA:
                print("ERROR!! the {0} is Running now!!".format(line.strip().split()[1]))
            elif line.strip().startswith('#server') and line.strip().split()[1] in groupA:
                line = line.replace('#server','server')
                print("Start {0} successful!!".format(line.strip().split()[1]))
            fw.write(line)


def shutdownA():
    with open('../conf/nginx.conf', 'r', encoding='utf-8') as f:
        datas = f.readlines()
    with open('../conf/nginx.conf', 'w', encoding='utf-8') as fw:
        for line in datas:
            if line.strip().startswith('#server') and line.strip().split()[1] in groupA:
                print("ERROR!! The {0} Already shutdown!!".format(line.strip().split()[1]))
            elif line.strip().startswith('#server') and line.strip().split()[1] in groupB:
                print("WARNING!! The {0} is Shutdown now!!".format(line.strip().split()[1]))
            elif line.strip().startswith('server') and line.strip().split()[1] in groupA:
                line = line.replace('server','#server')
                print("Shutdown {0} successful!!".format(line.strip().split()[1]))
            fw.write(line)


def startB():
    with open('../conf/nginx.conf', 'r', encoding='utf-8') as f:
        datas = f.readlines()
    with open('../conf/nginx.conf', 'w', encoding='utf-8') as fw:
        for line in datas:
            if line.strip().startswith('server') and line.strip().split()[1] in groupB:
                print("ERROR!! the {0} is Running now!!".format(line.strip().split()[1]))
            elif line.strip().startswith('#server') and line.strip().split()[1] in groupB:
                line = line.replace('#server','server')
                print("Start {0} successful!!".format(line.strip().split()[1]))
            fw.write(line)


def shutdownB():
    with open('../conf/nginx.conf', 'r', encoding='utf-8') as f:
        datas = f.readlines()
    with open('../conf/nginx.conf', 'w', encoding='utf-8') as fw:
        for line in datas:
            if line.strip().startswith('#server') and line.strip().split()[1] in groupB:
                print("ERROR!! The {0} Already shutdown!!".format(line.strip().split()[1]))
            elif line.strip().startswith('#server') and line.strip().split()[1] in groupA:
                print("WARNING!! The {0} is Shutdown now!!".format(line.strip().split()[1]))
            elif line.strip().startswith('server') and line.strip().split()[1] in groupB:
                line = line.replace('server','#server')
                print("Shutdown {0} successful!!".format(line.strip().split()[1]))
            fw.write(line)


def restartNginx():
    print("Restart Nginx successful!!")


def updateCode():
    print("Update Code successful!!")


if __name__ == '__main__':
    print('1:start nginx_A\n2:Shutdown nginx_A\n3:start nginx_B\n4:shutdown nginx_B\n5:restart Nginx\n6:update code')
    while 1:
        input_num = input('Pls choice the number [quit for exit]: ')
        if input_num.isdigit():
            input_num = int(input_num)
            if(input_num==1):
                startA()
            elif(input_num==2):
                shutdownA()
            elif(input_num==3):
                startB()
            elif(input_num==4):
                shutdownB()
            elif (input_num == 5):
                restartNginx()
            elif(input_num==6):
                updateCode()
            else:
                print("pls just input 1, 2, 3, 4!!")
                continue
        elif (input_num == "quit"):
            break
        else:
            print("you input was wrong!!")
            continue