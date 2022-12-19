str_user = input()      #输入
str_ls = list(str_user)     #将字符串变为列表
str_len = len(str_ls)     #获取列表长度
str_bls = list(str_user)    #备份列表
str_bls.reverse()           #将列表所有元素反转

if str_ls == str_bls:       #原字符串本身为回文串
    out_put = "".join(str_ls)
    print(out_put)
elif str_len % 2 == 0:
    if str_ls[1:str_len] == str_bls[0:str_len-1]:       #判断列表本身有无回文串
        out_put = "".join(str_ls + str_bls[-1:])
        print(out_put)
    else:
        out_put = "".join(str_ls + str_bls[1:])
        print(out_put)
elif str_len % 2 == 1:
    if str_ls[2:str_len] == str_bls[0:str_len-2]:       #判断列表本身有无回文串
        out_put = "".join(str_ls + str_bls[-2:])
        print(out_put)
    else:
        out_put = "".join(str_ls + str_bls[1:])
        print(out_put)