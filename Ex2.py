# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint as rnd

min_number = int(input('Введете минимальное значение: '))
max_number = int(input('Введете максимальное значение: '))
list1 = (rnd(1, 30) for i in range(1, rnd(1, 10)))
print(list(map(int, list1)))
