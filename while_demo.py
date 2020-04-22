n = 3
while n <= 30:
    print('=========>',n)
    n += 3

n = 1
while n <= 30:
    if n%3 == 0:
        print('-------->',n)
    n+=1

n = 1
while n <= 30:
    if n %3 == 0  and n %5 == 0:
        print('--------------->',n)
    n += 1

sum = 0
i= 1
while i<= 20:
    sum += i
    i +=1
print('---->累加和为：',sum)

print('*'*30)

# for i in range(10)
#     print('*'*i)

for i in range(1,10):
    for j in range(i,10):
        # print(i,j,i*j,end=' ')
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i, j, i * j), end=' ')
    print()

i = 1
while i <= 9:
    j = 1
    while j <= i:

        print('{}*{}={}'.format(i, j, i * j), end=' ')
        j += 1
    i += 1
    print('')

i = 9
while 0<i<10:
    j = 1
    while j <= i:
        print('{}*{}={}'.format(i, j, i * j), end=' ')
        j += 1
    i -=1
    print()

