"""
输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符
"""

# s1 = input('请输入第一个字符串：')
# s2 = input('请输入第二个字符串：')
# s3 = ''
# # for i in '字符串' 也可以遍历
# for i in s1:
# #     print(i,end='')
#     if i not in s2:
#         s3+=i
# print(s3)
#
# for i  in s2:
#     s1 = s1.replace(i,'')
# print(s1)

# word = input('请输入单词：')
# for i in range(len(word)):
#     # if word[i].isupper():
#     #     print('i like it')
#     # else:
#     #     print('i hate it')
#     if word[i] <'A' or word[i] > 'Z':
#         print('i hate it')
#         break
#
#     else:
#         if i<len(word) -1 and word[i] == word[i+1]:
#             print('i hate it,double str')
#             break
# else:
#     print('i like it')
#

s = ''
while True:
    username = input('请输入用户名:')
    password = input('请输入密码:')
    email = input('请输邮箱:')

    name = username[0:20]
    ps = password[0:20]
    mail = email[0:20]

    msg = '{}\t{}\t{}\t\n'.format(name,ps,mail)
    msg=msg.expandtabs(7)

    s+=msg
    if name == 'q' or name == 'Q' or ps == 'q' or mail == 'q' or ps == 'Q' or mail == 'Q':
        break
print(s)

