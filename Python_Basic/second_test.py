#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-16 08:37
# @Author  : zhdya
# @File    : second_test.py

# 字符串1：" abc deFGh&*ijkl opq mnrst((uvwxyz "
# 字符串2：" ABC#DEF GH%IJ MNOPQ KLRS&&TUVWX(*&YZ "
# 使用字符串的各种方法转换成如下方式
# ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba

aa = " abc deFGh&*ijkl opq mnrst((uvwxyz "
xx = " ABC#DEF GH%IJ MNOPQ KLRS&&TUVWX(*&YZ "
bb = aa.strip().lower().replace(' ','').replace('&','').replace('*','').replace('(','')
nbb = bb[:12] + bb[15:17] + bb[12:15] + bb[17:27]
asd = nbb[::-1]
print(asd)

xx1 = xx.strip().replace(' ','').replace('&','').replace('*','').replace('(','').replace('#','').replace('#','').replace('%','')
print(xx1)
xx2 = xx1[:10] + xx1[15:17] + xx1[10:15] +xx1[17:27]
print(xx2)
nnn = xx2 + asd
print(nnn)
