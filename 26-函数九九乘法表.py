# 乘法表
def mtable(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print('%s*%s=%s ' % (j, i, i * j),end = '')
			# 内层循环结束 实现换行
		print()
mtable(11)