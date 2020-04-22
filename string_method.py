# 字符串内建函数 startswith()  endswith()

# filename = '笔记.doc'
#
# result = filename.endswith('doc')
# print(result)

# path = input('请选择文件：')
# p = path.rfind('/')
# p1 = path.rfind('\\')
# filename = path[p+1:]
# file = path[p1+1:]
# print(filename)

# result = file.endswith()

# isalpha()
# isdigit()
s = 'abdc'
result = s.isalpha()   #是否是字母
print(result)

result1 = s.isdigit()   #是否是数字
print(result1)

# sum = 0
# for i in range(3):
#     num = input('请输入数字：')
#     if num.isdigit():
#         num = int(num)
#         sum += num
# print('sum=',sum)

# sum =0
# i = 1
# while i <= 3:
#     num = input('请输入数字：')
#
#     if num.isdigit():
#         num = int(num)
#         sum += num
#         print('第{}个数字累加成功！'.format(i))
#         i += 1
#     else:
#         print('输入的不是数字！')
# print('sum=',sum)

#join(seq)   以指定字符串为分隔符，将seq中所有的元素（的字符表示）合并为一个新的字符串

new_str = '-'.join('abc')
print(new_str)

list1 = ['a','w','f','f']
result = ''.join(list1)
print(result)

#lstrip      去除字符串左侧的空格    rstrip    strip
s = '    hello world         '
ls  = s.lstrip()
print(ls+'8')

rs = s.rstrip()
print(rs+'k')

ss = s.strip()
print(ss)

## split(str="",num=string.count(str))  分割字符串


s = 'hello world hello kitty'
result = s.split(' ',2)   # 按照空格作为分隔符，分割字符串2次
print(result)

n = s.count(' ')
print('个数:',n)

