#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 08:21
# @Author  : zhdya@zhdya.cn
# @File    : Start_Game.py
import random
import sys
import time

user_info = {'zhubajie':'zhubajie','shasheng':'shasheng','sunwukong':'sunwukong','tangzhanglao':'tangseng'}

class Hero(object):
    def __init__(self, HP = 1000, ATK = 1000, DEF = 1000, SP = 1000, RECOV = 1000):
        self.HP = int(HP)
        self.ATK = int(ATK)
        self.DEF = int(DEF)
        self.SP = int(SP)
        self.RECOV = int(RECOV)

    def zhubajie(self):
        ZBJEXP = 0.12 * self.HP + 0.75 * self.ATK + 1 * self.DEF + 0.25 * self.SP + 0.01 * self.RECOV
        return ZBJEXP

    def shasheng(self):
        SSEXP = 0.12 * self.HP + 0.85 * self.ATK + 0.5 * self.DEF + 0.25 * self.SP + 0.01 * self.RECOV
        return SSEXP

    def sunwukong(self):
        SWKEXP = 1 * self.HP + 3 * self.ATK + 3 * self.DEF + 3 * self.SP + 0.01 * self.RECOV
        return SWKEXP

    def tangzhanglao(self):
        TSEXP = 0.1 * self.HP + 0.015 * self.ATK + 0.001 * self.DEF + 0.25 * self.SP + 1 * self.RECOV
        return TSEXP

    def PkTangZhangLao(self):
        new_pk_dic = {'zhubajie': self.zhubajie(), 'shasheng': self.shasheng(), 'sunwukong': self.sunwukong(), 'tangzhanglao': self.tangzhanglao()}
        shaixuan_pk_dic = {'zhubajie': self.zhubajie(), 'shasheng': self.shasheng(), 'sunwukong': self.sunwukong()}
        helper = input("You can call a helper [Y/N]: ")
        if self.pk1 == 'tangzhanglao':
            del shaixuan_pk_dic[self.pk2]
            arandom = random.sample(shaixuan_pk_dic.keys(), 1)
            brandom = ''.join(arandom)
            if helper.strip().lower() != 'y':
                print("<Game Over>: 人生苦短，万事无常... 你被爱徒{0}干死了...".format(self.pk2))
                sys.exit()
            else:
                if new_pk_dic[brandom] > new_pk_dic[self.pk2]:
                    print("Start PK ...")
                    time.sleep(2)
                    print("The Finally Result is ...")
                    time.sleep(2)
                    print("You're so luckcy the helper is {0} and You're a Winner!".format(brandom))
                else:
                    print("Sorry, Unlucky the helper is {0} You Lose it!!".format(brandom))
        else:
            del shaixuan_pk_dic[self.pk1]
            arandom = random.sample(shaixuan_pk_dic.keys(), 1)
            brandom = ''.join(arandom)
            if helper.strip().lower() != 'y':
                print("<Game Over>: 人生苦短，万事无常... 你被爱徒{0}干死了...".format(self.pk1))
                sys.exit()
            else:
                print("Start PK ...")
                time.sleep(2)
                print("The Finally Result is ...")
                time.sleep(2)
                if new_pk_dic[brandom] > new_pk_dic[self.pk1]:
                    print("You're so luckcy the helper is {0} and You're a Winner!".format(brandom))
                else:
                    print("Sorry, Unlucky the helper is {0} You Lose it!!".format(brandom))

    def pk(self):
        new_pk_dic = {'zhubajie': self.zhubajie(), 'shasheng': self.shasheng(), 'sunwukong': self.sunwukong(), 'tangzhanglao': self.tangzhanglao()}
        mmode = input("Two Mode: [1(PK by manual)/2(PK By Auto)]: ")
        if mmode == '1':
            while True:
                self.pk1 = input("Pls input the PlayerA: ")
                self.pk2 = input("Pls input the PlayerB: ")
                if self.pk1 in user_info.keys() and self.pk2 in user_info.keys():
                    print("*********{0} PK {1}*********".format(self.pk1, self.pk2))
                    if self.pk1 == self.pk2:
                        print("Pls choice different role!!")
                        sys.exit()
                    if self.pk1 == 'tangzhanglao' or self.pk2 == 'tangzhanglao':
                        self.PkTangZhangLao()
                        break
                    else:
                        print("Start PK ...")
                        time.sleep(2)
                        print("The Finally Result is ...")
                        time.sleep(2)
                        if new_pk_dic[self.pk1] > new_pk_dic[self.pk2]:
                            print("Congralations, {0} is a Winnwer".format(self.pk1))
                            break
                        else:
                            print("Congralations, {0} is a Winnwer".format(self.pk2))
                            break
                else:
                    print("you input was wrong!!")
        elif mmode == '2':
            a = random.sample(user_info.keys(), 2)
            self.pk1 = a[0]
            self.pk2 = a[1]
            print("*********{0} PK {1}*********".format(self.pk1, self.pk2))
            if self.pk1 == 'tangzhanglao' or self.pk2 == 'tangzhanglao':
                self.PkTangZhangLao()
            else:
                print("Start PK ...")
                time.sleep(2)
                print("The Finally Result is ...")
                time.sleep(2)
                if new_pk_dic[self.pk1] > new_pk_dic[self.pk2]:
                    print("Congralations, {0} is a Winnwer".format(self.pk1))
                else:
                    print("Congralations, {0} is a Winnwer".format(self.pk2))

while True:
    mode_choice = input('pls choice the Number[1(CHECK EXP)/2(PK)/Quit For Exit]: ')
    if mode_choice == '1':
        getnick = input("Pls input your Hero's Nick name: ").strip()
        if getnick in user_info.keys() and getnick == 'zhubajie':
            AA = Hero()
            print("Zhubajie's EXP is {0}".format(AA.zhubajie()))
        elif getnick in user_info.keys() and getnick == 'shasheng':
            AA = Hero()
            print("Shasheng's EXP is {0}".format(AA.shasheng()))
        elif getnick in user_info.keys() and getnick == 'sunwukong':
            AA = Hero()
            print("Sunwukong's EXP is {0}".format(AA.sunwukong()))
        elif getnick in user_info.keys() and getnick == 'tangzhanglao':
            AA = Hero()
            print("Tangzhanglao's EXP is {0}, But he can RECOVERY one times!".format(AA.tangzhanglao()))
        else:
            print("pls confirm your Nick name!!")
    elif mode_choice == '2':
        AA = Hero()
        AA.pk()
    elif mode_choice.lower() == 'quit':
        sys.exit()
    else:
        print("you input was wrong!!")