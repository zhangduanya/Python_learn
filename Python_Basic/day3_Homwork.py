#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-21 22:58
# @Author  : zhdya@zhdya.cn
# @File    : day3_Homwork.py.py

# 练习1
# 1. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？ 1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

list1 = [1, 2, 3, 4]
for x in list1:
    for y in list1:
        for z in list1:
            if (x != y ) and (x != z) and (y != z):
                print(x,y,z)

# 2. 打印出所有的“水仙花数”,所谓“水仙花数”是指一个三位数,其各位数字立方和等于该数本身。例如：153是一个“水仙花数”,因为153=1的三次方＋5的三次方＋3的三次方。程序分析：利用for循环控制100-999个数,每个数分解出个位,十位,百位。

for i in range(100,1000):
    unit = i % 10
    ten = i // 10 % 10
    hundred = i // 100
    if unit ** 3 + ten ** 3 + hundred ** 3 == i:
        print("from 100 - 1000 the number is {0}".format(i))

# 3. 两个乒乓球队进行比赛,各出三人。甲队为a,b,c三人,乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比,c说他不和x,z比,请编程序找出三队赛手的名单。

for a in 'xyz':
    for b in 'xyz':
        for c in 'xyz':
            if a != b and b != c and c != a:
                if  a != 'x' and c != 'x' and c != 'z':
                    print("a vs {0}, b vs {1}, c vs {2}".format(a, b, c))

# 练习2
# 1. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 程序分析：对n进行分解质因数,应先找到一个最小的质数i,然后按下述步骤完成：
# (1)如果分解后商为1,则说明分解质因数的过程已经结束,打印出即可。
# (2)如果商不为1,则应打印出i的值,并用n除以i的商,作为新的正整数进行分解,
# 　重复执行第一步。
# (3)如果n不能被i整除,则i的值加1,重复执行第一步。

number = input("Pls input a number：")
if number.isdigit():
    number = int(number)
    chx = 2
    while chx <= number:
        if number % chx == 0:
            number /= chx
            print("{0}".format(chx), end=' ')
        else:
            chx += 1    #不能被num整除就加1
else:
    print("ERROR: Just allow a number!!")





# 2. 猴子吃桃问题：猴子第一天摘下若干个桃子,当即吃了一半,还不瘾,又多吃了一个，第二天早上又将剩下的桃子吃掉一半,又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时,见只剩下一个桃子了。求第一天共摘了多少。
# 程序分析：采取逆向思维的方法,从后往前推断。
