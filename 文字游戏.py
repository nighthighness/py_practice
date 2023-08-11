import time
# 定义打字机效果
def printer(text, delay=0.2): # 设置延迟
    """打字机效果""" 
    for i in text:
        print(i, end='', flush=True)
        time.sleep(delay)

# 定义变量
money = 100
wood = 10
print('目前木头',wood,'金币',money)
printer('欢迎来到小黑屋游戏\n')
printer('小黑屋极度深寒，火堆熄灭了，小黑屋很冷...\n')


dianhuo = input('请问你需要点火吗？y?是？')
if dianhuo == 'y' or dianhuo == '是':
    printer('火堆的光芒印进了茫茫的黑暗，火堆燃烧了。')
else:
    printer('你输入的格式不对，火堆熄灭了，僵尸即将来到门外，游戏结束')
printer('有一个流浪汉来到了你的窗外\n')
printer('流浪汉向你要100金币或10个木头 \n')

gliulangh = input('给流浪汉金币？A?给10个木头？B?让他滚蛋?C?')
if gliulangh == "a":
    money -= 10
    wood += 10
    printer('得到了10个木头\n')
    print('目前剩余{0}.format(wood)')
elif gliulangh == 'b':
    wood -= 10
    money += 10
    printer('得到了10金币\n')
    print('目前剩余{0}.format(money)')
elif gliulangh == 'c':
    printer('流浪汉走了 \n')
    print(money,wood)
else:
    print('输入有误')
