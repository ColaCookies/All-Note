# Author : .CseiseiG.
# -*- codeing = utf-8 -*-
# @Time : 2022/9/25 15:48
# @Author : 12542
# @File : P70_P78.py
# @Software : PyCharm


# case2 = [9, 8, 8, 3, 3, 1]
# out = [x for x in case2 if x % 2 != 0]
# print(out)

a = 100
b = 200


def change():
    global a
    a = 300
    b = 225
    # print(a)
    print(b)

change()
print(b)



print(f"\033[31m{'斐波拉契数列(递归版)':-^16}\033[0m")
def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(8))


print(f"\033[31m{'斐波拉契数列(for循环版)':-^16}\033[0m")
def feb(n):
    if n <= 1:
        return 0
    res = 0
    feb0 = 0
    feb1 = 1
    for i in range(2, n+1):
        print(f"res:{res}, feb:{feb0}, feb1:{feb1}")
        res = feb0 + feb1
        feb0 = feb1
        feb1 = res
    return res
print(feb(8))




