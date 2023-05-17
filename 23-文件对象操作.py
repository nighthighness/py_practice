# 打开 读写 关闭
#  创建 打开 写入
msg = 'this is fs write'
f = open('./exc-passwd.txt','w')  # 默认以 r 方式打开文本文件 如果没有创建该文件
f.write(msg)
f.close()


# 读4字节 
f2 = open('./exc-passwd.txt')
data = f2.read(4) # 文件指针移动 到 4 位置
print(data)
# 继续读取文件数据
data2 = f2.read() # 文件指针继续向前移动   移到结尾，直到没有数据
print(data2)
f2.close()

# 遍历文件数据
f3 = open('./exc-passwd.txt')
for line in f3:
	print(line,end='')
f3.close()

# 文件指针 
# f4 = open('./exc-passwd.txt')
# f4.tell()  # 查看文件指针的位置
# f4.readline(4)
# f4.tell()
# f4.seek(0,1)  # 第一个数字是偏移量，第二位数字是相对位置   0 表示开头 1 表示当前 2 表示结尾
# f4.tell()
# f4.close()
