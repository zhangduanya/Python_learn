#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-21 07:31
# @Author  : zhdya@zhdya.cn
# @File    : day2_Homwork.py

# 练习1：
# 1. 现有一个字典dict1 保存的是小写字母a-z对应的ASCII码

dict1 = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 96, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 117, 't': 116, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}

# 1） 将该字典按照ASCII码的值排序
dict1 = sorted(dict1.items(), key = lambda x:x[1])
print(dict1)

# 2） 有一个字母的ASCII错了，修改为正确的值，并重新排序
dict1.pop(0)
dict1.append(('o',111),)
dict1 = sorted(dict1)
print(dict1)

# 2. 用最简洁的代码，自己生成一个大写字母 A-Z 及其对应的ASCII码值的字典dict2(使用dict，zip，range方法)
list1 = ([i for i in range(65,91)])
list2 = ([chr(i) for i in range(ord("A"),ord("Z")+1)])      ##ord 函数将字符转换为整数显示，chr 函数将整数转换为字符显示；
dict2 = list(zip(list2,list1))      ##python3 如上结果是一个对象，python2可以直接显示；
print(dict2)

# 3. 将dict2与第一题排序后的dict1合并成一个dict3
dict3 = list()
dict1.extend(dict2)
dict3.extend(dict1)
print(dict3)

############################################################################################################################################################################################
# 练习2
# 1. 输入三个整数x,y,z，请把这三个数由小到大输出。 1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换， 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
x = input("Pls input a number: ")
y = input("Pls input a number: ")
z = input("Pls input a number: ")
if x.isdigit() and y.isdigit() and z.isdigit():
    aa = [x,y,z]
    for i in range(len(aa)):
        for j in range(i+1):
            if aa[i] < aa[j]:
                aa[i],aa[j] = aa[j],aa[i]
    print(aa)
else:
    print("you input is not a number!!")


# 2. 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高 于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提 成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于 40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于 100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

money = input("Pls input your lirun: ")
lirun = [100000, 200000, 400000, 600000, 1000000]
ticheng = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

if money.isdigit():
    money = int(money)
    if money <= lirun[0]:
        get_money = money * ticheng[0]
        print("this month you can get lirun is: {0}RMB".format(get_money))
    elif lirun[0] < money <= lirun[1]:
        get_money = (money - lirun[0]) * ticheng[1] + lirun[0] * ticheng[0]
        print("this month you can get lirun is: {0}RMB".format(get_money))
    elif lirun[1] < money <= lirun[2]:
        get_money = (money - lirun[1]) * ticheng[2] + lirun[0] * ticheng[0] + lirun[0] * ticheng[1]
        print("this month you can get lirun is: {0}RMB".format(get_money))
    elif lirun[2] < money <= lirun[3]:
        get_money = (money - lirun[2]) * ticheng[3] + lirun[0] * ticheng[0] + lirun[0] * ticheng[1] + lirun[1] * ticheng[2]
        print("this month you can get lirun is: {0}RMB".format(get_money))
    elif lirun[3] < money <= lirun[4]:
        get_money = (money - lirun[3]) * ticheng[4] + lirun[0] * ticheng[0] + lirun[0] * ticheng[1] + lirun[1] * ticheng[2] + lirun[2] * ticheng[3]
        print("this month you can get lirun is: {0}RMB".format(get_money))
    elif money > lirun[4]:
        get_money = (money - lirun[4]) * ticheng[5] + lirun[0] * ticheng[0] + lirun[0] * ticheng[1] + lirun[1] * ticheng[2] + lirun[2] * ticheng[3] + lirun[3] * ticheng[4]
        print("this month you can get lirun is: {0}RMB".format(get_money))
else:
    print("you input was wrong!!")
