# 拷贝文件
file1 = open('./exc_copy.txt','w+') # 创建需要拷贝的文件
file1.write('copy files\n')
file1.flush() # 将数据保存到磁盘
file1.writelines(['2ndline.\n'])
file1.close()  # 文件存在磁盘 并重新打开才能读取

file1 = open('./exc_copy.txt')
print(file1.read())
file1.close()


src_fname = './exc_copy.txt'   # 被拷贝的文件名称
dst_fname = './copyfilexc.txt' # 拷贝的文件名称

src_src = open(src_fname,'rb') 
dst_dst = open(dst_fname,'wb')


while True:
	data = src_src.read(4096) # 读取4字节大小
	if not data:
		break
	dst_dst.write(data) # 写入另外一个文件

src_src.close()
dst_dst.close()