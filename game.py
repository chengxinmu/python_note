import random

print('*'*30)
print('欢迎进入澳门赌场！')
print('*'*30)

username = input('请输入顾客大名：')
money = 0
answer = input('确定进入游戏么？(y/n)?')

if answer == 'y':
    while money <2:
        n = int(input('金币不足，请充值(100元30币，充值必须为100的倍数):'))
        if n%100==0 and n >0:
            money = (n // 100)*30
    print('当前游戏币是:{},玩一局游戏扣除2个币'.format(money))
    print('进入游戏-----------')
    while True:
        t1 = random.randint(1,6)
        t2 = random.randint(1,6)

        money -= 2

        print('系统洗牌完毕，请猜大小:')
        guess = input('请输入大或者小:')

        if guess == '大' and (t1 + t2)>6  or (t1 + t2) <= 6 and guess == '小':
            print('恭喜{}！本局游戏获得奖励3个游戏币！'.format(username))
            money += 1
        else:
            print('很遗憾！本局游戏输了TT-TT')

        answer =  input('是否再来一局游戏，要扣除2游戏币？(y/n)')
        if answer != 'y' and money >2:
            break
else:
    print('good by')

