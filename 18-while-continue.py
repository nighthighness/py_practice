#  while  continue 练习
num1 = 10
while num1 > 0:
   num1 = num1 -1
   if num1 == 5:
      continue  # 跳出本次 不执行 继续执行下一条语句
   print('当前变量值 :', num1)
print("Good bye!")

# 100以内的偶数之和
# 定义一个变量为 总和
sum = 0
counter = 0
while  counter < 100:
	counter += 1
	if counter %2 == 1:
		continue  # 跳出本次循环 向下继续执行
	sum += counter
	print(counter)
print(sum)

# 100以内的奇数和
sum = 0
counter = 0
while  counter < 100:
	counter += 1
	if counter %2 == 0:
		continue # 跳出本次循环 向下继续执行
	sum += counter
	print(counter)
print(sum)