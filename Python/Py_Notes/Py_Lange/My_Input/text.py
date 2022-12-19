# data = input()  # 姓名 年龄 性别
# s=0
# n=0
# i=0
# while data:
#     i=i+1
#     ls=data.split()
#     s=s+int(ls[2])
#     if ls[1]=='男':
#         n=n+1
#     data = input()
# s=s/i
# print("平均年龄是{:.2f} 男性人数是{}".format(s,n))

# str = int(input("输入数字："))
# if str <= 10:
#     print("<10")
# else:
#     print(">10")

# print(f"{'商品列表':-^18}")
# products = [["iphone", 6888],
#             ["MacPro", 14800],
#             ["小米6", 2499],
#             ["Coffee", 31],
#             ["Book", 60],
#             ["Nike", 699]]
# n = 0
# for product in products:
#     print(n, " ", product[0], "   \t", product[1])
#     n += 1
#
#
# buy = []
# for i in range(0, 99):
#     num = input("您需要购买什么？")
#     if num == "p":
#         break
#     elif int(num) <= 5:
#         buy.append(products[int(num)][0])
#     else:
#         print("没有该商品。")
# print(buy)


# from turtle import *
#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


"""绘制樱花树
    # !/usr/bin/env python
    # coding=utf-8
    # 画一棵樱花树（模拟）
    # 导入 turtle 模块
    import turtle
    # 导入 random 模块，每次绘制的樱花树形状随机
    import random
    from turtle import *
    from time import sleep


    # 画樱花的躯干，传入躯干长度、画布
    # 这里面会有递归调用
    # 先画主干，然后递归画树枝，树枝越来越短，颜色会随机生成
    def draw_tree(branchLen, t):
        sleep(0.0005)
        if branchLen > 3:
            # 末端的树枝
            if 8 <= branchLen <= 12:
                # 随机生成画笔的颜色，用来画末端的树枝
                if random.randint(0, 2) == 0:
                    # 白色
                    t.color('snow')
                else:
                    # 淡珊瑚色
                    t.color('lightcoral')
                # 画笔的线条粗细
                t.pensize(branchLen / 3)
            elif branchLen < 8:
                if random.randint(0, 1) == 0:
                    t.color('snow')
                else:
                    t.color('lightcoral')  # 淡珊瑚色
                t.pensize(branchLen / 2)
            else:
                # 树干的颜色赭 (zhě) 色、粗细 6
                t.color('sienna')
                t.pensize(branchLen / 10)
            # 向前移动 branchLen 个像素
            t.forward(branchLen)
            # 随机生成右转的角度
            a = 1.5 * random.random()
            t.right(20 * a)
            # 递归画樱花树
            b = 1.5 * random.random()
            draw_tree(branchLen - 10 * b, t)
            # 左转，递归画樱花树
            t.left(40 * a)
            draw_tree(branchLen - 10 * b, t)
            # 画笔回正方向，向前移动
            t.right(20 * a)
            t.up()
            t.backward(branchLen)
            t.down()


    # 掉落的花瓣，传入个数、画布
    def draw_petal(m, t):
        # 循环绘制 m 个花瓣
        for i in range(m):
            # 生成随机的移动像素个数，a 用来控制左右的移动，b 用来控制上下的移动
            # a 大一点，b 小一点，总体可以让花瓣看起来有透视立体感
            a = 200 - 400 * random.random()
            b = 10 - 20 * random.random()
            # 以下就是到达花瓣位置
            # 提起画笔
            t.up()
            # 向前移动 b 个像素
            t.forward(b)
            # 左转 90 度角度
            t.left(90)
            # 向前移动 a 个像素
            t.forward(a)
            # 放下画笔
            t.down()
            # 淡珊瑚色，花瓣的颜色
            t.color('lightcoral')
            # 以下是绘制一个花瓣
            # 绘制一个圆
            t.circle(1)
            # 以下就是回到中心点
            # 提起画笔
            t.up()
            # 向后移动 a 个像素
            t.backward(a)
            # 右转 90 度角度
            t.right(90)
            # 向后移动 b 个像素
            t.backward(b)


    def draw_cherry():
        # 海龟绘图区域
        t = turtle.Turtle()
        # 画布
        w = turtle.Screen()
        # 设置大小，4 个参数：宽度、高度、起始值 x 轴、起始值 y 轴
        w.setup(1000, 600, 200, 100)
        # 设置背景为小麦颜色
        w.bgcolor('wheat')
        # 隐藏画笔
        t.hideturtle()
        # 获取屏幕，并追踪
        t.getscreen().tracer(5, 0)
        t.left(90)
        t.up()
        t.backward(200)
        t.down()
        # 1、画樱花的躯干
        draw_tree(60, t)
        # 2、画掉落的花瓣
        draw_petal(200, t)
        # 3、点击退出
        w.exitonclick()


    # 程序入口
    if __name__ == "__main__":
        print(' 开始绘制樱花树 & apos;')
        draw_cherry()
        print(' 结束绘制樱花树 & apos;')
        # input (' 暂停，等待输入（输入任意内容按回车键可退出）：')
"""















































































