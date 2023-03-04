import random
 
n = set(random.randint(1, 30) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n)
m = set(random.randint(1, 30) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m)
s = sorted(n.intersection(m))
print(*s)