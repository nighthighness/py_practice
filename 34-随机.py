# random随机数
import random
print(random.randint(0,10))
for i in range(0,5):   # 生成5个随机整数
    print(random.randint(0,10))

# list中取随机数
data = [12,32,45,76,87,98,56]
print(random.choice(data))  # 取一个随机数
# 取 5个 随机数
for i in range(0,5):
    print(random.choice(data))

# 取多个元素
more_num = 5
print(random.sample(data,more_num))

# 取一个随机人名
stu = ['张三','李四','王五','john','eric','josh','alice']
print(random.choice(stu))
# 取多个随机人名
print(random.sample(stu,more_num))

