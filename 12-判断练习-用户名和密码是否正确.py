# 超出三次 锁定
counter = 0
while True:
	username = input('username:...')
	password = input('password:...')
	if counter < 3: # 超出3次 锁定
		if username == 'bob' and password == '123456':
			print('Login sucessful')
			break
		else:
			print('Login incorrect')
			counter += 1
	else:
		print('超出次数，将进行锁定')
		break