# Author : .CseiseiG.
# -*- codeing = utf-8 -*-
# @Time : 2022/10/2 20:55
# @Author : 12542
# @File : 1.py
# @Software : PyCharm
import random

print("\033[31m 1. --- print输出 ---\033[0m")
# print("莫道谗言如浪深，\n莫言迁客似沙沉.\n千淘万漉虽辛苦，\n吹尽狂沙始到金。")
# print("莫道谗言如浪深，\n"
#       "莫言迁客似沙沉，\n"
#       "千淘万漉虽辛苦，\n"
#       "吹尽狂沙始到金。")


print("\033[31m 2. --- if语句 ---\033[0m")
# one_num = random.randint(0, 100)
# for n in range(1, 100):
#     user_num = int(input("请输入0~100的数字："))
#     if user_num == one_num:
#         print("\033[32m √ \033[0m")
#         break
#     elif user_num < one_num:
#         print("你输\033[31m小\033[0m了！")
#     elif user_num > one_num:
#         print("你输\033[31m大\033[0m了!")


print("\033[31m 3. --- 判断 ---\033[0m")
# Adam = input("请输入‘管理员’ ： ")
# if Adam == "管理员":
#     print("admin")
# else:
#     print("Error！")


print("\033[31m 4. --- 判断奇偶 ---\033[0m")
# integer = int(input("请输入一个整数："))
# if integer % 2 == 0:
#     print("偶数！")
# else:
#     print("奇数！")


print("\033[31m 5. --- 计算BMI ---\033[0m")
# height, weight = (input("请输入身高和体重：").split())
# height = float(height)
# weight = int(weight)
# # print(height, weight, type(height))
# BMI = weight / (height * height)
# print(f"你的BMI值为：{BMI:.2f}")
# if BMI < 18.5:
#     print("过轻！")
# elif 18.5< BMI < 24.99:
#     print("正常！")
# elif 25 < BMI < 28:
#     print("过重！")
# elif 28 < BMI < 32:
#     print("肥胖! ")


print("\033[31m 6. --- 计算象限 ---\033[0m")
# x, y = (input("请输入X和Y：").split())
# x = float(x)
# y = float(y)
# if x == 0 and y == 0:
#     print("坐标再原点!")
# elif x == 0 or y == 0:
#     if x == 0 and y != 0:
#         print("坐标在Y轴上！")
#     elif y == 0 and x != 0:
#         print("坐标在X轴上！")
# elif x and y != 0:
#     if x > 0 and y > 0:
#         print("坐标在第一象限！")
#     elif x > 0 and y < 0:
#         print("坐标在第四象限！")
#     elif x < 0 and y > 0:
#         print("坐标在第二象限！")
#     elif x < 0 and y < 0:
#         print("坐标在第三象限！")


print("\033[31m 7. --- 计算季节 ---\033[0m")
# months = {
#     "春季": [3, 4, 5],
#     "夏季": [6, 7, 8],
#     "秋季": [9, 10, 11],
#     "冬季": [12, 1, 2]
# }
# num = (input("请输入月份："))
# print(months.keys())
# print(type(months.values()))
# for key, val in months.items():
#     if num in str(val):
#         print(key)
#         print(type(num))




print("\033[31m 8&9. --- 计算闰平年和月份天数 ---\033[0m")

year, month = (input("请输入年份和月份：").split())
year = int(year)


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return "闰年！"
    elif year % 400 == 0:
        return "闰年！"
    else:
        return "平年！"


how_year = leap_year(year)
month_days = {
    "28": [2],
    "30": [4, 6, 9, 11],
    "31": [1, 3, 5, 7, 8, 10, 12]
}
if int(month) == 2 and how_year == "闰年！":
    print("本月29天！")
else:
    for key, val in month_days.items():
        if month in str(val):
            print(f"本月{key}天！")
            break


# print(leap_year(year))



















