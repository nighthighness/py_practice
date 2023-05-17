# 字典 键值对 key 不可以重复，value可以重复
adict = {'name' : 'bob','nickname':'bob','age' : 23}
print(len(adict))  # 2
# 获取value
print(adict['name']) # bob
print(adict.get('name'))  # bob
# 添加key
adict['email'] = 'bob@163.com' # {'email':'bob@163.com'}
# 修改value
adict['age'] = 25 
print(adict) # {'name' : 'bob','age' : 25}

# 循环输出所有的key
for i in adict.values():  # for i in adict.keys() ---- name age email
    print(i)
    
# 循环输出所有的key 和 value
for i in adict.items():
    print('所有的键值对---',i)
    

# 练习 学生信息
aperson = {'name':'王二','age':'16','addr':'北外新华','英语':'120','数学':'125','语文':'130'}
print(aperson['name'])
# 字典通过 键--值对形式体现  如果现有的字典没有 key ，则增添新项
# 字典 中已有的 key ,更改其 value

# 删除字典中的键值对 del
del aperson['addr']
print(aperson)

if 'addr'  in aperson:
    print('地址为:',aperson['addr'])
else:
    aperson['addr'] = '颍州区易景国际'

print(aperson)

