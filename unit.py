__author__ = 'Klyucherev A.'

import math
import random
import numpy as np


def rnd_list_float(n, a, b):
    """ создаёт список из случайных вещественных значений в диапазоне (a, b) """
    return [random.uniform(float(a), float(b)) for i in range(n)]



def calc_result136(a: list):
    """ вычисляет выражение по формуле: (2*((sum(a[i]))**2))"""
    r = 0.0
    for i in range(len(a)):
        r += a[i]
    r=2*((r)**2)
    return r


def test_calc_result():
	assert(calc_result136([4, 1]) == 50)
	assert(calc_result136([4, 1, 3]) == 128)
	assert(calc_result136([3, 5, 2]) == 200)


def count_members178(a: list):
	"""возвращает количество элементов в списке, удовлетворяющих условию ak < ((ak-1 - ak+1)/2)"""
	c = 0
	for i in range(0, len(a)):
		if a[i] % 2 == 1:
			c += 1
	return c


def test_count_members():
	assert(count_members178([4, 1]) == 1)
	assert(count_members178([1, 8, 2, 1, 6]) == 2)
	assert(count_members178([100, 2, 50, 1, 20, 2]) == 1)



def summ335(a: int):
	""" вычисляет сумму по формуле: (j-i+1)/(i+j)
	 a и b - верхние границы i и j"""
	s = 0
	for i in range(1, a+1):
		s += i ** i
	return s


def test_count_335():
	assert(summ335(10) == 10405071317)
	assert(summ335(2) == 5)
	assert(summ335(5) == 3413)



def rearrange_columns676(m: np.ndarray):
	# Размеры матрицы
	rows, cols = m.shape

	# Создание новой матрицы для перестановки столбцов
	new_matrix = np.zeros((rows, cols), dtype=int)

	# Перестановка столбцов
	for i in range(cols):
		new_matrix[:, i] = m[:, cols - i - 1]

	return new_matrix



def test_rearrange_columns():
	matrix1 = np.array([
    	[1, 2, 3],
    	[4, 5, 6], 
    	[7, 8, 9],
	])

	m1 = np.array([
    	[3, 2, 1],
    	[6, 5, 4],
    	[9, 8, 7],
	])
	new_matrix1 = rearrange_columns676(matrix1)
	assert(np.allclose(m1, new_matrix1))

	matrix2 = np.array([
    	[-5, 8, 4, 7],
    	[9, 7, -6, 82], 
	])

	m2 = np.array([
    	[7, 4, 8, -5],
    	[82, -6, 7, 9],
	])
	new_matrix2 = rearrange_columns676(matrix2)
	assert(np.allclose(m2, new_matrix2))

	matrix3 = np.array([
    	[85, 96],
    	[-9, 7], 
    	[75,-4],
    	[-96, -57],
	])

	m3 = np.array([
    	[96, 85],
    	[7, -9],
    	[-4, 75],
    	[-57, -96],
	])
	new_matrix3 = rearrange_columns676(matrix3)
	assert(np.allclose(m3, new_matrix3))