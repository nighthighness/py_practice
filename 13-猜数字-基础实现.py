import random
num = random.randint(1,10)

while True:
	answer = int(input('输入你猜的数字...'))
	if answer == num :
		print('恭喜，你猜对了')
		break
	elif answer < num:
		print('猜小了')
	else:
		print('猜大了')

print('猜的数字是： ',num)