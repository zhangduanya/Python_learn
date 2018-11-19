#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-19 22:01
# @Author  : zhdya
# @File    : day1.py

# 练习1：
# 将 “123” 转换成整数
# 将 “9999999999999999999” 转换成长整数
# 将 “3.1415926” 转换成一个浮点数
# 将 123 转换成一个字符串
# 现有以下字符串
# 字符串1：" abc deFGh&*ijkl opq mnrst((uvwxyz "
# 字符串2：" ABC#DEF GH%IJ MNOPQ KLRS&&TUVWX(*&YZ "
# 使用字符串的各种方法转换成如下方式
# ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba

print(int("123"))
print(float("3.1415926"))
print(str(123))
aa = " abc deFGh&*ijkl opq mnrst((uvwxyz "
newaa = aa.strip().replace('&', '').replace('(', '').replace('*','').replace(' ','').lower()
newaa = newaa[:12] + newaa[15:17] + newaa[12:15] + newaa[17:27]
print(newaa)

bb = " ABC#DEF GH%IJ MNOPQ KLRS&&TUVWX(*&YZ "
newbb = bb.strip().replace('&', '').replace('(', '').replace('*','').replace(' ','').replace('%','').replace('#','')
newbb = newbb[:10] + newbb[15:17] + newbb[10:15] +newbb[17:27]
print(newbb)

newcc = newbb + newaa[::-1]
print(newcc)

##############################################################################
# 练习2：
# 现有列表
list1 = ['XXXX', 'b', 3, 'c', '&', 'a', 3, '3', 3, 'aa', '3', 'XXXX']
list2 = ['e', 'f', 'g']
# 要求对其做以下操作：
# 1. 取出 ‘XXXX’ 中间的部分，形成一个新的列表list3
# 2. 对list3 做一下几部操作
# 1）删除特殊符号
# 2）统计 3 在list3中出现的次数
# 3）用最简短的代码去除list3中 26个字母以外的元素(要求只能对list3操作)
# 4）对list3排序
# 5）在末尾追加'd',并把list2追加到list3

list3 = list1[1:11]

list3.pop(3)
print(list3)

print(list3.count(3))

list3.pop(1)
list3 = list3[0:3]
print(list3)

list3.sort()
print(list3)

list3.append('d')
print(list3)

list3.extend(list2)
print(list3)

###################################################################
# 练习3. 现有两个变量
a = ('h',)
b = ('h')
# 1）将a和b分别追加到上一题的list3中，观察有什么区别
# 2）将1生成的list3转换成元组(扩展：自己搜索方法)
# 3）打印出只有一个元素'h'的元组，在2中生成的元组中的索引

list3.extend(a)
list3.extend(b)
print(list3)

newlist3 = (list3,)
print(newlist3)

print(newlist3.index('h'))