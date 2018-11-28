#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-28 22:16
# @Author  : zhdya@zhdya.cn
# @File    : Python_Wednesday.py


##程序的递归
aaa = input("Pls input a number: ")

def asd(n):
    if n == 0:
        return 1
    else:
        return n * asd(n-1)

print(asd(int(aaa)))