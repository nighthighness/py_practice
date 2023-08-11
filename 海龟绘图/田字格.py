import turtle as t
t.color('red')
t.pensize(5)


def four(t):
    for i in range(4):
        t.lt(90)
        t.forward(50)
        
# 第一个正方形
# four(t)

# # 第二个正方形
# t.lt(90)
# four(t)

# # 第三个正方形
# t.lt(90)
# four(t)

# # 第四个正方形
# t.lt(90)
# four(t)

# 写入循环
for i in range(4):
    four(t)
    t.lt(90)
t.done()
