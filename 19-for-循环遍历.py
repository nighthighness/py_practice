# for 循环  字符 列表 元组  字典
astr = 'hello'
alist = [10,20,30]
atuple = ('bob','tom','alice')
adict = {'name':'john','age':'23'}

# for 循环
for i in astr:
	print(i)

for j in alist:
	print(j)

for name in atuple:
	print(name)

for key in adict:
	print('%s: %s' % (key,adict[key]))