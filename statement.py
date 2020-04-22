# age = int(input('输入你的年龄:'))
# username = input('输入你的用户名:')
#
# if age > 18 and username:
#     print('{}今年{}岁了！'.format(username,age))
# else:
#     print('你的输入有误！')
#
#
# print('---game over----')

# print('*'*10,'欢迎来到消消乐','*'*10)

import random
# print(random.randint(1,10))

ran = random.randint(1,10)
num = int(input('请输入一个1到10之间的整数：'))

if num == ran:
    print('congranlation you!')
else:
    print('the ran is:',ran)



