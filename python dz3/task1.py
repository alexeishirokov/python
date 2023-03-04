import random


size_list = int(input("Введите размер списка: "))
number = int(input("Введите число списка: "))

list = [random.randint(1, 100) for _ in range(size_list)]
print(list)

i = list.count(number)

print(f"Число {number} встречается {i} раз(а)!")