__author__ = 'Klyucherev A.'

#Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:
#удовлетворяющих условию ak < ((ak-1 - ak+1)/2)

import unit

unit.test_count_members()

n = int(input("Введите количество элементов: "))
a = []

#генератор списка
a = [  int(input("Введите элемент массива (натуральное положительное число): ")) #выражение для вычисления элементов списка (ввод пользователем)
       for i in range(n) #цикл повторяет выражение
       ]

#вызов функции из модуля
result = unit.count_members178(a)
print("Количество элементов, удовлетворяющих условию: ", result)

