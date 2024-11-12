"""Задача Игра - https://habr.com/ru/companies/yandex/articles/340784/"""
import random

print('Введите значение кратное 3')
n = input()
n = int(n)

list_of_values = [x for x in range(1, 1000)]
random.shuffle(list_of_values)
list_of_values = list_of_values[0:n]

Petya_list = []
Vasya_list = []
vasya_value, peter_value = 0, 0

for ind, num in enumerate(list_of_values):
    if ind == 0:
        Petya_list.append(num)
        vasya_value = 0
        peter_value = num

    elif ind != 0 and vasya_value > peter_value:
        Petya_list.append(num)
        peter_value = num

    elif ind != 0 and vasya_value < peter_value:
        Vasya_list.append(num)
        vasya_value = num

Peter_sum = sum(Petya_list)
Vasya_sum = sum(Vasya_list)

if Peter_sum > Vasya_sum:
    print('Peter Wins')
else:
    print('Vasiliy Wins')


