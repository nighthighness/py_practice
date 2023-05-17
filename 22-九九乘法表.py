# 九九乘法表
for i in range(1,10):
	print(i)
	for j in range(1,i+1):
		# end = '' 结束时不换行
		# print(j)
		print('%s*%s=%s ' % (j,i,i*j),end = '')  # 如何实现换行？
	# 内层循环结束实现换行	
	print()