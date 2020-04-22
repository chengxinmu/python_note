age = 12
s = '已经上'
message = '乔治说：我今年{}岁了,{}幼儿园！'.format(age,s)
print(message)

print('''
**********************
        捕鱼达人
**********************''')

username = input('输入参与游戏者用户名：')
password = input('输入密码:')

print('%s请充值才能加入游戏!'%username)

# coins = int(input('请充值:'))
# print('%s充值成功！当前游戏币是：%d'%(username,coins))

# coins = input('请充值：')
# print('{}充值成功！当前游戏币是:{}'.format(username,coins))

coins = input('请充值:')
coins = int(coins)
print('%s充值成功！当前游戏币是:%d'%(username,coins))