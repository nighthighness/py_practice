# 每一个py 模块以 py为扩展名都是一个模块
# 
hline = 'hello world'
def calc(n = 30):   # 什么意思？
	print('*' * n)

if __name__ == '__main__':
	calc()
	calc(50)