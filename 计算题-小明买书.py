# 计算题：
# 小明同学积攒了一部分压岁钱想要用来购买书籍，已知一本书的单价是23元，请根据小明压岁钱的金额，编写程序计算最多可以购买多少本书，还剩多少压岁钱。
# 要求：
# （1）程序开始运行后，提示输入压岁钱数；
# （2）程序会根据输入的数字计算最多可以购买多少本书并计算剩余的压岁钱金额；
# （3）输出结果：可以购买XX本书，剩余XX元。
# 如：输入压岁钱100，输出：可以购买4本书，剩余8元。
import math

bookprice = 20
money = int(input('请输入压岁钱...'))
rest = money % bookprice
print('能买',math.floor(money/bookprice),'本书',',买后压岁钱余额为',rest)

# def calc(money,bookprice):
#     rest = money % bookprice
#     print('能买',math.floor(money/bookprice),'本书',',买后压岁钱余额为：',rest)

# count = 0

# while True:
#     ans = input('是否开始购物？是？y?')
#     if ans == '是' or ans == 'y':
#         money = int(input('请输入压岁钱...'))
#         calc(money,bookprice)
#     else:
#         print('购物结束')
#         break

