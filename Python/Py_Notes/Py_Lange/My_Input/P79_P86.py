# Author : .CseiseiG.
# -*- codeing = utf-8 -*-
# @Time : 2022/10/3 11:47
# @Author : 12542
# @File : P79_P86.py
# @Software : PyCharm


# f = open("text.txt", "w", encoding="utf-8")
# f.write("你好啊，225ccbbll哈哈哈")

# content = ["cbl的", "小木屋", "zl的大头"]

# f.write("\n".join(content))
# f.writelines(content)
# f.close()

# f = open("text.txt", "w", encoding="utf-8")
# f.write("cbl的小木屋\n"*10)
# f.close()

# f = open("text.txt", "r", encoding="utf-8")
# data = f.read(12)
# print(data)
# f.close()
#
# f = open("text.txt", "r", encoding="utf-8")
#
# while True:
#     content = f.readline()
#     if content:
#         print(f"{content}", end="")
#     else:
#         print(content, type(content))
#         break;
# f.close()


f = open("text.txt", "r+", encoding="utf-8")
f.seek(0, 2)
f.write("zl的大头")
f.close()




































































