
# a = [40, 6, 45]
# print(a, id(a))
# b = a
# a.append(67)
# print("a:", a, id(a))
# print("b:", b, id(b))

# num1 = [1, 2, 5, 7]
# num2 = num1
# num1.append(9)
# print(num1, id(num1))
# print(num2, id(num2))


# num = [10, [34, 4], 12, 10]
# num2 = num.copy()

# num.append(67)
# num[0] = 8
# num[1].append(1000)
# print(num, id(num))
# print(num2, id(num2))
# print("num[1]:", id(num[1]))
# print("num2[1]", id(num2[1]))
# print("num:", num[0], id(num[0]))
# print("num2:", num[0], id(num2[0]))
# print("num:", num[0], id(num[0]))
# print("num11:", num[1][0], id(num[1][0]))
# print("num12:", num[1][1], id(num[1][1]))
# print("num2:", num[2], id(num[2]))
# print("num3:", num[3], id(num[3]))


import copy
num1 = [12, 23, [23, 56]]
num2 = copy.deepcopy(num1)
print(num1, id(num1))
print(num2, id(num2))
num1.append(67)
num1[0] = 8
num1[2].append(100)
print()
print(num1, id(num1))
print(num2, id(num2))















