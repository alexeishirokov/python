import random

n = list(random.randint(1, 10) for i in range (int(input('Кол-во кустов: '))))
print(n)
a = int(input('№ куста: '))
sum = 0
if a == 1:
    sum = n[0] + n[1] + n[-1]
elif a == len(n):
    sum = n[-2] + n[-1] + n[0]
else:
    sum = n[a-1] + n[a-2] + n[a]
print(sum, 'ягод')