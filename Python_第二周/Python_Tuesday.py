#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-27 07:48
# @Author  : zhdya@zhdya.cn
# @File    : Python_Tuesday.py


def fun(a, *aa, **aaa):
    print("{0}, {1}, {2}".format(a, aa, aaa))

if __name__ == '__main__':
    fun(1,2,3,4,5,x=1,y=7)

##结果输出：
# 1, (2, 3, 4, 5), {'x': 1, 'y': 7}

abc = lambda x,y,z:x+y+z
print(abc(1,2,3))

##随便输入一个数，求这个范围内的阶乘和

def jc(i):
    sum = 1
    if i == 1:
        return i
    else:
        for j in range(1,int(i)+1):
            sum *= j
            print(sum)
        return sum

def main():
    total = 0
    number = input("Pls input a number: ")
    if number.isdigit():
        for i in range(1,int(number)+1):
            total += jc(i)
            print(total)
        print(total)
    else:
        print("pls just input a number!!")

if __name__ == '__main__':
    main()

##随便输入一个数，求这个数的阶乘：
#
num = input("Pls input a number: ")
if num.isdigit():
    total = 1
    num = int(num)
    while num:
        total *= num
        num -= 1
    print(total)
else:
    print("you input was wrong!!")

# 1. 设计一个程序，从终端接收5个数字，并使用自己编写的排序函数，对5个数字排序后输出
import sys

list1 = list()
n = 5
while n:
    number = input("Pls input sth: ")
    if number.isdigit():
        list1.append(number)
    else:
        print("you input was wrong!!")
        sys.exit()
    len1 = len(list1)
    n -= 1

for i in range(0,len1):
    for j in range(i+1,len1):
        if int(list1[i]) > int(list1[j]):
            list1[i],list1[j] = list1[j],list1[i]
print(list1)




