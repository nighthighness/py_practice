# 正方形
import turtle as t
t.color('red','blue')
t.goto(0,0)
t.pensize(5)
t.speed(10)  # 速度
t.ht()  # hideturtle 
t.begin_fill()
for j in range(20):
    for i in range(4):
        t.fd(40)
        # t.right(30)
        t.right(90)
    t.right(30)
    t.fd(10)
t.end_fill()
t.done()

# 五边形
# for i in range(5):
#     t.fd(50)
#     t.left(360/5)
# t.done()

# 六边形
# for i in range(6):
#     t.fd(100)
#     t.left(360/6)
# t.done()

# 五角星
# for i in range(6):
#     t.fd(100)
#     t.left(144)
# t.done()

# 多变形 函数
# def multiple(n):
#     t.color('yellow','red')
#     t.goto(0,0)
#     t.pensize(3)
#     t.begin_fill()  # 填充颜色
#     for i in range(n):
#         t.fd(100)
#         t.left(360/n)
#     t.end_fill()
#     t.done()
# bian = int(input('请输入多边形边数...'))
# multiple(bian)
