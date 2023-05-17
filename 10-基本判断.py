#单个的数据也可作为判断条件。
# 任何值为0的数字、空对象都是False，任何非0数字、非空对象都是True。
#

if 3 > 0:
	print('yes')
	print('ok')

if 10 in [10, 20, 30]:
	print('ok')

num1 = 10
num2 = 20 
if num1 > num2:
	print('小于')
elif num1 < num2:
	print('大于')
else:
	print('等于')
