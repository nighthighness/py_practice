import random
all_chioces = ['石头','剪刀','布']
computer = random.choice(all_chioces)  # 从一个列表中选取一个随机元素
print(computer)
player = input('请出拳：')
# 第一种情况
if player == '石头':
	if computer == '石头':  
		print('平局')
	elif computer == '剪刀':
		print('你赢了！')
	else:
		print('你输了!')
# 第二种情况
elif player == '剪刀':
	if computer == '剪刀':
		print('平局')
	elif computer =='石头':
		print('你输了！')
	else:
		print('你赢了！')
# 第三种情况
elif player == '布':
	if computer == '石头':
		print('你赢了！')
	elif computer == '剪刀':
		print('你输了！')
	else:
		print('平局')
else:
	print('错误，请重新出拳')