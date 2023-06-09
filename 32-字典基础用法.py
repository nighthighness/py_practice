# 字典基础用法
adict = dict()  # {}
dict(['ab','cd'])
bdict = dict([('name','bob'),('age',25)])
{}.fromkeys(['zhangsan','lisi','wangwu'],11)

for key in bdict:
	print('%s: %s ' % (key,bdict[key]))

print("%(name)s:%(age)s" % bdict)

bdict['name'] = 'tom'
bdict['email'] = 'tom@123.com'

del bdict['email']
bdict.pop('age')
bdict.clear()