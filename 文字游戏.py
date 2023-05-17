print('你喜欢什么动画？')
print('A:海贼王  B:火影忍者  C:鬼灭之刃   D:我不喜欢动画，我喜欢玩原神')

ans = input()
if ans == 'a' or ans == 'A':
    print('那你喜欢红发香克斯吗？')
    print('A：不，我喜欢路飞  B:我不喜欢，我喜欢罗宾' )
    haizeians = input()
    if haizeians == 'a' or haizeians == 'A':
        print('好的，我们不一样')
    else:
        print('再见')
elif  ans == 'b' or ans == 'B':
    print('那你一定会喜欢鸣人')
elif  ans == 'c' or ans == 'C':
    print('我没有看过鬼灭，我跟你没有共同话题')
else:
    print('你用的是哥哥还是妹妹？ 我只喜欢叶天帝')

