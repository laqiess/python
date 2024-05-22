__author__ = 'Klyucherev A.'

import math
import random
import unit

unit.test_calc_result()

n = int(input("Введите количество элементов массива: "))  

a = unit.rnd_list_float(n, 0, 100)


r = unit.calc_result136(a)

print(f"Результат вычислений: {r:.3f}")
