import random
num = random.randint(1,10)
counter = 0
while  counter < 5:
	answer = int(input('请输入你猜的数字：'))
	if answer > num:
		print('猜大了')
	elif answer < num:
		print('猜小了')
	else:
		print('猜对了')
		break
	counter += 1
else:
	print('the number is:',num)
