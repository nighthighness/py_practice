# 生成随机列表  生成随机数字
import random
list1 = []
i = 0
while i < 5:
	num = random.randint(0,9)
	print(num)
	list1.append(num)
	i = i + 1 
print(list1)