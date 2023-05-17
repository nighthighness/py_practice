# 
alist = [10, 'john']
blist = list(enumerate(alist))
print(blist)

for i in range(len(alist)):
	print('%s:%s' %(i,alist[i]))

for i,val in enumerate(alist):
	print('%s:%s' %(i,val))

btuple = (96,34,65,87,2,76,23,90,84)
b = sorted(btuple)
print(b)