# 成绩查询
isContinue = '是'
while  isContinue == '是':
	score = int(input('输入你的分数：'))
	if score == 100:
		print('恭喜！你最棒！')
	elif score >= 90:
		print('你很优秀')
	elif score >= 70:
		print('良好')
	elif score >= 60:
		print('你及格了')
	else:
		print('不及格,你要努力了')
	print('是否继续查询？')
	isContinue = input('请输入是否继续查询...')
else:
	print('查询有误！')

