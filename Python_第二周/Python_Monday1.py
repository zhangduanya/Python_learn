#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-26 20:36
# @Author  : zhdya@zhdya.cn
# @File    : Python_Monday1.py

##判断输入的字符分别为多少个：

dig = list()
alp = list()
other = list()

alp2 = dict()


inpu = input('Pls input anything: ')

for i in inpu:
    if i.isdigit():
        dig.append(i)
    elif i.isalpha():
        alp.append(i)
    else:
        other.append(i)

for i in alp:
    alp2[i] = alp.count(i)
for k,v in alp2.items():
    print(k,v)

print("the number of digit is {0}".format(len(dig)))
print("the number of alp is {0}".format(len(alp)))
print("other total is {0}".format(len(other)))


##判断输入一个数是否为数字

def fun():
    sth = input("Pls input sth: ")

    try:
        sth = int(sth)
        if type(sth) == type(1):
            print("{0} is a number!".format(sth))
    except:
        print("{0} is not a number!!".format(sth))

if __name__ == '__main__':
    fun()




