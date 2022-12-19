# Author : .CseiseiG.
# -*- codeing = utf-8 -*-
# @Time : 2022/9/25 15:02
# @Author : 12542
# @File : P67_P69.py
# @Software : PyCharm

"""函数

def add2num(a, b):
    return a + b


def add3num(a, b, c):
    return add2num(add2num(a, b), c)


print(add3num(10, 20, 30))
"""

"""课堂练习
"""
# 练习1
def line(n):
    return "-" * n
print(line(20))


#练习2
def sum_3_num(a, b, c):
    return a + b + c
# print(sum_3_num(12, 34, 56))

a = int(input("1个数："))
b = int(input("2个数："))
c = int(input("3个数："))
print(sum_3_num(a, b, c))