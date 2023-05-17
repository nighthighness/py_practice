import os
'''
    txt文本
'''

# 第一种方法
with open('33-文本输出.txt','w') as f1:
    f1.write('输出了文字到文件，使用上下文的形式')

# 第二种方法
f2 = open('33-文本输出2.txt','w')
print('输出文字到这里',file=f2)