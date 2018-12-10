#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-9 16:29
# @Author  : zhdya@zhdya.cn
# @File    : Login_Sys.py


import sys
from Python_第四周.Third_HomeW.conf import settings

class Login(object):
    numberlisi = 1
    numberzhangsan = 1
    numberniuliu = 1
    numberwangwu = 1

    def lisi(self, pwd):
        self.pwd = pwd
        if settings.user_info[name] == pwd:
            print("This is you {0} times Login!!".format(Login.numberlisi))
            Login.numberlisi += 1

    def zhangsan(self, pwd):
        self.pwd = pwd
        if settings.user_info[name] == pwd:
            print("This is you {0} times Login!!".format(Login.numberzhangsan))
            Login.numberzhangsan += 1

    def wangwu(self, pwd):
        self.pwd = pwd
        if settings.user_info[name] == pwd:
            print("This is you {0} times Login!!".format(Login.numberwangwu))
            Login.numberwangwu += 1

    def niuliu(self, pwd):
        self.pwd = pwd
        if settings.user_info[name] == pwd:
            print("This is you {0} times Login!!".format(Login.numberniuliu))
            Login.numberniuliu += 1


    def check(self, name):
        self.name = name
        if name in settings.user_info.keys() and name == 'lisi':
            self.lisi(pwd)
        elif name in settings.user_info.keys() and name == 'zhangsan':
            self.zhangsan(pwd)
        elif name in settings.user_info.keys() and name == 'wangwu':
            self.wangwu(pwd)
        elif name in settings.user_info.keys() and name == 'niuliu':
            self.niuliu(pwd)
        # else:     ##if total the failue times, just start this func!!
        #     Login.number += 1


while True:
    name = input("Pls input your name['quit' for exit!]: ").strip()
    if name == 'quit':
        sys.exit()
    pwd = input("Pls input your password: ").strip()
    AA = Login()
    AA.check(name)