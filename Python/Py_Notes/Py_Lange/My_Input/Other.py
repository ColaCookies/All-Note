# age = 21
# news = "中国"
#
# print("我的年龄是%d岁，国籍是%s" % (age, news))


# info = {"name": "张三", "age": 18}
# str = "姓名：{name}, 年龄：{age}".format(**info)
#
# print(str)


# print("圆周率：{:.2f}".format(3.1415926))
# print("{:,}".format(10000000))
# print("{:.2e}".format(1000000000))

# str = "滴CBL滴"
# print("{:*>10}".format(str))
# print("{:#<10}".format(str))
# print("{:@^11}".format(str))


# s = input("请输入一个字符串:")
# print("{:=^14}".format(s))

# info = {"name": "张三", "age": 18}
# str = "姓名：{name}\n年龄：{age}".format(**info)
# print(str)


# path = r"c:\temp\1.mp3"
# print(path)


# str1 = "chenBL"
# print(len(str1))
# print(f"{str1}[2]:", str1[2])
# print(f"{str1}[0:2]:", str1[0:2])
# print(f"{str1}[2:5]:", str1[2:5])
# print(f"{str1}[2:-1]:", str1[2:-1])

# str1 = "IT私塾。"
# str1 += "学以致用"
# print(str1 + "高效学习")
# print('-' * 30)
# str2 = "这是一个很长的字符串，以至于一行都写不完" \
#        "那就第二行接着写"\
#        "可以一直写下去，都算一个字符串" \
#        "可以不可以" \
#        "啊哈哈啊"
# print(str2)


"""字母转换
str = "Cbl The Is A Good 9559"
res_capitalize = str.capitalize()
print(res_capitalize)
res_title = str.title()
print(res_title)
res_istitle = str.istitle()
print(res_istitle)
res_upper = str.upper()
print(res_upper)
res_swapcase = str.swapcase()
print(res_swapcase)
"""

"""统计与查找
str = "Cbl The 我 Is A cbl我的 Good 225 cbl 9559 我 我的的我"
print(len(str))
res_count = str.count("的", 30, 50)
print(res_count)
res_find = str.find("我", 46)
print(res_find)
res_find2 = str.find('cbl', 16)
print(res_find2)
res_indes = str.index('cbl', 35)
print(res_indes)
"""

"""判断开头结尾
str = "Cbl The 我 Is A cbl我的 Good 225 cbl 9559 我 我的的我"
print(len(str))
res = str.startswith('T', 4, 30)
print(res)
res_end = str.endswith("我", -19, -3)
print(res_end)

"""

"""分隔与拼接
str = "Cbl The 我 Is A_cbl_我的 Good_225 cbl 9559 我 我的的我"
lst = ['Cbl', 'The', '我', 'Is', 'A_cbl_我的', 'Good_225', 'cbl', '9559', '我', '我的的我']
res = str.split()
print(res)
res_sp = str.split("_", 2)
print(res_sp)
res_rsp = str.rsplit("_", 2)
print(res_rsp)
res_join = " ".join(lst)
print(str)
print(res_join)
lst_join = " ".join(['Cbl', 'The', '我', 'Is', 'A_cbl_我的', 'Good_225', 'cbl'])
print(lst_join)
"""

"""去掉与替换
str = " Cbl The 我 Is A_cbl_我的 Good_225 cbl 9559 我 我的的我 "
res = str.replace(" ", "/")
print(res)
res_str = str.strip()
print(res_str)
print(str)
res_lstr = str.lstrip()
print(res_lstr)
res_rstr = str.rstrip()
print(res_rstr)
"""

"""判断类型
"""

"""长度和填充
str = " Cbl The 我 Is A_cbl_我的_Good_225 cbl 9559 我 我的的我 "
print(len(str))
isme = str.split("_")
print(isme)

str_two = isme[1] + isme[2]
res = str_two.upper().center(11, "@")
print(res)
"""

"""编码和解码
str = " Cbl The 我 Is A_cbl_我的 Good_225 cbl 9559 我 我的的我 "

str_one = "大头的饼干"
print(max(str))
print(min(str))
print(chr(37049))

print(ord('邹'))
print(ord("刘"))

str_utf8 = str_one.encode("UTF-8")
str_gbk = str_one.encode("GBK")

print("\nUTF-8\t", str_utf8, type(str_utf8))
print("\nGBK\t", str_gbk, type(str_utf8))

print("\nUTF-8\t", str_utf8.decode('utf-8', 'strict'))

print("GBK", str_gbk.decode('gbk','strict'))
"""

##############################列表##################################
"""
# cbl = [x * 2 for x in range(5)]
# print(cbl)
# print(cbl[0:5:2])

# list1 = [10, 20, 22]
# list2 = list1*3
# print(list2)

#
# namelist = ["大头", "饼干", "tout"]
# for name in namelist:
#     print(name, end="^_^")
#
# name_temp = input("\n输入：")
# namelist.append(name_temp)
#
#
# for name in namelist:
#     print(name, end="^_^")
#
# number = [1, 2, 3]
# numbers = [4, 5, 6]
# num, numbs = [], []
# number.append(numbers)
# # print(num)
# # print(number)
# number.extend(numbers)
# print(number)

list_so = [
    [[12, 74], [45, 37]],
    [[23, 12], [78, 32]],
    [[34, 56], [56, 89]],
    [[23, 17], [56, 23]],
    [[34, 52], [65, 81]],
    [[34, 91], [89, 90]]
]
# print(list_so[2][2][0], list_so[5])

for soso in list_so:
    for so in soso:
        for s in so:
            print(s, end="%")
        print()
    print()
"""

###################练习题########################
"""一个学校，有三个办公室，现在有8位老师等待工位的分配，编写程序，完成工位的随机分配


import random
school_offices = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in names:
    num = random.randint(0, 2)
    # print(num)
    # print(name, end=",")
    school_offices[num].append(name)
i = 0
for office in school_offices:
    print(f"办公室{i + 1}的人数为：{len(office)}")
    i += 1
    for name in office:
        print(name, end="\t")
    print()
    print("-" * 17)
"""




