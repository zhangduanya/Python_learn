#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-12 22:01
# @Author  : zhdya
# @File    : hello_world.py

aa = "this iw a test file!  "

bb = aa.strip().replace('w','s').split(' ')
print(bb)

name = "zhangduanya"
age = 28

print("hello %s i know your age is %s" %(name, age))

print("asdaaaa".startswith('asd'))

qq = ['a','b','c','d']
print("".join(qq))

ww = list()
for i in range(1,10):
    ww.append(i)
print(ww)

print([i for i in range(1,10)])

asd = ['11','asa','12ws','2q']

asd.sort()
print(asd)