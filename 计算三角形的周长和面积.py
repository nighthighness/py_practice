# trigle 周长和面积
# import math
# a = float(input('三角形的一边的边长为...'))
# b = float(input('三角形的第二边的边长为...'))
# c = float(input('三角形的第三边的边长为...'))

# # 海伦公式  area = sqrt(s*(s-a)*(s-b)*(s-c))  
# # 在一个三角形中， 任意两边之和大于第三边。三角形面积计算公式：area的开方=​s(s−a)(s−b)(s−c)，其中s=(a+b+c)/2。
# s = (a + b + c)/2 

# if s > max(a,b,c):
#     area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     p = 2 * s
#     print('面积为：{0},周长为：{1}'.format(area,p))
# else:
#     print('输入的边长有误')

# 改写为函数，循环调用
import math
def area(a,b,c):
    s = (a + b + c) / 2
    if s > max(a,b,c):
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        p = 2 * s
        print('面积为：{0},周长为：{1}'.format(area,p))
    else:
        print('输入的边长有误')

while True:
    ans = input('是否进行计算？')
    if ans == 'yes' or ans == '是':
        a = float(input('三角形的一边的边长为...'))
        b = float(input('三角形的第二边的边长为...'))
        c = float(input('三角形的第三边的边长为...'))
        area(a,b,c)
    else:
        print('运算结束')
        break