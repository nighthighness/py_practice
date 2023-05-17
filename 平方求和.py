# 求和
def sum(num1,num2):
    num1 = int(input('请输入第一个数字...'))
    num2 = int(input('请输入第二个数字...'))
    print('第一个数字与第二个数字的和为：',num1 + num2)
    return

sum(15,32)

# 求平方
def squrt(num):
    num = float(input('请输入一个数字...'))
    num_sqrt = num ** 0.5   #*  代表乘法  ** 代表乘方
    print(num_sqrt)
    return

squrt(4)

# 计算三角形的面积
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
 
# 计算半周长
s = (a + b + c) / 2
 
# 计算面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积为 %0.2f' %area)