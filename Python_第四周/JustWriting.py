#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-9 13:30
# @Author  : zhdya@zhdya.cn
# @File    : JustWriting.py


# class MyClass11(object):
#     name = 'zhdya11'
#     gender = 'Man11'
#     age = 211
#     print("MyClass11 Init...")
#
#     def func1(self):
#         print(self.name)
#
# class MyClass22(object):
#     name = 'zhdya22'
#     gender = 'Man22'
#     age = 222
#     print("MyClass22 Init...")
#
#     def func1(self):
#         print(self.name)
#
# class MyClass33(object):
#     name = 'zhdya33'
#     gender = 'Man33'
#     age = 233
#     print("MyClass33 Init...")
#
#     def func1(self):
#         print(self.name)
#
# dict1 = {'aaa':MyClass11, 'bbb':MyClass22, 'ccc':MyClass33}
#
# for k,v in dict1.items():
#     AA = v()
#     AA.func1()

##########################################################################

# class PeopleRen(object):
#     kwell = 'earth'
#
#     def china(self):
#         print("China Init...")
#         self.name = 'zhdya'
#         self.gender = 'Man'
#         self.kwell += '123'
#         PeopleRen.kwell += '123'
#         print(self.kwell)
#         print(PeopleRen.kwell)
#
#
#     def japen(self):
#         print("Japen Init...")
#         self.hoby = 'FFFF'
#         self.eat = 'KKK'
#         print(self.name)
#         PeopleRen.kwell += '123'
#         self.kwell += '123'
#         print(self.kwell)
#         print(PeopleRen.kwell)
#
#
# QQ = PeopleRen()
# QQ.china()
# QQ.japen()

##################################################################


class MyClass(object):
    pass
    # def func1(self):
    #     print('okok')

class MyClass2(object):

    def func1(self):
        print('okok22')

class HHH(MyClass,MyClass2):
    pass


AA = HHH()
AA.func1()
























