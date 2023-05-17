# 定义总和
# sum = 0
# # # 计算累加
# counter = 0
# while counter < 100:
#     if counter%3==0:  # 如果取余3 == 0 能被整除
#         sum =sum + counter
#         print(counter)
#     counter += 1
# print(sum)


# ans = int(input('你需要计算多少范围内的能被3整除的数字之和？'))
# sum = 0
# counter = 0
# while counter < ans:
#     if counter%3 == 0:
#         sum += counter
#         print(counter)
#     counter += 1
# print(sum)

# 改写为函数
def calc(num):
    counter = 0
    sum = 0
    while counter < num:
        sum += counter
        print(counter)
        counter += 1
    print(sum)

while True:
    ans = input('是否开始计算？y?n?\n')
    if ans == 'y':
        num = int(input('请输入你需要计算能被3整除的数字之和的数字大小？\n'))
        calc(num)
    else:
        print('计算结束')
        break