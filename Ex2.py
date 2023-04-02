# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint as rnd

min_number = int(input('Введете минимальное значение: '))
max_number = int(input('Введете максимальное значение: '))

list1 = list(rnd(1, 30) for i in range(1, rnd(1, 20)))

print(len(list1))
print()

print(list(map(int, list1)))
list2 = []
for i in range(len(list1)):
    if min_number <= list1[i] <= max_number:
        list2.append(i)
print(list2)
dict = {i: list1[i] for i in range(len(list1))}
print(dict)
