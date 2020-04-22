# name = '小白'
# age = 18
# gender = 'boy'
#
# print(name,age,gender)
#
# print(name,age,gender,sep='-')

# print('亲爱的xxx:\n','\t请点击链接激活用户：激活用户',end='')
#
# print('hello\python')

# print(r'hello\t python')

# message = '''
#     亲爱的赵飞用户：
#     你注册的用户还未激活，请点击下方的链接激活用户
#     请点击：激活用户
#     激活用户可以刷抖音。
# '''
# print(message)
# 格式化输出
person = 'jhon'
address = 'beijing'
phone = 123456789

print('订单的收件人是:%s,收货地址是:%s,联系方式是:%s' %(person,address,phone))

age = 18
print("年龄是: " + str(age))

# %d 将数字强制转换成整型数字，int函数

age = 18
print("年龄是: %d"% age)

salary = 8899.99
print("我的薪水是:%.2f" %salary)

movie = '大侦探皮卡丘'
ticket = 45.9
count = 35
total = ticket*count

message = '''
电影：%s
人数：%d
单价：%.0f
总票价：%.1f
'''   %(movie,count,ticket,total)
print(message)